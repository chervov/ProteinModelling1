"""How much of each dataset falls inside the calibrated raw range?

Adding an avi_phred column is only worth doing where most rows get a value. The calibration
spans raw 0.296-2.632; intronic AVI averages ~0.04, so coverage will be poor on the locus
files and good on the coding ones. Measure before writing anything.
"""
import json
import pathlib

import pandas as pd

cal = json.load(open("ag/jak_avi_phred_calibration.json", encoding="utf-8"))
lo, hi = cal["valid_raw_range"]
print(f"calibrated range: raw {lo:.4f} .. {hi:.4f}\n")

files = [("JAK1 locus", "ag/JAK1_locus_avi.csv.gz", "avi_raw"),
         ("JAK2 locus", "ag/jak2_locus_avi.csv.gz", "avi_raw"),
         ("JAK3 locus", "ag/JAK3_locus_avi.csv.gz", "avi_raw"),
         ("TYK2 locus", "ag/TYK2_locus_avi.csv.gz", "avi_raw"),
         ("JAK2 CDS (SNV)", "ag/jak2_cds_avi_snv.csv", "avi_raw"),
         ("JAK2 CDS (protein)", "ag/jak2_cds_avi_protein.csv", "avi_max")]

print(f"{'dataset':20s} {'rows':>9s} {'in range':>9s} {'share':>7s} {'below':>7s} {'above':>7s}")
print("-" * 66)
for name, path, col in files:
    d = pd.read_csv(path, usecols=[col]) if path.endswith(".csv") else pd.read_csv(path, usecols=[col])
    v = pd.to_numeric(d[col], errors="coerce").dropna()
    inr = ((v >= lo) & (v <= hi)).sum()
    print(f"{name:20s} {len(v):9,} {inr:9,} {inr / len(v):6.1%} "
          f"{(v < lo).mean():6.1%} {(v > hi).mean():6.1%}")
