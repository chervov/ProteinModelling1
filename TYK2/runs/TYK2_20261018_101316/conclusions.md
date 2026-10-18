# TYK2_20261018_101316 — TYK2 WT_free_msa64-256_s8-15

TYK2 wild type, NO template, MSA 64/256, seeds 8–15: second half of TYK2_20261018_084732 (seeds 0–7), to reach 16 seeds per arm. Paired with P982A TYK2_P982A_20261018_101316 (seeds 8–15, run at the same time).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time ~75 min (inference only; setup reused from the seeds 0–7 run in the same sandbox).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 12 | 80.9 | 50.6 | 94.7 | 91.4 | AF2 |
| 9 | 6 | 81.1 | 50.5 | 93.2 | 92.0 | AF2 |
| 10 | 14 | 80.7 | 47.6 | 94.3 | 84.7 | AF2 |
| 11 | 6 | 80.8 | 50.0 | 94.4 | 90.1 | AF2 |
| 12 | 12 | 81.0 | 51.2 | 91.0 | 92.0 | AF2 |
| 13 | 8 | 80.8 | 51.8 | 89.7 | 91.0 | AF2 |
| 14 | 8 | 80.3 | 46.9 | 50.2 | 41.2 | AF2 |
| 15 | 7 | 80.9 | 49.5 | 83.0 | 84.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 34.8 | 15 | 2 | 75.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 68.6 | 50.4 | 46.1 |
| 2 | 76.3 | 38.2 | 38.4 |
| 3 | 79.7 | 45.1 | 46.9 |
| 4 | 80.3 | 54.9 | 57.8 |
| 5 | 80.4 | 70.5 | 72.8 |
| 6 | 80.6 | 73.9 | 74.4 |
| 7 | 80.6 | 83.9 | 79.4 |
| 8 | 80.6 | 86.0 | 82.1 |
| 9 | 80.3 | 88.9 | 84.0 |
| 10 | 80.5 | 88.4 | 84.6 |
| 11 | 80.4 | 89.1 | 84.0 |
| 12 | 80.6 | 88.5 | 83.7 |
| 13 | 80.5 | 89.0 | 85.0 |
| 14 | 80.4 | 89.4 | 81.8 |
| 15 | 80.2 | 89.7 | 84.3 |

pLDDT 67.8–81.1; JH2–JH1 46.5–66.6 Å; FERM–JH1 34.3–96.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 44 34 44 52 84 95 95 94 95 93 95 95 95 95 96 | open-like (> 80) |
| 9 | 54 39 44 61 89 93 95 95 94 95 95 95 94 95 95 | open-like (> 80) |
| 10 | 48 37 47 57 72 79 95 94 94 95 95 94 95 94 94 | open-like (> 80) |
| 11 | 46 36 44 62 91 94 94 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 12 | 54 38 47 50 55 60 72 76 92 90 91 91 93 95 94 | open-like (> 80) |
| 13 | 60 41 48 62 72 65 89 90 95 95 96 95 96 95 96 | open-like (> 80) |
| 14 | 52 41 43 47 49 47 46 50 50 51 51 49 51 51 52 | intermediate |
| 15 | 46 40 43 47 53 56 83 94 95 93 95 94 94 95 96 | open-like (> 80) |

## Combined: wild type vs P982A at 64/256, 16 seeds per arm

Runs: wild type TYK2_20261018_084732 (seeds 0–7) + TYK2_20261018_101316 (seeds 8–15);
P982A TYK2_P982A_20261018_084539 (seeds 0–7) + TYK2_P982A_20261018_101316 (seeds 8–15). Selected FERM–JH1 per seed (Å):

| | seeds 0–7 | seeds 8–15 | median | compact (< 60 Å) | extended (> 80 Å) |
|---|---|---|--:|--:|--:|
| wild type | 40 57 56 77 87 34 57 51 | 95 93 94 94 91 90 50 83 | 80.0 | 7/16 (6/8 + 1/8) | 8/16 |
| P982A | 53 86 92 86 94 46 50 89 | 85 93 96 91 85 90 95 94 | 89.5 | 3/16 (3/8 + 0/8) | 13/16 |

P982A vs wild type: Mann-Whitney p = 0.27; Fisher on compact counts p = 0.25; Fisher on extended counts p = 0.14.
Wild type seeds 0–7 vs 8–15: 6/8 vs 1/8 compact, Fisher p = 0.041.

**Conclusion: no significant effect of P982A at 64/256 with 16 seeds per arm.** P982A leans towards the extended state
(13/16 vs 8/16 extended; no P982A seed in the second half is compact), but the difference is not significant.

**Correction of the seeds 0–7 reading:** after the first half, wild type looked mostly compact at 64/256 (6/8). The second
half is mostly extended (7/8), so wild type at 64/256 is genuinely mixed (7/16 compact, 8/16 extended): this depth sits on
TYK2's switch between the compact and extended basins, rather than below it. The two halves of the same wild-type
condition differ more (p = 0.041) than P982A differs from wild type, the same kind of half-to-half heterogeneity flagged
for JAK3 A572V; 8-seed batches are not reliable estimates of the state fraction here.

Next options: a shallower depth (32/64 or 48/192) where wild type should be compact in nearly all seeds, which is the
condition under which the JAK3 mutations separated cleanly from wild type; or more seeds at 64/256 (32 per arm) if the
mixed regime itself is the object of study.
