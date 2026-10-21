# TYK2_20261021_105513 — TYK2 WT_rel4OLI_msa128-512_s0-7__seed3

TYK2 WT with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. wild type reference. wild type, the control: with 4OLI imposed in all recycles it holds the closed state 16/16 at 0.5-2 A, but it has never been run with the template RELEASED, so this run defines the baseline the mutants are judged against.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 7 | 80.3 | 37.4 | 38.6 | 1.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.1 | 3 | 2 | 79.7 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.8 | 42.7 | 1.2 |
| 2 (template) | 79.7 | 40.5 | 1.1 |
| 3 (template) | 81.0 | 40.0 | 1.5 |
| 4 | 80.0 | 39.2 | 1.8 |
| 5 | 80.3 | 38.8 | 1.8 |
| 6 | 80.1 | 39.0 | 1.8 |
| 7 | 80.3 | 38.6 | 1.9 |
| 8 | 79.8 | 38.9 | 2.4 |
| 9 | 80.0 | 38.8 | 3.3 |
| 10 | 79.6 | 38.7 | 2.0 |
| 11 | 80.0 | 38.9 | 2.4 |
| 12 | 79.9 | 38.9 | 2.3 |
| 13 | 80.1 | 39.3 | 2.4 |
| 14 | 79.9 | 38.8 | 2.5 |
| 15 | 79.9 | 39.0 | 2.4 |

pLDDT 76.8–81.0; JH2–JH1 36.8–37.4 Å; FERM–JH1 38.6–42.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 43 40 40 39 39 39 39 39 39 39 39 39 39 39 39 | closed-like (< 50) |
