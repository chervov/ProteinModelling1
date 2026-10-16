# JAK1_V658F_20261015_223123 — JAK2 experiment JAK1_V658F_msa512-8192

JAK1 V658F (activating mutation; = JAK2 V617F), MSA 512/8192, seeds 0-9. Overnight run on Google Colab (no template, 15 recycles; moved to Colab after the molab sandboxes were shut down). Wild type JAK1 is open in all seeds at this depth; JAK2 V617F at this depth: all open (wild type JAK2 7/16 closed).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9; MSA 512 clusters / 8192 extra; no template. Run time 241 min (whole Colab session incl. setup, Google Colab A100).

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
| 0 | 12 | 86.0 | 46.4 | 92.7 | 3.3 | 1.5 | 81.5 | 82.8 | ma-a1sai |
| 1 | 5 | 85.9 | 46.3 | 92.7 | 3.5 | 1.6 | 81.4 | 82.7 | ma-a1sai |
| 2 | 5 | 86.0 | 46.4 | 92.7 | 3.9 | 1.5 | 81.7 | 82.9 | ma-a1sai |
| 3 | 8 | 85.8 | 46.3 | 92.6 | 3.5 | 1.6 | 81.4 | 82.6 | ma-a1sai |
| 4 | 10 | 85.8 | 46.4 | 92.7 | 3.9 | 1.6 | 81.6 | 82.9 | ma-a1sai |
| 5 | 11 | 86.0 | 46.5 | 92.8 | 3.2 | 1.0 | 81.8 | 83.0 | ma-a1sai |
| 6 | 12 | 85.9 | 46.7 | 93.0 | 3.2 | 0.9 | 82.1 | 83.5 | ma-a1sai |
| 7 | 9 | 85.9 | 46.5 | 92.6 | 3.6 | 1.8 | 81.6 | 82.8 | ma-a1sai |
| 8 | 10 | 86.0 | 46.4 | 92.6 | 3.5 | 1.1 | 81.7 | 82.9 | ma-a1sai |
| 9 | 3 | 85.8 | 46.6 | 93.0 | 3.5 | 1.0 | 82.0 | 83.3 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 2.0 | 0 | 3 | 85.7 | 148 |
| ma-a1sai (open) | 0.6 | 5 | 2 | 85.4 | 148 |
| ma-l9b1f (closed) | 80.6 | 1 | 1 | 83.9 | 0 |
| Shan 2014 (closed, JH2–JH1) | 82.2 | 1 | 1 | 83.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 83.5 | 94.3 | 9.5 | 9.0 | 84.3 | 85.8 |
| 2 | 85.4 | 93.0 | 5.2 | 3.2 | 82.3 | 83.6 |
| 3 | 85.7 | 92.9 | 3.1 | 1.8 | 81.6 | 82.9 |
| 4 | 85.6 | 92.7 | 3.2 | 1.2 | 81.7 | 83.0 |
| 5 | 85.8 | 92.8 | 3.7 | 1.4 | 81.7 | 83.0 |
| 6 | 85.7 | 92.8 | 3.5 | 1.3 | 81.8 | 83.1 |
| 7 | 85.8 | 92.8 | 3.4 | 1.4 | 81.7 | 83.0 |
| 8 | 85.8 | 92.8 | 3.3 | 1.5 | 81.6 | 83.0 |
| 9 | 85.8 | 92.8 | 3.4 | 1.5 | 81.7 | 83.0 |
| 10 | 85.8 | 92.8 | 3.5 | 1.5 | 81.6 | 82.9 |
| 11 | 85.8 | 92.7 | 3.8 | 1.5 | 81.9 | 83.1 |
| 12 | 85.8 | 92.8 | 3.3 | 1.4 | 81.7 | 83.0 |
| 13 | 85.8 | 92.7 | 3.4 | 1.5 | 81.6 | 82.9 |
| 14 | 85.7 | 92.8 | 3.6 | 1.5 | 81.7 | 83.0 |
| 15 | 85.8 | 92.7 | 3.6 | 1.6 | 81.7 | 83.0 |

pLDDT 83.2–86.0; JH2–JH1 46.2–50.1 Å; FERM–JH1 92.0–95.3 Å (open ma-a1sai 92.5 Å, closed ma-l9b1f 40.1 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: ma-a1sai 144, AF2 6.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 94 93 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 1 | 93 93 93 93 93 92 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 2 | 94 93 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 3 | 95 93 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 4 | 95 95 93 92 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 5 | 95 93 93 92 92 93 93 93 93 93 93 92 93 93 93 | open-like (> 80) |
| 6 | 95 93 93 93 93 93 93 93 93 93 93 93 93 92 93 | open-like (> 80) |
| 7 | 92 93 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 8 | 95 93 93 93 93 93 93 93 93 93 92 93 93 92 93 | open-like (> 80) |
| 9 | 94 93 93 93 93 93 93 93 93 93 93 93 92 93 92 | open-like (> 80) |
