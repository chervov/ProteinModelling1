# TYK2_20261021_231855 — TYK2 WT_free_msa256-1024_s0-7__seed3

TYK2 wild type, template-free, MSA 256/1024, seeds 0-7. fills the one remaining hole in the TYK2 depth ladder, between 128/512 (collapsed open, spread 0.6 A) and 64/256 (the only bimodal depth, spread 60.5 A). Knowing where the transition starts matters because every TYK2 mutation result rests on 64/256 being the sole depth with dynamic range. Prediction stated in advance: open, near 93 A.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 256 clusters / 1024 extra; no template. Run time 13 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 5 | 82.1 | 46.5 | 92.9 | 82.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.5 | 3 | 13 | 81.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 78.8 | 93.0 | 84.3 |
| 2 | 81.9 | 93.5 | 81.7 |
| 3 | 81.8 | 92.9 | 82.0 |
| 4 | 81.8 | 93.3 | 82.2 |
| 5 | 82.1 | 92.9 | 82.0 |
| 6 | 81.8 | 93.0 | 81.7 |
| 7 | 81.9 | 92.8 | 81.9 |
| 8 | 81.8 | 93.2 | 82.3 |
| 9 | 81.9 | 93.2 | 82.2 |
| 10 | 81.9 | 93.2 | 82.2 |
| 11 | 81.9 | 93.3 | 82.1 |
| 12 | 81.8 | 93.0 | 81.9 |
| 13 | 81.7 | 93.3 | 81.5 |
| 14 | 82.0 | 93.2 | 81.6 |
| 15 | 82.0 | 93.1 | 82.2 |

pLDDT 78.8–82.1; JH2–JH1 46.4–47.1 Å; FERM–JH1 92.8–93.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 93 94 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
