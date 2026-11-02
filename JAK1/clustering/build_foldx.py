"""FoldX ddG for JAK1 in EV1 order, from the ProtVar extract already in this repository.

The paper's "MutFunc score" is ambiguous - today's mutfunc returns four columns
(Pathogenicity, Stability ddG, pDockQ, Pocket score) - but its Stability column is FoldX,
and mutfunc covers only ~8% of variants because it needs structural coverage.

external_data/protvar_foldx_jak_src.csv already holds FoldX v5 ddG computed on AlphaFold2
models for all four JAKs, with JAK1 (P23458) at 20,805 substitutions. That is the same
quantity at roughly twelve times the coverage, so it is used instead.
"""
import pathlib

import pandas as pd

HERE = pathlib.Path(__file__).parent
SRC = "https://raw.githubusercontent.com/chervov/ProteinModelling1/main/external_data/protvar_foldx_jak_src.csv"

d = pd.read_csv(SRC)
j = d[d.uniprot_accession == "P23458"].copy()
print(f"ProtVar FoldX rows for JAK1 (P23458): {len(j):,}")
j["variant_id"] = j.wild_type + j.uniprot_position.astype(str) + j.mutated_type
j = j[j.wild_type != j.mutated_type]
print(f"after dropping self-substitutions: {len(j):,}; distinct: {j.variant_id.nunique():,}")

# one value per substitution; check there is no ambiguity to resolve
g = j.groupby("variant_id").foldx_ddg
print(f"substitutions with >1 row: {(g.size() > 1).sum():,}; "
      f"max spread {(g.max() - g.min()).max():.4f}")

agg = j.groupby("variant_id").agg(foldx_ddg=("foldx_ddg", "max"),
                                  plddt=("plddt", "max"))

base = pd.read_csv(HERE / "jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
out = base.copy()
out["foldx_ddg"] = out.variant_id.map(agg.foldx_ddg).round(4)
out["plddt"] = out.variant_id.map(agg.plddt)
out.to_csv(HERE / "jak1_foldx.csv", index=False)

real = (base.wt != base.alt).sum()
n = out.foldx_ddg.notna().sum()
print(f"\nwrote jak1_foldx.csv: {len(out):,} rows in EV1 order; "
      f"{n:,} of {real:,} ({n / real:.1%})")
print(f"   ddG range {out.foldx_ddg.min():.2f} .. {out.foldx_ddg.max():.2f} kcal/mol, "
      f"median {out.foldx_ddg.median():.3f}")
print(f"   positions covered: {out.loc[out.foldx_ddg.notna(), 'pos'].nunique():,} of 1,154")

# which positions are missing, and why
missing_pos = sorted(set(range(1, 1155)) - set(out.loc[out.foldx_ddg.notna(), "pos"]))
print(f"   positions with no FoldX at all: {len(missing_pos)}")
if missing_pos:
    print(f"      {missing_pos[:20]}{' ...' if len(missing_pos) > 20 else ''}")
have = out.dropna(subset=["foldx_ddg"])
print(f"   pLDDT where covered: median {have.plddt.median():.1f}, "
      f"min {have.plddt.min():.1f}")

# sign convention check against a few known destabilising changes
print("\nsample (FoldX convention: positive = destabilising):")
print(out[out.variant_id.isin(["A1005E", "I617T", "H647Q", "P815S", "G571R"])]
      [["variant_id", "foldx_ddg", "plddt"]].to_string(index=False))
