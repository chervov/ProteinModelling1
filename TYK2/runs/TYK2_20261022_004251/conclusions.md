# TYK2_20261022_004251 — TYK2 WT_free_msa512-8192_s0-7__seed6

TYK2 wild type, template-free, MSA 512/8192, seeds 0-7. the deepest setting and AlphaFold's own standard MSA depth. TYK2 has never been run here in any variant: the ladder stops at 128/512. The motivating discrepancy is that the AlphaFold model of TYK2 is CLOSED (FERM-JH1 39.7 A) while our template-free prediction at 128/512 is 100 percent OPEN (93.6 A, 0/8 compact, seed spread 0.6 A). Running at AlphaFold's depth asks directly whether the difference is the MSA depth or something else in the pipeline - guided recycling, the selection objective, or template handling. Prediction stated in advance: 0/8 compact, median ~93.5 A, spread under 1 A. If it comes back CLOSED that is a significant finding and explains the gap.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 6; MSA 512 clusters / 8192 extra; no template. Run time 19 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 6 | 5 | 82.5 | 46.5 | 93.2 | 81.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 81.0 | 6 | 6 | 82.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 80.6 | 93.8 | 84.9 |
| 2 | 82.1 | 93.1 | 82.6 |
| 3 | 82.4 | 93.0 | 82.2 |
| 4 | 82.2 | 93.3 | 82.3 |
| 5 | 82.5 | 93.2 | 81.9 |
| 6 | 82.2 | 93.3 | 81.0 |
| 7 | 82.1 | 93.0 | 81.2 |
| 8 | 82.3 | 92.9 | 81.8 |
| 9 | 82.3 | 93.3 | 81.7 |
| 10 | 82.3 | 93.3 | 81.3 |
| 11 | 82.2 | 93.2 | 81.7 |
| 12 | 82.2 | 93.1 | 81.4 |
| 13 | 82.2 | 93.3 | 81.5 |
| 14 | 82.4 | 93.2 | 81.9 |
| 15 | 82.2 | 93.3 | 81.1 |

pLDDT 80.6–82.5; JH2–JH1 46.4–47.8 Å; FERM–JH1 92.9–93.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 6 | 94 93 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
