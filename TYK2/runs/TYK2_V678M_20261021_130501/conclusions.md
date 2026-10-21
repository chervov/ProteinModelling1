# TYK2_V678M_20261021_130501 — TYK2 V678M_rel4OLI_msa128-512_s0-7__seed2

TYK2 V678M with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.561, abundance +0.002. strongest measured activator at the position (97th percentile) with protein abundance untouched. THE DISCRIMINATING CASE: if the method has functional sensitivity it should release the closed state; if it tracks foldability it should hold like wild type.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 4 | 80.5 | 37.0 | 39.1 | 1.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 2 | 3 | 81.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.3 | 41.6 | 1.7 |
| 2 (template) | 80.9 | 39.3 | 1.5 |
| 3 (template) | 81.0 | 38.8 | 1.0 |
| 4 | 80.5 | 39.1 | 1.1 |
| 5 | 80.3 | 39.1 | 1.4 |
| 6 | 80.2 | 39.2 | 1.4 |
| 7 | 80.0 | 39.1 | 1.6 |
| 8 | 80.2 | 39.0 | 2.1 |
| 9 | 80.3 | 39.3 | 1.6 |
| 10 | 80.2 | 39.3 | 1.7 |
| 11 | 80.4 | 39.4 | 1.9 |
| 12 | 80.1 | 39.0 | 1.1 |
| 13 | 80.4 | 39.1 | 1.6 |
| 14 | 80.4 | 39.0 | 1.6 |
| 15 | 80.4 | 39.2 | 1.4 |

pLDDT 77.3–81.0; JH2–JH1 37.0–37.5 Å; FERM–JH1 38.8–41.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 42 39 39 39 39 39 39 39 39 39 39 39 39 39 39 | closed-like (< 50) |
