# JAK2 L805I: homologous positions, predictors and evidence

**Aligned positions: JAK2 L805 ↔ JAK1 I845 ↔ JAK3 L777 ↔ TYK2 L866.**

Research date: 25 October 2026. This is a scientific evidence review, not a formal clinical classification. Comparisons replace each aligned residue with the target amino acid I; they do not assume that the original residues or effects are identical.

## Predictor comparison

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK2 L805I | 0.1504; likely benign | 0.01; deleterious_low_confidence | 0.78; possibly_damaging | 0.439 | 25.6 | -0.96 |
| JAK1 I845I | N/A: unchanged residue | N/A | N/A | N/A | N/A | N/A |
| JAK3 L777I | 0.1147; likely benign | 0.01; deleterious | 0.327; benign | 0.568 | 24.4 | -1.07, -1.03 |
| TYK2 L866I | 0.1136; likely benign | 0.02; deleterious | 0.305; benign | 0.343 | 23.3 | -0.95, -1 |

**All four original JAK2 variants have low-confidence SIFT labels in the current VEP response. Those labels must be retained. None of these scores establishes GOF, LOF or drug response.**

## Local alignment

Each pair below has the target at the eleventh alignment column; dashes are gaps.

```text
JAK2 RPSFRAIIRDLNSLFTPDYEL
JAK1 RPFFRAIMRDINKLEEQNPDI
               ^

JAK2 RPSFRAIIRDLNSLFTPDYEL
JAK3 RPSFRAVIRDLNSLISSDYEL
               ^

JAK2 RPSFRAIIRDLNSLFTPDY-E
TYK2 RPSFRTILRDLTRLQPHNLAD
               ^

```

## Alleles used for prediction

| Protein | Protein change | Coding query | Codon change | Minimum changed bases |
|---|---|---|---|---|
| JAK2 | L805I | ENST00000381652:c.2413C>A | CTT→ATT | 1 |
| JAK1 | I845I | Not applicable | ATT | 0 |
| JAK3 | L777I | ENST00000458235:c.2329C>A | CTC→ATC | 1 |
| TYK2 | L866I | ENST00000525621:c.2596C>A | CTC→ATC | 1 |

## Evidence and interpretation

L805 is near the end of JH2 (UniProt 545–809). The substitution is conservative, but context matters. An informative alignment result is that **JAK1 already carries isoleucine at I845**, the corresponding position. Thus the comparison I845→I is unchanged protein, not a missense mutant; it has no meaningful missense pathogenicity score. This natural paralog difference supports tolerance as a hypothesis, but cannot prove that JAK2 L805I is neutral.

**Exact observation:** L805I is present in CCLE Broad 2019 in the osteosarcoma cell line **SARC9371_BONE**, GRCh37 chr9:5080662 C>A. It is also listed in supplementary Table 2 of [Diaz et al., 2026, Landscape and functional impact of variants of unknown significance of immune response genes in human cancer](https://www.nature.com/articles/s41417-026-01024-9). The [final supplement](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41417-026-01024-9/MediaObjects/41417_2026_1024_MOESM3_ESM.pdf) contains the row on PDF page 7. A catalogue entry in a paper with “functional impact” in its title is not evidence that every listed variant was individually functionally validated. No L805I-specific assay or drug-response result was established here.

**Prediction provenance discrepancy:** that table reports SIFT **0.30, tolerated**, PolyPhen-2 **0.773, possibly damaging**, and AlphaMissense **0.1504, benign**. The current canonical VEP query returns SIFT **0.01, deleterious_low_confidence**, and PolyPhen-2 **0.780, possibly damaging**. Canonical AlphaMissense remains **0.1504**. Both source sets are preserved; the reason for the SIFT difference was not established. It may reflect annotation/version inputs, but that explanation has not been verified.

The current exact-L805I COSMIC-index query returns no match despite the CCLE observation. Position-level L805= is synonymous and must not be counted as L805I. In the homologous protein, **TYK2 L866I** is present in two returned rows sharing **COSM6229424**, with colorectal carcinoma metadata and no PMID. These are catalogue records, not two confirmed independent patients. TYK2 L866H is separately linked to [PMID 34778799, Integrative Genomic Analysis of Pediatric Myeloid-Related Acute Leukemias](https://pubmed.ncbi.nlm.nih.gov/34778799/); that different substitution supplies no L866I or L805I functional direction. JAK3 L777= is synonymous, not L777I.

The region lies within the broad C-terminal JH2 inhibitory segment examined by [Saharinen et al., 2003, PMID 12686600](https://pmc.ncbi.nlm.nih.gov/articles/PMC153113/). Those deletion/mutagenesis experiments support domain-level regulation, not an L805I-specific effect.

**Functional call: unresolved.** AlphaMissense 0.1504, PROVEAN -0.96 and the JAK1 reference isoleucine support a tolerance hypothesis, while other predictors flag possible effects. None establishes an immune-checkpoint resistance or JAK-inhibitor sensitivity biomarker.

## Methods, score meanings and limitations

Canonical UniProt sequences: [JAK1 P23458](https://rest.uniprot.org/uniprotkb/P23458.json), [JAK2 O60674](https://rest.uniprot.org/uniprotkb/O60674.json), [JAK3 P52333](https://rest.uniprot.org/uniprotkb/P52333.json), [TYK2 P29597](https://rest.uniprot.org/uniprotkb/P29597.json). Pairwise global affine-gap BLOSUM62 alignments used gap-open 10/extension 0.5, comparing full proteins with domain segments expanded by 30 residues. Additional domain-only checks used 8/0.5, 10/0.5 and 12/1. All mappings were stable in these checks except G571→JAK1, reported explicitly. This is sequence alignment, not structural superposition or proof of equivalent biochemical effects.

AlphaMissense scores are from EMBL-EBI canonical protein all-substitution files (https://alphafold.ebi.ac.uk/files/AF-ACCESSION-F1-aa-substitutions.csv). SIFT/PolyPhen-2 are selected for the queried Ensembl transcript, with returned codon, residue and substitution verified. REVEL/CADD/PROVEAN are from exact genomic-allele MyVariant.info/dbNSFP records. Full responses and alternative transcripts are preserved. Protein substitutions were encoded using a minimum-base-change codon; when alternatives tie, the chosen allele and alternatives are recorded. Genomic scores apply to that chosen allele, not every possible nucleotide route to the same protein change.

Higher AlphaMissense indicates greater predicted pathogenicity; <0.34 is likely benign, >0.564 likely pathogenic, otherwise ambiguous. SIFT ≤0.05 is usually deleterious; preserve its explicit low-confidence flags. Higher PolyPhen-2 indicates greater predicted damage. Higher REVEL prioritizes potential pathogenicity, but no clinical threshold is imposed here. CADD PHRED is a genome-wide prioritization rank, not an activity value or percent probability of disease. PROVEAN ≤-2.5 generally predicts deleterious effect. Array values are preserved as distinct retrieved values rather than silently averaged. [EMBL-EBI guidance](https://www.ebi.ac.uk/training/online/courses/alphafold/classifying-the-effects-of-missense-variants-using-alphamissense/understanding-pathogenicity-scores-from-alphamissense/); [Ensembl documentation](https://www.ensembl.org/info/docs/tools/vep/script/vep_options.html); [dbNSFP](https://www.dbnsfp.org/).

For multi-base substitutions, the single-nucleotide MyVariant/dbNSFP lookup used here does not supply the same additional metrics. “Not retrieved” is not zero, benign, or a statement that no tool could ever compute a score. Scores for component SNVs must not be added or averaged. No new CADD/PROVEAN model was run. Model outputs are neither clinical classifications nor GOF/LOF measurements; correlated predictors are not independent experimental votes.

COSMIC was queried through NLM Clinical Tables, both for exact substitutions and positions. Search can match unrelated genes, intronic coordinates or synonymous variants; the scientific interpretations above exclude these false matches. Repeated identifiers are not automatically independent patients. PubMed links supplied only by an index remain bibliographic leads unless the primary evidence was checked. Prior ClinVar/CCLE checks are identified as such rather than presented as new queries. No licensed full export or exhaustive unindexed-supplement search was performed, and no novelty claim is made.

## Drugs and next evidence needed

No exact-variant clinical response, resistance result or matched mutant/wild-type inhibitor IC50 was verified for this JAK2 substitution. General JAK-inhibitor activity, a same-gene cancer diagnosis, or structural proximity to a drug-bound kinase does not establish a mutation-specific response. No immune-checkpoint resistance classification can be assigned without evidence of the relevant signaling defect. Hypothetical homologous substitutions are comparator analyses, not demonstrated patient mutations unless explicitly stated.

Useful follow-up information includes disease/specimen context, transcript and nucleotide allele, allele fraction, matched-normal status and co-occurring alterations. Functional experiments should distinguish expression/stability, basal signaling, cytokine-stimulated signaling and relevant receptor context. A change in phosphorylation alone need not mean functional activation.

## Supporting files

- [All predictor responses](JAK2-four-variant-predictor-results.json)
- [Additional genomic predictors](JAK2-four-variant-additional-predictors.json)
- [Alignment results](JAK2-four-variant-alignments.json) and [sensitivity checks](JAK2-alignment-sensitivity.json)
- [Position-level COSMIC queries](JAK2-homologous-position-COSMIC.json)
- [Earlier evidence review](JAK2-evidence-notes.md)
