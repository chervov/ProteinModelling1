# TYK2_20261022_124236 — TYK2 WT_96-384_s16-23__seed22

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 22; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 22 | 7 | 81.6 | 46.3 | 93.0 | 81.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 45.6 | 22 | 1 | 72.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.7 | 21.2 | 45.6 |
| 2 | 78.5 | 92.7 | 81.0 |
| 3 | 81.2 | 93.3 | 82.4 |
| 4 | 81.4 | 93.3 | 82.0 |
| 5 | 81.3 | 93.1 | 82.0 |
| 6 | 81.3 | 92.9 | 82.1 |
| 7 | 81.6 | 93.0 | 81.8 |
| 8 | 81.2 | 93.5 | 81.9 |
| 9 | 81.4 | 93.6 | 82.1 |
| 10 | 81.5 | 93.5 | 82.1 |
| 11 | 81.5 | 93.3 | 81.9 |
| 12 | 81.4 | 93.5 | 82.1 |
| 13 | 81.4 | 93.4 | 82.0 |
| 14 | 81.1 | 93.5 | 81.8 |
| 15 | 81.5 | 93.4 | 81.9 |

pLDDT 72.7–81.6; JH2–JH1 46.3–59.3 Å; FERM–JH1 21.2–93.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 22 | 21 93 93 93 93 93 93 94 94 94 93 94 93 94 93 | open-like (> 80) |
