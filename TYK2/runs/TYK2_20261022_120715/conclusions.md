# TYK2_20261022_120715 — TYK2 WT_96-384_s16-23__seed19

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 19; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 19 | 8 | 81.7 | 46.5 | 93.2 | 82.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 36.2 | 19 | 1 | 72.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.0 | 30.2 | 36.2 |
| 2 | 79.0 | 93.3 | 83.8 |
| 3 | 80.8 | 92.8 | 82.9 |
| 4 | 81.6 | 93.3 | 82.6 |
| 5 | 81.5 | 93.8 | 82.2 |
| 6 | 81.4 | 93.2 | 82.2 |
| 7 | 81.5 | 93.6 | 82.5 |
| 8 | 81.7 | 93.2 | 82.1 |
| 9 | 81.4 | 93.5 | 82.0 |
| 10 | 81.4 | 93.3 | 82.2 |
| 11 | 81.3 | 93.6 | 82.7 |
| 12 | 81.5 | 93.5 | 82.0 |
| 13 | 81.5 | 93.5 | 82.2 |
| 14 | 81.5 | 93.2 | 82.1 |
| 15 | 81.4 | 93.5 | 82.1 |

pLDDT 72.0–81.7; JH2–JH1 39.0–47.5 Å; FERM–JH1 30.2–93.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 19 | 30 93 93 93 94 93 94 93 94 93 94 94 94 93 94 | open-like (> 80) |
