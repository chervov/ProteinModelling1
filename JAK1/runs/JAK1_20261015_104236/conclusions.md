# JAK1_20261015_104236 — JAK1, no template, MSA 256 clusters / 1024 extra

Part of the JAK1 MSA-depth scan. OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4, no template. Run time 52 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 14 | 85.7 | 46.7 | 93.1 | 3.0 | 2.2 | 82.2 | 83.7 | ma-a1sai |
| 1 | 15 | 85.8 | 46.6 | 93.2 | 3.0 | 1.5 | 81.7 | 83.0 | ma-a1sai |
| 2 | 10 | 85.8 | 46.6 | 93.2 | 3.4 | 0.8 | 82.0 | 83.3 | ma-a1sai |
| 3 | 11 | 85.8 | 46.7 | 93.1 | 2.8 | 1.0 | 81.9 | 83.3 | ma-a1sai |
| 4 | 14 | 85.5 | 46.5 | 92.8 | 3.0 | 1.2 | 82.0 | 83.3 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 1.2 | 3 | 6 | 85.5 | 68 |
| ma-a1sai (open) | 0.6 | 4 | 6 | 85.2 | 68 |
| ma-l9b1f (closed) | 19.0 | 2 | 1 | 82.0 | 0 |
| Shan 2014 (closed, JH2–JH1) | 24.8 | 2 | 1 | 82.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 82.3 | 40.6 | 93.4 | 94.6 | 25.5 | 31.3 |
| 2 | 84.5 | 93.4 | 15.1 | 13.1 | 86.8 | 87.7 |
| 3 | 85.2 | 93.2 | 4.1 | 2.5 | 82.9 | 84.2 |
| 4 | 85.2 | 93.2 | 3.5 | 1.4 | 82.4 | 83.8 |
| 5 | 85.4 | 93.0 | 3.6 | 1.8 | 82.4 | 83.7 |
| 6 | 85.3 | 92.9 | 2.7 | 1.9 | 82.0 | 83.3 |
| 7 | 85.4 | 92.8 | 2.8 | 1.9 | 81.9 | 83.3 |
| 8 | 85.5 | 92.9 | 3.0 | 1.4 | 82.0 | 83.3 |
| 9 | 85.5 | 93.1 | 3.1 | 1.6 | 82.2 | 83.5 |
| 10 | 85.5 | 92.9 | 3.1 | 1.2 | 82.0 | 83.3 |
| 11 | 85.5 | 93.1 | 3.2 | 1.9 | 82.2 | 83.6 |
| 12 | 85.6 | 93.0 | 3.0 | 1.7 | 81.9 | 83.3 |
| 13 | 85.5 | 93.2 | 2.9 | 1.4 | 81.8 | 83.1 |
| 14 | 85.6 | 93.1 | 3.2 | 1.2 | 82.1 | 83.4 |
| 15 | 85.6 | 93.0 | 3.0 | 1.4 | 81.8 | 83.1 |

pLDDT 82.0–85.8; JH2–JH1 46.4–53.5 Å; FERM–JH1 38.9–94.4 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-a1sai 65, ma-l9b1f 5, AF2 5.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~92, closed ~40)

| seed | recycles 1–15 |
|---|---|
| 0 | 39 94 93 93 93 93 93 93 93 93 93 93 93 93 93 |
| 1 | 42 94 94 93 93 93 93 93 94 93 93 93 93 93 93 |
| 2 | 40 93 93 93 93 93 93 93 93 93 94 94 93 93 93 |
| 3 | 42 93 94 93 93 93 93 93 93 93 93 93 94 93 93 |
| 4 | 41 93 92 93 93 93 93 93 93 92 93 92 93 93 93 |

## Interpretation
- **Open in all seeds, from recycle 2 on.** Selected structures are 0.8–2.2 Å from Orianne's open ma-a1sai (closest
  0.6 Å), pLDDT 85.5–85.8; 68 of 75 conformations are within 15 Å of the open references.
- Recycle 1 is FERM-bound in every seed (FERM–JH1 39–42 Å) but not the closed state (≥ 19 Å from ma-l9b1f); the
  network leaves it immediately at recycle 2.
- So at 256/1024 the MSA already gives the open state as clearly as the whole MSA (512/8192). The bistable depth is
  narrow, around 128/512 (see [JAK1/MSA_scan_summary.md](../../MSA_scan_summary.md)).
