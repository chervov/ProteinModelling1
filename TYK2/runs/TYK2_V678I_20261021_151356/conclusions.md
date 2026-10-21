# TYK2_V678I_20261021_151356 — TYK2 V678I_rel4OLI_msa128-512_s0-7__seed1

TYK2 V678I with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.520, abundance -0.088. second strongest activator, abundance essentially intact. Second discriminating case, independent of V678M.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 57 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 10 | 80.7 | 37.2 | 38.2 | 1.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.6 | 1 | 2 | 80.9 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.7 | 44.7 | 1.8 |
| 2 (template) | 80.9 | 39.4 | 0.6 |
| 3 (template) | 81.2 | 38.1 | 1.1 |
| 4 | 80.6 | 38.5 | 0.9 |
| 5 | 80.4 | 38.2 | 2.1 |
| 6 | 80.3 | 38.0 | 2.0 |
| 7 | 80.2 | 38.2 | 2.2 |
| 8 | 80.2 | 38.6 | 1.5 |
| 9 | 80.4 | 38.4 | 1.1 |
| 10 | 80.7 | 38.2 | 1.5 |
| 11 | 80.4 | 39.4 | 2.1 |
| 12 | 80.3 | 38.8 | 2.0 |
| 13 | 80.4 | 38.9 | 2.2 |
| 14 | 79.9 | 39.3 | 2.0 |
| 15 | 80.1 | 38.6 | 2.0 |

pLDDT 76.7–81.2; JH2–JH1 37.1–37.5 Å; FERM–JH1 38.0–44.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 45 39 38 38 38 38 38 39 38 38 39 39 39 39 39 | closed-like (< 50) |
