# JAK1_20261015_135849 — JAK1, no template, MSA 96 clusters / 384 extra

Part of the JAK1 MSA-depth scan (see JAK1/MSA_scan_summary.md). OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4, no template. Run time 45 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 6 | 84.1 | 46.9 | 45.7 | 86.4 | 87.6 | 19.1 | 27.2 | ma-l9b1f |
| 1 | 2 | 84.1 | 42.7 | 47.4 | 80.1 | 81.2 | 12.1 | 22.0 | ma-l9b1f |
| 2 | 11 | 85.4 | 44.6 | 84.3 | 46.5 | 44.6 | 81.6 | 80.7 | ma-a1sai |
| 3 | 2 | 84.3 | 44.4 | 47.0 | 82.8 | 84.0 | 16.2 | 25.5 | ma-l9b1f |
| 4 | 12 | 85.8 | 44.1 | 84.0 | 45.8 | 43.9 | 81.2 | 80.4 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 44.9 | 0 | 9 | 84.1 | 0 |
| ma-a1sai (open) | 43.3 | 4 | 9 | 85.6 | 0 |
| ma-l9b1f (closed) | 3.8 | 4 | 3 | 83.6 | 15 |
| Shan 2014 (closed, JH2–JH1) | 13.5 | 4 | 2 | 83.6 | 2 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 77.7 | 42.9 | 71.4 | 71.5 | 30.5 | 27.2 |
| 2 | 83.9 | 46.7 | 81.0 | 82.1 | 13.9 | 22.9 |
| 3 | 83.9 | 45.5 | 83.3 | 84.5 | 14.7 | 24.0 |
| 4 | 84.0 | 46.6 | 82.3 | 83.6 | 18.6 | 27.5 |
| 5 | 84.0 | 55.3 | 76.5 | 77.1 | 33.6 | 40.3 |
| 6 | 84.4 | 55.4 | 75.9 | 76.5 | 33.3 | 39.9 |
| 7 | 84.5 | 62.4 | 69.1 | 69.0 | 47.7 | 52.2 |
| 8 | 84.4 | 61.8 | 70.1 | 70.0 | 45.2 | 49.9 |
| 9 | 84.6 | 69.2 | 60.3 | 60.1 | 56.6 | 60.4 |
| 10 | 84.4 | 60.8 | 68.5 | 68.4 | 41.9 | 47.1 |
| 11 | 84.6 | 61.5 | 68.7 | 68.7 | 42.8 | 47.9 |
| 12 | 84.6 | 61.5 | 68.6 | 68.6 | 44.4 | 49.3 |
| 13 | 84.4 | 60.7 | 67.9 | 67.9 | 41.3 | 46.5 |
| 14 | 84.6 | 67.1 | 64.6 | 64.7 | 54.7 | 58.9 |
| 15 | 84.6 | 61.6 | 68.6 | 68.6 | 44.5 | 49.3 |

pLDDT 77.1–85.8; JH2–JH1 31.4–50.6 Å; FERM–JH1 24.2–86.0 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-l9b1f 49, ma-a1sai 20, Shan 2014 5, AF2 1.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~92, closed ~40)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 45 53 49 47 47 46 49 46 83 46 46 47 47 70 46 | closed-like (< 50) |
| 1 | 50 47 46 45 43 44 46 46 49 44 46 45 44 48 46 | closed-like (< 50) |
| 2 | 24 42 43 52 54 58 85 86 83 84 84 84 84 84 84 | open-like (> 80) |
| 3 | 49 47 48 47 47 46 47 47 47 46 47 48 45 50 48 | closed-like (< 50) |
| 4 | 46 44 41 41 85 84 84 84 84 84 84 84 84 84 84 | open-like (> 80) |

## Interpretation
- **No seed goes open at this depth.** Seeds 0, 1, 3 stay next to FERM for all 15 recycles (FERM–JH1 ~45–48 Å),
  12–19 Å from the closed ma-l9b1f (selected structures) — close to, but not quite, the closed reference arrangement.
  Seeds 2 and 4 move to the **third arrangement** seen at 64/256 (FERM–JH1 ~84 Å, ~44 Å from the open ma-a1sai,
  ~81 Å from the closed ma-l9b1f); seed 4 passes within 3.8 Å of ma-l9b1f at recycle 3 on the way.
- 49 of 75 conformations are nearest to the closed ma-l9b1f, none is within 15 Å of an open reference.
- **96/384 is between the bistable depth (128/512: open or closed) and 64/256 (third arrangement only):** the open
  state disappears first when the MSA is reduced; the FERM-bound state and the third arrangement remain.
