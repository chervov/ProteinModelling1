# TYK2_20261019_101530 — TYK2 WT_free_msa96-384_s0-7

TYK2 wild type, no template, 8 seeds. Depth scan to find where the closed arrangement appears. At 128/512 TYK2 is uniformly OPEN (run TYK2_20261016_175018: all 8 seeds FERM-JH1 93.2-93.8 A, 82 A from the AF2 closed-like reference, spread of only 0.6 A), so that depth is a ceiling and no opening mutation could show an effect there. TYK2 therefore needs a SHALLOWER MSA than JAK3, which is bistable at 128/512. This is one step shallower.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 96 clusters / 384 extra; no template. Run time 84 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 5 | 81.4 | 46.9 | 93.4 | 82.6 | AF2 |
| 1 | 4 | 80.8 | 49.8 | 89.8 | 90.6 | AF2 |
| 2 | 11 | 80.8 | 46.9 | 93.6 | 82.4 | AF2 |
| 3 | 7 | 81.3 | 46.7 | 93.8 | 82.5 | AF2 |
| 4 | 13 | 81.1 | 46.7 | 93.5 | 82.5 | AF2 |
| 5 | 13 | 81.0 | 46.7 | 93.4 | 81.8 | AF2 |
| 6 | 12 | 81.3 | 46.8 | 93.8 | 82.5 | AF2 |
| 7 | 15 | 80.7 | 47.0 | 93.6 | 82.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 25.6 | 1 | 2 | 77.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 71.6 | 31.0 | 38.1 |
| 2 | 77.4 | 29.6 | 36.7 |
| 3 | 80.2 | 84.3 | 80.2 |
| 4 | 80.8 | 93.4 | 85.1 |
| 5 | 80.9 | 93.8 | 83.8 |
| 6 | 80.8 | 94.0 | 83.5 |
| 7 | 80.8 | 93.9 | 83.4 |
| 8 | 80.8 | 93.6 | 83.3 |
| 9 | 80.7 | 93.6 | 83.4 |
| 10 | 80.7 | 93.5 | 83.2 |
| 11 | 80.8 | 93.8 | 83.7 |
| 12 | 80.9 | 93.6 | 83.4 |
| 13 | 80.9 | 93.8 | 82.7 |
| 14 | 80.8 | 93.5 | 83.3 |
| 15 | 80.8 | 93.7 | 83.3 |

pLDDT 70.8–81.4; JH2–JH1 38.3–59.6 Å; FERM–JH1 7.0–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 43 36 94 93 93 94 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 1 | 25 28 53 90 95 95 95 94 94 94 94 95 94 94 94 | open-like (> 80) |
| 2 | 13 20 93 94 94 94 94 93 93 93 94 93 94 94 94 | open-like (> 80) |
| 3 | 20 37 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 4 | 47 7 94 94 94 94 94 94 93 93 94 93 94 93 94 | open-like (> 80) |
| 5 | 35 38 94 93 94 94 94 93 93 93 94 93 93 93 93 | open-like (> 80) |
| 6 | 32 35 89 95 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 7 | 33 35 65 95 94 95 94 94 94 94 94 94 94 93 94 | open-like (> 80) |
