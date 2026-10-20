# JAK2_V578I_20261020_165924 — JAK3 V578I_msa512-8192_s0-7

JAK2 V578I, seeds 0-7, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. conservative substitution, fully buried in the JH2 core (0 percent exposed), 0.0 A^2 interface burial - expected near-neutral and included as a control. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 512 clusters / 8192 extra; no template. Run time 120 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 12 | 85.2 | 41.5 | 46.8 | 83.6 | 11.0 | Shan 2014 |
| 1 | 14 | 85.2 | 43.1 | 47.2 | 85.3 | 14.4 | Shan 2014 |
| 2 | 14 | 85.3 | 42.7 | 49.9 | 83.7 | 13.0 | Shan 2014 |
| 3 | 11 | 85.3 | 39.2 | 45.0 | 81.8 | 6.8 | Shan 2014 |
| 4 | 14 | 86.5 | 46.3 | 94.8 | 2.3 | 83.0 | AF2 |
| 5 | 11 | 85.0 | 41.5 | 47.9 | 83.4 | 10.3 | Shan 2014 |
| 6 | 14 | 84.9 | 39.8 | 46.1 | 82.1 | 7.5 | Shan 2014 |
| 7 | 15 | 85.3 | 39.2 | 44.9 | 81.8 | 7.0 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.8 | 4 | 4 | 86.2 | 14 |
| Shan 2014 (closed, JH2–JH1) | 6.4 | 3 | 13 | 85.1 | 73 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.4 | 59.7 | 82.8 | 37.2 |
| 2 | 84.9 | 57.6 | 74.7 | 29.3 |
| 3 | 85.1 | 55.3 | 74.0 | 25.0 |
| 4 | 85.0 | 53.5 | 73.9 | 21.9 |
| 5 | 85.1 | 53.4 | 73.6 | 21.3 |
| 6 | 85.0 | 53.2 | 73.3 | 20.5 |
| 7 | 85.1 | 53.2 | 73.8 | 21.2 |
| 8 | 85.1 | 53.3 | 73.5 | 20.6 |
| 9 | 85.0 | 53.1 | 73.6 | 21.4 |
| 10 | 85.2 | 53.8 | 73.8 | 21.8 |
| 11 | 85.2 | 53.0 | 73.6 | 20.7 |
| 12 | 85.2 | 52.8 | 73.3 | 20.0 |
| 13 | 85.1 | 52.7 | 72.8 | 18.8 |
| 14 | 85.3 | 52.7 | 72.8 | 18.5 |
| 15 | 85.2 | 52.4 | 72.2 | 17.6 |

pLDDT 83.0–86.5; JH2–JH1 39.0–49.8 Å; FERM–JH1 44.8–95.8 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 106, AF2 14.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 63 53 50 49 50 49 50 49 49 51 50 47 46 47 47 | closed-like (< 50) |
| 1 | 58 50 50 48 48 48 47 48 48 48 47 48 47 47 48 | closed-like (< 50) |
| 2 | 58 56 55 50 49 48 48 49 48 49 49 50 50 50 47 | closed-like (< 50) |
| 3 | 58 48 45 45 45 45 45 46 46 46 45 45 45 45 45 | closed-like (< 50) |
| 4 | 68 96 94 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 5 | 61 58 53 48 48 48 48 48 48 49 48 46 46 46 46 | closed-like (< 50) |
| 6 | 54 49 47 46 46 47 46 46 46 46 46 46 46 46 47 | closed-like (< 50) |
| 7 | 57 52 48 47 46 46 46 46 46 47 45 45 46 46 45 | closed-like (< 50) |
