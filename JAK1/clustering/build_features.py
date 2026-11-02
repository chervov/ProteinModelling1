"""Step 3-5 of the JAK1 clustering rebuild.

1. verify the UniProt sequence against every variant_id in Dataset EV1
2. verify jak1_features.json is in EV1 order
3. emit per-feature CSVs aligned row-for-row with EV1

EV1 has 23,080 rows including the 1,154 self-substitutions (A1005A etc.);
jak1_features.json has the 21,926 real variants. Every CSV written here keeps all
23,080 EV1 rows in EV1 order, so any two can be pasted side by side.
"""
import json
import pathlib

import openpyxl
import pandas as pd

HERE = pathlib.Path(__file__).parent
XLSX = HERE / "44321_2025_317_MOESM3_ESM.xlsx"
FEATURES = pathlib.Path("sources/orianne/jak1_features.json")

# ---- the sequence ------------------------------------------------------------
fasta = (HERE / "JAK1_P23458.fasta").read_text(encoding="utf-8").splitlines()
seq = "".join(l.strip() for l in fasta[1:])
print(f"UniProt P23458: {len(seq)} aa")

# ---- EV1, in file order ------------------------------------------------------
ws = openpyxl.load_workbook(XLSX, read_only=True, data_only=True)["Sheet1"]
rows = ws.iter_rows(values_only=True)
hdr = next(rows)
ev1 = [(str(r[0]), r[1]) for r in rows if r and r[0]]
print(f"EV1: {len(ev1):,} rows, header {hdr}")

# ---- 1. sequence check -------------------------------------------------------
bad, selfsub = [], 0
parsed = []
for vid, cl in ev1:
    wt, pos, alt = vid[0], int(vid[1:-1]), vid[-1]
    parsed.append((vid, wt, pos, alt, cl))
    if pos < 1 or pos > len(seq):
        bad.append((vid, "position out of range"))
    elif seq[pos - 1] != wt:
        bad.append((vid, f"sequence has {seq[pos - 1]}{pos}"))
    if wt == alt:
        selfsub += 1
print(f"\nCHECK 1 - wild-type residue vs UniProt sequence:")
print(f"   {len(ev1) - len(bad):,} of {len(ev1):,} match; {len(bad)} mismatches")
for v, why in bad[:10]:
    print(f"      {v}: {why}")
print(f"   self-substitutions (wt == alt): {selfsub:,}")
print(f"   positions covered: {len({p for _, _, p, _, _ in parsed}):,} of {len(seq):,}")

# ---- 2. order check ----------------------------------------------------------
feat = pd.DataFrame(json.load(open(FEATURES, encoding="utf-8")))
feat["variant_id"] = feat.wt + feat.pos.astype(str) + feat.alt
ev1_nonself = [v for v, w, p, a, c in parsed if w != a]
same = list(feat.variant_id) == ev1_nonself
print(f"\nCHECK 2 - jak1_features.json order vs EV1 order (self-subs removed):")
print(f"   features rows {len(feat):,}, EV1 non-self {len(ev1_nonself):,}")
print(f"   identical sequence of variant_ids: {same}")
if not same:
    for i, (a, b) in enumerate(zip(feat.variant_id, ev1_nonself)):
        if a != b:
            print(f"   first divergence at row {i}: features={a} ev1={b}")
            break
    print(f"   same set regardless of order: {set(feat.variant_id) == set(ev1_nonself)}")

# cluster labels must also agree
cl_ev1 = {v: c for v, w, p, a, c in parsed if w != a}
agree = sum(1 for r in feat.itertuples() if cl_ev1.get(r.variant_id) == r.cluster)
print(f"   cluster labels agreeing with EV1: {agree:,} of {len(feat):,}")

# ---- 3. write the aligned CSVs ----------------------------------------------
base = pd.DataFrame(parsed, columns=["variant_id", "wt", "pos", "alt", "cluster"])
lookup = feat.set_index("variant_id")

for col, fname, label in (("esm1b", "jak1_esm1b.csv", "ESM-1b"),
                          ("alphamissense", "jak1_alphamissense.csv", "AlphaMissense")):
    out = base.copy()
    out[col] = out.variant_id.map(lookup[col])
    out.to_csv(HERE / fname, index=False)
    n = out[col].notna().sum()
    print(f"\n{fname}: {len(out):,} rows in EV1 order, {n:,} with a {label} value "
          f"({n / len(out):.1%}); blanks are the {selfsub:,} self-substitutions")
    print(out.head(3).to_string(index=False))
    print(f"   range {out[col].min():.4g} .. {out[col].max():.4g}")
