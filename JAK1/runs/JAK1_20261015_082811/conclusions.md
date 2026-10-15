# JAK1_20261015_082811 — JAK1, no template, MSA 128 clusters / 512 extra

Part of the JAK1 MSA-depth scan. OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4, no template. Run time 52 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 12 | 84.9 | 53.4 | 74.9 | 69.0 | 70.7 | 68.8 | 73.9 | ma-l9b1f |
| 1 | 15 | 85.1 | 46.6 | 93.0 | 2.6 | 2.5 | 82.0 | 83.5 | ma-a1sai |
| 2 | 3 | 84.6 | 48.7 | 45.8 | 87.6 | 88.9 | 25.1 | 32.6 | ma-l9b1f |
| 3 | 13 | 85.6 | 44.8 | 85.1 | 45.1 | 43.3 | 81.8 | 81.1 | ma-a1sai |
| 4 | 13 | 83.9 | 40.0 | 40.8 | 80.9 | 81.8 | 4.5 | 14.4 | ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 2.6 | 1 | 15 | 85.1 | 11 |
| ma-a1sai (open) | 2.5 | 1 | 15 | 85.1 | 11 |
| ma-l9b1f (closed) | 2.4 | 4 | 4 | 83.5 | 15 |
| Shan 2014 (closed, JH2–JH1) | 11.1 | 4 | 3 | 83.7 | 12 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 79.4 | 63.6 | 53.4 | 53.8 | 50.1 | 52.2 |
| 2 | 84.2 | 60.9 | 76.6 | 78.1 | 45.9 | 52.2 |
| 3 | 84.5 | 55.9 | 79.9 | 81.4 | 36.8 | 43.9 |
| 4 | 84.3 | 62.4 | 70.3 | 71.6 | 44.1 | 50.6 |
| 5 | 84.3 | 55.0 | 80.6 | 82.1 | 35.4 | 42.8 |
| 6 | 84.4 | 67.3 | 64.6 | 65.5 | 52.6 | 58.0 |
| 7 | 84.3 | 68.4 | 56.6 | 56.8 | 52.3 | 57.3 |
| 8 | 84.3 | 61.3 | 64.7 | 65.4 | 39.1 | 45.7 |
| 9 | 84.3 | 61.1 | 66.4 | 67.1 | 39.8 | 46.5 |
| 10 | 84.2 | 67.3 | 58.6 | 58.6 | 50.4 | 55.3 |
| 11 | 84.3 | 68.7 | 59.3 | 59.5 | 53.7 | 58.3 |
| 12 | 84.6 | 69.3 | 56.7 | 56.7 | 54.2 | 58.6 |
| 13 | 84.7 | 72.1 | 44.7 | 44.5 | 56.1 | 59.9 |
| 14 | 84.5 | 72.0 | 48.1 | 47.9 | 58.2 | 61.7 |
| 15 | 84.5 | 71.4 | 46.0 | 45.6 | 56.3 | 59.8 |

pLDDT 78.6–85.6; JH2–JH1 29.4–53.4 Å; FERM–JH1 40.2–95.7 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-l9b1f 49, ma-a1sai 21, AF2 5.
