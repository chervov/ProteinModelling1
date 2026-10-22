# TYK2_P982A_20261022_094253 — TYK2 P982A_96-384_s8-15__seed8

TYK2 P982A, template-free, MSA 96/384, seeds 8-15. Takes the comparison against wild type at this depth from n=8 to n=16. P982A gave 2/8 canonical open against WT 7/8 (p=0.041 uncorrected, 0.57 after Holm over the campaign's 14 depth-matched comparisons), and produced the only two active-dimer-like structures in 385 TYK2 structures. Both signals are n=8 and die under correction. Prediction stated in advance: if the reduction is real, P982A lands near 4/16 open against WT near 14/16; if it is noise, both sit near 14/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 12 | 81.0 | 46.9 | 93.4 | 82.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 73.6 | 8 | 1 | 72.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.5 | 64.6 | 73.6 |
| 2 | 79.4 | 92.1 | 95.7 |
| 3 | 80.8 | 93.9 | 84.0 |
| 4 | 80.8 | 93.2 | 82.6 |
| 5 | 80.7 | 93.3 | 82.9 |
| 6 | 80.8 | 93.3 | 82.6 |
| 7 | 80.8 | 93.4 | 82.8 |
| 8 | 80.7 | 93.5 | 82.6 |
| 9 | 80.6 | 93.3 | 82.4 |
| 10 | 80.5 | 93.7 | 83.0 |
| 11 | 80.8 | 93.6 | 81.9 |
| 12 | 81.0 | 93.4 | 82.7 |
| 13 | 80.6 | 93.2 | 82.5 |
| 14 | 80.6 | 93.0 | 82.5 |
| 15 | 80.4 | 93.1 | 82.6 |

pLDDT 72.5–81.0; JH2–JH1 46.2–53.0 Å; FERM–JH1 64.6–93.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 65 92 94 93 93 93 93 94 93 94 94 93 93 93 93 | open-like (> 80) |
