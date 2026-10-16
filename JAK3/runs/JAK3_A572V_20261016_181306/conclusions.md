# JAK3_A572V_20261016_181306 — JAK3 A572V_msa128-512_s8-15

JAK3 A572V, the canonical activating JAK3 pseudokinase mutation (Walters et al., Cancer Cell 2006; acute megakaryoblastic leukaemia, transforms Ba/F3 cells to factor-independent growth). JAK3 has adjacent alanines at 572 and 573; the earlier A573V run used the neighbour, which is not the reported allele. MSA 128/512, seeds 8-15. Split into 8-seed halves: molab sandboxes died at 3h11m and 2h59m, and a 16-seed run takes 2h10m plus setup, so halves are restart-safe. Paired with wild type JAK3_20261016_125830 (16 seeds, all compact, max 56 A).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 63 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 9 | 84.4 | 51.1 | 47.9 | 49.8 | AF2 |
| 9 | 8 | 84.2 | 47.0 | 52.0 | 60.6 | AF2 |
| 10 | 14 | 84.5 | 49.7 | 51.1 | 79.1 | AF2 |
| 11 | 4 | 84.1 | 48.2 | 52.8 | 58.4 | AF2 |
| 12 | 15 | 84.5 | 49.2 | 55.9 | 80.3 | AF2 |
| 13 | 9 | 84.0 | 46.4 | 44.6 | 17.8 | AF2 |
| 14 | 14 | 84.3 | 53.0 | 47.8 | 47.7 | AF2 |
| 15 | 2 | 84.0 | 51.8 | 46.5 | 33.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 7.5 | 13 | 12 | 83.4 | 11 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.4 | 43.6 | 54.9 |
| 2 | 83.8 | 52.6 | 58.0 |
| 3 | 84.0 | 49.9 | 49.9 |
| 4 | 83.8 | 50.0 | 51.2 |
| 5 | 84.0 | 50.0 | 51.2 |
| 6 | 84.0 | 49.0 | 51.2 |
| 7 | 83.8 | 50.0 | 52.1 |
| 8 | 83.9 | 49.7 | 51.3 |
| 9 | 84.1 | 49.4 | 47.9 |
| 10 | 83.9 | 49.5 | 51.2 |
| 11 | 83.8 | 49.9 | 50.2 |
| 12 | 83.9 | 49.3 | 47.2 |
| 13 | 83.9 | 48.9 | 48.9 |
| 14 | 84.1 | 48.9 | 45.0 |
| 15 | 84.0 | 48.3 | 42.5 |

pLDDT 77.9–84.5; JH2–JH1 41.9–54.9 Å; FERM–JH1 32.2–62.2 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 46 55 47 48 48 48 47 48 48 50 48 48 47 48 47 | closed-like (< 50) |
| 9 | 38 51 50 50 52 51 53 52 49 51 52 51 51 50 50 | in between |
| 10 | 50 62 56 55 54 53 56 56 55 54 57 55 51 51 50 | in between |
| 11 | 43 49 52 53 52 51 52 51 52 52 52 51 51 52 52 | in between |
| 12 | 44 57 57 55 56 55 55 57 54 54 58 55 56 56 56 | in between |
| 13 | 52 47 43 45 45 43 45 43 45 44 44 44 44 44 45 | closed-like (< 50) |
| 14 | 32 53 51 51 50 50 49 48 49 49 47 48 48 48 45 | closed-like (< 50) |
| 15 | 44 46 42 43 43 42 43 43 44 44 42 43 43 43 43 | closed-like (< 50) |
