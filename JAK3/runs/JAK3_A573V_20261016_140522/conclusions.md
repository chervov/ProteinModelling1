# JAK3_A573V_20261016_140522 — JAK3 A573V_msa128-512

JAK3 A573V, no template, MSA 128/512, 16 seeds. Known activating JAK3 mutation (JH2 pseudokinase; T-ALL, NKTCL).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 128 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 84.3 | 53.6 | 48.1 | 80.4 | AF2 |
| 1 | 15 | 84.3 | 53.7 | 46.9 | 78.2 | AF2 |
| 2 | 6 | 83.7 | 38.3 | 42.2 | 2.5 | AF2 |
| 3 | 6 | 83.9 | 38.3 | 42.2 | 1.8 | AF2 |
| 4 | 3 | 83.4 | 42.7 | 43.4 | 8.7 | AF2 |
| 5 | 10 | 83.9 | 51.3 | 53.8 | 64.4 | AF2 |
| 6 | 3 | 83.5 | 43.9 | 43.9 | 11.7 | AF2 |
| 7 | 6 | 83.6 | 38.6 | 42.9 | 2.0 | AF2 |
| 8 | 9 | 84.4 | 50.4 | 50.3 | 78.8 | AF2 |
| 9 | 4 | 83.0 | 38.9 | 42.4 | 2.0 | AF2 |
| 10 | 6 | 83.7 | 38.0 | 41.7 | 2.3 | AF2 |
| 11 | 3 | 83.3 | 41.6 | 43.5 | 7.1 | AF2 |
| 12 | 6 | 83.6 | 38.8 | 42.5 | 1.9 | AF2 |
| 13 | 6 | 83.9 | 38.1 | 42.1 | 2.1 | AF2 |
| 14 | 15 | 83.4 | 37.9 | 41.6 | 2.3 | AF2 |
| 15 | 6 | 83.4 | 38.0 | 41.8 | 2.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 0.9 | 3 | 10 | 83.5 | 167 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.3 | 50.5 | 47.5 |
| 2 | 83.2 | 48.0 | 30.9 |
| 3 | 83.5 | 44.6 | 22.1 |
| 4 | 83.4 | 44.0 | 20.7 |
| 5 | 83.4 | 44.4 | 20.6 |
| 6 | 83.6 | 44.3 | 19.1 |
| 7 | 83.4 | 43.9 | 18.3 |
| 8 | 83.4 | 44.6 | 18.6 |
| 9 | 83.5 | 44.1 | 19.9 |
| 10 | 83.5 | 43.7 | 20.0 |
| 11 | 83.3 | 43.8 | 20.0 |
| 12 | 83.2 | 43.8 | 18.8 |
| 13 | 83.5 | 43.9 | 19.9 |
| 14 | 83.4 | 43.8 | 20.0 |
| 15 | 83.5 | 43.6 | 20.1 |

pLDDT 76.6–84.4; JH2–JH1 24.2–55.8 Å; FERM–JH1 41.1–62.4 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 240.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 62 52 49 48 50 47 49 49 48 47 48 48 47 46 47 | closed-like (< 50) |
| 1 | 62 54 51 50 50 49 49 51 48 49 48 47 48 46 47 | closed-like (< 50) |
| 2 | 44 45 42 41 42 42 42 42 42 42 42 42 42 42 42 | closed-like (< 50) |
| 3 | 49 46 42 42 42 42 42 42 42 42 42 42 42 42 42 | closed-like (< 50) |
| 4 | 46 52 43 42 43 43 42 43 43 42 43 42 42 42 42 | closed-like (< 50) |
| 5 | 50 52 53 53 54 55 53 55 53 54 53 51 53 53 52 | in between |
| 6 | 52 47 44 43 43 43 42 43 43 42 42 43 43 43 42 | closed-like (< 50) |
| 7 | 42 45 43 42 43 43 42 43 43 42 42 42 42 42 42 | closed-like (< 50) |
| 8 | 55 57 52 51 50 49 51 53 50 50 50 50 50 49 50 | in between |
| 9 | 55 46 42 42 42 42 42 42 42 42 42 42 42 42 42 | closed-like (< 50) |
| 10 | 44 43 42 41 42 42 41 41 42 41 41 42 41 42 41 | closed-like (< 50) |
| 11 | 54 48 44 42 42 42 42 42 43 42 42 42 42 43 42 | closed-like (< 50) |
| 12 | 55 46 43 42 43 42 42 42 42 42 42 42 42 42 42 | closed-like (< 50) |
| 13 | 48 45 42 41 42 42 42 42 42 41 41 42 42 42 41 | closed-like (< 50) |
| 14 | 43 44 42 41 41 42 41 42 42 42 42 42 42 42 42 | closed-like (< 50) |
| 15 | 47 44 42 41 42 42 41 42 42 41 41 42 42 42 41 | closed-like (< 50) |
