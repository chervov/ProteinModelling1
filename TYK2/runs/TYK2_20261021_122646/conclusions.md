# TYK2_20261021_122646 — TYK2 WT_rel4OLI_msa128-512_s0-7__seed6

TYK2 WT with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. wild type reference. wild type, the control: with 4OLI imposed in all recycles it holds the closed state 16/16 at 0.5-2 A, but it has never been run with the template RELEASED, so this run defines the baseline the mutants are judged against.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 6; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 2 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 6 | 4 | 80.8 | 37.1 | 38.6 | 1.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 6 | 2 | 80.6 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 78.2 | 39.8 | 2.1 |
| 2 (template) | 80.6 | 39.0 | 0.8 |
| 3 (template) | 81.2 | 39.1 | 1.1 |
| 4 | 80.8 | 38.6 | 1.3 |
| 5 | 80.6 | 39.1 | 1.9 |
| 6 | 80.3 | 38.9 | 1.4 |
| 7 | 80.4 | 38.8 | 2.1 |
| 8 | 80.7 | 39.4 | 1.5 |
| 9 | 80.3 | 39.3 | 1.5 |
| 10 | 80.6 | 39.1 | 1.8 |
| 11 | 80.4 | 39.5 | 1.6 |
| 12 | 80.6 | 39.5 | 1.4 |
| 13 | 80.5 | 39.2 | 1.6 |
| 14 | 80.5 | 39.0 | 1.5 |
| 15 | 80.3 | 39.1 | 1.5 |

pLDDT 78.2–81.2; JH2–JH1 36.9–37.5 Å; FERM–JH1 38.6–39.8 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 6 | 40 39 39 39 39 39 39 39 39 39 40 40 39 39 39 | closed-like (< 50) |
