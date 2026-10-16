# JAK1_V658F_20261015_220522 — JAK2 experiment JAK1_V658F_msa32-64

JAK1 V658F, MSA 32/64, seeds 0-4, on a Colab L4. Overnight run on Google Colab (no template, 15 recycles; moved to Colab after the molab sandboxes were shut down). Wild type at this depth only from the earlier campaign (compact, FERM-bound, low confidence).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 32 clusters / 64 extra; no template. Run time 224 min (whole Colab session incl. setup, Google Colab L4).

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
| 0 | 6 | 81.7 | 58.1 | 47.9 | 103.9 | 102.6 | 68.0 | 58.6 | Shan 2014 |
| 1 | 12 | 82.1 | 58.5 | 44.4 | 104.7 | 104.5 | 40.7 | 34.3 | Shan 2014 |
| 2 | 13 | 81.5 | 54.8 | 48.0 | 99.4 | 98.9 | 43.3 | 35.7 | Shan 2014 |
| 3 | 15 | 82.4 | 52.9 | 57.4 | 99.2 | 99.1 | 34.3 | 28.2 | Shan 2014 |
| 4 | 11 | 82.4 | 59.2 | 49.8 | 106.9 | 105.9 | 61.6 | 52.0 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 87.4 | 1 | 13 | 76.7 | 0 |
| ma-a1sai (open) | 86.5 | 1 | 13 | 76.7 | 0 |
| ma-l9b1f (closed) | 27.8 | 3 | 13 | 82.2 | 0 |
| Shan 2014 (closed, JH2–JH1) | 24.4 | 3 | 13 | 82.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 57.5 | 48.6 | 98.5 | 97.8 | 42.5 | 33.7 |
| 2 | 68.6 | 48.9 | 103.2 | 102.3 | 56.8 | 47.6 |
| 3 | 72.9 | 51.3 | 104.0 | 102.8 | 64.0 | 54.1 |
| 4 | 76.1 | 51.0 | 103.6 | 102.5 | 61.5 | 51.8 |
| 5 | 78.3 | 47.8 | 105.3 | 104.3 | 63.1 | 53.4 |
| 6 | 78.9 | 47.1 | 103.0 | 101.9 | 59.9 | 50.3 |
| 7 | 79.8 | 48.8 | 105.6 | 104.6 | 60.2 | 50.9 |
| 8 | 79.6 | 47.3 | 104.2 | 103.4 | 56.6 | 47.9 |
| 9 | 79.5 | 47.9 | 104.2 | 103.4 | 54.2 | 45.7 |
| 10 | 81.4 | 48.4 | 104.9 | 104.3 | 53.3 | 44.7 |
| 11 | 81.3 | 40.1 | 101.7 | 101.1 | 54.3 | 47.1 |
| 12 | 81.7 | 48.4 | 102.7 | 102.1 | 49.6 | 41.8 |
| 13 | 80.6 | 42.3 | 99.2 | 98.5 | 51.8 | 44.5 |
| 14 | 81.7 | 50.7 | 103.0 | 102.6 | 45.2 | 37.9 |
| 15 | 81.8 | 49.2 | 103.0 | 102.5 | 47.3 | 39.7 |

pLDDT 56.4–82.4; JH2–JH1 47.3–63.0 Å; FERM–JH1 11.6–57.6 Å (open ma-a1sai 92.5 Å, closed ma-l9b1f 40.1 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 75.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 44 51 50 50 48 48 48 47 47 47 48 50 47 48 48 | closed-like (< 50) |
| 1 | 53 53 50 49 45 46 50 45 46 47 43 44 12 47 41 | closed-like (< 50) |
| 2 | 48 54 58 53 50 49 50 52 52 51 15 44 48 57 52 | in between |
| 3 | 48 33 42 48 46 46 46 43 45 48 45 53 58 57 57 | in between |
| 4 | 50 54 57 55 50 47 50 50 50 49 50 51 47 46 47 | closed-like (< 50) |
