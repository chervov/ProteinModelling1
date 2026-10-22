# TYK2_V678W_20261022_021927 — TYK2 V678W_rel4OLI_msa128-512_s0-7__seed6

TYK2 V678W with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. measured IFN-alpha +0.227, abundance -0.361. most destabilising substitution at the position but only weakly activating. Foldability predicts release; function predicts it holds better than M or I.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 6; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 6 | 4 | 80.7 | 37.3 | 39.6 | 2.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.7 | 6 | 2 | 80.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 78.3 | 41.2 | 3.9 |
| 2 (template) | 80.8 | 40.1 | 1.7 |
| 3 (template) | 81.5 | 39.6 | 2.2 |
| 4 | 80.6 | 39.6 | 2.3 |
| 5 | 80.4 | 40.6 | 1.9 |
| 6 | 80.2 | 40.0 | 1.9 |
| 7 | 80.4 | 39.8 | 2.0 |
| 8 | 80.5 | 39.7 | 1.8 |
| 9 | 80.3 | 40.2 | 1.8 |
| 10 | 80.4 | 39.1 | 1.9 |
| 11 | 80.2 | 39.7 | 2.0 |
| 12 | 80.5 | 40.3 | 1.9 |
| 13 | 80.4 | 40.1 | 1.7 |
| 14 | 80.4 | 39.8 | 1.9 |
| 15 | 80.1 | 39.4 | 2.1 |

pLDDT 78.3–81.5; JH2–JH1 37.1–37.6 Å; FERM–JH1 39.1–41.2 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 6 | 41 40 40 40 41 40 40 40 40 39 40 40 40 40 39 | closed-like (< 50) |
