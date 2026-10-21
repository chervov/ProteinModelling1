# TYK2_V678F_20261021_122608 — TYK2 V678F_rel4OLI_msa128-512_s0-7__seed1

TYK2 V678F with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.390, abundance -0.323. activating AND strongly destabilising (abundance near the nonsense anchor). Both accounts predict release, so this is the positive control.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 6 | 80.4 | 37.3 | 38.8 | 1.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.9 | 1 | 3 | 81.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.9 | 36.4 | 2.1 |
| 2 (template) | 80.9 | 38.7 | 1.1 |
| 3 (template) | 81.0 | 37.8 | 0.9 |
| 4 | 80.1 | 38.2 | 1.2 |
| 5 | 80.0 | 38.6 | 1.8 |
| 6 | 80.4 | 38.8 | 1.9 |
| 7 | 79.6 | 43.1 | 2.1 |
| 8 | 79.8 | 38.1 | 1.9 |
| 9 | 80.0 | 38.4 | 1.7 |
| 10 | 79.9 | 39.2 | 1.9 |
| 11 | 79.9 | 38.4 | 1.8 |
| 12 | 80.0 | 38.4 | 1.8 |
| 13 | 80.1 | 39.2 | 2.7 |
| 14 | 79.9 | 38.5 | 1.5 |
| 15 | 79.7 | 38.4 | 2.3 |

pLDDT 76.9–81.0; JH2–JH1 37.0–38.0 Å; FERM–JH1 36.4–43.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 36 39 38 38 39 39 43 38 38 39 38 38 39 38 38 | closed-like (< 50) |
