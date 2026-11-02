"""Precomputed FoldX ddG for JAK1, in EV1 order.

Not computed here. EBI ProtVar publishes FoldX v5.0 ddG on AlphaFold2 models across the human
proteome; external_data/protvar_foldx_jak_src.csv is the extract for the four JAKs plus SRC,
and this reshapes JAK1 (P23458) onto the Dataset EV1 row set.

The 2025.02.10 ProtVar release no longer applies the pLDDT >= 70 filter that earlier releases
did, so a `high_confidence` flag is added: low-pLDDT rows are biased toward ddG near zero,
which reads as "tolerated" when the model simply has no structure to judge.
"""
import pathlib

import pandas as pd

HERE = pathlib.Path(__file__).parent
SRC = ("https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"
       "external_data/protvar_foldx_jak_src.csv")
OUT = HERE / "jak1_ddg_foldx_precomputed.csv"

d = pd.read_csv(SRC)
j = d[d.uniprot_accession == "P23458"].copy()
j["variant_id"] = j.wild_type + j.uniprot_position.astype(str) + j.mutated_type
j = j[j.wild_type != j.mutated_type]
print(f"ProtVar FoldX rows for JAK1 (P23458): {len(j):,}; "
      f"distinct substitutions: {j.variant_id.nunique():,}")

g = j.groupby("variant_id").foldx_ddg
print(f"substitutions appearing more than once: {(g.size() > 1).sum():,} "
      f"(max spread {(g.max() - g.min()).max():.4f}) - nothing to aggregate")

agg = j.groupby("variant_id").agg(foldx_ddg=("foldx_ddg", "max"),
                                  plddt=("plddt", "max"))

base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
out = base.copy()
out["foldx_ddg"] = out.variant_id.map(agg.foldx_ddg).round(4)
out["plddt"] = out.variant_id.map(agg.plddt).round(2)
# 1 where the AlphaFold model is confident enough to trust the ddG, 0 where it is not,
# blank where there is no value at all
out["high_confidence"] = out.plddt.ge(70).astype("Int64").where(out.plddt.notna())
out.to_csv(OUT, index=False)

real = (base.wt != base.alt).sum()
n = out.foldx_ddg.notna().sum()
hi = (out.high_confidence == 1).sum()
print(f"\nwrote {OUT.name}: {len(out):,} rows in EV1 order")
print(f"   populated       {n:,} of {real:,} ({n / real:.1%})")
print(f"   high_confidence {hi:,} ({hi / n:.1%} of populated); "
      f"low {int((out.high_confidence == 0).sum()):,}")
print(f"   ddG range {out.foldx_ddg.min():.2f} .. {out.foldx_ddg.max():.2f}, "
      f"median {out.foldx_ddg.median():.3f}")
print(f"   median ddG: high-confidence {out.loc[out.high_confidence == 1, 'foldx_ddg'].median():.3f}"
      f", low {out.loc[out.high_confidence == 0, 'foldx_ddg'].median():.3f}")
print(f"   positions covered {out.loc[out.foldx_ddg.notna(), 'pos'].nunique():,} of 1,154")
print("\nhead:")
print(out.head(4).to_string(index=False))
