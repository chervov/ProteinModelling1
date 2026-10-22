# TYK2_V678W_20261022_011048 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed1

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 4 | 80.6 | 37.2 | 40.3 | 1.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 1 | 4 | 80.6 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.0 | 43.8 | 1.8 |
| 2 (template) | 81.0 | 39.7 | 1.1 |
| 3 (template) | 81.0 | 39.5 | 1.4 |
| 4 | 80.6 | 40.3 | 1.0 |
| 5 | 80.5 | 40.2 | 1.5 |
| 6 | 80.5 | 40.2 | 2.0 |
| 7 | 80.1 | 40.6 | 2.3 |
| 8 | 80.6 | 40.2 | 1.7 |
| 9 | 80.4 | 40.2 | 1.4 |
| 10 | 80.5 | 40.5 | 1.5 |
| 11 | 80.3 | 40.3 | 1.6 |
| 12 | 80.4 | 40.7 | 1.6 |
| 13 | 80.4 | 40.4 | 2.3 |
| 14 | 80.3 | 40.5 | 1.6 |
| 15 | 80.4 | 40.4 | 1.6 |

pLDDT 77.0–81.0; JH2–JH1 37.0–37.9 Å; FERM–JH1 39.5–43.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 44 40 40 40 40 40 41 40 40 40 40 41 40 40 40 | closed-like (< 50) |
