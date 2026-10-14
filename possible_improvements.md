# Possible improvements of the closed JAK2 form

Current closed JAK2 (run [JAK2_20261014_115511](JAK2/runs/JAK2_20261014_115511)): obtained with a single template,
the JAK1 closed model ma-l9b1f (itself a model, 45% identical to JAK2). It is 6.6–6.8 Å from Shan's JAK2 model
(JH1 RMSD after superposing JH2), pLDDT ~86.5. "Improving" can mean three things: more JAK2-specific, better grounded
in experimental data, or shown to be stable rather than just copied. Ideas, ranked:

## 1. Better templates: experimental structures and JAK2's own sequence
Up to 4 templates are allowed; we use one.
- **TYK2 pseudokinase–kinase crystal structure** (Lupardus et al. 2014, PNAS; probably PDB 4OLI): the experimental
  autoinhibited JH2–JH1 arrangement that Shan's models were built on — the best experimental source for the key interface.
- **Shan's JAK2 model as a second template:** identical sequence over JH2–JH1, adds the JAK2-specific details.
- **Experimental JAK2 fragments:** FERM–SH2, JH2 and JH1 crystal structures — accurate domain shapes, identical sequence.
- **Together with ma-l9b1f,** for where FERM sits relative to JH1 — the only part with no experimental data
  (no full-length autoinhibited JAK structure exists).

PDB IDs need checking before use. Technically the same as the current run: one mmCIF per template in the template folder.

## 2. Test whether the closed form is stable: template only in the first recycles
- Give the closed template for recycles 1–3, then let the JAK2 sequence and MSA continue alone
  (zero `template_mask` / `template_torsion_angles_mask` for later recycles; reset the guided "best state" when the template is switched off).
- If it stays closed, the closed form is a stable state for JAK2, not just a copy. If it opens, the deep MSA prefers
  open for JAK2 as it did for JAK1.
- Either way, the template-free recycles show the model's own JAK2 closed structure.

## 3. Find the closed state without any template: MSA subsampling
- Cluster the JAK2 MSA into subfamilies (AF-Cluster approach), or use shallow random subsets, and predict from each.
- For other proteins some clusters give the alternative state; our JAK1 MSA-depth scan already shows MSA depth changes the result.
- A template-free closed JAK2 would be the strongest evidence that it is not a template artefact.

## 4. Better assessment of the closed form
- **Functional interface check:** in autoinhibited JAK2, JH2 around V617 (V617F hotspot) packs against JH1 —
  measure those contacts and the fraction of interface contacts shared with Shan's model (Q).
- **Confidence in the arrangement:** run with `model_1_ptm` to get inter-domain PAE (JH1 vs JH2/FERM);
  high pLDDT does not show that the arrangement is confident.
- **Second model:** also run model_2, the other AF2 model that takes templates.

## 5. Clean-up
- Amber relaxation (currently skipped) of the final closed models, to remove clashes at the new interfaces.

## Suggested order
1. Idea 2, template release with ma-l9b1f: cheap (small patch, one ~1 h run), answers whether the closed form is stable.
2. In parallel, prepare idea 1: the experimental template set (TYK2 JH2–JH1, Shan JAK2, JAK2 fragments).
