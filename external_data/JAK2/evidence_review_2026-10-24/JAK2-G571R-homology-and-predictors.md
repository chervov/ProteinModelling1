# JAK2 G571R: homologous positions, predictors and evidence

**Aligned positions: JAK2 G571 ↔ JAK1 G610 (alternative S612; uncertain) ↔ JAK3 G546 ↔ TYK2 G634.**

Research date: 25 October 2026. This is a scientific evidence review, not a formal clinical classification. Comparisons replace each aligned residue with the target amino acid R; they do not assume that the original residues or effects are identical.

## Predictor comparison

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK2 G571R | 0.2686; likely benign | 0.01; deleterious_low_confidence | 0.94; probably_damaging | 0.874 | 33 | -4.36 |
| JAK1 G610R | 0.1418; likely benign | 0; deleterious | 0.957; probably_damaging | 0.364 | 24.3 | -1.54 |
| JAK3 G546R | 0.1249; likely benign | 0.04; deleterious | 0.267; benign | 0.334 | 17.32 | -3.51, -3.41 |
| TYK2 G634R | 0.1072; likely benign | 0.13; tolerated | 0.184; benign | 0.314 | 8.038 | -1.43, -1.06, -1.24 |

**All four original JAK2 variants have low-confidence SIFT labels in the current VEP response. Those labels must be retained. None of these scores establishes GOF, LOF or drug response.**

## Local alignment

Each pair below has the target at the eleventh alignment column; dashes are gaps.

```text
JAK2 GVRREV-GDYGQLHE--TEVL
JAK1 GTLMDYKDDEGTSEEKKIKVI
               ^

JAK2 KGVRREVGDYGQLHETEVLLK
JAK3 RGCRHEVVD-GEARKTEVLLK
               ^

JAK2 --------DYGQLHETEVLLK
TYK2 EDPLVPGRDRGQ--ELRVVLK
               ^

```

## Alleles used for prediction

| Protein | Protein change | Coding query | Codon change | Minimum changed bases |
|---|---|---|---|---|
| JAK2 | G571R | ENST00000381652:c.1711G>C | GGT→CGT | 1 |
| JAK1 | G610R | ENST00000342505:c.1828G>C | GGA→CGA | 1 |
| JAK3 | G546R | ENST00000458235:c.1636G>C | GGG→CGG | 1 |
| TYK2 | G634R | ENST00000525621:c.1900G>C | GGG→CGG | 1 |

## Evidence and interpretation

G571 is in the JH2 regulatory pseudokinase domain, immediately after inhibitory phosphorylation site Y570. Glycine-to-arginine replaces a small flexible residue with a large basic side chain. Altering the local loop or Tyr570 accessibility is plausible, but neither the structure change nor diminished Tyr570 phosphorylation has been directly established for G571R in the sources located.

**Exact observation:** [Ma et al., 2009, PMID 19074595](https://pmc.ncbi.nlm.nih.gov/articles/PMC2607565/) reported one heterozygous G571R in a suspected-MPN diagnostic cohort. The COSMIC record COSM29109 points to that same paper; it is not an independent functional experiment. The related diagnostic patents repeat overlapping evidence. See the existing [patent and mechanism audit](JAK2-G571R-patents-and-mechanism.md) for family documents and the PRM-151 treatment-patent mention, neither of which supplies a G571R-specific response result.

**Independent mechanism evidence:** [Feener et al., 2004, PMID 15143188](https://pubmed.ncbi.nlm.nih.gov/15143188/) and [Argetsinger et al., 2004, PMID 15143187](https://pmc.ncbi.nlm.nih.gov/articles/PMC416404/) experimentally support inhibitory Y570 regulation. [Ungureanu et al., 2011](https://www.nature.com/articles/nsmb.2099) demonstrated JH2-dependent regulatory phosphorylation. These test site biology, not the exact G571R mechanism.

**Same position, different mutation:** [Milosevic Feenstra et al., 2016, PMID 26423830](https://pubmed.ncbi.nlm.nih.gov/26423830/) and [Lin et al., 2019](https://www.nature.com/articles/s41375-019-0459-z) investigated G571S. The latter found receptor-context-dependent transformation involving CRLF2/IL7R-alpha. These findings cannot be transferred to arginine. A position-level COSMIC query also returns G571D, which is another separate allele.

**Alignment uncertainty matters:** default full-length and extended-domain alignments match G571 to JAK1 G610, JAK3 G546 and TYK2 G634. However, JAK1 shifts to **S612** with gap-open 12/extension 1 in a JH2-only alignment. The JAK1 match is therefore provisional. For the alternative S612R comparison, AlphaMissense is **0.1298 (likely benign)**, SIFT **0.05 (deleterious)** and PolyPhen-2 **0.263 (benign)**. This differs substantially from G610R's PolyPhen-2 result. Neither mapping has been resolved by structural superposition. The original G571R scores are unaffected by this uncertainty.

The Y570 phosphotyrosine context is not identically preserved across these local JAK sequences. Do not assume the same inhibitory phosphorylation mechanism in each paralog just because a glycine aligns nearby. No exact G610R/G546R/G634R COSMIC hit or functional study was located in the queries used.

**Functional call: unresolved, with a specific regulatory hypothesis worth testing.** REVEL 0.874 and CADD 33 strongly prioritize investigation, while AlphaMissense 0.2686 is in its likely-benign category. None of these tools distinguishes activation from inactivation. The relevant experiment would separate protein abundance, Y570 phosphorylation, basal versus cytokine-induced STAT signaling and receptor context. Adjacent mutations may alter antibody recognition, so phospho-antibody signal alone would be insufficient.

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
