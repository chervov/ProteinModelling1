# TYK2_V678W_20261022_020727 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed5

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 4 | 80.4 | 37.3 | 38.8 | 1.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.6 | 5 | 2 | 80.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.6 | 38.9 | 1.4 |
| 2 (template) | 80.8 | 38.8 | 0.6 |
| 3 (template) | 81.1 | 38.9 | 0.9 |
| 4 | 80.4 | 38.8 | 1.1 |
| 5 | 80.1 | 39.0 | 1.0 |
| 6 | 80.2 | 39.2 | 1.5 |
| 7 | 80.1 | 39.0 | 1.5 |
| 8 | 79.9 | 38.6 | 2.2 |
| 9 | 80.1 | 39.0 | 1.1 |
| 10 | 80.0 | 38.7 | 1.8 |
| 11 | 80.2 | 38.8 | 1.5 |
| 12 | 80.1 | 39.0 | 1.4 |
| 13 | 80.2 | 38.7 | 1.7 |
| 14 | 80.1 | 38.9 | 1.2 |
| 15 | 80.1 | 38.5 | 1.5 |

pLDDT 76.7–81.1; JH2–JH1 37.3–37.7 Å; FERM–JH1 38.5–39.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 39 39 39 39 39 39 39 39 39 39 39 39 39 39 38 | closed-like (< 50) |
