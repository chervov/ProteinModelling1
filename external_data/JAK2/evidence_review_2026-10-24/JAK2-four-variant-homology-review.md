# JAK2 V1110E, G571R, V578I and L805I: homologous positions and predictors

Research date: 25 October 2026. Evidence review, not a clinical classification.

## Aligned positions first

| JAK2 target | JAK1 | JAK3 | TYK2 | Caveat |
|---|---|---|---|---|
| V1110E | P1136 | P1082 | A1156 | Reference amino acids differ |
| G571R | G610 or S612 | G546 | G634 | JAK1 mapping is alignment-sensitive |
| V578I | V619 | V553 | V639 | Valine conserved across these JAKs |
| L805I | I845 | L777 | L866 | JAK1 already has target I |

## Original JAK2 substitutions: scores

| Variant | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| [V1110E](JAK2-V1110E-homology-and-predictors.md) | 0.2891 (likely benign) | 0.01 (deleterious, low confidence) | 0.862 (possibly_damaging) | 0.477 | 23 | 0.24 |
| [G571R](JAK2-G571R-homology-and-predictors.md) | 0.2686 (likely benign) | 0.01 (deleterious, low confidence) | 0.94 (probably_damaging) | 0.874 | 33 | -4.36 |
| [V578I](JAK2-V578I-homology-and-predictors.md) | 0.2368 (likely benign) | 0 (deleterious, low confidence) | 0.999 (probably_damaging) | 0.618 | 29.3 | -0.91 |
| [L805I](JAK2-L805I-homology-and-predictors.md) | 0.1504 (likely benign) | 0.01 (deleterious, low confidence) | 0.78 (possibly_damaging) | 0.439 | 25.6 | -0.96 |

Each linked report contains the same predictor comparison for JAK1, JAK3 and TYK2, exact coding queries, local sequences, literature, database observations and limitations.

## Evidence assessment

- **V1110E:** exact function unresolved; other substitutions at V1110 and homologous positions are catalogued, but no exact glutamate drug-response evidence was found.
- **G571R:** published suspected-MPN observation and a plausible Y570 regulatory hypothesis; no direct GOF/LOF or drug-response validation located. The JAK1 correspondence is uncertain.
- **V578I:** exact function unresolved; prediction disagreement persists despite conservative chemistry and conserved valine across the JAKs.
- **L805I:** observed in SARC9371_BONE; no exact functional direction established. JAK1 naturally carries isoleucine at the aligned site. The older published SIFT 0.30 differs from current VEP 0.01 (low confidence); both are documented.

AlphaMissense classifies all four original JAK2 changes as likely benign, while other predictors disagree. Those are model labels, not clinical classifications. The highest REVEL among these four is G571R (0.874), which prioritizes investigation but does not establish activation.

## Methods, score meanings and limitations

Canonical UniProt sequences: [JAK1 P23458](https://rest.uniprot.org/uniprotkb/P23458.json), [JAK2 O60674](https://rest.uniprot.org/uniprotkb/O60674.json), [JAK3 P52333](https://rest.uniprot.org/uniprotkb/P52333.json), [TYK2 P29597](https://rest.uniprot.org/uniprotkb/P29597.json). Pairwise global affine-gap BLOSUM62 alignments used gap-open 10/extension 0.5, comparing full proteins with domain segments expanded by 30 residues. Additional domain-only checks used 8/0.5, 10/0.5 and 12/1. All mappings were stable in these checks except G571→JAK1, reported explicitly. This is sequence alignment, not structural superposition or proof of equivalent biochemical effects.

AlphaMissense scores are from EMBL-EBI canonical protein all-substitution files (https://alphafold.ebi.ac.uk/files/AF-ACCESSION-F1-aa-substitutions.csv). SIFT/PolyPhen-2 are selected for the queried Ensembl transcript, with returned codon, residue and substitution verified. REVEL/CADD/PROVEAN are from exact genomic-allele MyVariant.info/dbNSFP records. Full responses and alternative transcripts are preserved. Protein substitutions were encoded using a minimum-base-change codon; when alternatives tie, the chosen allele and alternatives are recorded. Genomic scores apply to that chosen allele, not every possible nucleotide route to the same protein change.

Higher AlphaMissense indicates greater predicted pathogenicity; <0.34 is likely benign, >0.564 likely pathogenic, otherwise ambiguous. SIFT ≤0.05 is usually deleterious; preserve its explicit low-confidence flags. Higher PolyPhen-2 indicates greater predicted damage. Higher REVEL prioritizes potential pathogenicity, but no clinical threshold is imposed here. CADD PHRED is a genome-wide prioritization rank, not an activity value or percent probability of disease. PROVEAN ≤-2.5 generally predicts deleterious effect. Array values are preserved as distinct retrieved values rather than silently averaged. [EMBL-EBI guidance](https://www.ebi.ac.uk/training/online/courses/alphafold/classifying-the-effects-of-missense-variants-using-alphamissense/understanding-pathogenicity-scores-from-alphamissense/); [Ensembl documentation](https://www.ensembl.org/info/docs/tools/vep/script/vep_options.html); [dbNSFP](https://www.dbnsfp.org/).

For multi-base substitutions, the single-nucleotide MyVariant/dbNSFP lookup used here does not supply the same additional metrics. “Not retrieved” is not zero, benign, or a statement that no tool could ever compute a score. Scores for component SNVs must not be added or averaged. No new CADD/PROVEAN model was run. Model outputs are neither clinical classifications nor GOF/LOF measurements; correlated predictors are not independent experimental votes.

COSMIC was queried through NLM Clinical Tables, both for exact substitutions and positions. Search can match unrelated genes, intronic coordinates or synonymous variants; the scientific interpretations above exclude these false matches. Repeated identifiers are not automatically independent patients. PubMed links supplied only by an index remain bibliographic leads unless the primary evidence was checked. Prior ClinVar/CCLE checks are identified as such rather than presented as new queries. No licensed full export or exhaustive unindexed-supplement search was performed, and no novelty claim is made.

## Drugs and next evidence needed

No exact-variant clinical response, resistance result or matched mutant/wild-type inhibitor IC50 was verified for this JAK2 substitution. General JAK-inhibitor activity, a same-gene cancer diagnosis, or structural proximity to a drug-bound kinase does not establish a mutation-specific response. No immune-checkpoint resistance classification can be assigned without evidence of the relevant signaling defect. Hypothetical homologous substitutions are comparator analyses, not demonstrated patient mutations unless explicitly stated.

Useful follow-up information includes disease/specimen context, transcript and nucleotide allele, allele fraction, matched-normal status and co-occurring alterations. Functional experiments should distinguish expression/stability, basal signaling, cytokine-stimulated signaling and relevant receptor context. A change in phosphorylation alone need not mean functional activation.
