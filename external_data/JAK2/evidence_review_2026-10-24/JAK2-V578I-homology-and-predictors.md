# JAK2 V578I: homologous positions, predictors and evidence

**Aligned positions: JAK2 V578 ↔ JAK1 V619 ↔ JAK3 V553 ↔ TYK2 V639.**

Research date: 25 October 2026. This is a scientific evidence review, not a formal clinical classification. Comparisons replace each aligned residue with the target amino acid I; they do not assume that the original residues or effects are identical.

## Predictor comparison

| Protein/substitution | AlphaMissense | SIFT | PolyPhen-2 | REVEL | CADD PHRED | PROVEAN |
|---|---|---|---|---|---|---|
| JAK2 V578I | 0.2368; likely benign | 0; deleterious_low_confidence | 0.999; probably_damaging | 0.618 | 29.3 | -0.91 |
| JAK1 V619I | 0.355; ambiguous | 0; deleterious | 0.995; probably_damaging | Not retrieved | Not retrieved | Not retrieved |
| JAK3 V553I | 0.1951; likely benign | 0; deleterious | 0.714; possibly_damaging | Not retrieved | Not retrieved | Not retrieved |
| TYK2 V639I | 0.325; likely benign | 0; deleterious | 1; probably_damaging | Not retrieved | Not retrieved | Not retrieved |

**All four original JAK2 variants have low-confidence SIFT labels in the current VEP response. Those labels must be retained. None of these scores establishes GOF, LOF or drug response.**

## Local alignment

Each pair below has the target at the eleventh alignment column; dashes are gaps.

```text
JAK2 YGQLHE--TEVLLKVLDKAHR
JAK1 EGTSEEKKIKVILKVLDPSHR
               ^

JAK2 GDYGQLHETEVLLKVLDKAHR
JAK3 VD-GEARKTEVLLKVMDAKHK
               ^

JAK2 -DYGQLHETEVLLKVLDKAHR
TYK2 RDRGQ--ELRVVLKVLDPSHH
               ^

```

## Alleles used for prediction

| Protein | Protein change | Coding query | Codon change | Minimum changed bases |
|---|---|---|---|---|
| JAK2 | V578I | ENST00000381652:c.1732G>A | GTT→ATT | 1 |
| JAK1 | V619I | ENST00000342505:c.1855_1857delinsATT | GTG→ATT | 2 |
| JAK3 | V553I | ENST00000458235:c.1657_1659delinsATT | GTG→ATT | 2 |
| TYK2 | V639I | ENST00000525621:c.1915_1917delinsATT | GTG→ATT | 2 |

## Evidence and interpretation

V578 lies in JH2, close in sequence to the ATP-binding lysine K581. The aligned residue is valine in all four canonical human JAK proteins. This is conservation across paralogs; it is not a quantitative survey of JAK2 conservation across species. Valine-to-isoleucine retains a hydrophobic side chain but changes its size and branching, so it cannot be assumed functionally silent.

No exact V578I primary functional experiment, patient-response result or inhibitor-resistance study was located. The previous exact ClinVar/CCLE queries and current COSMIC query did not return the allele. The three equivalent V→I substitutions also had no COSMIC-index match in this run.

[Ungureanu et al., 2011](https://www.nature.com/articles/nsmb.2099) and [Bandaranayake et al., 2012, Crystal structures of the Jak2 pseudokinase domain and the pathogenic mutant V617F](https://pmc.ncbi.nlm.nih.gov/articles/PMC3414675/) establish that JH2 participates in regulatory phosphorylation and provide structural context. They do not test V578I. Nearby ATP-site or activating mutations cannot be used as its functional classification.

The predictors provide a meaningful conflict: JAK2 AlphaMissense **0.2368** and PROVEAN **-0.91** lean toward tolerance, while PolyPhen-2 **0.999**, SIFT **0.00 (low confidence)** and REVEL **0.618** flag potential impact. Similar discordance exists in the other JAKs. A large PolyPhen-2 score is not proof of GOF or of drug resistance.

**Functional call: unresolved.** A focused modelling hypothesis is altered local packing around the JH2 nucleotide-binding region, but no pocket geometry, ATP affinity or stability change was calculated here. Neither proximity to K581 nor conservative chemistry resolves direction. Protein abundance, downstream signaling and relevant receptor-dependent stimulation would need direct comparison with wild type.

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
