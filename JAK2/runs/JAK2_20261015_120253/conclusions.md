# JAK2_20261015_120253 — JAK2 experiment D_4templates_msa128-512

As experiment C (4 templates in all recycles) with a shallower MSA (128 clusters / 512 extra).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A + Shan 2014 JAK2 model (JH2–JH1) + PDB 6E2Q chain A + ModelArchive ma-l9b1f (all recycles). Run time 42 min (whole notebook incl. setup, RTX PRO 6000).

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
| 0 | 9 | 86.2 | 39.5 | 41.9 | 81.6 | 7.9 | 3.7 | 1.7 | template ModelArchive ma-l9b1f |
| 1 | 7 | 86.3 | 39.6 | 42.0 | 81.7 | 7.8 | 3.8 | 1.8 | template ModelArchive ma-l9b1f |
| 2 | 13 | 86.1 | 39.6 | 41.8 | 81.7 | 8.1 | 3.9 | 1.7 | template ModelArchive ma-l9b1f |
| 3 | 11 | 86.1 | 39.6 | 42.0 | 81.8 | 8.1 | 4.0 | 1.8 | template ModelArchive ma-l9b1f |
| 4 | 12 | 86.2 | 39.6 | 42.1 | 81.6 | 7.7 | 3.6 | 1.8 | template ModelArchive ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 81.5 | 0 | 6 | 85.8 | 0 |
| Shan 2014 (closed, JH2–JH1) | 7.1 | 3 | 2 | 85.4 | 75 |
| template PDB 4OLI chain A (mapped) | 3.1 | 3 | 2 | 85.4 | 75 |
| template ModelArchive ma-l9b1f (mapped) | 1.6 | 0 | 5 | 86.0 | 75 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 | vs template PDB 4OLI chain A | vs template ModelArchive ma-l9b1f |
|--:|--:|--:|--:|--:|--:|--:|
| 1 | 84.1 | 42.7 | 82.1 | 7.3 | 3.6 | 2.0 |
| 2 | 85.4 | 42.2 | 81.7 | 7.3 | 3.3 | 2.0 |
| 3 | 85.4 | 42.2 | 81.7 | 7.7 | 3.6 | 1.8 |
| 4 | 85.7 | 42.0 | 81.7 | 7.6 | 3.6 | 1.9 |
| 5 | 85.9 | 42.2 | 81.6 | 7.7 | 3.6 | 1.7 |
| 6 | 85.9 | 42.0 | 81.6 | 7.7 | 3.6 | 1.7 |
| 7 | 86.1 | 42.0 | 81.7 | 7.8 | 3.7 | 1.8 |
| 8 | 85.8 | 41.9 | 81.7 | 7.8 | 3.8 | 1.8 |
| 9 | 86.0 | 42.0 | 81.6 | 7.9 | 3.8 | 1.7 |
| 10 | 86.0 | 42.0 | 81.6 | 7.9 | 3.8 | 1.7 |
| 11 | 86.1 | 42.0 | 81.7 | 7.9 | 3.8 | 1.7 |
| 12 | 86.1 | 42.0 | 81.7 | 7.8 | 3.7 | 1.7 |
| 13 | 86.0 | 41.8 | 81.7 | 8.0 | 3.9 | 1.7 |
| 14 | 86.0 | 41.9 | 81.7 | 8.0 | 3.9 | 1.7 |
| 15 | 85.9 | 41.8 | 81.7 | 8.1 | 4.0 | 1.7 |

pLDDT 83.9–86.3; JH2–JH1 39.5–40.1 Å; FERM–JH1 41.7–42.8 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: template ModelArchive ma-l9b1f 75.

## Interpretation
- **Closed in all seeds and recycles**, the most compact closed form so far: FERM–JH1 41.7–42.8 Å (closed reference
  ma-l9b1f mapped to JAK2: 42.2 Å).
- **With the shallower MSA (128/512) the templates dominate even more:** 1.7–1.8 Å from ma-l9b1f (default MSA in
  experiment C: 2.5–2.7 Å) and slightly further from Shan's JAK2 (7.7–8.1 Å vs 6.8–7.3 Å). As expected: less MSA signal
  → closer copy of the template, less JAK2-specific adjustment.
- pLDDT 86.1–86.3 for the selected structures (slightly lower than experiment C, 86.7–86.9).
- Run time 42 min (shallower MSA is faster).
