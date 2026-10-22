# TYK2_H582W_20261022_143850 — TYK2 H582W_free_msa64-256_s0-7__seed1

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 64 clusters / 256 extra; no template. Run time 11 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 4 | 79.2 | 39.2 | 40.4 | 5.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.8 | 1 | 12 | 78.9 | 12 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 64.8 | 45.7 | 77.0 |
| 2 | 76.1 | 40.9 | 55.3 |
| 3 | 78.8 | 40.7 | 18.0 |
| 4 | 79.2 | 40.4 | 5.7 |
| 5 | 78.8 | 40.7 | 4.6 |
| 6 | 79.0 | 40.6 | 4.4 |
| 7 | 78.7 | 40.6 | 6.0 |
| 8 | 78.7 | 40.4 | 4.8 |
| 9 | 79.0 | 40.3 | 3.9 |
| 10 | 79.0 | 40.5 | 3.8 |
| 11 | 79.0 | 40.9 | 4.4 |
| 12 | 78.9 | 40.6 | 1.8 |
| 13 | 78.9 | 40.3 | 4.4 |
| 14 | 78.6 | 40.8 | 2.5 |
| 15 | 79.0 | 40.6 | 5.6 |

pLDDT 64.8–79.2; JH2–JH1 38.2–61.7 Å; FERM–JH1 40.3–45.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 46 41 41 40 41 41 41 40 40 40 41 41 40 41 41 | closed-like (< 50) |
