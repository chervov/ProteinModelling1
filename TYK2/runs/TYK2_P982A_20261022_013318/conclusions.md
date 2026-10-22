# TYK2_P982A_20261022_013318 — TYK2 P982A_rel4OLI_msa128-512_s0-7__seed1

TYK2 P982A with 4OLI imposed in recycles 1-3 then released, MSA 128/512, seeds 0-7. THE POSITIVE CONTROL THE RELEASE ASSAY LACKS. P982 is the only TRUE JH2-JH1 interface residue in the variant set - it buries 59.8 A^2 across the closed contact, while every V678 substitution buries 0.0 A^2 there and all of them held the closed state perfectly. P982A has been run template-free at four depths (null everywhere) but NEVER with a template, so we have only asked whether it prevents FINDING the closed state, never whether it destabilises the closed state once given. Measured DMS: IFN-alpha -0.321 (mild loss), abundance -0.230

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 1; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 12 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to TYK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 537, "identity_aligned": 0.996, "query_range": [579, 1177]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 1 | 4 | 80.5 | 37.3 | 38.9 | 1.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 1.0 | 1 | 8 | 79.8 | 15 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 (template) | 76.4 | 42.5 | 1.7 |
| 2 (template) | 80.8 | 39.1 | 1.3 |
| 3 (template) | 81.0 | 38.3 | 1.7 |
| 4 | 80.6 | 38.9 | 1.2 |
| 5 | 80.0 | 39.1 | 1.7 |
| 6 | 80.2 | 39.7 | 2.7 |
| 7 | 79.8 | 38.9 | 2.2 |
| 8 | 79.8 | 39.8 | 1.0 |
| 9 | 80.1 | 38.8 | 1.4 |
| 10 | 80.1 | 39.1 | 1.6 |
| 11 | 79.9 | 39.1 | 1.2 |
| 12 | 80.1 | 38.9 | 1.3 |
| 13 | 80.3 | 38.9 | 1.7 |
| 14 | 79.7 | 39.1 | 1.7 |
| 15 | 80.0 | 38.3 | 2.8 |

pLDDT 76.4–81.0; JH2–JH1 37.0–37.7 Å; FERM–JH1 38.3–42.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 15.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 1 | 42 39 38 39 39 40 39 40 39 39 39 39 39 39 38 | closed-like (< 50) |
