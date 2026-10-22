# TYK2_20261022_110542 — TYK2 WT_96-384_s8-15__seed15

TYK2 wild type, template-free, MSA 96/384, seeds 8-15. The matched control arm for the P982A test running on the other slot; takes WT at this depth from n=8 (7/8 canonical open) to n=16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 15; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 15 | 11 | 81.6 | 46.7 | 93.2 | 82.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 27.7 | 15 | 1 | 72.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.1 | 36.6 | 27.7 |
| 2 | 78.3 | 89.1 | 74.7 |
| 3 | 81.5 | 93.2 | 81.7 |
| 4 | 81.3 | 93.3 | 82.3 |
| 5 | 81.0 | 93.2 | 82.4 |
| 6 | 81.0 | 93.6 | 82.3 |
| 7 | 81.4 | 93.6 | 82.1 |
| 8 | 80.8 | 93.1 | 82.2 |
| 9 | 81.4 | 93.3 | 82.4 |
| 10 | 81.0 | 93.4 | 82.1 |
| 11 | 81.6 | 93.2 | 82.2 |
| 12 | 81.4 | 93.1 | 82.0 |
| 13 | 80.8 | 93.1 | 82.2 |
| 14 | 81.4 | 93.0 | 82.2 |
| 15 | 81.2 | 93.2 | 82.2 |

pLDDT 72.1–81.6; JH2–JH1 44.4–46.8 Å; FERM–JH1 36.6–93.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 15 | 37 89 93 93 93 94 94 93 93 93 93 93 93 93 93 | open-like (> 80) |
