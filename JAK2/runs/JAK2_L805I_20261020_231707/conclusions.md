# JAK2_L805I_20261020_231707 — JAK3 L805I_msa512-8192_s8-15

JAK2 L805I, seeds 8-15, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. installs the residue JAK1 already carries at the equivalent position (I845); 1 percent exposed, 0.0 A^2 interface burial; SIFT calls it tolerated. The second control. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 512 clusters / 8192 extra; no template. Run time 112 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 8 | 9 | 85.1 | 41.8 | 48.6 | 83.3 | 11.0 | Shan 2014 |
| 9 | 8 | 85.2 | 45.2 | 51.0 | 85.9 | 19.0 | Shan 2014 |
| 10 | 8 | 86.4 | 46.2 | 94.8 | 1.1 | 83.3 | AF2 |
| 11 | 8 | 86.4 | 46.3 | 94.9 | 1.5 | 83.3 | AF2 |
| 12 | 9 | 86.2 | 46.4 | 94.9 | 1.4 | 83.4 | AF2 |
| 13 | 14 | 86.5 | 46.2 | 94.7 | 0.9 | 83.5 | AF2 |
| 14 | 9 | 86.4 | 46.4 | 95.0 | 1.1 | 83.5 | AF2 |
| 15 | 8 | 85.1 | 41.6 | 47.5 | 83.6 | 11.2 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.7 | 13 | 10 | 86.3 | 65 |
| Shan 2014 (closed, JH2–JH1) | 8.6 | 15 | 11 | 85.0 | 24 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.3 | 64.1 | 77.5 | 47.8 |
| 2 | 84.9 | 64.2 | 68.4 | 45.0 |
| 3 | 85.4 | 78.4 | 36.4 | 59.3 |
| 4 | 85.5 | 77.9 | 32.7 | 58.4 |
| 5 | 85.7 | 78.2 | 32.4 | 58.0 |
| 6 | 85.7 | 77.9 | 32.9 | 57.8 |
| 7 | 85.8 | 77.8 | 32.8 | 57.7 |
| 8 | 85.9 | 77.8 | 32.4 | 57.3 |
| 9 | 85.8 | 77.3 | 32.1 | 56.5 |
| 10 | 85.7 | 77.2 | 32.3 | 56.6 |
| 11 | 85.7 | 77.2 | 32.5 | 57.0 |
| 12 | 85.7 | 77.1 | 32.5 | 56.5 |
| 13 | 85.8 | 77.0 | 32.6 | 56.7 |
| 14 | 85.7 | 76.9 | 32.4 | 56.6 |
| 15 | 85.8 | 77.2 | 32.4 | 56.8 |

pLDDT 83.2–86.5; JH2–JH1 40.2–52.0 Å; FERM–JH1 45.8–96.1 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 68, Shan 2014 52.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 57 50 50 49 49 49 49 49 49 47 47 47 47 47 46 | closed-like (< 50) |
| 9 | 60 51 52 51 52 52 52 51 48 49 49 48 48 48 49 | closed-like (< 50) |
| 10 | 65 61 96 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 11 | 59 57 93 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 12 | 60 54 96 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 13 | 92 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 14 | 64 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 15 | 56 50 50 50 50 48 47 48 46 46 46 46 46 46 46 | closed-like (< 50) |
