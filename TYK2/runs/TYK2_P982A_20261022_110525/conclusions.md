# TYK2_P982A_20261022_110525 — TYK2 P982A_96-384_s8-15__seed15

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 15; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 15 | 7 | 81.3 | 46.7 | 93.1 | 82.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 30.7 | 15 | 1 | 70.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.6 | 33.5 | 30.7 |
| 2 | 79.1 | 38.5 | 37.6 |
| 3 | 80.5 | 93.5 | 84.4 |
| 4 | 81.0 | 92.8 | 82.4 |
| 5 | 81.1 | 92.7 | 82.0 |
| 6 | 81.3 | 93.1 | 82.1 |
| 7 | 81.3 | 93.1 | 82.3 |
| 8 | 80.9 | 92.8 | 82.1 |
| 9 | 81.0 | 93.0 | 81.8 |
| 10 | 80.8 | 93.2 | 81.8 |
| 11 | 81.2 | 93.1 | 82.1 |
| 12 | 81.0 | 93.2 | 81.9 |
| 13 | 80.9 | 93.1 | 82.0 |
| 14 | 81.0 | 93.0 | 82.1 |
| 15 | 81.1 | 92.9 | 82.0 |

pLDDT 70.6–81.3; JH2–JH1 46.4–57.8 Å; FERM–JH1 33.5–93.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 15 | 34 38 94 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
