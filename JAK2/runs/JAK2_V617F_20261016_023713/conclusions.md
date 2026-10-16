# JAK2_V617F_20261016_023713 — JAK2 experiment JAK2_V617F_msa64-256

JAK2 V617F, MSA 64/256, seeds 0-15. Overnight run on Google Colab (no template, 15 recycles; moved to Colab after the molab sandboxes were shut down). Wild type at this depth (seeds 0-4): all detached-JH1 intermediate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 173 min (whole Colab session incl. setup, Google Colab A100).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 84.1 | 58.3 | 69.9 | 78.7 | 98.1 | AF2 |
| 1 | 11 | 84.2 | 55.0 | 62.6 | 81.3 | 91.2 | AF2 |
| 2 | 5 | 84.2 | 51.9 | 59.9 | 80.8 | 88.0 | AF2 |
| 3 | 6 | 83.9 | 54.8 | 70.5 | 72.4 | 96.0 | AF2 |
| 4 | 11 | 84.2 | 56.8 | 69.2 | 78.0 | 96.0 | AF2 |
| 5 | 11 | 83.8 | 57.4 | 73.5 | 74.1 | 98.8 | AF2 |
| 6 | 12 | 84.0 | 58.0 | 68.0 | 80.4 | 96.3 | AF2 |
| 7 | 11 | 84.2 | 55.0 | 66.9 | 76.8 | 94.0 | AF2 |
| 8 | 11 | 84.1 | 54.5 | 53.4 | 92.4 | 49.4 | Shan 2014 |
| 9 | 11 | 84.3 | 47.3 | 56.0 | 78.6 | 82.0 | AF2 |
| 10 | 6 | 84.2 | 56.1 | 70.2 | 74.8 | 97.2 | AF2 |
| 11 | 12 | 84.1 | 49.1 | 56.1 | 80.8 | 83.7 | AF2 |
| 12 | 11 | 83.9 | 60.0 | 67.6 | 83.8 | 98.0 | AF2 |
| 13 | 12 | 84.1 | 51.1 | 59.6 | 80.3 | 86.4 | AF2 |
| 14 | 11 | 84.2 | 58.3 | 72.8 | 76.9 | 96.6 | AF2 |
| 15 | 11 | 84.1 | 56.8 | 73.0 | 74.0 | 98.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 51.8 | 7 | 2 | 80.1 | 0 |
| Shan 2014 (closed, JH2–JH1) | 47.5 | 8 | 9 | 83.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 73.8 | 49.8 | 82.7 | 70.4 |
| 2 | 81.2 | 65.7 | 66.2 | 81.9 |
| 3 | 83.6 | 68.9 | 68.6 | 88.6 |
| 4 | 83.8 | 68.3 | 71.7 | 89.5 |
| 5 | 83.9 | 68.1 | 73.2 | 90.1 |
| 6 | 83.7 | 66.0 | 76.4 | 88.9 |
| 7 | 83.8 | 64.8 | 78.2 | 89.7 |
| 8 | 83.8 | 65.6 | 78.0 | 90.3 |
| 9 | 83.7 | 65.1 | 79.2 | 90.3 |
| 10 | 83.8 | 67.3 | 76.6 | 91.1 |
| 11 | 84.1 | 65.1 | 79.1 | 90.2 |
| 12 | 83.9 | 64.9 | 79.6 | 90.6 |
| 13 | 83.8 | 63.1 | 82.5 | 90.3 |
| 14 | 83.8 | 63.7 | 81.5 | 90.4 |
| 15 | 83.8 | 63.1 | 80.9 | 89.7 |

pLDDT 72.2–84.3; JH2–JH1 29.3–60.6 Å; FERM–JH1 34.9–78.1 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 211, Shan 2014 29.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 44 72 72 72 73 72 69 68 68 71 70 69 66 67 66 | in between |
| 1 | 56 65 68 67 64 63 64 66 65 65 63 64 61 62 63 | in between |
| 2 | 37 48 70 64 60 58 57 58 59 58 57 59 56 58 57 | in between |
| 3 | 55 72 72 72 73 70 69 68 66 69 69 69 67 68 68 | in between |
| 4 | 48 65 72 71 77 72 68 70 68 73 69 69 67 68 67 | in between |
| 5 | 63 70 68 69 74 72 72 73 73 75 74 74 74 73 74 | in between |
| 6 | 59 72 73 73 78 71 67 68 68 71 68 68 66 67 67 | in between |
| 7 | 56 60 67 65 65 66 66 68 68 70 67 65 65 64 64 | in between |
| 8 | 37 56 61 63 56 54 52 53 52 54 53 51 52 50 51 | in between |
| 9 | 35 67 64 60 56 51 58 55 58 57 56 57 56 56 55 | in between |
| 10 | 49 72 73 76 75 70 68 68 69 71 70 70 68 69 68 | in between |
| 11 | 51 67 68 63 58 59 56 56 58 58 56 56 56 56 55 | in between |
| 12 | 49 72 74 74 72 69 67 68 68 71 68 65 63 65 63 | in between |
| 13 | 48 54 58 60 60 57 57 61 60 60 59 60 58 59 59 | in between |
| 14 | 47 70 73 74 77 77 76 77 72 78 73 71 67 66 66 | in between |
| 15 | 63 69 71 70 72 74 72 73 72 76 73 70 67 69 68 | in between |

## Interpretation (vs wild type)
- Final states (16 seeds): **14 detached JH1, 2 other** (JH1 on JH2 in a non-reference position); none open, closed or 7T6F-like.
- Wild type at the same depth ([JAK2_20261015_134839](../JAK2_20261015_134839), 5 seeds): 5/5 detached JH1. **No effect of V617F at this shallow MSA.**
