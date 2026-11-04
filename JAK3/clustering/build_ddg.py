"""The three dual-state ddG features for JAK3.

Computed fresh on 4 November 2026 with PyRosetta, locally, using `pipeline/ddg/worker.py`
(see `JAK2/clustering/ddg/RUNBOOK_jak2_dualstate_ddg.md` for the design). Results land in
`data/ddg/ddg_JAK3_all.json`; this script only joins them onto the canonical variant order.

THE TWO STRUCTURES - read before using ddg_delta
  closed  JAK3/af3_notemplate/jak3_af3_notemplate_closed_model0.pdb
          AF3, no template. FERM-JH1 40.7 A; 0.82 A from the AlphaFold DB model after a JH2 fit.
  open    JAK3/runs/JAK3_20261016_172413/selected_open.pdb
          OpenFold, no template. FERM-JH1 94.1 A.

Both were measured, not trusted from their filenames: 14 of JAK3's 30 selected_*.pdb files are
mislabelled, and three OpenFold runs produced *compact* models that sit 15-16 A from the
autoinhibited arrangement - collapsed into some other state. FERM-JH1 distance alone would have
accepted all of them.

CONFOUND: the closed model comes from AF3 and the open from OpenFold, so the pair differs in
predictor as well as in conformation. Milder than TYK2's pair, where the FERM domain alone
differed by 5.47 A; here every per-domain RMSD between the two states is 0.31-0.93 A, so they
really are related by a motion of JH1. But it is not the single-run pair JAK2 pair 1 was.

JAK3 has NO experimental closed structure, so the reference arrangement is the AlphaFold DB
model, which is itself closed. Weaker than TYK2's 4OLI crystal.

Sign convention: ddG = dG_WT - dG_mut, so NEGATIVE = destabilising. Opposite to FoldX.
"""
import json, pathlib
import pandas as pd

HERE = pathlib.Path(__file__).parent
SRC = HERE / ".." / ".." / "data" / "ddg" / "ddg_JAK3_all.json"

base = pd.read_csv(HERE / "jak3_variant_universe.csv")
base["wt"] = base.variant.str[0]
base["pos"] = base.variant.str[1:-1].astype(int)
base["alt"] = base.variant.str[-1]
rec = {(r["pos"], r["alt"]): r for r in json.load(open(SRC))}

mism = [v for v, p, w in zip(base.variant, base.pos, base.wt)
        if (p, v[-1]) in rec and rec[(p, v[-1])]["wt"] != w]
print(f"wild-type mismatches against P52333: {len(mism)}" + (f"  {mism[:5]}" if mism else " - clean"))
assert not mism, "the ddG table disagrees with the canonical sequence"

for col, key in (("ddg_closed", "ddg_closed"), ("ddg_open", "ddg_open"), ("ddg_delta", "delta")):
    base[col] = [rec.get((p, a), {}).get(key) for p, a in zip(base.pos, base.alt)]
    out = base[["index", "variant", "wt", "pos", "alt", col]]
    out.to_csv(HERE / f"jak3_{col}.csv", index=False)
    n = out[col].notna().sum()
    print(f"jak3_{col}.csv: {n:,}/{len(out):,} ({100*n/len(out):.1f}%)")
