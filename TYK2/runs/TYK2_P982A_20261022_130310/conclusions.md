# TYK2_P982A_20261022_130310 — TYK2 P982A_96-384_s16-23__seed23

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 23; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 23 | 14 | 81.4 | 43.2 | 83.7 | 77.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 17.5 | 23 | 4 | 80.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.6 | 45.2 | 48.7 |
| 2 | 76.4 | 23.9 | 21.8 |
| 3 | 79.9 | 37.3 | 20.5 |
| 4 | 80.1 | 36.5 | 17.5 |
| 5 | 80.8 | 83.4 | 74.7 |
| 6 | 81.0 | 86.9 | 81.0 |
| 7 | 80.7 | 85.9 | 80.0 |
| 8 | 80.7 | 85.4 | 78.1 |
| 9 | 80.9 | 85.3 | 78.6 |
| 10 | 81.0 | 86.5 | 80.5 |
| 11 | 80.9 | 86.5 | 79.7 |
| 12 | 80.6 | 86.6 | 78.6 |
| 13 | 81.1 | 84.9 | 77.4 |
| 14 | 81.4 | 83.7 | 77.2 |
| 15 | 81.2 | 84.3 | 77.2 |

pLDDT 71.7–81.4; JH2–JH1 41.8–46.8 Å; FERM–JH1 23.9–86.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 23 | 45 24 37 36 83 87 86 85 85 86 86 87 85 84 84 | open-like (> 80) |
