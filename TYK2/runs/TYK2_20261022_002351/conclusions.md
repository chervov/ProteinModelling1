# TYK2_20261022_002351 — TYK2 WT_free_msa512-8192_s0-7__seed5

TYK2 wild type, template-free, MSA 512/8192, seeds 0-7. the deepest setting and AlphaFold's own standard MSA depth. TYK2 has never been run here in any variant: the ladder stops at 128/512. The motivating discrepancy is that the AlphaFold model of TYK2 is CLOSED (FERM-JH1 39.7 A) while our template-free prediction at 128/512 is 100 percent OPEN (93.6 A, 0/8 compact, seed spread 0.6 A). Running at AlphaFold's depth asks directly whether the difference is the MSA depth or something else in the pipeline - guided recycling, the selection objective, or template handling. Prediction stated in advance: 0/8 compact, median ~93.5 A, spread under 1 A. If it comes back CLOSED that is a significant finding and explains the gap.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 512 clusters / 8192 extra; no template. Run time 19 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 13 | 82.8 | 46.6 | 93.1 | 82.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.9 | 5 | 8 | 82.5 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 80.8 | 93.7 | 84.7 |
| 2 | 82.2 | 93.3 | 82.0 |
| 3 | 82.4 | 93.7 | 82.3 |
| 4 | 82.5 | 93.3 | 82.4 |
| 5 | 82.6 | 93.5 | 82.2 |
| 6 | 82.6 | 93.4 | 82.3 |
| 7 | 82.6 | 93.2 | 82.1 |
| 8 | 82.5 | 93.2 | 81.9 |
| 9 | 82.5 | 93.4 | 82.1 |
| 10 | 82.5 | 93.4 | 81.9 |
| 11 | 82.6 | 93.2 | 82.3 |
| 12 | 82.4 | 93.4 | 82.1 |
| 13 | 82.8 | 93.1 | 82.2 |
| 14 | 82.4 | 93.9 | 82.4 |
| 15 | 82.5 | 93.6 | 82.0 |

pLDDT 80.8–82.8; JH2–JH1 46.4–48.0 Å; FERM–JH1 93.1–93.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 94 93 94 93 94 93 93 93 93 93 93 93 93 94 94 | open-like (> 80) |
