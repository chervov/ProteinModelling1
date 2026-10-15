# JAK1_20261015_131035 — JAK1, no template, MSA 160 clusters / 640 extra

Part of the JAK1 MSA-depth scan (see JAK1/MSA_scan_summary.md). OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4, no template. Run time 48 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 85.8 | 46.5 | 93.1 | 2.4 | 1.5 | 81.9 | 83.3 | ma-a1sai |
| 1 | 6 | 85.4 | 46.5 | 93.1 | 3.6 | 1.9 | 82.4 | 83.7 | ma-a1sai |
| 2 | 5 | 85.5 | 46.5 | 93.2 | 2.9 | 1.6 | 82.1 | 83.5 | ma-a1sai |
| 3 | 14 | 85.8 | 46.5 | 93.0 | 2.8 | 1.3 | 81.9 | 83.3 | ma-a1sai |
| 4 | 7 | 85.8 | 46.5 | 93.1 | 3.6 | 0.8 | 82.2 | 83.5 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 0.8 | 0 | 13 | 85.6 | 69 |
| ma-a1sai (open) | 0.4 | 4 | 10 | 85.4 | 69 |
| ma-l9b1f (closed) | 10.4 | 1 | 1 | 80.4 | 1 |
| Shan 2014 (closed, JH2–JH1) | 17.1 | 1 | 1 | 80.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 80.3 | 39.9 | 91.3 | 92.4 | 20.4 | 26.5 |
| 2 | 84.8 | 93.7 | 15.4 | 13.6 | 86.6 | 87.2 |
| 3 | 85.4 | 92.8 | 2.8 | 1.7 | 81.9 | 83.3 |
| 4 | 85.4 | 92.9 | 3.0 | 1.8 | 82.0 | 83.4 |
| 5 | 85.4 | 93.2 | 3.1 | 1.4 | 82.1 | 83.5 |
| 6 | 85.6 | 93.1 | 3.3 | 1.4 | 82.2 | 83.5 |
| 7 | 85.5 | 93.2 | 3.2 | 1.5 | 82.1 | 83.4 |
| 8 | 85.4 | 93.2 | 3.2 | 1.8 | 82.1 | 83.5 |
| 9 | 85.5 | 93.0 | 3.0 | 1.5 | 82.0 | 83.4 |
| 10 | 85.4 | 93.1 | 3.2 | 1.0 | 81.9 | 83.2 |
| 11 | 85.6 | 93.0 | 3.0 | 1.4 | 82.1 | 83.4 |
| 12 | 85.4 | 93.1 | 3.3 | 1.8 | 82.2 | 83.6 |
| 13 | 85.5 | 93.0 | 2.4 | 2.3 | 81.8 | 83.3 |
| 14 | 85.6 | 93.2 | 3.2 | 1.2 | 82.1 | 83.4 |
| 15 | 85.5 | 93.2 | 3.3 | 1.2 | 82.1 | 83.4 |

pLDDT 80.1–85.8; JH2–JH1 43.0–52.7 Å; FERM–JH1 37.4–94.3 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-a1sai 66, ma-l9b1f 5, AF2 4.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~92, closed ~40)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 42 93 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 1 | 40 93 94 93 93 93 94 94 93 93 93 93 94 93 93 | open-like (> 80) |
| 2 | 40 94 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 3 | 37 94 93 93 93 93 93 93 92 93 93 93 93 93 93 | open-like (> 80) |
| 4 | 41 94 92 93 93 93 93 93 93 93 93 93 92 93 93 | open-like (> 80) |
