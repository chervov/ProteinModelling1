# TYK2_P982A_20261022_123943 — TYK2 P982A_96-384_s16-23__seed21

TYK2 P982A, template-free, MSA 96/384, seeds 16-23. Third batch, taking the arm to n=24 and with the matched wild-type arm to n=24. At n=16 P982A gave 8/16 canonical open against WT 15/16, raw p=0.0155, Holm 0.264 over the campaign's 20 comparisons; the effect strengthened when n doubled (p 0.050 -> 0.0155) rather than regressing. Prediction stated in advance: if the reduction is real the arm holds near 0.50 and raw p falls below 0.005; if it is noise it drifts up toward WT.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 21; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 21 | 4 | 79.6 | 37.8 | 39.8 | 1.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.2 | 21 | 8 | 79.2 | 14 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.0 | 55.7 | 34.2 |
| 2 | 78.6 | 37.3 | 10.4 |
| 3 | 79.4 | 39.8 | 2.1 |
| 4 | 79.6 | 39.8 | 1.6 |
| 5 | 79.4 | 40.0 | 1.7 |
| 6 | 78.8 | 40.0 | 2.5 |
| 7 | 78.7 | 40.5 | 3.0 |
| 8 | 79.2 | 40.5 | 1.2 |
| 9 | 79.2 | 39.7 | 1.7 |
| 10 | 79.0 | 40.1 | 1.7 |
| 11 | 79.1 | 39.9 | 1.9 |
| 12 | 79.2 | 40.4 | 1.3 |
| 13 | 79.0 | 39.7 | 1.6 |
| 14 | 79.2 | 40.6 | 1.6 |
| 15 | 79.0 | 40.1 | 1.7 |

pLDDT 71.0–79.6; JH2–JH1 37.4–52.2 Å; FERM–JH1 37.3–55.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 21 | 56 37 40 40 40 40 40 40 40 40 40 40 40 41 40 | closed-like (< 50) |
