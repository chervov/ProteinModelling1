# TYK2_20261022_103016 — TYK2 WT_96-384_s8-15__seed12

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 12; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 12 | 8 | 81.1 | 47.0 | 93.7 | 82.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 42.5 | 12 | 2 | 78.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.8 | 35.5 | 52.0 |
| 2 | 78.6 | 42.4 | 42.5 |
| 3 | 79.9 | 93.9 | 91.7 |
| 4 | 80.3 | 94.5 | 85.5 |
| 5 | 80.5 | 93.4 | 83.8 |
| 6 | 80.5 | 93.4 | 83.1 |
| 7 | 80.6 | 93.3 | 82.6 |
| 8 | 81.1 | 93.7 | 82.8 |
| 9 | 80.6 | 93.8 | 83.1 |
| 10 | 80.6 | 93.6 | 83.6 |
| 11 | 80.5 | 93.6 | 82.7 |
| 12 | 80.8 | 93.7 | 83.0 |
| 13 | 81.0 | 93.9 | 83.2 |
| 14 | 80.6 | 93.4 | 82.7 |
| 15 | 80.6 | 93.8 | 83.0 |

pLDDT 70.8–81.1; JH2–JH1 46.7–50.8 Å; FERM–JH1 35.5–94.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 12 | 36 42 94 94 93 93 93 94 94 94 94 94 94 93 94 | open-like (> 80) |
