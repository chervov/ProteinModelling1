# JAK2_20261016_053140 — JAK2 experiment JAK2_WT_msa64-256_seeds5-15

JAK2 wild type, MSA 64/256, seeds 5-15 (with seeds 0-4: 16 seeds). Overnight run on Google Colab (no template, 15 recycles; moved to Colab after the molab sandboxes were shut down).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5,6,7,8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 127 min (whole Colab session incl. setup, Google Colab A100).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 5 | 10 | 83.9 | 54.5 | 57.1 | 90.6 | 50.7 | Shan 2014 |
| 6 | 14 | 84.1 | 53.4 | 58.3 | 89.2 | 49.2 | Shan 2014 |
| 7 | 7 | 84.0 | 60.0 | 60.0 | 90.3 | 93.4 | AF2 |
| 8 | 7 | 84.3 | 56.5 | 55.2 | 89.8 | 83.0 | Shan 2014 |
| 9 | 14 | 83.9 | 51.5 | 52.3 | 90.1 | 38.5 | Shan 2014 |
| 10 | 10 | 84.2 | 60.2 | 57.2 | 92.6 | 92.5 | Shan 2014 |
| 11 | 12 | 84.3 | 59.6 | 62.1 | 88.1 | 94.9 | AF2 |
| 12 | 7 | 83.8 | 53.9 | 63.7 | 84.0 | 59.1 | Shan 2014 |
| 13 | 7 | 84.3 | 60.8 | 60.3 | 91.2 | 92.3 | AF2 |
| 14 | 14 | 83.9 | 51.4 | 49.5 | 91.5 | 39.0 | Shan 2014 |
| 15 | 14 | 83.9 | 54.3 | 56.9 | 90.0 | 53.7 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 56.8 | 6 | 2 | 80.3 | 0 |
| Shan 2014 (closed, JH2–JH1) | 20.9 | 8 | 1 | 72.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 72.3 | 33.7 | 90.1 | 39.7 |
| 2 | 82.2 | 48.2 | 89.0 | 60.3 |
| 3 | 83.7 | 55.1 | 88.6 | 64.9 |
| 4 | 83.7 | 56.1 | 89.5 | 66.5 |
| 5 | 83.6 | 56.4 | 89.1 | 66.2 |
| 6 | 83.5 | 57.0 | 89.4 | 66.1 |
| 7 | 84.0 | 57.1 | 89.1 | 66.7 |
| 8 | 83.6 | 57.2 | 89.5 | 67.4 |
| 9 | 83.8 | 56.5 | 90.9 | 68.3 |
| 10 | 84.0 | 57.2 | 89.9 | 67.4 |
| 11 | 83.7 | 57.3 | 89.5 | 68.1 |
| 12 | 83.8 | 56.6 | 90.2 | 68.0 |
| 13 | 83.7 | 56.1 | 90.8 | 67.3 |
| 14 | 84.0 | 57.0 | 90.4 | 67.8 |
| 15 | 83.7 | 57.4 | 89.7 | 68.7 |

pLDDT 71.0–84.3; JH2–JH1 20.7–61.3 Å; FERM–JH1 20.1–68.3 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 133, AF2 32.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 35 43 54 55 57 57 56 57 57 57 61 59 60 61 61 | in between |
| 6 | 35 51 55 53 54 54 55 60 60 58 57 57 56 58 57 | in between |
| 7 | 32 48 56 59 59 61 60 57 57 58 58 56 58 57 59 | in between |
| 8 | 31 45 52 53 55 55 55 53 55 54 55 54 55 54 56 | in between |
| 9 | 39 41 51 48 47 50 49 53 52 52 52 51 51 52 52 | in between |
| 10 | 41 54 56 56 57 57 58 56 55 57 57 56 56 56 57 | in between |
| 11 | 55 59 64 65 68 67 67 62 61 62 63 62 60 62 62 | in between |
| 12 | 38 52 60 62 62 61 64 62 61 62 61 61 61 62 61 | in between |
| 13 | 20 48 54 60 60 61 60 58 57 59 59 59 57 58 60 | in between |
| 14 | 22 49 53 53 50 52 51 51 50 50 50 48 49 50 49 | closed-like (< 50) |
| 15 | 21 41 52 52 52 51 54 58 58 59 57 57 56 57 58 | in between |

## Interpretation
- Final states (seeds 5–15): 5 detached JH1, 4 other (JH1 on JH2 in a non-reference position), 2 next to FERM; none open, closed or 7T6F-like.
- Pooled with seeds 0–4 ([JAK2_20261015_134839](../JAK2_20261015_134839)): **16 seeds — 10 detached JH1**, 4 other, 2 next to FERM. V617F at this depth ([JAK2_V617F_20261016_023713](../JAK2_V617F_20261016_023713)): 14/16 detached — no meaningful mutation effect at 64/256.
