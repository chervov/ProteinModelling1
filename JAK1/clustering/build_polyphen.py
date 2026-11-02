"""Turn the PolyPhen-2 batch output into a feature CSV in EV1 order, and validate it.

Validation is against the 6,873 dbNSFP HVAR values already in the repo: the new
full-coverage run must reproduce them, otherwise the pipeline is wrong rather than
merely more complete.
"""
import pathlib
import sys

import pandas as pd

HERE = pathlib.Path(__file__).parent
MODEL = sys.argv[1] if len(sys.argv) > 1 else "humvar"
DIRNAME = {"humvar": "pph2_hvar", "humdiv": "pph2_hdiv"}[MODEL]
SRC = HERE / DIRNAME / "pph2-short.txt"

rows = []
for line in SRC.read_text(encoding="utf-8", errors="replace").splitlines():
    if line.startswith("#") or not line.strip():
        continue
    f = [c.strip() for c in line.split("\t")]
    if len(f) < 12:
        continue
    rows.append({"pos": int(f[1]), "wt": f[2], "alt": f[3],
                 "prediction": f[9],
                 "prob": pd.to_numeric(f[10], errors="coerce"),
                 "fpr": pd.to_numeric(f[11], errors="coerce")})
pph = pd.DataFrame(rows)
pph["variant_id"] = pph.wt + pph.pos.astype(str) + pph.alt
print(f"parsed {len(pph):,} rows; {pph.prob.notna().sum():,} with a probability")
print(f"duplicate variant_ids: {pph.variant_id.duplicated().sum()}")
print("\nprediction classes:")
print(pph.prediction.value_counts(dropna=False).to_string())

# ---- align to EV1 order -----------------------------------------------------
base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
look = pph.drop_duplicates("variant_id").set_index("variant_id")
out = base.copy()
out[f"polyphen2_{MODEL}_prob"] = out.variant_id.map(look["prob"])
out[f"polyphen2_{MODEL}_pred"] = out.variant_id.map(look["prediction"])
fname = HERE / f"jak1_polyphen2_{MODEL}.csv"
out.to_csv(fname, index=False)
n = out[f"polyphen2_{MODEL}_prob"].notna().sum()
real = (out.wt != out.alt).sum()
print(f"\nwrote {fname.name}: {len(out):,} rows in EV1 order")
print(f"   {n:,} of {real:,} real substitutions scored = {n / real:.2%} coverage")
print(f"   (dbNSFP gave 6,873 = 31.3%)")

# ---- validate against dbNSFP ------------------------------------------------
ext = pd.read_csv("sources/counts/JAK1_ext.csv", low_memory=False)
ext = ext[ext.Variant.str.match(r"^[A-Z]\d+[A-Z]$", na=False)]
#  HVAR scores are in the curated "PolyPhen-2 HVAR" column; HDIV has its own dbNSFP column
col = "PolyPhen-2 HVAR" if MODEL == "humvar" else "dbNSFP polyphen2.hdiv.score"
if col not in ext.columns:
    raise SystemExit(f"no column {col!r}; available: "
                     f"{[c for c in ext.columns if 'oly' in c]}")
if col in ext.columns:
    ext["db"] = pd.to_numeric(ext[col].astype(str).str.split("|").str[0], errors="coerce")
    m = out.merge(ext[["Variant", "db"]], left_on="variant_id", right_on="Variant")
    m = m.dropna(subset=["db", f"polyphen2_{MODEL}_prob"])
    d = (m[f"polyphen2_{MODEL}_prob"] - m.db).abs()
    print(f"\nvalidation against {col}: {len(m):,} shared variants")
    print(f"   Pearson {m[f'polyphen2_{MODEL}_prob'].corr(m.db):.4f}, "
          f"Spearman {m[f'polyphen2_{MODEL}_prob'].corr(m.db, method='spearman'):.4f}")
    print(f"   identical to 3dp: {(d < 0.0005).sum():,} ({(d < 0.0005).mean():.1%}); "
          f"max abs difference {d.max():.4f}; median {d.median():.5f}")
    big = m[d > 0.1]
    print(f"   differing by >0.1: {len(big):,}")
    if len(big):
        print(big[["variant_id", f"polyphen2_{MODEL}_prob", "db"]].head(8).to_string(index=False))
