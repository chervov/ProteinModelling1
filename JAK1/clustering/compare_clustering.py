"""Per-variant comparison of the rebuilt JAK1 clustering against the paper's Dataset EV1.

This is the measure the project was missing: not cluster sizes and marginal statistics, but
agreement variant by variant - Adjusted Rand Index and a confusion matrix - plus the
sensitivity checks that say whether any agreement is real or an artefact of the method.
"""
import itertools
import json
import pathlib

import numpy as np
import pandas as pd
from scipy.stats import mannwhitneyu

HERE = pathlib.Path(__file__).parent
R = pd.read_csv(HERE / "jak1_clustering_rebuilt.csv")
names = json.load(open(HERE / "jak1_clustering_config.json"))["features"]
SEED1 = ["S383G", "I62V", "I878V", "T138H", "S512L"]
SEED2 = ["S703I", "A634D", "C787F", "H596D", "V985I"]


def ari(a, b):
    """Adjusted Rand Index, computed from the contingency table."""
    ct = pd.crosstab(a, b).to_numpy()
    nC2 = lambda n: n * (n - 1) / 2
    sij = sum(nC2(v) for v in ct.ravel())
    si = sum(nC2(v) for v in ct.sum(axis=1))
    sj = sum(nC2(v) for v in ct.sum(axis=0))
    n = nC2(ct.sum())
    exp = si * sj / n
    return (sij - exp) / ((si + sj) / 2 - exp)


a, b = R.cluster, R.my_cluster
print(f"n = {len(R):,}\n")
print("confusion matrix  (rows: paper EV1, cols: rebuilt)")
ct = pd.crosstab(a, b, margins=True)
print(ct.to_string(), "\n")

agree = int((a == b).sum())
print(f"same label        {agree:,}  ({agree / len(R):.2%})")
print(f"Adjusted Rand     {ari(a, b):.4f}")
print(f"Cohen's kappa     "
      f"{(lambda po, pe: (po - pe) / (1 - pe))(agree / len(R), sum((a == c).mean() * (b == c).mean() for c in (1, 2))):.4f}")
print(f"\nsizes   paper {int((a == 1).sum()):,} / {int((a == 2).sum()):,}"
      f"     rebuilt {int((b == 1).sum()):,} / {int((b == 2).sum()):,}")

# ---- is the agreement more than the marginals alone would give? -----------------
rs = np.random.default_rng(0)
perm = [ (a.to_numpy() == rs.permutation(b.to_numpy())).mean() for _ in range(2000) ]
print(f"\nlabel-permutation null: mean {np.mean(perm):.4f}, "
      f"97.5th pct {np.percentile(perm, 97.5):.4f}  -> observed {agree/len(R):.4f}")

# ---- which features drive the disagreement? ------------------------------------
print("\nfeature medians by agreement (AlphaMissense / ESM-1b shown as the reference scales)")
ok = a == b
rows = []
for n_ in names:
    g, h = R.loc[ok, n_].dropna(), R.loc[~ok, n_].dropna()
    if len(g) > 30 and len(h) > 30:
        u, p = mannwhitneyu(g, h)
        rows.append((n_, g.median(), h.median(), p))
print(pd.DataFrame(rows, columns=["feature", "agree", "disagree", "p"]).to_string(index=False))

# ---- leave-one-feature-out: how much does each feature matter? -----------------
print("\nleave-one-feature-out ARI against EV1 (full set = baseline)")
M_all = R[names].to_numpy(dtype=float)
idx = {v: i for i, v in enumerate(R.variant_id)}


def run(cols):
    M = R[cols].to_numpy(dtype=float)
    rng = np.nanmax(M, axis=0) - np.nanmin(M, axis=0)
    rng[rng == 0] = 1.0
    s1 = [idx[v] for v in SEED1 if v in idx]
    s2 = [idx[v] for v in SEED2 if v in idx]
    reps = [np.nanmean(M[s1], axis=0), np.nanmean(M[s2], axis=0)]
    lab = None
    for _ in range(100):
        D = np.empty((M.shape[0], 2))
        for j, rep in enumerate(reps):
            both = ~np.isnan(M) & ~np.isnan(rep)[None, :]
            d = np.abs(M - rep[None, :]) / rng[None, :]
            den = both.sum(axis=1)
            D[:, j] = np.where(den > 0, np.nansum(np.where(both, d, 0.0), axis=1) / np.maximum(den, 1), np.nan)
        # a row with no feature in common with either representative is unassignable;
        # nanargmin raises on such a row, so mask it out rather than guarding after the fact
        dead = np.isnan(D).all(axis=1)
        new = np.full(M.shape[0], -1)
        new[~dead] = np.nanargmin(D[~dead], axis=1)
        new[s1] = 0
        new[s2] = 1
        if lab is not None and (new == lab).all():
            break
        lab = new
        reps = [np.nanmean(M[lab == c], axis=0) for c in (0, 1)]
    return pd.Series(np.where(lab < 0, np.nan, lab + 1), index=R.index)


base = ari(a, run(names))
out = [("(all 11)", base, 0.0, int((a == run(names)).sum()))]
for n_ in names:
    sub = [x for x in names if x != n_]
    l = run(sub)
    out.append((f"-{n_}", ari(a, l), ari(a, l) - base, int((a == l).sum())))
df = pd.DataFrame(out, columns=["features", "ARI", "delta", "same_label"])
print(df.to_string(index=False, float_format=lambda x: f"{x:+.4f}"))

# ---- the paper's own ambiguities, tested -----------------------------------------
print("\nsensitivity to the choices the paper does not pin down")
variants = {
    "baseline (HumVar, FoldX in, ddG clipped +/-10)": names,
    "without ddG delta (AUC 0.50, p=0.89)": [n for n in names if n != "ddg_delta"],
    "without all three ddG": [n for n in names if not n.startswith("ddg")],
    "only the 100%-coverage features": ["esm1b", "alphamissense", "ddg_closed", "ddg_open",
                                        "ddg_delta", "polyphen2", "blosum62"],
    "only the 31.3% genomic features": ["cadd", "sift", "clinpred"],
    "ESM-1b + AlphaMissense alone": ["esm1b", "alphamissense"],
    "ESM-1b alone": ["esm1b"],
}
res = []
for lab, cols in variants.items():
    l = run(cols)
    # score only where the reduced set could assign a label at all
    m = l.notna()
    res.append((lab, len(cols), ari(a[m], l[m]), (a[m] == l[m]).mean(),
                int((l == 1).sum()), int((l == 2).sum()), int((~m).sum())))
print(pd.DataFrame(res, columns=["feature set", "k", "ARI", "same", "n_c1", "n_c2", "unassigned"])
      .to_string(index=False, float_format=lambda x: f"{x:.4f}"))

R.to_csv(HERE / "jak1_clustering_rebuilt.csv", index=False)
json.dump({"n": len(R), "ari": round(ari(a, b), 4), "same_label": agree,
           "same_label_frac": round(agree / len(R), 4),
           "confusion": pd.crosstab(a, b).to_dict(),
           "sizes_paper": [int((a == 1).sum()), int((a == 2).sum())],
           "sizes_rebuilt": [int((b == 1).sum()), int((b == 2).sum())],
           "leave_one_out": {r[0]: round(r[1], 4) for r in out},
           "sensitivity": {r[0]: round(r[2], 4) for r in res},
           "seed_T138H": "absent - position 138 is Tyr in P23458, not Thr"},
          open(HERE / "jak1_clustering_comparison.json", "w"), indent=2)
print("\nwrote jak1_clustering_comparison.json")
