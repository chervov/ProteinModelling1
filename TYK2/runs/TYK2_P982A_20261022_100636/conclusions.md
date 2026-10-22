# TYK2_P982A_20261022_100636 — TYK2 P982A_96-384_s8-15__seed10

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 10; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 10 | 14 | 81.5 | 46.6 | 93.6 | 82.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 72.9 | 10 | 1 | 70.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.4 | 58.6 | 72.9 |
| 2 | 78.2 | 83.8 | 88.6 |
| 3 | 80.9 | 94.1 | 83.4 |
| 4 | 81.0 | 93.0 | 82.3 |
| 5 | 81.2 | 93.5 | 82.1 |
| 6 | 81.4 | 93.4 | 82.2 |
| 7 | 81.2 | 93.5 | 82.2 |
| 8 | 81.2 | 93.3 | 82.1 |
| 9 | 81.2 | 93.3 | 82.2 |
| 10 | 81.1 | 93.5 | 82.1 |
| 11 | 81.4 | 93.5 | 81.9 |
| 12 | 81.2 | 93.0 | 81.8 |
| 13 | 81.4 | 93.4 | 82.1 |
| 14 | 81.5 | 93.6 | 82.1 |
| 15 | 81.0 | 93.4 | 82.3 |

pLDDT 70.4–81.5; JH2–JH1 46.0–50.0 Å; FERM–JH1 58.6–94.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 10 | 59 84 94 93 94 93 94 93 93 94 94 93 93 94 93 | open-like (> 80) |
