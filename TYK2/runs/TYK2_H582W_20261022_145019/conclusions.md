# TYK2_H582W_20261022_145019 — TYK2 H582W_free_msa64-256_s0-7__seed2

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 6 | 80.8 | 52.7 | 92.0 | 95.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 46.3 | 2 | 2 | 77.0 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 67.2 | 41.6 | 55.9 |
| 2 | 77.0 | 49.3 | 46.3 |
| 3 | 78.3 | 51.2 | 55.8 |
| 4 | 80.3 | 78.1 | 86.4 |
| 5 | 80.2 | 94.1 | 91.9 |
| 6 | 80.8 | 92.0 | 95.0 |
| 7 | 80.3 | 95.2 | 89.6 |
| 8 | 80.2 | 94.0 | 90.8 |
| 9 | 80.2 | 94.0 | 91.5 |
| 10 | 80.4 | 94.5 | 89.6 |
| 11 | 80.5 | 94.0 | 91.6 |
| 12 | 80.5 | 94.0 | 92.6 |
| 13 | 80.2 | 94.5 | 89.0 |
| 14 | 80.0 | 94.5 | 89.8 |
| 15 | 80.4 | 94.6 | 90.1 |

pLDDT 67.2–80.8; JH2–JH1 49.2–53.7 Å; FERM–JH1 41.6–95.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 42 49 51 78 94 92 95 94 94 94 94 94 94 94 95 | open-like (> 80) |
