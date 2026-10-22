# TYK2_20261022_114338 — TYK2 WT_96-384_s16-23__seed17

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 17; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 17 | 13 | 81.2 | 46.5 | 93.1 | 82.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 27.2 | 17 | 1 | 73.3 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 73.3 | 34.1 | 27.2 |
| 2 | 77.8 | 33.4 | 35.6 |
| 3 | 80.8 | 83.7 | 86.9 |
| 4 | 81.0 | 94.7 | 86.6 |
| 5 | 80.6 | 93.3 | 83.5 |
| 6 | 80.7 | 93.7 | 84.4 |
| 7 | 80.9 | 93.5 | 83.7 |
| 8 | 80.8 | 93.4 | 83.8 |
| 9 | 81.1 | 93.1 | 83.5 |
| 10 | 81.1 | 93.4 | 82.6 |
| 11 | 81.0 | 93.8 | 83.2 |
| 12 | 80.9 | 93.2 | 82.9 |
| 13 | 81.2 | 93.1 | 82.4 |
| 14 | 80.8 | 93.3 | 82.3 |
| 15 | 81.1 | 93.3 | 82.5 |

pLDDT 73.3–81.2; JH2–JH1 46.5–55.3 Å; FERM–JH1 33.4–94.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 17 | 34 33 84 95 93 94 94 93 93 93 94 93 93 93 93 | open-like (> 80) |
