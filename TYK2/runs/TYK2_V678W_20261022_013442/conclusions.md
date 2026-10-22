# TYK2_V678W_20261022_013442 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed3

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 4 | 80.6 | 37.3 | 39.5 | 1.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.9 | 3 | 3 | 81.5 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.9 | 47.3 | 1.6 |
| 2 (template) | 80.8 | 39.5 | 1.2 |
| 3 (template) | 81.5 | 39.4 | 0.9 |
| 4 | 80.6 | 39.5 | 1.2 |
| 5 | 80.3 | 39.3 | 1.7 |
| 6 | 80.3 | 39.2 | 1.4 |
| 7 | 80.4 | 39.5 | 1.4 |
| 8 | 80.4 | 39.3 | 1.7 |
| 9 | 80.2 | 39.6 | 1.4 |
| 10 | 80.0 | 39.3 | 1.4 |
| 11 | 80.6 | 39.4 | 1.3 |
| 12 | 80.3 | 39.5 | 1.7 |
| 13 | 80.3 | 39.3 | 1.3 |
| 14 | 80.4 | 39.1 | 1.5 |
| 15 | 80.3 | 39.0 | 1.9 |

pLDDT 76.9–81.5; JH2–JH1 37.3–37.6 Å; FERM–JH1 39.0–47.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 47 40 39 40 39 39 40 39 40 39 39 40 39 39 39 | closed-like (< 50) |
