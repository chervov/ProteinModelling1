# TYK2_H582W_20261022_151409 — TYK2 H582W_free_msa96-384_s0-7__seed4

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 4; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 4 | 7 | 81.1 | 46.9 | 93.2 | 83.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 29.1 | 4 | 1 | 72.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.9 | 34.6 | 29.1 |
| 2 | 77.9 | 36.9 | 32.7 |
| 3 | 80.5 | 68.3 | 72.1 |
| 4 | 80.9 | 92.5 | 90.2 |
| 5 | 80.9 | 94.1 | 84.9 |
| 6 | 81.0 | 94.3 | 86.0 |
| 7 | 81.1 | 93.2 | 83.4 |
| 8 | 80.7 | 93.5 | 83.3 |
| 9 | 80.9 | 93.2 | 83.5 |
| 10 | 80.7 | 93.2 | 82.8 |
| 11 | 80.9 | 93.3 | 83.1 |
| 12 | 80.8 | 93.2 | 83.2 |
| 13 | 80.8 | 93.4 | 83.5 |
| 14 | 80.9 | 93.5 | 82.9 |
| 15 | 81.0 | 93.4 | 83.8 |

pLDDT 72.9–81.1; JH2–JH1 43.1–53.9 Å; FERM–JH1 34.6–94.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 4 | 35 37 68 92 94 94 93 94 93 93 93 93 93 94 93 | open-like (> 80) |
