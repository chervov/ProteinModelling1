"""Analyse whatever ddG results exist so far, cluster, and write/push a report.

Safe to run at any time: every table states its own n, and because positions are processed in
shuffled order the partial set is an unbiased random sample rather than a biased prefix.
"""
import base64, csv, json, os, sys, time
import numpy as np
from scipy.stats import mannwhitneyu, spearmanr, pearsonr
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

LOCAL = "/Users/chervov/ddg_overnight"
OB = "/Users/chervov/orianne_tyk2"
L = []
def w(s=""): L.append(s)

def auc(y, s):
    y = np.asarray(y); s = np.asarray(s)
    a = s[y == 1]; b = s[y == 0]
    if len(a) < 5 or len(b) < 5: return np.nan, np.nan
    u, p = mannwhitneyu(a, b, alternative="two-sided")
    return u / (len(a) * len(b)), p

def fl(x):
    try: return float(x)
    except Exception: return None

def load(gene):
    p = os.path.join(LOCAL, f"ddg_{gene}_all.json")
    return json.load(open(p)) if os.path.exists(p) else []

def clip(v): return np.clip(np.asarray(v, float), -10, 10)

w("# Overnight dual-state ddG: TYK2 and JAK1 at scale")
w()
w(f"Auto-generated {time.strftime('%Y-%m-%d %H:%M')} by `analyse_ddg.py`; regenerated every 30 min")
w("as results arrive. **This supersedes the 469-variant and 500-variant pilots of sections 56-59**,")
w("which were too small and, for TYK2, confined to the 4OLI interface.")
w()
w("Protocol is unchanged from section 56 (verified against the PyRosetta PagP tutorial to four")
w("decimals): FastRelax with coordinate constraints on each model, `mutate_residue` with an 8 A")
w("repack shell, the native repacked identically so neither side is favoured, and the paper's sign")
w("convention ddG = dG_WT - dG_mut, so **negative = destabilizing**. One efficiency change: the WT")
w("repack is computed once per position and reused across that position's substitutions, which is")
w("exact (the shell is identical) and ~19x cheaper.")
w()

for gene, models in [("TYK2", "the matched AlphaFold 3 pair"),
                     ("JAK1", "Jeanpierre's own open and closed models")]:
    R = load(gene)
    w(f"## {gene} - {models}")
    w()
    if len(R) < 50:
        w(f"*{len(R)} variants so far - too few to analyse; this section fills in automatically.*")
        w(); continue
    c = clip([r["ddg_closed"] for r in R]); o = clip([r["ddg_open"] for r in R])
    d = o - c
    npos = len(set(r["pos"] for r in R))
    tot = 22536 if gene == "TYK2" else 21926
    w(f"**{len(R):,} variants** at {npos:,} positions ({100*len(R)/tot:.1f}% of the {tot:,} possible).")
    w()
    w("| | ddG_closed | ddG_open | ddG_open - ddG_closed |")
    w("|---|--:|--:|--:|")
    w(f"| median | {np.median(c):+.2f} | {np.median(o):+.2f} | {np.median(d):+.2f} |")
    w(f"| SD | {c.std():.2f} | {o.std():.2f} | {d.std():.2f} |")
    raw_c = np.array([r["ddg_closed"] for r in R]); raw_o = np.array([r["ddg_open"] for r in R])
    w(f"| fraction inside [-10,10] | {np.mean(abs(raw_c)<=10):.3f} | {np.mean(abs(raw_o)<=10):.3f} | - |")
    w()
    w(f"- Pearson r(closed, open) = **{pearsonr(c,o)[0]:+.3f}**, Spearman **{spearmanr(c,o)[0]:+.3f}**")
    w(f"- the difference's SD is **{100*d.std()/c.std():.0f}%** of ddG_closed's")
    bl = os.path.join(LOCAL, f"baselines_{gene}.json")
    w()

    if gene == "TYK2":
        rows = {(int(r["pos"]), r["alt"]): r for r in csv.DictReader(open(f"{OB}/tyk2_variants.csv"))}
        keys = [(r["pos"], r["alt"]) for r in R]
        def col(cn):
            return np.array([fl(rows[k][cn]) if k in rows and fl(rows[k][cn]) is not None
                             else np.nan for k in keys])
        i1, i100, ab = col("dms_ifn1"), col("dms_ifn100"), col("dms_abund")
        allr = list(rows.values())
        g1 = np.array([fl(r["dms_ifn1"]) for r in allr if fl(r["dms_ifn1"]) is not None])
        g100 = np.array([fl(r["dms_ifn100"]) for r in allr if fl(r["dms_ifn100"]) is not None])
        TG = [("LOF, IFN-a 1 U/mL", i1 <= np.percentile(g1, 10), ~np.isnan(i1)),
              ("LOF, IFN-a 100 U/mL", i100 <= np.percentile(g100, 10), ~np.isnan(i100)),
              ("GOF, IFN-a 1 U/mL", i1 >= np.percentile(g1, 90), ~np.isnan(i1))]
        w("### Against measured phenotype (the test the paper could not run)")
        w()
        w("AUC oriented so **higher = more damaging**; targets are the global DMS deciles.")
        w()
        w("| feature | " + " | ".join(t[0] for t in TG) + " | rho vs IFN 1 U |")
        w("|---|" + "--:|" * (len(TG) + 1))
        FE = [("ddG_closed", -c), ("ddG_open", -o), ("**ddG_open - ddG_closed**", -d),
              ("AlphaMissense (ref)", col("alphamissense")), ("ESM-1b (ref)", -col("esm1b"))]
        for nm, v in FE:
            cells = []
            for _, y, msk in TG:
                m = msk & ~np.isnan(v)
                a, p = auc(y[m].astype(int), v[m])
                cells.append("n/a" if np.isnan(a) else f"{a:.3f}")
            m = ~np.isnan(v) & ~np.isnan(i1)
            cells.append(f"{spearmanr(v[m], i1[m])[0]:+.3f}")
            w(f"| {nm} | " + " | ".join(cells) + " |")
        w()
        w("### Correlation with the sequence predictors")
        w()
        w("| predictor | vs ddG_closed | vs ddG_open | vs the difference | n |")
        w("|---|--:|--:|--:|--:|")
        for nm, cn, sg in [("AlphaMissense", "alphamissense", +1), ("ESM-1b", "esm1b", -1),
                           ("REVEL", "revel", +1), ("SIFT", "sift", -1),
                           ("PolyPhen-2", "polyphen", +1), ("BLOSUM62", "blosum62", -1)]:
            v = sg * col(cn); m = ~np.isnan(v)
            if m.sum() < 30: continue
            w(f"| {nm} | {spearmanr(v[m],-c[m])[0]:+.3f} | {spearmanr(v[m],-o[m])[0]:+.3f} | "
              f"{spearmanr(v[m],-d[m])[0]:+.3f} | {int(m.sum()):,} |")
        w()
        # clustering with ddG included, scored against DMS
        w("### Clustering with ddG included, scored against the DMS")
        w()
        F = [("alphamissense", +1), ("esm1b", -1), ("revel", +1), ("polyphen", +1),
             ("sift", -1), ("blosum62", -1), ("dvol", +1), ("dhyd", +1)]
        X = np.column_stack([sg * col(cn) for cn, sg in F] + [-c, -o])
        lo, hi = np.nanmin(X, 0), np.nanmax(X, 0)
        Z = (X - lo) / np.where(hi - lo == 0, 1, hi - lo)
        Zi = np.where(np.isnan(Z), np.nanmean(Z, 0), Z)
        km = KMeans(n_clusters=2, n_init=25, random_state=0).fit(Zi)
        lab = km.labels_
        if np.nanmean(Zi[lab == 0, 0]) > np.nanmean(Zi[lab == 1, 0]): lab = 1 - lab
        cl = lab + 1
        w(f"| cluster | n | median IFN 1U | median IFN 100U | % LOF 1U | % LOF 100U | % GOF |")
        w("|---|--:|--:|--:|--:|--:|--:|")
        for k in (1, 2):
            m = (cl == k) & ~np.isnan(i1)
            w(f"| {k} | {int((cl==k).sum()):,} | {np.nanmedian(i1[m]):+.3f} | "
              f"{np.nanmedian(i100[m]):+.3f} | {100*np.mean(TG[0][1][m]):.1f} | "
              f"{100*np.mean(TG[1][1][m&~np.isnan(i100)]):.1f} | {100*np.mean(TG[2][1][m]):.1f} |")
        w()
        try:
            sil = silhouette_score(Zi[:min(5000, len(Zi))], cl[:min(5000, len(cl))])
            w(f"Silhouette **{sil:.3f}** (the paper's JAK1 clusters: 0.098).")
        except Exception: pass
        for nm, y, msk in TG:
            m = msk
            a, p = auc(y[m].astype(int), (cl[m] == 2).astype(float))
            w(f"- cluster-2 membership vs {nm}: AUC **{a:.3f}** (p={p:.2g})")
        w()
    else:
        CL = json.load(open(f"{OB}/jak1_paper_clusters.json"))
        FEJ = {(r["pos"], r["alt"]): r for r in json.load(open(f"{OB}/jak1_features.json"))}
        lab = np.array([CL.get(f"{r['pos']}_{r['alt']}", 0) for r in R])
        m = lab > 0
        w("### Against the paper's own cluster labels")
        w()
        if m.sum() > 50:
            y = (lab[m] == 2).astype(int)
            w("| feature | AUC vs their labels | p | median C1 | median C2 |")
            w("|---|--:|--:|--:|--:|")
            for nm, v in [("ddG_closed", c), ("ddG_open", o), ("**ddG_open - ddG_closed**", d)]:
                a, p = auc(y, -v[m])
                w(f"| {nm} | {a:.3f} | {p:.2g} | {np.median(v[m][y==0]):+.2f} | "
                  f"{np.median(v[m][y==1]):+.2f} |")
            w("| *paper's reported medians (ddG_closed)* | - | - | *-2.05* | *-6.36* |")
            w()
            w("### Correlation with the sequence predictors")
            w()
            w("| predictor | vs ddG_closed | vs ddG_open | vs the difference | n |")
            w("|---|--:|--:|--:|--:|")
            for nm, cn, sg in [("AlphaMissense", "alphamissense", +1), ("ESM-1b", "esm1b", -1),
                               ("ClinPred", "clinpred", +1), ("REVEL", "revel", +1),
                               ("SIFT", "sift", -1), ("PolyPhen-2", "polyphen", +1),
                               ("BLOSUM62", "blosum62", -1)]:
                v = np.array([sg * FEJ[(r["pos"], r["alt"])][cn]
                              if (r["pos"], r["alt"]) in FEJ
                              and FEJ[(r["pos"], r["alt"])][cn] is not None else np.nan
                              for r in R], dtype=float)
                mm = ~np.isnan(v)
                if mm.sum() < 30: continue
                w(f"| {nm} | {spearmanr(v[mm],-c[mm])[0]:+.3f} | {spearmanr(v[mm],-o[mm])[0]:+.3f} | "
                  f"{spearmanr(v[mm],-d[mm])[0]:+.3f} | {int(mm.sum()):,} |")
            w()
        else:
            w("*not enough labelled overlap yet*"); w()

out = os.path.join(LOCAL, "ddg_overnight.md")
open(out, "w").write("\n".join(L) + "\n")
print(f"wrote {out} ({len(''.join(L))} chars)")
sys.path.insert(0, "/Users/chervov")
import collect as C
C.push([("ddg_overnight.md", out)],
       f"ddg_overnight.md: regenerated {time.strftime('%Y-%m-%d %H:%M')}\n\n"
       "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>")
