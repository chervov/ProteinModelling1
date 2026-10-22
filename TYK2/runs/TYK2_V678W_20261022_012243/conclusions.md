# TYK2_V678W_20261022_012243 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed2

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 11 | 80.2 | 37.3 | 38.6 | 2.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.1 | 2 | 3 | 81.3 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.1 | 39.4 | 1.7 |
| 2 (template) | 80.8 | 38.9 | 1.5 |
| 3 (template) | 81.3 | 39.0 | 1.1 |
| 4 | 80.1 | 38.4 | 1.6 |
| 5 | 80.1 | 38.3 | 1.7 |
| 6 | 80.0 | 38.5 | 1.8 |
| 7 | 79.9 | 38.3 | 1.7 |
| 8 | 79.8 | 38.4 | 1.7 |
| 9 | 79.8 | 39.1 | 1.6 |
| 10 | 80.0 | 38.5 | 1.9 |
| 11 | 80.2 | 38.6 | 2.1 |
| 12 | 80.0 | 38.3 | 2.4 |
| 13 | 80.0 | 38.0 | 2.9 |
| 14 | 79.9 | 38.6 | 2.1 |
| 15 | 80.0 | 38.4 | 2.3 |

pLDDT 77.1–81.3; JH2–JH1 36.9–37.6 Å; FERM–JH1 38.0–39.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 39 39 39 38 38 38 38 38 39 38 39 38 38 39 38 | closed-like (< 50) |
