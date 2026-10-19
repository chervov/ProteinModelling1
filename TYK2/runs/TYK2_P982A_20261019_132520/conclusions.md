# TYK2_P982A_20261019_132520 — TYK2 P982A_free_msa96-384_s0-7

TYK2 P982A at MSA 96/384, pairing with wild type TYK2_20261019_101530 at the same depth (median 82.5 A from closed, spread 8.8 A). P982A showed no effect at 128/512, 64/256 or 32/64; this fills the remaining depth.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 96 clusters / 384 extra; no template. Run time 82 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 7 | 81.2 | 45.9 | 85.8 | 80.0 | AF2 |
| 1 | 5 | 80.6 | 50.1 | 93.5 | 90.7 | AF2 |
| 2 | 10 | 81.4 | 46.7 | 93.5 | 82.5 | AF2 |
| 3 | 7 | 81.3 | 46.5 | 87.3 | 81.9 | AF2 |
| 4 | 6 | 81.2 | 48.6 | 88.7 | 90.6 | AF2 |
| 5 | 13 | 80.7 | 46.2 | 87.5 | 82.8 | AF2 |
| 6 | 7 | 81.5 | 44.7 | 86.6 | 78.3 | AF2 |
| 7 | 14 | 81.3 | 49.4 | 89.3 | 91.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 6.5 | 6 | 2 | 77.7 | 4 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.1 | 25.5 | 29.9 |
| 2 | 78.3 | 35.9 | 19.4 |
| 3 | 80.0 | 67.2 | 58.7 |
| 4 | 80.7 | 87.7 | 84.1 |
| 5 | 80.8 | 90.1 | 86.0 |
| 6 | 80.8 | 89.3 | 84.7 |
| 7 | 81.0 | 90.2 | 83.6 |
| 8 | 80.8 | 88.9 | 84.1 |
| 9 | 80.8 | 89.8 | 84.9 |
| 10 | 80.8 | 88.9 | 84.2 |
| 11 | 80.9 | 89.8 | 84.1 |
| 12 | 80.9 | 89.7 | 83.8 |
| 13 | 81.0 | 90.9 | 84.8 |
| 14 | 80.9 | 89.6 | 84.3 |
| 15 | 80.9 | 90.0 | 84.4 |

pLDDT 70.0–81.5; JH2–JH1 31.4–50.9 Å; FERM–JH1 15.5–95.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 27 35 44 85 86 86 86 86 86 85 86 84 86 86 86 | open-like (> 80) |
| 1 | 23 40 64 86 94 95 95 95 95 94 95 95 95 95 95 | open-like (> 80) |
| 2 | 25 38 85 95 95 94 94 93 94 94 94 94 94 94 94 | open-like (> 80) |
| 3 | 16 35 62 89 90 89 87 88 90 88 90 89 95 90 88 | open-like (> 80) |
| 4 | 27 34 76 88 90 89 95 89 93 92 93 95 94 94 91 | open-like (> 80) |
| 5 | 38 36 59 87 88 88 88 86 87 86 86 87 88 85 87 | open-like (> 80) |
| 6 | 27 34 74 85 85 87 87 85 85 85 85 85 86 85 85 | open-like (> 80) |
| 7 | 22 36 74 86 93 88 90 88 89 88 88 90 90 89 94 | open-like (> 80) |
