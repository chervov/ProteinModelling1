# TYK2_V678M_20261021_134103 — TYK2 V678M_rel4OLI_msa128-512_s0-7__seed5

TYK2 V678M with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.561, abundance +0.002. strongest measured activator at the position (97th percentile) with protein abundance untouched. THE DISCRIMINATING CASE: if the method has functional sensitivity it should release the closed state; if it tracks foldability it should hold like wild type.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 13 | 80.7 | 37.4 | 38.9 | 1.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 5 | 2 | 80.6 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 75.6 | 43.5 | 1.3 |
| 2 (template) | 80.6 | 39.6 | 0.8 |
| 3 (template) | 81.4 | 39.4 | 0.9 |
| 4 | 80.6 | 39.2 | 0.8 |
| 5 | 80.4 | 39.2 | 1.1 |
| 6 | 80.2 | 38.7 | 1.0 |
| 7 | 80.4 | 38.9 | 1.1 |
| 8 | 80.4 | 38.7 | 1.2 |
| 9 | 80.4 | 38.6 | 1.2 |
| 10 | 80.3 | 38.8 | 1.4 |
| 11 | 80.6 | 38.9 | 1.4 |
| 12 | 80.6 | 39.2 | 0.9 |
| 13 | 80.7 | 38.9 | 1.3 |
| 14 | 80.4 | 38.8 | 2.2 |
| 15 | 80.3 | 38.7 | 1.7 |

pLDDT 75.6–81.4; JH2–JH1 37.2–37.8 Å; FERM–JH1 38.6–43.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 44 40 39 39 39 39 39 39 39 39 39 39 39 39 39 | closed-like (< 50) |
