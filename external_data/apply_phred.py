"""Add an avi_phred column to the JAK2 coding datasets, where the calibration covers 84-97%.

Not applied to the whole-locus files: there only 5-12% of rows fall inside the calibrated
range, because intronic AVI averages ~0.04 while the calibration starts at 0.296. A column
that is 90% blank is worse than no column; the calibration JSON is published instead so it
can be applied by anyone who needs it.
"""
import json
import pathlib

import pandas as pd
from scipy.interpolate import PchipInterpolator

OUT = pathlib.Path("ag")
cal = json.load(open(OUT / "jak_avi_phred_calibration.json", encoding="utf-8"))
k = pd.DataFrame(cal["knots"]).sort_values("raw")
pchip = PchipInterpolator(k.raw.values, k.phred.values, extrapolate=False)
lo, hi = cal["valid_raw_range"]
print(f"calibration: {len(k)} knots, raw {lo:.4f}..{hi:.4f}, "
      f"max residual {cal['max_residual_at_knots']:.4f}")

for path, col in (("jak2_cds_avi_snv.csv", "avi_raw"),
                  ("jak2_cds_avi_protein.csv", "avi_max")):
    d = pd.read_csv(OUT / path)
    v = pd.to_numeric(d[col], errors="coerce")
    d["avi_phred"] = pchip(v).round(2)                     # NaN outside the range
    # percentile of all genome-wide SNVs scoring at least this high
    d["avi_top_pct"] = (10 ** (-d.avi_phred / 10) * 100).round(4)
    n = d.avi_phred.notna().sum()
    d.to_csv(OUT / path, index=False)
    print(f"\n{path}: {n:,} of {len(d):,} ({n / len(d):.1%}) given a Phred")
    print(d.loc[d.avi_phred.notna(),
                [c for c in ('variant', 'variant_dna', 'consequence') if c in d.columns]
                + [col, "avi_phred", "avi_top_pct"]].head(5).to_string(index=False))
    known = {"V617F": 24.19, "V617I": 23.01}
    if "variant" in d.columns:
        for var, exp in known.items():
            row = d[d.variant == var]
            if len(row):
                got = row.avi_phred.iloc[0]
                print(f"   check {var}: calibrated {got:.2f} vs panel_24 {exp} "
                      f"(difference {abs(got - exp):.2f})")
