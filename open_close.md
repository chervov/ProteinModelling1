# How to tell open vs closed — JAK1 / JAK2 domain arrangement

Ideas for measuring the open vs closed (autoinhibited) arrangement of FERM–SH2–JH2–JH1 in our OpenFold models,
roughly in order of usefulness.

## What we use now, and its limits
- **JH2–JH1 centroid distance** (the pipeline's metric): weak, 46 Å open vs 38–41 Å closed. The transition is
  mostly a rotation of JH1, so the centroid barely moves. It should not be used to select open/closed structures.
- **FERM–JH1 centroid distance:** strong and needs no reference, ~92 Å open vs ~40 Å closed. A good quick label.
- **JH1 RMSD after superposing JH2, against each reference:** very clear, but only says "near reference X" and needs references.

## Better ideas
1. **Position along the open→closed path (λ).** Superpose on JH2 and take the JH1 displacement vector from the open
   to the closed reference. Project each model onto it: λ = 0 is open, λ = 1 is closed, in-between values are
   intermediates. Add the perpendicular distance from the path to catch states that are neither. One number per
   structure that shows intermediates; works for JAK2 too (AF2 open and Shan or the mapped ma-l9b1f closed).
2. **Fraction of native interface contacts (Q).** Take the residue contacts between domains in each reference
   (JH1–FERM, JH1–JH2, JH2–SH2/FERM) and measure what fraction each model reproduces: Q_open and Q_closed.
   The standard measure for conformational transitions: local and physical, robust to loop noise, shows which
   interface forms, and works across homologs through a sequence alignment.
3. **Network confidence in the domain arrangement (inter-domain PAE).** model_1 doesn't output PAE, but the
   `model_1_ptm` preset does. The JH1↔FERM and JH1↔JH2 blocks of the PAE matrix show whether the network is
   confident about where JH1 sits: low PAE in a closed model = confident closed state; high PAE = placement is a
   guess. pLDDT is per residue and doesn't capture this.
4. **Rigid-body description of JH1 relative to JH2.** Rotation angle, hinge axis and translation from the JH2-fit
   transform, giving physical numbers ("JH1 rotates ~X° about a hinge near the JH2–JH1 linker") for comparing
   references and models.
5. **Functional markers.**
   - Contacts around the pseudokinase mutation hotspot at the JH2–JH1 interface: V617 in JAK2, V658 in JAK1.
   - Where JH1's activation-loop tyrosines sit (JAK2 Y1007/1008, JAK1 Y1034/1035): buried against JH2 or exposed.
   - The JH1 αC-helix and DFG state — a separate question: JH1's own active/inactive state, not the domain arrangement.

## How to show it
- **A 2D map of all conformations:** x = λ (or FERM–JH1 distance), y = Q_closed, coloured by run, recycle or pLDDT,
  with the references as stars. One figure showing all runs (templates, MSA depths, seeds) and any intermediates.
- **Clustering or PCA of JH1 positions after JH2 fit,** to find distinct states without assuming the references
  are the only ones.

## Practical recommendation
1. Add λ and Q_open/Q_closed to the comparison cell, and make the 2D map across all runs (template runs, MSA scan).
2. Switch guided-recycling selection from the JH2–JH1 distance to FERM–JH1 or λ, so "selected open/closed" means something.
3. Use `model_1_ptm` in a future run to get inter-domain PAE.

## Reference values for the centroid criteria

Domain-centroid distances (Cα centroids, Å) for all reference models. Domain boundaries from UniProt, as in the pipeline:
JAK1 FERM 34–420, SH2 439–544, JH2 583–855, JH1 875–1153; JAK2 FERM 37–380, SH2 401–482, JH2 545–809, JH1 849–1124.

| Target | Reference | State | JH2–JH1 | **FERM–JH1** | SH2–JH1 | FERM–JH2 | SH2–JH2 | FERM–SH2 |
|---|---|---|---|---|---|---|---|---|
| JAK1 | AF2 AF-P23458-F1 | open | 46.3 | **92.2** | 78.9 | 46.2 | 40.2 | 40.1 |
| JAK1 | ma-a1sai (Orianne) | open | 46.0 | **92.5** | 77.7 | 46.6 | 40.2 | 40.4 |
| JAK1 | ma-l9b1f (Orianne) | closed | 39.5 | **40.1** | 55.3 | 47.4 | 40.3 | 40.4 |
| JAK1 | Shan 2014 (JH2–JH1 only) | closed | 38.0 | – | – | – | – | – |
| JAK2 | AF2 AF-O60674-F1 | open | 45.9 | **93.8** | 78.3 | 48.1 | 39.7 | 35.9 |
| JAK2 | Shan 2014 (JH2–JH1 only) | closed | 40.9 | – | – | – | – | – |
| JAK2 | ma-l9b1f mapped to JAK2* | closed | 39.8 | **42.2** | 54.9 | 48.1 | 39.9 | 36.7 |

\* The JAK1 closed model renumbered onto JAK2 through the sequence alignment (1087 of 1132 residues covered);
the template of run JAK2_20261014_115511.

**Which distances separate open from closed:**

| Distance | Open | Closed | Difference | Usefulness |
|---|---|---|---|---|
| **FERM–JH1** | 92–94 | 40–42 | ~52 Å | best single criterion |
| **SH2–JH1** | 78–79 | 55 | ~23 Å | good second criterion |
| JH2–JH1 (current pipeline metric) | 46 | 38–41 | 5–8 Å | weak |
| FERM–JH2, SH2–JH2, FERM–SH2 | 46–48 / 40 / 36–40 | about the same | ~0 | no signal: the FERM–SH2–JH2 block is the same in both states |

Everything that changes involves JH1: open and closed differ by where JH1 sits, while the rest of the protein keeps
its shape. A simple centroid rule: **FERM–JH1 > ~80 Å → open; < ~50 Å → closed; in between → intermediate.**
The Shan models contain only JH2–JH1, so the FERM/SH2 criteria can't be applied to them.
