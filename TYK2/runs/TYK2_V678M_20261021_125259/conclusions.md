# TYK2_V678M_20261021_125259 — TYK2 V678M_rel4OLI_msa128-512_s0-7__seed1

TYK2 V678M with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.561, abundance +0.002. strongest measured activator at the position (97th percentile) with protein abundance untouched. THE DISCRIMINATING CASE: if the method has functional sensitivity it should release the closed state; if it tracks foldability it should hold like wild type.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 4 | 80.6 | 37.1 | 40.0 | 1.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 1 | 2 | 79.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 75.4 | 46.2 | 1.7 |
| 2 (template) | 79.8 | 40.7 | 0.8 |
| 3 (template) | 81.4 | 39.3 | 1.3 |
| 4 | 80.6 | 40.0 | 1.6 |
| 5 | 80.1 | 38.8 | 1.9 |
| 6 | 80.6 | 39.1 | 1.5 |
| 7 | 80.2 | 39.1 | 1.9 |
| 8 | 80.3 | 39.2 | 1.3 |
| 9 | 80.5 | 39.1 | 1.1 |
| 10 | 80.4 | 39.2 | 1.4 |
| 11 | 80.4 | 39.2 | 1.4 |
| 12 | 80.0 | 39.2 | 1.5 |
| 13 | 80.5 | 39.2 | 1.2 |
| 14 | 80.1 | 39.3 | 1.8 |
| 15 | 80.6 | 39.0 | 1.5 |

pLDDT 75.4–81.3; JH2–JH1 37.0–37.5 Å; FERM–JH1 38.8–46.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 46 41 39 40 39 39 39 39 39 39 39 39 39 39 39 | closed-like (< 50) |
