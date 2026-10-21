# TYK2_V678A_20261021_070859 — TYK2 V678A_free_msa64-256_s8-15

TYK2 V678A at 64/256, seeds 8-15. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678A is -0.228. small; LOSS of signalling in the DMS. Predict it preserves or tightens the closed state - the opposite direction, which no variant in this project has yet shown. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 82 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 13 | 80.5 | 47.1 | 93.5 | 83.5 | AF2 |
| 9 | 9 | 80.2 | 46.8 | 93.0 | 83.2 | AF2 |
| 10 | 13 | 80.3 | 47.0 | 93.3 | 83.5 | AF2 |
| 11 | 10 | 80.1 | 46.7 | 93.1 | 82.6 | AF2 |
| 12 | 10 | 80.7 | 47.2 | 93.3 | 84.0 | AF2 |
| 13 | 13 | 80.3 | 52.2 | 93.8 | 94.1 | AF2 |
| 14 | 9 | 80.3 | 47.1 | 93.4 | 83.7 | AF2 |
| 15 | 9 | 80.5 | 46.6 | 93.1 | 82.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 27.8 | 12 | 2 | 75.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 68.8 | 59.5 | 80.1 |
| 2 | 76.3 | 38.8 | 36.5 |
| 3 | 78.6 | 70.2 | 66.8 |
| 4 | 79.7 | 91.4 | 89.8 |
| 5 | 79.6 | 93.4 | 87.4 |
| 6 | 79.8 | 94.0 | 86.9 |
| 7 | 80.2 | 93.8 | 85.1 |
| 8 | 80.1 | 93.3 | 84.4 |
| 9 | 80.2 | 93.2 | 84.8 |
| 10 | 80.1 | 93.3 | 84.9 |
| 11 | 79.8 | 93.3 | 84.9 |
| 12 | 79.8 | 93.3 | 84.6 |
| 13 | 80.2 | 93.5 | 84.8 |
| 14 | 80.0 | 93.5 | 84.0 |
| 15 | 79.8 | 93.5 | 84.0 |

pLDDT 67.8–80.7; JH2–JH1 34.9–58.9 Å; FERM–JH1 33.4–94.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 55 35 67 94 94 94 94 93 93 94 94 93 94 93 93 | open-like (> 80) |
| 9 | 61 38 79 94 94 94 94 93 93 94 94 94 93 94 93 | open-like (> 80) |
| 10 | 56 37 56 93 94 94 93 93 93 93 94 93 93 93 93 | open-like (> 80) |
| 11 | 58 41 91 94 94 94 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 12 | 65 33 79 94 94 94 94 94 93 93 94 93 94 93 94 | open-like (> 80) |
| 13 | 60 38 56 92 93 93 95 94 94 93 92 94 94 95 95 | open-like (> 80) |
| 14 | 63 46 44 75 92 94 94 94 93 94 94 93 94 93 93 | open-like (> 80) |
| 15 | 60 41 91 94 93 94 94 93 93 93 93 93 94 93 93 | open-like (> 80) |
