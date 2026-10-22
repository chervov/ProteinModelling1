# TYK2_P982A_20261022_030225 — TYK2 P982A_rel4OLI_msa128-512_s0-7__seed5

TYK2 P982A with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. THE POSITIVE CONTROL THE RELEASE ASSAY LACKS. P982 is the only TRUE JH2-JH1 interface residue in the variant set - it buries 59.8 A^2 across the closed contact, while every V678 substitution buries 0.0 A^2 there and all of them held the closed state perfectly. P982A has been run template-free at four depths (null everywhere) but NEVER with a template, so we have only asked whether it prevents FINDING the closed state, never whether it destabilises the closed state once given. Measured DMS: IFN-alpha -0.321 (mild loss), abundance -0.230

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 5; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 5 | 4 | 80.2 | 37.2 | 38.9 | 1.0 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.8 | 5 | 2 | 80.0 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 75.8 | 44.4 | 1.3 |
| 2 (template) | 80.0 | 40.2 | 0.8 |
| 3 (template) | 81.0 | 39.4 | 1.2 |
| 4 | 80.2 | 38.9 | 1.0 |
| 5 | 79.7 | 39.6 | 1.5 |
| 6 | 79.9 | 39.4 | 1.4 |
| 7 | 79.6 | 39.1 | 1.3 |
| 8 | 80.0 | 39.3 | 1.5 |
| 9 | 79.9 | 39.0 | 1.4 |
| 10 | 79.8 | 39.1 | 1.5 |
| 11 | 79.7 | 39.7 | 1.6 |
| 12 | 79.8 | 39.3 | 1.2 |
| 13 | 79.7 | 39.2 | 1.5 |
| 14 | 79.8 | 38.5 | 1.7 |
| 15 | 79.8 | 39.4 | 0.9 |

pLDDT 75.8–81.0; JH2–JH1 36.9–37.7 Å; FERM–JH1 38.5–44.4 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 5 | 44 40 39 39 40 39 39 39 39 39 40 39 39 38 39 | closed-like (< 50) |
