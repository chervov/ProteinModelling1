# TYK2_P982A_20261022_122757 — TYK2 P982A_96-384_s16-23__seed20

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 20; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 20 | 6 | 80.7 | 47.0 | 93.5 | 83.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 37.5 | 20 | 2 | 77.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.3 | 64.8 | 69.9 |
| 2 | 77.1 | 37.1 | 37.5 |
| 3 | 80.3 | 90.0 | 88.6 |
| 4 | 80.6 | 95.0 | 86.1 |
| 5 | 80.5 | 93.7 | 83.3 |
| 6 | 80.7 | 93.5 | 83.2 |
| 7 | 80.7 | 93.3 | 83.2 |
| 8 | 80.6 | 93.5 | 82.9 |
| 9 | 80.7 | 93.1 | 82.4 |
| 10 | 80.4 | 93.4 | 82.6 |
| 11 | 80.7 | 93.2 | 82.7 |
| 12 | 80.6 | 93.1 | 83.0 |
| 13 | 80.4 | 93.5 | 82.8 |
| 14 | 80.6 | 93.5 | 82.6 |
| 15 | 80.7 | 93.4 | 82.8 |

pLDDT 69.3–80.7; JH2–JH1 41.8–52.9 Å; FERM–JH1 37.1–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 20 | 65 37 90 95 94 94 93 94 93 93 93 93 94 94 93 | open-like (> 80) |
