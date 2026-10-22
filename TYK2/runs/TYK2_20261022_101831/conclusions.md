# TYK2_20261022_101831 — TYK2 WT_96-384_s8-15__seed11

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 11; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 11 | 13 | 81.1 | 46.9 | 93.6 | 82.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 42.1 | 11 | 1 | 70.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.2 | 44.1 | 42.1 |
| 2 | 78.9 | 57.5 | 70.4 |
| 3 | 80.6 | 88.6 | 94.5 |
| 4 | 80.7 | 95.1 | 87.7 |
| 5 | 80.4 | 94.2 | 84.8 |
| 6 | 80.8 | 93.8 | 83.8 |
| 7 | 80.6 | 93.5 | 83.0 |
| 8 | 80.6 | 93.5 | 83.0 |
| 9 | 81.0 | 93.5 | 82.9 |
| 10 | 81.1 | 93.8 | 83.1 |
| 11 | 80.9 | 93.7 | 82.8 |
| 12 | 81.0 | 93.6 | 82.7 |
| 13 | 81.1 | 93.6 | 82.6 |
| 14 | 80.3 | 93.5 | 82.6 |
| 15 | 80.8 | 93.5 | 82.2 |

pLDDT 70.2–81.1; JH2–JH1 44.5–63.7 Å; FERM–JH1 44.1–95.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 11 | 44 58 89 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
