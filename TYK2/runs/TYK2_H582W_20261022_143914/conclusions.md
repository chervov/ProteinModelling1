# TYK2_H582W_20261022_143914 — TYK2 H582W_free_msa96-384_s0-7__seed1

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 13 | 81.4 | 46.7 | 93.5 | 82.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 26.2 | 1 | 2 | 76.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.2 | 61.3 | 66.4 |
| 2 | 76.2 | 34.6 | 26.2 |
| 3 | 79.1 | 61.4 | 61.3 |
| 4 | 80.6 | 95.2 | 86.8 |
| 5 | 80.6 | 93.3 | 83.7 |
| 6 | 81.1 | 93.7 | 82.7 |
| 7 | 80.7 | 93.7 | 82.9 |
| 8 | 81.1 | 93.8 | 83.0 |
| 9 | 80.7 | 93.3 | 82.8 |
| 10 | 81.2 | 93.2 | 82.7 |
| 11 | 81.3 | 93.5 | 83.0 |
| 12 | 81.2 | 93.6 | 82.3 |
| 13 | 81.4 | 93.5 | 82.6 |
| 14 | 81.0 | 93.4 | 82.4 |
| 15 | 81.2 | 93.6 | 82.4 |

pLDDT 71.2–81.4; JH2–JH1 36.9–49.5 Å; FERM–JH1 34.6–95.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 61 35 61 95 93 94 94 94 93 93 94 94 94 93 94 | open-like (> 80) |
