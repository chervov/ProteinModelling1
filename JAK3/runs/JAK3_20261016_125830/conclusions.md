# JAK3_20261016_125830 — JAK3 WT_msa128-512

JAK3 wild type, no template, MSA 128/512, 16 seeds. JAK1: bistable (7 open, 6 next to FERM); JAK2: mostly detached JH1.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 131 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 83.8 | 46.3 | 43.1 | 19.7 | AF2 |
| 1 | 15 | 84.3 | 62.5 | 55.6 | 91.2 | AF2 |
| 2 | 4 | 83.9 | 54.9 | 54.8 | 57.6 | AF2 |
| 3 | 7 | 84.3 | 63.1 | 51.5 | 89.0 | AF2 |
| 4 | 12 | 84.0 | 46.8 | 46.1 | 19.7 | AF2 |
| 5 | 11 | 84.4 | 51.1 | 52.3 | 77.8 | AF2 |
| 6 | 11 | 84.3 | 49.7 | 56.3 | 67.0 | AF2 |
| 7 | 3 | 83.9 | 44.9 | 43.7 | 16.2 | AF2 |
| 8 | 12 | 84.2 | 62.7 | 54.2 | 90.9 | AF2 |
| 9 | 15 | 84.4 | 50.0 | 54.9 | 65.3 | AF2 |
| 10 | 12 | 83.9 | 45.0 | 43.2 | 15.9 | AF2 |
| 11 | 10 | 83.3 | 47.8 | 43.7 | 23.2 | AF2 |
| 12 | 15 | 84.1 | 50.1 | 53.7 | 71.3 | AF2 |
| 13 | 3 | 83.8 | 47.3 | 43.7 | 21.1 | AF2 |
| 14 | 11 | 84.2 | 50.6 | 53.9 | 67.7 | AF2 |
| 15 | 12 | 83.4 | 45.3 | 44.8 | 17.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 3.8 | 7 | 9 | 83.5 | 35 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 77.8 | 23.3 | 51.8 |
| 2 | 83.6 | 49.1 | 55.3 |
| 3 | 83.8 | 50.6 | 52.3 |
| 4 | 83.6 | 49.6 | 48.7 |
| 5 | 83.8 | 50.2 | 51.3 |
| 6 | 83.6 | 49.6 | 48.7 |
| 7 | 83.6 | 50.0 | 48.2 |
| 8 | 83.7 | 51.1 | 50.0 |
| 9 | 83.7 | 49.8 | 49.4 |
| 10 | 83.8 | 50.1 | 50.5 |
| 11 | 83.8 | 49.9 | 51.4 |
| 12 | 83.9 | 49.5 | 48.0 |
| 13 | 83.6 | 48.8 | 46.8 |
| 14 | 83.5 | 49.2 | 46.3 |
| 15 | 83.8 | 48.8 | 45.7 |

pLDDT 76.9–84.4; JH2–JH1 36.7–65.3 Å; FERM–JH1 16.2–64.9 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 240.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 20 50 44 45 45 43 43 44 43 43 43 43 44 44 42 | closed-like (< 50) |
| 1 | 16 25 55 56 58 55 58 58 56 60 56 58 55 56 56 | in between |
| 2 | 18 54 56 55 53 54 55 52 55 52 55 55 55 56 56 | in between |
| 3 | 32 49 49 50 51 52 52 51 51 53 53 53 51 50 51 | in between |
| 4 | 35 52 53 49 52 51 49 54 51 51 46 46 44 43 42 | closed-like (< 50) |
| 5 | 16 54 56 54 54 52 54 57 54 55 52 50 51 51 50 | in between |
| 6 | 29 55 54 56 56 57 60 57 57 56 56 55 54 53 54 | in between |
| 7 | 20 45 44 44 44 43 43 44 43 43 43 43 44 44 43 | closed-like (< 50) |
| 8 | 23 55 57 54 52 53 51 53 52 53 54 54 47 53 54 | in between |
| 9 | 24 55 53 48 52 52 52 53 49 52 54 56 53 53 55 | in between |
| 10 | 28 42 46 44 44 44 43 44 44 43 43 43 44 44 43 | closed-like (< 50) |
| 11 | 22 47 44 45 44 44 43 45 44 44 44 43 44 43 42 | closed-like (< 50) |
| 12 | 24 53 55 54 55 54 55 65 55 56 58 54 53 55 54 | in between |
| 13 | 22 46 44 43 43 43 43 43 43 43 43 43 44 43 42 | closed-like (< 50) |
| 14 | 19 51 53 52 52 52 53 54 53 54 54 52 54 56 55 | in between |
| 15 | 24 51 48 46 48 44 45 45 46 45 45 45 44 44 43 | closed-like (< 50) |
