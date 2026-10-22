# TYK2_H582W_20261022_142716 — TYK2 H582W_free_msa96-384_s0-7__seed0

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0; MSA 96 clusters / 384 extra; no template. Run time 16 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 81.0 | 49.1 | 94.5 | 88.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 46.1 | 0 | 2 | 78.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.4 | 50.4 | 76.6 |
| 2 | 78.4 | 53.5 | 46.1 |
| 3 | 80.4 | 61.3 | 61.7 |
| 4 | 80.9 | 91.8 | 89.8 |
| 5 | 80.8 | 95.0 | 87.9 |
| 6 | 80.7 | 94.8 | 86.7 |
| 7 | 80.8 | 94.8 | 86.9 |
| 8 | 80.6 | 94.6 | 85.6 |
| 9 | 81.0 | 94.5 | 88.1 |
| 10 | 80.5 | 94.3 | 85.8 |
| 11 | 80.7 | 93.5 | 83.9 |
| 12 | 80.5 | 93.9 | 84.1 |
| 13 | 80.6 | 94.0 | 84.9 |
| 14 | 80.8 | 94.8 | 85.6 |
| 15 | 80.7 | 94.1 | 85.9 |

pLDDT 70.4–81.0; JH2–JH1 34.7–51.0 Å; FERM–JH1 50.4–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 50 54 61 92 95 95 95 95 94 94 94 94 94 95 94 | open-like (> 80) |
