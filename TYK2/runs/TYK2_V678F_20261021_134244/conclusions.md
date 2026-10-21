# TYK2_V678F_20261021_134244 — TYK2 V678F_rel4OLI_msa128-512_s0-7__seed2

TYK2 V678F with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.390, abundance -0.323. activating AND strongly destabilising (abundance near the nonsense anchor). Both accounts predict release, so this is the positive control.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 15 | 80.4 | 37.4 | 39.0 | 1.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 2 | 4 | 80.3 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.4 | 41.3 | 3.3 |
| 2 (template) | 80.2 | 38.4 | 1.2 |
| 3 (template) | 80.8 | 38.5 | 1.0 |
| 4 | 80.3 | 38.1 | 1.0 |
| 5 | 80.3 | 38.4 | 1.5 |
| 6 | 80.1 | 38.5 | 1.3 |
| 7 | 80.0 | 38.4 | 1.4 |
| 8 | 80.0 | 38.4 | 1.4 |
| 9 | 79.8 | 38.3 | 1.4 |
| 10 | 80.1 | 38.5 | 1.4 |
| 11 | 80.4 | 39.3 | 1.5 |
| 12 | 80.3 | 38.7 | 1.8 |
| 13 | 80.3 | 39.3 | 2.1 |
| 14 | 80.0 | 39.6 | 1.9 |
| 15 | 80.4 | 39.0 | 1.7 |

pLDDT 77.4–80.8; JH2–JH1 37.0–37.6 Å; FERM–JH1 38.1–41.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 41 38 38 38 38 38 38 38 38 38 39 39 39 40 39 | closed-like (< 50) |
