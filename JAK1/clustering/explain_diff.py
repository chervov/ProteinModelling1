"""Why do 13% of the new PolyPhen-2 scores differ from the dbNSFP ones?

Hypothesis: PolyPhen-2 mixes sequence and structural features. Its PDB/DSSP snapshot is
dated 25-May-2021 in this run, newer than whenever dbNSFP's values were computed. If that
is the cause, variants scored with a structure should disagree more than variants scored
from the alignment alone.
"""
import pathlib

import pandas as pd

HERE = pathlib.Path(__file__).parent
rows = []
for line in (HERE / "pph2_hvar" / "pph2-full.txt").read_text(errors="replace").splitlines():
    if line.startswith("#") or not line.strip():
        continue
    f = [c.strip() for c in line.split("\t")]
    if len(f) < 30:
        continue
    rows.append({"variant_id": f"{f[2]}{f[1]}{f[3]}",
                 "prob": pd.to_numeric(f[15], errors="coerce"),
                 "based_on": f[12], "pdb_id": f[29] if f[29] not in ("?", "") else None})
new = pd.DataFrame(rows)
print(f"{len(new):,} rows; based_on: {new.based_on.value_counts().to_dict()}")
print(f"with a PDB structure: {new.pdb_id.notna().sum():,} "
      f"({new.pdb_id.notna().mean():.1%})")

ext = pd.read_csv("sources/counts/JAK1_ext.csv", low_memory=False)
ext = ext[ext.Variant.str.match(r"^[A-Z]\d+[A-Z]$", na=False)]
ext["db"] = pd.to_numeric(ext["PolyPhen-2 HVAR"], errors="coerce")
m = new.merge(ext[["Variant", "db"]], left_on="variant_id", right_on="Variant").dropna(
    subset=["prob", "db"])
m["absdiff"] = (m.prob - m.db).abs()
print(f"\n{len(m):,} shared variants with both scores")

print("\nagreement split by whether a structure was used:")
for has, grp in m.groupby(m.pdb_id.notna()):
    label = "structure used" if has else "alignment only"
    print(f"   {label:16s} n={len(grp):4d}  median |diff| {grp.absdiff.median():.4f}  "
          f"mean {grp.absdiff.mean():.4f}  >0.1: {(grp.absdiff > 0.1).mean():.1%}")

print("\nagreement split by based_on:")
for b, grp in m.groupby("based_on"):
    print(f"   {b:16s} n={len(grp):4d}  median |diff| {grp.absdiff.median():.4f}  "
          f">0.1: {(grp.absdiff > 0.1).mean():.1%}")
