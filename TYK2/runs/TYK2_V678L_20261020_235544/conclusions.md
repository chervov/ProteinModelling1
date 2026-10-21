# TYK2_V678L_20261020_235544 — TYK2 V678L_free_msa64-256_s0-7

TYK2 V678L at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678L is +0.145. bulky aliphatic, only weakly activating in the DMS; predict a weaker effect than I or M. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 70 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 14 | 80.7 | 46.5 | 82.0 | 88.6 | AF2 |
| 1 | 6 | 79.9 | 39.8 | 40.6 | 11.9 | AF2 |
| 2 | 11 | 80.6 | 46.1 | 80.9 | 85.5 | AF2 |
| 3 | 9 | 80.7 | 46.4 | 83.8 | 86.7 | AF2 |
| 4 | 9 | 80.8 | 50.3 | 60.0 | 67.7 | AF2 |
| 5 | 8 | 79.7 | 40.2 | 40.5 | 13.8 | AF2 |
| 6 | 8 | 80.8 | 45.6 | 77.9 | 84.1 | AF2 |
| 7 | 14 | 81.1 | 46.2 | 81.6 | 86.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 8.9 | 5 | 11 | 79.4 | 23 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 63.9 | 52.4 | 56.0 |
| 2 | 75.2 | 43.4 | 47.8 |
| 3 | 77.6 | 34.9 | 29.6 |
| 4 | 79.3 | 50.7 | 44.9 |
| 5 | 80.0 | 58.6 | 56.5 |
| 6 | 80.2 | 62.9 | 60.0 |
| 7 | 80.0 | 65.9 | 61.6 |
| 8 | 80.4 | 66.6 | 62.8 |
| 9 | 80.2 | 67.5 | 64.9 |
| 10 | 80.2 | 69.6 | 66.4 |
| 11 | 80.3 | 67.4 | 64.0 |
| 12 | 80.1 | 67.9 | 65.7 |
| 13 | 80.3 | 70.1 | 65.2 |
| 14 | 80.4 | 69.7 | 65.5 |
| 15 | 80.4 | 69.8 | 67.0 |

pLDDT 63.5–81.1; JH2–JH1 38.6–55.4 Å; FERM–JH1 28.2–86.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 53 42 40 66 77 80 80 80 80 80 80 79 82 82 82 | open-like (> 80) |
| 1 | 50 43 35 41 40 41 40 40 40 40 40 41 41 40 41 | closed-like (< 50) |
| 2 | 52 44 38 40 50 63 69 74 78 80 81 82 85 84 84 | open-like (> 80) |
| 3 | 54 43 28 69 82 80 83 84 84 83 84 83 87 86 84 | open-like (> 80) |
| 4 | 54 44 34 49 52 54 56 56 60 73 57 63 61 64 64 | in between |
| 5 | 50 44 36 39 40 40 41 40 40 40 40 41 40 40 40 | closed-like (< 50) |
| 6 | 51 43 34 49 58 70 78 78 79 80 79 78 81 80 80 | in between |
| 7 | 55 44 35 53 68 76 80 81 79 81 78 78 84 82 84 | open-like (> 80) |
