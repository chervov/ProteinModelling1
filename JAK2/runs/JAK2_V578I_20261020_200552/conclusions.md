# JAK2_V578I_20261020_200552 — JAK3 V578I_msa512-8192_s8-15

JAK2 V578I, seeds 8-15, MSA 512/8192 - the depth where JAK2 wild type is most balanced (7 closed / 7 open / 2 FERM-bound of 16), so a mutation can shift it either way. conservative substitution, fully buried in the JH2 core (0 percent exposed), 0.0 A^2 interface burial - expected near-neutral and included as a control. Note that the interface-burial ranking has since failed as a predictor: JAK3 Y581C and TYK2 V678F both bury 0.0 A^2 yet give the two strongest effects in the project, while the only true interface residue (TYK2 P982A) shows none.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 512 clusters / 8192 extra; no template. Run time 6 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 8 | 3 | 85.0 | 44.8 | 51.5 | 85.2 | 17.3 | Shan 2014 |
| 9 | 14 | 86.5 | 46.2 | 94.9 | 1.0 | 83.4 | AF2 |
| 10 | 10 | 85.1 | 46.9 | 49.7 | 88.7 | 24.1 | Shan 2014 |
| 11 | 8 | 85.1 | 47.1 | 51.6 | 88.1 | 22.7 | Shan 2014 |
| 12 | 3 | 85.0 | 45.6 | 49.3 | 87.5 | 16.9 | Shan 2014 |
| 13 | 13 | 86.2 | 46.4 | 95.1 | 2.0 | 83.3 | AF2 |
| 14 | 2 | 84.8 | 46.7 | 49.5 | 88.1 | 22.5 | Shan 2014 |
| 15 | 12 | 85.0 | 40.3 | 46.6 | 82.4 | 8.7 | Shan 2014 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.6 | 9 | 6 | 86.2 | 28 |
| Shan 2014 (closed, JH2–JH1) | 7.2 | 15 | 13 | 84.9 | 20 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.3 | 66.5 | 74.6 | 42.3 |
| 2 | 85.0 | 57.1 | 77.4 | 33.2 |
| 3 | 85.1 | 61.4 | 65.6 | 34.8 |
| 4 | 85.0 | 61.2 | 64.8 | 35.2 |
| 5 | 85.1 | 61.0 | 65.2 | 35.1 |
| 6 | 85.1 | 61.3 | 64.9 | 35.5 |
| 7 | 85.1 | 60.9 | 65.0 | 35.4 |
| 8 | 85.2 | 60.8 | 65.0 | 34.3 |
| 9 | 85.2 | 60.6 | 65.0 | 34.1 |
| 10 | 85.2 | 60.9 | 65.1 | 35.1 |
| 11 | 85.3 | 60.5 | 65.0 | 34.2 |
| 12 | 85.2 | 60.3 | 65.0 | 33.9 |
| 13 | 85.3 | 60.0 | 65.2 | 33.6 |
| 14 | 85.2 | 60.3 | 65.0 | 34.1 |
| 15 | 85.1 | 60.4 | 65.2 | 34.1 |

pLDDT 82.9–86.5; JH2–JH1 39.6–50.4 Å; FERM–JH1 46.3–95.2 Å (open = AF2 JAK3; closed reference: JAK1 ma-l9b1f mapped (see JAK3 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 92, AF2 28.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 58 52 52 48 48 49 48 48 48 49 49 49 48 48 48 | closed-like (< 50) |
| 9 | 93 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 10 | 68 51 50 50 49 50 49 51 50 50 48 48 47 48 48 | closed-like (< 50) |
| 11 | 64 58 51 52 51 52 54 52 50 51 50 51 50 50 51 | in between |
| 12 | 67 50 49 49 48 49 48 48 49 50 48 48 48 48 49 | closed-like (< 50) |
| 13 | 63 50 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 14 | 61 50 50 50 50 51 50 49 50 51 51 50 50 50 50 | in between |
| 15 | 59 51 51 50 52 50 49 49 47 47 47 47 46 47 47 | closed-like (< 50) |
