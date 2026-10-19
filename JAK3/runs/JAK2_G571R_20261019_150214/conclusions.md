# JAK2_G571R_20261019_150214 — JAK3 G571R_msa512-8192_s0-7

JAK2 G571R, seeds 0-7, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. CADD 33.0 (joint highest of the seven, equal to V617F) and REVEL 0.874, but 51 percent solvent-exposed in JAK2 own closed structure with 0.0 A^2 interface burial. The neighbouring G571S is reported in a single erythrocytosis case with no functional data. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 512 clusters / 8192 extra; no template. Run time 105 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 12 | 86.1 | 46.3 | 95.0 | 1.5 | 83.3 | AF2 |
| 1 | 10 | 86.4 | 46.5 | 95.3 | 2.4 | 83.3 | AF2 |
| 2 | 14 | 85.3 | 46.3 | 50.5 | 87.4 | 25.3 | Shan 2014 |
| 3 | 7 | 85.0 | 44.4 | 52.1 | 84.5 | 15.5 | Shan 2014 |
| 4 | 6 | 86.3 | 46.4 | 95.0 | 1.8 | 83.4 | AF2 |
| 5 | 10 | 86.3 | 46.4 | 95.1 | 2.8 | 83.2 | AF2 |
| 6 | 15 | 85.0 | 45.8 | 49.8 | 87.6 | 19.6 | Shan 2014 |
| 7 | 15 | 85.2 | 46.9 | 48.2 | 89.1 | 23.6 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.8 | 5 | 5 | 86.0 | 48 |
| Shan 2014 (closed, JH2–JH1) | 13.1 | 3 | 9 | 84.9 | 5 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.6 | 67.2 | 73.3 | 48.5 |
| 2 | 85.1 | 68.2 | 58.0 | 49.4 |
| 3 | 85.2 | 67.4 | 55.4 | 44.8 |
| 4 | 85.3 | 66.8 | 54.8 | 43.7 |
| 5 | 85.3 | 67.6 | 54.5 | 45.4 |
| 6 | 85.4 | 67.4 | 54.9 | 46.7 |
| 7 | 85.4 | 67.4 | 55.2 | 44.8 |
| 8 | 85.4 | 66.9 | 55.0 | 44.3 |
| 9 | 85.4 | 72.2 | 44.9 | 51.6 |
| 10 | 85.6 | 72.1 | 44.8 | 51.9 |
| 11 | 85.5 | 72.5 | 44.3 | 51.8 |
| 12 | 85.5 | 72.2 | 44.7 | 52.2 |
| 13 | 85.5 | 72.4 | 44.4 | 51.8 |
| 14 | 85.6 | 72.6 | 44.2 | 52.3 |
| 15 | 85.6 | 72.1 | 44.3 | 51.6 |

pLDDT 83.3–86.4; JH2–JH1 42.7–51.1 Å; FERM–JH1 48.2–95.3 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 70, AF2 50.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 72 55 51 51 51 52 52 52 95 95 95 95 95 95 95 | open-like (> 80) |
| 1 | 72 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 2 | 57 52 51 50 54 53 50 49 49 48 51 50 50 50 49 | closed-like (< 50) |
| 3 | 57 50 50 50 51 50 52 50 49 49 50 50 50 50 49 | closed-like (< 50) |
| 4 | 66 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 5 | 93 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 6 | 61 52 52 50 50 50 51 49 50 50 50 50 50 51 50 | in between |
| 7 | 60 51 51 50 49 50 50 50 50 49 49 48 49 49 48 | closed-like (< 50) |
