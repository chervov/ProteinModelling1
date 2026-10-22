# TYK2_20261022_121859 — TYK2 WT_96-384_s16-23__seed20

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 20; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 20 | 7 | 81.5 | 46.8 | 93.3 | 83.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 74.3 | 20 | 1 | 70.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 70.2 | 44.5 | 74.3 |
| 2 | 79.1 | 93.6 | 88.7 |
| 3 | 80.9 | 93.8 | 83.8 |
| 4 | 81.1 | 93.5 | 82.6 |
| 5 | 81.0 | 93.4 | 82.3 |
| 6 | 81.3 | 93.4 | 82.6 |
| 7 | 81.5 | 93.3 | 83.0 |
| 8 | 81.2 | 93.4 | 82.2 |
| 9 | 81.2 | 93.3 | 82.2 |
| 10 | 81.2 | 93.2 | 82.3 |
| 11 | 81.2 | 93.2 | 82.4 |
| 12 | 81.1 | 93.3 | 82.3 |
| 13 | 81.1 | 93.3 | 82.8 |
| 14 | 81.3 | 93.4 | 82.7 |
| 15 | 81.2 | 93.2 | 82.6 |

pLDDT 70.2–81.5; JH2–JH1 46.6–55.6 Å; FERM–JH1 44.5–93.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 20 | 44 94 94 94 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
