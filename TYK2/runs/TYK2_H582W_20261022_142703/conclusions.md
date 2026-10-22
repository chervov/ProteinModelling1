# TYK2_H582W_20261022_142703 — TYK2 H582W_free_msa64-256_s0-7__seed0

TYK2 H582W, template-free, MSA 64/256, seeds 0-7. H582W is the ONLY variant in this campaign tested solely in the template-release assay, which section 49 showed returns 'closed' for every sequence and has no dynamic range. It is also the strongest candidate in the whole deep mutational scan: IFN-alpha +1.339 at 1 U/mL (99.92nd percentile, only 18 of 22,536 variants beat it), +0.968 at 100 U/mL so activating at BOTH doses, and abundance -0.083 (47.8th percentile) so entirely unconfounded by stability - unlike V678F (-0.323, near the nonsense anchor). It sits on the 4OLI JH2-JH1 interface. 64/256 is chosen because wild type is 2/24 open there, leaving room to detect an INCREASE. Prediction stated in advance: if the arrangement score tracks activation, H582W should open like V678F (0.75); if it tracks stability, it should look like wild type (0.08) since its abundance is normal.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0; MSA 64 clusters / 256 extra; no template. Run time 16 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 13 | 80.5 | 49.5 | 88.0 | 90.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 42.5 | 0 | 3 | 78.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 67.4 | 51.4 | 64.8 |
| 2 | 76.7 | 43.6 | 43.7 |
| 3 | 78.7 | 39.8 | 42.5 |
| 4 | 79.5 | 44.4 | 46.8 |
| 5 | 79.6 | 51.3 | 55.3 |
| 6 | 79.7 | 57.3 | 62.0 |
| 7 | 79.4 | 54.1 | 58.3 |
| 8 | 79.4 | 57.2 | 62.5 |
| 9 | 79.7 | 57.6 | 63.8 |
| 10 | 79.8 | 60.1 | 64.5 |
| 11 | 79.9 | 59.4 | 66.2 |
| 12 | 80.2 | 76.9 | 84.3 |
| 13 | 80.4 | 88.0 | 90.6 |
| 14 | 80.2 | 93.0 | 91.6 |
| 15 | 80.3 | 91.2 | 91.8 |

pLDDT 67.5–80.5; JH2–JH1 49.5–57.3 Å; FERM–JH1 39.8–93.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 51 44 40 44 51 57 54 57 58 60 59 77 88 93 91 | open-like (> 80) |
