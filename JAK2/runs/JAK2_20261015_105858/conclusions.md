# JAK2_20261015_105858 — JAK2 experiment C_4templates_msa-default

Option 1 of possible_improvements.md: better templates for the closed JAK2, used in all recycles: TYK2 JH2–JH1 crystal structure (PDB 4OLI, autoinhibited interface), Shan 2014 JAK2 JH2–JH1 model (identical sequence), JAK2 FERM–SH2 crystal structure (PDB 6E2Q chain A) and the JAK1 closed model ma-l9b1f (FERM–JH1 placement).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA model_1 default 512/5120; templates: PDB 4OLI chain A + Shan 2014 JAK2 model (JH2–JH1) + PDB 6E2Q chain A + ModelArchive ma-l9b1f (all recycles). Run time 64 min (whole notebook incl. setup, RTX PRO 6000).

Template identity to JAK2: `{"PDB 4OLI chain A": {"observed_residues": 539, "aligned": 539, "identical": 266, "identity_aligned": 0.494, "query_range": [535, 1131]}, "Shan 2014 JAK2 model (JH2\u2013JH1)": {"observed_residues": 612, "aligned": 612, "identical": 612, "identity_aligned": 1.0, "query_range": [520, 1131]}, "PDB 6E2Q chain A": {"observed_residues": 473, "aligned": 473, "identical": 471, "identity_aligned": 0.996, "query_range": [35, 515]}, "ModelArchive ma-l9b1f": {"observed_residues": 1154, "aligned": 1076, "identical": 508, "identity_aligned": 0.472, "query_range": [1, 1128]}}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |
| template PDB 4OLI chain A (mapped) | 39.2 | nan |
| template ModelArchive ma-l9b1f (mapped) | 39.8 | 42.0 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | vs template PDB 4OLI chain A | vs template ModelArchive ma-l9b1f | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 12 | 86.7 | 39.4 | 43.6 | 81.9 | 7.3 | 3.6 | 2.5 | template ModelArchive ma-l9b1f |
| 1 | 10 | 86.8 | 39.4 | 43.8 | 81.7 | 6.8 | 3.1 | 2.6 | template ModelArchive ma-l9b1f |
| 2 | 10 | 86.9 | 39.3 | 43.7 | 81.8 | 6.8 | 3.3 | 2.7 | template ModelArchive ma-l9b1f |
| 3 | 10 | 86.7 | 39.3 | 43.7 | 81.7 | 6.9 | 3.2 | 2.6 | template ModelArchive ma-l9b1f |
| 4 | 10 | 86.8 | 39.3 | 43.7 | 81.8 | 7.1 | 3.5 | 2.5 | template ModelArchive ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 81.6 | 0 | 5 | 86.5 | 0 |
| Shan 2014 (closed, JH2–JH1) | 6.7 | 0 | 14 | 86.6 | 75 |
| template PDB 4OLI chain A (mapped) | 3.1 | 0 | 4 | 86.6 | 75 |
| template ModelArchive ma-l9b1f (mapped) | 2.2 | 0 | 1 | 85.0 | 75 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 | vs template PDB 4OLI chain A | vs template ModelArchive ma-l9b1f |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 85.1 | 44.3 | 82.3 | 7.4 | 4.0 | 2.4 |
| 2 | 86.0 | 43.6 | 82.0 | 7.1 | 3.6 | 2.7 |
| 3 | 86.3 | 43.4 | 82.0 | 7.2 | 3.7 | 2.6 |
| 4 | 86.5 | 43.9 | 81.7 | 6.8 | 3.2 | 2.7 |
| 5 | 86.5 | 43.7 | 81.8 | 7.0 | 3.4 | 2.6 |
| 6 | 86.5 | 43.7 | 81.8 | 7.0 | 3.4 | 2.6 |
| 7 | 86.5 | 43.6 | 81.8 | 7.1 | 3.5 | 2.6 |
| 8 | 86.5 | 43.6 | 81.8 | 7.0 | 3.5 | 2.6 |
| 9 | 86.6 | 43.6 | 81.8 | 7.1 | 3.5 | 2.6 |
| 10 | 86.8 | 43.8 | 81.7 | 6.9 | 3.3 | 2.6 |
| 11 | 86.6 | 43.5 | 81.9 | 7.2 | 3.6 | 2.6 |
| 12 | 86.7 | 43.5 | 82.0 | 7.3 | 3.7 | 2.6 |
| 13 | 86.6 | 43.5 | 81.8 | 7.0 | 3.5 | 2.6 |
| 14 | 86.7 | 43.5 | 81.9 | 7.1 | 3.6 | 2.6 |
| 15 | 86.7 | 43.5 | 81.8 | 7.1 | 3.5 | 2.6 |

pLDDT 85.0–86.9; JH2–JH1 39.2–40.1 Å; FERM–JH1 43.2–44.8 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: template ModelArchive ma-l9b1f 75.

## Interpretation
- **Closed in all seeds and recycles**, very stable: FERM–JH1 43.2–44.8 Å throughout, all 75 conformations nearest to
  the JAK1 closed template, none within 80 Å of the open AF2 model.
- **Highest confidence so far for the closed JAK2:** pLDDT 86.7–86.9 for the selected structures (single ma-l9b1f
  template: ~86.5; template switched off after recycle 3: ~85.7).
- **The four templates are mutually consistent:** the structures are 2.5–2.7 Å from ma-l9b1f and 3.1–3.6 Å from the
  experimental TYK2 JH2–JH1 crystal structure 4OLI (mapped to JAK2) — the modelled JAK1 closed arrangement and the
  experimental autoinhibited TYK2 interface agree.
- **But not closer to Shan's JAK2 model** (6.8–7.3 Å) than with ma-l9b1f alone (6.6–6.8 Å) or after template release
  (6.0–6.9 Å), even though Shan's JAK2 model was one of the templates and has the identical sequence. The network follows
  the full-length template (ma-l9b1f) and the experimental 4OLI interface rather than Shan's JH2–JH1 model.
