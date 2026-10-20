# TYK2_V678W_20261020_224357 — TYK2 V678W_free_msa64-256_s0-7

TYK2 V678W at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678W is +0.227. largest side chain tested; activating in the DMS but also the most destabilising (abundance -0.361); separates size from fold integrity. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 80.3 | 49.8 | 90.0 | 91.4 | AF2 |
| 1 | 11 | 80.2 | 49.4 | 88.2 | 90.9 | AF2 |
| 2 | 7 | 80.4 | 47.3 | 72.3 | 77.8 | AF2 |
| 3 | 7 | 80.1 | 53.5 | 42.5 | 43.7 | AF2 |
| 4 | 7 | 80.4 | 49.1 | 90.6 | 89.9 | AF2 |
| 5 | 14 | 79.9 | 49.2 | 82.6 | 84.7 | AF2 |
| 6 | 7 | 80.2 | 53.1 | 53.7 | 60.2 | AF2 |
| 7 | 7 | 80.4 | 50.3 | 92.6 | 91.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 35.8 | 1 | 2 | 76.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 65.3 | 48.8 | 59.2 |
| 2 | 75.6 | 43.3 | 41.9 |
| 3 | 77.5 | 42.1 | 42.5 |
| 4 | 79.0 | 47.9 | 46.1 |
| 5 | 79.3 | 50.8 | 52.8 |
| 6 | 79.6 | 57.6 | 62.1 |
| 7 | 80.0 | 63.6 | 66.2 |
| 8 | 79.8 | 69.9 | 74.7 |
| 9 | 79.8 | 75.5 | 77.4 |
| 10 | 79.9 | 71.7 | 75.4 |
| 11 | 80.0 | 78.0 | 79.8 |
| 12 | 79.9 | 79.8 | 77.8 |
| 13 | 79.8 | 77.0 | 78.0 |
| 14 | 79.9 | 84.2 | 83.7 |
| 15 | 80.0 | 81.0 | 81.6 |

pLDDT 64.2–80.4; JH2–JH1 45.5–66.3 Å; FERM–JH1 35.8–94.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 54 41 44 50 51 46 47 54 61 75 90 95 93 94 93 | open-like (> 80) |
| 1 | 51 46 40 46 50 53 58 71 89 81 88 95 90 92 90 | open-like (> 80) |
| 2 | 36 44 41 46 49 63 72 80 84 78 81 88 80 84 82 | open-like (> 80) |
| 3 | 53 45 42 48 49 36 42 52 50 48 52 49 48 57 47 | closed-like (< 50) |
| 4 | 41 45 43 48 57 82 91 92 94 93 94 94 93 94 93 | open-like (> 80) |
| 5 | 52 41 40 47 46 48 52 57 54 50 58 63 61 83 93 | open-like (> 80) |
| 6 | 52 44 43 51 52 47 54 59 78 55 66 60 56 75 56 | in between |
| 7 | 52 40 44 46 53 87 93 94 94 94 94 95 94 95 94 | open-like (> 80) |
