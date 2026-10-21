# TYK2_20261021_094916 — TYK2 WT_rel4OLI_msa128-512_s0-7__seed1

TYK2 WT with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. wild type reference. wild type, the control: with 4OLI imposed in all recycles it holds the closed state 16/16 at 0.5-2 A, but it has never been run with the template RELEASED, so this run defines the baseline the mutants are judged against.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 4 | 80.4 | 37.3 | 38.6 | 1.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.2 | 1 | 9 | 80.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.6 | 50.6 | 1.9 |
| 2 (template) | 79.6 | 39.4 | 1.5 |
| 3 (template) | 81.0 | 38.8 | 1.8 |
| 4 | 80.4 | 38.6 | 1.3 |
| 5 | 80.1 | 38.4 | 1.7 |
| 6 | 80.0 | 38.6 | 2.0 |
| 7 | 79.7 | 38.2 | 2.0 |
| 8 | 79.9 | 38.1 | 1.6 |
| 9 | 80.0 | 38.3 | 1.2 |
| 10 | 79.9 | 38.3 | 1.4 |
| 11 | 79.9 | 38.8 | 1.6 |
| 12 | 80.2 | 38.4 | 1.5 |
| 13 | 79.8 | 38.6 | 1.4 |
| 14 | 80.1 | 38.3 | 1.8 |
| 15 | 79.8 | 38.3 | 1.4 |

pLDDT 76.6–81.0; JH2–JH1 36.9–37.5 Å; FERM–JH1 38.1–50.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 51 39 39 39 38 39 38 38 38 38 39 38 39 38 38 | closed-like (< 50) |
