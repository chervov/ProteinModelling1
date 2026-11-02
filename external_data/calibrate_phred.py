"""Build an auditable raw-AVI -> AVI-Phred calibration and save it.

The Atlas API returns only the raw AVI score; Phred (-10*log10(tail quantile)) is not an
available scorer. Two sets of paired (raw, Phred) points exist in this project:

  1. JAK2/variant_panel_24/alphagenome_avi_raw_output.md - 24 variants, both columns
  2. JAK2/variant_panel_24/JAK2_benign_AVI_background.csv - 12 variants with Phred;
     their raw scores are fetched here from the Atlas

A quadratic fit on set 2 alone (what I did first) is unusable: its leading coefficient is
negative, so it turns over at raw ~1.1 and would *decrease* for the higher scores that make
up much of the data. Phred is monotone in raw by construction, so the fit must be too.
PCHIP interpolation over the combined knots is exact at the knots and monotone between them.
"""
import json
import pathlib
import re

import numpy as np
import pandas as pd
from alphagenome.atlas import atlas
from alphagenome.data import genome
from scipy.interpolate import PchipInterpolator

OUT = pathlib.Path("ag")
client = atlas.create(pathlib.Path("alphagenome_token.txt").read_text("utf-8").strip())

# ---- set 1: the 24-variant panel, which already has both columns ------------
text = pathlib.Path("sources/ag/avi_raw.md").read_text(encoding="utf-8", errors="replace")
pairs = []
for m in re.finditer(r"`(chr\d+:\d+:[ACGT]>[ACGT])`\s*\|\s*\*\*([\d.]+)\*\*\s*\|\s*([\d.]+)", text):
    pairs.append({"variant": m.group(1), "phred": float(m.group(2)),
                  "raw": float(m.group(3)), "source": "panel_24"})
print(f"set 1 (panel_24 table): {len(pairs)} paired points")

# ---- set 2: the benign background, raw scores fetched from the Atlas --------
ben = pd.read_csv("sources/ag/benign.csv")
for r in ben.itertuples():
    c, p, change = r.GRCh38_variant.split(":")
    ref, alt = change.split(">")
    v = genome.Variant(chromosome=c, position=int(p),
                       reference_bases=ref, alternate_bases=alt)
    raw = float(client.query_variant(variant=v,
                                     requested_scorers=["AVI_SCORE"])["AVI_SCORE"].X[0, 0])
    pairs.append({"variant": r.GRCh38_variant, "phred": float(r.AVI_Phred),
                  "raw": raw, "source": "benign_background"})
print(f"set 2 (benign background): {len(ben)} points fetched")

df = pd.DataFrame(pairs).drop_duplicates("variant").sort_values("raw").reset_index(drop=True)
print(f"\ncombined: {len(df)} knots, raw {df.raw.min():.4f}..{df.raw.max():.4f}, "
      f"Phred {df.phred.min():.2f}..{df.phred.max():.2f}")

# monotonicity check: Phred must increase with raw
bad = df[df.phred.diff() < 0]
print(f"non-monotone knots: {len(bad)}")
if len(bad):
    print(df.to_string(index=False))

# ---- compare candidate forms ------------------------------------------------
x, y = df.raw.values, df.phred.values
for name, pred in (
        ("linear in raw", np.polyval(np.polyfit(x, y, 1), x)),
        ("quadratic in raw", np.polyval(np.polyfit(x, y, 2), x)),
        ("linear in log10(raw)", np.polyval(np.polyfit(np.log10(x), y, 1), np.log10(x))),
):
    r = np.abs(pred - y)
    print(f"   {name:22s} max residual {r.max():6.2f}  mean {r.mean():5.2f}")
q = np.polyfit(x, y, 2)
print(f"   quadratic vertex at raw = {-q[1] / (2 * q[0]):.3f}  "
      f"(turns over -> unusable above this)")

# ---- the calibration we keep: monotone interpolation ------------------------
pchip = PchipInterpolator(x, y, extrapolate=False)
resid = np.abs(pchip(x) - y)
print(f"   {'PCHIP (monotone)':22s} max residual {np.nanmax(resid):6.4f}  (exact at knots)")

cal = {
    "what": "raw AVI -> AVI Phred, interpolated from paired observations",
    "why": "the Atlas API exposes AVI_SCORE only; no phred/quantile scorer exists",
    "method": "PCHIP monotone cubic interpolation over the knots below; no extrapolation",
    "phred_definition": "phred = -10 * log10(tail quantile); percentile = 10^(-phred/10) * 100",
    "valid_raw_range": [float(x.min()), float(x.max())],
    "valid_phred_range": [float(y.min()), float(y.max())],
    "n_knots": int(len(df)),
    "max_residual_at_knots": float(np.nanmax(resid)),
    "caution": ("outside valid_raw_range the mapping is left blank rather than extrapolated. "
                "A quadratic fit on the benign set alone turns over at raw "
                f"{-q[1] / (2 * q[0]):.2f} and must not be used."),
    "knots": df[["variant", "raw", "phred", "source"]].to_dict(orient="records"),
}
(OUT / "jak_avi_phred_calibration.json").write_text(json.dumps(cal, indent=2) + "\n",
                                                    encoding="utf-8")
print(f"\nwrote {OUT / 'jak_avi_phred_calibration.json'}")
