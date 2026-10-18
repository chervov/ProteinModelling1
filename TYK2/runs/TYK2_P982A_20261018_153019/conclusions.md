# TYK2_P982A_20261018_153019 — TYK2 P982A_free_msa32-64_s8-15

TYK2 P982A, NO template, MSA 32/64, seeds 8–15: second half of TYK2_P982A_20261018_135623 (seeds 0–6; seed 7 lost when that sandbox was terminated), giving 15 seeds per arm. Paired with wild type TYK2_20261018_153027 (seeds 8–15, run at the same time).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 32 clusters / 64 extra; no template. Run time ~100 min (whole notebook incl. setup, fresh molab sandbox).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 11 | 76.9 | 57.8 | 42.0 | 54.5 | AF2 |
| 9 | 14 | 77.3 | 47.4 | 38.4 | 52.0 | AF2 |
| 10 | 13 | 79.1 | 50.8 | 53.9 | 36.4 | AF2 |
| 11 | 13 | 77.7 | 53.5 | 46.3 | 40.9 | AF2 |
| 12 | 12 | 77.6 | 45.2 | 37.7 | 46.5 | AF2 |
| 13 | 14 | 79.1 | 55.2 | 44.3 | 45.7 | AF2 |
| 14 | 12 | 76.9 | 59.6 | 36.4 | 49.6 | AF2 |
| 15 | 15 | 77.3 | 48.3 | 40.0 | 33.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 28.1 | 8 | 1 | 59.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 58.4 | 52.9 | 44.0 |
| 2 | 67.8 | 58.7 | 45.9 |
| 3 | 70.6 | 54.2 | 47.8 |
| 4 | 72.1 | 50.6 | 48.9 |
| 5 | 73.9 | 47.3 | 49.1 |
| 6 | 74.6 | 44.9 | 49.9 |
| 7 | 75.6 | 43.3 | 47.8 |
| 8 | 76.0 | 43.7 | 48.3 |
| 9 | 76.4 | 42.9 | 48.2 |
| 10 | 75.0 | 40.7 | 47.3 |
| 11 | 76.6 | 42.7 | 48.1 |
| 12 | 76.5 | 42.8 | 49.2 |
| 13 | 77.4 | 43.0 | 45.2 |
| 14 | 77.6 | 41.3 | 46.0 |
| 15 | 77.2 | 40.4 | 44.1 |

pLDDT 53.4–79.1; JH2–JH1 43.0–67.9 Å; FERM–JH1 29.6–71.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 58 64 71 59 48 43 42 42 42 33 42 36 41 39 39 | closed-like (< 50) |
| 9 | 54 62 58 48 43 43 42 42 40 43 38 42 41 38 40 | closed-like (< 50) |
| 10 | 54 53 44 43 43 48 48 51 52 51 53 56 54 51 50 | closed-like (< 50) |
| 11 | 51 57 46 46 47 46 45 48 47 44 51 49 46 44 44 | closed-like (< 50) |
| 12 | 60 67 50 46 41 39 39 38 40 40 38 38 38 37 38 | closed-like (< 50) |
| 13 | 59 57 49 43 39 38 39 41 40 41 39 41 46 44 34 | closed-like (< 50) |
| 14 | 57 57 64 56 51 43 42 40 38 38 38 36 37 36 38 | closed-like (< 50) |
| 15 | 30 51 51 64 67 59 49 48 44 36 41 45 41 40 40 | closed-like (< 50) |

## Combined: wild type vs P982A at 32/64, 15 seeds per arm

Runs: wild type TYK2_20261018_135623 (seeds 0–6) + TYK2_20261018_153027 (seeds 8–15);
P982A TYK2_P982A_20261018_135623 (seeds 0–6) + TYK2_P982A_20261018_153019 (seeds 8–15). Seed 7 of the first pair was lost
when both sandboxes were terminated.

| | compact (< 60 Å) | median FERM–JH1 (range) | median JH2–JH1 (range) | JH2–JH1 median, 1st / 2nd half |
|---|--:|---|---|---|
| wild type | 15/15 | 45.2 (38.4–52.3) | 49.3 (41.4–60.2) | 43.1 / 51.6 |
| P982A | 15/15 | 42.4 (36.4–53.9) | 53.5 (43.7–63.3) | 53.5 / 52.1 |

P982A vs wild type, Mann-Whitney: FERM–JH1 p = 0.10; JH2–JH1 p = 0.097.

**Conclusion: at 32/64 TYK2 is compact in all 30 seeds, and P982A has no significant effect on either distance.**
The borderline JH2–JH1 difference seen with seeds 0–6 (p = 0.058) does not hold up: it came mostly from a low first half of
wild type (median 43.1 vs 51.6 Å in its second half), while P982A was the same in both halves. If anything P982A is
slightly *more* compact in FERM–JH1 (median 42.4 vs 45.2 Å, not significant).

## TYK2 MSA-depth scan (selected FERM–JH1 state per seed)

| depth | wild type | P982A | P982A vs wild type |
|---|---|---|---|
| 32/64 | 15/15 compact | 15/15 compact | FERM–JH1 p = 0.10, JH2–JH1 p = 0.097 |
| 64/256 | 7/16 compact, 8/16 extended | 3/16 compact, 13/16 extended | Mann-Whitney p = 0.27 |
| 128/512 | 8/8 extended | 8/8 extended | 0.5 Å shift within the extended state |

Across the scan, P982A does not change TYK2's FERM–JH1 state at any depth. Wild type switches from compact (32/64) through
mixed (64/256) to extended (128/512); P982A follows the same switch, leaning extended only in the mixed regime (not
significant). In this assay P982A shows none of the opening that JAK3 M592F showed at JAK3's compact depth (5/16 open, p = 0.011).
