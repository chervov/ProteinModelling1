# TYK2_V678F_20261019_102630 — TYK2 V678F_free_msa64-256_s8-15

TYK2 V678F, MSA 64/256, seeds 8-15, completing the 8-seed run TYK2_V678F_20261018_165935 to n=16. V678F is the reported activating substitution; at this depth its first 8 seeds were confined to 90.7-94.8 A from the closed arrangement while wild type ranged 41.2-92.0 A (Mann-Whitney p=0.0008). Replication to 16 seeds matters because the JAK3 A572V result weakened from p=0.0009 to p=0.035 when its second half arrived.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 152 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 6 | 80.6 | 52.7 | 92.9 | 94.7 | AF2 |
| 9 | 6 | 81.0 | 53.6 | 92.1 | 96.1 | AF2 |
| 10 | 4 | 80.6 | 50.9 | 84.2 | 93.0 | AF2 |
| 11 | 6 | 80.1 | 54.6 | 85.3 | 95.4 | AF2 |
| 12 | 10 | 80.7 | 48.4 | 94.9 | 85.6 | AF2 |
| 13 | 6 | 80.1 | 50.7 | 93.4 | 92.6 | AF2 |
| 14 | 7 | 80.2 | 50.5 | 94.9 | 91.0 | AF2 |
| 15 | 4 | 80.2 | 50.0 | 91.8 | 90.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 29.6 | 14 | 1 | 66.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 66.6 | 51.2 | 57.0 |
| 2 | 76.1 | 45.1 | 48.2 |
| 3 | 79.6 | 58.1 | 60.6 |
| 4 | 80.3 | 82.1 | 88.6 |
| 5 | 80.1 | 91.7 | 93.6 |
| 6 | 80.3 | 92.8 | 92.8 |
| 7 | 80.2 | 94.0 | 90.9 |
| 8 | 80.1 | 94.5 | 90.2 |
| 9 | 80.2 | 93.5 | 91.4 |
| 10 | 80.3 | 94.5 | 89.0 |
| 11 | 80.1 | 94.6 | 89.2 |
| 12 | 80.1 | 94.8 | 89.5 |
| 13 | 80.1 | 94.4 | 89.2 |
| 14 | 80.1 | 94.2 | 88.6 |
| 15 | 80.1 | 94.7 | 86.8 |

pLDDT 65.5–81.0; JH2–JH1 39.7–58.3 Å; FERM–JH1 36.0–95.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 49 45 63 86 93 93 95 95 94 95 95 95 95 95 95 | open-like (> 80) |
| 9 | 51 38 45 82 92 92 90 93 91 94 93 95 93 92 95 | open-like (> 80) |
| 10 | 51 36 56 84 93 93 94 93 90 92 94 93 93 95 94 | open-like (> 80) |
| 11 | 50 49 51 68 84 85 93 94 92 94 94 94 94 94 95 | open-like (> 80) |
| 12 | 50 45 71 91 95 95 95 95 96 95 95 95 95 94 94 | open-like (> 80) |
| 13 | 51 48 46 65 86 93 96 96 95 95 95 96 95 95 95 | open-like (> 80) |
| 14 | 58 51 61 89 95 95 95 95 95 95 95 95 95 94 95 | open-like (> 80) |
| 15 | 50 49 73 92 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
