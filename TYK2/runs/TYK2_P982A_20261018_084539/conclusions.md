# TYK2_P982A_20261018_084539 — TYK2 P982A_free_msa64-256_s0-7

TYK2 P982A, NO template, MSA 64/256, 8 seeds. Shallower-MSA follow-up to TYK2_P982A_20261017_181325 (128/512), where both wild type (TYK2_20261016_175018) and P982A sat entirely in the extended state (FERM–JH1 ~93 Å), so the mutation had no room to act. Paired with a wild type run at 64/256 started at the same time in a second sandbox. An earlier attempt at this pair (2026-10-17 evening) was lost when both sandboxes were terminated overnight.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time ~78 min (whole notebook incl. setup, molab).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 80.4 | 52.8 | 53.0 | 55.6 | AF2 |
| 1 | 9 | 80.7 | 47.0 | 85.5 | 87.4 | AF2 |
| 2 | 9 | 81.0 | 49.6 | 91.7 | 89.9 | AF2 |
| 3 | 13 | 81.4 | 47.0 | 85.7 | 85.6 | AF2 |
| 4 | 9 | 80.8 | 53.4 | 94.2 | 95.8 | AF2 |
| 5 | 4 | 79.9 | 48.7 | 46.0 | 37.6 | AF2 |
| 6 | 9 | 79.7 | 46.5 | 49.9 | 36.7 | AF2 |
| 7 | 15 | 80.4 | 49.1 | 89.4 | 91.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 30.8 | 3 | 2 | 74.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 68.1 | 38.6 | 58.3 |
| 2 | 75.1 | 32.6 | 44.6 |
| 3 | 79.3 | 46.1 | 43.6 |
| 4 | 80.1 | 52.8 | 50.5 |
| 5 | 80.2 | 56.2 | 54.2 |
| 6 | 80.1 | 62.6 | 60.2 |
| 7 | 79.9 | 66.5 | 62.3 |
| 8 | 79.8 | 65.1 | 62.1 |
| 9 | 80.4 | 69.5 | 66.7 |
| 10 | 80.0 | 74.5 | 71.4 |
| 11 | 80.1 | 72.3 | 68.7 |
| 12 | 80.0 | 70.8 | 70.5 |
| 13 | 80.4 | 72.4 | 69.5 |
| 14 | 80.2 | 74.0 | 72.3 |
| 15 | 80.4 | 74.0 | 71.9 |

pLDDT 66.9–81.4; JH2–JH1 38.3–62.4 Å; FERM–JH1 13.7–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 58 15 47 53 53 52 52 51 52 54 51 50 51 52 52 | intermediate |
| 1 | 24 18 42 45 50 75 86 86 85 87 87 85 86 86 86 | open-like (> 80) |
| 2 | 29 27 48 54 59 79 93 91 92 94 94 91 93 93 93 | open-like (> 80) |
| 3 | 48 32 47 49 50 52 53 53 75 87 87 86 86 86 87 | open-like (> 80) |
| 4 | 58 14 52 79 91 94 95 95 94 94 94 92 94 92 93 | open-like (> 80) |
| 5 | 41 66 45 46 45 46 45 45 47 45 45 44 45 46 44 | closed-like (< 50) |
| 6 | 24 45 49 51 52 52 51 47 50 49 49 50 49 49 46 | closed-like (< 50) |
| 7 | 27 45 38 46 49 51 57 54 62 87 72 68 75 87 89 | open-like (> 80) |
