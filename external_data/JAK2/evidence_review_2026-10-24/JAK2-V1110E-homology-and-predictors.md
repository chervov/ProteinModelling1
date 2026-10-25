# JAK2 V1110E: homologous positions, predictors and evidence

**Aligned positions: JAK2 V1110 ↔ JAK1 P1136 ↔ JAK3 P1082 ↔ TYK2 A1156.**

Research date: 25 October 2026. This is a scientific evidence review, not a formal clinical classification. Comparisons replace each aligned residue with the target amino acid E; they do not assume that the original residues or effects are identical.

## Predictor comparison

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK2 V1110E | 0.2891; likely benign | 0.01; deleterious_low_confidence | 0.862; possibly_damaging | 0.477 | 23 | 0.24 |
| JAK1 P1136E | 0.6898; likely pathogenic | 0; deleterious | 0.4; benign | Not retrieved | Not retrieved | Not retrieved |
| JAK3 P1082E | 0.4725; ambiguous | 0; deleterious | 0.471; possibly_damaging | Not retrieved | Not retrieved | Not retrieved |
| TYK2 A1156E | 0.4621; ambiguous | 0; deleterious | 0.864; possibly_damaging | 0.5 | 28.7 | -1.1, -1.09 |

**All four original JAK2 variants have low-confidence SIFT labels in the current VEP response. Those labels must be retained. None of these scores establishes GOF, LOF or drug response.**

## Local alignment

Each pair below has the target at the eleventh alignment column; dashes are gaps.

```text
JAK2 MIMTECWNNNVNQRPSFRDLA
JAK1 QLMRKCWEFQPSNRTSFQNLI
               ^

JAK2 MIMTECWNNNVNQRPSFRDLA
JAK3 ELMKLCWAPSPQDRPSFSALG
               ^

JAK2 MIMTECWNNNVNQRPSFRDLA
TYK2 HLMKNCWETEASFRPTFENLI
               ^

```

## Alleles used for prediction

| Protein | Protein change | Coding query | Codon change | Minimum changed bases |
|---|---|---|---|---|
| JAK2 | V1110E | ENST00000381652:c.3329T>A | GTA→GAA | 1 |
| JAK1 | P1136E | ENST00000342505:c.3406_3407delinsGA | CCA→GAA | 2 |
| JAK3 | P1082E | ENST00000458235:c.3244_3245delinsGA | CCA→GAA | 2 |
| TYK2 | A1156E | ENST00000525621:c.3467C>A | GCG→GAG | 1 |

## Evidence and interpretation

V1110 is near the C-terminal end of the catalytic JH1 domain (UniProt 849–1124). Replacing hydrophobic valine with negatively charged glutamate is nonconservative, but this does not establish inactivation or activation. The aligned position is not invariant: JAK1/JAK3 contain proline and TYK2 alanine. Accordingly, P→E and A→E predictions are comparisons in different protein backgrounds, not replications of V→E.

No verified exact-V1110E functional study, clinical response or resistance result was located. Earlier ClinVar/COSMIC-index and CCLE checks were negative for the exact substitution; the current COSMIC query is again negative. This does not prove the allele has never occurred.

The position-level COSMIC search does return **JAK2 V1110L** (COSM1636193; liver carcinoma; no PMID in the returned record) and **V1110I** (COSM7453586; stomach adenoma; PMID 27175599). These are different, chemically more conservative substitutions. The latter paper's full details were not independently retrievable in this update; treat it as a database-derived bibliographic lead, not a functional validation.

Homologous-position records include JAK1 P1136L (COSM9369612; melanoma; PMID 28467829), JAK3 P1082L (COSM9796684; skin carcinoma; PMID 26950094), JAK3 P1082S (COSM9485286; melanoma; PMID 28467829), and TYK2 A1156V (COSM4738519; colorectal carcinoma). Their exact glutamate comparators have no returned COSMIC match. The [Bonilla et al. basal-cell carcinoma sequencing study](https://pubmed.ncbi.nlm.nih.gov/26950094/) is a primary source linked by the P1082L record; no exact P1082L functional experiment was established here. Tumour detection alone does not establish a driver.

The 2025 primary modelling paper [Impact of Ruxolitinib Interactions on JAK2 JH1 Domain Dynamics](https://www.mdpi.com/1422-0067/26/8/3727) labels V1110 in a structure based on JAK2–ruxolitinib PDB 6VGL. It does not test V1110E. This is a useful structural template, not evidence of resistance or sensitivity.

**Functional call: unresolved.** AlphaMissense and PROVEAN lean toward tolerance, whereas SIFT (low confidence) and PolyPhen-2 flag possible impact. The cross-paralog scores cannot settle that disagreement. A useful next modelling question is whether V1110E changes local packing or conformational stability in JH1; direct kinase/downstream-signaling measurements would still be needed to determine direction.

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
