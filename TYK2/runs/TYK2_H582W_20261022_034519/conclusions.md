# TYK2_H582W_20261022_034519 — TYK2 H582W_rel4OLI_msa128-512_s0-7__seed0

TYK2 H582W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. The strongest candidate in the entire deep mutational scan for destabilising the closed state: residue 582 is in the 4OLI JH2-JH1 interface, the substitution is the MOST ACTIVATING at any interface residue (IFN-alpha +1.339, 99.9th percentile of 23,723 variants, and activating at BOTH 1 U/mL and 100 U/mL unlike most gain-of-function variants), and protein abundance is intact (-0.083, 48th percentile) so it is not confounded the way V678F is (-0.323, near the nonsense anchor). If this does not release the closed state, the assay cannot detect destabilisation at all

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 19 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 9 | 80.8 | 37.4 | 39.4 | 1.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.9 | 0 | 2 | 80.1 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.2 | 48.6 | 2.1 |
| 2 (template) | 80.1 | 39.7 | 0.9 |
| 3 (template) | 81.2 | 39.6 | 1.3 |
| 4 | 80.5 | 39.5 | 1.1 |
| 5 | 80.2 | 39.3 | 1.2 |
| 6 | 80.4 | 39.6 | 1.3 |
| 7 | 80.1 | 39.7 | 1.3 |
| 8 | 80.4 | 39.6 | 1.1 |
| 9 | 80.8 | 39.4 | 1.4 |
| 10 | 80.4 | 39.5 | 1.8 |
| 11 | 80.2 | 39.7 | 1.9 |
| 12 | 80.2 | 39.6 | 1.9 |
| 13 | 80.4 | 39.6 | 2.1 |
| 14 | 80.3 | 39.5 | 2.2 |
| 15 | 80.3 | 39.6 | 1.9 |

pLDDT 77.2–81.2; JH2–JH1 37.0–37.5 Å; FERM–JH1 39.3–48.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 49 40 40 40 39 40 40 40 39 40 40 40 40 40 40 | closed-like (< 50) |
