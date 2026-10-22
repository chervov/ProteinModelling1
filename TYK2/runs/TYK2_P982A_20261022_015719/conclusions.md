# TYK2_P982A_20261022_015719 — TYK2 P982A_rel4OLI_msa128-512_s0-7__seed3

TYK2 P982A with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. THE POSITIVE CONTROL THE RELEASE ASSAY LACKS. P982 is the only TRUE JH2-JH1 interface residue in the variant set - it buries 59.8 A^2 across the closed contact, while every V678 substitution buries 0.0 A^2 there and all of them held the closed state perfectly. P982A has been run template-free at four depths (null everywhere) but NEVER with a template, so we have only asked whether it prevents FINDING the closed state, never whether it destabilises the closed state once given. Measured DMS: IFN-alpha -0.321 (mild loss), abundance -0.230

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 3; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 3 | 5 | 80.5 | 37.3 | 38.9 | 1.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.4 | 3 | 1 | 76.7 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.7 | 42.3 | 1.4 |
| 2 (template) | 80.4 | 39.1 | 2.1 |
| 3 (template) | 80.7 | 38.4 | 1.9 |
| 4 | 79.9 | 38.9 | 2.0 |
| 5 | 80.5 | 38.9 | 1.9 |
| 6 | 80.0 | 39.8 | 2.1 |
| 7 | 80.5 | 40.8 | 1.9 |
| 8 | 80.1 | 39.8 | 2.6 |
| 9 | 80.1 | 40.1 | 2.4 |
| 10 | 79.0 | 38.0 | 5.1 |
| 11 | 80.2 | 40.4 | 2.3 |
| 12 | 80.0 | 39.5 | 3.7 |
| 13 | 80.2 | 39.3 | 2.7 |
| 14 | 80.1 | 39.9 | 3.0 |
| 15 | 80.3 | 39.2 | 2.4 |

pLDDT 76.7–80.7; JH2–JH1 37.1–37.8 Å; FERM–JH1 38.0–42.3 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 3 | 42 39 38 39 39 40 41 40 40 38 40 40 39 40 39 | closed-like (< 50) |
