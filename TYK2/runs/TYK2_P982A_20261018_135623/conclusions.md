# TYK2_P982A_20261018_135623 — TYK2 P982A_free_msa32-64_s0-6 (s7 lost)

TYK2 P982A, NO template, MSA 32/64, seeds 0–7 launched; 7 completed (seeds 0–6). The molab sandbox was terminated at ~17:05 (about 6.5 h after it was created) during seed 7, before the notebook's selection and save steps, so this folder was rebuilt from the monitor's incremental backup: every recycle of seeds 0–6 is complete, but there is no pipeline selection_report.json / selected_open / selected_closed. Paired with wild type TYK2_20261018_135623 (same settings, same fate). Follow-up to the 64/256 pair, where wild type was mixed (7/16 compact).

Settings: OpenFold model_1, guided recycling, 15 recycles; MSA 32 clusters / 64 extra; no template.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 76.0 | 57.3 | 45.7 | 34.7 | AF2 |
| 1 | 15 | 77.8 | 51.7 | 46.8 | 41.7 | AF2 |
| 2 | 9 | 74.4 | 63.3 | 42.3 | 43.6 | AF2 |
| 3 | 12 | 75.7 | 57.7 | 45.0 | 44.7 | AF2 |
| 4 | 12 | 77.1 | 53.5 | 45.1 | 38.7 | AF2 |
| 5 | 8 | 78.7 | 43.7 | 42.4 | 48.6 | AF2 |
| 6 | 9 | 77.1 | 49.7 | 37.9 | 49.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 22.9 | 0 | 7 | 72.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 52.6 | 43.1 | 76.7 |
| 2 | 61.0 | 53.1 | 73.8 |
| 3 | 64.9 | 51.7 | 64.7 |
| 4 | 68.8 | 48.8 | 57.7 |
| 5 | 71.0 | 47.7 | 53.3 |
| 6 | 72.6 | 47.7 | 52.7 |
| 7 | 73.8 | 48.3 | 49.4 |
| 8 | 74.7 | 47.7 | 48.0 |
| 9 | 75.6 | 43.4 | 45.1 |
| 10 | 74.7 | 44.6 | 52.7 |
| 11 | 75.9 | 44.2 | 47.2 |
| 12 | 76.4 | 43.5 | 42.8 |
| 13 | 75.9 | 43.8 | 41.6 |
| 14 | 75.6 | 44.5 | 44.8 |
| 15 | 76.2 | 43.2 | 41.9 |

pLDDT 46.6–78.7; JH2–JH1 35.8–66.6 Å; FERM–JH1 28.6–66.7 Å (FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 43 45 47 49 48 47 54 50 46 49 46 46 46 46 45 | closed-like (< 50) |
| 1 | 38 58 46 44 44 44 44 44 44 46 49 49 48 52 47 | closed-like (< 50) |
| 2 | 45 48 49 40 43 49 47 44 42 41 42 42 41 37 40 | closed-like (< 50) |
| 3 | 42 56 61 57 60 54 57 63 47 48 47 45 45 46 44 | closed-like (< 50) |
| 4 | 67 55 53 55 53 55 53 51 47 46 49 45 51 52 49 | closed-like (< 50) |
| 5 | 29 62 58 55 46 47 45 42 41 42 39 40 40 41 40 | closed-like (< 50) |
| 6 | 39 48 47 42 40 38 38 39 38 40 38 38 37 39 38 | closed-like (< 50) |

## Comparison: wild type vs P982A at 32/64 (seeds 0–6 each)

Runs: wild type TYK2_20261018_135623, P982A TYK2_P982A_20261018_135623. Selected structure per seed:

| | FERM–JH1 per seed (Å) | median FERM–JH1 | median JH2–JH1 | compact (< 60 Å) | extended (> 80 Å) |
|---|---|--:|--:|--:|--:|
| wild type | 45 42 47 47 43 50 39 | 45.2 | 43.1 | 7/7 | 0/7 |
| P982A | 46 47 42 45 45 42 38 | 45.0 | 53.5 | 7/7 | 0/7 |

Exact permutation test on medians (7 vs 7; SciPy unavailable after both sandboxes died): FERM–JH1 p = 0.77, JH2–JH1 p = 0.058.

**Conclusion: at 32/64 TYK2 wild type is compact in every completed seed, and P982A does not open it.**

- Both arms sit entirely in the compact FERM–JH1 basin (38–50 Å, close to the closed reference ~40 Å and to AF2 TYK2 39.7 Å).
- P982A does not shift FERM–JH1 at all (median 45.0 vs 45.2 Å).
- JH2–JH1 is larger in P982A (median 53.5 vs 43.1 Å; p = 0.058, borderline with 7 per arm): a possible loosening of the
  JH2–JH1 contact without leaving the compact state, worth checking with more seeds.
- Confidence is lower at this depth (selected pLDDT 73–79, vs ~80–82 at 64/256 and 128/512).

## TYK2 MSA-depth scan so far (selected FERM–JH1 state per seed)

| depth | wild type | P982A |
|---|---|---|
| 32/64 | 7/7 compact | 7/7 compact |
| 64/256 | 7/16 compact, 8/16 extended (mixed) | 3/16 compact, 13/16 extended |
| 128/512 | 8/8 extended | 8/8 extended |

The wild-type switch lies between 32/64 and 128/512, with 64/256 in the mixed regime. P982A leans towards the extended state
only where wild type is already mixed (64/256, not significant: Mann-Whitney p = 0.27), and has no effect on the FERM–JH1
state at the compact depth. Unlike JAK3 M592F (which pushed 5/16 seeds open at JAK3's compact depth, p = 0.011), P982A shows
no clear activating-like opening in this assay.
