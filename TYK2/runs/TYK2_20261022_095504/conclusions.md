# TYK2_20261022_095504 — TYK2 WT_96-384_s8-15__seed9

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 9; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 9 | 5 | 80.6 | 50.0 | 95.0 | 90.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 37.6 | 9 | 1 | 72.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.9 | 49.8 | 37.6 |
| 2 | 77.8 | 36.7 | 40.1 |
| 3 | 80.5 | 64.0 | 71.3 |
| 4 | 80.5 | 88.9 | 93.7 |
| 5 | 80.6 | 95.0 | 90.0 |
| 6 | 80.2 | 94.1 | 85.4 |
| 7 | 80.1 | 94.5 | 86.3 |
| 8 | 80.2 | 94.8 | 87.8 |
| 9 | 79.9 | 94.5 | 85.5 |
| 10 | 80.1 | 94.4 | 85.4 |
| 11 | 79.8 | 94.6 | 86.2 |
| 12 | 80.0 | 94.5 | 85.8 |
| 13 | 80.1 | 94.3 | 86.4 |
| 14 | 80.0 | 94.8 | 86.5 |
| 15 | 80.0 | 94.7 | 87.6 |

pLDDT 72.9–80.6; JH2–JH1 47.8–53.7 Å; FERM–JH1 36.7–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 9 | 50 37 64 89 95 94 94 95 94 94 95 94 94 95 95 | open-like (> 80) |
