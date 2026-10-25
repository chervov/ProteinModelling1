# JAK3 Y581C: homologous positions and functional evidence

**Aligned human positions: JAK3 Y581 ↔ JAK1 H647 ↔ JAK2 H606 ↔ TYK2 H667.**

| JAK family member | Residue aligned to JAK3 Y581 | Cysteine substitution compared below |
|---|---|---|
| JAK3 | Y581 (tyrosine) | Y581C |
| JAK1 | H647 (histidine) | H647C |
| JAK2 | H606 (histidine) | H606C |
| TYK2 | H667 (histidine) | H667C |

These correspondences were obtained from canonical human sequences; full-length and JH2-only alignments agree. The comparator mutations are **H→C**, not Y→C, because the reference residues differ. The scores below describe substitutions, not an intrinsic score assigned to the position. The JAK1/JAK2/TYK2 cysteine substitutions are hypothetical comparisons here, not claims that they were observed in patients.

## Predictor comparison at the aligned positions

Retrieved 25 October 2026. AlphaMissense is from the canonical UniProt protein's all-amino-acid-substitution file at EMBL-EBI; SIFT and PolyPhen-2 are from the Ensembl-canonical transcript returned by VEP. No averaging across transcripts was performed.

| Substitution | AlphaMissense score / model class | SIFT score / prediction | PolyPhen-2 score / prediction |
|---|---|---|---|
| **JAK3 Y581C** | **0.0993 — likely benign** | **0.00 — deleterious** | **0.820 — possibly damaging** |
| **JAK1 H647C** | **0.6183 — likely pathogenic** | **0.01 — deleterious** | **0.999 — probably damaging** |
| **JAK2 H606C** | **0.1584 — likely benign** | **0.00 — deleterious, low confidence** | **0.786 — possibly damaging** |
| **TYK2 H667C** | **0.4041 — ambiguous** | **0.01 — deleterious** | **0.999 — probably damaging** |

Interpretation: AlphaMissense suggests greater intolerance of the cysteine replacement in JAK1 than in JAK2/JAK3, with TYK2 intermediate. SIFT flags all four, with an explicit low-confidence flag for JAK2 H606C, and PolyPhen-2 also predicts possible or probable damage. This disagreement is part of the result; it is not resolved by majority vote. **None of these scores determines GOF versus LOF, drug sensitivity, or a clinical diagnosis.** AlphaMissense's likely-benign/likely-pathogenic labels here are model outputs, not clinical variant classifications.

Score directions: higher AlphaMissense and PolyPhen-2 scores indicate greater predicted pathogenicity/damage; lower SIFT scores indicate greater predicted impact (≤0.05 is commonly called deleterious). AlphaMissense uses <0.34 for likely benign and >0.564 for likely pathogenic, with the intervening range ambiguous. See [EMBL-EBI AlphaMissense interpretation](https://www.ebi.ac.uk/training/online/courses/alphafold/classifying-the-effects-of-missense-variants-using-alphamissense/understanding-pathogenicity-scores-from-alphamissense/) and [Ensembl predictor documentation](https://www.ensembl.org/info/docs/tools/vep/script/vep_options.html). Scores are not percentages of kinase activity.

| Additional predictor | JAK3 Y581C | JAK1 H647C | JAK2 H606C | TYK2 H667C |
|---|---|---|---|---|
| REVEL | 0.369 | Not retrieved* | Not retrieved* | Not retrieved* |
| CADD PHRED | 22.2 | Not retrieved* | Not retrieved* | Not retrieved* |
| PROVEAN | -5.09 to -5.22 across returned entries | Not retrieved* | Not retrieved* | Not retrieved* |

*The reference codon is CAC at all three histidine positions, and conversion to cysteine TGC requires a two-nucleotide change, CA→TG. JAK3 TAC→TGC requires only one. Standard [dbNSFP](https://www.dbnsfp.org/) lookup tables focus on nonsynonymous single-nucleotide variants, so their missing entries cannot be read as benign scores. No separate CADD/PROVEAN computation for the double substitutions was run; these tools' potential capabilities should not be confused with the coverage of the retrieved precomputed tables. The combined substitution must not be scored by adding or averaging its component SNV scores. The three shared predictors above do provide exact amino-acid-substitution scores for all four proteins.

### Exact score provenance and identity checks

| Gene | VEP query, coding HGVS | Ensembl-canonical transcript | Confirmed protein change |
|---|---|---|---|
| JAK3 | NM_000215.4:c.1742A>G | ENST00000458235 | ENSP00000391676.1:p.Tyr581Cys |
| JAK1 | NM_002227.4:c.1939_1940delinsTG | ENST00000342505 | ENSP00000343204.4:p.His647Cys |
| JAK2 | NM_004972.4:c.1816_1817delinsTG | ENST00000381652 | ENSP00000371067.4:p.His606Cys |
| TYK2 | NM_003331.5:c.1999_2000delinsTG | ENST00000525621 | ENSP00000431885.1:p.His667Cys |

VEP normalizes the two-base CA→TG changes as `inv` in some transcript HGVS outputs; these encode the same queried double substitution. Returned codons and protein identities were checked. Other transcripts can have different residue numbering or predictor values and are retained in the raw JSON, not mixed into the table.

AlphaMissense source files: [JAK3 P52333](https://alphafold.ebi.ac.uk/files/AF-P52333-F1-aa-substitutions.csv), [JAK1 P23458](https://alphafold.ebi.ac.uk/files/AF-P23458-F1-aa-substitutions.csv), [JAK2 O60674](https://alphafold.ebi.ac.uk/files/AF-O60674-F1-aa-substitutions.csv), [TYK2 P29597](https://alphafold.ebi.ac.uk/files/AF-P29597-F1-aa-substitutions.csv). These contain protein substitution scores, distinct from AlphaFold structure-confidence scores. JAK3's canonical AlphaMissense value 0.0993 is one of the values previously returned through dbNSFP; its earlier multi-transcript range is retained later for provenance.

The accompanying [JAK-family-cysteine-predictor-results.json](JAK-family-cysteine-predictor-results.json) preserves full VEP responses and query URLs, exact selected scores, and all 19 AlphaMissense substitutions at each of the four aligned positions. Additional JAK3 metrics come from the [exact MyVariant.info allele record](https://myvariant.info/v1/variant/chr19:g.17947982T%3EC), with raw provenance preserved in the original database-results file.

Research date: 25 October 2026. Evidence review, not a clinical classification.

**Main finding: human JAK3 Y581 aligns to JAK1 H647, JAK2 H606 and TYK2 H667. JAK2 H606Q provides a relevant structural-modelling precedent, and JAK1 H647Q has a COSMIC observation. Neither establishes gain or loss of function for JAK3 Y581C.**

## 1. Sequence correspondence

I aligned canonical human UniProt sequences, using global affine-gap alignment with BLOSUM62, gap opening 10 and extension 0.5. Full-length and independently restricted JH2-domain alignments agreed for all three comparisons. This is a sequence analysis performed for this review, not a published structural superposition.

| Protein | UniProt | Corresponding residue | JH2 domain used |
|---|---|---|---|
| JAK3 | P52333 | **Y581** | 521–781 |
| JAK1 | P23458 | **H647** | 583–855 |
| JAK2 | O60674 | **H606** | 545–809 |
| TYK2 | P29597 | **H667** | 589–875 |

Local sequence, with the equivalent position bracketed:

```text
JAK3  571  EAASLMSQVS[Y]RHLVLLHGVC  591
JAK1  637  EAASMMRQVS[H]KHIVYLYGVC  657
JAK2  596  EAASMMSKLS[H]KHLVLNYGVC  616
TYK2  657  ETASLMSQVS[H]THLAFVHGVC  677
```

Sources: [JAK3](https://rest.uniprot.org/uniprotkb/P52333.json), [JAK1](https://rest.uniprot.org/uniprotkb/P23458.json), [JAK2](https://rest.uniprot.org/uniprotkb/O60674.json), [TYK2](https://rest.uniprot.org/uniprotkb/P29597.json). Companion JSON preserves both alignment modes; reference sequences and a Python script accompany this report.

This is not an invariant tyrosine across JAK paralogs: the other three proteins have histidine. Tyrosine and histidine both have aromatic rings, although their chemistry differs. Cysteine lacks that ring. Loss of packing or hydrogen-bond interactions is therefore a plausible hypothesis, not an established mechanism or direction of activity change. This comparison does not measure conservation among JAK3 orthologs across species.

Y581 is in the regulatory pseudokinase domain. By sequence correspondence to the modelled JAK2 position, it is around the alpha-C/beta-4 connecting region. I did not calculate JAK3 Y581C binding energies, molecular dynamics, or a structural superposition.

## 2. JAK2 H606Q: the strongest exact-position literature lead

**Ma et al., 2009, Mutation Profile of JAK2 Transcripts in Patients with Chronic Myeloproliferative Neoplasias. PMID 19074595.** Table 1 reports one heterozygous H606Q observation, c.1818C>A, in the investigated suspected-MPN cohort. This is an observation in a cancer-related diagnostic series, not a direct activity assay. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC2607565/).

**Lee et al., 2009, Structural effects of clinically observed mutations in JAK2 exons 13–15: comparison with V617F and exon 12 mutations. PMID 19744331; DOI 10.1186/1472-6807-9-58.** The authors modelled H606Q and simulated changes around the alpha-C/beta-4 loop. They proposed disruption of contacts with the L604/L609 backbones and altered positioning relative to V617, potentially disturbing autoinhibitory organization. Figure 8 is the most relevant illustration. This is an older homology-model/MD result, not experimental validation of H606Q activity and not a Y581C simulation. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC2749040/).

Current curated interpretations remain cautious: [CKB H606Q](https://ckb.genomenon.com/geneVariant/show?geneVariantId=28794) calls its protein effect unknown and notes the absence of biochemical characterization. [ClinVar 1906053](https://www.ncbi.nlm.nih.gov/clinvar/variation/1906053/) records germline uncertain significance. A germline classification is distinct from an assessment of somatic oncogenicity; neither proves normal function.

In human terms: **the equivalent position has been implicated in the machinery controlling JAK activity, but the evidence does not show that changing it always releases the brake.** Disrupting a regulatory domain can also impair activation or protein stability.

## 3. What the COSMIC records actually add

Direct NLM Clinical Tables COSMIC-index queries returned:

| Position/variant | Returned records | Provenance |
|---|---:|---|
| JAK1 H647Q | 1 | COSM11054440; COSV109689950; c.1941C>A; large intestine/carcinoma; PMID 32217638 |
| JAK2 H606Q | 3 rows | Two share COSM29116/COSV67610086 and PMID 19074595; another is COSM142902, c.?, PMID 21326037 |
| TYK2 H667 | 0 | No match in this index |

**Rows are not necessarily independent patients, publications, or functional validations.** In particular, the two JAK2 rows with the same variant identifiers and paper must not be counted as two independent studies.

The JAK1 reference is **Yan et al., 2020, Organoid cultures of early-onset colorectal cancers reveal distinct and rare genetic profiles**, PMID 32217638; DOI 10.1136/gutjnl-2019-320019. This is an organoid/exome study. The specific H647Q link is supplied by the COSMIC-index record; I have not independently verified its sample-level supplementary row or found a functional H647Q assay. [Primary paper abstract](https://pubmed.ncbi.nlm.nih.gov/32217638/).

The additional JAK2 reference is **Ma et al., 2011, MPL mutation profile in JAK2 mutation-negative patients with myeloproliferative disorders**, PMID 21326037; DOI 10.1097/PDM.0b013e3181ecd261. This is a diagnostic sequencing study. H606Q is linked by the index; the abstract does not name that allele. Its sample-level details and independence from the earlier cohort remain unverified. It adds a bibliographic lead, not biochemical confirmation. [Primary paper](https://pubmed.ncbi.nlm.nih.gov/21326037/).

ClinVar-index searches using three-letter amino-acid names returned H606Q/1906053, but no JAK1 His647 or TYK2 His667 match. Raw query URLs and results are saved in the companion database JSON files. Index coverage is limited; negative results are not evidence of worldwide absence.

## 4. Nearby experiments: both activation and impaired signaling occur

**JAK3 H583Y, two residues away:** Sim et al., 2017 demonstrated IL-3-independent Ba/F3 growth and inhibition by tofacitinib, cellular IC50 85 ± 10 nM. Their JAK3 G589D mutant also transformed cells, with IC50 54 ± 9 nM. These are genuine functional results for those substitutions, not Y581C. PMID 28284718; DOI 10.1016/j.ajpath.2017.01.004. [Primary paper](https://pubmed.ncbi.nlm.nih.gov/28284718/).

Adjacent **JAK3 R582W** has SCID-associated annotation, while **G589S** has immunodeficiency evidence despite G589D being activating. See [UniProt JAK3](https://www.uniprot.org/uniprotkb/P52333/entry), [R582W ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/RCV001852597.10/) and [Roberts et al., PMID 14615376](https://pubmed.ncbi.nlm.nih.gov/14615376/). This is why nearby disease variants cannot determine Y581C's direction.

**TYK2 H669P:** Yeh et al., 2000 selected this mutant in a loss-of-function screen. It was catalytically impaired and failed to support normal interferon-alpha signaling despite high basal phosphorylation. PMID 10908660; DOI 10.1073/pnas.160130297. This is especially useful evidence that a highly phosphorylated JAK protein is not automatically functionally activated. [Primary paper](https://pubmed.ncbi.nlm.nih.gov/10908660/).

### A correspondence discrepancy in older literature

Saharinen et al., 2003 explicitly describe TYK2 H669 as corresponding to JAK2 H606. [Paper, PMID 12686600](https://pmc.ncbi.nlm.nih.gov/articles/PMC153113/). However, the canonical sequence alignments performed here place **TYK2 H667 at JAK2 H606/JAK3 Y581**, and **TYK2 H669 at JAK2 H608/JAK3 H583**. Both histidines occur in the short local motif. The older paper uses mouse Jak2 numbering; checking the current mouse Q62120 local sequence does not remove the two-position discrepancy. The historical mapping is not treated here as proof that H669P is an exact Y581 homolog. It is nearby-region evidence. No structural-superposition resolution was performed.

## 5. Further leads: veterinary observations and patents

**Campbell et al., 2022, Targeted sequencing of candidate gene regions for myelofibrosis in dogs** reports a canine JAK2 H606Y variant at VAF 3.6%, with conflicting SIFT/PROVEAN predictions. The authors discuss possible effects on the regulatory loop but explicitly did not establish functional effects. This is veterinary observational evidence using the paper's numbering; a separate canine-human sequence alignment was not performed here. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC9308436/).

JAK2 H606Q also appears in the mutation-detection patent family **Compositions and methods for detecting mutations in JAK2 nucleic acid**, including [EP2340315B1](https://patents.google.com/patent/EP2340315B1/en) and [EP3572530B1](https://patents.google.com/patent/EP3572530B1/en). Its presence in these lists supports that it was a detection target; it does not independently demonstrate signaling or a drug response. No exact JAK3 Y581C functional patent result was located.

## 6. Predictions for Y581C itself

The exact-allele annotations retrieved in the preceding review remain discordant:

| Predictor | Retrieved result | What it tells us |
|---|---|---|
| AlphaMissense via dbNSFP | 0.0972–0.1409, benign labels across returned entries | Predicts relative tolerance; does not establish normal signaling |
| SIFT via VEP | 0.00, deleterious | Possible functional perturbation; no GOF/LOF direction |
| PolyPhen-2 via VEP | 0.82 possibly damaging; 0.92 probably damaging in another transcript | Transcript-dependent impact prediction |
| REVEL | 0.369 | Numerical prioritization evidence, not an activity result |
| CADD | PHRED 22.2 | Prioritization score, not percent probability of pathogenicity |
| PROVEAN | -5.09 to -5.22, deleterious | Possible perturbation; no directional classification |

[Exact MyVariant.info allele](https://myvariant.info/v1/variant/chr19:g.17947982T%3EC); [Ensembl VEP](https://rest.ensembl.org/vep/human/hgvs/NM_000215.4:c.1742A%3EG?content-type=application/json). Raw results and transcript/provenance distinctions are in JAK3-Y581C-database-results.json and the preceding evidence review. Older embedded PolyPhen annotation disagrees with VEP; do not merge these silently or count correlated algorithms as independent experiments.

The checked [iPTMnet JAK3 page](https://research.bioinformatics.udel.edu/iptmnet/entry/P52333/) and UniProt record did not list Y581 phosphorylation. This is a bounded negative result, not proof phosphorylation is impossible. **There is no established basis here to describe Y581C as removal of a known inhibitory phosphotyrosine.** It is not equivalent to JAK2 Y570.

## 7. Interpretation and useful next work

The most defensible annotation is: **JAK3 Y581C, functional effect unknown; regulatory-domain variant at a position corresponding to JAK2 H606; plausible local structural perturbation, with conflicting variant predictions.**

There is no verified Y581C-specific activity assay, drug-response measurement or clinical-response evidence in the sources located. Neither the JAK2 model nor nearby tofacitinib-sensitive JAK3 mutants establishes a treatment biomarker for Y581C.

For modelling, the focused question is whether Y581C changes local packing and the alpha-C/beta-4 region in relevant JAK3 conformations. A stability prediction alone would still not decide GOF versus LOF. For functional assessment, compare wild-type and Y581C expression, basal and cytokine-stimulated downstream signaling in an appropriate receptor/JAK1 context, and a cellular growth or signaling output. Include activating and impaired-function controls. Measuring JAK phosphorylation alone is insufficient, as the TYK2 experiment illustrates.

Search scope included exact variants, homologous residues, one- and three-letter names, primary literature, COSMIC/ClinVar indexes, curated protein and PTM records, predictions and patents. Licensed full database exports and every unindexed supplement were not available; the report does not claim exhaustive absence or novelty.
