# TYK2_V678F_20261021_095301 — TYK2 V678F_rel4OLI_msa128-512_s0-7__seed0

TYK2 V678F with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.390, abundance -0.323. activating AND strongly destabilising (abundance near the nonsense anchor). Both accounts predict release, so this is the positive control.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 17 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 80.8 | 37.1 | 39.1 | 1.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.5 | 0 | 2 | 81.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 78.7 | 42.1 | 1.8 |
| 2 (template) | 81.8 | 40.0 | 0.5 |
| 3 (template) | 81.5 | 39.3 | 1.4 |
| 4 | 80.8 | 39.1 | 1.3 |
| 5 | 80.6 | 39.4 | 1.9 |
| 6 | 80.5 | 39.3 | 1.7 |
| 7 | 80.1 | 39.9 | 1.6 |
| 8 | 80.3 | 39.0 | 1.6 |
| 9 | 80.5 | 39.2 | 1.5 |
| 10 | 80.6 | 39.4 | 1.9 |
| 11 | 80.5 | 38.8 | 1.3 |
| 12 | 80.8 | 40.0 | 1.5 |
| 13 | 80.6 | 39.2 | 2.3 |
| 14 | 80.5 | 39.3 | 1.5 |
| 15 | 80.4 | 39.2 | 1.6 |

pLDDT 78.7–81.8; JH2–JH1 37.1–37.5 Å; FERM–JH1 38.8–42.1 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 42 40 39 39 39 39 40 39 39 39 39 40 39 39 39 | closed-like (< 50) |
