# TYK2_20261021_122845 — TYK2 WT_rel4OLI_msa128-512_s0-7__seed7

TYK2 WT with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. wild type reference. wild type, the control: with 4OLI imposed in all recycles it holds the closed state 16/16 at 0.5-2 A, but it has never been run with the template RELEASED, so this run defines the baseline the mutants are judged against.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 7; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 7 | 4 | 80.7 | 37.5 | 40.2 | 1.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.6 | 7 | 2 | 80.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 77.1 | 46.6 | 1.4 |
| 2 (template) | 80.8 | 40.8 | 0.6 |
| 3 (template) | 81.0 | 40.4 | 0.9 |
| 4 | 80.7 | 40.2 | 1.0 |
| 5 | 80.4 | 39.6 | 1.8 |
| 6 | 80.4 | 40.0 | 1.5 |
| 7 | 80.1 | 40.8 | 2.1 |
| 8 | 80.4 | 40.9 | 2.3 |
| 9 | 80.3 | 39.8 | 1.6 |
| 10 | 80.1 | 39.9 | 2.2 |
| 11 | 80.2 | 40.1 | 1.4 |
| 12 | 80.1 | 40.0 | 1.5 |
| 13 | 80.6 | 39.9 | 1.6 |
| 14 | 80.5 | 40.8 | 1.8 |
| 15 | 80.2 | 40.2 | 1.6 |

pLDDT 77.1–81.0; JH2–JH1 37.0–37.8 Å; FERM–JH1 39.6–46.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 7 | 47 41 40 40 40 40 41 41 40 40 40 40 40 41 40 | closed-like (< 50) |
