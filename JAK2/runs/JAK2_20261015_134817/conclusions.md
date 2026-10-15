# JAK2_20261015_134817 — JAK2 experiment JAK2_notemplate_msa256-1024

JAK2 no-template MSA-depth scan (does JAK2 close on its own, like JAK1 at 128/512?). OpenFold model_1, guided recycling, no template. MSA 256 clusters / 1024 extra.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 256 clusters / 1024 extra; no template. Run time 88 min (whole Colab session incl. setup, Google Colab A100).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 3 | 86.1 | 46.0 | 94.5 | 0.6 | 83.5 | AF2 |
| 1 | 14 | 86.3 | 46.3 | 94.8 | 1.0 | 83.5 | AF2 |
| 2 | 8 | 86.5 | 46.3 | 94.8 | 0.9 | 83.7 | AF2 |
| 3 | 8 | 86.5 | 46.2 | 94.7 | 1.4 | 83.2 | AF2 |
| 4 | 8 | 86.5 | 46.2 | 95.1 | 2.6 | 82.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.5 | 4 | 5 | 86.4 | 70 |
| Shan 2014 (closed, JH2–JH1) | 82.9 | 1 | 10 | 85.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 82.7 | 67.0 | 70.4 | 90.2 |
| 2 | 85.4 | 95.4 | 2.9 | 84.8 |
| 3 | 86.0 | 94.6 | 1.5 | 83.8 |
| 4 | 86.0 | 94.9 | 1.3 | 83.6 |
| 5 | 86.2 | 94.8 | 0.9 | 83.4 |
| 6 | 86.1 | 94.9 | 1.7 | 83.3 |
| 7 | 86.0 | 94.9 | 1.5 | 83.4 |
| 8 | 86.4 | 94.9 | 1.4 | 83.4 |
| 9 | 86.3 | 94.9 | 1.8 | 83.3 |
| 10 | 86.0 | 95.0 | 1.5 | 83.4 |
| 11 | 86.0 | 95.0 | 1.5 | 83.4 |
| 12 | 86.1 | 94.8 | 1.3 | 83.5 |
| 13 | 86.2 | 95.0 | 1.4 | 83.5 |
| 14 | 86.2 | 94.9 | 1.3 | 83.6 |
| 15 | 86.1 | 95.0 | 1.5 | 83.6 |

pLDDT 82.2–86.5; JH2–JH1 46.0–58.1 Å; FERM–JH1 59.9–95.9 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 75.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 80 96 94 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 1 | 67 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 2 | 64 96 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 3 | 63 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 4 | 60 96 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
