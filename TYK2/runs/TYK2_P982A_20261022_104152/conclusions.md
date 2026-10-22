# TYK2_P982A_20261022_104152 — TYK2 P982A_96-384_s8-15__seed13

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 13; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 13 | 4 | 80.9 | 49.0 | 87.4 | 83.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 28.0 | 13 | 2 | 78.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.1 | 20.3 | 36.3 |
| 2 | 78.9 | 32.7 | 28.0 |
| 3 | 79.8 | 75.8 | 67.4 |
| 4 | 80.9 | 87.4 | 83.6 |
| 5 | 80.6 | 90.0 | 85.4 |
| 6 | 80.7 | 86.5 | 81.1 |
| 7 | 80.1 | 88.2 | 82.9 |
| 8 | 80.6 | 87.9 | 84.2 |
| 9 | 80.6 | 86.2 | 79.7 |
| 10 | 80.5 | 88.3 | 83.7 |
| 11 | 80.5 | 86.8 | 83.1 |
| 12 | 80.5 | 88.0 | 83.8 |
| 13 | 80.4 | 87.0 | 81.5 |
| 14 | 80.3 | 86.7 | 81.2 |
| 15 | 80.6 | 87.5 | 84.0 |

pLDDT 72.1–80.9; JH2–JH1 43.1–49.2 Å; FERM–JH1 20.3–90.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 13 | 20 33 76 87 90 86 88 88 86 88 87 88 87 87 88 | open-like (> 80) |
