# TYK2_H582W_20261022_151315 — TYK2 H582W_free_msa64-256_s0-7__seed4

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 4; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 4 | 8 | 80.1 | 47.1 | 93.5 | 83.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 20.7 | 4 | 3 | 76.3 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 66.1 | 54.8 | 64.4 |
| 2 | 74.8 | 41.7 | 50.7 |
| 3 | 76.3 | 37.2 | 20.7 |
| 4 | 79.4 | 92.6 | 88.7 |
| 5 | 79.5 | 94.5 | 85.7 |
| 6 | 79.7 | 93.6 | 84.1 |
| 7 | 80.0 | 93.4 | 83.0 |
| 8 | 80.1 | 93.5 | 83.0 |
| 9 | 79.8 | 93.1 | 82.6 |
| 10 | 79.2 | 93.3 | 82.7 |
| 11 | 79.7 | 93.2 | 82.8 |
| 12 | 79.9 | 93.0 | 82.7 |
| 13 | 80.0 | 93.2 | 82.9 |
| 14 | 79.8 | 93.2 | 83.0 |
| 15 | 79.9 | 93.5 | 83.1 |

pLDDT 66.1–80.1; JH2–JH1 28.4–67.3 Å; FERM–JH1 37.2–94.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 4 | 55 42 37 93 94 94 93 94 93 93 93 93 93 93 94 | open-like (> 80) |
