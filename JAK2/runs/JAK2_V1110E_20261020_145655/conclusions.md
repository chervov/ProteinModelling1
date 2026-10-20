# JAK2_V1110E_20261020_145655 — JAK3 V1110E_msa512-8192_s8-15

JAK2 V1110E, seeds 8-15, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. PolyPhen-2 calls it benign (0.18) and ESM1b is nearly neutral (-1.22); 30 percent exposed in JH1, 0.0 A^2 interface burial. An earlier prediction that it buries a charge was withdrawn after measuring it in JAK2 own structure. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 512 clusters / 8192 extra; no template. Run time 121 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 8 | 3 | 85.1 | 42.0 | 49.0 | 83.1 | 11.3 | Shan 2014 |
| 9 | 3 | 85.1 | 43.0 | 50.0 | 83.7 | 13.3 | Shan 2014 |
| 10 | 3 | 85.0 | 43.1 | 49.1 | 84.3 | 12.8 | Shan 2014 |
| 11 | 12 | 86.4 | 46.4 | 95.2 | 1.2 | 83.7 | AF2 |
| 12 | 3 | 85.3 | 45.1 | 50.8 | 85.5 | 18.2 | Shan 2014 |
| 13 | 3 | 85.2 | 44.2 | 49.5 | 85.2 | 15.9 | Shan 2014 |
| 14 | 9 | 86.4 | 46.3 | 94.9 | 0.9 | 83.6 | AF2 |
| 15 | 12 | 85.1 | 39.6 | 45.6 | 82.0 | 7.6 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.5 | 11 | 3 | 86.0 | 26 |
| Shan 2014 (closed, JH2–JH1) | 7.4 | 15 | 11 | 85.0 | 70 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.3 | 57.4 | 86.7 | 36.4 |
| 2 | 84.8 | 55.6 | 76.8 | 28.9 |
| 3 | 85.2 | 55.4 | 73.8 | 23.1 |
| 4 | 84.9 | 59.6 | 63.3 | 30.5 |
| 5 | 85.2 | 60.0 | 63.2 | 30.3 |
| 6 | 85.0 | 59.5 | 63.2 | 29.8 |
| 7 | 85.2 | 59.4 | 63.2 | 29.7 |
| 8 | 85.3 | 59.2 | 62.8 | 29.2 |
| 9 | 85.3 | 59.8 | 62.9 | 29.9 |
| 10 | 85.2 | 59.3 | 62.8 | 29.1 |
| 11 | 85.3 | 59.8 | 62.8 | 29.7 |
| 12 | 85.3 | 59.5 | 63.1 | 29.7 |
| 13 | 85.3 | 59.8 | 63.1 | 29.8 |
| 14 | 85.3 | 59.4 | 63.1 | 29.9 |
| 15 | 85.2 | 59.5 | 63.2 | 29.9 |

pLDDT 82.9–86.4; JH2–JH1 39.4–51.4 Å; FERM–JH1 45.1–95.5 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 94, AF2 26.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 54 49 49 47 48 47 47 47 47 47 48 47 48 47 47 | closed-like (< 50) |
| 9 | 56 49 50 48 49 48 48 47 48 48 48 48 48 48 48 | closed-like (< 50) |
| 10 | 56 50 49 48 48 48 48 48 48 47 48 48 48 48 47 | closed-like (< 50) |
| 11 | 59 95 95 95 95 95 95 95 95 96 95 95 95 95 95 | open-like (> 80) |
| 12 | 57 51 51 49 49 49 48 49 50 49 49 49 50 49 49 | closed-like (< 50) |
| 13 | 60 49 50 49 49 48 48 48 48 48 49 49 49 49 48 | closed-like (< 50) |
| 14 | 63 53 52 94 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 15 | 54 49 48 46 47 46 46 46 46 45 46 46 45 45 46 | closed-like (< 50) |
