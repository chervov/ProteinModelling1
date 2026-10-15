# JAK1 — the third arrangement (neither open nor closed)

Analysis of the JAK1 structures that ended in neither the open nor the closed arrangement (no template, shallow MSA),
and comparison with references and experimental cryo-EM structures. Data and script: [third_arrangement/](third_arrangement/).

## Summary
- **It is one well-defined arrangement**, reached by 6 of the 7 structures (5 seeds at MSA 64/256, 2 of 5 at 96/384;
  one 64/256 seed is an outlier). Within the cluster JH1 sits within 0.7–9.5 Å of each other (after superposing JH2).
- **JH1 is rotated ~130–150° relative to JH2** compared with the open state (and ~100–120° compared with closed), and
  touches **only JH2**, through a **small interface of its own**: JH2 residues ~750 and 798–807, JH1 residues ~930–941
  and 997. This interface shares almost nothing with the open or the closed JH2–JH1 interface and does not involve the
  V658 region of JH2 (central to the closed interface).
- **It matches an experimental structure: the cryo-EM structure of the active JAK1 dimer, PDB 7T6F** (mouse JAK1 V657F,
  bound to the IFNλR1 intracellular domain; Glassman et al., *Science* 2022, doi:10.1126/science.abn8933):
  **4.9 Å** (JH1 RMSD after superposing JH2), the same domain distances (FERM–JH1 84.4, SH2–JH1 53.8, JH2–JH1 44.8 Å)
  and **the same JH2–JH1 interface residues**. The second cryo-EM JAK1 dimer structure, **8EWY** (Caveney et al.,
  *Cell Reports* 2023), matches instead our **open** state (3.7–4.5 Å).
- So OpenFold, given the wild-type JAK1 sequence and a shallow MSA, produces the JH2–JH1 arrangement seen experimentally
  in the active (V657F) JAK1 dimer — a third, experimentally supported conformation besides the open and the
  autoinhibited (closed) model arrangements.

## Where it appears (no template, 15 recycles)
| MSA | run | seeds in the third arrangement |
|---|---|---|
| 64/256 | [JAK1_20261015_095803](runs/JAK1_20261015_095803) | all 5 (from recycle ~3–5; seed 4 an outlier) |
| 96/384 | [JAK1_20261015_135849](runs/JAK1_20261015_135849) | 2 of 5 (seeds 2, 4; after recycles 4–7) |
| 128/512 and deeper | – | none (open or closed) |

Structures analysed: final recycle (15) of each seed.

## Geometry (Å; JH1 position = RMSD of JH1 Cα after superposing JH2 Cα)

| structure | FERM–JH1 | SH2–JH1 | JH2–JH1 | JH1 vs open ma-a1sai | JH1 vs closed ma-l9b1f | JH1 rotation vs open / vs closed | pLDDT JH1 |
|---|--:|--:|--:|--:|--:|--:|--:|
| 64/256 seed 0 | 84.3 | 54.0 | 45.8 | 48.3 | 82.5 | 154° / 102° | 88.9 |
| 64/256 seed 1 | 84.6 | 55.7 | 44.5 | 44.3 | 81.1 | 144° / 107° | 89.7 |
| 64/256 seed 2 | 83.7 | 54.0 | 44.5 | 46.0 | 80.8 | 135° / 113° | 89.8 |
| 64/256 seed 3 | 84.0 | 53.7 | 45.4 | 47.3 | 81.7 | 146° / 106° | 89.2 |
| 96/384 seed 2 | 83.8 | 54.9 | 43.9 | 43.5 | 80.6 | 129° / 118° | 90.6 |
| 96/384 seed 4 | 83.7 | 54.8 | 43.9 | 43.7 | 80.8 | 130° / 118° | 91.2 |
| 64/256 seed 4 (outlier) | 87.2 | 61.8 | 44.4 | 35.6 | 82.1 | 97° / 138° | 87.3 |
| ma-a1sai (open, Orianne) | 92.5 | 77.7 | 46.0 | 0.0 | 81.7 | 0° / 142° | 90.6 |
| AF2 AF-P23458-F1 (open) | 92.2 | 78.9 | 46.3 | 3.4 | 81.0 | 7° / 146° | 90.5 |
| ours, open (512/8192 seed 0) | 92.8 | 78.0 | 46.4 | 0.9 | 82.0 | 2° / 141° | 91.4 |
| ma-l9b1f (closed, Orianne) | 40.1 | 55.3 | 39.5 | 81.7 | 0.0 | 142° / 0° | 99.0 |
| ours, closed (128/512 seed 7) | 41.4 | 56.7 | 39.0 | 81.3 | 1.2 | 140° / 4° | 88.2 |
| ours, next to FERM (96/384 seed 1) | 46.3 | 67.7 | 44.0 | 84.0 | 17.9 | 164° / 27° | 88.4 |
| **7T6F** cryo-EM, active JAK1 dimer (V657F) | 84.4 | 53.8 | 44.8 | 47.2 | 82.8 | – | (EM) |
| **8EWY** cryo-EM, JAK1 dimer | 94.4 | 78.8 | 47.0 | 4.5 | 80.0 | – | (EM) |

All domains keep their fold (each domain ≤ 1.3 Å Cα RMSD from the AF2 model, seed-4 outlier JH1 1.9 Å); pLDDT is as
high as in open/closed models — these are not broken or low-confidence structures.

## Is it one arrangement? JH1 position between the structures (Å)

| | 64/256 seed 0 | 64/256 seed 1 | 64/256 seed 2 | 64/256 seed 3 | 96/384 seed 2 | 96/384 seed 4 | 64/256 seed 4* |
|---|--:|--:|--:|--:|--:|--:|--:|
| 64/256 seed 0 | 0.0 | 5.9 | 6.5 | 3.3 | 9.5 | 9.1 | 22.0 |
| 64/256 seed 1 | 5.9 | 0.0 | 3.7 | 3.7 | 4.7 | 4.4 | 17.0 |
| 64/256 seed 2 | 6.5 | 3.7 | 0.0 | 3.4 | 3.8 | 3.6 | 17.0 |
| 64/256 seed 3 | 3.3 | 3.7 | 3.4 | 0.0 | 6.6 | 6.3 | 19.6 |
| 96/384 seed 2 | 9.5 | 4.7 | 3.8 | 6.6 | 0.0 | 0.7 | 13.7 |
| 96/384 seed 4 | 9.1 | 4.4 | 3.6 | 6.3 | 0.7 | 0.0 | 14.0 |
| 64/256 seed 4* | 22.0 | 17.0 | 17.0 | 19.6 | 13.7 | 14.0 | 0.0 |

Six structures form one cluster (0.7–9.5 Å); 64/256 seed 4 (*) is 14–22 Å from them — a variant/intermediate.

## Contacts (residue pairs with heavy atoms < 4.5 Å)

| structure | JH1–JH2 | JH1–FERM | JH1–SH2 | JH2–FERM | FERM–SH2 |
|---|--:|--:|--:|--:|--:|
| 64/256 seed 0 | 10 | 0 | 0 | 22 | 23 |
| 64/256 seed 1 | 13 | 0 | 0 | 23 | 24 |
| 64/256 seed 2 | 15 | 0 | 0 | 21 | 24 |
| 64/256 seed 3 | 13 | 0 | 0 | 20 | 23 |
| 96/384 seed 2 | 18 | 0 | 0 | 23 | 24 |
| 96/384 seed 4 | 18 | 0 | 0 | 22 | 23 |
| 64/256 seed 4 (outlier) | 7 | 0 | 0 | 22 | 24 |
| ma-a1sai (open, Orianne) | 36 | 0 | 0 | 39 | 31 |
| ours, open (512/8192 seed 0) | 23 | 0 | 0 | 22 | 23 |
| ma-l9b1f (closed, Orianne) | 46 | 8 | 0 | 37 | 29 |
| ours, closed (128/512 seed 7) | 30 | 7 | 0 | 17 | 25 |

JH1 touches only JH2, with fewer contacts (7–18 pairs) than in the open (19–36) or closed (25–46) arrangements.

### JH2–JH1 interface residues

| structure | JH2 residues at the interface | JH1 residues at the interface |
|---|---|---|
| 64/256 seed 2 | 749, 750, 753, 798, 800, 801, 803, 804, 807 | 930, 932, 933, 939, 940, 941, 942, 997 |
| 96/384 seed 2 | 749, 750, 753, 798, 799, 800, 801, 803, 804, 807 | 903, 929, 930, 931, 932, 933, 939, 940, 941, 997 |
| **7T6F** (cryo-EM, active dimer) | 749, 753, 798, 799, 800, 801, 803, 804, 807 | 930, 931, 933, 939, 940, 941 |
| ma-a1sai (open, Orianne) | 587, 588, 589, 590, 591, 592, 593, 594, 598, 627, 677, 681, 748, 750, 751, 754, 755, 799 | 875, 876, 877, 890, 896, 897, 898, 899, 900, 912, 947, 948, 949, 950, 953 |
| ma-l9b1f (closed, Orianne) | 604, 606, 615, 617, 643, 644, 645, 646, 648, 651, 652, 654, 668, 669, 670, 671, 708, 723, 724, 731, 734, 736 | 877, 878, 879, 888, 891, 893, 897, 899, 900, 901, 902, 903, 904, 958, 960, 961, 962, 1012 |
| ours, closed (128/512 seed 7) | 604, 606, 609, 615, 617, 643, 652, 654, 668, 669, 723, 724, 731, 734, 736 | 877, 878, 879, 880, 888, 890, 891, 893, 897, 899, 900, 901, 904, 913, 958, 960 |

- Core shared by all 6 cluster members: JH2 750, 798, 800, 803, 804, 807; JH1 930, 932, 933, 940, 941, 997 —
  essentially the 7T6F interface.
- Overlap (Jaccard) of the third-arrangement JH2 interface with the open interfaces 0.04–0.12, with the closed ones 0.
- The closed interface (ma-l9b1f, Shan, our seed 7) uses the V658 region of JH2 (643–671); the third arrangement does not.
- By-product: our closed seed 7 reproduces the ma-l9b1f interface residue by residue (14 of its 15 JH2 interface residues).

## Caveats
- 7T6F is **mouse** JAK1 with the activating **V657F** mutation (human V658F), in a **dimer bound to a receptor fragment**;
  our models are wild-type human JAK1 monomers. The match is in the JH2–JH1 arrangement of one protomer.
- 8EWY (same construct type; residue 657 is also Phe in its sequence) matches our open state — the two cryo-EM
  structures show different JH2–JH1 arrangements, and our runs reproduce both.
- In our runs the third arrangement appears only with a shallow MSA (≤ 96/384), where the network has less
  co-evolution information; whether that is meaningful (e.g. a sub-family signal in the MSA) is open.
- One structure per seed (final recycle); the 64/256 seed 4 is a variant 14–22 Å from the cluster.

## Possible next steps
- JAK1 **V658F** at the same depths (64/256, 96/384, 128/512): does the mutation favour this arrangement (as in 7T6F)?
- Compare JAK2 (no-template scan running) for a corresponding arrangement.
- Check the MSA: which sequences/sub-families drive the third arrangement at shallow depth (MSA subsampling / clustering).
