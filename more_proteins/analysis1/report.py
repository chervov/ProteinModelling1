import json, os, sys, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pipe

def fmt_p(p):
    if p is None: return "—"
    return "<1e-300" if p == 0 else (f"{p:.2g}")

def md(r):
    g, acc = r["gene"], r["acc"]
    L = [f"# {g} — variant-effect analysis", "",
         f"*{r.get('name') or ''}* · UniProt `{acc}` · {r.get('length')} aa · "
         f"{'**reference**' if r['kind']=='reference' else r['kind']}",
         "", "*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is "
         "computed from the sources in §7, not quoted from a paper.*", ""]
    # 1 architecture
    L += ["## 1. Architecture and the domain pair", ""]
    if r["domains"]:
        L += ["| domain | range | length |", "|---|---|--:|"]
        for n, a, b in r["domains"]:
            L.append(f"| {n} | {a}–{b} | {b-a+1} |")
    else:
        L.append("No UniProt `Domain` features — nothing measurable. See the InterPro note in "
                 "`more_proteins/jak_analogue_search_proposal.md` §2.")
    L.append("")
    if r.get("pair"):
        L.append(f"**Pair analysed:** {r['pair'].replace('|',' ↔ ')}")
    pd = r.get("pae_dom") or {}
    if pd:
        L += ["", f"**AlphaFold PAE:** inter-module mean **{pd['inter']} Å**, intra-module "
              f"**{pd['intra']} Å**, **ratio {pd['ratio']}**. A ratio above ~2 means AlphaFold is "
              "confident about each domain and unsure where they sit relative to each other."]
    if r.get("geom"):
        L += ["", "### Inter-domain geometry per structure", "",
              "| structure | centroid Å | contacts | coverage |", "|---|--:|--:|---|"]
        for x in r["geom"]:
            L.append(f"| {x['source']} | {x['dist']:.1f} | {x['contacts']} | {x['cov_a']}% / {x['cov_b']}% |")
    L.append("")
    # 2 interface
    L += ["## 2. The inter-domain interface", ""]
    f = r.get("iface")
    if not f or not f["resA"]:
        L.append("**No interface found** in any available structure for this pair — so there is no "
                 "closed state to model. By the Stream B criterion of "
                 "`jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state "
                 "switch, however mobile it looks.")
    else:
        L += [f"Most compact structure: `{f['file']}`, centroid distance **{f['dist']} Å**, "
              f"**{f['n']} residue pairs** in contact within 5 Å.", "",
              f"**Domain A interface residues ({len(f['resA'])}):** `" + ", ".join(map(str, f["resA"])) + "`", "",
              f"**Domain B interface residues ({len(f['resB'])}):** `" + ", ".join(map(str, f["resB"])) + "`", ""]
        if r.get("iface_tests"):
            L += ["### Are interface variants different? (Mann–Whitney, interface vs the rest)", "",
                  "| feature | n interface | n other | median interface | median other | p |",
                  "|---|--:|--:|--:|--:|--:|"]
            for k, t in r["iface_tests"].items():
                L.append(f"| {t['label']} | {t['n_in']:,} | {t['n_out']:,} | {t['med_in']} | "
                         f"{t['med_out']} | {fmt_p(t['p'])} |")
            L.append("")
    # 3 features
    L += ["## 3. Feature coverage and independence", "",
          "| feature | variants scored |", "|---|--:|"]
    NAMES = {"am":"AlphaMissense","esm1v":"ESM-1v","foldx":"FoldX ΔΔG (ProtVar)","tmpnn":"ThermoMPNN ΔΔG"}
    for k, v in r["coverage"].items():
        L.append(f"| {NAMES.get(k,k)} | {v:,} |")
    L += ["", "*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG "
          "methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide "
          "change** — typically ~30% of all substitutions — which is the same boundary documented "
          "for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: "
          "the `++` in its field name breaks the myvariant.info field path.*", ""]
    if r.get("cors"):
        L += ["All-vs-all Spearman (signs as reported, not oriented):", "",
              "| pair | ρ |", "|---|--:|"]
        for k, v in r["cors"].items():
            a, b = k.split("|")
            L.append(f"| {NAMES.get(a,a)} vs {NAMES.get(b,b)} | {v:+.3f} |")
        L.append("")
        L.append("*Two ΔΔG methods correlating well below 1.0 is the expected result — see "
                 "`external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at "
                 "ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*")
    L.append("")
    # 4 clinical
    L += ["## 4. ClinVar and gnomAD", ""]
    cv = r.get("clinvar") or {}
    if cv:
        L += ["| ClinVar significance | n |", "|---|--:|"]
        for k, v in cv.items(): L.append(f"| {k} | {v} |")
    else:
        L.append("No ClinVar-linked variants in the Liao & Lehner table for this protein.")
    L += ["", f"**gnomAD r4 missense variants mapped:** {r.get('gnomad_n', 0):,}", ""]
    # 5 clustering
    L += ["## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)", ""]
    c = r.get("cluster")
    if not c:
        L.append("Not enough jointly-scored variants to cluster.")
    else:
        L += [f"k-means, k = 2, on z-scored features oriented so that higher = more damaging. "
              f"**n = {c['n']:,}** variants with all of {', '.join(c['names'])}.", "",
              f"| | cluster 0 (tolerant) | cluster 1 (damaging) |", "|---|--:|--:|",
              f"| size | {c['sizes'][0]:,} | {c['sizes'][1]:,} |"]
        for nm in c["names"]:
            L.append(f"| mean {nm} | {c['means']['0'][nm] if '0' in c['means'] else c['means'][0][nm]} "
                     f"| {c['means']['1'][nm] if '1' in c['means'] else c['means'][1][nm]} |")
        if c.get("gnomad_frac"):
            L.append(f"| **fraction seen in gnomAD** | **{100*c['gnomad_frac'][0]:.2f}%** "
                     f"({c['gnomad_n'][0]:,}) | **{100*c['gnomad_frac'][1]:.2f}%** ({c['gnomad_n'][1]:,}) |")
        if c.get("iface_frac"):
            L.append(f"| fraction at the interface | {100*c['iface_frac'][0]:.2f}% | {100*c['iface_frac'][1]:.2f}% |")
        L.append("")
        if c.get("gnomad_frac"):
            a, b = c["gnomad_frac"]
            if a > 0 and b >= 0:
                L.append(f"**Validation:** the damaging cluster is "
                         f"{'**depleted**' if b < a else 'enriched'} in the population — "
                         f"{100*b:.2f}% of it appears in gnomAD against {100*a:.2f}% of the tolerant "
                         f"cluster ({'a ' + format(a/b, '.1f') + '-fold difference' if b > 0 else 'none at all'}). "
                         "Purifying selection acting on the damaging cluster is the expected pattern "
                         "and is an independent check on the split.")
        if c.get("clinvar_tab"):
            t = c["clinvar_tab"]
            L += ["", f"**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): "
                  f"cluster 1 has {t[0][0]} pathogenic / {t[0][1]} benign, cluster 0 has "
                  f"{t[1][0]} / {t[1][1]}; OR = {c.get('clinvar_or')}, p = {fmt_p(c.get('clinvar_p'))}."]
    L.append("")
    cf = r.get("cluster_full")
    if cf:
        L += ["", "### The same split on all variants, using only the four full-coverage features", "",
              f"The table above uses {len((r.get('cluster') or {}).get('names',[]))} features and is "
              f"therefore restricted to variants dbNSFP scores — i.e. those reachable by a single "
              f"nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG "
              f"and ThermoMPNN ΔΔG**, which score every substitution, gives **n = {cf['n']:,}**:", "",
              "| | cluster 0 (tolerant) | cluster 1 (damaging) |", "|---|--:|--:|",
              f"| size | {cf['sizes'][0]:,} | {cf['sizes'][1]:,} |"]
        for nm in cf["names"]:
            m0 = cf["means"]["0"] if "0" in cf["means"] else cf["means"][0]
            m1 = cf["means"]["1"] if "1" in cf["means"] else cf["means"][1]
            L.append(f"| mean {nm} | {m0[nm]} | {m1[nm]} |")
        if cf.get("gnomad_frac"):
            a, b = cf["gnomad_frac"]
            L.append(f"| **fraction seen in gnomAD** | **{100*a:.2f}%** ({cf['gnomad_n'][0]:,}) "
                     f"| **{100*b:.2f}%** ({cf['gnomad_n'][1]:,}) |")
            if b > 0:
                L += ["", f"Depletion **{a/b:.1f}×**. The two splits should be read together: the "
                      "12-feature one uses richer evidence on a third of the variants, the 4-feature "
                      "one uses weaker evidence on all of them."]
        if cf.get("iface_frac"):
            L.append(f"| fraction at the interface | {100*cf['iface_frac'][0]:.2f}% | {100*cf['iface_frac'][1]:.2f}% |")
    L.append("")
    # 6 proteingym
    L += ["## 6. ProteinGym", ""]
    pg = r.get("proteingym") or []
    if pg:
        L += ["**Present**, so published experimental data and precomputed baseline scores exist:", "",
              "| DMS_id | mutants | selection | region |", "|---|--:|---|---|"]
        for x in pg:
            L.append(f"| `{x['id']}` | {int(x['n']):,} | {x.get('sel') or '—'} | {x.get('region') or '—'} |")
        L += ["", "Fold definitions (`fold_random_5`, `fold_modulo_5`, `fold_contiguous_5`) ship with "
              "the benchmark; `fold_modulo_5` is the by-position split and the honest one. See "
              "`external_data/ddg_study.md` §8 and the ProteinGym notes in `external_data/ddg_docs_review.md`."]
    else:
        L.append("**Absent** from the 217 ProteinGym DMS substitution assays, so no published "
                 "experimental variant data and no precomputed baselines for this protein.")
    L.append("")
    # 7 sources
    L += ["## 7. Sources", "",
          "| value | source |", "|---|---|",
          "| FoldX ΔΔG, pLDDT | EBI ProtVar, FoldX v5 on AlphaFold2, 208,792,558 rows "
          "(`external_data/protvar_foldx_jak_src.csv` for the JAKs) |",
          "| ThermoMPNN ΔΔG, ESM-1v, AlphaMissense, RASA, pLDDT, secondary structure, disorder, "
          "ClinVar | Liao & Lehner 2026, Zenodo 18386427 |",
          "| gnomAD allele frequencies | gnomAD r4 GraphQL API, missense with HGVS protein notation |",
          "| domain boundaries | UniProt |",
          "| structures | AlphaFold DB v6, SWISS-MODEL Repository, RCSB PDB, ModelArchive |",
          "| interface contacts | `more_proteins/interface.py` (heavy atoms within 5 Å) |",
          "| ProteinGym membership | `reference_files/DMS_substitutions.csv`, 217 assays |", "",
          "### Caveats carried from the method work", "",
          "- **ΔΔG magnitudes are unreliable**; ranks are usable. FoldX and ThermoMPNN disagree by "
          "a factor of ~40 on the equilibrium shift for a single variant "
          "(`PTPN2/jeanpierre2024_variant_analysis.md` §2.1b).",
          "- **ΔΔG is a mechanism channel, not a pathogenicity score** — ρ ≈ 0.26–0.28 against DMS "
          "data against ≈ 0.35–0.40 for sequence predictors (`external_data/ddg_study.md` §5).",
          "- **A ΔΔG near zero with AlphaMissense near 1 identifies a functional-site variant** with "
          "no structural cost — the PTPN2 C216S pattern.",
          "- **Interface residues come from the most compact structure available.** Where that is an "
          "AlphaFold model rather than an experiment, the interface is predicted, not observed.", ""]
    return "\n".join(L)
