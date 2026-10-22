# TYK2_P982A_20261022_122015 — TYK2 P982A_96-384_s16-23__seed16

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 16; MSA 96 clusters / 384 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 16 | 14 | 81.0 | 50.2 | 94.2 | 90.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 20.9 | 16 | 7 | 79.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.6 | 47.0 | 33.6 |
| 2 | 77.0 | 37.9 | 35.3 |
| 3 | 78.7 | 34.2 | 28.7 |
| 4 | 78.7 | 52.4 | 35.3 |
| 5 | 78.7 | 56.9 | 43.2 |
| 6 | 78.1 | 54.7 | 49.9 |
| 7 | 79.0 | 38.6 | 20.9 |
| 8 | 79.3 | 53.1 | 31.5 |
| 9 | 80.7 | 84.9 | 85.7 |
| 10 | 80.8 | 90.4 | 91.7 |
| 11 | 80.4 | 94.3 | 89.1 |
| 12 | 80.7 | 93.7 | 90.1 |
| 13 | 80.7 | 94.3 | 90.7 |
| 14 | 81.0 | 94.2 | 90.6 |
| 15 | 80.6 | 94.9 | 87.5 |

pLDDT 70.6–81.0; JH2–JH1 13.4–56.8 Å; FERM–JH1 34.2–94.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 16 | 47 38 34 52 57 55 39 53 85 90 94 94 94 94 95 | open-like (> 80) |
