# TYK2_V678M_20261020_102158 — TYK2 V678M_free_msa64-256_s0-7

TYK2 V678M. V678 is the position equivalent to JAK2 V617 and JAK1 V658. V678F, the substitution reported to raise TYK2 kinase activity, abolishes wild type partial approaches to the closed arrangement at 64/256 (90.7-94.8 A against wild type 41.2-92.0 A, p = 0.00012 at n=16). V678M installs methionine, which is what JAK3 carries natively at the equivalent position (M592) and which lacks the aromatic ring the V617F mechanism is thought to require. Position versus chemistry: if V678M does nothing while V678F does, the ring matters rather than the location. One of the seven variants supplied by the user. Seeds 0-7, at the depth where V678F gave its result.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 83 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 6 | 80.1 | 44.7 | 50.5 | 46.7 | AF2 |
| 1 | 11 | 80.2 | 50.4 | 91.1 | 90.8 | AF2 |
| 2 | 12 | 80.9 | 48.9 | 87.4 | 91.6 | AF2 |
| 3 | 9 | 80.8 | 45.2 | 80.9 | 85.9 | AF2 |
| 4 | 9 | 80.8 | 50.3 | 83.1 | 87.4 | AF2 |
| 5 | 15 | 80.2 | 44.2 | 71.6 | 78.4 | AF2 |
| 6 | 9 | 80.7 | 47.8 | 86.8 | 89.3 | AF2 |
| 7 | 15 | 80.6 | 44.5 | 80.1 | 84.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 15.9 | 5 | 4 | 79.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 67.8 | 43.2 | 46.6 |
| 2 | 76.0 | 35.7 | 32.3 |
| 3 | 79.7 | 45.9 | 38.4 |
| 4 | 79.9 | 57.1 | 52.6 |
| 5 | 79.7 | 61.3 | 58.0 |
| 6 | 80.1 | 63.4 | 59.6 |
| 7 | 79.7 | 64.8 | 58.4 |
| 8 | 80.0 | 64.7 | 61.2 |
| 9 | 80.3 | 66.7 | 63.6 |
| 10 | 80.2 | 72.4 | 71.4 |
| 11 | 80.1 | 77.4 | 75.8 |
| 12 | 80.4 | 76.9 | 77.9 |
| 13 | 80.2 | 78.1 | 78.0 |
| 14 | 80.3 | 82.2 | 82.7 |
| 15 | 80.3 | 81.2 | 82.4 |

pLDDT 66.6–80.9; JH2–JH1 31.9–57.6 Å; FERM–JH1 22.3–94.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 49 31 43 53 50 50 48 53 53 55 51 52 51 59 51 | in between |
| 1 | 43 37 42 46 53 53 57 58 63 74 91 93 94 94 94 | open-like (> 80) |
| 2 | 57 37 48 53 68 80 83 81 83 84 90 87 90 94 91 | open-like (> 80) |
| 3 | 30 34 50 80 81 83 84 82 81 82 82 80 81 85 82 | open-like (> 80) |
| 4 | 58 44 49 64 69 71 74 74 83 91 90 87 89 92 91 | open-like (> 80) |
| 5 | 29 42 41 41 41 42 42 42 42 47 48 51 52 60 72 | in between |
| 6 | 22 29 51 76 84 85 88 85 87 90 91 86 90 93 89 | open-like (> 80) |
| 7 | 56 31 43 43 44 43 43 43 42 56 77 79 79 80 80 | in between |
