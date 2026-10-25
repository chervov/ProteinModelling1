# OMIM allelic variants for JAK2 (MIM 147796), and what R715T tells us

Read from [omim.org/allelicVariants/147796](https://omim.org/allelicVariants/147796) on 25 Oct 2026. OMIM is a curated, literature-backed source: a handful of selected variants per gene, each tied to a publication and usually to functional work. It is **complementary to ClinVar** (thousands of submitted variants, mostly uncertain) rather than a substitute. The full list for all four JAK genes is in [`omim_allelic_variants.csv`](../omim_allelic_variants.csv), and an `OMIM allelic variant` column has been added to the JAK1/JAK2/JAK3/TYK2 variant tables.

## The five JAK2 allelic variants

| OMIM | Variant | Phenotype |
|---|---|---|
| 147796.0001 | **V617F** | Polycythemia vera, thrombocythemia 3, myelofibrosis, erythrocytosis, AML, Budd-Chiari syndrome (all somatic) |
| 147796.0002 | **K607N** | Acute myelogenous leukemia, somatic |
| 147796.0003 | **K539L** | JAK2-related erythrocytosis, somatic (exon 12) |
| 147796.0004 | **V617I** | Thrombocythemia 3 |
| 147796.0005 | **R715T** | Variant of unknown significance; germline PV-like erythrocytosis in three generations |

The first four are the classical somatic myeloproliferative-neoplasm alleles. The fifth is new and is the reason this page is worth reading.

## 147796.0005 - JAK2 R715T

**Song J, Lanikova L, Kim SJ, Papadopoulos N, Meznarich J, Constantinescu SN, Parsegov B, Prchal JF, Prchal JT.** Novel germline JAK2 R715T mutation causing PV-like erythrocytosis in 3 generations: amelioration by Ropeg-interferon. *Am J Hematol* 2024;99:1220-1229. PMID [38629639](https://pubmed.ncbi.nlm.nih.gov/38629639/).

- Proband: 38-year-old woman, thrombotic stroke and polycythemia-vera-like erythrocytosis, **negative for V617F and exon 12 mutations**.
- **R715T in the pseudokinase (JH2) domain**, 47.5% allele fraction, also present in nail DNA - i.e. **germline**, not clonal haematopoiesis.
- Her 68-year-old mother and 11-year-old son also carried it with erythrocytosis (**three generations**); proband and mother had **polyclonal** myelopoiesis, excluding a somatic clone.
- **Functional gain of function:** erythropoietin-independent erythroid progenitor growth, increased STAT5 phosphorylation, up-regulated prothrombotic and inflammatory transcripts, and increased JAK2 kinase activity in vitro - the V617F-like pattern.
- **Treatment:** JAK inhibitors were not tolerated; **ropeg-interferon-alpha-2b** produced remission and reduced JAK2 activity in proband and mother.

## Why this matters for this project

**1. A positive control for the computational pipeline.** R715T was already in our table as ClinVar *uncertain significance*. Every predictor we use calls it damaging, and it is now a proven gain-of-function variant:

| Variant | AlphaMissense | REVEL | CADD | SIFT | PolyPhen-2 | MetaRNN | ESM1b | EVE | ClinVar | gnomAD AC |
|---|---|---|---|---|---|---|---|---|---|---|
| **R715T** | 0.96 (likely pathogenic) | 0.79 | 28.7 | 0.000 | 0.982 | 0.90 | -14.9 | 0.81 | Uncertain significance | 13 |

So on this case the predictors were right and ClinVar's "uncertain" was conservative - a reminder that a VUS with a unanimous damaging prediction in a JH2 position deserves functional follow-up.

**2. Independent support for reading the TYK2 deep mutational scan as an activation assay.** R715 is conserved across the family (JAK1 R755, JAK3 R687, **TYK2 R775**). In the TYK2 scan, substitutions at the equivalent R775 **increase** IFN-alpha signalling:

| TYK2 substitution | DMS signalling | Abundance |
|---|---|---|
| R775E | **+1.07 +- 0.37** (99.7th percentile of the whole scan) | -0.31 |
| R775A | +0.98 +- 0.48 | -0.02 |
| R775V | +0.72 +- 0.49 | -0.08 |
| R775C | +0.59 +- 0.42 | -0.05 |

Position R775 ranks in the **most activating 17%** of TYK2 positions (mean +0.02 against a scan median of -0.12). A position where a germline gain of function is proven in JAK2 therefore scores positive in the TYK2 scan, which supports treating positive scan scores as a gain-of-function signal rather than noise.

**3. Context for the priority variants.** Comparing the TYK2 equivalents of the JAK2 variants under study (see [`jak2_homology_inf.md`](jak2_homology_inf.md)):

| JAK2 variant | TYK2 equivalent position | Rank among TYK2 positions (most activating first) |
|---|---|---|
| **R715T** (proven gain of function) | R775 | top 17% |
| G571R | G634 | top 11% |
| L805I | L866 | bottom 14% overall, but L866I itself +0.57 |
| V578I | V639 | bottom 5% (loss-prone position) |

**4. A different clinical frame.** The germline JAK2 story is **familial erythrocytosis with thrombosis, V617F-negative**, not only somatic myeloproliferative neoplasia. If one of the variants under study is activating, that is the phenotype to look for in carriers - and this report provides a treatment precedent (ropeg-interferon-alpha-2b) for patients who do not tolerate JAK inhibitors.

## Note on coverage

OMIM lists *selected* examples, not a complete variant catalogue: 4 variants for JAK1, 5 for JAK2, 7 for JAK3, 12 for TYK2. Of these, the ones expressible as a simple protein change are annotated in our tables (JAK1 5, JAK2 5, JAK3 5, TYK2 7); the remainder are indels described only at nucleotide level in OMIM. Absence of an OMIM entry says nothing about a variant.
