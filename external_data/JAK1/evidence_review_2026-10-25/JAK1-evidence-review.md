# JAK1: evidence review for the requested JAK-family positions

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

JAK1 P1136E, G610R (or alternative S612R), V619I and H647C are homolog-based comparisons, not established patient variants in this review. I845 already is isoleucine: I845I is unchanged protein, not a missense variant.

The G571-to-JAK1 correspondence changes with alignment settings. Alternative S612R scores are AlphaMissense 0.1298, SIFT 0.05 and PolyPhen-2 0.263; the default G610R scores below must not hide this uncertainty.

At H647, COSMIC-index record COSM11054440 describes H647Q, a different substitution, linked to [Yan et al., 2020, PMID 32217638](https://pubmed.ncbi.nlm.nih.gov/32217638/). The primary study concerns early-onset colorectal-cancer organoids; its exact supplementary variant row and an H647Q functional assay were not independently verified in the prior review. It does not validate H647C.

No exact-comparator functional direction or mutation-specific drug response was established in the reviewed sources.

## Exact-substitution predictor scores

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK1 P1136E | 0.6898; likely pathogenic | 0; deleterious | 0.4; benign | Not retrieved | Not retrieved | Not retrieved |
| JAK1 G610R | 0.1418; likely benign | 0; deleterious | 0.957; probably_damaging | 0.364 | 24.3 | -1.54 |
| JAK1 V619I | 0.355; ambiguous | 0; deleterious | 0.995; probably_damaging | Not retrieved | Not retrieved | Not retrieved |
| JAK1 I845I | N/A: unchanged residue | N/A | N/A | N/A | N/A | N/A |
| JAK1 H647C | 0.6183; likely pathogenic | 0.01; deleterious | 0.999; probably damaging | Not retrieved | Not retrieved | Not retrieved |

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
