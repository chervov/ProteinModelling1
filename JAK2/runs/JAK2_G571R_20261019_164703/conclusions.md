# JAK2_G571R_20261019_164703 — JAK3 G571R_msa512-8192_s8-15

JAK2 G571R, seeds 8-15, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. CADD 33.0 (joint highest of the seven, equal to V617F) and REVEL 0.874, but 51 percent solvent-exposed in JAK2 own closed structure with 0.0 A^2 interface burial. The neighbouring G571S is reported in a single erythrocytosis case with no functional data. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 512 clusters / 8192 extra; no template. Run time 113 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 8 | 8 | 86.4 | 46.3 | 95.2 | 1.3 | 83.4 | AF2 |
| 9 | 13 | 86.5 | 46.3 | 95.1 | 1.2 | 83.4 | AF2 |
| 10 | 8 | 86.5 | 46.5 | 95.2 | 1.8 | 83.7 | AF2 |
| 11 | 8 | 86.5 | 46.2 | 94.8 | 1.6 | 83.1 | AF2 |
| 12 | 9 | 86.4 | 46.3 | 94.9 | 1.2 | 83.5 | AF2 |
| 13 | 8 | 86.4 | 46.3 | 94.9 | 1.4 | 83.3 | AF2 |
| 14 | 9 | 86.6 | 46.3 | 95.0 | 0.9 | 83.6 | AF2 |
| 15 | 8 | 86.5 | 46.4 | 95.1 | 1.3 | 83.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.7 | 8 | 5 | 86.2 | 117 |
| Shan 2014 (closed, JH2–JH1) | 52.4 | 8 | 1 | 83.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.6 | 90.3 | 19.2 | 81.3 |
| 2 | 85.8 | 95.0 | 1.7 | 83.5 |
| 3 | 86.1 | 95.0 | 1.6 | 83.2 |
| 4 | 86.2 | 94.9 | 1.3 | 83.4 |
| 5 | 86.2 | 94.9 | 1.3 | 83.4 |
| 6 | 86.1 | 95.0 | 1.5 | 83.4 |
| 7 | 86.3 | 94.9 | 1.4 | 83.4 |
| 8 | 86.4 | 95.0 | 1.6 | 83.3 |
| 9 | 86.3 | 95.0 | 1.3 | 83.4 |
| 10 | 86.2 | 95.1 | 1.6 | 83.5 |
| 11 | 86.2 | 95.1 | 1.5 | 83.4 |
| 12 | 86.3 | 95.0 | 1.8 | 83.2 |
| 13 | 86.4 | 95.1 | 1.6 | 83.4 |
| 14 | 86.3 | 95.0 | 1.6 | 83.4 |
| 15 | 86.3 | 95.1 | 1.4 | 83.5 |

pLDDT 83.2–86.6; JH2–JH1 45.8–48.4 Å; FERM–JH1 63.8–95.4 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 119, Shan 2014 1.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 64 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 9 | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 10 | 92 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 11 | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 12 | 94 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 13 | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 14 | 94 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 15 | 93 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
