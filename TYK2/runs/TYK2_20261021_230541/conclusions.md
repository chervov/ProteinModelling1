# TYK2_20261021_230541 — TYK2 WT_free_msa256-1024_s0-7__seed2

TYK2 wild type, template-free, MSA 256/1024, seeds 0-7. fills the one remaining hole in the TYK2 depth ladder, between 128/512 (collapsed open, spread 0.6 A) and 64/256 (the only bimodal depth, spread 60.5 A). Knowing where the transition starts matters because every TYK2 mutation result rests on 64/256 being the sole depth with dynamic range. Prediction stated in advance: open, near 93 A.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 256 clusters / 1024 extra; no template. Run time 13 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 14 | 82.2 | 46.5 | 92.1 | 81.8 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.5 | 2 | 9 | 82.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 79.2 | 91.9 | 83.4 |
| 2 | 81.5 | 92.6 | 82.2 |
| 3 | 82.1 | 92.2 | 82.1 |
| 4 | 82.2 | 92.5 | 81.8 |
| 5 | 82.2 | 93.1 | 81.8 |
| 6 | 82.0 | 92.2 | 81.8 |
| 7 | 82.1 | 92.4 | 81.9 |
| 8 | 82.2 | 92.4 | 81.7 |
| 9 | 82.0 | 92.3 | 81.5 |
| 10 | 82.0 | 92.7 | 82.0 |
| 11 | 82.0 | 92.5 | 82.1 |
| 12 | 82.2 | 92.3 | 82.1 |
| 13 | 82.0 | 92.1 | 81.6 |
| 14 | 82.2 | 92.1 | 81.8 |
| 15 | 82.1 | 92.4 | 82.0 |

pLDDT 79.2–82.2; JH2–JH1 46.4–47.2 Å; FERM–JH1 91.9–93.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 92 93 92 92 93 92 92 92 92 93 92 92 92 92 92 | open-like (> 80) |
