# TYK2_V678M_20261021_135303 — TYK2 V678M_rel4OLI_msa128-512_s0-7__seed6

TYK2 V678M with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.561, abundance +0.002. strongest measured activator at the position (97th percentile) with protein abundance untouched. THE DISCRIMINATING CASE: if the method has functional sensitivity it should release the closed state; if it tracks foldability it should hold like wild type.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 6; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 6 | 4 | 80.0 | 36.9 | 38.4 | 2.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 6 | 2 | 80.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.8 | 40.3 | 1.5 |
| 2 (template) | 80.0 | 39.2 | 1.0 |
| 3 (template) | 80.9 | 38.6 | 1.3 |
| 4 | 80.0 | 38.4 | 2.0 |
| 5 | 79.6 | 38.4 | 2.2 |
| 6 | 79.4 | 38.4 | 1.6 |
| 7 | 79.8 | 38.4 | 2.3 |
| 8 | 79.7 | 38.8 | 1.6 |
| 9 | 79.6 | 38.4 | 1.7 |
| 10 | 79.5 | 38.5 | 2.2 |
| 11 | 79.6 | 38.6 | 2.2 |
| 12 | 79.7 | 38.6 | 1.9 |
| 13 | 79.6 | 38.3 | 2.1 |
| 14 | 79.8 | 38.5 | 2.0 |
| 15 | 79.6 | 38.3 | 1.9 |

pLDDT 76.8–80.9; JH2–JH1 36.8–37.4 Å; FERM–JH1 38.3–40.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 6 | 40 39 39 38 38 38 38 39 38 38 39 39 38 38 38 | closed-like (< 50) |
