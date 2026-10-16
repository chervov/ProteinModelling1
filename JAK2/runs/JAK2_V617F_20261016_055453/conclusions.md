# JAK2_V617F_20261016_055453 — JAK2 experiment JAK2_V617F_msa96-384_rerun

JAK2 V617F, MSA 96/384, seeds 0-15. Overnight run on Google Colab (no template, 15 recycles; moved to Colab after the molab sandboxes were shut down). Rerun: the first run finished but its GitHub push was rejected by a concurrent commit. Wild type at this depth (seeds 0-4): 4 next to FERM, 1 detached JH1 (JAK2_20261015_172727).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 96 clusters / 384 extra; no template. Run time 173 min (whole Colab session incl. setup, Google Colab A100).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 84.6 | 50.0 | 53.7 | 83.0 | 83.3 | AF2 |
| 1 | 7 | 84.3 | 50.3 | 52.2 | 89.7 | 38.2 | Shan 2014 |
| 2 | 5 | 84.5 | 58.3 | 62.3 | 86.4 | 95.3 | AF2 |
| 3 | 3 | 84.6 | 50.5 | 58.4 | 80.6 | 86.5 | AF2 |
| 4 | 7 | 84.8 | 48.6 | 57.2 | 79.8 | 83.6 | AF2 |
| 5 | 10 | 84.5 | 47.9 | 60.6 | 75.1 | 87.0 | AF2 |
| 6 | 12 | 84.5 | 59.3 | 55.7 | 92.0 | 92.2 | AF2 |
| 7 | 4 | 84.0 | 44.9 | 45.2 | 87.7 | 17.1 | Shan 2014 |
| 8 | 10 | 84.3 | 48.1 | 50.9 | 88.7 | 25.1 | Shan 2014 |
| 9 | 7 | 84.7 | 49.6 | 54.5 | 82.3 | 84.0 | AF2 |
| 10 | 10 | 84.5 | 61.3 | 59.4 | 92.5 | 95.2 | AF2 |
| 11 | 10 | 84.3 | 62.1 | 59.3 | 92.3 | 95.7 | AF2 |
| 12 | 10 | 84.2 | 48.3 | 50.4 | 88.9 | 26.0 | Shan 2014 |
| 13 | 4 | 84.3 | 53.0 | 51.5 | 92.1 | 47.5 | Shan 2014 |
| 14 | 10 | 84.3 | 58.2 | 62.1 | 84.4 | 95.7 | AF2 |
| 15 | 3 | 84.7 | 51.5 | 55.6 | 83.4 | 86.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 64.4 | 4 | 4 | 79.5 | 0 |
| Shan 2014 (closed, JH2–JH1) | 6.9 | 7 | 6 | 83.7 | 11 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 76.6 | 43.4 | 97.3 | 79.8 |
| 2 | 83.1 | 51.4 | 91.6 | 77.8 |
| 3 | 84.1 | 56.9 | 87.4 | 76.7 |
| 4 | 83.9 | 56.0 | 85.4 | 72.9 |
| 5 | 84.1 | 56.8 | 85.0 | 72.7 |
| 6 | 84.2 | 57.2 | 84.6 | 73.2 |
| 7 | 84.3 | 55.6 | 85.5 | 69.9 |
| 8 | 84.0 | 55.4 | 85.0 | 68.3 |
| 9 | 84.2 | 55.7 | 85.2 | 69.4 |
| 10 | 84.4 | 55.0 | 85.5 | 69.1 |
| 11 | 84.1 | 54.8 | 85.0 | 67.8 |
| 12 | 84.2 | 56.0 | 84.6 | 70.2 |
| 13 | 84.1 | 55.2 | 85.1 | 68.9 |
| 14 | 84.1 | 55.1 | 85.9 | 69.0 |
| 15 | 84.2 | 55.5 | 85.0 | 69.0 |

pLDDT 74.4–84.8; JH2–JH1 30.9–64.5 Å; FERM–JH1 22.2–65.7 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 142, Shan 2014 98.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 44 59 61 58 54 55 53 53 54 52 54 53 53 54 53 | in between |
| 1 | 34 51 57 53 53 54 52 49 50 50 50 50 50 49 51 | in between |
| 2 | 50 51 57 62 62 60 55 59 60 57 56 61 60 61 59 | in between |
| 3 | 44 61 58 57 59 58 57 58 57 58 58 58 58 58 59 | in between |
| 4 | 42 56 59 51 60 57 57 57 57 57 57 58 58 58 58 | in between |
| 5 | 36 55 55 58 59 61 64 60 62 61 60 62 60 64 61 | in between |
| 6 | 51 22 59 61 62 60 59 60 60 55 56 56 54 53 53 | in between |
| 7 | 40 22 43 45 45 46 45 46 45 46 45 46 46 45 46 | closed-like (< 50) |
| 8 | 47 48 54 50 53 53 52 50 50 51 51 51 52 49 54 | in between |
| 9 | 54 65 63 60 57 57 54 55 56 54 54 56 56 55 54 | in between |
| 10 | 40 59 60 61 63 62 60 60 61 59 58 60 59 58 59 | in between |
| 11 | 32 57 58 61 61 63 60 61 60 59 58 60 60 59 58 | in between |
| 12 | 35 58 53 49 50 52 52 50 50 50 49 50 49 48 50 | in between |
| 13 | 47 39 55 52 50 54 50 50 52 51 51 52 50 51 51 | in between |
| 14 | 45 59 62 63 64 65 63 63 62 62 63 66 64 62 64 | in between |
| 15 | 52 60 56 56 57 57 55 56 56 56 57 57 56 57 58 | in between |

## Interpretation (vs wild type)
- Final states (16 seeds): **12 detached JH1, 3 next to FERM, 1 closed (3.3 Å)**.
- Wild type at the same depth ([JAK2_20261015_172727](../JAK2_20261015_172727), 5 seeds): 4 next to FERM, 1 detached. Here V617F shifts JAK2 towards the detached-JH1 state (1/5 → 12/16, p = 0.047) — the opposite of 128/512.
