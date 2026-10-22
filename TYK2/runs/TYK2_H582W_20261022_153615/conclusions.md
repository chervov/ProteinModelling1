# TYK2_H582W_20261022_153615 — TYK2 H582W_free_msa64-256_s0-7__seed6

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 6; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 6 | 12 | 80.3 | 47.7 | 83.2 | 89.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 41.8 | 6 | 5 | 79.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 67.2 | 34.9 | 43.9 |
| 2 | 74.6 | 40.9 | 48.6 |
| 3 | 77.8 | 45.0 | 44.1 |
| 4 | 79.2 | 45.4 | 42.1 |
| 5 | 79.1 | 46.6 | 41.8 |
| 6 | 79.0 | 49.2 | 51.4 |
| 7 | 79.7 | 76.3 | 77.3 |
| 8 | 80.0 | 81.8 | 88.1 |
| 9 | 80.0 | 82.3 | 88.0 |
| 10 | 79.6 | 85.1 | 89.1 |
| 11 | 79.8 | 81.1 | 88.1 |
| 12 | 80.3 | 83.2 | 89.0 |
| 13 | 79.8 | 88.5 | 91.0 |
| 14 | 80.1 | 88.6 | 90.4 |
| 15 | 80.1 | 84.5 | 89.5 |

pLDDT 67.2–80.3; JH2–JH1 41.6–64.5 Å; FERM–JH1 34.9–88.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 6 | 35 41 45 45 47 49 76 82 82 85 81 83 88 89 84 | open-like (> 80) |
