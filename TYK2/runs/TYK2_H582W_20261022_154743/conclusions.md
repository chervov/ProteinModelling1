# TYK2_H582W_20261022_154743 — TYK2 H582W_free_msa64-256_s0-7__seed7

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 7; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 7 | 15 | 80.1 | 47.0 | 93.1 | 83.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 35.0 | 7 | 2 | 76.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 66.5 | 44.1 | 37.6 |
| 2 | 76.6 | 37.1 | 35.0 |
| 3 | 78.6 | 68.8 | 71.0 |
| 4 | 79.3 | 94.8 | 90.2 |
| 5 | 79.2 | 93.9 | 83.6 |
| 6 | 78.9 | 94.5 | 85.6 |
| 7 | 79.2 | 94.2 | 84.1 |
| 8 | 79.2 | 95.0 | 86.5 |
| 9 | 79.2 | 94.3 | 84.0 |
| 10 | 79.3 | 94.4 | 85.0 |
| 11 | 79.0 | 94.7 | 86.3 |
| 12 | 78.9 | 94.5 | 84.1 |
| 13 | 79.4 | 94.7 | 85.2 |
| 14 | 79.5 | 93.4 | 83.5 |
| 15 | 80.1 | 93.1 | 83.1 |

pLDDT 66.5–80.1; JH2–JH1 41.9–52.0 Å; FERM–JH1 37.1–95.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 7 | 44 37 69 95 94 94 94 95 94 94 95 94 95 93 93 | open-like (> 80) |
