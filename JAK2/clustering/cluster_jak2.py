"""JAK2 variant clustering - version 1, WITHOUT the dual-state ddG features.

Method follows the Jeanpierre/Debeaupuis appendix, as rebuilt for JAK1:
Gower distance, which handles missingness without imputation, and semi-supervised K-means
seeded from 10 labelled variants with the seeds pinned to their own cluster.

    d_ij = sum_k delta_ijk * d_ijk / sum_k delta_ijk

delta_ijk = 1 only when BOTH variants have feature k; d_ijk is the range-normalised absolute
difference. A missing value is removed from numerator and denominator rather than filled in.
Weights are not published, so all are 1.

EIGHT FEATURES, NOT ELEVEN. The paper's ddG closed, ddG open and ddG delta need a dual-state
Rosetta run on JAK2, which does not exist - hence `v1_wo_ddg_oc` in the report name. On JAK1
those three features were the weakest of the set: ddg_delta was inert (AUC 0.4966) and dropping
all three IMPROVED agreement with the paper (ARI 0.484 -> 0.492). So their absence is a real
limitation but probably a small one, and it removes the conformational axis entirely.

SEEDS. The paper names 10 JAK1 variants; JAK2 has no published equivalent, so they are derived
by an explicit rule from data no feature saw:

  Cluster 1 (tolerant)  = the 5 ClinVar benign / likely-benign variants with the HIGHEST gnomAD
                          allele frequency. All five are 2-star. This mirrors the paper's
                          "common in the general population (from gnomAD v4)".
  Cluster 2 (damaging)  = the 5 ClinVar pathogenic / likely-pathogenic variants ranked by review
                          stars, ties broken by literature attestation. This mirrors the paper's
                          "clinically reported to cause gain-of-function".

On JAK1 the seeds turned out barely to matter - 25 random 5+5 draws gave ARI 0.4833-0.4839
against 0.4836 for the published ones - so this choice orients the result (which pole is
"Cluster 1") more than it determines it. The same test is run here.

Writes jak2_clustering_v1.csv, jak2_clustering_v1_config.json.
"""
import csv
import json
import pathlib

import numpy as np
import pandas as pd

HERE = pathlib.Path(__file__).parent

#                           5 highest-AF ClinVar benign, all 2-star
SEED1 = ["R1063H", "D1096E", "C480F", "N337D", "K244R"]
#                           ClinVar pathogenic by review stars
SEED2 = ["V617F", "R867Q", "R938Q", "P1095L", "K539L"]

FEATURES = [
    ("esm1b",         "jak2_esm1b.csv",             "esm1b"),
    ("alphamissense", "jak2_alphamissense.csv",     "alphamissense"),
    ("cadd",          "jak2_cadd.csv",              "cadd"),
    ("foldx",         "jak2_foldx.csv",             "foldx"),        # stands in for MutFunc
    ("sift",          "jak2_sift.csv",              "sift"),
    ("polyphen2",     "jak2_polyphen2_humvar.csv",  "polyphen2_humvar"),
    ("blosum62",      "jak2_blosum62.csv",          "blosum62"),
    ("clinpred",      "jak2_clinpred.csv",          "clinpred"),
]
NAMES = [f[0] for f in FEATURES]


def assemble():
    base = pd.read_csv(HERE / "jak2_variant_universe.csv")
    base["wt"] = base.variant.str[0]
    base["pos"] = base.variant.str[1:-1].astype(int)
    base["alt"] = base.variant.str[-1]
    for name, fname, col in FEATURES:
        s = pd.read_csv(HERE / fname).set_index("variant")[col]
        base[name] = base.variant.map(s)
    return base


def gower(M, rng, reps):
    out = np.empty((M.shape[0], len(reps)))
    for j, rep in enumerate(reps):
        both = ~np.isnan(M) & ~np.isnan(rep)[None, :]
        diff = np.abs(M - rep[None, :]) / rng[None, :]
        num = np.nansum(np.where(both, diff, 0.0), axis=1)
        den = both.sum(axis=1)
        out[:, j] = np.where(den > 0, num / np.maximum(den, 1), np.nan)
    return out


def run(M, rng, idx, s1, s2, pin=True, maxit=100):
    reps = [np.nanmean(M[[idx[v] for v in s if v in idx]], axis=0) for s in (s1, s2)]
    labels = None
    for it in range(1, maxit + 1):
        D = gower(M, rng, reps)
        new = np.where(np.isnan(D).all(axis=1), -1, np.nanargmin(D, axis=1))
        if pin:
            for v in s1:
                if v in idx: new[idx[v]] = 0
            for v in s2:
                if v in idx: new[idx[v]] = 1
        moved = len(new) if labels is None else int((new != labels).sum())
        labels = new
        reps = [np.nanmean(M[labels == c], axis=0) for c in (0, 1)]
        if moved == 0:
            return labels, it
    return labels, maxit


def main():
    df = assemble()
    print(f"{len(df):,} substitutions, {len(NAMES)} features "
          f"(the paper's 11 minus the three dual-state ddG)")
    print("\ncoverage:")
    for n in NAMES:
        c = df[n].notna().sum()
        print(f"   {n:<14}{c:>7,}  ({100*c/len(df):5.1f}%)")
    nfeat = df[NAMES].notna().sum(axis=1)
    print(f"\nrows with all {len(NAMES)}: {(nfeat==len(NAMES)).sum():,}; "
          f"median features per row: {int(nfeat.median())}; none: {(nfeat==0).sum():,}")

    seq = (HERE / "JAK2_O60674_1132aa.txt").read_text().splitlines()[1]
    print("\nseed check against O60674:")
    for lab, seeds in (("C1 tolerant", SEED1), ("C2 damaging", SEED2)):
        for v in seeds:
            ok = seq[int(v[1:-1]) - 1] == v[0]
            print(f"   {lab:<12}{v:<8}{'sequence OK' if ok else 'MISMATCH'}, "
                  f"in data: {v in set(df.variant)}")

    M = df[NAMES].to_numpy(dtype=float)
    rng = np.nanmax(M, axis=0) - np.nanmin(M, axis=0)
    rng[rng == 0] = 1.0
    idx = {v: i for i, v in enumerate(df.variant)}

    labels, iters = run(M, rng, idx, SEED1, SEED2)
    print(f"\nconverged in {iters} iterations")
    sizes = [int((labels == c).sum()) for c in (0, 1)]
    print(f"cluster sizes: C1 {sizes[0]:,}  C2 {sizes[1]:,}  unassigned {int((labels==-1).sum())}")

    df["cluster"] = labels + 1          # 0,1 -> 1,2; nothing is unassigned
    df[["index", "variant", "wt", "pos", "alt"] + NAMES + ["cluster"]].to_csv(
        HERE / "jak2_clustering_v1.csv", index=False)
    print(f"wrote jak2_clustering_v1.csv")

    # does the seed choice matter? the JAK1 answer was "barely"
    rs = np.random.default_rng(0)
    pool1 = [v for v in df.variant[labels == 0]]
    pool2 = [v for v in df.variant[labels == 1]]
    agree = []
    for _ in range(15):
        a = list(rs.choice(pool1, 5, replace=False))
        b = list(rs.choice(pool2, 5, replace=False))
        lab2, _ = run(M, rng, idx, a, b)
        agree.append(float((lab2 == labels).mean()))
    print(f"\nseed sensitivity: 15 random 5+5 draws from the result reproduce "
          f"{min(agree):.4f}-{max(agree):.4f} of labels")

    json.dump({"version": "v1_wo_ddg_oc",
               "features": NAMES, "n": len(df),
               "seeds_cluster1_tolerant": SEED1, "seeds_cluster2_damaging": SEED2,
               "seed_rule_c1": "5 ClinVar benign/likely-benign with highest gnomAD AF (all 2-star)",
               "seed_rule_c2": "5 ClinVar pathogenic/likely-pathogenic by review stars",
               "excluded_features": ["ddg_closed", "ddg_open", "ddg_delta"],
               "excluded_reason": "no dual-state Rosetta run exists for JAK2",
               "iterations": iters, "sizes": sizes,
               "ranges": {n: float(r) for n, r in zip(NAMES, rng)},
               "seed_sensitivity_label_agreement": [round(a, 4) for a in agree]},
              open(HERE / "jak2_clustering_v1_config.json", "w"), indent=1)
    print("wrote jak2_clustering_v1_config.json")


if __name__ == "__main__":
    main()
