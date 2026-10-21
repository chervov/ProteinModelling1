# TYK2_V678D_20261021_074015 — TYK2 V678D_free_msa64-256_s0-7

TYK2 V678D at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678D is -0.479. small and charged; equal-strongest loss of signalling. Second test of the reversed direction. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 15 | 80.6 | 51.9 | 79.9 | 86.9 | AF2 |
| 1 | 4 | 80.0 | 50.9 | 47.3 | 44.4 | AF2 |
| 2 | 15 | 80.6 | 52.4 | 94.4 | 93.7 | AF2 |
| 3 | 15 | 80.8 | 53.2 | 95.2 | 95.3 | AF2 |
| 4 | 15 | 80.2 | 50.0 | 94.7 | 89.7 | AF2 |
| 5 | 4 | 80.8 | 54.9 | 47.4 | 55.5 | AF2 |
| 6 | 4 | 80.4 | 48.8 | 46.1 | 41.1 | AF2 |
| 7 | 4 | 79.9 | 43.1 | 41.8 | 23.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 15.9 | 7 | 13 | 79.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 65.4 | 55.9 | 57.4 |
| 2 | 76.6 | 40.6 | 39.1 |
| 3 | 79.8 | 44.9 | 48.6 |
| 4 | 80.2 | 54.3 | 57.3 |
| 5 | 80.0 | 63.0 | 61.1 |
| 6 | 79.9 | 66.8 | 64.7 |
| 7 | 80.0 | 62.0 | 59.8 |
| 8 | 79.9 | 68.0 | 66.1 |
| 9 | 80.0 | 64.1 | 61.8 |
| 10 | 79.9 | 64.0 | 61.5 |
| 11 | 80.0 | 66.5 | 63.7 |
| 12 | 80.1 | 66.0 | 64.6 |
| 13 | 80.0 | 66.0 | 61.1 |
| 14 | 80.0 | 67.6 | 64.9 |
| 15 | 80.3 | 69.7 | 66.0 |

pLDDT 64.0–80.8; JH2–JH1 40.5–67.4 Å; FERM–JH1 36.3–95.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 54 40 46 53 54 57 52 55 54 53 54 56 57 61 80 | in between |
| 1 | 56 44 43 47 52 54 50 59 51 52 51 52 50 51 50 | in between |
| 2 | 56 36 47 75 91 92 93 93 91 92 94 92 90 92 94 | open-like (> 80) |
| 3 | 55 39 49 60 78 82 67 88 75 75 86 82 94 94 95 | open-like (> 80) |
| 4 | 58 38 50 63 81 86 89 92 92 94 95 94 94 94 95 | open-like (> 80) |
| 5 | 50 44 43 47 59 72 56 66 59 58 62 61 54 60 54 | in between |
| 6 | 61 41 42 46 48 49 48 48 49 47 49 49 47 47 48 | closed-like (< 50) |
| 7 | 57 42 39 42 42 42 42 42 42 41 42 41 41 42 42 | closed-like (< 50) |
