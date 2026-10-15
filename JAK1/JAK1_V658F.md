# JAK1 V658F vs wild type — no template

V658F is the JAK1 equivalent of the activating JAK2 V617F mutation (in JH2, at the JH2–JH1 autoinhibitory interface); the
cryo-EM structure of the active JAK1 dimer (PDB 7T6F) carries the mouse equivalent V657F. Both series: OpenFold model_1, guided
recycling, no template, MSA 128/512 (the depth where wild-type JAK1 is bistable), 15 recycles, seeds 0–14. Classification of
the **final recycle** of each seed: JH1 RMSD after superposing JH2 ≤ 10 Å to the open (ma-a1sai), closed (ma-l9b1f) or
7T6F (cryo-EM active dimer) arrangement; otherwise 'next to FERM' (FERM–JH1 < 55 Å) or 'other'.

Runs: V658F [JAK1_V658F_20261015_160458](runs/JAK1_V658F_20261015_160458); wild type
[JAK1_20261015_082811](runs/JAK1_20261015_082811) (seeds 0–4) + [JAK1_20261015_114024](runs/JAK1_20261015_114024) (seeds 5–14).

## Result

| final state | wild type (15 seeds) | **V658F (15 seeds)** | Fisher exact p |
|---|--:|--:|--:|
| open (ma-a1sai) | 6 (+1 at 10.4 Å) | **9** | 0.47 |
| **closed** (ma-l9b1f) | **3** | **0** | 0.22 |
| next to FERM, not closed | 4 | 1 | |
| **closed + next to FERM** | **7** | **1** | **0.035** |
| **7T6F-like** (active dimer) | 1 | **4** (+1 part way, 18.6 Å) | 0.33 (0.17 incl. partial) |

- **The mutation removes the FERM-bound/closed arrangement** (7 of 15 → 1 of 15, p = 0.035): no V658F seed ends in the
  closed (autoinhibited-model) arrangement; the only FERM-bound seed is 30 Å from it.
- **It shifts seeds towards the 7T6F-like active-dimer arrangement** (1 → 4–5 of 15): V658F seeds 10, 12, 13, 14 are
  5.3–6.6 Å from 7T6F and use its JH2–JH1 interface (overlap 0.82–0.90). With 15 seeds this trend is not yet significant;
  more depths (96/384, 64/256, 32/64, 512/8192, 16 seeds each) are running.
- This is the direction expected for an activating mutation that destabilises the autoinhibitory JH2–JH1 interface, and it
  matches the experimental active-dimer structure, which carries the same mutation.
- Correction to earlier summaries: wild-type seed 3 (run JAK1_20261015_082811), previously described as 'switching, ends
  open-like', ends in the 7T6F-like arrangement (4.6 Å). With the final-recycle criterion wild type has 3 closed seeds
  (4, 7, 13; 3.7–8.1 Å).

## Per seed (final recycle; Å)

| seed | WT: FERM–JH1 / vs open / vs closed / vs 7T6F → class | V658F: FERM–JH1 / vs open / vs closed / vs 7T6F → class |
|--:|---|---|
| 0 | 95.3 / 10.4 / 87.6 / 48.0 → **other** | 93.9 / 4.7 / 84.1 / 48.3 → **open** |
| 1 | 93.0 / 2.5 / 82.0 / 48.8 → **open** | 94.1 / 3.4 / 83.3 / 48.3 → **open** |
| 2 | 44.1 / 88.1 / 22.3 / 94.3 → **next to FERM (not closed)** | 94.5 / 3.5 / 84.2 / 47.1 → **open** |
| 3 | 83.7 / 44.3 / 81.3 / 4.6 → **7T6F-like** | 90.0 / 43.2 / 87.3 / 18.6 → **other** |
| 4 | 41.0 / 82.9 / 8.1 / 86.1 → **closed** | 93.7 / 2.2 / 82.9 / 47.9 → **open** |
| 5 | 93.1 / 1.5 / 82.4 / 48.0 → **open** | 93.3 / 1.8 / 82.7 / 47.9 → **open** |
| 6 | 92.9 / 2.2 / 81.7 / 48.6 → **open** | 93.2 / 2.9 / 82.4 / 48.9 → **open** |
| 7 | 40.7 / 81.7 / 3.7 / 84.0 → **closed** | 92.8 / 2.7 / 82.0 / 48.8 → **open** |
| 8 | 50.7 / 80.0 / 26.0 / 89.3 → **next to FERM (not closed)** | 94.1 / 3.0 / 83.3 / 48.4 → **open** |
| 9 | 45.9 / 87.5 / 21.9 / 94.0 → **next to FERM (not closed)** | 93.9 / 2.7 / 83.5 / 47.4 → **open** |
| 10 | 92.9 / 1.4 / 81.8 / 48.0 → **open** | 84.1 / 43.5 / 81.0 / 5.6 → **7T6F-like** |
| 11 | 93.0 / 2.3 / 81.9 / 48.7 → **open** | 50.6 / 86.8 / 30.3 / 95.9 → **next to FERM (not closed)** |
| 12 | 93.3 / 1.8 / 82.2 / 48.4 → **open** | 83.8 / 43.7 / 80.9 / 5.3 → **7T6F-like** |
| 13 | 41.5 / 82.6 / 4.2 / 85.0 → **closed** | 84.2 / 42.5 / 80.6 / 6.6 → **7T6F-like** |
| 14 | 44.8 / 84.3 / 15.1 / 89.7 → **next to FERM (not closed)** | 83.9 / 43.8 / 80.8 / 5.4 → **7T6F-like** |

## Trajectories (V658F)

Most V658F seeds start next to FERM at recycles 1–2 (FERM–JH1 39–60 Å), as wild type does, but leave it: 9 go open by
recycles 2–4, and 4 (seeds 10, 12, 13, 14) stay near FERM for 3–6 recycles and then move to the 7T6F-like arrangement
(FERM–JH1 ~84 Å) and stay there. Per-seed tables: the run's conclusions.md.

## MSA 96/384 (V658F 16 seeds, wild type 5 seeds)

| final state | wild type ([JAK1_20261015_135849](runs/JAK1_20261015_135849)) | **V658F ([JAK1_V658F_20261015_175956](runs/JAK1_V658F_20261015_175956))** |
|---|--:|--:|
| **7T6F-like** (active dimer) | 2 | **16** (4.8–6.5 Å from 7T6F) |
| next to FERM | 3 | 0 |
| open / closed | 0 / 0 | 0 / 0 |

- **At 96/384 the mutation drives every seed into the 7T6F-like arrangement** (16/16 vs 2/5, Fisher p = 0.0075).
- Together with 128/512 (closed/FERM-bound 7/15 → 1/15; 7T6F-like 1 → 4–5), V658F consistently moves JAK1 away from the
  autoinhibited (closed) arrangement and into the arrangement of the experimental active dimer, which carries the same mutation.

## Caveats
- 15 seeds per condition; only the combined closed + FERM-bound difference is significant (p = 0.035).
- MSAs were computed separately for the mutant and wild-type query (7576 vs 7390 sequences, same ColabFold search).
- 7T6F is mouse JAK1 V657F in a receptor-bound dimer; our models are human JAK1 monomers.
