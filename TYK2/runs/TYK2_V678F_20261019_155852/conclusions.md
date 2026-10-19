# TYK2_V678F_20261019_155852 — TYK2 V678F_free_msa96-384_s0-7

TYK2 V678F at MSA 96/384, pairing with wild type at the same depth. Tests whether the strong V678F effect seen at 64/256 is depth-dependent.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 96 clusters / 384 extra; no template. Run time 79 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 15 | 81.1 | 46.6 | 93.3 | 82.0 | AF2 |
| 1 | 15 | 81.2 | 46.6 | 93.6 | 81.9 | AF2 |
| 2 | 15 | 81.2 | 46.6 | 93.0 | 82.0 | AF2 |
| 3 | 12 | 81.1 | 46.7 | 93.1 | 82.3 | AF2 |
| 4 | 12 | 81.0 | 46.7 | 92.8 | 82.4 | AF2 |
| 5 | 13 | 81.1 | 46.8 | 93.6 | 82.3 | AF2 |
| 6 | 10 | 81.3 | 46.6 | 93.3 | 81.9 | AF2 |
| 7 | 12 | 80.8 | 46.7 | 93.4 | 81.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 24.4 | 4 | 2 | 76.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 72.7 | 34.7 | 63.5 |
| 2 | 77.5 | 63.3 | 58.0 |
| 3 | 80.5 | 92.9 | 82.5 |
| 4 | 80.9 | 92.9 | 82.2 |
| 5 | 80.6 | 93.1 | 82.2 |
| 6 | 81.0 | 93.1 | 82.1 |
| 7 | 80.8 | 93.2 | 82.0 |
| 8 | 80.5 | 93.3 | 82.0 |
| 9 | 80.8 | 93.2 | 82.1 |
| 10 | 80.9 | 93.2 | 82.0 |
| 11 | 80.7 | 93.3 | 82.0 |
| 12 | 81.0 | 93.2 | 82.1 |
| 13 | 81.0 | 93.3 | 82.0 |
| 14 | 80.8 | 93.1 | 82.0 |
| 15 | 81.0 | 93.2 | 82.1 |

pLDDT 71.2–81.3; JH2–JH1 34.5–63.0 Å; FERM–JH1 17.5–93.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 42 61 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 1 | 48 68 93 93 93 93 93 93 93 93 94 93 93 93 94 | open-like (> 80) |
| 2 | 29 76 92 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 3 | 18 76 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 4 | 47 28 94 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 5 | 33 69 92 93 93 93 93 93 93 93 93 93 94 93 93 | open-like (> 80) |
| 6 | 35 62 93 93 94 94 94 94 94 93 94 94 94 93 94 | open-like (> 80) |
| 7 | 27 66 93 93 93 93 93 94 94 93 93 93 93 93 93 | open-like (> 80) |
