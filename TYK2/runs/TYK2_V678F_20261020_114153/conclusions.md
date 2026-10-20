# TYK2_V678F_20261020_114153 — TYK2 V678F_free_msa96-384_s8-15

TYK2 V678F at MSA 96/384, seeds 8-15, completing n=16 at a second depth. Tests whether the strong 64/256 effect is depth-dependent.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 96 clusters / 384 extra; no template. Run time 77 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 11 | 81.8 | 46.7 | 93.6 | 82.6 | AF2 |
| 9 | 6 | 81.3 | 46.7 | 93.3 | 82.5 | AF2 |
| 10 | 11 | 81.5 | 46.8 | 93.7 | 82.2 | AF2 |
| 11 | 10 | 81.6 | 46.7 | 93.4 | 82.5 | AF2 |
| 12 | 11 | 81.7 | 46.7 | 93.0 | 82.4 | AF2 |
| 13 | 11 | 81.6 | 46.7 | 93.3 | 82.4 | AF2 |
| 14 | 9 | 81.4 | 46.8 | 93.5 | 82.6 | AF2 |
| 15 | 11 | 81.9 | 46.7 | 93.5 | 82.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 41.5 | 15 | 1 | 69.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.5 | 28.0 | 53.9 |
| 2 | 78.8 | 86.2 | 76.9 |
| 3 | 81.1 | 93.4 | 82.7 |
| 4 | 81.1 | 93.1 | 82.7 |
| 5 | 81.4 | 93.2 | 82.5 |
| 6 | 81.4 | 93.2 | 82.8 |
| 7 | 81.3 | 93.3 | 82.6 |
| 8 | 81.3 | 93.2 | 82.5 |
| 9 | 81.4 | 93.2 | 82.5 |
| 10 | 81.4 | 93.5 | 82.8 |
| 11 | 81.5 | 93.4 | 82.4 |
| 12 | 81.4 | 93.5 | 82.5 |
| 13 | 81.3 | 93.6 | 82.6 |
| 14 | 81.2 | 93.4 | 82.4 |
| 15 | 81.2 | 93.5 | 82.6 |

pLDDT 69.0–81.9; JH2–JH1 16.6–52.5 Å; FERM–JH1 11.4–94.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 18 52 94 93 93 93 94 93 93 94 94 94 94 93 93 | open-like (> 80) |
| 9 | 35 94 93 93 93 93 93 93 93 94 93 94 93 93 94 | open-like (> 80) |
| 10 | 34 93 94 93 93 93 93 93 93 93 94 94 94 94 94 | open-like (> 80) |
| 11 | 36 94 93 94 94 94 93 93 93 93 94 94 94 93 94 | open-like (> 80) |
| 12 | 48 94 93 93 93 93 93 93 93 93 93 93 94 93 93 | open-like (> 80) |
| 13 | 29 85 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 14 | 11 82 94 94 94 93 94 94 94 94 93 94 94 94 94 | open-like (> 80) |
| 15 | 14 94 93 93 93 93 93 93 93 94 94 94 94 93 94 | open-like (> 80) |
