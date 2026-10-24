# JAK2 variant evidence notes

Search date: 24 October 2026. Variants: V1110E, G571R, V578I, L805I. This is an evidence review, not a formal clinical classification.

## Findings

| Variant | Exact-variant evidence verified | Interpretation |
|---|---|---|
| V1110E | No exact-variant publication, functional result, or treatment response located. No match in the queried NLM ClinVar or COSMIC indexes, or CCLE Broad 2019 JAK2 mutation data. | Unresolved. A nonconservative substitution in JH1; chemistry alone cannot establish gain or loss of function. |
| G571R | Ma et al. 2009: one heterozygous observation in approximately 20,000 samples submitted for suspected MPN. COSMIC COSM29109 / COSV67665667 points to the same publication, PMID 19074595. | Reported in suspected MPN; activation is hypothesized, not demonstrated for this exact substitution in the evidence located. No exact-variant drug-response result located. |
| V578I | No exact-variant publication, functional result, or treatment response located. No match in queried NLM ClinVar or COSMIC indexes, or CCLE Broad 2019 JAK2 mutation data. | Unresolved. Conservative substitution in JH2; not enough evidence to call benign or oncogenic. |
| L805I | Independently verified in CCLE Broad 2019 through cBioPortal: SARC9371_BONE, GRCh37 chr9:5080662 C>A, NM_004972.3. Present in Diaz et al. 2026 supplementary Table 2, PDF page 7. | Observed in an osteosarcoma cell line. SIFT 0.30 tolerated; PolyPhen-2 0.773 possibly damaging; AlphaMissense 0.1504 benign prediction. No exact-variant functional/drug-response result located. |

The reference amino acids at all four positions were checked against UniProt O60674: G571, V578, L805, V1110. G571, V578 and L805 are in JH2; V1110 is in JH1. Domain location is not a functional classification.

## Direct database checks

- NLM Clinical Tables ClinVar service: queried JAK2 plus the three-letter changes Val1110Glu, Gly571Arg, Val578Ile and Leu805Ile. All returned zero matches. A control query for JAK2 Gly571Ser returned ClinVar 1336051, confirming the correct name format. The service advertised ClinVar data dated 2026-10-05.
- NLM Clinical Tables COSMIC service: queried all four one-letter changes under both GRCh37 and GRCh38. Only G571R matched. GRCh37 returned two record identifiers and GRCh38 one; all point to COSM29109 and PMID 19074595. These are not evidence of three independent patients. The service advertised COSMIC v104 (2026-05-19).
- cBioPortal CCLE Broad 2019 API: retrieved JAK2 mutations and filtered exact protein changes. L805I matched SARC9371_BONE; the other three did not match this particular dataset.
- UniProt O60674: confirmed sequence numbering and domains. No exact natural-variant feature for these four was found in the current entry retrieved. An older indexed ExPASy variant page should not be treated as a current clinical classification.
- OncoKB and CKB: searched publicly accessible pages and indexed results. No verified exact-variant therapeutic annotation located. CKB detail access was limited; OncoKB exact-variant pages were not readable through the web reader. These outcomes do not establish absence from licensed databases.
- CIViC: targeted indexed searches did not produce an exact-variant evidence result. This was not an exhaustive database export.
- gnomAD: no reliable exact-allele population frequency established. Do not describe any of these as absent from population databases on the basis of this search.

Negative search results mean no match in the specified source/query, not proof that a variant has never been observed. The L805I CCLE observation despite its absence from the queried COSMIC index illustrates this limitation.

## Drug evidence

No exact-variant clinical response, resistance result, or mutant-versus-wild-type inhibitor IC50 was located for any of the four.

OncoKB's JAK2 oncogenic-mutation/MPN page notes that ruxolitinib, fedratinib, pacritinib and momelotinib are approved for selected MPN settings irrespective of JAK2 mutation status. That disease-level fact cannot establish these four variants as drug-sensitivity biomarkers.

A 2025 molecular-dynamics paper on JAK2 JH1 and ruxolitinib labels residue V1110 in a structural figure, but does not test V1110E. It provides structural context, not evidence of V1110E sensitivity or resistance.

JAK1/2 loss of function has been associated with interferon-gamma signaling failure and resistance to PD-1 blockade in particular cancers (Shin et al. 2017). None of these four substitutions was established as such a loss-of-function biomarker in the evidence located. Do not infer immunotherapy resistance from the gene name alone.

## Evidence pitfalls

G571R and G571S must be kept separate. Some literature aggregators match the shared locus/rs identifier and attach G571S literature to G571R. The well-described c.1711G>A G571S allele is different from c.1711G>C G571R. G571S functional studies and ClinVar classifications cannot be transferred to G571R.

Ma et al.'s mechanism involving adjacent inhibitory Tyr570 is a proposed explanation. A subsequent COSMIC entry, patent, or review repeating the same observation is not an independent functional validation.

Prediction terms such as AlphaMissense 'benign' and PolyPhen-2 'possibly damaging' describe model output. They are not clinical classifications, and they do not directly measure oncogenicity or drug response.

## References and reproducible endpoints

1. [Ma et al. 2009, Mutation Profile of JAK2 Transcripts in Patients with Chronic Myeloproliferative Neoplasias](https://pmc.ncbi.nlm.nih.gov/articles/PMC2607565/). PMID 19074595.
2. [Diaz et al. 2026, Landscape and functional impact of variants of unknown significance of immune response genes in human cancer](https://www.nature.com/articles/s41417-026-01024-9). Cancer Gene Therapy 33:456-464; published 4 April 2026.
3. [Diaz et al. final supplementary tables](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41417-026-01024-9/MediaObjects/41417_2026_1024_MOESM3_ESM.pdf). L805I is in Table 2, PDF page 7.
4. [CCLE Broad 2019 JAK2 mutation API query](https://www.cbioportal.org/api/molecular-profiles/ccle_broad_2019_mutations/mutations?sampleListId=ccle_broad_2019_all&entrezGeneId=3717&projection=DETAILED&pageSize=10000).
5. [Cellosaurus Sarc9371](https://www.cellosaurus.org/CVCL_5G89). DepMap ACH-002396; GDSC/COSMIC cell-line ID 1303910. Cellosaurus confirms identity and screening resources, not the JAK2 variant itself.
6. [COSMIC G571R via NLM, GRCh38](https://clinicaltables.nlm.nih.gov/api/cosmic/v4/search?terms=JAK2%20G571R&grchv=38&ef=PubmedPMID,LegacyMutationID,GenomicMutationID,PrimarySite,PrimaryHistology).
7. [NLM COSMIC API documentation](https://clinicaltables.nlm.nih.gov/apidoc/cosmic/v4/doc.html).
8. [ClinVar exact G571R query via NLM](https://clinicaltables.nlm.nih.gov/api/variants/v4/search?terms=JAK2%20Gly571Arg&df=VariationID,GeneSymbol,HGVS_c,AminoAcidChange).
9. [UniProt O60674](https://www.uniprot.org/uniprotkb/O60674/entry).
10. [Milosevic Feenstra et al. 2016](https://pubmed.ncbi.nlm.nih.gov/26423830/). Functional study includes G571S, not G571R.
11. [JAK2 G571S in B-cell precursor ALL, 2019](https://www.nature.com/articles/s41375-019-0459-z). Same-codon contextual evidence only.
12. [ClinVar G571S](https://www.ncbi.nlm.nih.gov/clinvar/variation/1336051/). Different allele; do not use its classifications for G571R.
13. [Impact of Ruxolitinib Interactions on JAK2 JH1 Domain Dynamics, 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12028094/). Structural context, not a V1110E study.
14. [OncoKB JAK2 oncogenic mutations in MPN](https://www.oncokb.org/gene/JAK2/somatic/Oncogenic%20Mutations/Myeloproliferative%20Neoplasms). Disease-level therapeutic context.
15. [Shin et al. 2017, Primary Resistance to PD-1 Blockade Mediated by JAK1/2 Mutations](https://pubmed.ncbi.nlm.nih.gov/27903500/). General loss-of-function context, not evidence for these four variants.

## Most useful next information

Tumor/disease type, specimen type, exact transcript and nucleotide changes, variant allele fractions, whether all variants come from one sample, matched-normal results, and other alterations would materially change interpretation. For research, direct signaling assays and matched mutant/wild-type drug-response experiments are needed to resolve activation, loss of function, and inhibitor sensitivity.
