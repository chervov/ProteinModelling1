# TYK2_V678G_20261021_045409 — TYK2 V678G_free_msa64-256_s8-15

TYK2 V678G at 64/256, seeds 8-15. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678G is -0.474. smallest; strongest loss of signalling at the position, worse than a nonsense variant. The strongest prediction of a reversed effect. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 82 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 14 | 80.5 | 46.8 | 93.6 | 83.0 | AF2 |
| 9 | 11 | 80.2 | 49.4 | 53.6 | 55.8 | AF2 |
| 10 | 11 | 80.6 | 51.2 | 93.8 | 92.4 | AF2 |
| 11 | 11 | 80.3 | 49.5 | 92.0 | 90.0 | AF2 |
| 12 | 11 | 80.0 | 49.5 | 92.8 | 89.0 | AF2 |
| 13 | 11 | 80.4 | 49.1 | 95.3 | 87.6 | AF2 |
| 14 | 9 | 80.8 | 50.2 | 90.2 | 92.6 | AF2 |
| 15 | 11 | 80.3 | 48.0 | 64.1 | 62.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 31.6 | 12 | 2 | 76.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 65.3 | 54.9 | 49.1 |
| 2 | 76.3 | 44.5 | 37.3 |
| 3 | 78.8 | 48.8 | 49.4 |
| 4 | 79.8 | 57.0 | 58.4 |
| 5 | 79.5 | 63.0 | 64.3 |
| 6 | 79.6 | 61.6 | 65.5 |
| 7 | 79.8 | 70.4 | 72.7 |
| 8 | 79.8 | 74.9 | 76.0 |
| 9 | 80.1 | 73.8 | 75.0 |
| 10 | 80.1 | 80.2 | 77.8 |
| 11 | 80.3 | 84.7 | 81.7 |
| 12 | 80.0 | 86.4 | 80.2 |
| 13 | 80.2 | 88.2 | 83.5 |
| 14 | 80.0 | 87.8 | 82.3 |
| 15 | 80.2 | 88.3 | 84.8 |

pLDDT 64.6–80.8; JH2–JH1 42.1–62.5 Å; FERM–JH1 38.2–95.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 59 39 87 95 95 95 95 95 94 95 94 94 94 94 94 | open-like (> 80) |
| 9 | 60 45 41 47 48 46 48 49 49 53 54 58 63 62 63 | in between |
| 10 | 40 48 49 52 58 58 71 89 90 95 94 95 95 95 93 | open-like (> 80) |
| 11 | 59 46 42 55 58 57 80 80 62 64 92 94 95 95 95 | open-like (> 80) |
| 12 | 57 42 47 55 55 54 57 58 63 86 93 95 95 95 95 | open-like (> 80) |
| 13 | 55 43 38 54 74 59 76 89 91 94 95 94 95 94 94 | open-like (> 80) |
| 14 | 55 49 42 47 64 74 86 89 90 95 92 95 94 94 93 | open-like (> 80) |
| 15 | 55 44 44 50 52 49 50 51 51 59 64 66 75 74 79 | in between |
