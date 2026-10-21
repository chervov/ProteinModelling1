# TYK2_V678L_20261021_035113 — TYK2 V678L_free_msa64-256_s8-15

TYK2 V678L at 64/256, seeds 8-15. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678L is +0.145. bulky aliphatic, only weakly activating in the DMS; predict a weaker effect than I or M. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 14 | 80.9 | 51.6 | 87.4 | 91.7 | AF2 |
| 9 | 14 | 81.1 | 47.1 | 79.2 | 88.4 | AF2 |
| 10 | 14 | 81.0 | 51.5 | 94.9 | 92.7 | AF2 |
| 11 | 12 | 80.5 | 50.6 | 94.7 | 91.3 | AF2 |
| 12 | 12 | 80.9 | 49.7 | 87.5 | 91.8 | AF2 |
| 13 | 12 | 80.3 | 51.1 | 55.2 | 58.1 | AF2 |
| 14 | 14 | 80.7 | 50.5 | 87.0 | 92.6 | AF2 |
| 15 | 11 | 81.0 | 48.0 | 82.2 | 88.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 25.9 | 10 | 1 | 69.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.3 | 50.0 | 31.7 |
| 2 | 76.6 | 38.3 | 46.2 |
| 3 | 79.5 | 48.6 | 50.2 |
| 4 | 79.8 | 53.4 | 54.7 |
| 5 | 80.2 | 56.2 | 59.6 |
| 6 | 80.2 | 61.9 | 67.9 |
| 7 | 80.4 | 66.4 | 73.6 |
| 8 | 80.4 | 67.5 | 73.7 |
| 9 | 80.4 | 70.1 | 76.5 |
| 10 | 80.4 | 73.3 | 76.7 |
| 11 | 80.4 | 69.3 | 75.4 |
| 12 | 80.6 | 74.3 | 77.7 |
| 13 | 80.6 | 78.0 | 82.5 |
| 14 | 80.7 | 84.2 | 87.2 |
| 15 | 80.5 | 85.6 | 86.5 |

pLDDT 68.7–81.1; JH2–JH1 42.6–54.0 Å; FERM–JH1 27.8–95.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 53 40 48 49 55 59 58 54 56 58 54 57 63 87 94 | open-like (> 80) |
| 9 | 51 38 48 54 56 64 72 77 79 80 76 81 77 79 81 | open-like (> 80) |
| 10 | 46 43 41 45 53 54 59 59 59 60 57 67 87 95 95 | open-like (> 80) |
| 11 | 52 36 50 68 76 90 93 92 93 94 90 95 95 95 95 | open-like (> 80) |
| 12 | 53 28 48 53 53 59 66 70 77 84 81 88 89 90 89 | open-like (> 80) |
| 13 | 49 43 51 52 51 54 56 56 58 60 55 55 55 57 55 | in between |
| 14 | 46 45 58 54 54 58 61 60 62 64 59 65 74 87 91 | open-like (> 80) |
| 15 | 49 35 46 52 53 56 67 71 77 87 82 86 84 83 84 | open-like (> 80) |
