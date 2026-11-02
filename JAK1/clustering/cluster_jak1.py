"""Rebuild the Jeanpierre/Debeaupuis JAK1 clustering, and compare it with Dataset EV1.

Method, from Appendix S2.1-2.2:
  - 11 features, Gower distance, which handles missingness without imputation:
        d_ij = sum_k w_k * delta_ijk * d_ijk  /  sum_k w_k * delta_ijk
    where delta_ijk = 1 only if BOTH variants have feature k, and d_ijk is the
    range-normalised absolute difference. Weights are not stated, so all are 1.
  - semi-supervised, initialised from 10 labelled variants:
        Cluster 1 (common in gnomAD v4): S383G, I62V, I878V, T138H, S512L
        Cluster 2 (reported gain-of-function): S703I, A634D, C787F, H596D, V985I
  - the paper clips the ddG features to [-10, 10]; done here too.

Because Gower has no natural centroid, each cluster is represented by its per-feature mean
over assigned members (ignoring missing), and points are assigned to the nearer
representative by Gower distance - K-means with Gower as the metric, which is the reading
that matches "K-means ... these variants served as initial anchors".
"""
import json
import pathlib

import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).parent

SEED1 = ["S383G", "I62V", "I878V", "T138H", "S512L"]          # common -> Cluster 1
SEED2 = ["S703I", "A634D", "C787F", "H596D", "V985I"]          # GOF    -> Cluster 2

# the paper's 11 features, mapped onto the files in this directory
FEATURES = [
    ("esm1b",          "jak1_esm1b.csv",                  "esm1b"),
    ("alphamissense",  "jak1_alphamissense.csv",          "alphamissense"),
    ("ddg_closed",     "jak1_ddg_rosetta_dualstate.csv",  "ddg_closed"),
    ("ddg_open",       "jak1_ddg_rosetta_dualstate.csv",  "ddg_open"),
    ("ddg_delta",      "jak1_ddg_rosetta_dualstate.csv",  "delta"),
    ("cadd",           "jak1_cadd.csv",                   "cadd_phred"),
    ("foldx",          "jak1_ddg_foldx_precomputed.csv",  "foldx_ddg"),   # for MutFunc
    ("sift",           "jak1_sift.csv",                   "sift"),
    ("polyphen2",      "jak1_polyphen2_humvar.csv",       "polyphen2_humvar_prob"),
    ("blosum62",       "jak1_blosum62.csv",               "blosum62"),
    ("clinpred",       "jak1_clinpred.csv",               "clinpred"),
]
CLIP = {"ddg_closed": (-10, 10), "ddg_open": (-10, 10), "ddg_delta": (-10, 10)}

# ---- assemble -----------------------------------------------------------------
base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
X = base.copy()
for name, fname, col in FEATURES:
    s = pd.read_csv(HERE / fname).set_index("variant_id")[col]
    X[name] = X.variant_id.map(s)
    if name in CLIP:
        X[name] = X[name].clip(*CLIP[name])

real = X[X.wt != X.alt].reset_index(drop=True)                  # drop self-substitutions
print(f"{len(real):,} real substitutions ({len(X):,} EV1 rows - 1,154 self)")
names = [f[0] for f in FEATURES]
print("\nfeature coverage:")
for n in names:
    c = real[n].notna().sum()
    print(f"   {n:14s} {c:6,} ({c / len(real):6.1%})")
print(f"\nrows with all 11: {real[names].notna().all(axis=1).sum():,}; "
      f"with none: {real[names].isna().all(axis=1).sum():,}")

# ---- seed sanity check --------------------------------------------------------
seq = "".join(l.strip() for l in
              (HERE / "JAK1_P23458.fasta").read_text(encoding="utf-8").splitlines()[1:])
print("\nseed check against P23458:")
for lab, seeds in (("C1 common", SEED1), ("C2 GOF", SEED2)):
    for v in seeds:
        wt, pos, alt = v[0], int(v[1:-1]), v[-1]
        ok_seq = seq[pos - 1] == wt
        present = v in set(real.variant_id)
        print(f"   {lab:10s} {v:7s} sequence {'OK' if ok_seq else f'MISMATCH ({seq[pos-1]}{pos})'}"
              f"   in data: {present}")

# ---- Gower -------------------------------------------------------------------
M = real[names].to_numpy(dtype=float)
rng = np.nanmax(M, axis=0) - np.nanmin(M, axis=0)
rng[rng == 0] = 1.0
print("\nfeature ranges used for normalisation:")
for n, r in zip(names, rng):
    print(f"   {n:14s} {r:10.3f}")


def gower_to(reps):
    """Gower distance from every row to each representative vector.

    Features missing in either the row or the representative are excluded from both the
    numerator and the denominator, which is exactly the delta_ijk term in the paper.
    """
    out = np.empty((M.shape[0], len(reps)))
    for j, rep in enumerate(reps):
        both = ~np.isnan(M) & ~np.isnan(rep)[None, :]
        diff = np.abs(M - rep[None, :]) / rng[None, :]
        num = np.nansum(np.where(both, diff, 0.0), axis=1)
        den = both.sum(axis=1)
        out[:, j] = np.where(den > 0, num / np.maximum(den, 1), np.nan)
    return out


idx = {v: i for i, v in enumerate(real.variant_id)}
reps = [np.nanmean(M[[idx[v] for v in s if v in idx]], axis=0) for s in (SEED1, SEED2)]

labels = None
for it in range(1, 101):
    D = gower_to(reps)
    new = np.where(np.isnan(D).all(axis=1), -1, np.nanargmin(D, axis=1))
    # the seeds stay pinned to their own cluster: that is what "semi-supervised" means here
    for v in SEED1:
        if v in idx:
            new[idx[v]] = 0
    for v in SEED2:
        if v in idx:
            new[idx[v]] = 1
    moved = (labels is None) or int((new != labels).sum())
    labels = new
    reps = [np.nanmean(M[labels == c], axis=0) for c in (0, 1)]
    print(f"   iteration {it:3d}: moved {moved:,}" if it < 6 or moved == 0 else "", end="")
    if moved == 0:
        print(f"\nconverged after {it} iterations")
        break

real["my_cluster"] = np.where(labels < 0, np.nan, labels + 1)
real.to_csv(HERE / "jak1_clustering_rebuilt.csv", index=False)
print(f"\nunassignable (no features at all): {(labels < 0).sum():,}")
print(real.my_cluster.value_counts(dropna=False).to_string())

json.dump({"seeds_cluster1": SEED1, "seeds_cluster2": SEED2,
           "features": names, "clip": {k: list(v) for k, v in CLIP.items()},
           "ranges": dict(zip(names, rng.round(4).tolist()))},
          open(HERE / "jak1_clustering_config.json", "w"), indent=2)
print("\nwrote jak1_clustering_rebuilt.csv and jak1_clustering_config.json")
