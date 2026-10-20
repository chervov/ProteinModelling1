# TYK2_20261020_153026 — TYK2 WT_free_msa64-256_s16-23

TYK2 wild type at 64/256, seeds 16-23. Extends the 64/256 comparison from n=16 to n=24. This is the strongest result in the project - V678F abolishes wild type's partial approaches to the closed arrangement, p = 0.00012 - and three earlier results in this campaign weakened when their second half arrived (A572V 0.0009 to 0.035; R657Q lost significance), so deepening the headline comparison is worth the GPU time.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 16,17,18,19,20,21,22,23; MSA 64 clusters / 256 extra; no template. Run time 81 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 16 | 15 | 79.8 | 50.7 | 91.0 | 92.4 | AF2 |
| 17 | 15 | 80.5 | 48.1 | 84.4 | 88.8 | AF2 |
| 18 | 15 | 80.0 | 53.9 | 84.0 | 95.6 | AF2 |
| 19 | 8 | 80.1 | 50.3 | 94.1 | 90.9 | AF2 |
| 20 | 15 | 80.1 | 49.8 | 59.6 | 68.8 | AF2 |
| 21 | 4 | 80.3 | 53.4 | 87.8 | 95.6 | AF2 |
| 22 | 6 | 80.0 | 50.3 | 92.5 | 91.4 | AF2 |
| 23 | 15 | 80.2 | 50.2 | 93.6 | 91.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 35.3 | 19 | 2 | 74.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 68.2 | 47.9 | 41.9 |
| 2 | 75.9 | 34.6 | 38.6 |
| 3 | 78.3 | 47.4 | 50.4 |
| 4 | 79.6 | 58.8 | 65.6 |
| 5 | 79.5 | 70.2 | 76.6 |
| 6 | 79.7 | 72.6 | 78.7 |
| 7 | 79.6 | 78.6 | 81.4 |
| 8 | 79.9 | 78.3 | 81.4 |
| 9 | 79.9 | 80.6 | 83.0 |
| 10 | 79.8 | 82.0 | 83.8 |
| 11 | 79.6 | 81.8 | 85.0 |
| 12 | 79.9 | 84.8 | 87.8 |
| 13 | 79.9 | 88.9 | 90.1 |
| 14 | 79.8 | 88.3 | 92.6 |
| 15 | 80.1 | 86.5 | 89.0 |

pLDDT 66.9–80.5; JH2–JH1 41.2–57.2 Å; FERM–JH1 16.6–95.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 16 | 49 37 47 52 59 61 63 64 74 88 88 91 92 90 91 | open-like (> 80) |
| 17 | 48 37 46 48 50 50 53 52 54 53 53 67 80 84 84 | open-like (> 80) |
| 18 | 46 37 42 62 76 80 86 84 85 86 86 86 89 86 84 | open-like (> 80) |
| 19 | 55 17 45 50 66 66 86 94 95 95 94 95 95 94 95 | open-like (> 80) |
| 20 | 56 36 45 52 58 57 61 55 58 57 56 61 75 80 60 | in between |
| 21 | 43 37 56 88 89 88 92 92 92 89 90 88 91 88 90 | open-like (> 80) |
| 22 | 42 37 50 58 77 92 95 95 95 94 94 95 95 94 95 | open-like (> 80) |
| 23 | 44 38 49 62 86 86 94 90 92 94 92 95 94 92 94 | open-like (> 80) |
