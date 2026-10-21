# TYK2_V678L_20261021_034851 — TYK2 V678L_free_msa64-256_s0-7

TYK2 V678L at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678L is +0.145. bulky aliphatic, only weakly activating in the DMS; predict a weaker effect than I or M. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 80.3 | 50.3 | 92.0 | 91.3 | AF2 |
| 1 | 13 | 80.2 | 49.6 | 91.2 | 92.0 | AF2 |
| 2 | 5 | 80.3 | 51.7 | 91.6 | 93.3 | AF2 |
| 3 | 7 | 81.0 | 53.1 | 92.2 | 93.8 | AF2 |
| 4 | 9 | 81.0 | 50.6 | 87.5 | 90.3 | AF2 |
| 5 | 13 | 80.4 | 51.1 | 92.6 | 93.4 | AF2 |
| 6 | 8 | 80.5 | 50.4 | 94.3 | 91.2 | AF2 |
| 7 | 15 | 80.7 | 49.9 | 94.6 | 89.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 26.3 | 7 | 2 | 74.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 65.3 | 57.9 | 42.0 |
| 2 | 74.9 | 38.7 | 35.0 |
| 3 | 78.9 | 45.7 | 44.3 |
| 4 | 80.0 | 54.7 | 57.4 |
| 5 | 79.9 | 74.6 | 80.7 |
| 6 | 80.1 | 83.9 | 87.1 |
| 7 | 80.2 | 78.7 | 78.9 |
| 8 | 80.4 | 80.9 | 82.8 |
| 9 | 80.4 | 89.4 | 87.8 |
| 10 | 80.2 | 91.9 | 92.5 |
| 11 | 80.1 | 93.3 | 91.5 |
| 12 | 79.9 | 92.4 | 91.7 |
| 13 | 80.4 | 92.9 | 91.4 |
| 14 | 80.3 | 93.7 | 91.8 |
| 15 | 80.4 | 94.4 | 89.8 |

pLDDT 63.7–81.0; JH2–JH1 45.1–60.3 Å; FERM–JH1 20.1–95.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 61 45 46 54 76 84 58 70 92 94 95 94 95 95 95 | open-like (> 80) |
| 1 | 63 48 50 52 55 56 52 54 68 87 92 91 91 94 94 | open-like (> 80) |
| 2 | 60 40 41 69 92 95 92 93 95 94 94 93 94 95 95 | open-like (> 80) |
| 3 | 58 38 50 55 79 87 92 92 92 90 91 91 90 92 94 | open-like (> 80) |
| 4 | 57 20 48 61 73 81 62 65 88 92 94 91 92 91 94 | open-like (> 80) |
| 5 | 54 47 43 50 78 91 93 93 95 92 93 93 93 93 95 | open-like (> 80) |
| 6 | 55 49 44 48 71 91 94 94 95 94 94 94 94 95 95 | open-like (> 80) |
| 7 | 55 23 44 48 73 86 87 86 91 93 93 92 93 94 95 | open-like (> 80) |
