# TYK2_20261022_001920 — TYK2 WT_free_msa256-1024_s0-7__seed5

TYK2 wild type, template-free, MSA 256/1024, seeds 0-7. fills the one remaining hole in the TYK2 depth ladder, between 128/512 (collapsed open, spread 0.6 A) and 64/256 (the only bimodal depth, spread 60.5 A). Knowing where the transition starts matters because every TYK2 mutation result rests on 64/256 being the sole depth with dynamic range. Prediction stated in advance: open, near 93 A.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 256 clusters / 1024 extra; no template. Run time 13 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 4 | 81.9 | 46.7 | 93.5 | 82.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 30.4 | 5 | 1 | 78.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.7 | 42.5 | 30.4 |
| 2 | 81.3 | 93.5 | 83.0 |
| 3 | 81.3 | 93.0 | 82.4 |
| 4 | 81.9 | 93.5 | 82.2 |
| 5 | 81.5 | 92.9 | 82.4 |
| 6 | 81.6 | 93.2 | 81.7 |
| 7 | 81.6 | 93.4 | 82.4 |
| 8 | 81.6 | 93.1 | 81.8 |
| 9 | 81.6 | 93.2 | 81.8 |
| 10 | 81.5 | 93.3 | 81.7 |
| 11 | 81.9 | 93.3 | 82.4 |
| 12 | 81.9 | 93.4 | 81.8 |
| 13 | 81.5 | 93.0 | 81.7 |
| 14 | 81.7 | 93.4 | 82.7 |
| 15 | 81.6 | 93.1 | 81.9 |

pLDDT 78.7–81.9; JH2–JH1 46.4–50.6 Å; FERM–JH1 42.5–93.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 42 94 93 94 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
