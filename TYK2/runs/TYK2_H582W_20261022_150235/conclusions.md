# TYK2_H582W_20261022_150235 — TYK2 H582W_free_msa96-384_s0-7__seed3

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 11 | 80.6 | 46.6 | 93.4 | 82.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 32.5 | 3 | 2 | 77.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.3 | 54.6 | 58.6 |
| 2 | 77.8 | 36.2 | 32.5 |
| 3 | 79.1 | 50.8 | 41.0 |
| 4 | 79.9 | 93.8 | 90.0 |
| 5 | 80.1 | 95.1 | 86.1 |
| 6 | 80.1 | 94.0 | 84.4 |
| 7 | 80.4 | 94.1 | 83.6 |
| 8 | 80.1 | 93.6 | 82.7 |
| 9 | 80.1 | 93.8 | 83.0 |
| 10 | 79.8 | 93.5 | 82.8 |
| 11 | 80.6 | 93.4 | 82.3 |
| 12 | 80.3 | 93.4 | 82.4 |
| 13 | 80.3 | 93.4 | 82.2 |
| 14 | 80.0 | 93.6 | 82.8 |
| 15 | 80.6 | 93.1 | 82.0 |

pLDDT 71.3–80.6; JH2–JH1 36.1–50.3 Å; FERM–JH1 36.2–95.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 55 36 51 94 95 94 94 94 94 94 93 93 93 94 93 | open-like (> 80) |
