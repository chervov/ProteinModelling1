# Mutation effects in human kinases

**Coverage through 1 November 2026.** This overview covers 15 primary research and methods papers published since January 2024, plus one variant-effect atlas. The scope is the [41 modelling targets](criterion3_coverage.csv) plus JAK1, JAK2, JAK3 and TYK2. Kinome-wide studies are included when their data or software can be applied to these targets. The [480-kinase structural survey](kinome480_report.md) provides the broader context.

**How large is the literature?** The initial planning estimate was on the order of hundreds of relevant papers across the 45 genes when experimental, structural, computational, expression and drug-response studies are all included. The estimate has yet to be tested by a systematic gene-by-gene search and deduplication. The 15 papers below are the documented first pass. Several cover multiple genes.

## Structural mechanisms and functional experiments

| Protein | Study and evidence | Relevance to mutation modelling |
|---|---|---|
| LRRK2 | Cryo-EM and structure-guided mutagenesis showed how a 14-3-3 dimer stabilizes inactive LRRK2. Parkinson’s-associated mutations at the COR interface and in the GTPase domain weakened 14-3-3 binding. [Nature Communications, 2025](https://pubmed.ncbi.nlm.nih.gov/40764514/) | A direct test of whether a distal mutation disrupts a partner that stabilizes the inactive state. Include the partner when modelling the interface. |
| LRRK2 | Cryo-EM, biochemical reconstitution and cell assays linked the nucleotide state of the ROC GTPase to kinase activation. GTP favored activation and GDP favored autoinhibition. [Cell, 2026](https://pubmed.ncbi.nlm.nih.gov/42575089/) | Experimentally supported reference conformations for interpreting distal mutations. The states alone do not establish a particular variant’s effect. |
| BTK, HCK | In a study of full-length BTK, catalytically inactive BTK L528W activated HCK. This required the proline-rich region of BTK. [Full-length BTK conformation and resistance study](https://pmc.ncbi.nlm.nih.gov/articles/PMC11677227/) | Score BTK catalytic activity and downstream signaling separately. A model of the isolated kinase domain misses the region required for the HCK effect. |
| BTK | Biochemical and cellular experiments compared resistance alleles and tested the degrader NX-2127. C481S retained near-WT catalytic behavior, whereas other resistance alleles impaired catalysis. [Kinase-impaired BTK mutations and NX-2127, 2024](https://pmc.ncbi.nlm.nih.gov/articles/PMC11103405/) | Distinguishes kinase activity, drug resistance and dependence on the physical presence of BTK. |
| ABL1 | N-lobe mutations in BCR::ABL1 conferred resistance to asciminib, which targets the myristoyl pocket in the C-lobe. [Blood, 2024](https://pubmed.ncbi.nlm.nih.gov/38643492/) | A distal-resistance test set. Retain the fusion context when interpreting results for ABL1. |
| BRAF | LABEL-seq produced approximately 20,000 measurements for 1,600 BRAF variants. At recurrent cancer positions, substitutions could alter activity, partner interactions or drug response while leaving intracellular abundance relatively unchanged. [Nature Methods, 2024](https://www.nature.com/articles/s41592-024-02456-7) | Compare several readouts for the same substitution to distinguish impaired abundance from altered interactions or signaling. |
| INSR | A scan of approximately 14,000 extracellular missense variants measured cell-surface expression, insulin binding and stimulated signaling. [Nature Communications, 2025](https://pubmed.ncbi.nlm.nih.gov/41093840/) | Directly relevant to the ectodomain models. Ask which variants preserve surface expression but impair binding or signaling. |
| JAK1 | scSNV-seq paired direct single-cell genotyping with RNA profiling after interferon-γ stimulation. WT comparisons distinguished benign, loss-of-function and separation-of-function missense variants. [Genome Biology, 2024](https://pubmed.ncbi.nlm.nih.gov/38225637/) | A source of measured expression phenotypes for testing hypotheses from JAK1 open/closed models. The RNA readout does not directly measure conformation. |

## Functional maps and drug response

| Target | Measurements | Potential use |
|---|---|---|
| CHEK2 | Multiplexed functional complementation measured the effects of human CHK2 missense variants. [American Journal of Human Genetics, 2024](https://pubmed.ncbi.nlm.nih.gov/39642869/) | Benchmark functional impairment while retaining the assay system as part of each label. |
| MET | Deep mutational scanning profiled approximately 5,764 kinase-domain variants against 11 inhibitors. [MET resistance map](https://pmc.ncbi.nlm.nih.gov/articles/PMC11832172/) | Compare different drug responses for the same substitution. |
| FGFR1–4 | Saturation mutagenesis screened 11,520 possible point mutations across four kinase domains for activation and inhibitor resistance. [FGFR saturation mutagenesis study](https://pubmed.ncbi.nlm.nih.gov/41361008/) | Test whether homologous substitutions have consistent effects across paralogs. FGFR1, FGFR2 and FGFR4 are on the 41-gene list. |
| ALK | A functional atlas recovered established resistance alleles including G1202R and L1196M and identified drug-specific and shared resistance profiles. [ALK variant atlas, 2026](https://pubmed.ncbi.nlm.nih.gov/41630044/) | Separate broadly resistant variants from those whose effect depends on the inhibitor. |
| Multiple kinases | Biochemical profiling tested 86 approved inhibitors against 409 WT kinases and 349 oncogenic variants. [Nature Biotechnology, 2026](https://pubmed.ncbi.nlm.nih.gov/42010121/) | An independent biochemical comparison for interpreting cell-growth screens. |

## Computational methods and reusable resources

| Method or resource | Coverage and use |
|---|---|
| Kinase variant classifier | The authors curated 2,505 variants across 441 kinases with activating, deactivating, resistance and neutral labels. The dataset and classifier provide a baseline for testing the added value of structural features. [Methods paper, 2025](https://pubmed.ncbi.nlm.nih.gov/41152984/) · [Code](https://github.com/russelllab/kinaseResistance) |
| Structure-based kinase mutation interpretation tool | This web resource uses structural context to interpret kinase mutations found by clinical sequencing. The authors tested selected activation predictions in cells. [Methods paper, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12358288/) |
| MAPK Variant Effect Atlas | The atlas reports 186,676 variants across 17 RAS–MAPK pathway proteins, with measurements of intracellular abundance and pathway activity. Counted here as a data resource. [Explore the atlas](https://mapk.gs.washington.edu/index.html) |

## First comparisons for open/closed modelling

**LRRK2** offers the clearest connection between a disease-associated mutation, a physical interface and stabilization of an inactive state. **BTK L528W** tests a different mechanism: loss of intrinsic catalysis with signaling through another kinase. **INSR** and **BRAF** offer the largest opportunities here to compare distinct readouts for the same substitution. **JAK1** provides an expression-based test of whether a structural hypothesis can explain selective functional changes after stimulation.

For each comparison, record the substitution, experimental construct, partner or ligand, WT comparator, and measured phenotype. A change in an inter-domain distance is a structural hypothesis. Partner binding, enzyme activity, cell-surface abundance, drug response and RNA expression each test a different consequence.
