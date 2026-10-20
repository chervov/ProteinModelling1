# TYK2_V678W_20261020_224623 — TYK2 V678W_free_msa64-256_s8-15

TYK2 V678W at 64/256, seeds 8-15. Part of the V678 substitution series testing the deep mutational scan's volume trend at this position. Measured IFN-alpha effect (1 U/mL) for V678W is +0.227. largest side chain tested; activating in the DMS but also the most destabilising (abundance -0.361); separates size from fold integrity. 64/256 is the only TYK2 depth with dynamic range - wild type is 8/24 compact there, and 100 percent open at every deeper setting - so this is the only depth where any of these can separate.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 8,9,10,11,12,13,14,15; MSA 64 clusters / 256 extra; no template. Run time 64 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 5 | 80.8 | 54.3 | 93.1 | 97.1 | AF2 |
| 9 | 8 | 80.5 | 53.0 | 94.7 | 95.0 | AF2 |
| 10 | 12 | 80.5 | 52.5 | 85.7 | 91.3 | AF2 |
| 11 | 15 | 80.8 | 51.4 | 96.1 | 91.8 | AF2 |
| 12 | 5 | 80.0 | 52.4 | 95.3 | 94.2 | AF2 |
| 13 | 4 | 80.7 | 54.0 | 89.6 | 96.7 | AF2 |
| 14 | 12 | 80.5 | 51.0 | 94.3 | 92.4 | AF2 |
| 15 | 15 | 81.0 | 50.3 | 95.5 | 89.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 37.6 | 15 | 2 | 77.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 66.3 | 42.6 | 55.1 |
| 2 | 76.9 | 53.7 | 66.2 |
| 3 | 79.8 | 74.7 | 86.6 |
| 4 | 80.4 | 80.0 | 89.1 |
| 5 | 80.5 | 90.4 | 94.0 |
| 6 | 80.3 | 93.8 | 91.4 |
| 7 | 80.2 | 90.2 | 92.9 |
| 8 | 80.4 | 90.3 | 92.2 |
| 9 | 80.2 | 90.1 | 91.5 |
| 10 | 80.3 | 89.6 | 88.9 |
| 11 | 80.2 | 91.4 | 90.4 |
| 12 | 80.5 | 93.7 | 90.2 |
| 13 | 80.3 | 94.6 | 90.8 |
| 14 | 80.2 | 94.6 | 89.8 |
| 15 | 80.5 | 95.1 | 90.9 |

pLDDT 65.3–81.0; JH2–JH1 41.0–66.1 Å; FERM–JH1 25.0–96.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 46 73 83 88 93 96 94 95 96 96 96 96 96 95 96 | open-like (> 80) |
| 9 | 28 63 86 87 93 95 94 95 95 95 94 95 94 95 95 | open-like (> 80) |
| 10 | 25 46 52 55 78 89 69 70 69 60 72 86 96 96 95 | open-like (> 80) |
| 11 | 35 52 80 90 96 96 95 95 95 96 96 96 95 95 96 | open-like (> 80) |
| 12 | 58 50 86 92 95 95 95 96 96 95 95 95 96 95 96 | open-like (> 80) |
| 13 | 58 58 87 90 92 94 90 90 90 89 90 93 91 92 91 | open-like (> 80) |
| 14 | 44 48 75 83 90 92 90 88 88 91 92 94 95 95 96 | open-like (> 80) |
| 15 | 47 39 48 54 86 95 94 94 92 95 95 95 94 94 96 | open-like (> 80) |
