# JAK3_Y581C_20261019_114115 — JAK3 Y581C_msa128-512_s0-7

JAK3 Y581C, seeds 0-7, MSA 128/512, paired with wild type JAK3_20261016_125830. One of seven variants of interest supplied by the user; no functional study exists for it in the literature. Structurally it buries 0.0 A^2 at the JH2-JH1 interface in JAK3 own closed structure (20 percent exposed, no cross-domain contacts), so any conformational effect must be indirect - unlike TYK2 P982A, the only one of the seven at a real interface. Sequence predictors call it the mildest of the seven (AlphaMissense 0.10-0.14, CADD 22.2, REVEL 0.37), though PolyPhen-2 disagrees at 0.97.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 128 clusters / 512 extra; no template. Run time 69 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 5 | 84.7 | 58.1 | 52.2 | 87.6 | AF2 |
| 1 | 10 | 83.9 | 62.5 | 51.0 | 88.5 | AF2 |
| 2 | 10 | 84.0 | 63.0 | 50.7 | 88.3 | AF2 |
| 3 | 10 | 84.2 | 65.6 | 50.8 | 89.3 | AF2 |
| 4 | 6 | 84.1 | 62.9 | 50.7 | 88.1 | AF2 |
| 5 | 10 | 84.2 | 62.7 | 51.1 | 88.6 | AF2 |
| 6 | 10 | 84.4 | 62.5 | 51.4 | 88.7 | AF2 |
| 7 | 9 | 84.3 | 62.1 | 50.2 | 88.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 27.6 | 4 | 10 | 83.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.1 | 41.6 | 74.8 |
| 2 | 83.5 | 55.5 | 89.8 |
| 3 | 84.0 | 53.9 | 89.3 |
| 4 | 84.0 | 53.3 | 89.4 |
| 5 | 84.1 | 51.7 | 89.0 |
| 6 | 84.1 | 51.8 | 89.4 |
| 7 | 84.0 | 51.2 | 88.9 |
| 8 | 83.9 | 54.4 | 86.1 |
| 9 | 84.0 | 50.6 | 88.4 |
| 10 | 84.1 | 49.0 | 80.2 |
| 11 | 83.9 | 49.8 | 87.2 |
| 12 | 83.9 | 49.4 | 84.5 |
| 13 | 84.1 | 49.9 | 86.6 |
| 14 | 83.9 | 50.2 | 87.6 |
| 15 | 83.9 | 50.4 | 86.1 |

pLDDT 77.5–84.7; JH2–JH1 46.2–65.9 Å; FERM–JH1 26.8–84.4 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 39 49 69 67 52 50 49 49 49 48 47 49 49 50 50 | in between |
| 1 | 50 60 51 51 52 52 52 51 51 51 50 51 50 51 52 | in between |
| 2 | 43 52 50 50 50 51 50 49 50 51 51 50 50 51 51 | in between |
| 3 | 38 60 55 53 53 54 52 52 52 51 49 50 49 49 49 | closed-like (< 50) |
| 4 | 29 48 49 50 52 51 50 46 48 41 50 45 47 49 48 | closed-like (< 50) |
| 5 | 50 67 53 52 52 52 52 52 52 51 50 50 50 50 51 | in between |
| 6 | 58 61 52 53 53 53 53 52 52 51 52 52 52 52 53 | in between |
| 7 | 27 47 53 50 50 52 51 84 50 48 49 48 51 49 50 | in between |
