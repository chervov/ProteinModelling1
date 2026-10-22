# TYK2_20261022_123047 — TYK2 WT_96-384_s16-23__seed21

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 21; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 21 | 13 | 81.0 | 47.1 | 93.6 | 83.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 42.3 | 21 | 1 | 72.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.0 | 10.9 | 42.3 |
| 2 | 78.6 | 40.1 | 46.1 |
| 3 | 80.9 | 92.9 | 92.0 |
| 4 | 80.8 | 94.6 | 85.2 |
| 5 | 80.9 | 94.2 | 85.4 |
| 6 | 80.2 | 93.6 | 83.6 |
| 7 | 80.7 | 93.8 | 83.8 |
| 8 | 80.8 | 93.8 | 83.3 |
| 9 | 80.5 | 93.5 | 84.0 |
| 10 | 80.8 | 93.2 | 82.8 |
| 11 | 80.8 | 93.4 | 83.3 |
| 12 | 80.5 | 93.6 | 84.1 |
| 13 | 81.0 | 93.6 | 83.1 |
| 14 | 80.8 | 93.2 | 82.4 |
| 15 | 80.8 | 93.4 | 82.5 |

pLDDT 72.0–81.0; JH2–JH1 45.0–50.8 Å; FERM–JH1 10.9–94.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 21 | 11 40 93 95 94 94 94 94 94 93 93 94 94 93 93 | open-like (> 80) |
