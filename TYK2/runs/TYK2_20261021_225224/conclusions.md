# TYK2_20261021_225224 — TYK2 WT_free_msa256-1024_s0-7__seed1

TYK2 wild type, template-free, MSA 256/1024, seeds 0-7. fills the one remaining hole in the TYK2 depth ladder, between 128/512 (collapsed open, spread 0.6 A) and 64/256 (the only bimodal depth, spread 60.5 A). Knowing where the transition starts matters because every TYK2 mutation result rests on 64/256 being the sole depth with dynamic range. Prediction stated in advance: open, near 93 A.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 256 clusters / 1024 extra; no template. Run time 13 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 4 | 82.1 | 46.7 | 93.2 | 82.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.6 | 1 | 7 | 81.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 79.8 | 86.2 | 87.2 |
| 2 | 81.5 | 94.2 | 84.5 |
| 3 | 81.9 | 93.2 | 82.5 |
| 4 | 82.1 | 93.2 | 82.3 |
| 5 | 81.9 | 93.0 | 82.3 |
| 6 | 81.7 | 93.1 | 82.2 |
| 7 | 81.5 | 92.9 | 81.6 |
| 8 | 82.1 | 93.2 | 82.4 |
| 9 | 81.9 | 93.4 | 82.0 |
| 10 | 82.1 | 92.9 | 82.1 |
| 11 | 81.8 | 93.2 | 82.0 |
| 12 | 81.9 | 93.4 | 82.2 |
| 13 | 81.8 | 93.4 | 81.9 |
| 14 | 82.0 | 93.2 | 82.2 |
| 15 | 81.9 | 93.4 | 82.5 |

pLDDT 79.8–82.1; JH2–JH1 46.4–48.0 Å; FERM–JH1 86.2–94.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 86 94 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
