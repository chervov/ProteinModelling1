# TYK2_20261016_130845 — TYK2 experiment TYK2_WT_4OLI_rel3_msa128-512

TYK2 wild type. The experimental autoinhibited structure 4OLI (TYK2 JH2-JH1, Lupardus et al. 2014, 2.8 A, chain A residues 579-1177, 99.6 percent identical to the query: the crystal is the kinase-dead D1023N variant) is the template in recycles 1-3 only, then switched off; MSA 128/512, 15 recycles, seeds 0-15. Baseline for the paired P982A run: once the template is released, how often does the closed arrangement survive? 4OLI covers JH2-JH1 only (no FERM-SH2), so the readout is JH1 RMSD against the mapped template after superposing JH2, not the FERM-JH1 distance used for JAK1/JAK2/JAK3.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; templates: PDB 4OLI chain A (recycles 1–3 only). Run time 219 min (whole Colab session incl. setup, Google Colab A100).

Template identity to TYK2: `{"aligned": 539, "identical": 537, "identity_aligned": 0.996, "identity_vs_shorter": 0.996}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |
| template pdb:4OLI:A (mapped) | 39.0 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs template pdb:4OLI:A | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 81.1 | 37.1 | 39.2 | 0.7 | 1.9 | AF2 |
| 1 | 4 | 80.8 | 37.2 | 39.3 | 1.1 | 1.8 | AF2 |
| 2 | 9 | 80.8 | 37.4 | 40.0 | 1.2 | 1.6 | AF2 |
| 3 | 4 | 80.8 | 37.2 | 39.5 | 0.9 | 1.7 | AF2 |
| 4 | 4 | 81.0 | 37.3 | 39.2 | 0.8 | 1.9 | AF2 |
| 5 | 4 | 80.8 | 37.2 | 39.1 | 0.5 | 1.7 | AF2 |
| 6 | 14 | 80.6 | 37.4 | 39.3 | 1.4 | 1.8 | AF2 |
| 7 | 4 | 80.9 | 37.2 | 39.7 | 0.8 | 2.0 | AF2 |
| 8 | 8 | 80.6 | 37.5 | 38.8 | 2.1 | 1.4 | template pdb:4OLI:A |
| 9 | 4 | 80.9 | 37.2 | 41.3 | 1.7 | 1.7 | AF2 |
| 10 | 4 | 80.9 | 37.3 | 39.4 | 1.2 | 1.6 | AF2 |
| 11 | 4 | 80.8 | 37.2 | 38.9 | 0.7 | 1.7 | AF2 |
| 12 | 4 | 80.8 | 37.2 | 39.9 | 1.4 | 1.9 | AF2 |
| 13 | 4 | 80.7 | 37.3 | 39.6 | 0.8 | 1.9 | AF2 |
| 14 | 4 | 80.4 | 37.1 | 39.5 | 1.3 | 1.6 | AF2 |
| 15 | 4 | 80.7 | 37.3 | 39.2 | 0.7 | 2.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 0.5 | 5 | 4 | 80.8 | 240 |
| template pdb:4OLI:A (mapped) | 1.0 | 6 | 2 | 80.3 | 240 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs template pdb:4OLI:A |
|--:|--:|--:|--:|--:|
| 1 (template) | 76.9 | 44.3 | 1.1 | 2.1 |
| 2 (template) | 80.9 | 39.7 | 0.9 | 1.3 |
| 3 (template) | 81.3 | 39.7 | 1.2 | 1.7 |
| 4 | 80.7 | 39.5 | 1.0 | 1.8 |
| 5 | 80.1 | 39.3 | 1.2 | 1.6 |
| 6 | 80.4 | 39.5 | 1.2 | 1.8 |
| 7 | 80.5 | 39.3 | 1.4 | 1.7 |
| 8 | 80.5 | 39.1 | 1.4 | 1.7 |
| 9 | 80.6 | 39.4 | 1.4 | 1.6 |
| 10 | 80.4 | 39.4 | 1.4 | 1.6 |
| 11 | 80.4 | 39.4 | 1.2 | 1.8 |
| 12 | 80.4 | 39.6 | 1.4 | 1.7 |
| 13 | 80.3 | 39.7 | 1.4 | 1.7 |
| 14 | 80.6 | 39.5 | 1.5 | 1.8 |
| 15 | 80.3 | 39.3 | 1.5 | 1.6 |

pLDDT 75.8–81.7; JH2–JH1 36.9–38.1 Å; FERM–JH1 38.5–47.2 Å (see the reference table above; 4OLI covers JH2–JH1 only, so it has no FERM–JH1 value; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 211, template pdb:4OLI:A 29.
## Per-seed escape from the template arrangement (JH1|JH2 vs template pdb:4OLI:A (Å), Å)

Started from the experimental closed structure 4OLI (template in recycles 1–3, then switched off). Reference scale: the closed JAK1 model ma-l9b1f sits 4.2 Å from 4OLI by this measure, the open model 80.6 Å.

| seed | recycles 1–15 | final | verdict |
|--:|---|--:|---|
| 0 | 1.9 1.3 5.1 1.9 1.5 1.6 1.8 1.6 1.6 1.5 1.8 1.7 1.7 1.9 1.6 | 1.6 | kept closed (< 10 Å) |
| 1 | 1.9 1.3 1.5 1.8 1.6 1.8 1.6 1.7 1.7 1.8 1.8 1.9 2.0 1.7 1.7 | 1.7 | kept closed (< 10 Å) |
| 2 | 2.5 1.5 1.6 2.0 1.5 1.9 1.6 1.6 1.6 1.8 1.5 2.2 1.7 1.8 1.4 | 1.4 | kept closed (< 10 Å) |
| 3 | 2.0 1.2 1.6 1.7 1.6 1.7 1.7 1.7 1.5 1.6 2.0 1.7 1.7 1.6 1.5 | 1.5 | kept closed (< 10 Å) |
| 4 | 1.5 1.4 1.6 1.9 1.6 1.7 1.7 1.8 1.5 1.5 1.8 1.7 1.7 1.7 1.7 | 1.7 | kept closed (< 10 Å) |
| 5 | 1.8 1.3 1.1 1.7 1.7 1.7 1.6 1.7 1.6 1.7 1.8 1.7 1.8 1.8 1.8 | 1.8 | kept closed (< 10 Å) |
| 6 | 2.1 1.0 2.0 1.6 1.4 1.7 1.5 1.7 1.6 1.4 1.9 1.6 1.7 1.8 1.4 | 1.4 | kept closed (< 10 Å) |
| 7 | 2.1 1.4 1.5 2.0 1.6 1.7 1.8 1.8 1.8 1.5 2.0 1.6 1.7 1.9 1.8 | 1.8 | kept closed (< 10 Å) |
| 8 | 2.2 1.4 1.2 1.5 1.4 1.4 1.4 1.4 1.5 1.5 1.5 1.5 1.4 1.5 1.4 | 1.4 | kept closed (< 10 Å) |
| 9 | 1.6 1.4 1.6 1.7 1.6 1.8 1.6 1.8 1.7 1.6 1.7 1.7 1.7 1.8 1.6 | 1.6 | kept closed (< 10 Å) |
| 10 | 2.2 1.2 1.5 1.6 1.5 1.9 1.7 1.6 1.5 1.8 1.9 1.7 1.6 1.7 1.8 | 1.8 | kept closed (< 10 Å) |
| 11 | 2.9 1.3 1.3 1.7 1.8 2.2 1.8 1.6 1.6 1.4 2.0 1.8 1.9 1.9 1.5 | 1.5 | kept closed (< 10 Å) |
| 12 | 3.4 1.4 1.4 1.9 1.4 1.7 1.6 1.7 1.4 1.5 1.6 1.4 1.6 1.6 1.6 | 1.6 | kept closed (< 10 Å) |
| 13 | 1.8 1.2 1.7 1.9 1.6 1.8 1.7 1.8 1.6 1.6 2.0 1.5 1.9 2.1 1.6 | 1.6 | kept closed (< 10 Å) |
| 14 | 1.9 1.2 1.5 1.6 1.5 1.9 1.9 1.8 1.7 1.7 1.9 1.7 1.9 1.7 1.8 | 1.8 | kept closed (< 10 Å) |
| 15 | 2.2 1.5 1.6 2.1 1.8 2.1 1.9 1.9 1.8 1.8 2.1 1.9 1.7 1.9 1.9 | 1.9 | kept closed (< 10 Å) |

**16/16 seeds kept the closed arrangement, 0/16 escaped.**

## Per-seed trajectories (FERM–JH1 centroid distance, Å)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 43 40 42 39 39 39 39 39 39 39 39 39 39 39 39 | compact (< 50) |
| 1 | 44 40 40 39 40 40 39 39 40 40 40 40 40 40 40 | compact (< 50) |
| 2 | 47 40 39 40 40 40 40 40 40 40 40 41 41 41 40 | compact (< 50) |
| 3 | 44 40 40 40 40 40 40 40 40 40 40 40 40 40 40 | compact (< 50) |
| 4 | 43 40 39 39 39 39 39 39 39 39 39 39 39 39 39 | compact (< 50) |
| 5 | 43 39 39 39 39 39 39 39 39 39 39 39 39 39 39 | compact (< 50) |
| 6 | 46 40 39 39 39 39 38 38 39 39 39 39 39 39 39 | compact (< 50) |
| 7 | 44 39 39 40 40 40 40 40 40 40 40 40 40 40 40 | compact (< 50) |
| 8 | 46 40 39 39 39 39 39 39 39 39 39 39 39 39 39 | compact (< 50) |
| 9 | 45 40 42 41 39 39 39 39 39 39 39 39 39 39 39 | compact (< 50) |
| 10 | 44 39 39 39 39 39 39 39 39 39 39 39 39 40 39 | compact (< 50) |
| 11 | 44 39 39 39 39 40 40 39 39 39 40 40 40 40 39 | compact (< 50) |
| 12 | 46 40 39 40 39 40 39 39 39 39 39 39 40 40 39 | compact (< 50) |
| 13 | 45 40 39 40 39 40 40 39 40 40 39 40 40 40 40 | compact (< 50) |
| 14 | 43 40 40 40 40 40 39 39 39 40 40 40 40 39 39 | compact (< 50) |
| 15 | 44 40 39 39 39 40 39 39 39 39 39 39 40 40 39 | compact (< 50) |
