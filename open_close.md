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
