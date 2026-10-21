# TYK2_V678A_20261021_040215 — TYK2 V678A_free_msa64-256_s0-7

TYK2 V678A at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678A is -0.228. small; LOSS of signalling in the DMS. Predict it preserves or tightens the closed state - the opposite direction, which no variant in this project has yet shown. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 84 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 80.3 | 50.1 | 48.9 | 53.7 | AF2 |
| 1 | 10 | 80.3 | 51.0 | 54.6 | 57.6 | AF2 |
| 2 | 5 | 80.2 | 50.7 | 50.9 | 55.1 | AF2 |
| 3 | 7 | 81.0 | 51.3 | 93.3 | 93.1 | AF2 |
| 4 | 15 | 80.5 | 47.0 | 93.7 | 83.6 | AF2 |
| 5 | 11 | 80.7 | 49.8 | 93.5 | 91.0 | AF2 |
| 6 | 12 | 80.8 | 50.0 | 91.9 | 91.3 | AF2 |
| 7 | 15 | 80.3 | 49.9 | 51.4 | 52.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 35.0 | 7 | 2 | 75.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 66.9 | 28.3 | 46.7 |
| 2 | 75.4 | 34.4 | 44.2 |
| 3 | 78.6 | 50.2 | 54.2 |
| 4 | 80.2 | 54.2 | 59.3 |
| 5 | 80.1 | 55.2 | 59.6 |
| 6 | 80.2 | 63.2 | 65.4 |
| 7 | 80.3 | 73.1 | 76.4 |
| 8 | 80.1 | 72.3 | 72.5 |
| 9 | 79.7 | 71.2 | 70.7 |
| 10 | 80.1 | 72.3 | 71.2 |
| 11 | 80.4 | 73.0 | 71.3 |
| 12 | 80.4 | 73.2 | 71.2 |
| 13 | 80.2 | 78.4 | 76.9 |
| 14 | 80.2 | 73.2 | 72.8 |
| 15 | 80.3 | 74.1 | 72.5 |

pLDDT 66.1–81.0; JH2–JH1 36.8–61.3 Å; FERM–JH1 6.7–95.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 39 36 46 52 52 51 52 49 49 49 49 49 55 51 51 | in between |
| 1 | 16 40 45 46 47 50 66 58 42 55 56 59 81 56 61 | in between |
| 2 | 35 23 44 48 51 51 53 50 50 49 48 51 59 52 52 | in between |
| 3 | 42 24 46 54 56 81 93 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 4 | 22 39 88 91 91 93 94 95 95 95 95 94 94 94 94 | open-like (> 80) |
| 5 | 18 38 45 50 52 70 90 94 94 92 94 95 95 94 95 | open-like (> 80) |
| 6 | 47 33 44 46 47 57 84 92 93 92 94 92 94 93 94 | open-like (> 80) |
| 7 | 7 41 43 47 46 51 52 45 51 52 53 51 54 52 51 | in between |
