# Search protocol, audit trail, and gaps

## Scope and cutoff

- Search executed: 2026-10-22.
- Proteins/genes: human `JAK1`, `JAK2`, `JAK3`, `TYK2` / `tyrosine kinase 2`; include historical `Jak` spelling.
- Included: functional studies of observed or engineered variants; variant-rich functional screens; structural studies that explicitly test a mutation.
- Separated: disease association/sequencing-only work, reviews, models/MD without experiment, and database entries are supporting—not direct—evidence.
- No language restriction was intended, but English-language indexing and abstract availability bias the present inventory.

## Reproducible PubMed searches

Run each query without a date filter, export all fields (PMID, DOI, abstract, publication type), deduplicate by PMID/DOI, then screen full text and supplements.

```text
(JAK1[Title/Abstract] OR Janus kinase 1[Title/Abstract]) AND
(mutation OR variant OR mutant OR missense OR "gain of function" OR "loss of function") AND
(functional OR signaling OR signalling OR activity OR phosphorylation OR transformation OR "deep mutational")

(JAK2[Title/Abstract] OR Janus kinase 2[Title/Abstract]) AND
(mutation OR variant OR mutant OR V617F OR "exon 12") AND
(functional OR signaling OR signalling OR activity OR phosphorylation OR transformation OR structural)

(JAK3[Title/Abstract] OR Janus kinase 3[Title/Abstract]) AND
(mutation OR variant OR mutant OR SCID OR leukemia OR leukaemia) AND
(functional OR signaling OR signalling OR activity OR phosphorylation OR transformation)

(TYK2[Title/Abstract] OR "tyrosine kinase 2"[Title/Abstract]) AND
(mutation OR variant OR mutant OR P1104A OR deficiency) AND
(functional OR signaling OR signalling OR activity OR phosphorylation OR "deep mutational")
```

### Supplementary retrieval searches

```text
("JAK1" OR "JAK2" OR "JAK3" OR "TYK2") AND
("variant of uncertain significance" OR VUS OR "patient-derived" OR "germline" OR "somatic")

(("JAK1" OR "JAK2" OR "JAK3" OR "TYK2") AND
(structure OR cryo-EM OR crystall* OR "molecular dynamics" OR "AlphaFold") AND (mutation OR mutant))

(("JAK1" OR "JAK2" OR "JAK3" OR "TYK2") AND
("drug resistance" OR inhibitor OR ruxolitinib OR tofacitinib OR deucravacitinib) AND (mutation OR variant))
```

## Mandatory screening fields

Use a spreadsheet or reference database with: PMID; DOI; gene; transcript and build; HGVS c./p.; rsID/COSMIC ID; germline/somatic/engineered; disease and cohort; zygosity/VAF; model; receptor/cytokine; assay; direction and magnitude; controls; replication; drug; conclusion; limitations; full-text/supplement access.

## What this search could still miss

1. **Terminology drift.** Older papers use `Jak`, `JH1`, `JH2`, `PTK`, “pseudokinase,” or a mutation name without placing the gene in title/abstract.
2. **JAK2 scale.** JAK2 V617F literature is vast. Many papers test combinations of V617F with receptor, STAT, adaptor, or inhibitor perturbations; a full review needs a formal systematic-review workflow and possibly a defined question (activation mechanism, clinical disease, or therapy resistance).
3. **Allele-level granularity.** One paper may test a long panel. Conversely, a reported variant might never have been functionally assayed. Never extend the paper’s conclusion to untested substitutions in the same domain.
4. **Noncoding and splice effects.** The TYK2 splicing/dosage study shows why protein-only searches will miss functional regulatory alleles. Expand to eQTL/sQTL and RNA studies if these variants matter.
5. **Cancer versus inherited disease.** A somatic allele’s transforming effect does not establish germline pathogenicity; a recessive loss allele does not predict a tumour allele’s behaviour.
6. **Preprints and indexing lag.** Newly released 2026 work may be absent from one index or change after peer review.
7. **Negative data.** Failed functional tests and neutral variants are underpublished; seek supplementary tables, MaveDB, ClinVar submitter evidence and systematic saturation screens.

## Self-critique and questions for you

- “All papers” needs a boundary. Do you want every paper that *mentions* a mutation, or only primary experiments that measure a molecular/cellular/clinical effect? The latter is the boundary used here.
- Should species-specific engineered mutants (mouse/zebrafish) be co-equal with human variants, or placed in a separate mechanistic appendix?
- Is the target a particular variant set, disease area (MPN, T-ALL, SCID, infection, autoimmunity), or drug-resistance question? A focused second pass can be much more exhaustive.
- Do you need a machine-readable CSV/BibTeX library with full author/journal/DOI metadata? That requires a database export and full-text/supplement screening, not just a web search.

## Next rigorous step

Export the four core PubMed searches to CSV, combine them, deduplicate, and screen titles/abstracts in duplicate against the inclusion rule. Then perform backward/forward citation chaining from the landmark papers in `01_direct_experimental_papers.md`, including “cited by” results in Europe PMC/OpenAlex. Record the final PRISMA-style counts and unresolved full texts. That is the defensible path to an exhaustive literature review.
