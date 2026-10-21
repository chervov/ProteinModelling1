# TYK2_V678D_20261021_074240 — TYK2 V678D_free_msa64-256_s8-15

TYK2 V678D at 64/256, seeds 8-15. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678D is -0.479. small and charged; equal-strongest loss of signalling. Second test of the reversed direction. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 75 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 11 | 80.7 | 50.6 | 86.2 | 88.4 | AF2 |
| 9 | 6 | 80.5 | 47.0 | 93.6 | 82.9 | AF2 |
| 10 | 6 | 80.1 | 49.0 | 94.6 | 87.2 | AF2 |
| 11 | 4 | 80.5 | 50.8 | 95.1 | 91.0 | AF2 |
| 12 | 6 | 80.3 | 47.6 | 93.9 | 84.4 | AF2 |
| 13 | 6 | 80.5 | 50.3 | 95.0 | 90.1 | AF2 |
| 14 | 6 | 80.6 | 50.5 | 90.0 | 91.9 | AF2 |
| 15 | 6 | 80.3 | 47.4 | 93.9 | 83.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 34.3 | 11 | 2 | 75.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 64.3 | 48.9 | 83.2 |
| 2 | 75.4 | 43.3 | 58.5 |
| 3 | 79.1 | 75.0 | 75.6 |
| 4 | 80.2 | 84.5 | 82.0 |
| 5 | 79.7 | 87.4 | 81.9 |
| 6 | 80.4 | 89.2 | 83.7 |
| 7 | 79.8 | 92.7 | 85.6 |
| 8 | 79.8 | 92.6 | 84.8 |
| 9 | 79.9 | 90.4 | 83.4 |
| 10 | 79.9 | 92.4 | 84.7 |
| 11 | 80.1 | 93.2 | 85.0 |
| 12 | 79.8 | 94.3 | 85.1 |
| 13 | 79.9 | 94.4 | 85.9 |
| 14 | 80.1 | 94.3 | 86.1 |
| 15 | 79.9 | 94.2 | 85.5 |

pLDDT 63.2–80.7; JH2–JH1 38.3–57.6 Å; FERM–JH1 34.4–95.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 49 42 40 44 50 57 82 82 63 80 86 96 95 95 95 | open-like (> 80) |
| 9 | 56 56 95 94 94 94 94 94 94 94 94 94 94 94 93 | open-like (> 80) |
| 10 | 56 50 62 94 94 95 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 11 | 38 34 81 95 95 95 94 94 95 95 94 94 94 95 94 | open-like (> 80) |
| 12 | 66 38 93 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 13 | 44 39 92 94 94 95 94 94 95 94 95 94 95 94 94 | open-like (> 80) |
| 14 | 45 38 51 66 85 90 95 96 95 96 96 95 95 95 95 | open-like (> 80) |
| 15 | 37 49 86 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
