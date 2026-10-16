# JAK3_A572V_20261016_181046 — JAK3 A572V_msa128-512_s0-7

JAK3 A572V, the canonical activating JAK3 pseudokinase mutation (Walters et al., Cancer Cell 2006; acute megakaryoblastic leukaemia, transforms Ba/F3 cells to factor-independent growth). JAK3 has adjacent alanines at 572 and 573; the earlier A573V run used the neighbour, which is not the reported allele. MSA 128/512, seeds 0-7. Split into 8-seed halves: molab sandboxes died at 3h11m and 2h59m, and a 16-seed run takes 2h10m plus setup, so halves are restart-safe. Paired with wild type JAK3_20261016_125830 (16 seeds, all compact, max 56 A).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 128 clusters / 512 extra; no template. Run time 70 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 13 | 84.4 | 63.3 | 54.2 | 91.1 | AF2 |
| 1 | 2 | 84.1 | 63.6 | 58.3 | 92.4 | AF2 |
| 2 | 3 | 84.3 | 64.0 | 56.6 | 91.5 | AF2 |
| 3 | 4 | 84.2 | 64.1 | 54.1 | 90.9 | AF2 |
| 4 | 12 | 84.4 | 60.9 | 63.1 | 93.4 | AF2 |
| 5 | 3 | 84.4 | 62.7 | 54.0 | 90.3 | AF2 |
| 6 | 3 | 84.7 | 59.4 | 56.0 | 89.3 | AF2 |
| 7 | 8 | 84.7 | 64.8 | 49.4 | 88.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 12.5 | 3 | 11 | 82.8 | 1 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.0 | 41.9 | 67.4 |
| 2 | 84.1 | 56.6 | 90.1 |
| 3 | 84.4 | 55.5 | 90.7 |
| 4 | 84.1 | 55.8 | 91.0 |
| 5 | 83.9 | 55.0 | 90.6 |
| 6 | 84.2 | 56.5 | 91.0 |
| 7 | 84.0 | 55.5 | 87.1 |
| 8 | 84.2 | 55.2 | 87.0 |
| 9 | 83.8 | 55.8 | 91.2 |
| 10 | 84.1 | 55.5 | 90.3 |
| 11 | 83.8 | 54.0 | 75.5 |
| 12 | 84.1 | 56.7 | 90.7 |
| 13 | 84.2 | 56.1 | 89.8 |
| 14 | 84.0 | 54.2 | 89.7 |
| 15 | 83.9 | 53.6 | 77.1 |

pLDDT 76.4–84.7; JH2–JH1 37.5–68.5 Å; FERM–JH1 26.2–65.7 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 26 55 55 54 54 56 56 54 56 55 54 56 54 52 51 | in between |
| 1 | 32 58 61 61 58 60 60 60 59 60 60 62 60 60 59 | in between |
| 2 | 39 61 57 58 57 59 57 57 57 59 57 59 58 57 58 | in between |
| 3 | 44 61 50 54 52 53 50 50 52 54 45 53 56 51 46 | closed-like (< 50) |
| 4 | 53 66 62 60 59 61 60 60 61 59 59 63 60 57 57 | in between |
| 5 | 34 50 54 54 54 55 55 53 54 54 54 55 54 54 54 | in between |
| 6 | 51 64 56 56 56 57 58 57 58 55 56 58 58 56 55 | in between |
| 7 | 57 37 49 49 50 50 48 49 48 48 47 47 50 47 48 | closed-like (< 50) |
