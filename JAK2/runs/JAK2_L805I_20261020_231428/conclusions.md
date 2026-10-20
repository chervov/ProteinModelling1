# JAK2_L805I_20261020_231428 — JAK3 L805I_msa512-8192_s0-7

JAK2 L805I, seeds 0-7, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. installs the residue JAK1 already carries at the equivalent position (I845); 1 percent exposed, 0.0 A^2 interface burial; SIFT calls it tolerated. The second control. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 512 clusters / 8192 extra; no template. Run time 118 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 7 | 86.6 | 46.2 | 94.7 | 1.3 | 83.2 | AF2 |
| 1 | 10 | 86.4 | 46.5 | 94.9 | 1.1 | 83.6 | AF2 |
| 2 | 14 | 86.4 | 46.2 | 94.8 | 1.2 | 83.3 | AF2 |
| 3 | 11 | 85.1 | 44.9 | 49.7 | 86.2 | 18.3 | Shan 2014 |
| 4 | 14 | 86.5 | 46.3 | 95.0 | 1.2 | 83.5 | AF2 |
| 5 | 15 | 86.3 | 46.3 | 94.9 | 1.2 | 83.5 | AF2 |
| 6 | 15 | 86.3 | 46.3 | 94.9 | 1.6 | 83.5 | AF2 |
| 7 | 10 | 86.3 | 46.3 | 94.8 | 1.2 | 83.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.6 | 1 | 7 | 86.3 | 100 |
| Shan 2014 (closed, JH2–JH1) | 17.3 | 3 | 15 | 84.8 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.1 | 73.6 | 54.3 | 59.5 |
| 2 | 85.6 | 89.0 | 15.1 | 76.6 |
| 3 | 86.0 | 88.8 | 12.5 | 75.5 |
| 4 | 86.0 | 89.0 | 12.1 | 75.7 |
| 5 | 86.1 | 88.9 | 12.4 | 75.9 |
| 6 | 86.1 | 89.2 | 12.0 | 75.4 |
| 7 | 86.1 | 89.2 | 12.1 | 75.3 |
| 8 | 86.0 | 89.5 | 12.1 | 75.6 |
| 9 | 86.1 | 89.5 | 12.0 | 75.3 |
| 10 | 86.1 | 89.3 | 12.0 | 75.6 |
| 11 | 86.1 | 89.3 | 12.1 | 75.2 |
| 12 | 86.0 | 89.3 | 12.2 | 75.1 |
| 13 | 86.1 | 89.3 | 12.1 | 75.4 |
| 14 | 86.1 | 89.1 | 12.1 | 75.4 |
| 15 | 86.1 | 89.1 | 12.2 | 75.1 |

pLDDT 82.8–86.6; JH2–JH1 44.0–49.9 Å; FERM–JH1 47.8–96.0 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 101, Shan 2014 19.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 92 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 1 | 66 95 95 95 95 94 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 2 | 64 95 94 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 3 | 53 48 48 49 48 50 50 51 51 50 50 49 50 49 48 | closed-like (< 50) |
| 4 | 93 94 94 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 5 | 94 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 6 | 65 96 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 7 | 62 94 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
