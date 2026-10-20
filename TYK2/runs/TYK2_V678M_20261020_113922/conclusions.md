# TYK2_V678M_20261020_113922 — TYK2 V678M_free_msa64-256_s8-15

TYK2 V678M. V678 is the position equivalent to JAK2 V617 and JAK1 V658. V678F, the substitution reported to raise TYK2 kinase activity, abolishes wild type partial approaches to the closed arrangement at 64/256 (90.7-94.8 A against wild type 41.2-92.0 A, p = 0.00012 at n=16). V678M installs methionine, which is what JAK3 carries natively at the equivalent position (M592) and which lacks the aromatic ring the V617F mechanism is thought to require. Position versus chemistry: if V678M does nothing while V678F does, the ring matters rather than the location. One of the seven variants supplied by the user. Seeds 8-15, completing n=16 to match V678F.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 77 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 8 | 80.1 | 50.3 | 52.3 | 49.2 | AF2 |
| 9 | 8 | 80.7 | 50.1 | 95.8 | 89.1 | AF2 |
| 10 | 14 | 80.3 | 49.7 | 95.1 | 89.7 | AF2 |
| 11 | 8 | 80.6 | 50.2 | 52.1 | 51.4 | AF2 |
| 12 | 12 | 80.3 | 47.3 | 94.3 | 83.6 | AF2 |
| 13 | 8 | 80.8 | 52.9 | 94.8 | 95.2 | AF2 |
| 14 | 9 | 79.9 | 49.8 | 48.5 | 44.9 | AF2 |
| 15 | 11 | 80.7 | 47.2 | 94.1 | 83.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 40.1 | 14 | 15 | 79.3 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.0 | 39.5 | 64.7 |
| 2 | 78.3 | 63.2 | 67.0 |
| 3 | 80.0 | 74.0 | 73.5 |
| 4 | 80.2 | 76.3 | 75.2 |
| 5 | 80.1 | 76.5 | 74.3 |
| 6 | 80.2 | 77.9 | 76.0 |
| 7 | 80.1 | 76.0 | 74.6 |
| 8 | 80.4 | 77.2 | 74.2 |
| 9 | 80.1 | 77.4 | 73.2 |
| 10 | 80.0 | 78.2 | 73.0 |
| 11 | 80.2 | 78.3 | 74.7 |
| 12 | 80.2 | 78.2 | 72.6 |
| 13 | 80.1 | 79.0 | 72.7 |
| 14 | 80.2 | 77.6 | 71.7 |
| 15 | 80.0 | 78.0 | 71.2 |

pLDDT 67.2–80.8; JH2–JH1 38.3–56.4 Å; FERM–JH1 17.9–96.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 48 49 53 52 53 57 51 52 52 56 56 54 57 51 55 | in between |
| 9 | 26 57 84 92 94 96 94 96 95 95 95 95 95 95 95 | open-like (> 80) |
| 10 | 18 71 84 89 87 88 87 87 89 90 90 95 96 95 95 | open-like (> 80) |
| 11 | 54 47 49 50 50 53 49 52 52 54 56 53 54 52 53 | in between |
| 12 | 64 90 96 94 94 94 95 95 94 94 94 94 94 94 94 | open-like (> 80) |
| 13 | 38 57 83 91 92 94 92 95 95 95 94 95 96 94 94 | open-like (> 80) |
| 14 | 29 45 48 49 49 47 46 46 48 47 47 46 47 46 45 | closed-like (< 50) |
| 15 | 39 90 96 94 94 94 95 94 94 94 94 94 94 94 94 | open-like (> 80) |
