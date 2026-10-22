# TYK2_20261022_113143 — TYK2 WT_96-384_s16-23__seed16

TYK2 wild type, template-free, MSA 96/384, seeds 16-23. Matched control arm for the third P982A batch. At n=16 wild type is 15/16 canonical open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 16; MSA 96 clusters / 384 extra; no template. Run time 12 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 16 | 12 | 81.6 | 46.6 | 93.4 | 82.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 34.3 | 16 | 1 | 72.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.8 | 31.8 | 34.3 |
| 2 | 78.7 | 39.9 | 39.1 |
| 3 | 80.8 | 93.5 | 82.8 |
| 4 | 81.2 | 93.2 | 82.2 |
| 5 | 81.5 | 93.3 | 82.2 |
| 6 | 81.3 | 93.9 | 82.6 |
| 7 | 81.2 | 93.2 | 82.1 |
| 8 | 81.2 | 93.5 | 82.2 |
| 9 | 81.4 | 93.8 | 82.0 |
| 10 | 81.1 | 93.8 | 82.3 |
| 11 | 81.3 | 93.6 | 82.1 |
| 12 | 81.6 | 93.4 | 82.0 |
| 13 | 81.4 | 93.7 | 82.4 |
| 14 | 81.6 | 93.6 | 82.3 |
| 15 | 81.5 | 93.5 | 82.4 |

pLDDT 72.8–81.6; JH2–JH1 46.5–55.8 Å; FERM–JH1 31.8–93.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 16 | 32 40 94 93 93 94 93 94 94 94 94 93 94 94 94 | open-like (> 80) |
