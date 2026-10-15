# JAK2_20261015_134839 — JAK2 experiment JAK2_notemplate_msa64-256

JAK2 no-template MSA-depth scan (does JAK2 close on its own, like JAK1 at 128/512?). OpenFold model_1, guided recycling, no template. MSA 64 clusters / 256 extra. Run on an L4 (also to measure L4 speed).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 64 clusters / 256 extra; no template. Run time 219 min (whole Colab session incl. setup, Google Colab L4).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 10 | 84.0 | 57.9 | 58.7 | 87.8 | 92.1 | AF2 |
| 1 | 10 | 83.9 | 59.2 | 62.6 | 87.1 | 95.5 | AF2 |
| 2 | 10 | 84.1 | 56.2 | 68.8 | 75.7 | 96.3 | AF2 |
| 3 | 12 | 83.8 | 60.9 | 60.4 | 89.6 | 96.5 | AF2 |
| 4 | 14 | 84.0 | 53.4 | 68.0 | 72.9 | 93.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 68.5 | 4 | 11 | 83.0 | 0 |
| Shan 2014 (closed, JH2–JH1) | 65.5 | 1 | 1 | 73.3 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 73.1 | 42.7 | 91.3 | 76.4 |
| 2 | 81.5 | 65.2 | 78.3 | 94.2 |
| 3 | 83.6 | 66.0 | 80.5 | 95.8 |
| 4 | 83.4 | 62.4 | 83.7 | 94.5 |
| 5 | 83.6 | 64.4 | 80.6 | 94.7 |
| 6 | 83.5 | 63.7 | 82.4 | 94.3 |
| 7 | 83.7 | 64.1 | 81.4 | 94.2 |
| 8 | 83.6 | 63.2 | 82.2 | 93.9 |
| 9 | 83.6 | 63.5 | 80.6 | 94.2 |
| 10 | 83.9 | 63.3 | 83.2 | 94.5 |
| 11 | 83.4 | 61.6 | 84.4 | 93.3 |
| 12 | 83.8 | 63.0 | 84.3 | 95.1 |
| 13 | 83.8 | 64.3 | 80.8 | 93.8 |
| 14 | 83.6 | 63.0 | 83.3 | 94.2 |
| 15 | 83.7 | 63.2 | 83.5 | 94.5 |

pLDDT 71.6–84.1; JH2–JH1 48.0–63.2 Å; FERM–JH1 29.6–69.7 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 70, Shan 2014 5.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 30 65 70 60 65 62 62 59 59 59 58 57 56 58 59 | in between |
| 1 | 30 62 65 61 63 63 63 63 62 63 61 63 66 60 64 | in between |
| 2 | 50 67 67 65 66 67 68 67 68 69 66 68 68 68 67 | in between |
| 3 | 55 66 63 57 62 60 62 61 62 60 59 60 61 62 62 | in between |
| 4 | 49 66 66 68 65 67 67 66 65 66 64 67 70 68 65 | in between |

## Interpretation
- **All 5 seeds in the detached-JH1 intermediate:** FERM–JH1 59–67 Å, JH2–JH1 54–60 Å, 77–97 Å from every reference (including 7T6F); JH1 nearly without contacts (0–10 pairs with JH2, 0–4 with FERM). Run on a Colab L4 (219 min).
- Details: [JAK2_intermediate.md](../../JAK2_intermediate.md).
