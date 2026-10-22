# TYK2_P982A_20261022_103007 — TYK2 P982A_96-384_s8-15__seed12

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 12; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 12 | 12 | 81.6 | 42.1 | 76.6 | 76.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 18.9 | 12 | 5 | 80.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.3 | 21.0 | 37.3 |
| 2 | 78.9 | 33.7 | 24.3 |
| 3 | 79.3 | 45.6 | 49.0 |
| 4 | 81.0 | 39.6 | 33.1 |
| 5 | 80.1 | 36.5 | 18.9 |
| 6 | 81.0 | 45.8 | 37.3 |
| 7 | 81.0 | 49.7 | 43.2 |
| 8 | 81.1 | 62.9 | 60.3 |
| 9 | 80.9 | 69.2 | 68.8 |
| 10 | 81.4 | 75.0 | 76.9 |
| 11 | 81.3 | 73.4 | 76.3 |
| 12 | 81.6 | 76.6 | 76.6 |
| 13 | 81.4 | 81.4 | 85.9 |
| 14 | 81.3 | 78.0 | 82.2 |
| 15 | 81.4 | 81.7 | 85.0 |

pLDDT 71.3–81.6; JH2–JH1 19.7–52.1 Å; FERM–JH1 21.0–81.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 12 | 21 34 46 40 36 46 50 63 69 75 73 77 81 78 82 | open-like (> 80) |
