# JAK2_V1110E_20261020_105626 — JAK3 V1110E_msa512-8192_s0-7

JAK2 V1110E, seeds 0-7, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. PolyPhen-2 calls it benign (0.18) and ESM1b is nearly neutral (-1.22); 30 percent exposed in JH1, 0.0 A^2 interface burial. An earlier prediction that it buries a charge was withdrawn after measuring it in JAK2 own structure. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 512 clusters / 8192 extra; no template. Run time 112 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 14 | 86.3 | 46.4 | 95.2 | 0.9 | 83.7 | AF2 |
| 1 | 10 | 86.5 | 46.4 | 95.1 | 2.1 | 83.2 | AF2 |
| 2 | 14 | 86.5 | 46.3 | 94.9 | 1.1 | 83.5 | AF2 |
| 3 | 8 | 84.9 | 44.2 | 50.2 | 84.9 | 15.2 | Shan 2014 |
| 4 | 14 | 86.6 | 46.4 | 95.0 | 2.2 | 83.1 | AF2 |
| 5 | 14 | 86.4 | 46.5 | 95.1 | 1.5 | 83.6 | AF2 |
| 6 | 14 | 86.3 | 46.3 | 95.0 | 1.9 | 83.1 | AF2 |
| 7 | 10 | 86.3 | 46.3 | 94.9 | 1.2 | 83.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.5 | 1 | 7 | 86.4 | 97 |
| Shan 2014 (closed, JH2–JH1) | 12.0 | 3 | 3 | 84.7 | 7 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.4 | 74.1 | 59.7 | 65.2 |
| 2 | 85.4 | 84.1 | 24.3 | 69.1 |
| 3 | 85.8 | 89.1 | 11.9 | 74.3 |
| 4 | 85.9 | 89.1 | 11.4 | 74.5 |
| 5 | 86.1 | 89.3 | 11.5 | 74.6 |
| 6 | 86.0 | 89.3 | 11.7 | 74.9 |
| 7 | 86.0 | 89.3 | 11.6 | 74.7 |
| 8 | 86.1 | 89.4 | 12.1 | 74.8 |
| 9 | 86.0 | 89.3 | 12.0 | 75.0 |
| 10 | 86.1 | 89.2 | 12.0 | 75.0 |
| 11 | 86.1 | 89.2 | 11.9 | 74.8 |
| 12 | 86.0 | 89.3 | 11.9 | 74.9 |
| 13 | 85.9 | 89.3 | 11.9 | 75.3 |
| 14 | 86.2 | 89.3 | 12.0 | 74.9 |
| 15 | 86.2 | 89.2 | 12.1 | 74.7 |

pLDDT 82.9–86.6; JH2–JH1 42.6–51.3 Å; FERM–JH1 48.8–95.6 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 101, Shan 2014 19.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 90 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 1 | 76 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 2 | 63 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 3 | 61 51 49 50 51 50 50 50 50 49 49 49 50 49 49 | closed-like (< 50) |
| 4 | 94 94 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 5 | 85 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 6 | 65 96 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 7 | 59 51 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
