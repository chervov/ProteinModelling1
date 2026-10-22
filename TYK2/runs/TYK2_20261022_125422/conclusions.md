# TYK2_20261022_125422 — TYK2 WT_96-384_s16-23__seed23

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 23; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 23 | 15 | 81.1 | 46.9 | 94.0 | 83.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 52.2 | 23 | 2 | 79.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.7 | 44.7 | 55.9 |
| 2 | 79.5 | 52.9 | 52.2 |
| 3 | 81.0 | 91.5 | 89.9 |
| 4 | 81.0 | 94.9 | 85.2 |
| 5 | 80.7 | 94.1 | 84.0 |
| 6 | 80.8 | 94.1 | 83.4 |
| 7 | 80.7 | 94.0 | 83.8 |
| 8 | 80.8 | 94.0 | 83.1 |
| 9 | 80.8 | 93.8 | 83.2 |
| 10 | 80.9 | 93.9 | 83.7 |
| 11 | 80.7 | 94.2 | 84.2 |
| 12 | 80.4 | 93.7 | 83.2 |
| 13 | 80.9 | 93.4 | 82.9 |
| 14 | 80.7 | 93.8 | 83.4 |
| 15 | 81.1 | 94.0 | 83.2 |

pLDDT 72.7–81.1; JH2–JH1 44.5–49.8 Å; FERM–JH1 44.7–94.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 23 | 45 53 92 95 94 94 94 94 94 94 94 94 93 94 94 | open-like (> 80) |
