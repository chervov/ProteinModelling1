# TYK2_P982A_20261018_101316 — TYK2 P982A_free_msa64-256_s8-15

TYK2 P982A, NO template, MSA 64/256, seeds 8–15: second half of TYK2_P982A_20261018_084539 (seeds 0–7), to reach 16 seeds per arm. Paired with wild type TYK2_20261018_101316 (seeds 8–15, run at the same time).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time ~75 min (inference only; setup reused from the seeds 0–7 run in the same sandbox).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 5 | 80.8 | 49.2 | 84.8 | 86.0 | AF2 |
| 9 | 13 | 80.8 | 50.6 | 92.8 | 92.2 | AF2 |
| 10 | 13 | 80.7 | 49.4 | 95.5 | 88.3 | AF2 |
| 11 | 8 | 80.7 | 51.5 | 90.9 | 94.4 | AF2 |
| 12 | 12 | 80.9 | 47.6 | 84.5 | 89.9 | AF2 |
| 13 | 4 | 80.7 | 52.1 | 89.6 | 95.2 | AF2 |
| 14 | 9 | 80.7 | 49.4 | 94.5 | 89.2 | AF2 |
| 15 | 11 | 80.5 | 48.9 | 94.4 | 87.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 15.2 | 10 | 1 | 60.3 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 65.0 | 57.7 | 34.2 |
| 2 | 76.2 | 42.8 | 41.3 |
| 3 | 79.3 | 56.5 | 60.7 |
| 4 | 80.2 | 65.5 | 70.0 |
| 5 | 80.5 | 77.7 | 82.4 |
| 6 | 80.4 | 84.2 | 88.2 |
| 7 | 80.4 | 89.6 | 92.1 |
| 8 | 80.6 | 91.8 | 92.0 |
| 9 | 80.5 | 92.6 | 91.0 |
| 10 | 80.2 | 93.7 | 90.3 |
| 11 | 80.5 | 92.3 | 90.9 |
| 12 | 80.6 | 92.5 | 88.5 |
| 13 | 80.5 | 93.1 | 89.8 |
| 14 | 79.9 | 93.2 | 88.2 |
| 15 | 80.3 | 93.9 | 87.6 |

pLDDT 60.2–80.9; JH2–JH1 40.4–61.2 Å; FERM–JH1 35.7–95.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 57 40 48 52 85 95 95 95 95 96 95 95 96 95 95 | open-like (> 80) |
| 9 | 47 53 41 48 60 85 92 93 93 93 92 93 93 95 95 | open-like (> 80) |
| 10 | 72 55 49 56 64 70 79 85 93 95 94 95 95 94 95 | open-like (> 80) |
| 11 | 56 41 45 52 78 89 90 91 92 93 93 91 92 93 94 | open-like (> 80) |
| 12 | 56 36 73 84 89 89 90 88 86 88 84 85 87 87 92 | open-like (> 80) |
| 13 | 59 39 78 90 94 91 92 94 93 94 91 93 94 94 93 | open-like (> 80) |
| 14 | 59 42 50 53 59 62 84 95 94 95 95 94 95 94 94 | open-like (> 80) |
| 15 | 55 38 68 89 94 93 94 93 94 95 94 94 94 94 94 | open-like (> 80) |

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
