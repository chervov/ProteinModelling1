# JAK3_20261016_172413 — JAK3 WT_msa256-1024

JAK3 wild type, no template, MSA 256/1024, 16 seeds. Locates the open/closed transition: JAK3 is unanimously compact at 128/512 (16/16, max 56 A) and unanimously open at 512/8192 (8/8 at 94 A). The depth where both states appear is the one where a mutation can shift the balance. JAK2 was bistable at this depth.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 256 clusters / 1024 extra; no template. Run time 147 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 13 | 85.5 | 46.6 | 93.9 | 81.9 | AF2 |
| 1 | 6 | 85.3 | 46.6 | 94.1 | 82.4 | AF2 |
| 2 | 6 | 85.4 | 46.7 | 93.9 | 82.5 | AF2 |
| 3 | 5 | 85.4 | 46.6 | 93.9 | 82.6 | AF2 |
| 4 | 13 | 85.3 | 46.4 | 93.9 | 82.3 | AF2 |
| 5 | 6 | 85.3 | 46.8 | 94.1 | 82.8 | AF2 |
| 6 | 13 | 85.3 | 46.6 | 94.0 | 82.2 | AF2 |
| 7 | 6 | 84.2 | 45.1 | 43.1 | 15.7 | AF2 |
| 8 | 9 | 85.4 | 46.6 | 93.9 | 82.2 | AF2 |
| 9 | 5 | 85.4 | 46.7 | 94.0 | 82.6 | AF2 |
| 10 | 7 | 85.3 | 46.5 | 94.0 | 82.4 | AF2 |
| 11 | 5 | 85.5 | 46.6 | 94.0 | 82.6 | AF2 |
| 12 | 6 | 85.5 | 46.7 | 94.1 | 82.6 | AF2 |
| 13 | 7 | 85.4 | 46.5 | 93.8 | 82.2 | AF2 |
| 14 | 6 | 85.4 | 46.8 | 94.2 | 82.7 | AF2 |
| 15 | 12 | 85.3 | 46.8 | 94.1 | 82.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 4.8 | 7 | 12 | 84.1 | 13 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 80.6 | 49.7 | 24.7 |
| 2 | 83.9 | 82.2 | 69.1 |
| 3 | 84.8 | 89.2 | 75.4 |
| 4 | 84.8 | 87.9 | 75.1 |
| 5 | 85.2 | 90.9 | 78.4 |
| 6 | 85.2 | 91.0 | 78.3 |
| 7 | 85.2 | 90.8 | 78.0 |
| 8 | 85.0 | 90.8 | 77.7 |
| 9 | 85.1 | 90.7 | 77.6 |
| 10 | 85.1 | 90.9 | 77.6 |
| 11 | 84.9 | 91.0 | 77.9 |
| 12 | 85.1 | 90.9 | 77.7 |
| 13 | 85.2 | 90.8 | 77.5 |
| 14 | 85.0 | 90.7 | 77.8 |
| 15 | 84.9 | 90.8 | 77.9 |

pLDDT 79.2–85.5; JH2–JH1 25.6–48.9 Å; FERM–JH1 41.1–96.6 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 240.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 45 63 96 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 1 | 63 72 95 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 2 | 44 96 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 3 | 45 95 94 94 94 97 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 4 | 52 95 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 5 | 46 92 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 6 | 52 64 54 48 95 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 7 | 43 54 51 43 44 43 43 43 42 43 43 43 43 43 43 | closed-like (< 50) |
| 8 | 62 95 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 9 | 43 58 95 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 10 | 56 95 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 11 | 51 95 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 12 | 41 94 94 94 94 94 94 94 94 94 95 94 94 94 94 | open-like (> 80) |
| 13 | 48 57 96 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 14 | 55 94 95 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 15 | 49 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
