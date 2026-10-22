# TYK2_P982A_20261022_114303 — TYK2 P982A_96-384_s16-23__seed17

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 17; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 17 | 6 | 80.9 | 52.3 | 95.3 | 93.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 27.9 | 17 | 1 | 69.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.6 | 13.0 | 27.9 |
| 2 | 79.2 | 43.9 | 51.6 |
| 3 | 80.8 | 87.4 | 96.1 |
| 4 | 80.7 | 91.8 | 96.6 |
| 5 | 80.7 | 90.5 | 96.6 |
| 6 | 80.9 | 95.3 | 93.7 |
| 7 | 80.6 | 95.6 | 87.9 |
| 8 | 80.6 | 94.4 | 84.6 |
| 9 | 80.8 | 94.5 | 84.5 |
| 10 | 80.5 | 94.7 | 84.3 |
| 11 | 80.5 | 94.6 | 83.7 |
| 12 | 80.8 | 94.6 | 85.1 |
| 13 | 80.3 | 94.1 | 84.1 |
| 14 | 80.4 | 95.4 | 85.7 |
| 15 | 80.7 | 95.4 | 86.7 |

pLDDT 69.6–80.9; JH2–JH1 37.2–53.9 Å; FERM–JH1 13.0–95.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 17 | 13 44 87 92 90 95 96 94 94 95 95 95 94 95 95 | open-like (> 80) |
