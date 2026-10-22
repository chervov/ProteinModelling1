# TYK2_P982A_20261022_122602 — TYK2 P982A_96-384_s16-23__seed19

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 19; MSA 96 clusters / 384 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 19 | 12 | 81.1 | 46.6 | 93.3 | 82.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 35.8 | 19 | 1 | 70.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.8 | 44.7 | 35.8 |
| 2 | 78.8 | 89.0 | 88.1 |
| 3 | 80.5 | 93.9 | 86.6 |
| 4 | 80.9 | 93.5 | 83.6 |
| 5 | 80.8 | 93.7 | 82.7 |
| 6 | 80.8 | 93.3 | 83.1 |
| 7 | 80.5 | 93.8 | 83.6 |
| 8 | 80.9 | 93.1 | 82.8 |
| 9 | 80.6 | 93.3 | 82.5 |
| 10 | 80.9 | 93.0 | 82.3 |
| 11 | 80.7 | 93.2 | 82.3 |
| 12 | 81.1 | 93.3 | 82.2 |
| 13 | 80.7 | 93.4 | 82.7 |
| 14 | 80.6 | 93.1 | 82.4 |
| 15 | 81.0 | 93.2 | 82.3 |

pLDDT 70.8–81.1; JH2–JH1 46.5–48.1 Å; FERM–JH1 44.7–93.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 19 | 45 89 94 94 94 93 94 93 93 93 93 93 93 93 93 | open-like (> 80) |
