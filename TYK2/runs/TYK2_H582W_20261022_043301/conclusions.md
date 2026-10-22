# TYK2_H582W_20261022_043301 — TYK2 H582W_rel4OLI_msa128-512_s0-7__seed4

TYK2 H582W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. The strongest candidate in the entire deep mutational scan for destabilising the closed state: residue 582 is in the 4OLI JH2-JH1 interface, the substitution is the MOST ACTIVATING at any interface residue (IFN-alpha +1.339, 99.9th percentile of 23,723 variants, and activating at BOTH 1 U/mL and 100 U/mL unlike most gain-of-function variants), and protein abundance is intact (-0.083, 48th percentile) so it is not confounded the way V678F is (-0.323, near the nonsense anchor). If this does not release the closed state, the assay cannot detect destabilisation at all

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 4; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 4 | 15 | 80.6 | 37.5 | 39.3 | 1.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 4 | 2 | 80.3 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.5 | 44.9 | 2.1 |
| 2 (template) | 80.3 | 40.0 | 0.8 |
| 3 (template) | 80.8 | 39.6 | 1.1 |
| 4 | 80.2 | 39.0 | 1.3 |
| 5 | 79.9 | 39.1 | 1.5 |
| 6 | 79.8 | 39.4 | 1.4 |
| 7 | 79.9 | 39.6 | 2.0 |
| 8 | 79.9 | 39.2 | 2.2 |
| 9 | 80.4 | 39.1 | 1.8 |
| 10 | 80.1 | 39.2 | 1.8 |
| 11 | 80.1 | 39.5 | 1.9 |
| 12 | 80.1 | 39.3 | 2.0 |
| 13 | 80.2 | 39.5 | 1.7 |
| 14 | 80.4 | 39.6 | 2.1 |
| 15 | 80.6 | 39.3 | 1.5 |

pLDDT 77.5–80.8; JH2–JH1 37.2–37.6 Å; FERM–JH1 39.0–44.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 4 | 45 40 40 39 39 39 40 39 39 39 40 39 40 40 39 | closed-like (< 50) |
