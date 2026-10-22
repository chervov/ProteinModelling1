# JAK1/JAK2/JAK3/TYK2 mutation-effects research inventory

Prepared 2026-10-22. This is an annotated, auditable **starting inventory**, not a claim that every paper ever published has been captured. “Mutation effects” was interpreted broadly: experimentally tested germline or somatic variants, engineered mechanistic mutants, and high-throughput variant-effect assays. Papers that merely report a variant without testing an effect are excluded from the direct list unless they make a useful clinical/structural contribution.

## Files

- `01_direct_experimental_papers.md` — primary studies that test a mutation/variant or use informative engineered mutations.
- `02_indirect_evidence_and_resources.md` — structural, disease, review, and database resources that can help interpret an untested variant.
- `03_search_protocol_and_gaps.md` — exact scope, reproducible searches, exclusions, and questions that could uncover missing work.

## Bottom line

The evidence is not interchangeable across paralogues or contexts.

| Protein | Most mature mutation-effect literature | Main interpretive caution |
|---|---|---|
| JAK1 | Somatic GOF in leukemias/lymphomas and germline/mosaic immune dysregulation | A mutation may be cytokine-, receptor-, and cell-type-specific. |
| JAK2 | V617F and exon-12 MPN mutations; unusually rich JH2/JH1 structural genetics | V617F mechanisms and drug response cannot automatically be transferred to other JAKs. |
| JAK3 | Recessive loss-of-function SCID and somatic T-cell neoplasm variants | Many clinical alleles have only expression/signalling data, not purified-protein biochemistry. |
| TYK2 | Loss/partial loss in infection, P1104A autoimmune protection, and recent DMS | A signalling-competent kinase-impaired allele illustrates that catalytic activity alone is insufficient. |

## How to use this inventory

1. Normalize a query variant to HGVS against a stated transcript and genome build.
2. Check direct evidence first; record assay, zygosity/allele fraction, cell type, receptor/cytokine, and readout.
3. Use the indirect sources to formulate—not prove—a mechanism.
4. Triangulate clinical claims in ClinVar/ClinGen for germline and CIViC/OncoKB/COSMIC/cBioPortal for somatic cancer. Database assertions are curated evidence, not substitutes for an assay.
5. Retrieve the full text and supplements before making a clinical or mechanistic assertion. Titles/abstracts and an individual case are insufficient for pathogenicity classification.

## High-confidence cross-cutting conclusions

- The pseudokinase (JH2) domain is an active regulatory domain: pathogenic activation is frequently mediated by altered interdomain regulation rather than a simple increase in isolated kinase catalytic rate.
- Pairwise JAK/receptor context matters. For example, TYK2 and JAK1 can provide catalytic and scaffolding functions that are not equivalent in all cytokine pathways.
- Functional consequences are multidimensional: protein abundance, receptor stability, basal activity, ligand-induced activity, STAT specificity, transformation, drug response, and organismal phenotype can disagree.
- The most complete single-variant functional dataset in this four-protein set currently appears to be the 2026 TYK2 deep-mutational scan; it should still be treated as an assay- and condition-specific score, not a universal clinical label.

## Citation convention

Each paper has a stable PMID link when available. Where a DOI is known, it is supplied. Verify bibliographic fields through PubMed/Crossref before importing to a manuscript manager.
