# JAK1 — the third domain arrangement

OpenFold, given the wild-type JAK1 sequence, a **shallow MSA and no template**, produced a
JH2–JH1 arrangement that is neither open nor closed. It matches **7T6F**, the cryo-EM structure of
the **active JAK1 dimer**, to **4.9 Å**.

**[`jak1_third_structure.html`](jak1_third_structure.html)** — the page: all seven structures in
3D, the superposition against 7T6F, and the distance tables. One self-contained file, 2.1 MB.

| | from the third arrangement |
|---|--:|
| **7T6F** (experimental active dimer) | **4.9 Å** |
| open (ma-a1sai) | 47.1 Å |
| closed (ma-l9b1f) | 83.0 Å |

Measured as JH1 Cα RMSD after superposing JH2 — the metric that says *which* arrangement a
structure is in, rather than how extended it is.

## Why this is a real third state and not a partly-open one

**FERM–JH1 resolves three bands:** closed 40 Å, third **84 Å**, open 92–94 Å. But distance alone
would not settle it, so three further things do:

1. **SH2–JH1 is 52–55 Å, against 78 Å for open.** JH1 has swung somewhere else, not merely moved
   less far.
2. **JH1 is rotated 130–150° relative to open** and touches **only JH2**, through a small
   interface of its own — JH2 ~750 and 798–807, JH1 ~930–941 and 997 — which shares almost nothing
   with either the open or the closed interface and does **not** involve the V658 region central
   to the closed one.
3. **The metric is calibrated.** Same-state pairs land under ~6 Å (the open family — 8EWY,
   ma-a1sai, AFDB — agree to 3.4–6.3 Å); different-state pairs are above 45 Å. 4.9 Å is
   same-state.

**The best control is 8EWY.** It is also a cryo-EM JAK1 dimer, and it sits **6.3 Å from open** and
48.5 Å from 7T6F. So the two experimental JAK1 dimer structures are themselves in *different*
arrangements, and our runs reproduce **both** — the third arrangement matches one, our open models
match the other. That makes the 4.9 Å a real correspondence rather than an artefact of the metric.

## Where it appears

| MSA depth | seeds reaching it |
|---|---|
| 64 / 256 | all 5 (seed 4 a variant, 14–22 Å away) |
| 96 / 384 | 2 of 5 |
| 128 / 512 and deeper | none — open or closed only |

No template, 15 recycles, wild-type sequence. It appears **only at shallow MSA depth** and
disappears as the alignment deepens, which pulls the prediction to the AlphaFold default — open,
for JAK1.

The structures are not degraded: each domain is within 1.3 Å Cα RMSD of the AF2 model and JH1
pLDDT is 87–91, as high as in the open and closed models.

## What it is not

**A positive control, not a discovery.** 7T6F *is* a JAK1 structure, so a JAK1 prediction
reaching it shows the pipeline can find a measured arrangement from sequence alone. It does not
make JAK1 special and it predicts nothing that was not already known experimentally.

**The arrangement is JAK1-only in our runs** — 35 hits of 129 for JAK1, against 0, 0 and 2 for
JAK2, JAK3 and TYK2. Related: JAK2 never reaches an experimentally characterised extended state
(0 of 237) although 96 of its structures match extended AF2 JAK2 — it "goes extended without going
anywhere known".

**A correction sits underneath all of this.** 7T6F and 8EWY are **mouse JAK1**, not JAK2 — 98.0%
identity to JAK1_MOUSE against 43.1% to JAK2. An earlier note had them as mouse JAK2, citing
P52332, which is itself JAK1_MOUSE. The consequence still constrains the whole project: **there is
no experimental multi-domain structure for JAK2, JAK3 or TYK2 at all**, so every closed-state
number for those three is against a prediction or a cross-paralogue JAK1 structure.

## Files

| file | what |
|---|---|
| `jak1_third_structure.html` | the page |
| `JAK1_third.md` | the original analysis — contacts, interface residues, rotations, caveats |
| `analyse.py`, `analysis.json`, `exp_compare.json`, `wt_vs_v658f_128.json` | the original scripts and results (formerly `../third_arrangement/`, now removed as a duplicate) |
| `analyse_third.py` → `third_analysis.json` | the geometry behind this page |
| `build_html.py` | builds the page |
| `structures/` | all seven structures, including 7T6F and 8EWY from the PDB |

References: **7T6F** Glassman et al., *Science* 2022,
[10.1126/science.abn8933](https://doi.org/10.1126/science.abn8933) ·
**8EWY** Caveney et al., *Cell Reports* 2023 ·
family-wide state definitions in [`../../reference_states.md`](../../reference_states.md)

```bash
python3 analyse_third.py && python3 build_html.py
```
