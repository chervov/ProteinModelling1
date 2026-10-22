# TYK2_V678W_20261022_020528 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed4

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 4; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 4 | 4 | 80.1 | 37.2 | 39.2 | 1.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.7 | 4 | 3 | 80.3 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.3 | 39.7 | 1.2 |
| 2 (template) | 79.4 | 38.4 | 0.9 |
| 3 (template) | 80.3 | 38.6 | 0.7 |
| 4 | 80.1 | 39.2 | 1.3 |
| 5 | 79.5 | 39.0 | 1.6 |
| 6 | 79.4 | 39.0 | 1.8 |
| 7 | 79.7 | 38.9 | 1.8 |
| 8 | 79.3 | 38.8 | 1.9 |
| 9 | 79.5 | 38.9 | 1.6 |
| 10 | 79.6 | 38.8 | 1.3 |
| 11 | 79.6 | 39.1 | 1.6 |
| 12 | 79.5 | 38.3 | 1.5 |
| 13 | 79.9 | 38.5 | 1.5 |
| 14 | 79.8 | 38.6 | 1.8 |
| 15 | 79.7 | 38.4 | 1.6 |

pLDDT 76.3–80.3; JH2–JH1 37.1–37.4 Å; FERM–JH1 38.3–39.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 4 | 40 38 39 39 39 39 39 39 39 39 39 38 38 39 38 | closed-like (< 50) |
