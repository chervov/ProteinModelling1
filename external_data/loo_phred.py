"""Leave-one-out error for the raw->Phred calibration.

Agreement at the knots is guaranteed by construction, so it proves nothing. Dropping each
knot and predicting it from the other 34 gives an honest estimate of the error on a variant
that was not used to build the mapping.
"""
import json

import numpy as np
import pandas as pd
from scipy.interpolate import PchipInterpolator

cal = json.load(open("ag/jak_avi_phred_calibration.json", encoding="utf-8"))
k = pd.DataFrame(cal["knots"]).sort_values("raw").reset_index(drop=True)

errs = []
for i in range(len(k)):
    train = k.drop(index=i)
    f = PchipInterpolator(train.raw.values, train.phred.values, extrapolate=False)
    pred = f(k.raw.iloc[i])
    if np.isnan(pred):                      # the two endpoints cannot be interpolated
        continue
    errs.append({"variant": k.variant.iloc[i], "raw": k.raw.iloc[i],
                 "actual": k.phred.iloc[i], "predicted": float(pred),
                 "abs_error": abs(float(pred) - k.phred.iloc[i])})
e = pd.DataFrame(errs)
print(f"leave-one-out over {len(e)} of {len(k)} knots "
      f"(endpoints excluded - cannot interpolate)\n")
print(f"   mean   abs error {e.abs_error.mean():.3f} Phred")
print(f"   median abs error {e.abs_error.median():.3f} Phred")
print(f"   90th pct         {e.abs_error.quantile(0.9):.3f}")
print(f"   max              {e.abs_error.max():.3f}  ({e.loc[e.abs_error.idxmax(), 'variant']})")
print(f"\n   in percentile terms, a {e.abs_error.median():.2f} Phred error at Phred 24 means "
      f"{10 ** (-24 / 10) * 100:.3f}% vs {10 ** (-(24 + e.abs_error.median()) / 10) * 100:.3f}%")
print("\nworst five:")
print(e.nlargest(5, "abs_error").to_string(index=False))

cal["leave_one_out"] = {
    "n": int(len(e)), "mean_abs_error_phred": round(float(e.abs_error.mean()), 3),
    "median_abs_error_phred": round(float(e.abs_error.median()), 3),
    "p90_abs_error_phred": round(float(e.abs_error.quantile(0.9)), 3),
    "max_abs_error_phred": round(float(e.abs_error.max()), 3),
    "note": "endpoints excluded; PCHIP cannot interpolate outside the knot range",
}
open("ag/jak_avi_phred_calibration.json", "w", encoding="utf-8").write(
    json.dumps(cal, indent=2) + "\n")
print("\nrecorded in jak_avi_phred_calibration.json")
