# TYK2_H582W_20261022_150146 — TYK2 H582W_free_msa64-256_s0-7__seed3

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 5 | 80.5 | 53.5 | 92.4 | 96.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 52.7 | 3 | 2 | 75.9 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 67.6 | 66.3 | 65.3 |
| 2 | 75.9 | 43.8 | 52.7 |
| 3 | 79.1 | 65.2 | 63.6 |
| 4 | 79.9 | 80.6 | 89.1 |
| 5 | 80.4 | 92.4 | 96.1 |
| 6 | 80.3 | 95.4 | 91.4 |
| 7 | 80.2 | 95.5 | 87.6 |
| 8 | 80.3 | 95.1 | 91.0 |
| 9 | 80.1 | 95.3 | 88.9 |
| 10 | 80.0 | 94.4 | 91.8 |
| 11 | 80.1 | 95.2 | 86.6 |
| 12 | 80.1 | 94.8 | 91.2 |
| 13 | 80.2 | 95.2 | 88.5 |
| 14 | 80.3 | 95.6 | 91.7 |
| 15 | 80.4 | 95.4 | 91.1 |

pLDDT 67.6–80.5; JH2–JH1 28.1–53.5 Å; FERM–JH1 43.8–95.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 66 44 65 81 92 95 96 95 95 94 95 95 95 96 95 | open-like (> 80) |
