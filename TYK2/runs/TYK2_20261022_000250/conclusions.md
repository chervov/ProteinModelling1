# TYK2_20261022_000250 — TYK2 WT_free_msa512-8192_s0-7__seed3

TYK2 wild type, template-free, MSA 512/8192, seeds 0-7. the deepest setting and AlphaFold's own standard MSA depth. TYK2 has never been run here in any variant: the ladder stops at 128/512. The motivating discrepancy is that the AlphaFold model of TYK2 is CLOSED (FERM-JH1 39.7 A) while our template-free prediction at 128/512 is 100 percent OPEN (93.6 A, 0/8 compact, seed spread 0.6 A). Running at AlphaFold's depth asks directly whether the difference is the MSA depth or something else in the pipeline - guided recycling, the selection objective, or template handling. Prediction stated in advance: 0/8 compact, median ~93.5 A, spread under 1 A. If it comes back CLOSED that is a significant finding and explains the gap.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 512 clusters / 8192 extra; no template. Run time 2 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 4 | 82.9 | 46.8 | 93.6 | 81.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.5 | 3 | 12 | 82.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 80.5 | 92.6 | 83.1 |
| 2 | 82.6 | 93.1 | 81.9 |
| 3 | 82.8 | 93.3 | 81.8 |
| 4 | 82.9 | 93.6 | 81.9 |
| 5 | 82.7 | 93.2 | 81.7 |
| 6 | 82.6 | 93.2 | 81.9 |
| 7 | 82.7 | 93.1 | 81.9 |
| 8 | 82.8 | 93.1 | 81.9 |
| 9 | 82.4 | 93.2 | 81.9 |
| 10 | 82.8 | 93.3 | 81.9 |
| 11 | 82.7 | 93.4 | 82.0 |
| 12 | 82.5 | 93.3 | 81.5 |
| 13 | 82.7 | 93.3 | 81.6 |
| 14 | 82.7 | 93.1 | 81.6 |
| 15 | 82.8 | 93.2 | 81.7 |

pLDDT 80.5–82.9; JH2–JH1 46.4–47.1 Å; FERM–JH1 92.6–93.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 93 93 93 94 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
