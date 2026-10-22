# TYK2_V678I_20261022_053546 — TYK2 V678I_rel4OLI_msa128-512_s0-7__seed3

TYK2 V678I with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.520, abundance -0.088. second strongest activator, abundance essentially intact. Second discriminating case, independent of V678M.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 9 | 80.0 | 37.6 | 39.1 | 1.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.7 | 3 | 2 | 80.6 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 74.9 | 39.8 | 1.6 |
| 2 (template) | 80.6 | 39.3 | 0.7 |
| 3 (template) | 80.6 | 38.7 | 0.9 |
| 4 | 79.7 | 38.4 | 1.0 |
| 5 | 80.0 | 38.8 | 1.5 |
| 6 | 79.8 | 39.4 | 1.3 |
| 7 | 79.9 | 39.2 | 1.3 |
| 8 | 79.7 | 40.0 | 1.6 |
| 9 | 80.0 | 39.1 | 1.4 |
| 10 | 79.6 | 39.0 | 1.6 |
| 11 | 79.8 | 39.5 | 1.4 |
| 12 | 79.9 | 38.9 | 1.4 |
| 13 | 80.0 | 39.1 | 1.4 |
| 14 | 79.5 | 38.8 | 1.6 |
| 15 | 79.6 | 38.9 | 1.7 |

pLDDT 74.9–80.7; JH2–JH1 37.2–37.6 Å; FERM–JH1 38.4–40.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 40 39 39 38 39 39 39 40 39 39 40 39 39 39 39 | closed-like (< 50) |
