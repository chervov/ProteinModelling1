# TYK2_20261022_094311 — TYK2 WT_96-384_s8-15__seed8

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 12 | 81.5 | 46.8 | 93.7 | 82.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 32.6 | 8 | 1 | 71.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.5 | 36.4 | 32.6 |
| 2 | 79.4 | 92.7 | 89.9 |
| 3 | 80.8 | 94.3 | 83.8 |
| 4 | 81.0 | 93.4 | 82.6 |
| 5 | 81.3 | 93.5 | 82.8 |
| 6 | 81.5 | 93.5 | 82.6 |
| 7 | 80.9 | 93.7 | 82.7 |
| 8 | 81.2 | 93.5 | 82.1 |
| 9 | 81.2 | 93.5 | 82.4 |
| 10 | 81.0 | 93.8 | 82.3 |
| 11 | 81.2 | 93.4 | 82.2 |
| 12 | 81.5 | 93.7 | 82.6 |
| 13 | 81.1 | 93.6 | 82.7 |
| 14 | 80.9 | 93.4 | 82.7 |
| 15 | 80.7 | 93.5 | 82.2 |

pLDDT 71.5–81.5; JH2–JH1 29.5–49.2 Å; FERM–JH1 36.4–94.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 36 93 94 93 94 94 94 94 94 94 93 94 94 93 94 | open-like (> 80) |
