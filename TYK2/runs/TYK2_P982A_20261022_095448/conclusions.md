# TYK2_P982A_20261022_095448 — TYK2 P982A_96-384_s8-15__seed9

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 9; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 9 | 13 | 81.2 | 46.7 | 93.4 | 82.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 33.8 | 9 | 3 | 80.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.5 | 55.1 | 60.0 |
| 2 | 78.9 | 36.4 | 39.2 |
| 3 | 80.2 | 38.9 | 33.8 |
| 4 | 79.7 | 48.3 | 34.5 |
| 5 | 80.6 | 92.2 | 83.8 |
| 6 | 80.9 | 94.3 | 84.5 |
| 7 | 81.2 | 93.6 | 83.2 |
| 8 | 81.1 | 93.4 | 82.2 |
| 9 | 81.0 | 93.5 | 82.7 |
| 10 | 80.7 | 93.6 | 82.6 |
| 11 | 80.8 | 93.6 | 82.8 |
| 12 | 80.8 | 93.7 | 83.0 |
| 13 | 81.2 | 93.4 | 82.8 |
| 14 | 81.1 | 93.8 | 82.7 |
| 15 | 81.1 | 93.8 | 82.9 |

pLDDT 71.5–81.2; JH2–JH1 26.0–58.6 Å; FERM–JH1 36.4–94.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 9 | 55 36 39 48 92 94 94 93 94 94 94 94 93 94 94 | open-like (> 80) |
