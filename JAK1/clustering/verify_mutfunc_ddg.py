"""Is mutfunc's pred_ddg really the same number as ProtVar's FoldX ddG?

Checked on two variants earlier, which is not enough to rest a conclusion on. This takes a
spread of 12 - low, middling and high ddG, buried and exposed - and compares them.
One request, so the server sees a single small query.
"""
import sys

import pandas as pd

sys.path.insert(0, "mutfunc")
from fetch_mutfunc import submit, table                     # noqa: E402

fx = pd.read_csv("clustering/jak1_foldx.csv").dropna(subset=["foldx_ddg"])
fx = fx.set_index("variant_id")

# a spread across the ddG range, plus a couple of low-pLDDT ones
picks = (fx.nlargest(3, "foldx_ddg").index.tolist()
         + fx.nsmallest(3, "foldx_ddg").index.tolist()
         + fx[(fx.foldx_ddg > 0.9) & (fx.foldx_ddg < 1.3)].index[:3].tolist()
         + fx[fx.plddt < 70].index[:3].tolist())
picks = list(dict.fromkeys(picks))
print(f"checking {len(picks)} variants: {', '.join(picks)}\n")

r1 = submit("\n".join(f"P23458 {v}" for v in picks))
rv = (r1.get("response") or {}).get("variant-list", {}).get("data")
rows = (table(rv).get("response") or {}).get("variants", {}).get("rowData") or []
got = {r["variant_id"].split("/")[1]: r for r in rows if r.get("variant_id")}
print(f"mutfunc mapped {len(got)} of {len(picks)}\n")

print(f"{'variant':9s} {'pLDDT':>7s} {'ProtVar FoldX':>14s} {'mutfunc pred_ddg':>17s} {'diff':>9s}")
print("-" * 62)
diffs = []
for v in picks:
    mine = float(fx.loc[v, "foldx_ddg"])
    pl = float(fx.loc[v, "plddt"])
    if v not in got or got[v].get("pred_ddg") is None:
        print(f"{v:9s} {pl:7.1f} {mine:14.4f} {'not mapped':>17s}")
        continue
    theirs = float(got[v]["pred_ddg"])
    diffs.append(abs(theirs - mine))
    print(f"{v:9s} {pl:7.1f} {mine:14.4f} {theirs:17.4f} {theirs - mine:9.4f}")

if diffs:
    print(f"\n{len(diffs)} compared: max |difference| {max(diffs):.6f}, "
          f"mean {sum(diffs) / len(diffs):.6f}")
    print("identical to 4 decimals" if max(diffs) < 5e-4 else "NOT identical")
