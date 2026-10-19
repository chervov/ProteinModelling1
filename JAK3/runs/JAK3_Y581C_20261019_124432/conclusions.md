# JAK3_Y581C_20261019_124432 — JAK3 Y581C_msa128-512_s8-15

JAK3 Y581C, seeds 8-15, MSA 128/512, paired with wild type JAK3_20261016_125830. One of seven variants of interest supplied by the user; no functional study exists for it in the literature. Structurally it buries 0.0 A^2 at the JH2-JH1 interface in JAK3 own closed structure (20 percent exposed, no cross-domain contacts), so any conformational effect must be indirect - unlike TYK2 P982A, the only one of the seven at a real interface. Sequence predictors call it the mildest of the seven (AlphaMissense 0.10-0.14, CADD 22.2, REVEL 0.37), though PolyPhen-2 disagrees at 0.97.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 63 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 4 | 84.3 | 47.9 | 95.3 | 83.9 | AF2 |
| 9 | 3 | 84.8 | 50.2 | 64.8 | 86.8 | AF2 |
| 10 | 3 | 84.3 | 62.1 | 52.0 | 88.3 | AF2 |
| 11 | 4 | 84.3 | 61.1 | 51.1 | 87.9 | AF2 |
| 12 | 13 | 84.2 | 60.1 | 59.5 | 91.8 | AF2 |
| 13 | 2 | 83.9 | 60.8 | 61.5 | 92.5 | AF2 |
| 14 | 15 | 84.4 | 62.5 | 58.0 | 92.1 | AF2 |
| 15 | 3 | 84.0 | 63.5 | 56.8 | 92.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 31.2 | 9 | 1 | 78.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.5 | 57.7 | 77.2 |
| 2 | 83.5 | 61.0 | 90.7 |
| 3 | 84.1 | 63.5 | 90.6 |
| 4 | 84.2 | 60.0 | 87.9 |
| 5 | 83.9 | 59.2 | 88.1 |
| 6 | 83.8 | 60.5 | 88.7 |
| 7 | 83.9 | 59.2 | 88.1 |
| 8 | 84.0 | 63.5 | 89.0 |
| 9 | 84.0 | 60.4 | 87.8 |
| 10 | 84.1 | 61.2 | 89.3 |
| 11 | 84.0 | 64.6 | 89.2 |
| 12 | 84.0 | 60.0 | 88.5 |
| 13 | 84.1 | 61.5 | 88.6 |
| 14 | 83.8 | 59.0 | 88.2 |
| 15 | 84.1 | 59.8 | 88.6 |

pLDDT 78.0–84.8; JH2–JH1 34.0–65.0 Å; FERM–JH1 26.1–96.2 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 67 67 96 95 94 94 95 95 94 94 94 94 94 95 95 | open-like (> 80) |
| 9 | 26 64 65 58 56 59 59 63 59 62 61 58 60 57 60 | in between |
| 10 | 62 55 52 49 50 52 49 51 51 53 51 52 52 51 51 | in between |
| 11 | 64 59 55 51 50 49 49 49 49 50 50 50 49 50 50 | in between |
| 12 | 61 66 59 57 57 57 55 72 59 59 88 55 60 55 56 | in between |
| 13 | 64 62 59 58 55 56 57 68 61 57 60 56 60 55 56 | in between |
| 14 | 61 55 66 57 60 60 58 57 60 59 58 59 62 58 58 | in between |
| 15 | 56 60 57 54 53 56 53 53 51 55 54 55 56 52 53 | in between |
