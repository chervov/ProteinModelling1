# JAK3_R657Q_20261019_112943 — JAK3 R657Q_msa128-512_s0-7

JAK3 R657Q, a reported activating JAK3 mutation in the JH2 pseudokinase domain (T-ALL, ETP-ALL). MSA 128/512, seeds 0-7. Split into 8-seed halves: molab sandboxes died at 3h11m and 2h59m, and a 16-seed run takes 2h10m plus setup, so halves are restart-safe. Paired with wild type JAK3_20261016_125830 (16 seeds, all compact, max 56 A).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 128 clusters / 512 extra; no template. Run time 3 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 83.9 | 40.3 | 41.8 | 3.7 | AF2 |
| 1 | 15 | 84.4 | 63.5 | 49.8 | 88.6 | AF2 |
| 2 | 10 | 83.5 | 38.4 | 42.7 | 2.0 | AF2 |
| 3 | 7 | 83.5 | 38.3 | 42.1 | 2.0 | AF2 |
| 4 | 11 | 84.5 | 66.5 | 51.3 | 91.0 | AF2 |
| 5 | 13 | 84.1 | 65.5 | 51.2 | 90.6 | AF2 |
| 6 | 14 | 83.5 | 37.8 | 42.4 | 3.0 | AF2 |
| 7 | 8 | 84.2 | 59.8 | 45.5 | 82.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 1.6 | 3 | 14 | 83.4 | 55 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 77.2 | 29.4 | 28.0 |
| 2 | 83.0 | 49.4 | 48.5 |
| 3 | 83.8 | 48.0 | 46.2 |
| 4 | 83.5 | 47.6 | 46.2 |
| 5 | 83.6 | 48.1 | 46.4 |
| 6 | 83.7 | 47.1 | 45.7 |
| 7 | 83.6 | 47.8 | 46.2 |
| 8 | 83.6 | 47.4 | 46.4 |
| 9 | 83.5 | 47.2 | 46.3 |
| 10 | 83.8 | 47.1 | 45.6 |
| 11 | 83.8 | 46.0 | 45.3 |
| 12 | 83.6 | 46.6 | 45.8 |
| 13 | 83.7 | 46.1 | 45.5 |
| 14 | 83.8 | 46.3 | 45.3 |
| 15 | 83.7 | 45.5 | 45.1 |

pLDDT 75.9–84.5; JH2–JH1 37.8–66.5 Å; FERM–JH1 16.0–57.9 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 28 54 44 43 44 43 43 43 42 43 42 42 43 43 42 | closed-like (< 50) |
| 1 | 20 48 51 51 52 50 52 52 52 50 51 53 52 51 50 | in between |
| 2 | 42 46 42 42 43 42 42 42 42 43 42 43 42 42 42 | closed-like (< 50) |
| 3 | 37 51 44 43 43 43 42 42 42 42 43 43 42 42 43 | closed-like (< 50) |
| 4 | 23 51 55 57 58 56 58 58 56 57 51 50 49 51 49 | closed-like (< 50) |
| 5 | 16 50 52 54 54 53 55 53 54 54 52 52 51 51 50 | in between |
| 6 | 44 46 45 44 44 44 43 43 43 43 42 43 43 42 42 | closed-like (< 50) |
| 7 | 25 50 51 47 47 46 47 46 46 46 45 46 45 47 46 | closed-like (< 50) |
