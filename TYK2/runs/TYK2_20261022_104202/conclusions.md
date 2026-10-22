# TYK2_20261022_104202 — TYK2 WT_96-384_s8-15__seed13

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 13; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 13 | 4 | 81.3 | 50.1 | 94.5 | 90.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 24.6 | 13 | 1 | 70.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.5 | 43.8 | 24.6 |
| 2 | 78.2 | 38.4 | 33.2 |
| 3 | 80.8 | 87.9 | 86.6 |
| 4 | 81.3 | 94.5 | 90.7 |
| 5 | 80.8 | 94.5 | 86.0 |
| 6 | 80.9 | 94.7 | 86.4 |
| 7 | 81.0 | 94.0 | 84.6 |
| 8 | 81.1 | 95.0 | 86.4 |
| 9 | 80.9 | 95.1 | 88.4 |
| 10 | 81.0 | 94.9 | 88.7 |
| 11 | 81.1 | 94.5 | 85.8 |
| 12 | 80.9 | 94.0 | 84.9 |
| 13 | 80.8 | 95.1 | 86.9 |
| 14 | 81.0 | 94.6 | 85.8 |
| 15 | 81.0 | 94.6 | 85.7 |

pLDDT 70.5–81.3; JH2–JH1 45.8–59.0 Å; FERM–JH1 38.4–95.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 13 | 44 38 88 94 94 95 94 95 95 95 94 94 95 95 95 | open-like (> 80) |
