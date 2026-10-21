# TYK2_V678F_20261021_123205 — TYK2 V678F_rel4OLI_msa128-512_s0-7__seed4

TYK2 V678F with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.390, abundance -0.323. activating AND strongly destabilising (abundance near the nonsense anchor). Both accounts predict release, so this is the positive control.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 4; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 4 | 14 | 80.4 | 37.5 | 40.0 | 1.6 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.1 | 4 | 3 | 81.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.8 | 49.0 | 1.6 |
| 2 (template) | 80.3 | 39.3 | 1.2 |
| 3 (template) | 81.0 | 39.8 | 1.1 |
| 4 | 80.2 | 39.5 | 1.8 |
| 5 | 80.4 | 39.4 | 1.6 |
| 6 | 80.2 | 40.0 | 2.1 |
| 7 | 80.3 | 39.7 | 2.1 |
| 8 | 80.1 | 39.9 | 1.7 |
| 9 | 80.3 | 39.6 | 1.7 |
| 10 | 80.1 | 40.1 | 1.8 |
| 11 | 80.3 | 39.5 | 1.8 |
| 12 | 80.3 | 39.6 | 1.5 |
| 13 | 80.2 | 39.5 | 1.9 |
| 14 | 80.4 | 40.0 | 1.6 |
| 15 | 80.0 | 40.4 | 2.2 |

pLDDT 76.8–81.0; JH2–JH1 37.3–37.6 Å; FERM–JH1 39.3–49.0 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 4 | 49 39 40 40 39 40 40 40 40 40 40 40 40 40 40 | closed-like (< 50) |
