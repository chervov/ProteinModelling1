# Indirect evidence, structures, and data resources

## Indirect papers that materially help interpretation

| Area | Resource | Why it helps | Caveat |
|---|---|---|---|
| Shared activation mechanism | [Structure of a pseudokinase-domain switch that controls oncogenic activation of JAK kinases](https://pubmed.ncbi.nlm.nih.gov/24013208/) | Relates JAK2 V617F and analogous JAK1 V658F behaviour; useful paralogue framework. | Homology is evidence-generating, not proof for a residue in another JAK. |
| JAK trans-activation structure | [Structural basis of Janus kinase trans-activation](https://pmc.ncbi.nlm.nih.gov/articles/PMC10180219/) | Cryo-EM/structural framework for active versus autoinhibited JAK configurations. | Receptor/ligand state and species/construct determine relevance. |
| Human genetic disease overview | [Inborn errors of human JAKs and STATs](https://pubmed.ncbi.nlm.nih.gov/22520845/) | Places JAK3 and TYK2 loss-of-function within cytokine-pathway disease. | Review, not a variant assay source. |
| Pan-JAK malignancy structures | [Structural analysis of Janus kinase variants in hematological malignancies](https://www.mdpi.com/1422-0067/24/19/14573/xml) | Practical full-length modelling templates and disease hotspots across JAKs. | Review/modelling; inspect source studies. |
| Older family-wide reference | [The Janus kinases](https://pmc.ncbi.nlm.nih.gov/articles/PMC545791/) | Conserved domains, paralogue comparisons, orthologue alignment resources. | Predates modern structures and variant databases. |

## Protein and structural resources

| Resource | JAK1 | JAK2 | JAK3 | TYK2 | Use responsibly |
|---|---|---|---|---|---|
| UniProt | [P23458](https://www.uniprot.org/uniprotkb/P23458) | [O60674](https://www.uniprot.org/uniprotkb/O60674) | [P52333](https://www.uniprot.org/uniprotkb/P52333) | [P29597](https://www.uniprot.org/uniprotkb/P29597) | Canonical sequence, domains, curated variants/PTMs and cross-links. Freeze accession version/date. |
| AlphaFold DB | Search [JAK1](https://alphafold.ebi.ac.uk/entry/P23458) | Search [JAK2](https://alphafold.ebi.ac.uk/entry/O60674) | Search [JAK3](https://alphafold.ebi.ac.uk/entry/P52333) | Search [TYK2](https://alphafold.ebi.ac.uk/entry/P29597) | Use confidence/PAE, particularly at domain interfaces; models do not establish active state or mutation effect. |
| RCSB PDB | [JAK1 model](https://www.rcsb.org/structure/AF_AFP23458F1) | [Search](https://www.rcsb.org/search) | [Search](https://www.rcsb.org/search) | [Search](https://www.rcsb.org/search) | Prefer experimental domain/complex structures where available; record construct, ligands, resolution and species. |
| InterPro/Pfam | [InterPro search](https://www.ebi.ac.uk/interpro/search/text/JAK1/) | [InterPro search](https://www.ebi.ac.uk/interpro/search/text/JAK2/) | [InterPro search](https://www.ebi.ac.uk/interpro/search/text/JAK3/) | [InterPro search](https://www.ebi.ac.uk/interpro/search/text/TYK2/) | Consistent domain boundaries for mapping. |

## Germline and rare-disease resources

| Resource | What to obtain | Interpretation warning |
|---|---|---|
| [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) | Submitter-level assertions, review status, condition, phenotype and last-evaluated date; query each gene and exact HGVS. | Conflicting or single-submitter records are not consensus truth. |
| [ClinGen](https://clinicalgenome.org/) | Gene-disease validity and expert-panel specifications, if available for the disease. | Gene-level validity does not classify every variant. |
| [gnomAD](https://gnomad.broadinstitute.org/) | Allele count/frequency, ancestry distribution and coverage. | Absence is weak evidence; mosaic somatic variants are outside its purpose. |
| [OMIM](https://omim.org/) | Curated gene-phenotype historical references. | Licensing/access may constrain bulk use. |
| [Orphanet TYK2](https://www.orpha.net/en/disease/gene/TYK2) and [Orphanet JAK3-SCID](https://www.orpha.net/en/disease/detail/35078?mode=name) | Disease summaries, coding, and rare-disease context. | Not a variant-level functional database. |
| [NCBI Gene: JAK3](https://www.ncbi.nlm.nih.gov/gene/3718) / [TYK2](https://www.ncbi.nlm.nih.gov/gene/7297) | Links to RefSeq, GTR, phenotype and bibliography. | Verify transcript before translating residue numbers. |

## Somatic cancer and functional-genomics resources

| Resource | Best use |
|---|---|
| [COSMIC](https://cancer.sanger.ac.uk/cosmic) | Observed somatic variants, tumour context and recurrence; use accession/date and distinguish curated from raw data. |
| [cBioPortal](https://www.cbioportal.org/) | Cohort-level mutation, co-alteration, expression and outcome exploration. It reports occurrence, not automatically functional effect. |
| [CIViC](https://civicdb.org/) | Open, evidence-linked cancer variant interpretations; inspect evidence level/status. |
| [OncoKB](https://www.oncokb.org/) | Curated oncogenicity and treatment implications. Its FAQ explicitly separates cBioPortal occurrence data from OncoKB effect/therapeutic annotations. |
| [Cancer Genome Interpreter](https://www.cancergenomeinterpreter.org/) | Driver/passenger and biomarker interpretation; track release/version. |
| [DepMap](https://depmap.org/portal/) | Dependency and cell-line genomic context; useful for hypothesis generation around JAK addiction. |
| [CCLE](https://sites.broadinstitute.org/ccle/) | Cell-line mutation/expression context and model selection. |
| [MaveDB](https://mavedb.org/) | Search for multiplexed assays of variant effect. Check whether the TYK2 DMS data were deposited and cite the dataset version. |

## Assay and literature discovery resources

| Resource | Practical purpose |
|---|---|
| [PubMed](https://pubmed.ncbi.nlm.nih.gov/) | Controlled, reproducible biomedical literature search; use MeSH plus free text and export PMID/PMCID/DOI. |
| [Europe PMC](https://europepmc.org/) | Citation network, open full text, preprints and API-friendly export. |
| [OpenAlex](https://openalex.org/) | Citation chaining and works/author/institution graph. |
| [bioRxiv](https://www.biorxiv.org/) / [medRxiv](https://www.medrxiv.org/) | Recent preprints; label clearly as non-peer-reviewed. |
| [ClinicalTrials.gov](https://clinicaltrials.gov/) | Variant-stratified interventional evidence and trial status; not a proof of mutation effect. |

## Recommended interpretation matrix

For every variant, record these axes instead of a single “functional” label: (1) abundance/stability, (2) receptor binding/scaffolding, (3) basal phosphorylation, (4) ligand-specific STAT response, (5) transcriptional programme, (6) growth/transformation, (7) organismal/clinical phenotype, (8) inhibitor response. A result on one axis cannot substitute for the others.
