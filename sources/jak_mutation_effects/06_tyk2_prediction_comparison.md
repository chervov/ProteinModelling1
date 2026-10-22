# TYK2 prediction comparison: precomputed scores versus direct experiments

## Scope

This comparison uses four well-characterized TYK2 missense variants from the existing research pack. It combines (a) published, **precomputed** AlphaMissense and ESM1b values, (b) a **new local computation** with the small ESM-2 8M model, and (c) direct experimental evidence. It does not claim that ESM-2 is clinically calibrated or that a score alone determines GOF/LOF.

### Input and provenance

- Canonical protein: UniProt `P29597` (TYK2); the script checks the wild-type residue at each stated position.
- AlphaMissense and ESM1b values: Table 6-5 of a 2024 King’s College London thesis returned by web search; these are secondary-source values and must be re-queried from the official current source before clinical use. The source reports P1104A 0.8292 / -9.860, I684S 0.9672 / -13.622, A928V 0.9509 / -8.338, V362F 0.7239 / -5.632.
- Local score: `esm2_t6_8M_UR50D`, a 6-layer, 8M-parameter ESM-2 model. Score = `log P(mutant residue | local sequence context) - log P(wild-type residue | local context)`; more negative means the mutant is less likely to the model. It is **not** the ESM-1b score/class.
- Context window: 1,022 residues. For positions 684, 928 and 1104, the final 1,022-residue TYK2 window starts at residue 166; V362F uses residues 1–1,022.

## Results

| Variant | AlphaMissense (precomputed) | ESM1b (precomputed) | New local ESM-2 8M LLR | What direct experiments say | Interpretation |
|---|---:|---:|---:|---|---|
| P1104A / rs34536443 | 0.8292 | -9.860 | -3.035160 | Catalytically impaired; can retain signalling in appropriate context; homozygosity has IL-23/IFN-gamma-related infection susceptibility | All sequence predictors flag an unusual/damaging substitution, but they do not capture partial and pathway-specific function. |
| I684S / rs12720356 | 0.9672 | -13.622 | -4.769598 | Catalytically impaired but signalling competent; DMS reports reduced abundance but no significant IFN-alpha signalling change | Strongest ESM-2 penalty in this four-variant panel, yet experimental impact is not a universal LOF. |
| A928V / rs35018800 | 0.9509 | -8.338 | -4.588613 | Partial deficiency in compound-genotype context; phosphorylated after IL-12 stimulation in the patient-allele study | High predictor scores are compatible with a hypomorphic/pathway-specific allele, not necessarily complete deficiency. |
| V362F / rs2304256 | 0.7239 | -5.632 | -4.685082 | Common regulatory/splice-dose context; protein substitution itself was not defective in the cited tested systems | This is a quality-control warning: the secondary source labels its AlphaMissense class “likely benign” despite its reported numeric score being above commonly cited likely-pathogenic thresholds. Do not reuse that class/value without querying the official current record. |

## Reproducibility

```bash
.variant_predictors_venv/bin/python \
  JAK_mutation_effects_research/tyk2_predictors/score_tyk2_esm2.py
```

Input variants are in `tyk2_predictors/variants.tsv`; the captured output is in `tyk2_predictors/esm2_8m_results.tsv`. The script fetches the current UniProt FASTA and downloads the public checkpoint on first run.

## Primary experimental comparators

- [Two rare disease-associated TYK2 variants are catalytically impaired but signalling competent](https://pubmed.ncbi.nlm.nih.gov/23359498/) tests P1104A and I684S directly.
- [Inherited TYK2 deficiency study](https://pubmed.ncbi.nlm.nih.gov/36094518/) tests R864C, G634E, G996R, G1010D and A928V in addition to P1104A controls.
- [TYK2 deep-mutational scan](https://pubmed.ncbi.nlm.nih.gov/42268925/) provides IFN-alpha signalling and protein-abundance measurements across a large variant library; retrieve the per-variant supplement/dataset rather than inferring its numerical score from prose.

## What this comparison demonstrates—and does not

- It demonstrates that modern sequence-based predictors converge on high impact for several established TYK2 alleles, and that a lightweight, locally executable model ranks all four as sequence-unlikely.
- It does **not** validate an optimal cutoff, compare independent clinical classifiers fairly, diagnose a patient, determine a variant’s GOF/LOF direction, or predict signalling across all TYK2-dependent cytokines.
- The proper next comparison is a transcript-normalized VCF annotated with a pinned dbNSFP/VEP release, including AlphaMissense, EVE, REVEL, CADD, PrimateAI-3D, SpliceAI and conservation fields, followed by correlation against the 2026 TYK2 DMS per-variant measurements.
