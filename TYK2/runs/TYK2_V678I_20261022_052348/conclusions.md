# TYK2_V678I_20261022_052348 — TYK2 V678I_rel4OLI_msa128-512_s0-7__seed2

TYK2 V678I with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.520, abundance -0.088. second strongest activator, abundance essentially intact. Second discriminating case, independent of V678M.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 15 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 5 | 80.2 | 37.5 | 40.0 | 1.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.1 | 2 | 2 | 80.9 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.2 | 42.4 | 1.2 |
| 2 (template) | 80.9 | 39.4 | 1.1 |
| 3 (template) | 81.2 | 40.2 | 1.2 |
| 4 | 80.2 | 39.6 | 1.2 |
| 5 | 80.2 | 40.0 | 1.2 |
| 6 | 80.2 | 40.6 | 1.6 |
| 7 | 80.0 | 39.8 | 1.4 |
| 8 | 79.9 | 39.9 | 1.3 |
| 9 | 80.2 | 39.9 | 1.4 |
| 10 | 80.1 | 39.5 | 1.5 |
| 11 | 80.0 | 40.0 | 1.8 |
| 12 | 79.8 | 39.5 | 1.5 |
| 13 | 80.2 | 39.5 | 1.4 |
| 14 | 79.9 | 40.1 | 1.4 |
| 15 | 80.1 | 40.1 | 1.4 |

pLDDT 77.2–81.2; JH2–JH1 37.1–37.8 Å; FERM–JH1 39.4–42.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 42 39 40 40 40 41 40 40 40 40 40 40 40 40 40 | closed-like (< 50) |
