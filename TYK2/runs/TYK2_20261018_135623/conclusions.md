# TYK2_20261018_135623 — TYK2 WT_free_msa32-64_s0-6 (s7 lost)

TYK2 wild type, NO template, MSA 32/64, seeds 0–7 launched; 7 completed (seeds 0–6). The molab sandbox was terminated at ~17:05 (about 6.5 h after it was created) during seed 7, before the notebook's selection and save steps, so this folder was rebuilt from the monitor's incremental backup: every recycle of seeds 0–6 is complete, but there is no pipeline selection_report.json / selected_open / selected_closed. Paired with P982A TYK2_P982A_20261018_135623 (same settings, same fate). Follow-up to the 64/256 pair, where wild type was mixed (7/16 compact).

Settings: OpenFold model_1, guided recycling, 15 recycles; MSA 32 clusters / 64 extra; no template.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 15 | 77.9 | 54.6 | 45.2 | 41.5 | AF2 |
| 1 | 9 | 79.1 | 45.0 | 41.7 | 45.2 | AF2 |
| 2 | 13 | 77.8 | 42.0 | 46.9 | 47.0 | AF2 |
| 3 | 15 | 73.4 | 51.6 | 46.8 | 35.4 | AF2 |
| 4 | 14 | 77.8 | 41.4 | 42.8 | 45.0 | AF2 |
| 5 | 14 | 74.2 | 41.6 | 49.9 | 46.3 | AF2 |
| 6 | 9 | 78.3 | 43.1 | 38.8 | 46.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 32.8 | 3 | 3 | 62.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 52.6 | 47.7 | 53.5 |
| 2 | 63.4 | 48.1 | 50.2 |
| 3 | 67.2 | 49.2 | 48.0 |
| 4 | 70.5 | 47.6 | 50.3 |
| 5 | 71.5 | 47.3 | 50.7 |
| 6 | 72.5 | 46.4 | 47.5 |
| 7 | 74.4 | 45.9 | 46.4 |
| 8 | 74.4 | 45.3 | 44.4 |
| 9 | 75.6 | 44.3 | 44.3 |
| 10 | 75.9 | 44.0 | 44.4 |
| 11 | 76.1 | 44.2 | 44.2 |
| 12 | 75.3 | 42.1 | 44.5 |
| 13 | 76.2 | 43.8 | 44.3 |
| 14 | 76.6 | 44.1 | 43.7 |
| 15 | 76.5 | 43.9 | 44.0 |

pLDDT 38.5–79.1; JH2–JH1 40.0–64.6 Å; FERM–JH1 35.4–63.0 Å (FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 46 40 43 43 42 40 42 43 42 42 43 42 44 45 45 | closed-like (< 50) |
| 1 | 47 52 45 41 42 42 44 43 42 40 41 40 40 40 39 | closed-like (< 50) |
| 2 | 52 47 59 60 63 62 51 52 51 47 48 48 47 43 44 | closed-like (< 50) |
| 3 | 35 51 48 46 43 43 45 45 46 46 46 40 45 47 47 | closed-like (< 50) |
| 4 | 52 48 50 49 48 48 48 45 42 45 43 38 43 43 40 | closed-like (< 50) |
| 5 | 52 50 57 52 49 48 49 48 49 48 48 47 49 50 53 | intermediate |
| 6 | 50 48 44 42 43 43 42 41 39 40 40 39 38 41 40 | closed-like (< 50) |

## Comparison: wild type vs P982A at 32/64 (seeds 0–6 each)

Runs: wild type TYK2_20261018_135623, P982A TYK2_P982A_20261018_135623. Selected structure per seed:

| | FERM–JH1 per seed (Å) | median FERM–JH1 | median JH2–JH1 | compact (< 60 Å) | extended (> 80 Å) |
|---|---|--:|--:|--:|--:|
| wild type | 45 42 47 47 43 50 39 | 45.2 | 43.1 | 7/7 | 0/7 |
| P982A | 46 47 42 45 45 42 38 | 45.0 | 53.5 | 7/7 | 0/7 |

Exact permutation test on medians (7 vs 7; SciPy unavailable after both sandboxes died): FERM–JH1 p = 0.77, JH2–JH1 p = 0.058.

> **Update (2026-10-18):** with seeds 8–15 added (TYK2_20261018_153027 / TYK2_P982A_20261018_153019; 15 per arm) the JH2–JH1 difference is not significant (Mann-Whitney p = 0.097; first-half wild type was unusually low, 43.1 vs 51.6 Å in its second half). All 30 seeds are compact. See the combined section in TYK2_20261018_153027/conclusions.md.

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
