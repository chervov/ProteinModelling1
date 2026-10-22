# TYK2_H582W_20261022_154914 — TYK2 H582W_free_msa96-384_s0-7__seed7

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 7; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 7 | 14 | 81.3 | 46.9 | 93.8 | 82.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 48.0 | 7 | 2 | 76.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.6 | 56.4 | 58.5 |
| 2 | 76.2 | 21.1 | 48.0 |
| 3 | 80.1 | 78.8 | 80.9 |
| 4 | 80.5 | 92.9 | 91.9 |
| 5 | 80.9 | 95.4 | 88.5 |
| 6 | 81.0 | 94.1 | 84.4 |
| 7 | 81.0 | 93.9 | 83.1 |
| 8 | 80.8 | 93.8 | 82.8 |
| 9 | 80.9 | 93.8 | 82.8 |
| 10 | 81.0 | 93.6 | 82.9 |
| 11 | 80.9 | 93.5 | 82.8 |
| 12 | 81.1 | 93.5 | 82.7 |
| 13 | 80.9 | 93.6 | 82.2 |
| 14 | 81.3 | 93.8 | 82.7 |
| 15 | 81.1 | 93.8 | 83.0 |

pLDDT 70.6–81.3; JH2–JH1 45.7–62.9 Å; FERM–JH1 21.1–95.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 7 | 56 21 79 93 95 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
