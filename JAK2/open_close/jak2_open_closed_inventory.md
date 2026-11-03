# Do we have a closed full-length JAK2?

**Yes.** Measured 3 November 2026 by `inventory_jak2_states.py`, which re-measures every
JAK2 structure in the repository and ignores what the filenames claim.

Short version: **16 wild-type full-length closed JAK2 models**, the best at **6.0 Å** JH1 RMSD
from Shan's JAK2 after JH2 superposition, and the closed state is reproduced **without any
template**, so it is not simply the template handed back. The open state is the easy one — the
AlphaFold DB model, both AF3 runs and many OpenFold runs are all open at FERM–JH1 ≈ 94 Å.

## The starting confusion, resolved

Shan's JAK2 covers residues **520–1131** (JH2–JH1 only), as you remembered — it cannot be a
dual-state ΔΔG template on its own. But our own OpenFold runs are **full length, 1–1132**, and
several of them are closed.

## How "closed" is decided here

Three measures, in increasing order of trustworthiness:

| measure | open | closed | comment |
|---|--:|--:|---|
| JH2–JH1 centroid | 46 Å | 39 Å | **weak** — the transition is mostly a rotation of JH1, so the centroid barely moves |
| FERM–JH1 centroid | ~94 Å | ~42 Å | strong, needs no reference |
| **JH1 RMSD to Shan 2014 after fitting JH2** | ~83 Å | **< 10 Å** | says *which* closed state, not merely "compact" |

The third is the one that matters, and it is why this inventory exists. Twenty-one structures are
compact (FERM–JH1 < 60 Å) but **land 17–98 Å from Shan's JH1 position** — they are collapsed into
some other arrangement, not autoinhibited. Treating FERM–JH1 alone as the criterion would have
admitted all of them.

## The filenames are not usable

**41 of 71 structures are mislabelled** — `selected_open.pdb` is frequently closed and vice versa.
This is a known consequence, not a surprise: the guided-recycling selection used the JH2–JH1
centroid distance, and `../../open_close.md` already recommended switching to FERM–JH1 precisely
because *"'selected open/closed' means something"* only then. That switch was never applied
retroactively, so **every downstream use must re-measure**. The inventory JSON carries both the
filename label and the measurement for exactly this reason.

## Wild-type closed models, best first

| run | file | template | FERM–JH1 | JH2–JH1 | pLDDT | JH1 vs Shan |
|---|---|---|--:|--:|--:|--:|
| `JAK2_20261015_082903` | selected_closed | ma-l9b1f | 45.0 | 39.0 | 85.6 | **6.0** |
| `JAK2_20261015_105613` | selected_closed | ma-l9b1f | 45.1 | 39.0 | 85.6 | 6.2 |
| `JAK2_20261014_115511` | selected_closed | ma-l9b1f | 44.3 | 39.3 | 86.6 | 6.7 |
| `JAK2_20261015_111048` | selected_closed | ma-l9b1f | 44.1 | 39.0 | 86.0 | 6.7 |
| **`JAK2_20261015_161033`** | **selected_closed** | **none** | **44.8** | **39.3** | **85.3** | **6.9** |
| **`JAK2_20261015_134643`** | **selected_closed** | **none** | **45.6** | **39.5** | **85.0** | **6.9** |
| `JAK2_20261015_120253` | selected_closed | 4OLI+shan+6E2Q+ma-l9b1f | 41.9 | 39.5 | 86.2 | 7.9 |

Reference values from `../../open_close.md`: the JAK1 closed model mapped onto JAK2 (`ma-l9b1f`)
sits at FERM–JH1 42.2, JH2–JH1 39.8; Shan's JAK2 at JH2–JH1 40.9.

### Why the two bold rows are the important ones

Every other closed model above was built **from a closed template** — `ma-l9b1f` is the JAK1
closed model renumbered onto JAK2, so those runs largely return the arrangement they were given.
`JAK2_20261015_161033` and `JAK2_20261015_134643` had **`template_source: null`**: MSA only
(512/8192 clusters, 15 recycles, 11 seeds), wild-type, and they produced a closed model at 6.9 Å
from Shan anyway. That is independent evidence that AlphaFold finds the autoinhibited JAK2
arrangement from sequence, and it is what makes the closed state usable rather than circular.

**`JAK2_20261015_161033` additionally produced a genuinely open model in the same run**
(FERM–JH1 95.3, 83.3 Å from Shan's JH1, pLDDT 86.3). One run, one MSA, one set of hyperparameters,
both states — which is the ideal starting point for a dual-state comparison, because nothing
differs between the two structures except the conformation.

## Recommended pair for the dual-state ΔΔG

```
closed : JAK2/runs/JAK2_20261015_161033/selected_closed.pdb   FERM-JH1 44.8   pLDDT 85.3
open   : JAK2/runs/JAK2_20261015_161033/selected_open.pdb     FERM-JH1 95.3   pLDDT 86.3
```

With `JAK2_20261015_082903/selected_closed.pdb` (6.0 Å, templated) as the sensitivity check: if
ΔΔG_closed changes materially between the untemplated and templated closed models, the dual-state
feature is reporting on the model rather than on the protein.

### Caveats before using it
- **pLDDT ~85 overall**, but that is a whole-chain mean. The ΔΔG at a given position is only as
  good as the local confidence, and the JH2–JH1 linker and surface loops are much worse. Per-residue
  pLDDT should gate which positions get a dual-state ΔΔG, as on JAK1.
- **The open model is AlphaFold's default**, which is what AFDB and both AF3 runs also give. It is
  well supported but it is one state, not an ensemble.
- **No PAE for these runs.** `model_1` does not emit it; `model_1_ptm` would. Without inter-domain
  PAE there is no direct measure of how confident the network is about *where JH1 sits*, which is
  precisely the quantity the closed state depends on. `../../open_close.md` flagged this as an open
  item and it is still open.
- These are **OpenFold guided-recycling outputs**, selected per recycle, not vanilla predictions.

## Reproduce

```bash
python3 JAK2/open_close/inventory_jak2_states.py     # prints the table, writes jak2_state_inventory.json
```
