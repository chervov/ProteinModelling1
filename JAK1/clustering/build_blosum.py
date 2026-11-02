"""EV1 as CSV, and the BLOSUM62 feature computed locally in EV1 order.

BLOSUM62 is computed here from the matrix rather than copied from jak1_features.json,
then cross-checked against it on the 21,926 shared rows. Self-substitutions get the
matrix diagonal, which is a real value (A>A = 4), so this file has no blanks.
"""
import json
import pathlib

import openpyxl
import pandas as pd
from Bio.Align import substitution_matrices

HERE = pathlib.Path(__file__).parent
B62 = substitution_matrices.load("BLOSUM62")

ws = openpyxl.load_workbook(HERE / "44321_2025_317_MOESM3_ESM.xlsx",
                            read_only=True, data_only=True)["Sheet1"]
rows = ws.iter_rows(values_only=True)
next(rows)
rec = []
for r in rows:
    if not r or not r[0]:
        continue
    vid = str(r[0])
    rec.append({"variant_id": vid, "wt": vid[0], "pos": int(vid[1:-1]),
                "alt": vid[-1], "cluster": r[1]})
df = pd.DataFrame(rec)
print(f"EV1: {len(df):,} rows")

# EV1 verbatim, just converted
df[["variant_id", "cluster"]].to_csv(HERE / "jak1_ev1_clusters.csv", index=False)
print("wrote jak1_ev1_clusters.csv (same two columns, same order as the xlsx)")

df["blosum62"] = [int(B62[w][a]) for w, a in zip(df.wt, df.alt)]
df.to_csv(HERE / "jak1_blosum62.csv", index=False)

feat = pd.DataFrame(json.load(open("sources/orianne/jak1_features.json", encoding="utf-8")))
feat["variant_id"] = feat.wt + feat.pos.astype(str) + feat.alt
m = df.merge(feat[["variant_id", "blosum62"]], on="variant_id", suffixes=("_mine", "_repo"))
bad = m[m.blosum62_mine != m.blosum62_repo]
print(f"\nwrote jak1_blosum62.csv: {len(df):,} rows, no blanks")
print(f"cross-check against jak1_features.json: {len(m):,} shared rows, "
      f"{len(bad)} disagreements")
if len(bad):
    print(bad.head(10).to_string(index=False))
print(f"\nvalue distribution:")
print(df.blosum62.value_counts().sort_index().to_string())
print(f"\nself-substitutions (diagonal): n={(df.wt == df.alt).sum():,}, "
      f"range {df.loc[df.wt == df.alt, 'blosum62'].min()}"
      f"..{df.loc[df.wt == df.alt, 'blosum62'].max()}")
print(df.head(4).to_string(index=False))
