# TYK2_V678G_20261021_030907 — TYK2 V678G_free_msa64-256_s0-7

TYK2 V678G at 64/256, seeds 0-7. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678G is -0.474. smallest; strongest loss of signalling at the position, worse than a nonsense variant. The strongest prediction of a reversed effect. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time 87 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 13 | 80.2 | 52.1 | 93.6 | 94.1 | AF2 |
| 1 | 6 | 80.5 | 51.3 | 94.0 | 92.6 | AF2 |
| 2 | 11 | 81.0 | 51.6 | 93.0 | 93.6 | AF2 |
| 3 | 5 | 81.0 | 49.2 | 95.7 | 87.2 | AF2 |
| 4 | 6 | 80.5 | 51.6 | 94.4 | 92.9 | AF2 |
| 5 | 6 | 80.8 | 52.9 | 94.7 | 94.8 | AF2 |
| 6 | 8 | 80.7 | 50.2 | 83.5 | 90.1 | AF2 |
| 7 | 5 | 80.8 | 51.4 | 94.8 | 92.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 30.3 | 4 | 2 | 74.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 64.2 | 39.2 | 61.9 |
| 2 | 74.9 | 43.2 | 49.4 |
| 3 | 78.4 | 52.4 | 57.6 |
| 4 | 79.9 | 72.2 | 82.0 |
| 5 | 80.4 | 86.0 | 88.8 |
| 6 | 80.6 | 90.8 | 90.3 |
| 7 | 80.2 | 93.1 | 89.6 |
| 8 | 80.4 | 93.1 | 88.7 |
| 9 | 80.4 | 93.4 | 90.0 |
| 10 | 80.1 | 94.3 | 87.8 |
| 11 | 80.3 | 93.3 | 89.9 |
| 12 | 80.3 | 93.7 | 87.7 |
| 13 | 80.3 | 93.7 | 88.6 |
| 14 | 80.1 | 94.0 | 89.4 |
| 15 | 80.3 | 94.5 | 89.5 |

pLDDT 63.3–81.0; JH2–JH1 42.8–61.4 Å; FERM–JH1 25.6–95.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 31 41 51 74 93 95 94 94 95 95 93 95 94 95 95 | open-like (> 80) |
| 1 | 44 48 60 86 91 94 94 95 94 95 95 95 95 95 95 | open-like (> 80) |
| 2 | 42 40 40 53 68 88 93 94 93 96 93 94 95 94 95 | open-like (> 80) |
| 3 | 46 56 49 87 96 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 4 | 32 26 78 91 95 94 95 95 95 94 95 94 95 95 95 | open-like (> 80) |
| 5 | 40 52 57 62 87 95 94 94 95 94 94 95 95 95 96 | open-like (> 80) |
| 6 | 34 41 43 51 62 72 85 84 86 91 87 89 88 89 90 | open-like (> 80) |
| 7 | 46 42 41 74 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
