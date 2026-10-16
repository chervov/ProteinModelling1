# JAK3_20261016_130116 — JAK3 WT_msa512-8192_s0-7

JAK3 wild type, no template, MSA 512/8192 (all sequences), seeds 0–7. JAK1 at this depth: all open; JAK2: 7/16 closed, 7 open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 512 clusters / 8192 extra; no template. Run time 111 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 10 | 85.9 | 46.7 | 94.1 | 82.0 | AF2 |
| 1 | 11 | 85.8 | 46.7 | 94.2 | 82.2 | AF2 |
| 2 | 10 | 85.9 | 46.7 | 94.1 | 82.5 | AF2 |
| 3 | 14 | 85.8 | 46.7 | 94.2 | 82.6 | AF2 |
| 4 | 12 | 85.9 | 46.8 | 94.4 | 82.3 | AF2 |
| 5 | 4 | 85.7 | 46.6 | 94.1 | 81.9 | AF2 |
| 6 | 6 | 85.6 | 46.7 | 94.3 | 82.5 | AF2 |
| 7 | 9 | 85.9 | 46.6 | 94.0 | 82.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 13.1 | 4 | 1 | 82.4 | 1 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 83.1 | 88.2 | 73.8 |
| 2 | 85.2 | 92.9 | 81.0 |
| 3 | 85.5 | 94.4 | 82.4 |
| 4 | 85.5 | 94.1 | 82.2 |
| 5 | 85.4 | 94.1 | 82.4 |
| 6 | 85.5 | 94.2 | 82.4 |
| 7 | 85.5 | 94.2 | 82.4 |
| 8 | 85.6 | 94.2 | 82.5 |
| 9 | 85.6 | 94.2 | 82.4 |
| 10 | 85.7 | 94.1 | 82.4 |
| 11 | 85.6 | 94.2 | 82.3 |
| 12 | 85.6 | 94.2 | 82.5 |
| 13 | 85.6 | 94.1 | 82.4 |
| 14 | 85.6 | 94.1 | 82.4 |
| 15 | 85.6 | 94.2 | 82.4 |

pLDDT 82.4–85.9; JH2–JH1 40.6–47.4 Å; FERM–JH1 44.3–95.0 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 95 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 1 | 93 95 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 2 | 94 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 3 | 95 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 4 | 44 83 95 94 94 95 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 5 | 95 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 6 | 95 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 7 | 94 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
