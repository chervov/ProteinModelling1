"""The paper's three dual-state PyRosetta ddG features for JAK1, in EV1 order.

Source: data/ddg/ddg_JAK1_all.json - complete JAK1 saturation, 21,926 variants over all
1,154 positions, from the overnight run of 2026-10-22 on four molab CPU boxes, computed on
**Jeanpierre's own open and closed models** (RUNBOOK.md). So this is the paper's own
quantity on the paper's own structures.

Sign convention here is the project's: ddG = dG_WT - dG_mut, so NEGATIVE = destabilising -
the opposite of FoldX. delta = ddg_open - ddg_closed is a conformational-preference shift,
not a stability change.

A `within_15` flag is added because 27.8% of the single-state values exceed |10| and 11.0%
exceed |100| - unrelaxed steric clashes, diagnosed in conclusions_ddG_difference_feature.md
sections 8-10. rosetta_dualstate_qc.md uses |ddg| < 15 as the survivable window (74.3%).
"""
import json
import pathlib

import pandas as pd
import requests

HERE = pathlib.Path(__file__).parent
SRC = ("https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"
       "data/ddg/ddg_JAK1_all.json")
OUT = HERE / "jak1_ddg_rosetta_dualstate.csv"

r = requests.get(SRC, timeout=900)
r.raise_for_status()
d = pd.DataFrame(json.loads(r.content.decode("utf-8")))
d["variant_id"] = d.wt + d.pos.astype(str) + d.alt
print(f"source records: {len(d):,}; distinct substitutions: {d.variant_id.nunique():,}; "
      f"positions {d.pos.nunique():,}")

agg = d.drop_duplicates("variant_id").set_index("variant_id")
base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
out = base.copy()
for col in ("ddg_closed", "ddg_open", "delta"):
    out[col] = out.variant_id.map(agg[col]).round(4)
# 1 where both single-state values are inside the window the QC note uses, 0 outside
inwin = out.ddg_closed.abs().lt(15) & out.ddg_open.abs().lt(15)
out["within_15"] = inwin.astype("Int64").where(out.ddg_closed.notna())
out.to_csv(OUT, index=False)

real = (base.wt != base.alt).sum()
n = out.ddg_closed.notna().sum()
k = int((out.within_15 == 1).sum())
print(f"\nwrote {OUT.name}: {len(out):,} rows in EV1 order")
print(f"   populated  {n:,} of {real:,} ({n / real:.1%})")
print(f"   within_15  {k:,} ({k / n:.1%} of populated)  -  the rest are clash artefacts")
for c in ("ddg_closed", "ddg_open", "delta"):
    v = out[c]
    print(f"   {c:11s} range {v.min():10.2f} .. {v.max():9.2f}   median {v.median():8.4f}")
print("\nrestricted to within_15 (the usable subset):")
sub = out[out.within_15 == 1]
for c in ("ddg_closed", "ddg_open", "delta"):
    print(f"   {c:11s} range {sub[c].min():8.2f} .. {sub[c].max():7.2f}   "
          f"median {sub[c].median():8.4f}   SD {sub[c].std():.3f}")
print("\nhead:")
print(out.head(4).to_string(index=False))
