# TYK2_20261022_115528 — TYK2 WT_96-384_s16-23__seed18

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 18; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 18 | 9 | 81.8 | 51.2 | 95.2 | 90.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 32.6 | 18 | 1 | 73.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 73.0 | 41.1 | 32.6 |
| 2 | 80.2 | 47.0 | 49.3 |
| 3 | 81.2 | 56.8 | 58.8 |
| 4 | 81.4 | 60.8 | 67.2 |
| 5 | 81.1 | 60.1 | 63.6 |
| 6 | 81.1 | 61.9 | 63.3 |
| 7 | 81.2 | 61.9 | 63.3 |
| 8 | 81.4 | 83.1 | 86.9 |
| 9 | 81.8 | 95.2 | 90.9 |
| 10 | 81.6 | 95.4 | 90.7 |
| 11 | 81.5 | 95.3 | 85.8 |
| 12 | 81.4 | 95.8 | 90.6 |
| 13 | 81.4 | 95.2 | 86.8 |
| 14 | 81.6 | 96.2 | 89.9 |
| 15 | 81.5 | 95.2 | 87.4 |

pLDDT 73.0–81.8; JH2–JH1 42.5–51.2 Å; FERM–JH1 41.1–96.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 18 | 41 47 57 61 60 62 62 83 95 95 95 96 95 96 95 | open-like (> 80) |
