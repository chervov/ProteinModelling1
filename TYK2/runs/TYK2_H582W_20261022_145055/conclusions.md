# TYK2_H582W_20261022_145055 — TYK2 H582W_free_msa96-384_s0-7__seed2

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 13 | 81.8 | 46.7 | 85.5 | 87.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 29.2 | 2 | 2 | 78.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.2 | 46.9 | 53.7 |
| 2 | 78.2 | 40.6 | 29.2 |
| 3 | 80.6 | 44.8 | 40.2 |
| 4 | 80.8 | 49.0 | 46.2 |
| 5 | 81.2 | 69.9 | 70.4 |
| 6 | 81.1 | 89.1 | 89.5 |
| 7 | 81.5 | 80.8 | 80.8 |
| 8 | 81.3 | 88.2 | 87.7 |
| 9 | 81.4 | 84.5 | 85.0 |
| 10 | 81.2 | 93.1 | 89.7 |
| 11 | 81.7 | 83.8 | 84.6 |
| 12 | 81.4 | 88.6 | 87.9 |
| 13 | 81.8 | 85.5 | 87.2 |
| 14 | 81.3 | 83.6 | 87.6 |
| 15 | 81.5 | 85.9 | 88.2 |

pLDDT 70.2–81.8; JH2–JH1 42.4–49.6 Å; FERM–JH1 40.6–93.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 47 41 45 49 70 89 81 88 84 93 84 89 86 84 86 | open-like (> 80) |
