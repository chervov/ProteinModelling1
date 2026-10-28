#!/usr/bin/env python3
"""Per-protein variant-effect analysis, reproducing the JAK/Jeanpierre pipeline.

For each target: assemble a feature matrix, locate the inter-domain interface, pull ClinVar and
gnomAD, check ProteinGym membership, cluster into two groups, write a markdown report.
"""
import json, os, sys, csv, glob, math, time, urllib.request, collections, itertools
import numpy as np
from scipy.spatial import cKDTree
from scipy.stats import spearmanr, mannwhitneyu, fisher_exact

AA3 = {"Ala":"A","Arg":"R","Asn":"N","Asp":"D","Cys":"C","Gln":"Q","Glu":"E","Gly":"G","His":"H",
       "Ile":"I","Leu":"L","Lys":"K","Met":"M","Phe":"F","Pro":"P","Ser":"S","Thr":"T","Trp":"W",
       "Tyr":"Y","Val":"V","Ter":"*","Sec":"U"}
T = json.load(open("targets.json"))
PG = {}
try:
    for r in csv.DictReader(open("/Users/chervov/pg/DMS_substitutions.csv")):
        PG.setdefault(r.get("UniProt_ID",""), []).append(r)
except Exception:
    pass

def load_features(acc):
    """FoldX + ThermoMPNN/ESM-1v/AlphaMissense, keyed (pos, alt)."""
    F = {}
    p = f"feat/{acc}.foldx.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: F[(int(r["pos"]), r["alt"])] = {"wt": r["wt"], "foldx": float(r["foldx_ddg"]),
                                                 "plddt_fx": float(r["plddt"])}
            except ValueError: pass
    p = f"feat/{acc}.dbnsfp.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: k = (int(r["pos"]), r["alt"])
            except (ValueError, KeyError): continue
            d = F.setdefault(k, {"wt": r.get("wt")})
            for c in ("revel","cadd","sift","polyphen","metarnn","vest4","primateai",
                      "mutassessor","provean","gerp","esm1b","am_dbnsfp"):
                v = r.get(c)
                if v not in (None, ""):
                    try: d[c] = float(v)
                    except ValueError: pass
    p = f"feat/{acc}.tmpnn.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: k = (int(r["new_position"]), r["mutation"].strip())
            except (ValueError, KeyError): continue
            d = F.setdefault(k, {"wt": r.get("wildtype")})
            def num(c):
                try: return float(r[c])
                except (ValueError, KeyError, TypeError): return None
            d.update(tmpnn=num("ddG_pred"), esm1v=num("ESM1v_all_variants"),
                     am=num("am_pathogenicity"), am_class=r.get("am_class") or None,
                     rasa=num("exposure_rasa"), plddt=num("exposure_plddt"),
                     ss=r.get("exposure_ss") or None, disorder=num("spot_disorder"),
                     clinvar_id=(r.get("clinvar_variation_id") or "").strip() or None,
                     clinvar_sig=(r.get("clinvar_clinical_significance") or "").strip() or None)
    return F

def read_heavy(path, chain=None):
    out, ch = {}, None
    for L in open(path, errors="replace"):
        if not L.startswith("ATOM"): continue
        el = (L[76:78].strip() or L[12:16].strip()[0])
        if el == "H": continue
        c = L[21]
        if ch is None: ch = chain or c
        if c != ch: continue
        try: r = int(L[22:26])
        except ValueError: continue
        out.setdefault(r, []).append((float(L[30:38]), float(L[38:46]), float(L[46:54])))
    return out

def interface_residues(acc, e):
    """Residues of domain A within 5 A of domain B, in the most compact available structure."""
    pair = e.get("pair")
    if not pair: return None
    na, nb = pair.split("|")
    doms = e.get("domains", [])
    da = next((x for x in doms if x[0] == na), None); db = next((x for x in doms if x[0] == nb), None)
    if not (da and db): return None
    cands = []
    for root in ("/Users/chervov/cand20", "/Users/chervov/cand30"):
        cands += glob.glob(f"{root}/af/{acc}.pdb") + glob.glob(f"{root}/tpl/*{acc}*.pdb")
        cands += [p for p in glob.glob(f"{root}/tpl/*.pdb") if e["gene"] in os.path.basename(p)]
    cands += [p for p in glob.glob("/Users/chervov/mp_structs/*.pdb") if f"_{acc}_" in os.path.basename(p)]
    best = None
    for p in sorted(set(cands)):
        hv = read_heavy(p)
        ra = [r for r in range(da[1], da[2]+1) if r in hv]; rb = [r for r in range(db[1], db[2]+1) if r in hv]
        if len(ra) < 0.4*(da[2]-da[1]+1) or len(rb) < 0.4*(db[2]-db[1]+1): continue
        A = np.array([c for r in ra for c in hv[r]]); B = np.array([c for r in rb for c in hv[r]])
        ia = [r for r in ra for _ in hv[r]]; ib = [r for r in rb for _ in hv[r]]
        pr = cKDTree(A).query_ball_tree(cKDTree(B), 5.0)
        rp = {(ia[i], ib[j]) for i, js in enumerate(pr) for j in js}
        if best is None or len(rp) > best["n"]:
            best = dict(n=len(rp), file=os.path.basename(p),
                        resA=sorted({x for x, _ in rp}), resB=sorted({y for _, y in rp}),
                        dist=round(float(np.linalg.norm(A.mean(0)-B.mean(0))), 1))
    return best

def gnomad(gene):
    q = ("query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){variants(dataset:gnomad_r4)"
         "{consequence hgvsp exome{af ac an} genome{af ac an}}}}")
    body = json.dumps({"query": q, "variables": {"g": gene}}).encode()
    r = urllib.request.Request("https://gnomad.broadinstitute.org/api", data=body,
        headers={"Content-Type": "application/json", "User-Agent": "research-script"})
    out = {}
    try:
        d = json.load(urllib.request.urlopen(r, timeout=240))
        for v in (d["data"]["gene"]["variants"] or []):
            if v.get("consequence") != "missense_variant": continue
            h = v.get("hgvsp") or ""
            if not h.startswith("p."): continue
            body3 = h[2:]
            wt3, rest = body3[:3], body3[3:]
            pos = "".join(ch for ch in rest if ch.isdigit())
            alt3 = rest[len(pos):]
            if not pos or wt3 not in AA3 or alt3 not in AA3: continue
            af = (v.get("exome") or {}).get("af") or (v.get("genome") or {}).get("af")
            k = (int(pos), AA3[alt3])
            if af is not None and (k not in out or af > out[k]): out[k] = af
    except Exception as ex:
        return None, str(ex)[:80]
    return out, None

def two_clusters(X, names):
    """k-means, k=2, on z-scored features; returns labels and per-cluster means."""
    Z = (X - np.nanmean(X, 0)) / (np.nanstd(X, 0) + 1e-9)
    Z = np.nan_to_num(Z)
    rng = np.random.default_rng(0)
    C = Z[rng.choice(len(Z), 2, replace=False)]
    lab = np.zeros(len(Z), dtype=int)
    for _ in range(100):
        d = ((Z[:, None, :] - C[None, :, :])**2).sum(2)
        new = d.argmin(1)
        if (new == lab).all() and _ > 0: break
        lab = new
        for k in (0, 1):
            if (lab == k).any(): C[k] = Z[lab == k].mean(0)
    # orient so cluster 1 is the more damaging (higher mean z over damaging-oriented features)
    if Z[lab == 1].mean() < Z[lab == 0].mean(): lab = 1 - lab
    return lab, {k: {names[j]: round(float(np.nanmean(X[lab == k, j])), 3) for j in range(X.shape[1])}
                 for k in (0, 1)}

# ---------------------------------------------------------------- report writer

DAMAGING = [("am","AlphaMissense",+1),("esm1v","ESM-1v",-1),("foldx","FoldX ΔΔG",+1),
            ("tmpnn","ThermoMPNN ΔΔG",+1),("revel","REVEL",+1),("cadd","CADD phred",+1),
            ("sift","SIFT",-1),("polyphen","PolyPhen-2 HVAR",+1),("metarnn","MetaRNN",+1),
            ("vest4","VEST4",+1),("primateai","PrimateAI",+1),("mutassessor","MutationAssessor",+1),
            ("provean","PROVEAN",-1),("esm1b","ESM1b",-1),("am_dbnsfp","AlphaMissense (dbNSFP)",+1),
            ("gerp","GERP++",+1)]

def analyse(acc, e, gn):
    F = load_features(acc)
    if not F: return None
    iface = interface_residues(acc, e)
    rep = dict(acc=acc, gene=e["gene"], name=e.get("name"), length=e.get("length"),
               kind=e["kind"], pair=e.get("pair"), domains=e.get("domains", []),
               pae_dom=e.get("pae_dom"), geom=e.get("geom", []), iface=iface,
               n_variants=len(F))
    have = {k: sum(1 for v in F.values() if v.get(k) is not None) for k, _, _ in DAMAGING}
    rep["coverage"] = have
    # correlations among available features
    keys = [k for k, _, _ in DAMAGING if have.get(k, 0) > 200]
    cors = {}
    for a, b in itertools.combinations(keys, 2):
        xs = [(v[a], v[b]) for v in F.values() if v.get(a) is not None and v.get(b) is not None]
        if len(xs) > 200:
            r, _ = spearmanr([x for x, _ in xs], [y for _, y in xs])
            cors[f"{a}|{b}"] = round(float(r), 3)
    rep["cors"] = cors
    # ClinVar
    cv = collections.Counter()
    for v in F.values():
        if v.get("clinvar_sig"): cv[v["clinvar_sig"]] += 1
    rep["clinvar"] = dict(cv.most_common())
    # gnomAD
    rep["gnomad_n"] = len(gn) if gn else 0
    # interface vs non-interface test, on every feature available
    rep["iface_tests"] = {}
    if iface and iface["resA"]:
        S = set(iface["resA"]) | set(iface["resB"])
        for k, lab, sign in DAMAGING:
            inn = [v[k] for (p, a), v in F.items() if p in S and v.get(k) is not None]
            out = [v[k] for (p, a), v in F.items() if p not in S and v.get(k) is not None]
            if len(inn) > 20 and len(out) > 200:
                u = mannwhitneyu(inn, out)
                rep["iface_tests"][k] = dict(label=lab, n_in=len(inn), n_out=len(out),
                    med_in=round(float(np.median(inn)), 3), med_out=round(float(np.median(out)), 3),
                    p=float(u.pvalue))
    # two clusters
    SETS = [("rich", ["am","esm1v","foldx","tmpnn","revel","cadd","sift","polyphen","metarnn",
                       "vest4","primateai","provean"]),
            ("full", ["am","esm1v","foldx","tmpnn"])]
    for tag, CLUSTER_ON in SETS:
        keys = [k for k in CLUSTER_ON if have.get(k, 0) > 200]
        if len(keys) < 2: continue
        rows = [(kk, v) for kk, v in F.items() if all(v.get(k) is not None for k in keys)]
        if len(rows) > 200:
            X = np.array([[ (v[k] if sg > 0 else -v[k]) for k, _, sg in DAMAGING if k in keys]
                          for _, v in rows], dtype=float)
            names = [lab for k, lab, _ in DAMAGING if k in keys]
            lab, means = two_clusters(X, names)
            key = "cluster" if tag == "rich" else "cluster_full"
            rep[key] = dict(n=len(rows), names=names, tag=tag,
                            sizes=[int((lab == 0).sum()), int((lab == 1).sum())], means=means)
            # does the split agree with ClinVar and with gnomAD presence?
            pathog = np.array([1 if (v.get("clinvar_sig") or "").lower().startswith(("pathogenic","likely path"))
                               else 0 for _, v in rows])
            benign = np.array([1 if (v.get("clinvar_sig") or "").lower().startswith(("benign","likely benign"))
                               else 0 for _, v in rows])
            if pathog.sum() + benign.sum() >= 8:
                tab = [[int(((lab==1)&(pathog==1)).sum()), int(((lab==1)&(benign==1)).sum())],
                       [int(((lab==0)&(pathog==1)).sum()), int(((lab==0)&(benign==1)).sum())]]
                try: orr, pv = fisher_exact(tab)
                except Exception: orr, pv = None, None
                rep[key]["clinvar_tab"] = tab
                rep[key]["clinvar_or"] = None if orr is None else round(float(orr), 2)
                rep[key]["clinvar_p"] = None if pv is None else float(pv)
            if gn:
                ing = np.array([1 if kk in gn else 0 for kk, _ in rows])
                if ing.sum() >= 10:
                    f1 = float(ing[lab==1].mean()); f0 = float(ing[lab==0].mean())
                    rep[key]["gnomad_frac"] = [round(f0,4), round(f1,4)]
                    rep[key]["gnomad_n"] = [int(ing[lab==0].sum()), int(ing[lab==1].sum())]
            # interface enrichment per cluster
            if iface and iface["resA"]:
                S = set(iface["resA"]) | set(iface["resB"])
                inif = np.array([1 if kk[0] in S else 0 for kk, _ in rows])
                if inif.sum() >= 10:
                    rep[key]["iface_frac"] = [round(float(inif[lab==0].mean()),4),
                                                    round(float(inif[lab==1].mean()),4)]
    rep["proteingym"] = [dict(id=r["DMS_id"], n=r["DMS_total_number_mutants"],
                              sel=r.get("coarse_selection_type"), region=r.get("region_mutated"))
                         for r in PG.get((e["gene"] or "")+"_HUMAN", [])]
    return rep
