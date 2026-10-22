# Mutation-effect prediction tools and databases: TYK2-focused landscape

Prepared 2026-10-22. “All possible tools” has no stable finite answer: methods are continually released, retired, updated and re-trained. This is a broad, practical survey; use the [VIPdb / VEP guideline paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC11998465/) and the current [dbNSFP](https://www.dbnsfp.org/) release as the discovery index for new methods.

## Best first-line annotation route

For small human missense batches, use the current [Ensembl VEP](https://www.ensembl.org/Tools/VEP/) with appropriate plugins/data, or query [dbNSFP](https://www.dbnsfp.org/). VEP can report consequence and available external scores including AlphaMissense, CADD, SIFT, REVEL, SpliceAI, MaveDB and EVE; dbNSFP v5 aggregates far more precomputed tools and conservation features. Pin genome build, transcript, database release and query date.

## Predictor families

| Family / examples | Input and output | Installation / access | Best use | Key limitation |
|---|---|---|---|---|
| Sequence conservation | SIFT, SIFT4G, PROVEAN, GERP++, phyloP, phastCons | VEP/dbNSFP; SIFT4G/PROVEAN local with large homology/BLAST assets | Conserved-residue prioritization | Conservation does not determine direction (GOF versus LOF) or cell context. |
| Classical protein-function | PolyPhen-2, MutationAssessor, MutationTaster, FATHMM, FATHMM-XF | VEP/dbNSFP; some web/local legacy tools | Fast, interpretable historical baseline | Correlated training/features; older calibration and versioning matter. |
| Ensemble pathogenicity | REVEL, MetaSVM, MetaLR, MetaRNN, BayesDel, M-CAP, MPC, MVP, ClinPred, VARITY, VEST4, DANN, Eigen | Primarily dbNSFP/VEP/annotation services | Clinical missense prioritization | Combining correlated predictors does not create independent evidence. |
| Deep evolutionary / language models | EVE, ESM-1b, ESM-1v, ESM-2, popEVE, GPN-MSA, DeepSequence, GEMME | EVE / precomputed portals; ESM local Python; many scores in dbNSFP | Broad sequence-function plausibility | Model likelihood is not a disease mechanism or a clinical classification. |
| Structure-aware ML | AlphaMissense, PrimateAI-3D, MutFormer, PHACTboost, MisFit | AlphaMissense database/VEP/dbNSFP; models vary in public local availability | Missense pathogenicity prioritization | Predicted structures/embeddings are not functional assays; calibration is gene and phenotype dependent. |
| Mechanistic/feature-level | MutPred2, MutPred-PPI, Mutfunc, DynaMut2, FoldX, Rosetta | Web/local; MutPred2 requires legacy MATLAB and large assets; FoldX licensing applies | Stability, interface, PTM or molecular mechanism hypotheses | A protein-stability prediction may miss signalling/scaffolding effects. |
| Splicing / noncoding | SpliceAI, Pangolin, MMSplice, CADD, LINSIGHT, Eigen-PC, REMM | VEP plugins/online/local depending on tool | Essential for splice, synonymous and regulatory variants | Most missense predictors are inapplicable to these variants. |
| Multimodal phenotype ranking | Exomiser, LIRICAL, AMELIE, Phen2Gene | Local/container or web, with phenotype terms + VCF | Rare-disease diagnosis ranking | They prioritize gene/variant plausibility, not direct biochemical effect. |
| Experimental truth resources | MaveDB, ProteinGym, DMS papers, ClinVar functional evidence | Online data/resources | Benchmarking and direct assay lookup | Assay readout, dose, cell type and receptor pathway limit transferability. |

## Databases and portals

| Resource | What it provides | Practical role for TYK2 |
|---|---|---|
| [dbNSFP](https://www.dbnsfp.org/) | Precomputed values for dozens of missense/splice predictors and conservation metrics; downloadable/tabix and browser | Largest single-score aggregation; excellent batch annotation starting point. |
| [Ensembl VEP](https://www.ensembl.org/Tools/VEP/) | Variant consequence, transcript mapping, plugins/scores, MaveDB links | Transcript/build normalization plus a reproducible annotation command. |
| [AlphaMissense](https://alphafold.ebi.ac.uk/faq) | Proteome-wide missense pathogenicity scores/classes | Strong modern missense baseline; inspect score/provenance rather than only class. |
| [EVE](https://evemodel.org/) | Evolutionary variant-effect scores/classes | Independent evolutionary signal; scores are normalized within protein and are not cross-protein comparable. |
| [UCSC prediction tracks](https://genome.ucsc.edu/cgi-bin/hgTrackUi?db=hg38&g=predictionScoresSuper) | CADD, REVEL, EVE and related genome-browser tracks | Convenient visual cross-check and coordinate validation. |
| [MaveDB](https://mavedb.org/) / [ProteinGym](https://proteingym.org/) | Experimental multiplexed-assay data / benchmarks | Search for deposition of the 2026 TYK2 DMS source data; prefer actual scores to predictor scores. |
| [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/) / [ClinGen](https://clinicalgenome.org/) | Clinical assertions, submitter evidence, gene-disease curation | Clinical context and source papers; not a functional-prediction engine. |
| [gnomAD](https://gnomad.broadinstitute.org/) | Population frequencies and coverage | Frequency filters; do not use frequency as a functional assay. |
| [COSMIC](https://cancer.sanger.ac.uk/cosmic), [cBioPortal](https://www.cbioportal.org/), [CIViC](https://civicdb.org/), [OncoKB](https://www.oncokb.org/) | Cancer occurrence/curation/actionability | Use for somatic TYK2 and other JAK cancer alleles; distinguish recurrence from functional proof. |
| [UniProt P29597](https://www.uniprot.org/uniprotkb/P29597) / [RCSB PDB](https://www.rcsb.org/) / [AlphaFold DB](https://alphafold.ebi.ac.uk/entry/P29597) | Canonical sequence, curated variants/domains, experimental/predicted structures | Variant normalization and structure-based hypothesis formation. |

## What can be installed locally here

| Method | Status in this workspace | Notes |
|---|---|---|
| `fair-esm` + ESM-2 8M | **Installed and executed** in `.variant_predictors_venv` | Public package, PyTorch and checkpoint installed. Results are in `tyk2_predictors/esm2_8m_results.tsv`. |
| ESM-1v / ESM-1b | Installable with the same framework, **not run** | Requires a much larger model checkpoint; ESM-1v is the more relevant ESM family for mutation effect scoring. |
| Ensembl VEP + cache/plugins | Installable, **not installed** | Useful production annotator but requires cache/database/plugin downloads; online REST timed out from this runtime. |
| dbNSFP | Downloadable, **not downloaded** | Very large genome-scale data; use the browser/small-batch service or tabix subset for a later batch. |
| EVE | Code/precomputed results accessible, **not locally run** | Building a gene-specific evolutionary model needs homolog collection and training resources. |
| SIFT4G / PROVEAN | Installable, **not installed** | Useful only with large reference/homology databases. |
| PolyPhen-2 | Legacy local/web option, **not installed** | Prefer obtaining pinned precomputed values through VEP/dbNSFP. |
| MutPred2 | Public but **not installed** | Official site documents legacy MATLAB dependency and roughly 50 GB disk requirement. |
| FoldX / Rosetta / DynaMut2 | Potentially usable, **not installed** | Need a specific TYK2 structure/construct and careful handling of JAK conformational states; not a first-pass clinical predictor. |

## Do not average these indiscriminately

dbNSFP contains many overlapping methods. A score panel is useful for detecting disagreement and generating hypotheses, but an average of several correlated predictors is not independent confirmation. For TYK2 specifically, P1104A and I684S demonstrate why a high “damaging/pathogenic” score can coexist with pathway-specific or partial effects: the **2025 bioRxiv preprint** DMS reports no significant IFN-alpha signalling effect for I684S despite reduced abundance, while earlier work shows catalytic impairment with retained signalling competence. Use the exact MaveDB score set and condition; the preprint is not peer-reviewed. [TYK2 preprint](https://doi.org/10.1101/2025.10.11.681520), [functional study](https://pubmed.ncbi.nlm.nih.gov/23359498/).
