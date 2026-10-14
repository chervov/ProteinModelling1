# JAK1_20261014_135749 — JAK1, no template, MSA 128 clusters / 512 extra

Part of the JAK1 MSA-depth scan. OpenFold model_1, guided recycling, 8 recycles × seeds 0,1,2,3,4, no template. Run time 27 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 7 | 85.2 | 46.4 | 92.9 | 3.9 | 1.4 | 82.3 | 83.5 | ma-a1sai |
| 1 | 3 | 84.9 | 46.9 | 81.4 | 56.1 | 54.4 | 89.2 | 86.8 | ma-a1sai |
| 2 | 7 | 85.2 | 48.0 | 94.7 | 8.8 | 5.8 | 85.2 | 86.0 | ma-a1sai |
| 3 | 7 | 85.2 | 46.5 | 93.1 | 4.0 | 1.6 | 82.5 | 83.7 | ma-a1sai |
| 4 | 7 | 85.3 | 46.6 | 93.2 | 3.7 | 1.5 | 82.4 | 83.7 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 2.2 | 4 | 8 | 85.0 | 16 |
| ma-a1sai (open) | 1.0 | 0 | 8 | 85.1 | 17 |
| ma-l9b1f (closed) | 17.2 | 4 | 1 | 79.0 | 0 |
| Shan 2014 (closed, JH2–JH1) | 21.3 | 4 | 1 | 79.0 | 0 |

pLDDT 77.2–85.3; JH2–JH1 12.0–53.7 Å; FERM–JH1 37.3–95.1 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-a1sai 34, ma-l9b1f 4, AF2 2.
