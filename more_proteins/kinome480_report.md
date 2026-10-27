# Full reviewed human kinome — inter-domain centroid variation

All 480 reviewed human proteins carrying InterPro IPR000719 were scanned. **233 have two or
more UniProt-annotated Domain features** and can yield a domain pair; they produced **2435
observations** after gating. The earlier 104-protein batch was re-run with the per-file sequence
gate so the whole kinome uses one method — that alone raised its usable observations from 870 to
1185, because correctly-numbered PDB-relayed files are no longer discarded wholesale.

## Method

For each protein, templates come from the SWISS-MODEL Repository (its own models, PDB-relayed
entries) plus the AlphaFold v6 model. Every candidate chain is accepted only if its residue
**names** match the UniProt sequence at their own residue numbers in at least 80% of positions,
which rejects files served in PDB author numbering and picks the correct chain in complexes.
Domain centroids are Cα means over UniProt domain ranges, requiring 50% of the domain to be
present. Distances are rotation-invariant, so no superposition is needed. Models built on the same
parent template are collapsed to one observation, and only templates at 40% identity or above are
used, which excludes cross-family templates that measure the template's architecture rather than
the target's.

## Result

**270 domain pairs across 86 proteins** have two or more distinct experimental parent templates.
Of these, **64 exceed 15 Å of spread and 46 exceed 20 Å**. AlphaFold falls outside the range
spanned by the template-derived models in **75 of 269 pairs (28%)**.

The strongest signals, with the evidence class that supports each:

**PRKCA and PRKCG** are the cleanest new find: the C2-to-kinase distance spans 40.3–76.4 Å across
**five** parent templates (8SE1, 8SE3, 8SE4, 3PFQ), 36 Å of variation in the arrangement that
gates protein kinase C activation. AlphaFold sits at the compact end (39.4 Å), just below the
experimental minimum.

**CSF1R** remains the clearest single-protein case: Ig1-to-Ig5 is 75.6 Å on 4LIQ and 115.0 Å on
4WRM, both structures of CSF1R itself at 100% identity, with a 45%-identity homolog at 134.8 Å.

**The Eph receptors** give the broadest family replicate — LBD-to-FN3-2 varies by 26–34 Å in
eleven receptors (EPHA1, A3, A5–A8, A10, EPHB1–B4), each modelled independently.

**INSR** is the best-sampled system at **25 distinct parent templates**, spanning 35.4–67.7 Å, with
IGF1R (8 parents) and INSRR (11) repeating the pattern.

**The Tec family** shows large SH3-to-kinase ranges (ITK 44.9–85.2 Å over 3 parents; TEC and BTK
similar) and BTK's PH-to-SH3 spans 48.0–75.0 Å, with AlphaFold compact and outside in each case.

**ROS1 produces the largest raw numbers but the weakest support.** Its FN3-1-to-FN3-6 distance is
145.9 Å on template 9PVP and 255.1 Å on 9PWQ — a 109 Å difference — but both templates sit at 80%
identity, so this is a homolog comparison rather than two structures of ROS1, and only two parents
exist. What is unambiguous is that AlphaFold collapses this nine-FN3 ectodomain to 39.5 Å, far
below either template.

## Criterion 3 for the target table

Scoring the 41 genes in `kinase_targets_for_modelling.md` against measured multi-domain coverage —
the check its own Caveat 1 calls for — gives: **8 VARIES, 10 invariant, 12 criterion-3 failures
(no multi-domain template at all), 5 with a single structural parent, 6 outside the kinase set.**
The failures include three Tier 1 entries — EIF2AK2 (PKR), PAK1 and MELK — and AKT1 is invariant
across 11 parents rather than two-state, with only AlphaFold placing it elsewhere. Per-gene
verdicts are in `criterion3_coverage.csv`.

## Limits

Parent templates are reused across paralogs, so identical distances in related proteins are one
observation seen repeatedly, not independent evidence. UniProt Domain features omit receptor
tyrosine kinase ectodomain subdomains, so EGFR, ERBB2, ERBB4 and LTK are absent despite being
strong candidates. And no template in the entire kinome spans an ectodomain domain together with
the kinase domain for any type-III receptor (KIT, CSF1R, FLT1/3/4, PDGFRA, KDR), so the
membrane-spanning arrangement is unassessable by this method — the same wall as the JAK
FERM-to-JH1 pair before cross-species models were pooled in.
