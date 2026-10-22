# TYK2_P982A_20261022_125125 — TYK2 P982A_96-384_s16-23__seed22

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 22; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 22 | 11 | 81.2 | 46.6 | 93.3 | 82.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 26.9 | 22 | 1 | 72.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.2 | 21.3 | 26.9 |
| 2 | 79.1 | 45.9 | 34.6 |
| 3 | 80.7 | 53.4 | 51.8 |
| 4 | 80.9 | 85.7 | 84.6 |
| 5 | 80.7 | 95.4 | 87.3 |
| 6 | 80.8 | 94.6 | 88.5 |
| 7 | 80.9 | 94.5 | 85.0 |
| 8 | 81.0 | 93.7 | 83.0 |
| 9 | 81.1 | 93.8 | 82.6 |
| 10 | 80.8 | 93.6 | 82.5 |
| 11 | 81.2 | 93.3 | 82.3 |
| 12 | 81.2 | 93.8 | 82.6 |
| 13 | 80.8 | 93.5 | 82.3 |
| 14 | 80.9 | 93.7 | 82.5 |
| 15 | 80.5 | 93.8 | 82.4 |

pLDDT 72.2–81.2; JH2–JH1 46.5–51.5 Å; FERM–JH1 21.3–95.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 22 | 21 46 53 86 95 95 94 94 94 94 93 94 94 94 94 | open-like (> 80) |
