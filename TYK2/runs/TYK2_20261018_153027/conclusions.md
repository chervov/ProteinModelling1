# TYK2_20261018_153027 — TYK2 WT_free_msa32-64_s8-15

TYK2 wild type, NO template, MSA 32/64, seeds 8–15: second half of TYK2_20261018_135623 (seeds 0–6; seed 7 lost when that sandbox was terminated), giving 15 seeds per arm. Paired with P982A TYK2_P982A_20261018_153019 (seeds 8–15, run at the same time).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 32 clusters / 64 extra; no template. Run time ~100 min (whole notebook incl. setup, fresh molab sandbox).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 15 | 77.0 | 53.8 | 46.3 | 79.7 | AF2 |
| 9 | 14 | 79.5 | 49.3 | 52.3 | 28.2 | AF2 |
| 10 | 15 | 73.4 | 60.2 | 43.4 | 51.3 | AF2 |
| 11 | 15 | 76.8 | 45.5 | 38.4 | 46.4 | AF2 |
| 12 | 14 | 72.7 | 54.3 | 47.9 | 76.3 | AF2 |
| 13 | 13 | 78.7 | 49.4 | 43.9 | 43.3 | AF2 |
| 14 | 8 | 75.2 | 48.7 | 49.0 | 85.6 | AF2 |
| 15 | 14 | 74.6 | 56.1 | 44.6 | 56.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 15.1 | 10 | 2 | 60.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 52.2 | 47.9 | 46.1 |
| 2 | 63.4 | 52.7 | 42.5 |
| 3 | 67.5 | 52.4 | 47.5 |
| 4 | 69.4 | 50.9 | 52.3 |
| 5 | 71.2 | 49.9 | 52.7 |
| 6 | 72.0 | 47.1 | 59.0 |
| 7 | 73.3 | 46.7 | 59.5 |
| 8 | 74.4 | 46.2 | 58.9 |
| 9 | 74.5 | 44.2 | 59.9 |
| 10 | 74.9 | 46.6 | 62.4 |
| 11 | 75.1 | 44.5 | 61.2 |
| 12 | 75.3 | 44.2 | 60.8 |
| 13 | 75.5 | 46.0 | 60.8 |
| 14 | 75.9 | 45.6 | 60.0 |
| 15 | 75.8 | 46.7 | 57.6 |

pLDDT 47.9–79.5; JH2–JH1 32.2–66.1 Å; FERM–JH1 37.0–61.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 43 49 49 49 50 47 46 45 43 46 45 43 46 46 46 | closed-like (< 50) |
| 9 | 41 55 55 55 55 54 51 52 49 53 49 51 55 52 56 | intermediate |
| 10 | 51 56 61 58 56 48 44 45 41 46 42 42 44 44 43 | closed-like (< 50) |
| 11 | 50 54 54 52 54 41 48 45 41 40 41 37 39 37 38 | closed-like (< 50) |
| 12 | 52 54 54 51 50 50 49 48 48 49 48 48 48 48 51 | intermediate |
| 13 | 47 58 56 50 44 44 43 43 43 45 40 39 44 45 44 | closed-like (< 50) |
| 14 | 45 48 46 50 48 49 49 49 47 51 48 49 49 49 49 | closed-like (< 50) |
| 15 | 54 48 45 42 43 43 43 42 41 42 43 44 43 45 45 | closed-like (< 50) |

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
