# JAK1_V658F_20261015_160458 — JAK1 V658F_msa128-512

JAK1 V658F (activating mutation; = JAK2 V617F, mouse V657F of the cryo-EM active dimer 7T6F), no template, MSA 128/512. Seeds 0–14 (seed 15 in a separate short run). Wild type at this depth (15 seeds): 7 open, 6 next to FERM (2 matching the closed ma-l9b1f, best 1.2 Å), 2 switching.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14; MSA 128 clusters / 512 extra; no template. Run time 115 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to JAK1: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P23458-F1) | 46.3 | 92.2 |
| ma-a1sai (open) | 46.0 | 92.5 |
| ma-l9b1f (closed) | 39.5 | 40.1 |
| Shan 2014 (closed, JH2–JH1) | 38.0 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 6 | 85.1 | 48.1 | 94.8 | 8.6 | 6.9 | 85.5 | 86.6 | ma-a1sai |
| 1 | 6 | 85.2 | 47.2 | 93.9 | 4.9 | 3.6 | 83.5 | 84.8 | ma-a1sai |
| 2 | 4 | 85.3 | 53.4 | 96.7 | 33.9 | 31.4 | 96.2 | 95.4 | ma-a1sai |
| 3 | 4 | 85.2 | 49.8 | 87.0 | 54.2 | 51.9 | 88.0 | 86.0 | ma-a1sai |
| 4 | 6 | 85.1 | 48.0 | 94.8 | 7.8 | 6.1 | 85.2 | 86.4 | ma-a1sai |
| 5 | 13 | 85.3 | 46.8 | 93.3 | 3.2 | 1.8 | 82.4 | 83.8 | ma-a1sai |
| 6 | 10 | 85.2 | 47.1 | 93.8 | 3.7 | 3.1 | 83.0 | 84.4 | ma-a1sai |
| 7 | 10 | 85.3 | 46.6 | 93.1 | 2.9 | 2.7 | 82.2 | 83.7 | ma-a1sai |
| 8 | 5 | 85.2 | 52.5 | 97.8 | 23.8 | 21.5 | 92.8 | 93.0 | ma-a1sai |
| 9 | 6 | 85.0 | 48.5 | 95.3 | 9.5 | 7.6 | 86.2 | 87.3 | ma-a1sai |
| 10 | 10 | 85.8 | 44.1 | 84.0 | 45.4 | 43.5 | 81.2 | 80.4 | ma-a1sai |
| 11 | 3 | 84.7 | 51.4 | 53.1 | 86.6 | 88.1 | 35.7 | 43.2 | ma-l9b1f |
| 12 | 14 | 85.8 | 43.8 | 83.6 | 45.3 | 43.5 | 80.7 | 79.9 | ma-a1sai |
| 13 | 13 | 86.1 | 44.0 | 84.2 | 44.9 | 43.1 | 81.1 | 80.4 | ma-a1sai |
| 14 | 10 | 85.8 | 44.4 | 84.2 | 46.0 | 44.1 | 81.5 | 80.6 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 2.3 | 7 | 15 | 85.1 | 104 |
| ma-a1sai (open) | 1.5 | 9 | 11 | 84.8 | 104 |
| ma-l9b1f (closed) | 6.3 | 13 | 5 | 83.8 | 2 |
| Shan 2014 (closed, JH2–JH1) | 17.2 | 13 | 5 | 83.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 78.0 | 54.2 | 69.2 | 70.1 | 32.6 | 35.8 |
| 2 | 83.9 | 52.2 | 79.6 | 80.4 | 42.6 | 47.3 |
| 3 | 84.7 | 76.9 | 60.9 | 60.8 | 72.8 | 75.4 |
| 4 | 84.8 | 82.1 | 39.7 | 38.6 | 73.2 | 75.3 |
| 5 | 84.6 | 81.1 | 34.9 | 34.0 | 68.7 | 71.4 |
| 6 | 84.9 | 86.5 | 29.3 | 28.2 | 78.5 | 80.1 |
| 7 | 85.0 | 88.5 | 25.0 | 23.4 | 80.3 | 81.2 |
| 8 | 85.1 | 88.3 | 24.1 | 22.5 | 80.1 | 81.1 |
| 9 | 85.1 | 89.0 | 25.2 | 23.6 | 82.6 | 83.2 |
| 10 | 85.2 | 88.1 | 24.6 | 23.4 | 79.5 | 80.6 |
| 11 | 85.0 | 87.9 | 24.2 | 22.7 | 79.2 | 80.2 |
| 12 | 85.0 | 88.6 | 24.0 | 22.8 | 80.2 | 81.2 |
| 13 | 85.2 | 87.7 | 24.8 | 23.3 | 79.4 | 80.4 |
| 14 | 85.1 | 88.3 | 24.3 | 23.2 | 80.7 | 81.6 |
| 15 | 85.1 | 88.0 | 23.3 | 22.0 | 79.3 | 80.3 |

pLDDT 77.0–86.1; JH2–JH1 14.4–57.0 Å; FERM–JH1 38.9–97.8 Å (open ma-a1sai 92.5 Å, closed ma-l9b1f 40.1 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: ma-a1sai 166, ma-l9b1f 47, AF2 11, Shan 2014 1.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~92, closed ~40)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 58 55 93 95 96 95 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 1 | 57 39 87 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 2 | 42 41 87 97 96 96 94 94 96 97 95 96 95 96 94 | open-like (> 80) |
| 3 | 51 48 89 87 85 87 86 88 86 86 86 85 86 86 90 | open-like (> 80) |
| 4 | 60 59 80 96 95 95 94 94 95 94 94 94 94 94 94 | open-like (> 80) |
| 5 | 66 75 96 94 94 94 94 94 94 93 94 94 93 93 93 | open-like (> 80) |
| 6 | 64 93 94 93 93 93 94 94 94 94 93 94 93 93 93 | open-like (> 80) |
| 7 | 50 40 81 96 94 95 94 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 8 | 58 67 92 96 98 95 94 95 95 95 95 96 95 95 94 | open-like (> 80) |
| 9 | 49 48 61 95 95 95 94 94 95 94 94 95 94 94 94 | open-like (> 80) |
| 10 | 65 48 51 58 50 82 88 83 84 84 84 84 84 84 84 | open-like (> 80) |
| 11 | 49 44 53 50 50 54 53 56 64 50 50 53 48 57 51 | in between |
| 12 | 50 47 92 89 86 87 86 84 84 85 84 88 84 84 84 | open-like (> 80) |
| 13 | 47 39 49 45 46 86 84 84 84 84 84 84 84 84 84 | open-like (> 80) |
| 14 | 47 41 47 46 46 49 86 84 84 84 84 84 84 84 84 | open-like (> 80) |

## Interpretation (vs wild type, details: [JAK1_V658F.md](../../JAK1_V658F.md))
- Final states (15 seeds): **9 open, 4 in the 7T6F-like active-dimer arrangement (5.3–6.6 Å from 7T6F; +1 part way), 1 next to FERM, 0 closed**.
- Wild type at the same depth: 6 open, 3 closed, 4 next to FERM, 1 7T6F-like. The mutation removes the closed/FERM-bound arrangement (7 → 1 of 15, p = 0.035) and shifts seeds towards the 7T6F-like arrangement (1 → 4–5).
