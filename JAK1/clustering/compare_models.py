"""HumDiv vs HumVar on all 21,926 JAK1 substitutions, and each against the EV1 clusters."""
import pathlib

import pandas as pd
from scipy import stats

HERE = pathlib.Path(__file__).parent
hv = pd.read_csv(HERE / "jak1_polyphen2_humvar.csv")
hd = pd.read_csv(HERE / "jak1_polyphen2_humdiv.csv")
m = hv.merge(hd[["variant_id", "polyphen2_humdiv_prob", "polyphen2_humdiv_pred"]],
             on="variant_id")
m = m[m.wt != m.alt].dropna(subset=["polyphen2_humvar_prob", "polyphen2_humdiv_prob"])
print(f"{len(m):,} substitutions with both models\n")

print("call distribution:")
for col, name in (("polyphen2_humdiv_pred", "HumDiv"), ("polyphen2_humvar_pred", "HumVar")):
    vc = m[col].value_counts()
    print(f"   {name}: " + "  ".join(f"{k}={v:,} ({v / len(m):.1%})" for k, v in vc.items()))

dis = (m.polyphen2_humdiv_pred != m.polyphen2_humvar_pred).sum()
print(f"\nthe two models disagree on {dis:,} of {len(m):,} ({dis / len(m):.1%})")
print(f"mean probability: HumDiv {m.polyphen2_humdiv_prob.mean():.3f}  "
      f"HumVar {m.polyphen2_humvar_prob.mean():.3f}")
print(f"Pearson {m.polyphen2_humdiv_prob.corr(m.polyphen2_humvar_prob):.4f}  "
      f"Spearman {m.polyphen2_humdiv_prob.corr(m.polyphen2_humvar_prob, method='spearman'):.4f}")

print("\nAUC against the paper's EV1 clusters (cluster 2 = the damaging one):")
lab = (m.cluster == 2).astype(int)
for col, name in (("polyphen2_humdiv_prob", "PolyPhen-2 HumDiv (100%)"),
                  ("polyphen2_humvar_prob", "PolyPhen-2 HumVar (100%)")):
    x = m[col]
    u = stats.mannwhitneyu(x[lab == 1], x[lab == 0], alternative="greater")
    auc = u.statistic / ((lab == 1).sum() * (lab == 0).sum())
    print(f"   {name:28s} n={len(m):,}  AUC {auc:.4f}  p={u.pvalue:.3g}")
print("   for reference, the repo's AUC on 31.3% coverage: PolyPhen-2 0.9425")

print("\nmedian probability by cluster:")
print(m.groupby("cluster")[["polyphen2_humdiv_prob", "polyphen2_humvar_prob"]]
        .median().to_string())
