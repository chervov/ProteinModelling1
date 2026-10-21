# TYK2_V678M_20261021_140501 — TYK2 V678M_rel4OLI_msa128-512_s0-7__seed7

TYK2 V678M with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.561, abundance +0.002. strongest measured activator at the position (97th percentile) with protein abundance untouched. THE DISCRIMINATING CASE: if the method has functional sensitivity it should release the closed state; if it tracks foldability it should hold like wild type.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 7; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 7 | 14 | 80.6 | 37.3 | 38.8 | 1.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.9 | 7 | 3 | 81.2 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.1 | 41.0 | 1.7 |
| 2 (template) | 79.9 | 39.8 | 1.1 |
| 3 (template) | 81.2 | 39.1 | 0.9 |
| 4 | 80.5 | 38.8 | 1.2 |
| 5 | 80.3 | 38.5 | 1.8 |
| 6 | 80.4 | 38.9 | 1.8 |
| 7 | 80.0 | 38.7 | 1.7 |
| 8 | 80.1 | 38.6 | 2.0 |
| 9 | 80.1 | 39.0 | 1.6 |
| 10 | 80.3 | 38.7 | 2.3 |
| 11 | 79.9 | 38.6 | 1.8 |
| 12 | 80.4 | 38.4 | 1.3 |
| 13 | 80.3 | 38.4 | 1.7 |
| 14 | 80.6 | 38.8 | 1.5 |
| 15 | 80.4 | 38.5 | 2.4 |

pLDDT 77.1–81.2; JH2–JH1 36.9–37.5 Å; FERM–JH1 38.4–41.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 7 | 41 40 39 39 38 39 39 39 39 39 39 38 38 39 38 | closed-like (< 50) |
