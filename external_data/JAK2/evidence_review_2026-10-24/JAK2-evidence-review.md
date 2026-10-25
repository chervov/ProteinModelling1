# JAK2: evidence review for the requested JAK-family positions

Consolidated 25 October 2026 from the linked project reviews. Scope: four JAK2 variants and JAK3 Y581C, with their paralog comparisons; this is not a catalogue of every variant in this gene or a new exhaustive literature search.

## Position correspondence

| Original target | JAK1 | JAK2 | JAK3 | TYK2 |
|---|---|---|---|---|
| JAK2 V1110E | P1136E | V1110E | P1082E | A1156E |
| JAK2 G571R | G610R or S612R (uncertain) | G571R | G546R | G634R |
| JAK2 V578I | V619I | V578I | V553I | V639I |
| JAK2 L805I | I845 unchanged | L805I | L777I | L866I |
| JAK3 Y581C | H647C | H606C | Y581C | H667C |

## Evidence and relevance

The four original variants remain functionally unresolved in this review. G571R has a suspected-myeloproliferative-neoplasm observation in [Ma et al., 2009, PMID 19074595](https://pmc.ncbi.nlm.nih.gov/articles/PMC2607565/); adjacent inhibitory Y570 provides a mechanistic hypothesis, not a G571R activity measurement. COSMIC and diagnostic patents repeating that observation are not independent functional validations.

L805I is recorded in SARC9371_BONE in CCLE Broad 2019. Direct queries for CISH, SOCS2, SOCS3, PIM1, CCND1, BCL2L1, BIRC5, IRF1, CXCL9, CXCL10, TAP1, B2M and CD274 each returned 1,156 expression samples and no SARC9371 row. SARC9371 is absent from the whole RNA sample list. Therefore neither a downstream-expression effect size nor GOF/LOF inference can be computed for this line from that dataset. Missing expression is not zero expression. [Raw queries](JAK2-L805I-CCLE-downstream-expression-availability.json). Newer DepMap availability was not verified because the portal presented a security check.

The H606C comparator to JAK3 Y581C is hypothetical here. H606Q, a different substitution, has observational and modelling evidence, not an established H606C assay.

As a positive functional comparator, [Song et al., 2024, PMID 38629639](https://doi.org/10.1002/ajh.27311) studied inherited R715T in a family with erythrocytosis. Increased STAT5 phosphorylation, reporter activity and erythropoietin-independent progenitor growth support R715T gain of function. This does not classify our four variants or transfer the reported ropeginterferon response to them. The existing [OMIM report](../jak2_omim.md) is supplementary context; its predictor/DMS claims have not been revalidated in this consolidation.

## Exact-substitution predictor scores

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK2 V1110E | 0.2891; likely benign | 0.01; deleterious_low_confidence | 0.862; possibly_damaging | 0.477 | 23 | 0.24 |
| JAK2 G571R | 0.2686; likely benign | 0.01; deleterious_low_confidence | 0.94; probably_damaging | 0.874 | 33 | -4.36 |
| JAK2 V578I | 0.2368; likely benign | 0; deleterious_low_confidence | 0.999; probably_damaging | 0.618 | 29.3 | -0.91 |
| JAK2 L805I | 0.1504; likely benign | 0.01; deleterious_low_confidence | 0.78; possibly_damaging | 0.439 | 25.6 | -0.96 |
| JAK2 H606C | 0.1584; likely benign | 0; deleterious, low confidence | 0.786; possibly damaging | Not retrieved | Not retrieved | Not retrieved |

These are retrieved predictions, not experimental kinase activity, clinical classifications or probabilities of GOF. Conflicting models must not be resolved by counting votes. Low-confidence SIFT flags are preserved. Multiple PROVEAN values represent distinct returned entries, not replicate assays.

The H-to-C comparator codons require two nucleotide changes. Missing REVEL/CADD/PROVEAN values reflect the precomputed lookup coverage used, not benign predictions. Genomic-allele scores depend on the nucleotide route chosen; exact coding queries and transcript identifiers are in the source reports. No new model was run for this consolidation.

## Detailed sources and reproducibility

- [V1110E: alignment, coding alleles, predictors and literature](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK2/evidence_review_2026-10-24/JAK2-V1110E-homology-and-predictors.md)
- [G571R: alignment, coding alleles, predictors and literature](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK2/evidence_review_2026-10-24/JAK2-G571R-homology-and-predictors.md)
- [V578I: alignment, coding alleles, predictors and literature](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK2/evidence_review_2026-10-24/JAK2-V578I-homology-and-predictors.md)
- [L805I: alignment, coding alleles, predictors and literature](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK2/evidence_review_2026-10-24/JAK2-L805I-homology-and-predictors.md)
- [Y581C family comparison and exact score provenance](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK3/evidence_review_2026-10-25/JAK3-Y581C-homologous-position-review.md)
- [Four-variant raw predictor results](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK2/evidence_review_2026-10-24/JAK2-four-variant-predictor-results.json)
- [Additional predictor results](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK2/evidence_review_2026-10-24/JAK2-four-variant-additional-predictors.json)
- [Cysteine-comparator raw results](https://github.com/chervov/ProteinModelling1/blob/main/external_data/JAK3/evidence_review_2026-10-25/JAK-family-cysteine-predictor-results.json)

Negative search findings are bounded to the sources checked. Disease observations, related substitutions, structural hypotheses and exact-variant functional experiments are different evidence types. A useful assay compares matched wild-type and mutant abundance, basal and stimulated downstream STAT signaling, and a receptor-appropriate cellular output.
