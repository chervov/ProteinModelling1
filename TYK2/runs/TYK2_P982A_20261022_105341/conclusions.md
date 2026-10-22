# TYK2_P982A_20261022_105341 — TYK2 P982A_96-384_s8-15__seed14

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 14; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 14 | 8 | 81.5 | 50.2 | 94.3 | 91.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 14 | 2 | 78.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.7 | 32.1 | 42.6 |
| 2 | 78.6 | 40.4 | 37.2 |
| 3 | 80.2 | 48.2 | 46.9 |
| 4 | 80.8 | 51.8 | 49.1 |
| 5 | 81.4 | 85.8 | 87.4 |
| 6 | 81.4 | 92.2 | 91.3 |
| 7 | 81.4 | 89.6 | 92.8 |
| 8 | 81.5 | 94.3 | 91.0 |
| 9 | 81.4 | 95.0 | 87.3 |
| 10 | 81.1 | 95.1 | 88.3 |
| 11 | 81.1 | 95.0 | 88.0 |
| 12 | 81.0 | 94.8 | 87.3 |
| 13 | 80.9 | 94.8 | 85.8 |
| 14 | 80.9 | 94.6 | 85.8 |
| 15 | 81.3 | 94.6 | 85.9 |

pLDDT 69.7–81.5; JH2–JH1 46.1–57.1 Å; FERM–JH1 32.1–95.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 14 | 32 40 48 52 86 92 90 94 95 95 95 95 95 95 95 | open-like (> 80) |
