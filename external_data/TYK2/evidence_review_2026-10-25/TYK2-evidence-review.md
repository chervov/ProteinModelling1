# TYK2: evidence review for the requested JAK-family positions

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

A1156E, G634R, V639I, L866I and H667C are the TYK2 comparisons to the requested JAK2/JAK3 variants. Sequence equivalence does not guarantee the same receptor context or signaling effect.

TYK2 L866I has COSMIC-index observations sharing COSM6229424, with colorectal-carcinoma metadata but no PMID in the returned record. Repeated rows are not confirmed independent patients or functional validation. No exact L866I drug-response result was established in the prior source review.

Nearby H669P was catalytically impaired and failed to support normal interferon-alpha signaling despite high basal phosphorylation in [Yeh et al., 2000, PMID 10908660](https://pubmed.ncbi.nlm.nih.gov/10908660/). H669 is two residues from H667; it must not be relabeled as the exact JAK3 Y581 equivalent. An older literature correspondence differs from our canonical sequence alignment, as documented in the linked homology report.

This consolidation does not independently validate the TYK2 deep-mutational-scan scores mentioned elsewhere in the repository. Their assay definition, normalization, exact substitution and uncertainty need to be checked before treating them as directional evidence. No GOF/LOF classification is assigned to these comparators on the basis of the pathogenicity predictors below.

## Exact-substitution predictor scores

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| TYK2 A1156E | 0.4621; ambiguous | 0; deleterious | 0.864; possibly_damaging | 0.5 | 28.7 | -1.1, -1.09 |
| TYK2 G634R | 0.1072; likely benign | 0.13; tolerated | 0.184; benign | 0.314 | 8.038 | -1.43, -1.06, -1.24 |
| TYK2 V639I | 0.325; likely benign | 0; deleterious | 1; probably_damaging | Not retrieved | Not retrieved | Not retrieved |
| TYK2 L866I | 0.1136; likely benign | 0.02; deleterious | 0.305; benign | 0.343 | 23.3 | -0.95, -1 |
| TYK2 H667C | 0.4041; ambiguous | 0.01; deleterious | 0.999; probably damaging | Not retrieved | Not retrieved | Not retrieved |

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
