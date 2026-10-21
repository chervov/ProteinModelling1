# TYK2_20261021_122246 — TYK2 WT_rel4OLI_msa128-512_s0-7__seed4

TYK2 WT with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. wild type reference. wild type, the control: with 4OLI imposed in all recycles it holds the closed state 16/16 at 0.5-2 A, but it has never been run with the template RELEASED, so this run defines the baseline the mutants are judged against.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 4; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 4 | 4 | 81.0 | 37.4 | 38.7 | 0.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.7 | 4 | 2 | 79.3 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.7 | 39.5 | 1.6 |
| 2 (template) | 79.3 | 38.9 | 0.7 |
| 3 (template) | 80.9 | 39.5 | 0.9 |
| 4 | 81.0 | 38.7 | 0.7 |
| 5 | 80.8 | 38.9 | 0.9 |
| 6 | 80.5 | 39.0 | 1.5 |
| 7 | 80.4 | 39.2 | 1.2 |
| 8 | 80.4 | 38.9 | 1.0 |
| 9 | 80.4 | 39.0 | 1.0 |
| 10 | 80.2 | 38.7 | 1.7 |
| 11 | 80.5 | 38.6 | 1.2 |
| 12 | 80.6 | 38.8 | 0.8 |
| 13 | 80.8 | 38.7 | 1.0 |
| 14 | 80.7 | 38.7 | 1.2 |
| 15 | 80.6 | 38.7 | 0.8 |

pLDDT 76.7–81.0; JH2–JH1 37.0–37.5 Å; FERM–JH1 38.6–39.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 4 | 40 39 40 39 39 39 39 39 39 39 39 39 39 39 39 | closed-like (< 50) |
