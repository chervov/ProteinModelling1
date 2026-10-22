# TYK2_20261022_004536 — TYK2 WT_free_msa256-1024_s0-7__seed7

TYK2 wild type, template-free, MSA 256/1024, seeds 0-7. fills the one remaining hole in the TYK2 depth ladder, between 128/512 (collapsed open, spread 0.6 A) and 64/256 (the only bimodal depth, spread 60.5 A). Knowing where the transition starts matters because every TYK2 mutation result rests on 64/256 being the sole depth with dynamic range. Prediction stated in advance: open, near 93 A.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 7; MSA 256 clusters / 1024 extra; no template. Run time 13 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 7 | 13 | 82.6 | 46.6 | 91.7 | 81.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.7 | 7 | 14 | 82.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 79.3 | 92.9 | 84.9 |
| 2 | 81.8 | 92.0 | 82.3 |
| 3 | 82.2 | 91.8 | 82.1 |
| 4 | 82.2 | 91.9 | 82.1 |
| 5 | 82.2 | 91.6 | 81.9 |
| 6 | 82.2 | 91.8 | 82.1 |
| 7 | 82.3 | 91.8 | 82.2 |
| 8 | 82.4 | 91.6 | 82.1 |
| 9 | 82.2 | 91.9 | 82.0 |
| 10 | 82.2 | 91.9 | 82.0 |
| 11 | 82.3 | 92.1 | 82.0 |
| 12 | 82.2 | 91.8 | 81.7 |
| 13 | 82.6 | 91.7 | 81.9 |
| 14 | 82.1 | 91.5 | 81.7 |
| 15 | 82.4 | 91.6 | 82.2 |

pLDDT 79.3–82.6; JH2–JH1 46.4–47.8 Å; FERM–JH1 91.5–92.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 7 | 93 92 92 92 92 92 92 92 92 92 92 92 92 92 92 | open-like (> 80) |
