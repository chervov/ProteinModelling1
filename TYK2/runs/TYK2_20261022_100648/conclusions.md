# TYK2_20261022_100648 — TYK2 WT_96-384_s8-15__seed10

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 10; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 10 | 4 | 80.6 | 52.1 | 95.0 | 93.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 49.4 | 10 | 1 | 71.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.6 | 41.5 | 49.4 |
| 2 | 78.6 | 49.5 | 55.5 |
| 3 | 80.6 | 89.3 | 96.9 |
| 4 | 80.6 | 95.0 | 93.6 |
| 5 | 80.0 | 94.5 | 85.5 |
| 6 | 80.3 | 95.0 | 86.6 |
| 7 | 80.5 | 94.2 | 84.8 |
| 8 | 80.4 | 94.1 | 84.5 |
| 9 | 80.4 | 93.9 | 83.5 |
| 10 | 80.0 | 94.5 | 86.0 |
| 11 | 80.4 | 94.3 | 84.9 |
| 12 | 80.6 | 95.0 | 87.0 |
| 13 | 80.4 | 94.5 | 85.5 |
| 14 | 80.2 | 94.7 | 85.4 |
| 15 | 80.3 | 94.7 | 86.2 |

pLDDT 71.6–80.6; JH2–JH1 43.5–56.4 Å; FERM–JH1 41.5–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 10 | 42 50 89 95 94 95 94 94 94 94 94 95 94 95 95 | open-like (> 80) |
