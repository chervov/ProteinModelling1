# Variant-level experimental evidence table

`09_variant_effect_evidence.tsv` is a normalized **row-per-variant evidence table**. It now replaces the earlier source matrix as the working table for variants whose effect can be stated from the reviewed article text.

## Fields

- `effect_class` is the direction established in the stated assay, not a clinical classification.
- `value_or_observation` contains the reported qualitative result or a numerical result only when the article explicitly supplies one in the reviewed text.
- `assay_or_context` is mandatory because JAK effects often differ among purified protein, reconstituted cells, patient cells, cytokines, and organisms.
- `source_status` distinguishes full-text review from an article-level review and identifies the TYK2 DMS preprint.

## Important interpretation rules

1. A double mutant such as `JAK2 V617F/E596A` is an **engineered mechanistic perturbation**, not evidence that `E596A` alone is a patient GOF/LOF allele.
2. `GOF`, `LOF`, and `hypomorphic` remain assay-specific. TYK2 `P1104A` and `I684S` demonstrate why kinase activity, signalling, and clinical phenotype must not be collapsed to one value.
3. This first extraction contains only statements that were explicit enough to audit against the cited primary paper. The remaining papers in `01_direct_experimental_papers.md` need their tables/supplements extracted before the file can claim exhaustive coverage.
4. The Howard TYK2 DMS preprint is represented only where this table has an interpretable published observation. Its numerical, condition-specific data must be imported from MaveDB as a separate high-throughput score matrix; do not turn it into a single GOF/LOF label.

## Sources

The `source_id` values refer to `04_variant_effect_by_source_matrix.md`; each PMID can be resolved directly at `https://pubmed.ncbi.nlm.nih.gov/<PMID>/`.
