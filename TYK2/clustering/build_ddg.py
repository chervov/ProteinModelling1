"""The three dual-state ddG features for TYK2 - REUSED, not recomputed.

These come from the overnight PyRosetta run of 2026-10-22 documented in `data/ddg/RUNBOOK.md`,
which computed dual-state ddG for TYK2 across four molab CPU boxes. Nothing is recalculated here;
this script only joins `data/ddg/ddg_TYK2_all.json` onto the canonical variant order.

PROVENANCE OF THE TWO STRUCTURES - read before using ddg_delta
  closed  TYK2/af3/tyk2_af3_closed.pdb   AF3 job fold_18_48, seed 1087670550,
                                         useStructureTemplate: TRUE   (measured FERM-JH1 39.3 A)
  open    TYK2/af3/tyk2_af3_open.pdb     AF3 job fold_19_34, seed 1754329433,
                                         useStructureTemplate: FALSE  (measured FERM-JH1 82.9 A)

Both states were re-measured here rather than trusted from their filenames, after 41 of 71 JAK2
structure files turned out to be mislabelled. They are correctly named.

**The pair is confounded.** The two models come from different AF3 jobs with different seeds AND
different template settings, so they differ in provenance as well as in conformation. Nothing in
their ddG difference can be attributed cleanly to the conformational change. JAK2 pair 1 was
built specifically to avoid this (both states from one untemplated run); the TYK2 pair is
structurally equivalent to JAK2's *pair 2*, which exists only as a control.

Sign convention: ddG = dG_WT - dG_mut, so NEGATIVE = destabilising. Opposite to FoldX.
"""
import json, pathlib
import pandas as pd

HERE = pathlib.Path(__file__).parent
SRC = HERE / ".." / ".." / "data" / "ddg" / "ddg_TYK2_all.json"

base = pd.read_csv(HERE / "tyk2_variant_universe.csv")
base["wt"] = base.variant.str[0]
base["pos"] = base.variant.str[1:-1].astype(int)
base["alt"] = base.variant.str[-1]
rec = {(r["pos"], r["alt"]): r for r in json.load(open(SRC))}

seq = (HERE / "TYK2_P29597_1187aa.txt").read_text().splitlines()[1].strip()
mism = [v for v, p, w in zip(base.variant, base.pos, base.wt)
        if (p, v[-1]) in rec and rec[(p, v[-1])]["wt"] != w]
print(f"wild-type mismatches against P29597: {len(mism)}" + (f"  {mism[:5]}" if mism else " - clean"))
assert not mism, "the ddG table disagrees with the canonical sequence"

for col, key in (("ddg_closed", "ddg_closed"), ("ddg_open", "ddg_open"), ("ddg_delta", "delta")):
    base[col] = [rec.get((p, a), {}).get(key) for p, a in zip(base.pos, base.alt)]
    out = base[["index", "variant", "wt", "pos", "alt", col]]
    out.to_csv(HERE / f"tyk2_{col}.csv", index=False)
    n = out[col].notna().sum()
    print(f"tyk2_{col}.csv: {n:,}/{len(out):,} ({100*n/len(out):.1f}%)")
