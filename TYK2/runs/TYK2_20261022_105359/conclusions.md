# TYK2_20261022_105359 — TYK2 WT_96-384_s8-15__seed14

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 14; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 14 | 9 | 81.4 | 47.0 | 93.8 | 83.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 64.8 | 14 | 1 | 72.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.7 | 48.7 | 64.8 |
| 2 | 78.6 | 79.4 | 86.2 |
| 3 | 80.7 | 95.8 | 89.5 |
| 4 | 80.8 | 95.4 | 87.8 |
| 5 | 81.1 | 94.8 | 86.1 |
| 6 | 81.0 | 94.0 | 84.0 |
| 7 | 81.0 | 94.9 | 84.6 |
| 8 | 81.0 | 94.8 | 84.6 |
| 9 | 81.4 | 93.8 | 83.2 |
| 10 | 81.0 | 93.7 | 83.2 |
| 11 | 81.1 | 93.6 | 83.0 |
| 12 | 81.2 | 93.7 | 83.1 |
| 13 | 81.2 | 93.9 | 83.0 |
| 14 | 80.8 | 93.6 | 82.3 |
| 15 | 81.4 | 93.7 | 82.7 |

pLDDT 72.7–81.4; JH2–JH1 43.2–50.2 Å; FERM–JH1 48.7–95.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 14 | 49 79 96 95 95 94 95 95 94 94 94 94 94 94 94 | open-like (> 80) |
