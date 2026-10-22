# TYK2_H582W_20261022_152551 — TYK2 H582W_free_msa96-384_s0-7__seed5

TYK2 H582W, template-free, MSA 96/384, seeds 0-7. The second arm of the H582W test, at the depth where wild type is 23/24 open and P982A - the other 4OLI interface residue, and a loss-of-function variant - was confirmed to REDUCE openness to 13/24 (section 53). H582W is gain-of-function, so the directional prediction is the opposite: it should hold at the wild-type ceiling. A reduction here would mean the score responds to interface perturbation regardless of functional direction.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 4 | 80.7 | 41.2 | 41.2 | 17.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 10.7 | 5 | 3 | 79.9 | 2 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.5 | 44.2 | 31.6 |
| 2 | 77.8 | 32.9 | 15.6 |
| 3 | 79.9 | 39.6 | 10.7 |
| 4 | 80.7 | 41.2 | 17.4 |
| 5 | 80.0 | 41.3 | 17.0 |
| 6 | 80.7 | 58.3 | 49.6 |
| 7 | 79.9 | 42.3 | 20.1 |
| 8 | 80.2 | 41.3 | 18.2 |
| 9 | 78.9 | 40.2 | 24.4 |
| 10 | 80.3 | 41.3 | 19.9 |
| 11 | 80.2 | 40.8 | 13.1 |
| 12 | 79.9 | 41.5 | 15.6 |
| 13 | 80.4 | 41.0 | 18.0 |
| 14 | 80.2 | 41.7 | 16.1 |
| 15 | 80.2 | 40.3 | 15.6 |

pLDDT 70.5–80.7; JH2–JH1 38.3–56.9 Å; FERM–JH1 32.9–58.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 44 33 40 41 41 58 42 41 40 41 41 42 41 42 40 | closed-like (< 50) |
