# JAK3_M511I_20261016_191613 — JAK3 M511I_msa128-512_s0-7

JAK3 M511I, a reported activating JAK3 mutation in the SH2-JH2 linker, the most frequent JAK3 hotspot in T-ALL. MSA 128/512, seeds 0-7. Split into 8-seed halves: molab sandboxes died at 3h11m and 2h59m, and a 16-seed run takes 2h10m plus setup, so halves are restart-safe. Paired with wild type JAK3_20261016_125830 (16 seeds, all compact, max 56 A).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 128 clusters / 512 extra; no template. Run time 63 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 84.5 | 56.4 | 53.2 | 85.9 | AF2 |
| 1 | 15 | 84.3 | 52.9 | 53.0 | 83.6 | AF2 |
| 2 | 10 | 84.3 | 63.5 | 53.6 | 90.3 | AF2 |
| 3 | 9 | 84.3 | 62.2 | 53.3 | 89.5 | AF2 |
| 4 | 3 | 84.0 | 48.2 | 44.8 | 22.0 | AF2 |
| 5 | 8 | 84.2 | 62.0 | 52.8 | 88.5 | AF2 |
| 6 | 3 | 84.1 | 61.1 | 54.8 | 90.1 | AF2 |
| 7 | 11 | 84.5 | 60.8 | 53.2 | 89.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 8.5 | 4 | 15 | 83.8 | 9 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 77.7 | 46.5 | 73.0 |
| 2 | 83.8 | 54.3 | 82.0 |
| 3 | 84.1 | 53.1 | 80.7 |
| 4 | 84.0 | 53.2 | 74.8 |
| 5 | 83.6 | 52.2 | 78.6 |
| 6 | 83.9 | 52.0 | 77.3 |
| 7 | 83.9 | 52.6 | 78.5 |
| 8 | 84.0 | 52.4 | 78.2 |
| 9 | 83.9 | 51.0 | 75.3 |
| 10 | 83.7 | 52.0 | 67.2 |
| 11 | 84.1 | 52.8 | 77.5 |
| 12 | 83.9 | 50.5 | 63.1 |
| 13 | 83.6 | 51.3 | 67.5 |
| 14 | 83.5 | 49.1 | 62.2 |
| 15 | 83.8 | 51.8 | 66.9 |

pLDDT 76.8–84.5; JH2–JH1 41.9–64.8 Å; FERM–JH1 24.6–61.4 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 58 52 53 53 52 52 53 52 53 54 53 53 53 50 52 | in between |
| 1 | 52 61 53 55 54 54 54 54 54 54 55 54 55 53 53 | in between |
| 2 | 48 54 55 52 53 53 53 53 50 54 53 52 54 52 53 | in between |
| 3 | 51 60 55 54 51 50 53 54 53 53 54 53 52 51 51 | in between |
| 4 | 25 41 45 44 44 43 43 44 44 44 44 44 44 43 44 | closed-like (< 50) |
| 5 | 48 56 55 54 53 53 53 53 45 50 54 45 45 46 52 | in between |
| 6 | 39 54 55 58 57 56 57 55 56 56 58 54 57 55 57 | in between |
| 7 | 52 57 55 57 54 55 55 54 52 51 53 50 50 42 52 | in between |
