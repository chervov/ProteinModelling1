# new_mutation_method1 — mutant-vs-wild-type AlphaFold scan

*Assembled 27 October 2026. Self-contained copy of every document and data file behind the
mutation-effect results. Files are copies of the repository versions as of this date; the
originals remain at the paths listed in **Provenance** at the bottom.*

---

## What this is

A method for detecting the conformational effect of a point mutation from AlphaFold predictions
alone, by running the mutant **in the same cell as wild type** — same protein, same MSA depth,
same template mode — and comparing the two on two independent axes:

- **arrangement** — superpose on JH2, measure JH1 Cα RMSD against a reference panel, assign to
  open/closed within 15 Å
- **compactness** — FERM–JH1 centroid distance, tracked separately

**785 structure predictions · 40 mutant-vs-WT Fisher exact tests · Holm-corrected within protein.**
348 wild-type structures provide the matched baselines.

The two controls that make it work — varying MSA depth, and specifying the template — were not
used in the Jeanpierre/Debeaupuis pipeline. Every effect found here is visible only in a narrow
MSA-depth band, so neither control is optional.

---

## Read in this order

| # | file | what it says |
|---|---|---|
| 1 | [`new_methods_mutations20261023.md`](new_methods_mutations20261023.md) | **the results** — all 40 tests, the 5 hits in detail. §1 is one slide. |
| 2 | [`new_methods_summary20261023.md`](new_methods_summary20261023.md) | **the methods contribution** — the two new controls and what they unlock. §1 is one slide. |
| 3 | [`mutation_analysis.md`](mutation_analysis.md) | **full detail** — cross-JAK equivalent positions, 4OLI per-position structural analysis, predictor scores. The long one. |
| 4 | [`mutations_clustering.md`](mutations_clustering.md) | the clustering and state-assignment behind the open/closed calls |
| 5 | [`reference_states.md`](reference_states.md) | the reference structure panel the arrangement metric measures against |
| 6 | [`MASTER_VARIANT_ANALYSIS_SUMMARY.md`](MASTER_VARIANT_ANALYSIS_SUMMARY.md) | earlier cross-variant roll-up, kept for the record |

---

## Results at a glance

Significant after Holm correction:

| Protein | Mutation | Axis | Mutant | Wild type | Holm *p* |
|---|---|---|:---:|:---:|:---:|
| **TYK2** | **V678F** | opens | 18/24 (75%) | 2/24 (8%) | **0.0001** |
| **TYK2** | **V678A** | opens | 10/16 (62%) | 2/24 (8%) | **0.0083** |
| **TYK2** | **P982A** | **closes** | 13/24 (54%) | 23/24 (96%) | **0.034** |
| **JAK2** | **V617F** | extends | 0/16 compact | 9/16 compact | **0.0073** |
| JAK1 | V658F | extends | 0/16 compact | 3/5 compact | 0.030 |

**35 of 40 tests were null**, including every JAK3 mutation. Each hit appears in one MSA-depth
band only (V678F/V678A at 64, P982A at 96, V617F at 512); V617F's direction reverses at 256.
Read the caveats in document 1 §3 before quoting any of this.

---

## Per-variant files

One document per variant, in [`variants/`](variants/):

| variant | file | outcome |
|---|---|---|
| TYK2 P982A | [`TYK2_P982A_complete_analysis.md`](variants/TYK2_P982A_complete_analysis.md), [`TYK2_P982A_analysis.md`](variants/TYK2_P982A_analysis.md) | **significant — closes** |
| TYK2 V678M | [`TYK2_V678M_complete_analysis.md`](variants/TYK2_V678M_complete_analysis.md) | trend only (4/16 vs 2/24, p = 0.195) |
| JAK2 V617F | [`JAK2_V617F.md`](variants/JAK2_V617F.md) | **significant — loses compact state** |
| JAK2 V1110E | [`JAK2_V1110E_complete_analysis.md`](variants/JAK2_V1110E_complete_analysis.md) | null (1 cell) |
| JAK2 G571R | [`JAK2_G571R_complete_analysis.md`](variants/JAK2_G571R_complete_analysis.md) | null (1 cell) |
| JAK2 V578I | [`JAK2_V578I_complete_analysis.md`](variants/JAK2_V578I_complete_analysis.md) | null (1 cell) |
| JAK2 L805I | [`JAK2_L805I_complete_analysis.md`](variants/JAK2_L805I_complete_analysis.md) | null (1 cell) |
| JAK3 Y581C | [`JAK3_Y581C_complete_analysis.md`](variants/JAK3_Y581C_complete_analysis.md) | null (1 cell) |
| JAK3 M592F | [`JAK3_M592F.md`](variants/JAK3_M592F.md) | null |
| JAK1 V658F | [`JAK1_V658F.md`](variants/JAK1_V658F.md) | significant on compactness |
| — | [`JAK2_intermediate.md`](variants/JAK2_intermediate.md) | the JAK2 intermediate-state analysis |

**Caveat on the five one-cell nulls** (JAK2 V1110E/G571R/V578I/L805I, JAK3 Y581C): each was run
in a single cell, 16 runs, where wild type is 0/16 open. There was no headroom to detect an
arrangement effect, so these are uninformative cells rather than negative results. Re-running
them across the depth ladder is the obvious follow-up.

---

## Data

In [`data/`](data/):

| file | contents |
|---|---|
[`mut_vs_wt.json`](data/mut_vs_wt.json) | **all 40 tests** — one record per (protein, mutation, MSA depth, template mode) with mutant open/n, WT open/n, raw *p*, Holm *p* |
[`wt_simulation_summary.json`](data/wt_simulation_summary.json) | the matched wild-type baselines, per cell |
[`tyk2_per_run_rows.json`](data/tyk2_per_run_rows.json) | **per-run detail for TYK2** — 394 rows, each with the run id, variant, MSA depth, template mode, assigned state, FERM–JH1 distance, and RMSD to every reference structure |

`mut_vs_wt.json` record shape:

```json
{"cell": ["TYK2", "96/384", "free"], "mut": "P982A",
 "n": 24, "open": 13, "fo": 0.5417,
 "nwt": 24, "wtopen": 23, "fwt": 0.9583,
 "p": 0.0017974, "holm": 0.0683}
```

`fo`/`fwt` are the open fractions for mutant and wild type.

**The two Holm values differ, deliberately.** The `holm` field in this file is corrected over
**all 40 tests** (P982A 96/384: 0.0018 × 38 = 0.068). Document 1 reports **0.034**, which is the
same *p* corrected **within TYK2's 21 tests** (0.0018 × 19). TYK2 was scanned far more heavily
than the other three proteins, so the all-40 family penalises its hits for tests run on JAK2 and
JAK3; the within-protein family is the one the document argues for. P982A is the case where the
choice matters — it clears 0.05 under one family and not the other. Both numbers are in the open
here so the reader can pick.

---

## Code

[`code/make_clustering_report.py`](code/make_clustering_report.py) — the state-assignment and
reporting script that turns run directories into the rows in `tyk2_per_run_rows.json`.

---

## Structures

Prediction outputs are **not** copied here; they are large and already in the repository:

- `TYK2/runs/` — 294 run directories
- `JAK2/runs/` — 35
- `JAK3/runs/` — 14 (named by variant, e.g. `JAK3_Y581C_20261019_114115`)
- `JAK1/runs/`
- `JAK1/Jeanpierre2025_{Open,Closed}_WT_JAK1_best_model.pdb` and
  `JAK1/Shan2014_*.pdb` — the reference models

TYK2 and JAK2 run directories are named by timestamp only, with no variant in the name. To map a
run to its variant, join on the run id in `data/tyk2_per_run_rows.json`.

---

## Provenance

Every file here is a copy. Originals:

| this folder | repository original |
|---|---|
| `new_methods_mutations20261023.md` | `/new_methods_mutations20261023.md` (also `report2022623/`) |
| `new_methods_summary20261023.md` | `/new_methods_summary20261023.md` (also `report2022623/`) |
| `mutation_analysis.md` | `/mutation_analysis.md` |
| `mutations_clustering.md` | `/mutations_clustering.md` |
| `reference_states.md` | `/reference_states.md` |
| `MASTER_VARIANT_ANALYSIS_SUMMARY.md` | `/MASTER_VARIANT_ANALYSIS_SUMMARY.md` |
| `variants/TYK2_*` | `TYK2/` |
| `variants/JAK2_*` | `JAK2/` |
| `variants/JAK3_*` | `JAK3/` |
| `variants/JAK1_V658F.md` | `JAK1/JAK1_V658F.md` |
| `data/mut_vs_wt.json` | `data/orianne/mut_vs_wt.json` |
| `data/wt_simulation_summary.json` | `data/orianne/wt_simulation_summary.json` |
| `data/tyk2_per_run_rows.json` | not previously in the repository — local `~/tyk2_reclass/rows.json` |
| `code/make_clustering_report.py` | `analysis/make_clustering_report.py` |

`JAK3/` in the repository also contains stray copies of three JAK2 files (G571R, L805I, V578I);
those duplicates were not carried over — the JAK2 originals are in `variants/`.

Related work that is **not** part of this method and lives elsewhere in the repository:
`report2022623/` (the meeting pack), `interface_effect.md`, `conclusions_ddG_difference_feature.md`,
`TYK2/DMS_Howard2026/`.
