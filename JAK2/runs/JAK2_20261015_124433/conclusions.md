# JAK2_20261015_124433 — JAK2 experiment E_4templates_msa32-64

As experiment C (4 templates in all recycles) with an even shallower MSA (32 clusters / 64 extra).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 32 clusters / 64 extra; templates: PDB 4OLI chain A + Shan 2014 JAK2 model (JH2–JH1) + PDB 6E2Q chain A + ModelArchive ma-l9b1f (all recycles). Run time 38 min (whole notebook incl. setup, RTX PRO 6000).

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
| 0 | 15 | 86.0 | 40.0 | 41.4 | 81.9 | 7.1 | 3.3 | 2.0 | template ModelArchive ma-l9b1f |
| 1 | 15 | 86.3 | 40.0 | 41.7 | 81.8 | 7.0 | 3.1 | 2.1 | template ModelArchive ma-l9b1f |
| 2 | 12 | 86.0 | 40.1 | 41.5 | 81.9 | 7.1 | 3.3 | 2.0 | template ModelArchive ma-l9b1f |
| 3 | 14 | 86.0 | 40.2 | 41.4 | 82.1 | 7.0 | 3.3 | 2.2 | template ModelArchive ma-l9b1f |
| 4 | 15 | 86.5 | 39.9 | 41.6 | 81.7 | 7.2 | 3.2 | 1.9 | template ModelArchive ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 81.7 | 1 | 6 | 83.6 | 0 |
| Shan 2014 (closed, JH2–JH1) | 6.6 | 1 | 6 | 83.6 | 75 |
| template PDB 4OLI chain A (mapped) | 2.7 | 1 | 6 | 83.6 | 75 |
| template ModelArchive ma-l9b1f (mapped) | 1.6 | 4 | 2 | 83.9 | 75 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 | vs template PDB 4OLI chain A | vs template ModelArchive ma-l9b1f |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 82.9 | 41.9 | 82.2 | 7.2 | 3.4 | 2.0 |
| 2 | 84.5 | 41.4 | 81.9 | 7.2 | 3.3 | 1.9 |
| 3 | 84.8 | 41.5 | 82.0 | 7.3 | 3.4 | 2.0 |
| 4 | 85.0 | 41.5 | 81.8 | 7.2 | 3.2 | 2.0 |
| 5 | 85.4 | 41.6 | 81.9 | 7.1 | 3.2 | 2.1 |
| 6 | 84.1 | 41.4 | 82.0 | 6.9 | 3.2 | 2.3 |
| 7 | 84.2 | 41.3 | 81.9 | 7.0 | 3.1 | 2.2 |
| 8 | 85.6 | 41.3 | 81.9 | 7.1 | 3.3 | 2.0 |
| 9 | 85.2 | 41.4 | 82.0 | 7.2 | 3.4 | 2.0 |
| 10 | 83.7 | 41.5 | 82.0 | 7.1 | 3.3 | 2.1 |
| 11 | 85.9 | 41.3 | 81.9 | 7.2 | 3.3 | 2.0 |
| 12 | 86.0 | 41.4 | 81.9 | 7.1 | 3.3 | 2.0 |
| 13 | 85.5 | 41.6 | 81.9 | 7.2 | 3.3 | 2.0 |
| 14 | 85.9 | 41.5 | 81.9 | 7.1 | 3.2 | 2.0 |
| 15 | 86.0 | 41.5 | 81.8 | 7.1 | 3.2 | 2.0 |

pLDDT 81.5–86.5; JH2–JH1 39.9–40.6 Å; FERM–JH1 41.1–42.0 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: template ModelArchive ma-l9b1f 75.
