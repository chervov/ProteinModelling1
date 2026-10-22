# TYK2_H582W_20261022_152443 — TYK2 H582W_free_msa64-256_s0-7__seed5

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 15 | 80.6 | 49.6 | 89.7 | 90.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 28.5 | 5 | 2 | 76.2 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.7 | 57.5 | 46.2 |
| 2 | 76.2 | 30.7 | 28.5 |
| 3 | 79.2 | 38.4 | 44.1 |
| 4 | 80.2 | 47.1 | 52.7 |
| 5 | 80.2 | 49.5 | 54.6 |
| 6 | 80.4 | 55.2 | 59.2 |
| 7 | 80.2 | 66.5 | 71.8 |
| 8 | 80.4 | 67.9 | 72.7 |
| 9 | 80.5 | 62.3 | 65.9 |
| 10 | 80.4 | 68.2 | 76.3 |
| 11 | 80.2 | 70.7 | 76.6 |
| 12 | 80.4 | 72.2 | 80.3 |
| 13 | 80.4 | 64.3 | 73.1 |
| 14 | 80.6 | 77.3 | 83.8 |
| 15 | 80.6 | 89.7 | 90.1 |

pLDDT 69.7–80.6; JH2–JH1 49.1–55.7 Å; FERM–JH1 30.7–89.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 58 31 38 47 50 55 66 68 62 68 71 72 64 77 90 | open-like (> 80) |
