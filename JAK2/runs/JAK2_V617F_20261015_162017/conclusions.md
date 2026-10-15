# JAK2_V617F_20261015_162017 — JAK2 V617F_msa128-512

JAK2 V617F (activating mutation at the JH2–JH1 autoinhibitory interface; = JAK1 V658F), no template, MSA 128/512, 16 seeds. Wild type at this depth (JAK2_20261015_134222, 15 seeds): mostly in between (FERM–JH1 55–65 Å, neither open nor Shan's closed), 1 open.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. Run time 137 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 15 | 84.8 | 49.6 | 62.0 | 80.9 | 48.7 | Shan 2014 |
| 1 | 7 | 85.0 | 49.2 | 68.3 | 70.2 | 84.9 | AF2 |
| 2 | 6 | 84.6 | 52.2 | 52.7 | 92.1 | 39.4 | Shan 2014 |
| 3 | 12 | 84.6 | 52.8 | 58.4 | 88.1 | 46.7 | Shan 2014 |
| 4 | 15 | 84.8 | 47.1 | 95.3 | 1.8 | 84.9 | AF2 |
| 5 | 7 | 84.9 | 50.5 | 82.6 | 52.3 | 95.7 | AF2 |
| 6 | 12 | 84.7 | 51.5 | 60.6 | 85.6 | 49.0 | Shan 2014 |
| 7 | 12 | 84.4 | 50.9 | 51.3 | 90.1 | 42.4 | Shan 2014 |
| 8 | 12 | 84.5 | 51.7 | 58.3 | 88.4 | 37.8 | Shan 2014 |
| 9 | 6 | 84.3 | 51.2 | 53.6 | 90.5 | 36.7 | Shan 2014 |
| 10 | 13 | 85.2 | 46.7 | 95.1 | 3.2 | 84.2 | AF2 |
| 11 | 11 | 85.1 | 46.1 | 94.6 | 2.0 | 83.1 | AF2 |
| 12 | 13 | 85.1 | 46.4 | 94.8 | 3.0 | 83.1 | AF2 |
| 13 | 11 | 84.7 | 51.1 | 53.1 | 90.6 | 38.4 | Shan 2014 |
| 14 | 13 | 84.8 | 48.9 | 53.9 | 81.8 | 82.2 | AF2 |
| 15 | 12 | 85.3 | 46.0 | 94.2 | 2.4 | 82.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.9 | 10 | 15 | 85.0 | 43 |
| Shan 2014 (closed, JH2–JH1) | 13.8 | 13 | 15 | 84.4 | 1 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 78.5 | 54.4 | 64.5 | 60.1 |
| 2 | 83.7 | 63.7 | 77.8 | 60.3 |
| 3 | 84.3 | 61.2 | 80.0 | 58.9 |
| 4 | 84.3 | 61.4 | 78.0 | 56.1 |
| 5 | 84.3 | 62.0 | 78.1 | 56.5 |
| 6 | 84.5 | 65.8 | 69.7 | 58.8 |
| 7 | 84.5 | 65.2 | 69.5 | 58.7 |
| 8 | 84.4 | 65.5 | 66.3 | 57.3 |
| 9 | 84.4 | 66.2 | 64.7 | 58.5 |
| 10 | 84.5 | 66.4 | 65.0 | 58.4 |
| 11 | 84.6 | 70.7 | 55.2 | 61.6 |
| 12 | 84.7 | 70.3 | 56.6 | 61.4 |
| 13 | 84.6 | 71.2 | 53.6 | 60.2 |
| 14 | 84.5 | 70.4 | 55.1 | 58.9 |
| 15 | 84.6 | 70.6 | 53.6 | 58.9 |

pLDDT 76.8–85.3; JH2–JH1 15.2–53.4 Å; FERM–JH1 36.6–96.8 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 152, AF2 88.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 59 62 56 56 55 55 56 56 56 57 55 53 60 60 62 | in between |
| 1 | 59 68 70 63 71 80 68 64 67 65 72 77 73 64 67 | in between |
| 2 | 50 56 53 52 54 53 48 48 48 51 50 49 49 49 49 | closed-like (< 50) |
| 3 | 37 63 65 61 60 59 60 58 58 59 57 58 63 59 58 | in between |
| 4 | 69 62 56 56 56 56 58 58 59 59 95 89 97 95 95 | open-like (> 80) |
| 5 | 53 77 78 83 86 92 83 93 95 93 95 95 95 93 96 | open-like (> 80) |
| 6 | 53 64 60 58 58 57 58 58 58 56 58 61 60 60 61 | in between |
| 7 | 42 59 55 57 56 54 53 52 52 54 52 51 54 54 55 | in between |
| 8 | 52 61 59 60 58 58 57 56 60 58 57 58 54 55 51 | in between |
| 9 | 71 61 56 58 56 54 52 52 51 52 52 52 52 52 52 | in between |
| 10 | 58 71 78 95 95 96 94 95 95 95 94 94 95 95 94 | open-like (> 80) |
| 11 | 63 65 59 61 58 94 96 95 95 95 95 95 95 95 94 | open-like (> 80) |
| 12 | 58 63 58 54 58 73 92 96 95 95 95 95 95 95 94 | open-like (> 80) |
| 13 | 54 60 55 57 57 56 57 56 57 56 53 50 50 50 49 | closed-like (< 50) |
| 14 | 50 60 57 51 52 53 53 53 54 54 55 54 54 56 56 | in between |
| 15 | 41 67 62 62 62 62 58 59 61 65 96 94 95 95 95 | open-like (> 80) |

## Interpretation (vs wild type, details: [JAK2_V617F.md](../../JAK2_V617F.md))
- Final states (16 seeds): 6 open, 1 closed (8.9 Å), 3 next to FERM, 4 JH1 on JH2 in other positions, 2 detached JH1; none 7T6F-like.
- Wild type at the same depth (15): 1 open, 10 detached JH1. **V617F largely removes the detached-JH1 intermediate (p = 0.003) and increases the open fraction (p = 0.083).**
