# TYK2_V678W_20261022_005856 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed0

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 80.9 | 37.3 | 38.7 | 0.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 0 | 2 | 80.1 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.4 | 42.9 | 1.7 |
| 2 (template) | 80.1 | 39.3 | 0.8 |
| 3 (template) | 81.6 | 38.7 | 1.0 |
| 4 | 80.9 | 38.7 | 0.9 |
| 5 | 80.3 | 38.8 | 1.4 |
| 6 | 80.4 | 38.9 | 1.3 |
| 7 | 80.2 | 39.3 | 1.7 |
| 8 | 80.1 | 38.9 | 1.6 |
| 9 | 80.4 | 38.9 | 1.5 |
| 10 | 80.2 | 38.6 | 1.3 |
| 11 | 80.3 | 38.6 | 1.4 |
| 12 | 80.3 | 38.9 | 1.2 |
| 13 | 80.4 | 38.8 | 1.6 |
| 14 | 80.6 | 39.1 | 1.5 |
| 15 | 80.4 | 38.8 | 1.4 |

pLDDT 76.4–81.6; JH2–JH1 37.1–37.5 Å; FERM–JH1 38.6–42.9 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 43 39 39 39 39 39 39 39 39 39 39 39 39 39 39 | closed-like (< 50) |
