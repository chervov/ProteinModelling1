# TYK2_V678F_20261020_183512 — TYK2 V678F_free_msa64-256_s16-23

TYK2 V678F at 64/256, seeds 16-23, paired with the wild-type run above on the same seeds. Extends the 64/256 comparison from n=16 to n=24. This is the strongest result in the project - V678F abolishes wild type's partial approaches to the closed arrangement, p = 0.00012 - and three earlier results in this campaign weakened when their second half arrived (A572V 0.0009 to 0.035; R657Q lost significance), so deepening the headline comparison is worth the GPU time.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 16,17,18,19,20,21,22,23; MSA 64 clusters / 256 extra; no template. Run time 79 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 16 | 5 | 80.6 | 49.7 | 95.0 | 88.6 | AF2 |
| 17 | 6 | 80.7 | 47.5 | 94.4 | 83.4 | AF2 |
| 18 | 5 | 80.3 | 48.3 | 94.7 | 85.7 | AF2 |
| 19 | 14 | 80.6 | 47.2 | 93.9 | 83.5 | AF2 |
| 20 | 5 | 80.7 | 51.3 | 95.5 | 92.1 | AF2 |
| 21 | 5 | 80.5 | 51.8 | 95.8 | 92.7 | AF2 |
| 22 | 6 | 80.8 | 47.1 | 93.4 | 83.5 | AF2 |
| 23 | 14 | 80.2 | 49.6 | 95.4 | 88.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 31.7 | 18 | 3 | 78.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 63.6 | 50.2 | 76.2 |
| 2 | 75.2 | 46.6 | 48.4 |
| 3 | 79.3 | 58.7 | 61.7 |
| 4 | 80.4 | 91.0 | 88.2 |
| 5 | 80.4 | 94.7 | 87.3 |
| 6 | 80.4 | 94.6 | 85.7 |
| 7 | 80.3 | 94.2 | 84.0 |
| 8 | 80.2 | 94.8 | 86.3 |
| 9 | 80.2 | 94.4 | 85.0 |
| 10 | 80.1 | 94.4 | 84.7 |
| 11 | 80.1 | 94.4 | 84.1 |
| 12 | 79.9 | 94.3 | 85.6 |
| 13 | 79.9 | 94.7 | 85.4 |
| 14 | 80.4 | 94.7 | 86.0 |
| 15 | 80.3 | 94.2 | 84.5 |

pLDDT 62.9–80.8; JH2–JH1 44.1–64.8 Å; FERM–JH1 35.6–95.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 16 | 42 38 40 92 95 95 94 95 94 94 94 94 95 95 94 | open-like (> 80) |
| 17 | 51 44 75 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 18 | 47 50 38 94 95 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 19 | 46 57 89 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 20 | 56 50 47 89 96 96 95 95 95 96 95 96 96 95 95 | open-like (> 80) |
| 21 | 49 49 48 85 96 96 95 96 95 95 95 95 96 95 95 | open-like (> 80) |
| 22 | 50 36 93 94 94 93 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 23 | 61 48 40 85 95 96 95 96 95 95 95 94 96 95 95 | open-like (> 80) |
