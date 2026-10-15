# JAK1_20261015_095803 — JAK1, no template, MSA 64 clusters / 256 extra

Part of the JAK1 MSA-depth scan. OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4, no template. Run time 88 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 84.5 | 47.1 | 83.9 | 53.3 | 51.3 | 83.4 | 81.7 | ma-a1sai |
| 1 | 9 | 84.7 | 47.6 | 83.9 | 54.5 | 52.5 | 84.2 | 82.3 | ma-a1sai |
| 2 | 9 | 85.0 | 46.7 | 82.7 | 54.4 | 52.4 | 83.2 | 81.2 | ma-a1sai |
| 3 | 9 | 84.8 | 46.6 | 83.3 | 53.2 | 51.2 | 83.2 | 81.5 | ma-a1sai |
| 4 | 8 | 84.5 | 46.5 | 84.9 | 49.1 | 47.2 | 83.0 | 81.8 | ma-a1sai |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 37.4 | 4 | 15 | 83.5 | 0 |
| ma-a1sai (open) | 35.6 | 4 | 15 | 83.5 | 0 |
| ma-l9b1f (closed) | 31.8 | 1 | 2 | 80.8 | 0 |
| Shan 2014 (closed, JH2–JH1) | 34.7 | 1 | 2 | 80.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 72.4 | 50.9 | 70.0 | 68.4 | 62.5 | 56.4 |
| 2 | 80.4 | 43.2 | 87.8 | 88.8 | 36.3 | 38.5 |
| 3 | 83.1 | 68.6 | 73.1 | 73.1 | 73.0 | 74.4 |
| 4 | 83.9 | 82.9 | 62.2 | 60.8 | 88.1 | 86.8 |
| 5 | 84.3 | 85.9 | 55.7 | 53.9 | 88.8 | 87.1 |
| 6 | 84.3 | 84.8 | 53.6 | 51.4 | 85.8 | 83.8 |
| 7 | 84.1 | 83.6 | 54.0 | 52.0 | 83.7 | 81.9 |
| 8 | 84.5 | 83.5 | 54.0 | 52.0 | 83.6 | 81.7 |
| 9 | 84.6 | 83.7 | 53.5 | 51.4 | 83.7 | 81.9 |
| 10 | 84.5 | 83.8 | 50.2 | 48.2 | 82.5 | 81.1 |
| 11 | 84.5 | 83.9 | 52.8 | 50.8 | 83.7 | 82.0 |
| 12 | 84.4 | 84.3 | 51.3 | 49.3 | 83.4 | 81.9 |
| 13 | 84.5 | 83.7 | 50.9 | 49.0 | 82.5 | 81.0 |
| 14 | 84.5 | 83.7 | 50.3 | 48.4 | 82.3 | 81.0 |
| 15 | 84.1 | 84.8 | 46.1 | 44.3 | 81.6 | 80.8 |

pLDDT 71.5–85.0; JH2–JH1 3.9–59.1 Å; FERM–JH1 37.6–92.2 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-a1sai 62, ma-l9b1f 7, Shan 2014 6.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~92, closed ~40)

| seed | recycles 1–15 |
|---|---|
| 0 | 56 49 92 89 85 83 82 82 84 83 84 84 84 84 84 |
| 1 | 50 43 84 89 85 84 84 84 84 84 84 84 84 84 85 |
| 2 | 49 41 68 85 83 82 83 83 83 84 83 84 83 83 84 |
| 3 | 51 38 50 86 88 84 85 83 83 83 83 84 83 83 84 |
| 4 | 48 45 49 66 89 91 85 85 85 84 86 85 85 85 87 |

## Interpretation
- **All 5 seeds end in the same third arrangement, matching neither reference.** JH1 leaves FERM (FERM–JH1 ~83–87 Å,
  like the open models) but sits in a different place relative to JH2: 47–52 Å from the open ma-a1sai and ~83 Å from
  the closed ma-l9b1f (JH1 RMSD after superposing JH2). No conformation is within 15 Å of any reference.
- **Early recycles are FERM-bound** (FERM–JH1 38–50 Å at recycles 1–2), but even then they are ≥ 31.8 Å from the
  closed ma-l9b1f — compact, not the real closed state (as in the earlier 32/64 runs).
- pLDDT 84.5–85.0 for the selected structures, but down to 71.5 in some early recycles; one conformation has a
  JH2–JH1 centroid distance of only 3.9 Å (overlapping domains, a broken structure).
- **Comparison along the MSA-depth scan (no template, 15 recycles):** 512/8192 → open (ma-a1sai-like) in all seeds;
  **128/512 → bistable: 2/5 closed (best 2.4 Å from ma-l9b1f), 2 open, 1 switching**; 64/256 → a consistent
  non-reference arrangement. So 128/512 is the depth where both real states appear; at 64/256 the MSA signal is
  already too weak for either. (256/1024 is running next.)
- Note: this run was interrupted by a kernel restart; the detached inference continued, and the notebook was rerun.
