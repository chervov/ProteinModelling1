"""Compare ddG computed on different structure pairs: correlations, AUCs, ensembles, verdicts.

Answers: are the new per-structure features better than, the same as, or worse than the ddG we
already have - and does averaging across structures help?
"""
import csv, json, os, sys
import numpy as np
from scipy.stats import mannwhitneyu, spearmanr, pearsonr
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GroupKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

PAIRS = "/Users/chervov/ddg_pairs"
FULL  = "/Users/chervov/ddg_overnight"
OB    = "/Users/chervov/orianne_tyk2"
MIN_N = 300          # don't report a pair with fewer results than this

def auc(y, s):
    a, b = s[y == 1], s[y == 0]
    if len(a) < 10 or len(b) < 10: return np.nan, np.nan
    u, p = mannwhitneyu(a, b, alternative="two-sided")
    return u / (len(a) * len(b)), p

def cvauc(X, y, g):
    pred = np.zeros(len(y))
    for tr, te in GroupKFold(n_splits=5).split(X, y, g):
        m = make_pipeline(SimpleImputer(strategy="median"), StandardScaler(),
                          LogisticRegression(max_iter=3000))
        m.fit(X[tr], y[tr]); pred[te] = m.predict_proba(X[te])[:, 1]
    return auc(y, pred)[0]

def fl(x):
    try: return float(x)
    except Exception: return None

def load(path):
    if not os.path.exists(path): return {}
    R = json.load(open(path)) if path.endswith(".json") else \
        [json.loads(l) for l in open(path) if l.strip()]
    return {(r["pos"], r["alt"]): r for r in R}

# ---- gather every ddG source
SRC = {}
for g in ("T_within96", "T_crossmax", "T_af3xcamp", "T_nullctrl", "J_afdb"):
    d = load(os.path.join(PAIRS, f"ddg_{g}_all.json"))
    if len(d) >= MIN_N: SRC[g] = d
SRC["T_af3full"] = load(os.path.join(FULL, "ddg_TYK2_all.json"))     # the reference pair
SRC["J_jpfull"]  = load(os.path.join(FULL, "ddg_JAK1_all.json"))
GENE = {k: ("JAK1" if k.startswith("J") else "TYK2") for k in SRC}
print(f"ddG sources loaded: " + ", ".join(f"{k}({len(v):,})" for k, v in SRC.items()))

L = []
def w(s=""): L.append(s)
w("# ddG across structure pairs: are the new features better, the same, or worse?")
w()
w(f"*Auto-generated {__import__('time').strftime('%Y-%m-%d %H:%M')} by `analyse_pairs.py`.*")
w()
w("| source | structures | n |")
w("|---|---|--:|")
NOTE = {
 "T_af3full": "matched AlphaFold 3 pair (the reference, full coverage)",
 "T_within96": "within-run 96/384 pair - the one depth where TYK2 is genuinely bi-stable",
 "T_crossmax": "template-pinned closed x deep-MSA open - maximal separation",
 "T_af3xcamp": "AF3 closed x our own deep-MSA open - cross-method",
 "T_nullctrl": "**two IDENTICAL structures** - the noise floor, measured directly",
 "J_jpfull":  "Jeanpierre open/closed (the reference, full coverage)",
 "J_afdb":    "AlphaFold DB JAK1 x Jeanpierre open - cross-source",
}
for k, v in SRC.items():
    w(f"| `{k}` | {NOTE.get(k,'')} | {len(v):,} |")
w()

# ---- TYK2 phenotype targets
rows = list(csv.DictReader(open(f"{OB}/tyk2_variants.csv")))
TK = {(int(r["pos"]), r["alt"]): r for r in rows}
gi1  = np.array([fl(r["dms_ifn1"])  for r in rows if fl(r["dms_ifn1"])  is not None])
gi100= np.array([fl(r["dms_ifn100"])for r in rows if fl(r["dms_ifn100"])is not None])
gab  = np.array([fl(r["dms_abund"]) for r in rows if fl(r["dms_abund"]) is not None])
THR = {"abund": np.percentile(gab,10), "ifn1": np.percentile(gi1,10),
       "ifn100": np.percentile(gi100,10), "gof": np.percentile(gi1,90)}
JC = json.load(open(f"{OB}/jak1_paper_clusters.json"))
JF = {(r["pos"], r["alt"]): r for r in json.load(open(f"{OB}/jak1_features.json"))}

def feats(src, keys):
    c = np.clip(np.array([src[k]["ddg_closed"] for k in keys]), -10, 10)
    o = np.clip(np.array([src[k]["ddg_open"]   for k in keys]), -10, 10)
    return c, o, o - c

def tyk2_eval(c, o, d, keys):
    out = {}
    def col(cn):
        return np.array([fl(TK[k][cn]) if k in TK and fl(TK[k][cn]) is not None else np.nan
                         for k in keys])
    ab, i1, i100, am = col("dms_abund"), col("dms_ifn1"), col("dms_ifn100"), col("alphamissense")
    for nm, v in (("closed", -c), ("open", -o), ("diff", -d)):
        r = {}
        for tn, t, thr, hi in (("abund", ab, THR["abund"], False), ("ifn1", i1, THR["ifn1"], False),
                               ("ifn100", i100, THR["ifn100"], False), ("gof", i1, THR["gof"], True)):
            m = ~np.isnan(v) & ~np.isnan(t)
            y = (t[m] >= thr).astype(int) if hi else (t[m] <= thr).astype(int)
            r[tn] = auc(y, v[m])[0]
        m = ~np.isnan(v) & ~np.isnan(i1)
        r["rho_i1"] = spearmanr(v[m], i1[m])[0]
        m = ~np.isnan(v) & ~np.isnan(am)
        r["rho_am"] = spearmanr(v[m], am[m])[0]
        out[nm] = r
    return out, am, ab, i1, i100

def jak1_eval(c, o, d, keys):
    lab = np.array([JC.get(f"{k[0]}_{k[1]}", 0) for k in keys])
    m = lab > 0
    y = (lab[m] == 2).astype(int)
    return {nm: auc(y, -v[m])[0] for nm, v in (("closed", c), ("open", o), ("diff", d))}, m, y

w("## 1. Each pair against its own benchmark")
w()
w("AUC oriented so higher = more damaging. TYK2 against the DMS; JAK1 against the paper's clusters.")
w()
w("| source | feature | abundance | IFN 1U | IFN 100U | GOF | rho vs IFN1 | rho vs AlphaMiss |")
w("|---|---|--:|--:|--:|--:|--:|--:|")
TY = {}
for k, src in SRC.items():
    if GENE[k] != "TYK2": continue
    keys = [x for x in src if x in TK]
    c, o, d = feats(src, keys)
    res, am, ab, i1, i100 = tyk2_eval(c, o, d, keys)
    TY[k] = (keys, c, o, d)
    for nm in ("closed", "open", "diff"):
        r = res[nm]
        star = "**" if nm == "diff" else ""
        w(f"| `{k}` | {star}{nm}{star} | {r['abund']:.3f} | {r['ifn1']:.3f} | {r['ifn100']:.3f} | "
          f"{r['gof']:.3f} | {r['rho_i1']:+.3f} | {r['rho_am']:+.3f} |")
w()
w("| source | feature | AUC vs the paper's JAK1 clusters |")
w("|---|---|--:|")
JK = {}
for k, src in SRC.items():
    if GENE[k] != "JAK1": continue
    keys = [x for x in src if f"{x[0]}_{x[1]}" in JC]
    c, o, d = feats(src, keys)
    JK[k] = (keys, c, o, d)
    res, _, _ = jak1_eval(c, o, d, keys)
    for nm in ("closed", "open", "diff"):
        star = "**" if nm == "diff" else ""
        w(f"| `{k}` | {star}{nm}{star} | {res[nm]:.3f} |")
w()

# ---- cross-pair correlations on shared variants
w("## 2. Do different structure pairs agree with each other?")
w()
for gene, store in (("TYK2", TY), ("JAK1", JK)):
    ks = list(store)
    if len(ks) < 2: continue
    w(f"### {gene} - Spearman on variants present in both")
    w()
    w("| | " + " | ".join(f"`{x}`" for x in ks) + " |")
    w("|---" * (len(ks) + 1) + "|")
    for a in ks:
        cells = []
        for b in ks:
            if a == b: cells.append("-"); continue
            ka, kb = store[a][0], store[b][0]
            common = sorted(set(ka) & set(kb))
            if len(common) < 100: cells.append("n/a"); continue
            ia = {k: i for i, k in enumerate(ka)}; ib = {k: i for i, k in enumerate(kb)}
            va = store[a][1][[ia[k] for k in common]]
            vb = store[b][1][[ib[k] for k in common]]
            cells.append(f"{spearmanr(va, vb)[0]:+.3f}")
        w(f"| `{a}` (closed) | " + " | ".join(cells) + " |")
    w()
    w("| | " + " | ".join(f"`{x}`" for x in ks) + " |")
    w("|---" * (len(ks) + 1) + "|")
    for a in ks:
        cells = []
        for b in ks:
            if a == b: cells.append("-"); continue
            ka, kb = store[a][0], store[b][0]
            common = sorted(set(ka) & set(kb))
            if len(common) < 100: cells.append("n/a"); continue
            ia = {k: i for i, k in enumerate(ka)}; ib = {k: i for i, k in enumerate(kb)}
            va = store[a][3][[ia[k] for k in common]]
            vb = store[b][3][[ib[k] for k in common]]
            cells.append(f"{spearmanr(va, vb)[0]:+.3f}")
        w(f"| `{a}` (**difference**) | " + " | ".join(cells) + " |")
    w()

# ---- ensembles
w("## 3. Does averaging across structures help?")
w()
for gene, store in (("TYK2", TY), ("JAK1", JK)):
    ks = list(store)
    if len(ks) < 2: continue
    common = sorted(set.intersection(*[set(store[k][0]) for k in ks]))
    if len(common) < 200: continue
    idx = {k: {x: i for i, x in enumerate(store[k][0])} for k in ks}
    ens_c = np.mean([store[k][1][[idx[k][x] for x in common]] for k in ks], axis=0)
    ens_d = np.mean([store[k][3][[idx[k][x] for x in common]] for k in ks], axis=0)
    w(f"### {gene} - ensemble over {len(ks)} pairs, {len(common):,} shared variants")
    w()
    if gene == "TYK2":
        res, am, ab, i1, i100 = tyk2_eval(ens_c, ens_c, ens_d, common)
        w("| feature | abundance | IFN 1U | IFN 100U | GOF |")
        w("|---|--:|--:|--:|--:|")
        for nm, lbl in (("closed", "**ensemble mean ddG_closed**"), ("diff", "**ensemble mean difference**")):
            r = res[nm]
            w(f"| {lbl} | {r['abund']:.3f} | {r['ifn1']:.3f} | {r['ifn100']:.3f} | {r['gof']:.3f} |")
        for k in ks:
            kk, c, o, d = store[k]
            ii = {x: i for i, x in enumerate(kk)}
            r1 = tyk2_eval(c[[ii[x] for x in common]], o[[ii[x] for x in common]],
                           d[[ii[x] for x in common]], common)[0]
            w(f"| single: `{k}` closed | {r1['closed']['abund']:.3f} | {r1['closed']['ifn1']:.3f} | "
              f"{r1['closed']['ifn100']:.3f} | {r1['closed']['gof']:.3f} |")
        amv = np.array([fl(TK[x]["alphamissense"]) if x in TK and fl(TK[x]["alphamissense"]) is not None
                        else np.nan for x in common])
        abv = np.array([fl(TK[x]["dms_abund"]) if x in TK and fl(TK[x]["dms_abund"]) is not None
                        else np.nan for x in common])
        i1v = np.array([fl(TK[x]["dms_ifn1"]) if x in TK and fl(TK[x]["dms_ifn1"]) is not None
                        else np.nan for x in common])
        g = np.array([x[0] for x in common])
        w()
        w("**Incremental value over AlphaMissense** (5-fold CV, folds grouped by position):")
        w()
        w("| model | AUC abundance | AUC IFN 1U |")
        w("|---|--:|--:|")
        for lbl, cols in (("AlphaMissense alone", [amv]),
                          ("+ ensemble ddG_closed", [amv, -ens_c]),
                          ("+ ensemble difference", [amv, -ens_d]),
                          ("+ both", [amv, -ens_c, -ens_d])):
            cells = []
            for t, thr in ((abv, THR["abund"]), (i1v, THR["ifn1"])):
                m = ~np.isnan(t) & ~np.isnan(amv)
                X = np.column_stack([x[m] for x in cols])
                cells.append(f"{cvauc(X, (t[m] <= thr).astype(int), g[m]):.3f}")
            w(f"| {lbl} | " + " | ".join(cells) + " |")
    else:
        res, m, y = jak1_eval(ens_c, ens_c, ens_d, common)
        w("| feature | AUC vs the paper's clusters |")
        w("|---|--:|")
        w(f"| **ensemble mean ddG_closed** | {res['closed']:.3f} |")
        w(f"| **ensemble mean difference** | {res['diff']:.3f} |")
    w()

out = "/Users/chervov/ddg_pairs/pair_comparison.md"
open(out, "w").write("\n".join(L) + "\n")
print(f"wrote {out} ({len('\n'.join(L))} chars)")
sys.path.insert(0, "/Users/chervov")
import collect as C
C.push([("pair_comparison.md", out)],
       "pair_comparison.md: ddG across structure pairs - correlations, ensembles, verdicts\n\n"
       "Co-Authored-By: Claude Opus 5 <noreply@anthropic.com>")
