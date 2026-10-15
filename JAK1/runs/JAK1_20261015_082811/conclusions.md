# JAK1_20261015_082811 — JAK1, no template, MSA 128 clusters / 512 extra

Part of the JAK1 MSA-depth scan. OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4, no template. Run time 52 min (whole notebook, RTX PRO 6000).

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 12 | 84.9 | 53.4 | 74.9 | 69.0 | 70.7 | 68.8 | 73.9 | ma-l9b1f |
| 1 | 15 | 85.1 | 46.6 | 93.0 | 2.6 | 2.5 | 82.0 | 83.5 | ma-a1sai |
| 2 | 3 | 84.6 | 48.7 | 45.8 | 87.6 | 88.9 | 25.1 | 32.6 | ma-l9b1f |
| 3 | 13 | 85.6 | 44.8 | 85.1 | 45.1 | 43.3 | 81.8 | 81.1 | ma-a1sai |
| 4 | 13 | 83.9 | 40.0 | 40.8 | 80.9 | 81.8 | 4.5 | 14.4 | ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P23458-F1) | 2.6 | 1 | 15 | 85.1 | 11 |
| ma-a1sai (open) | 2.5 | 1 | 15 | 85.1 | 11 |
| ma-l9b1f (closed) | 2.4 | 4 | 4 | 83.5 | 15 |
| Shan 2014 (closed, JH2–JH1) | 11.1 | 4 | 3 | 83.7 | 12 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan 2014 |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 79.4 | 63.6 | 53.4 | 53.8 | 50.1 | 52.2 |
| 2 | 84.2 | 60.9 | 76.6 | 78.1 | 45.9 | 52.2 |
| 3 | 84.5 | 55.9 | 79.9 | 81.4 | 36.8 | 43.9 |
| 4 | 84.3 | 62.4 | 70.3 | 71.6 | 44.1 | 50.6 |
| 5 | 84.3 | 55.0 | 80.6 | 82.1 | 35.4 | 42.8 |
| 6 | 84.4 | 67.3 | 64.6 | 65.5 | 52.6 | 58.0 |
| 7 | 84.3 | 68.4 | 56.6 | 56.8 | 52.3 | 57.3 |
| 8 | 84.3 | 61.3 | 64.7 | 65.4 | 39.1 | 45.7 |
| 9 | 84.3 | 61.1 | 66.4 | 67.1 | 39.8 | 46.5 |
| 10 | 84.2 | 67.3 | 58.6 | 58.6 | 50.4 | 55.3 |
| 11 | 84.3 | 68.7 | 59.3 | 59.5 | 53.7 | 58.3 |
| 12 | 84.6 | 69.3 | 56.7 | 56.7 | 54.2 | 58.6 |
| 13 | 84.7 | 72.1 | 44.7 | 44.5 | 56.1 | 59.9 |
| 14 | 84.5 | 72.0 | 48.1 | 47.9 | 58.2 | 61.7 |
| 15 | 84.5 | 71.4 | 46.0 | 45.6 | 56.3 | 59.8 |

pLDDT 78.6–85.6; JH2–JH1 29.4–53.4 Å; FERM–JH1 40.2–95.7 Å (open references ~92 Å, closed ma-l9b1f 40 Å).
Nearest reference over all conformations: ma-l9b1f 49, ma-a1sai 21, AF2 5.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~92, closed ~40)

| seed | recycles 1–15 | final state |
|---|---|---|
| 0 | 73 73 73 71 67 73 70 69 71 67 73 75 94 96 95 | in between → **open** at recycle 13 |
| 1 | 69 72 68 94 67 92 95 94 95 95 95 95 94 93 93 | **open** from recycle 6 |
| 2 | 56 50 46 49 45 46 46 45 45 44 44 45 46 46 44 | **closed** (FERM-bound) from recycle 3 |
| 3 | 71 66 53 58 56 85 91 57 53 90 89 91 85 84 84 | switches several times, ends open-like |
| 4 | 49 42 40 41 41 40 41 41 41 40 41 41 41 42 41 | **closed**, stable from recycle 2 |

## Interpretation
- **First template-free run that produces the closed JAK1.** Seed 4 stays closed for all 15 recycles and matches
  Orianne's closed model ma-l9b1f to **2.4 Å** (recycle 4; selected structure recycle 13: 4.5 Å, FERM–JH1 40.8 Å,
  pLDDT 83.9). 15 conformations are within 15 Å of ma-l9b1f, 11 within 15 Å of the open ma-a1sai.
- **Both states from the same MSA depth.** At 128/512 the model is bistable: 2 seeds closed (2, 4), 2 open (0, 1),
  1 switching (3). The deep MSA (512/8192) gave only open; the AF2 template gave only open.
- **pLDDT does not separate the states** (closed seed 4: 83.9, open seed 1: 85.1), so the model is about equally
  confident in both — consistent with two real conformations rather than a low-confidence artefact.
- **15 recycles were needed:** seeds 0 and 3 only settle after recycle 12–13.
- **Not reproducible run-to-run:** yesterday's 8-recycle run at the same depth and seeds (JAK1_20261014_135749) went open
  in all seeds by recycle 4–8. Seeds alone do not fix the outcome (GPU non-determinism and the stochastic dropout amplify
  small differences in this bistable regime), so the fraction of closed vs open seeds is the meaningful quantity, not which seed closes.
- The selected structure of seed 2 (recycle 3) is FERM-bound but 25 Å from ma-l9b1f: JH1 binds FERM in a somewhat different
  orientation; its later recycles stay FERM-bound.
