# TYK2_P982A_20261022_122408 — TYK2 P982A_96-384_s16-23__seed18

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 18; MSA 96 clusters / 384 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 18 | 14 | 81.0 | 51.7 | 94.8 | 93.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 38.9 | 18 | 1 | 70.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.2 | 42.2 | 38.9 |
| 2 | 78.2 | 35.4 | 40.3 |
| 3 | 80.4 | 46.0 | 48.7 |
| 4 | 80.5 | 63.8 | 72.1 |
| 5 | 80.8 | 88.3 | 94.9 |
| 6 | 80.7 | 90.1 | 96.4 |
| 7 | 80.9 | 93.7 | 96.0 |
| 8 | 80.7 | 95.3 | 90.8 |
| 9 | 80.8 | 95.1 | 92.5 |
| 10 | 80.9 | 95.7 | 88.5 |
| 11 | 80.5 | 95.4 | 90.3 |
| 12 | 80.5 | 95.0 | 92.7 |
| 13 | 80.7 | 95.2 | 89.1 |
| 14 | 81.0 | 94.8 | 93.3 |
| 15 | 80.8 | 95.1 | 90.6 |

pLDDT 70.2–81.0; JH2–JH1 49.8–56.6 Å; FERM–JH1 35.4–95.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 18 | 42 35 46 64 88 90 94 95 95 96 95 95 95 95 95 | open-like (> 80) |
