# JAK3_R657Q_20261019_113206 — JAK3 R657Q_msa128-512_s8-15

JAK3 R657Q, a reported activating JAK3 mutation in the JH2 pseudokinase domain (T-ALL, ETP-ALL). MSA 128/512, seeds 8-15. Split into 8-seed halves: molab sandboxes died at 3h11m and 2h59m, and a 16-seed run takes 2h10m plus setup, so halves are restart-safe. Paired with wild type JAK3_20261016_125830 (16 seeds, all compact, max 56 A).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 4 | 84.3 | 64.7 | 54.7 | 92.3 | AF2 |
| 9 | 4 | 84.4 | 67.4 | 51.7 | 91.0 | AF2 |
| 10 | 3 | 84.5 | 65.6 | 50.6 | 89.0 | AF2 |
| 11 | 13 | 84.6 | 62.2 | 52.0 | 88.9 | AF2 |
| 12 | 12 | 84.5 | 62.1 | 51.8 | 89.1 | AF2 |
| 13 | 14 | 84.3 | 62.4 | 52.0 | 89.3 | AF2 |
| 14 | 12 | 84.4 | 66.0 | 51.9 | 90.5 | AF2 |
| 15 | 12 | 84.5 | 62.5 | 52.0 | 89.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 53.5 | 13 | 1 | 77.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.7 | 61.3 | 80.6 |
| 2 | 84.1 | 57.6 | 92.4 |
| 3 | 84.3 | 52.9 | 90.3 |
| 4 | 84.2 | 51.9 | 90.3 |
| 5 | 84.2 | 51.8 | 89.8 |
| 6 | 84.2 | 52.2 | 89.7 |
| 7 | 84.2 | 51.4 | 89.3 |
| 8 | 84.0 | 52.3 | 89.2 |
| 9 | 84.1 | 50.8 | 88.9 |
| 10 | 84.2 | 51.4 | 89.1 |
| 11 | 84.3 | 52.1 | 88.6 |
| 12 | 84.4 | 51.5 | 89.4 |
| 13 | 84.3 | 52.0 | 89.0 |
| 14 | 84.2 | 52.1 | 89.6 |
| 15 | 84.1 | 52.2 | 89.4 |

pLDDT 77.5–84.6; JH2–JH1 34.8–67.4 Å; FERM–JH1 47.0–69.6 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 62 59 53 55 53 52 51 54 52 53 53 53 52 51 52 | in between |
| 9 | 68 57 52 52 50 51 50 51 51 50 50 51 51 51 52 | in between |
| 10 | 56 55 51 51 52 51 50 51 51 51 52 51 52 51 51 | in between |
| 11 | 70 61 53 53 52 52 51 53 52 52 52 51 52 53 53 | in between |
| 12 | 57 59 53 53 52 53 52 53 50 51 52 52 53 53 53 | in between |
| 13 | 47 56 53 50 52 53 52 52 49 50 52 50 52 52 53 | in between |
| 14 | 64 54 53 50 53 53 52 52 51 52 53 52 52 52 52 | in between |
| 15 | 67 60 54 51 52 52 52 52 51 52 53 52 53 54 53 | in between |
