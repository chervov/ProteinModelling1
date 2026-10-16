# JAK3_M592F_20261016_105409 — JAK3 M592F_msa128-512

JAK3 M592F, no template, MSA 128/512, 16 seeds. M592 is the position of JAK2 V617 / JAK1 V658; analogue of the classic pseudokinase activating mutation (not a known JAK3 patient variant). JAK1 V658F at 128/512: closed + FERM-bound states lost (p = 0.035); JAK2 V617F at 128/512: detached JH1 10/15 -> 2/16.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 135 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 5 | 84.3 | 50.8 | 50.9 | 48.5 | AF2 |
| 1 | 15 | 84.9 | 55.5 | 52.4 | 66.6 | AF2 |
| 2 | 5 | 84.4 | 49.3 | 51.1 | 57.5 | AF2 |
| 3 | 8 | 84.4 | 49.7 | 91.2 | 91.6 | AF2 |
| 4 | 10 | 84.4 | 53.5 | 46.8 | 42.6 | AF2 |
| 5 | 5 | 84.4 | 52.0 | 59.6 | 66.6 | AF2 |
| 6 | 5 | 84.2 | 53.2 | 57.3 | 57.4 | AF2 |
| 7 | 3 | 84.6 | 53.2 | 54.7 | 61.0 | AF2 |
| 8 | 5 | 84.6 | 47.7 | 95.1 | 84.1 | AF2 |
| 9 | 5 | 84.6 | 48.2 | 85.7 | 91.2 | AF2 |
| 10 | 15 | 84.5 | 48.2 | 56.3 | 68.9 | AF2 |
| 11 | 5 | 84.4 | 50.0 | 53.0 | 61.4 | AF2 |
| 12 | 5 | 84.2 | 47.9 | 44.4 | 22.8 | AF2 |
| 13 | 5 | 84.5 | 50.5 | 54.3 | 54.9 | AF2 |
| 14 | 15 | 84.6 | 47.6 | 95.1 | 84.0 | AF2 |
| 15 | 5 | 84.7 | 46.9 | 94.2 | 83.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 8.0 | 12 | 8 | 83.7 | 10 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 77.8 | 58.1 | 49.6 |
| 2 | 83.7 | 66.8 | 66.2 |
| 3 | 84.2 | 66.3 | 66.5 |
| 4 | 84.1 | 65.2 | 64.0 |
| 5 | 84.4 | 65.8 | 65.0 |
| 6 | 84.1 | 64.9 | 63.7 |
| 7 | 84.1 | 65.8 | 65.0 |
| 8 | 84.1 | 64.8 | 64.4 |
| 9 | 84.1 | 64.5 | 63.0 |
| 10 | 84.3 | 64.5 | 64.4 |
| 11 | 84.0 | 65.7 | 64.1 |
| 12 | 84.0 | 64.9 | 61.5 |
| 13 | 84.2 | 64.9 | 63.8 |
| 14 | 84.1 | 64.6 | 64.8 |
| 15 | 84.3 | 64.9 | 63.2 |

pLDDT 77.2–84.9; JH2–JH1 23.7–56.0 Å; FERM–JH1 22.9–96.7 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 240.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 54 58 52 51 51 54 52 54 53 52 54 52 52 54 53 | in between |
| 1 | 69 74 67 62 60 60 61 61 60 61 63 60 60 53 52 | in between |
| 2 | 45 59 54 52 51 51 50 51 49 50 52 50 49 50 50 | in between |
| 3 | 68 87 85 90 96 93 94 91 95 94 93 95 93 94 97 | open-like (> 80) |
| 4 | 23 44 45 47 46 48 48 47 46 47 48 46 47 48 48 | closed-like (< 50) |
| 5 | 68 71 64 62 60 58 60 58 56 57 58 57 56 56 58 | in between |
| 6 | 70 69 58 55 57 59 61 58 56 57 62 60 59 55 55 | in between |
| 7 | 44 55 55 52 53 53 54 52 52 51 53 51 51 53 54 | in between |
| 8 | 57 78 96 95 95 95 95 95 94 94 94 94 94 95 94 | open-like (> 80) |
| 9 | 73 73 82 82 86 75 80 74 76 74 74 79 80 78 80 | in between |
| 10 | 58 58 55 54 56 55 56 56 55 56 58 57 56 58 56 | in between |
| 11 | 65 55 53 53 53 51 53 56 54 53 55 49 54 53 55 | in between |
| 12 | 41 55 50 45 44 44 43 43 44 43 44 43 43 44 44 | closed-like (< 50) |
| 13 | 69 57 54 55 54 53 55 53 51 52 54 53 53 54 53 | in between |
| 14 | 58 93 96 95 96 96 96 96 96 96 96 96 96 96 95 | open-like (> 80) |
| 15 | 67 83 96 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
