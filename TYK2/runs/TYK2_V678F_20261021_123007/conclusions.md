# TYK2_V678F_20261021_123007 — TYK2 V678F_rel4OLI_msa128-512_s0-7__seed3

TYK2 V678F with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.390, abundance -0.323. activating AND strongly destabilising (abundance near the nonsense anchor). Both accounts predict release, so this is the positive control.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 6 | 80.5 | 37.2 | 38.7 | 2.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 3 | 1 | 77.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.0 | 41.8 | 1.0 |
| 2 (template) | 80.1 | 39.4 | 1.4 |
| 3 (template) | 80.8 | 38.9 | 1.2 |
| 4 | 79.6 | 38.9 | 1.7 |
| 5 | 80.2 | 38.8 | 1.8 |
| 6 | 80.5 | 38.7 | 2.1 |
| 7 | 80.2 | 39.5 | 2.2 |
| 8 | 80.1 | 39.5 | 2.3 |
| 9 | 80.2 | 38.7 | 1.6 |
| 10 | 80.0 | 39.2 | 2.5 |
| 11 | 80.1 | 39.4 | 2.3 |
| 12 | 80.1 | 39.6 | 2.2 |
| 13 | 80.1 | 39.7 | 2.7 |
| 14 | 80.0 | 39.5 | 2.9 |
| 15 | 79.9 | 39.3 | 2.4 |

pLDDT 77.0–80.8; JH2–JH1 36.9–37.8 Å; FERM–JH1 38.7–41.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 42 39 39 39 39 39 40 40 39 39 39 40 40 40 39 | closed-like (< 50) |
