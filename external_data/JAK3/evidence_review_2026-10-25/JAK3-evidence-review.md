# JAK3: evidence review for the requested JAK-family positions

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

The original Y581C variant has conflicting predictions and no verified exact-variant activity or drug-response assay in the reviewed evidence. P1082E, G546R, V553I and L777I are comparisons derived from the four JAK2 variants, not functional substitutes for those JAK2 mutations.

Nearby mutations demonstrate opposite effects: H583Y and G589D have activating cellular results in [Sim et al., 2017, PMID 28284718](https://pubmed.ncbi.nlm.nih.gov/28284718/); G589S impairs kinase function in [Roberts et al., PMID 14615376](https://pubmed.ncbi.nlm.nih.gov/14615376/). The published tofacitinib cellular IC50 values for H583Y (85 ± 10 nM) and G589D (54 ± 9 nM) are not Y581C drug-response values.

See the dedicated [Y581C evidence review](JAK3-Y581C-evidence-review.md), [homology review](JAK3-Y581C-homologous-position-review.md), and [neigbours review](JAK3-Y581C-neigbours-evidence.md) for source-level detail.

## Exact-substitution predictor scores

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK3 P1082E | 0.4725; ambiguous | 0; deleterious | 0.471; possibly_damaging | Not retrieved | Not retrieved | Not retrieved |
| JAK3 G546R | 0.1249; likely benign | 0.04; deleterious | 0.267; benign | 0.334 | 17.32 | -3.51, -3.41 |
| JAK3 V553I | 0.1951; likely benign | 0; deleterious | 0.714; possibly_damaging | Not retrieved | Not retrieved | Not retrieved |
| JAK3 L777I | 0.1147; likely benign | 0.01; deleterious | 0.327; benign | 0.568 | 24.4 | -1.07, -1.03 |
| JAK3 Y581C | 0.0993; likely benign | 0; deleterious | 0.820; possibly damaging | 0.369 | 22.2 | -5.09 to -5.22 |

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
