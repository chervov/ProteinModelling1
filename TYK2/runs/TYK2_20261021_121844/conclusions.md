# TYK2_20261021_121844 — TYK2 WT_rel4OLI_msa128-512_s0-7__seed2

TYK2 WT with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. wild type reference. wild type, the control: with 4OLI imposed in all recycles it holds the closed state 16/16 at 0.5-2 A, but it has never been run with the template RELEASED, so this run defines the baseline the mutants are judged against.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 2; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 2 | 5 | 80.3 | 37.3 | 38.6 | 1.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.4 | 2 | 2 | 79.6 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.1 | 40.6 | 1.6 |
| 2 (template) | 79.6 | 38.6 | 1.4 |
| 3 (template) | 80.4 | 38.0 | 1.4 |
| 4 | 80.1 | 38.6 | 1.6 |
| 5 | 80.3 | 38.6 | 1.7 |
| 6 | 80.2 | 38.5 | 2.2 |
| 7 | 79.8 | 38.8 | 2.2 |
| 8 | 79.8 | 38.7 | 2.3 |
| 9 | 80.0 | 38.7 | 2.2 |
| 10 | 79.9 | 38.5 | 2.2 |
| 11 | 80.3 | 38.6 | 2.3 |
| 12 | 80.0 | 38.3 | 1.6 |
| 13 | 80.1 | 38.3 | 2.5 |
| 14 | 79.9 | 38.5 | 2.0 |
| 15 | 80.2 | 38.7 | 1.9 |

pLDDT 76.1–80.4; JH2–JH1 36.9–37.3 Å; FERM–JH1 38.0–40.6 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 2 | 41 39 38 39 39 38 39 39 39 38 39 38 38 38 39 | closed-like (< 50) |
