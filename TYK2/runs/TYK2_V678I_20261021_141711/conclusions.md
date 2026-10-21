# TYK2_V678I_20261021_141711 — TYK2 V678I_rel4OLI_msa128-512_s0-7__seed0

TYK2 V678I with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.520, abundance -0.088. second strongest activator, abundance essentially intact. Second discriminating case, independent of V678M.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 80.2 | 37.0 | 39.1 | 1.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 0 | 12 | 79.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.8 | 45.6 | 3.7 |
| 2 (template) | 80.0 | 39.4 | 1.2 |
| 3 (template) | 81.0 | 39.7 | 1.0 |
| 4 | 80.2 | 39.1 | 1.3 |
| 5 | 79.7 | 38.9 | 1.3 |
| 6 | 79.9 | 39.9 | 1.8 |
| 7 | 79.5 | 39.5 | 1.5 |
| 8 | 79.9 | 39.7 | 1.2 |
| 9 | 79.8 | 39.8 | 1.5 |
| 10 | 79.8 | 39.9 | 1.5 |
| 11 | 79.7 | 39.5 | 1.2 |
| 12 | 79.8 | 39.7 | 0.8 |
| 13 | 80.0 | 39.8 | 1.7 |
| 14 | 79.7 | 39.6 | 1.2 |
| 15 | 79.9 | 39.7 | 1.3 |

pLDDT 76.8–81.0; JH2–JH1 37.0–37.4 Å; FERM–JH1 38.9–45.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 46 39 40 39 39 40 40 40 40 40 40 40 40 40 40 | closed-like (< 50) |
