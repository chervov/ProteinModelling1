# JAK2_V617F_20261015_215648 — JAK2 experiment JAK2_V617F_msa256-1024

JAK2 overnight runs on Google Colab (no template, 15 recycles). JAK2 V617F, MSA 256/1024, seeds 0-7. Wild type at this depth: all open (seeds 0-4).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 256 clusters / 1024 extra; no template. Run time 106 min (whole Colab session incl. setup, Google Colab A100).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 85.8 | 46.3 | 94.9 | 1.1 | 83.5 | AF2 |
| 1 | 9 | 85.0 | 47.0 | 50.2 | 88.1 | 23.7 | Shan 2014 |
| 2 | 8 | 86.1 | 46.5 | 94.9 | 1.8 | 83.7 | AF2 |
| 3 | 8 | 85.0 | 47.6 | 50.4 | 88.6 | 24.3 | Shan 2014 |
| 4 | 5 | 85.0 | 45.7 | 49.5 | 86.7 | 19.5 | Shan 2014 |
| 5 | 10 | 86.1 | 46.2 | 94.9 | 1.3 | 83.3 | AF2 |
| 6 | 15 | 85.8 | 46.3 | 94.7 | 0.9 | 83.6 | AF2 |
| 7 | 2 | 85.1 | 49.5 | 47.6 | 91.5 | 29.4 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.7 | 2 | 13 | 85.9 | 53 |
| Shan 2014 (closed, JH2–JH1) | 10.2 | 7 | 7 | 84.6 | 7 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 81.8 | 46.2 | 82.9 | 48.2 |
| 2 | 84.9 | 66.2 | 67.6 | 64.0 |
| 3 | 85.1 | 72.8 | 45.5 | 55.1 |
| 4 | 85.1 | 72.4 | 44.9 | 51.6 |
| 5 | 85.2 | 72.8 | 44.6 | 51.8 |
| 6 | 85.3 | 72.8 | 44.8 | 52.6 |
| 7 | 85.1 | 72.3 | 43.9 | 51.0 |
| 8 | 85.4 | 72.5 | 44.8 | 52.3 |
| 9 | 85.3 | 72.3 | 43.7 | 50.5 |
| 10 | 85.2 | 72.2 | 44.1 | 51.2 |
| 11 | 85.1 | 71.8 | 44.6 | 51.0 |
| 12 | 85.3 | 72.6 | 43.9 | 50.3 |
| 13 | 85.2 | 72.4 | 43.7 | 50.5 |
| 14 | 85.1 | 72.0 | 43.8 | 50.0 |
| 15 | 85.2 | 72.2 | 43.5 | 49.3 |

pLDDT 80.7–86.1; JH2–JH1 28.7–55.2 Å; FERM–JH1 23.1–95.8 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 63, AF2 57.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 55 60 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 1 | 59 58 53 52 52 52 52 52 50 51 50 51 51 51 50 | in between |
| 2 | 36 80 96 94 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 3 | 46 54 50 51 51 51 50 50 51 51 49 52 51 50 51 | in between |
| 4 | 42 51 50 50 50 50 49 50 50 49 48 50 50 49 49 | closed-like (< 50) |
| 5 | 23 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 6 | 64 84 96 95 96 96 96 96 96 96 96 96 95 95 95 | open-like (> 80) |
| 7 | 45 48 48 47 49 49 47 47 48 47 46 48 48 48 48 | closed-like (< 50) |

## Interpretation (vs wild type)
- Final states (8 seeds): **4 open, 1 closed (6.6 Å from the closed JAK2), 3 next to FERM near the closed state (11.6–12.7 Å)**.
- Wild type at the same depth (16 seeds, [JAK2_20261015_134817](../JAK2_20261015_134817) + [JAK2_20261015_201144](../JAK2_20261015_201144)): all open.
- **Here V617F moves JAK2 towards the closed state** (closed or near-closed 0/16 → 4/8, Fisher p = 0.0066) — the opposite direction to 512/8192 (closed 7/16 → 0/16).
