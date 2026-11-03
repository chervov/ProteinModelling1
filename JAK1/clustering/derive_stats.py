"""Derived statistics for the report: stratified odds ratios, ARI by subset, disagreement tables.

Runs AFTER analyse.py and ADDS to stats.json rather than replacing it. Kept separate because
analyse.py rewrites stats.json from scratch, so anything computed inline there is lost on the
next run - a trap that bit this pipeline twice during development.
"""
import collections
import json
import pathlib

import numpy as np
import pandas as pd
from scipy import stats as sps

HERE = pathlib.Path(__file__).parent
F = ["esm1b", "alphamissense", "ddg_closed", "ddg_open", "ddg_delta", "cadd",
     "foldx", "sift", "polyphen2", "blosum62", "clinpred"]
# + = more damaging. Rosetta ddG is dG_WT - dG_mut, so negative = destabilising; FoldX is opposite.
SIGN = {"esm1b": -1, "alphamissense": 1, "ddg_closed": -1, "ddg_open": -1, "ddg_delta": -1,
        "cadd": 1, "foldx": 1, "sift": -1, "polyphen2": 1, "blosum62": -1, "clinpred": 1}


def adjusted_rand(a, b):
    n = len(a)
    cell = collections.Counter(zip(a, b))
    ra, rb = collections.Counter(a), collections.Counter(b)
    comb = lambda x: x * (x - 1) / 2
    idx = sum(comb(v) for v in cell.values())
    ea, eb = sum(comb(v) for v in ra.values()), sum(comb(v) for v in rb.values())
    exp, mx = ea * eb / comb(n), (ea + eb) / 2
    return (idx - exp) / (mx - exp)


def roc_auc(score, positive):
    m = ~np.isnan(score)
    s, y = score[m], positive[m]
    if y.sum() in (0, len(y)):
        return np.nan
    r = sps.rankdata(s)
    n1 = y.sum()
    return (r[y == 1].sum() - n1 * (n1 + 1) / 2) / (n1 * (len(y) - n1))


def main():
    X, pap = np.load(HERE / "X.npy"), np.load(HERE / "pap.npy")
    reb, ing = np.load(HERE / "reb.npy"), np.load(HERE / "ing.npy")
    ncov = np.load(HERE / "ncov.npy")
    df = pd.read_csv(HERE / "jak1_clustering_rebuilt.csv")
    pos, am = df.pos.to_numpy(), X[:, F.index("alphamissense")]
    dbn = ~np.isnan(X[:, F.index("cadd")])          # the 31.3% dbNSFP-reachable subset
    S = json.load(open(HERE / "stats.json"))

    # --- AUC on matched subsets, with the effective n behind each value ---
    keys = ["all variants", "dbNSFP-defined (all 11 features)",
            "dbNSFP-missing (8 features)", "in gnomAD r4"]
    masks = [np.ones(len(pap), bool), dbn, ~dbn, ing == 1]
    S["auc_subsets"], S["auc_n"] = {}, {}
    for f in F:
        i = F.index(f)
        S["auc_subsets"][f], S["auc_n"][f] = {}, {}
        for k, m in zip(keys, masks):
            a = roc_auc(SIGN[f] * X[m, i], (pap[m] == 2).astype(int))
            S["auc_subsets"][f][k] = None if np.isnan(a) else round(float(a), 4)
            S["auc_n"][f][k] = int((~np.isnan(X[m, i])).sum())

    # --- gnomAD enrichment, pooled AND stratified by dbNSFP reachability ---
    # Pooling is confounded: gnomAD variants are almost all dbNSFP-reachable, and the
    # tolerant cluster is disproportionately so. Mantel-Haenszel removes that.
    S["gnomad_strat"] = {}
    for name, lab in (("paper", pap), ("rebuilt", reb)):
        num = den = 0
        strata = []
        for sname, m in (("dbNSFP-defined", dbn), ("dbNSFP-missing", ~dbn)):
            a = int(((lab == 1) & (ing == 1) & m).sum())
            b = int(((lab == 1) & (ing == 0) & m).sum())
            c = int(((lab == 2) & (ing == 1) & m).sum())
            d = int(((lab == 2) & (ing == 0) & m).sum())
            n = a + b + c + d
            if n:
                num += a * d / n
                den += b * c / n
            strata.append({"stratum": sname, "c1_obs": a, "c1_n": a + b,
                           "c2_obs": c, "c2_n": c + d,
                           "or": round((a * d) / (b * c), 2) if b * c else None})
        pooled, _ = sps.fisher_exact(
            [[int(((lab == 1) & (ing == 1)).sum()), int(((lab == 1) & (ing == 0)).sum())],
             [int(((lab == 2) & (ing == 1)).sum()), int(((lab == 2) & (ing == 0)).sum())]])
        a = int(((lab == 1) & (ing == 1) & dbn).sum()); b = int(((lab == 1) & (ing == 0) & dbn).sum())
        c = int(((lab == 2) & (ing == 1) & dbn).sum()); d = int(((lab == 2) & (ing == 0) & dbn).sum())
        _, pw = sps.fisher_exact([[a, b], [c, d]])
        S["gnomad_strat"][name] = {"pooled_or": round(pooled, 2),
                                   "mh_or": round(num / den if den else float("nan"), 2),
                                   "within_dbnsfp_p": float(pw), "strata": strata}
    S["gnomad_confound"] = {
        "pct_gnomad_in_dbnsfp": round(100 * dbn[ing == 1].mean(), 1),
        "pct_all_dbnsfp": round(100 * dbn.mean(), 1),
        "pct_C1_dbnsfp": round(100 * dbn[pap == 1].mean(), 1),
        "pct_C2_dbnsfp": round(100 * dbn[pap == 2].mean(), 1)}

    # --- ARI by subset. The AlphaMissense splits are CIRCULAR (it is a clustering
    #     feature); strat_external uses only variables outside the feature set.
    conf = (~np.isnan(am)) & ((am < .25) | (am >= .80))
    S["strat"] = [{"name": n, "n": int(m.sum()),
                   "agree": round(100 * (pap[m] == reb[m]).mean(), 1),
                   "ari": round(adjusted_rand(pap[m], reb[m]), 3)}
                  for n, m in [("ALL — published headline", np.ones(len(pap), bool)),
                               ("high coverage (≥10 of 11)", ncov >= 10),
                               ("confident AlphaMissense", conf),
                               ("both", (ncov >= 10) & conf),
                               ("neither", (ncov <= 8) & (~np.isnan(am)) & (am >= .25) & (am < .80))]]
    S["strat_external"] = [{"name": n, "n": int(m.sum()),
                            "agree": round(100 * (pap[m] == reb[m]).mean(), 1),
                            "ari": round(adjusted_rand(pap[m], reb[m]), 3)}
                           for n, m in [("all variants", np.ones(len(pap), bool)),
                                        ("observed in gnomAD", ing == 1),
                                        ("absent from gnomAD", ing == 0),
                                        ("high coverage (≥10 feats)", ncov >= 10),
                                        ("low coverage (≤8 feats)", ncov <= 8)]]

    # --- disagreement by coverage, and by AlphaMissense band crossed with coverage ---
    S["cov_table"] = [{"k": int(k), "n": int((ncov == k).sum()),
                       "dis": round(100 * (pap[ncov == k] != reb[ncov == k]).mean(), 1)}
                      for k in sorted(set(ncov))]
    S["band_cov"] = []
    for lo, hi, nm in [(0, .25, "confident tolerant (&lt;0.25)"),
                       (.25, .55, "intermediate-low (0.25–0.55)"),
                       (.55, .80, "intermediate-high (0.55–0.80)"),
                       (.80, 1.01, "confident damaging (≥0.80)")]:
        sel = (~np.isnan(am)) & (am >= lo) & (am < hi)
        row = {"band": nm, "n": int(sel.sum()),
               "all": round(100 * (pap[sel] != reb[sel]).mean(), 1)}
        for key, cs in (("lo", ncov <= 8), ("hi", ncov >= 10)):
            m = sel & cs
            row[key] = round(100 * (pap[m] != reb[m]).mean(), 1) if m.sum() > 30 else None
        S["band_cov"].append(row)

    # --- damaging fraction vs gnomAD observation, in windows along the protein ---
    W = 25
    c2, gn = [], []
    for a in range(1, 1155, W):
        m = (pos >= a) & (pos < a + W)
        if m.sum() < 10:
            continue
        c2.append((pap[m] == 2).mean())
        gn.append(ing[m].mean())
    r = sps.spearmanr(c2, gn)
    S["window_anticorr"] = {"rho": round(r.statistic, 3), "p": float(r.pvalue),
                            "n_windows": len(c2)}
    S["gnomad_excluded"] = {"wt_mismatch": 89, "range": "665-708", "zero_ac": 100}

    json.dump(S, open(HERE / "stats.json", "w"), indent=1)
    print(f"stats.json extended: MH OR paper {S['gnomad_strat']['paper']['mh_or']}, "
          f"rebuilt {S['gnomad_strat']['rebuilt']['mh_or']}")
    print(f"  ARI external splits: " + ", ".join(
        f"{e['name']} {e['ari']:.3f}" for e in S["strat_external"]))


if __name__ == "__main__":
    main()
