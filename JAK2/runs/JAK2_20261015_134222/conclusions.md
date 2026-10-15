# JAK2_20261015_134222 — JAK2 experiment F_notemplate_msa128-512_15seeds

JAK2 without any template at the MSA depth where JAK1 is bistable (128/512; JAK1: 6 of 15 seeds end next to FERM, 2 in the closed reference arrangement). Does JAK2 close on its own? 15 seeds. Part of the JAK2 no-template MSA scan (other depths run on Colab).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14; MSA 128 clusters / 512 extra; no template. Run time 118 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 7 | 84.7 | 50.5 | 52.1 | 90.8 | 29.3 | Shan 2014 |
| 1 | 10 | 84.6 | 53.7 | 59.8 | 88.1 | 54.5 | Shan 2014 |
| 2 | 5 | 85.0 | 50.5 | 61.6 | 78.7 | 88.7 | AF2 |
| 3 | 14 | 85.0 | 58.2 | 69.4 | 79.6 | 97.5 | AF2 |
| 4 | 15 | 85.0 | 53.6 | 59.2 | 83.8 | 90.0 | AF2 |
| 5 | 10 | 85.1 | 46.3 | 60.3 | 74.6 | 84.5 | AF2 |
| 6 | 12 | 85.5 | 46.2 | 94.5 | 0.9 | 83.5 | AF2 |
| 7 | 10 | 84.9 | 58.1 | 62.3 | 85.2 | 93.7 | AF2 |
| 8 | 10 | 84.7 | 53.9 | 57.5 | 90.6 | 48.1 | Shan 2014 |
| 9 | 14 | 85.0 | 55.8 | 61.4 | 83.2 | 92.1 | AF2 |
| 10 | 10 | 85.0 | 49.4 | 55.8 | 81.6 | 83.7 | AF2 |
| 11 | 10 | 85.2 | 49.3 | 58.2 | 79.7 | 85.8 | AF2 |
| 12 | 10 | 85.0 | 52.3 | 61.9 | 80.2 | 90.0 | AF2 |
| 13 | 5 | 85.0 | 50.6 | 56.2 | 82.5 | 85.3 | AF2 |
| 14 | 10 | 85.1 | 50.4 | 55.3 | 82.8 | 86.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.6 | 6 | 14 | 85.0 | 11 |
| Shan 2014 (closed, JH2–JH1) | 23.5 | 0 | 6 | 84.4 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 78.6 | 34.1 | 91.0 | 51.9 |
| 2 | 83.8 | 57.8 | 86.3 | 84.5 |
| 3 | 84.5 | 59.4 | 87.9 | 85.9 |
| 4 | 84.7 | 61.9 | 81.9 | 83.2 |
| 5 | 84.7 | 60.3 | 81.2 | 81.2 |
| 6 | 84.7 | 63.8 | 74.0 | 79.4 |
| 7 | 84.8 | 61.9 | 78.7 | 79.8 |
| 8 | 84.6 | 61.8 | 77.7 | 80.1 |
| 9 | 84.7 | 62.0 | 77.3 | 80.1 |
| 10 | 84.9 | 62.9 | 74.5 | 79.4 |
| 11 | 84.8 | 64.0 | 73.3 | 79.4 |
| 12 | 84.8 | 60.9 | 77.2 | 78.3 |
| 13 | 84.7 | 65.4 | 71.1 | 79.0 |
| 14 | 84.8 | 68.3 | 66.0 | 80.0 |
| 15 | 84.8 | 61.8 | 76.3 | 77.8 |

pLDDT 78.0–85.5; JH2–JH1 32.4–60.8 Å; FERM–JH1 19.4–95.5 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 164, Shan 2014 61.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 37 58 60 54 52 51 52 51 51 50 50 50 50 49 50 | in between |
| 1 | 28 40 53 56 55 58 59 62 59 60 62 65 61 62 60 | in between |
| 2 | 34 52 55 58 62 92 63 64 68 91 90 69 90 95 64 | in between |
| 3 | 37 62 63 63 61 64 65 62 64 63 61 60 62 69 72 | in between |
| 4 | 54 60 59 58 57 57 60 58 58 58 60 56 61 62 59 | in between |
| 5 | 45 64 62 65 62 64 62 65 63 60 62 59 64 80 60 | in between |
| 6 | 28 49 59 95 93 95 92 96 96 95 94 94 95 94 95 | open-like (> 80) |
| 7 | 61 66 63 63 61 63 64 64 63 62 60 59 61 66 61 | in between |
| 8 | 32 54 61 58 59 58 54 59 59 58 56 56 60 60 57 | in between |
| 9 | 27 60 60 59 56 60 62 59 60 60 59 58 60 61 61 | in between |
| 10 | 23 67 66 61 56 55 57 55 56 56 56 55 55 56 55 | in between |
| 11 | 27 66 62 62 57 57 59 58 58 58 59 58 59 61 59 | in between |
| 12 | 20 61 62 63 61 66 64 60 61 62 80 63 91 93 62 | in between |
| 13 | 40 60 55 56 56 57 58 56 57 56 57 56 58 59 56 | in between |
| 14 | 19 47 52 57 55 58 57 57 57 55 56 55 56 57 56 | in between |

## Interpretation
- **Mostly a detached-JH1 intermediate:** 10 of 15 seeds end with FERM–JH1 55–72 Å and JH2–JH1 48–57 Å, 64–100 Å from every reference (open AF2, closed JAK2, Shan, 7T6F); JH1 makes almost no contacts (0–7 pairs with JH2, none with FERM). Not the 7T6F-like arrangement seen for JAK1.
- Seeds 0, 8, 1 are partially closed (21–42 Å from the closed references, 19–30 JH1–JH2 contacts); seed 6 is open (0.7 Å from AF2).
- Details: [JAK2_intermediate.md](../../JAK2_intermediate.md).
