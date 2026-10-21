# TYK2_V678F_20261021_135442 — TYK2 V678F_rel4OLI_msa128-512_s0-7__seed3

TYK2 V678F with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.390, abundance -0.323. activating AND strongly destabilising (abundance near the nonsense anchor). Both accounts predict release, so this is the positive control.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 9 | 80.4 | 37.9 | 39.3 | 3.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 3 | 1 | 76.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.8 | 40.9 | 1.0 |
| 2 (template) | 80.5 | 39.0 | 1.1 |
| 3 (template) | 81.1 | 39.3 | 1.5 |
| 4 | 80.1 | 38.8 | 1.3 |
| 5 | 80.4 | 38.3 | 1.5 |
| 6 | 80.3 | 38.2 | 1.8 |
| 7 | 80.3 | 38.2 | 1.5 |
| 8 | 80.4 | 38.4 | 2.0 |
| 9 | 80.4 | 39.3 | 3.1 |
| 10 | 79.7 | 38.8 | 1.8 |
| 11 | 80.3 | 38.9 | 1.8 |
| 12 | 80.2 | 39.5 | 2.0 |
| 13 | 79.8 | 39.0 | 2.0 |
| 14 | 79.9 | 39.0 | 2.2 |
| 15 | 80.2 | 39.2 | 2.3 |

pLDDT 76.8–81.1; JH2–JH1 37.0–37.9 Å; FERM–JH1 38.2–40.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 41 39 39 39 38 38 38 38 39 39 39 40 39 39 39 | closed-like (< 50) |
