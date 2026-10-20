# TYK2_V678I_20261020_212231 — TYK2 V678I_free_msa64-256_s8-15

TYK2 V678I at 64/256, seeds 8-15. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678I is +0.520. bulky aliphatic, activating in the DMS and NOT destabilising (abundance -0.088); predict it abolishes the closed state like F does. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 70 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 9 | 80.5 | 49.1 | 95.3 | 87.2 | AF2 |
| 9 | 9 | 80.9 | 47.9 | 94.3 | 85.2 | AF2 |
| 10 | 9 | 80.9 | 49.5 | 95.5 | 87.8 | AF2 |
| 11 | 4 | 78.9 | 42.2 | 44.1 | 40.1 | AF2 |
| 12 | 9 | 80.9 | 46.8 | 93.8 | 82.3 | AF2 |
| 13 | 8 | 80.9 | 48.9 | 88.7 | 91.1 | AF2 |
| 14 | 9 | 79.5 | 44.7 | 42.9 | 28.9 | AF2 |
| 15 | 9 | 80.5 | 49.8 | 92.5 | 91.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 24.1 | 14 | 6 | 78.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.3 | 51.6 | 58.3 |
| 2 | 76.5 | 47.1 | 41.8 |
| 3 | 77.8 | 40.4 | 44.0 |
| 4 | 79.4 | 51.6 | 53.5 |
| 5 | 79.9 | 63.3 | 66.9 |
| 6 | 79.9 | 68.0 | 70.0 |
| 7 | 79.8 | 73.7 | 73.9 |
| 8 | 80.2 | 76.1 | 74.4 |
| 9 | 80.3 | 81.0 | 73.4 |
| 10 | 80.0 | 80.8 | 72.9 |
| 11 | 80.0 | 81.1 | 73.0 |
| 12 | 80.0 | 80.9 | 72.4 |
| 13 | 80.2 | 80.8 | 72.8 |
| 14 | 79.8 | 80.9 | 72.2 |
| 15 | 80.2 | 80.5 | 72.7 |

pLDDT 68.1–80.9; JH2–JH1 42.1–67.8 Å; FERM–JH1 27.7–95.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 52 45 40 42 61 72 84 82 95 95 95 94 95 94 94 | open-like (> 80) |
| 9 | 49 47 28 58 85 91 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 10 | 49 46 38 44 60 54 68 86 96 95 95 94 94 94 94 | open-like (> 80) |
| 11 | 52 46 28 44 39 38 38 38 39 39 38 39 38 39 40 | closed-like (< 50) |
| 12 | 54 49 76 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 13 | 57 46 40 45 68 75 81 89 94 91 94 93 92 94 91 | open-like (> 80) |
| 14 | 54 49 33 39 41 41 41 41 43 44 44 44 43 43 42 | closed-like (< 50) |
| 15 | 47 49 41 46 57 78 89 85 92 94 95 95 95 95 95 | open-like (> 80) |
