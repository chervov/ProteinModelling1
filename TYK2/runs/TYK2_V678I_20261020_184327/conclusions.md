# TYK2_V678I_20261020_184327 — TYK2 V678I_free_msa64-256_s0-7

TYK2 V678I at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678I is +0.520. bulky aliphatic, activating in the DMS and NOT destabilising (abundance -0.088); predict it abolishes the closed state like F does. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 81 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 80.3 | 51.7 | 59.1 | 60.4 | AF2 |
| 1 | 12 | 80.4 | 50.3 | 58.8 | 62.1 | AF2 |
| 2 | 12 | 80.5 | 49.6 | 64.4 | 70.1 | AF2 |
| 3 | 12 | 81.0 | 50.3 | 94.1 | 90.6 | AF2 |
| 4 | 9 | 80.6 | 49.7 | 94.5 | 89.2 | AF2 |
| 5 | 4 | 80.4 | 49.0 | 43.3 | 38.8 | AF2 |
| 6 | 9 | 80.8 | 49.4 | 91.2 | 90.9 | AF2 |
| 7 | 12 | 80.3 | 49.7 | 93.9 | 90.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 25.0 | 0 | 2 | 76.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 65.8 | 51.3 | 64.7 |
| 2 | 76.0 | 35.9 | 36.5 |
| 3 | 79.7 | 47.0 | 46.4 |
| 4 | 80.2 | 54.4 | 55.8 |
| 5 | 80.2 | 60.3 | 63.4 |
| 6 | 80.1 | 71.0 | 72.8 |
| 7 | 80.3 | 78.1 | 78.4 |
| 8 | 80.0 | 74.6 | 72.4 |
| 9 | 80.3 | 78.0 | 77.0 |
| 10 | 79.8 | 76.5 | 74.7 |
| 11 | 79.9 | 75.7 | 73.5 |
| 12 | 80.4 | 74.6 | 72.8 |
| 13 | 80.1 | 74.4 | 71.8 |
| 14 | 79.9 | 80.7 | 78.8 |
| 15 | 80.3 | 75.3 | 72.5 |

pLDDT 65.1–81.0; JH2–JH1 37.3–57.4 Å; FERM–JH1 29.7–95.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 48 30 52 59 63 59 60 58 65 61 59 56 55 73 58 | in between |
| 1 | 54 39 45 51 57 57 70 53 57 60 59 59 60 72 58 | in between |
| 2 | 50 32 48 51 56 83 87 67 82 71 65 64 62 80 64 | in between |
| 3 | 53 38 48 71 92 95 96 95 95 95 96 94 94 95 95 | open-like (> 80) |
| 4 | 56 37 48 50 54 76 92 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 5 | 55 44 41 43 46 44 43 44 44 44 44 42 44 43 44 | closed-like (< 50) |
| 6 | 44 31 45 52 54 66 84 90 91 93 94 92 93 93 94 | open-like (> 80) |
| 7 | 52 36 49 57 61 88 94 94 95 94 94 94 95 95 95 | open-like (> 80) |
