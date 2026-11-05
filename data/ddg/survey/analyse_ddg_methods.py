"""Cross-method ddG survey: coverage, correlations, the target-residue outlier problem, RSA.

Answers four questions that were previously answered only for one method or one protein:
  1. how do the ddG methods correlate with each other, and with the predictors?
  2. is the four-residue (F/P/W/Y) outlier tail specific to PyRosetta, or general?
  3. how well does RSA alone track ddG - the claim behind RSALOR?
  4. do the ddG values separate the clustering's two clusters, and the TYK2 DMS?
"""
import json, os, pathlib
import numpy as np, pandas as pd
from scipy import stats as sps

R = pathlib.Path("/Users/chervov/ProteinModelling1")
OUT = R / "data" / "ddg" / "survey"
PROT = {"JAK1": ("P23458", "JAK1/clustering", "jak1"),
        "JAK2": ("O60674", "JAK2/clustering", "jak2"),
        "JAK3": ("P52333", "JAK3/clustering", "jak3"),
        "TYK2": ("P29597", "TYK2/clustering", "tyk2")}
ROSETTA = {"JAK1": "ddg_JAK1_all.json", "JAK2": "ddg_JAK2P1_all.json",
           "JAK3": "ddg_JAK3_all.json", "TYK2": "ddg_TYK2_all.json"}

tm_all = pd.read_csv(R / "external_data" / "thermompnn_jak_src.csv", low_memory=False)
S = {"proteins": {}}

for prot, (acc, cdir, pre) in PROT.items():
    D = {}
    # --- our Rosetta dual-state ---
    rec = json.load(open(R / "data" / "ddg" / ROSETTA[prot]))
    ro = pd.DataFrame(rec)
    ro["variant"] = ro.wt + ro.pos.astype(str) + ro.alt
    D["rosetta_closed"] = ro.set_index("variant").ddg_closed
    D["rosetta_open"] = ro.set_index("variant").ddg_open
    D["rosetta_delta"] = ro.set_index("variant").delta
    # --- ThermoMPNN + RSA ---
    tm = tm_all[tm_all[[c for c in tm_all.columns if "uni" in c.lower()][0]] == acc].copy()
    tm["variant"] = tm.wildtype + tm.new_position.astype(str) + tm.mutation
    D["thermompnn"] = tm.groupby("variant").ddG_pred.mean()
    D["rsa"] = tm.groupby("variant").exposure_rasa.mean()
    # --- FoldX + the predictors from the clustering directory ---
    # JAK1's feature files predate the shared naming: they key on variant_id and the FoldX
    # file is jak1_ddg_foldx_precomputed.csv. Resolve both spellings rather than special-casing.
    CAND = {"foldx": ([f"{pre}_foldx.csv", f"{pre}_ddg_foldx_precomputed.csv"], ["foldx", "foldx_ddg"]),
            "alphamissense": ([f"{pre}_alphamissense.csv"], ["alphamissense"]),
            "polyphen2": ([f"{pre}_polyphen2_humvar.csv"], ["polyphen2_humvar", "polyphen2"]),
            "esm1b": ([f"{pre}_esm1b.csv"], ["esm1b"]),
            "cadd": ([f"{pre}_cadd.csv"], ["cadd", "cadd_phred"])}
    for name, (files, cols) in CAND.items():
        for f in files:
            p = R / cdir / f
            if not p.exists(): continue
            d = pd.read_csv(p)
            key = "variant" if "variant" in d.columns else "variant_id"
            c = next((x for x in cols if x in d.columns), None)
            if c is None: continue
            D[name] = d.set_index(key)[c]
            break
    df = pd.DataFrame(D)
    df["wt"] = [v[0] for v in df.index]
    df["alt"] = [v[-1] for v in df.index]
    df["pos"] = [int(v[1:-1]) for v in df.index]
    # One source file carries wt->wt rows (one per position, no data in any column). They are
    # not substitutions; they inflated JAK1 from 21,926 to 23,080 before this filter.
    nself = int((df.wt == df.alt).sum())
    if nself:
        print(f"  {prot}: dropping {nself} self-substitution rows")
        df = df[df.wt != df.alt]

    P = {"n": int(len(df)),
         "coverage": {k: round(100 * df[k].notna().mean(), 1) for k in D},
         "describe": {k: {s: (None if pd.isna(v) else round(float(v), 3))
                          for s, v in df[k].describe().items()} for k in D}}

    # --- 2. the target-residue outlier tail, per method ---
    # Rosetta here is dG_WT - dG_mut (negative = destabilising); FoldX/ThermoMPNN are positive.
    EXTREME = {"rosetta_closed": -10.0, "rosetta_open": -10.0,
               "foldx": 10.0, "thermompnn": 10.0}
    P["by_target_aa"] = {}
    for meth, thr in EXTREME.items():
        if meth not in df: continue
        g = {}
        for aa, sub in df.groupby("alt"):
            v = sub[meth].dropna()
            if len(v) < 20: continue
            ext = (v < thr).mean() if thr < 0 else (v > thr).mean()
            g[aa] = {"n": int(len(v)), "median": round(float(v.median()), 2),
                     "pct_extreme": round(100 * float(ext), 1)}
        P["by_target_aa"][meth] = g
    df.to_csv(OUT / f"{pre}_methods.csv")

    # --- 1. correlation matrices ---
    cols = [c for c in D if df[c].notna().sum() > 100]
    SIGN = {"rosetta_closed": -1, "rosetta_open": -1, "rosetta_delta": -1, "esm1b": -1,
            "thermompnn": 1, "foldx": 1, "alphamissense": 1, "polyphen2": 1, "cadd": 1, "rsa": -1}
    X = df[cols] * pd.Series({c: SIGN.get(c, 1) for c in cols})
    P["corr_pearson"] = {a: {b: (None if np.isnan(v) else round(float(v), 3))
                             for b, v in X.corr().loc[a].items()} for a in cols}
    P["corr_spearman"] = {a: {b: (None if np.isnan(v) else round(float(v), 3))
                              for b, v in X.corr(method="spearman").loc[a].items()} for a in cols}
    P["corr_cols"] = cols

    # --- 4. cluster separation ---
    cl = R / cdir / (f"{pre}_clustering_v2.csv" if prot == "JAK2"
                     else f"{pre}_clustering_rebuilt.csv" if prot == "JAK1"
                     else f"{pre}_clustering_v1.csv")
    if cl.exists():
        c = pd.read_csv(cl)
        key = "variant" if "variant" in c.columns else "variant_id"
        lab = c.set_index(key)["cluster"]
        df["cluster"] = lab.reindex(df.index)
        P["by_cluster"] = {}
        for k in cols:
            a = df[df.cluster == 2][k].dropna(); b = df[df.cluster == 1][k].dropna()
            if len(a) < 20 or len(b) < 20: continue
            s = SIGN.get(k, 1)
            P["by_cluster"][k] = {
                "c1_mean": round(float(b.mean()), 3), "c2_mean": round(float(a.mean()), 3),
                "c1_median": round(float(b.median()), 3), "c2_median": round(float(a.median()), 3),
                "auc": round(float(sps.mannwhitneyu(s * a, s * b).statistic / (len(a) * len(b))), 3)}
    S["proteins"][prot] = P
    print(f"{prot}: {len(df):,} variants, {len(cols)} methods")

# --- TYK2 DMS: the only experimental anchor ---
dms = pd.read_csv(R / "TYK2" / "DMS_Howard2026" / "TYK2_DMS_Howard2026_all_arms.csv")
dms = dms[dms["class"] == "missense"].copy()
dms["variant"] = dms.wt + dms.pos.astype(str) + dms.alt
t = pd.read_csv(OUT / "tyk2_methods.csv", index_col=0)
j = t.join(dms.set_index("variant")[["ifn_100U", "abundance"]])
S["tyk2_dms"] = {}
for meth in [c for c in t.columns if c not in ("wt", "alt", "pos", "cluster")]:
    for arm in ("ifn_100U", "abundance"):
        x = j[[meth, arm]].dropna()
        if len(x) < 100: continue
        S["tyk2_dms"].setdefault(meth, {})[arm] = {
            "n": int(len(x)),
            "pearson": round(float(x[meth].corr(x[arm])), 3),
            "spearman": round(float(x[meth].corr(x[arm], method="spearman")), 3)}
json.dump(S, open(OUT / "ddg_survey.json", "w"), indent=1)
print(f"\nwrote ddg_survey.json")
