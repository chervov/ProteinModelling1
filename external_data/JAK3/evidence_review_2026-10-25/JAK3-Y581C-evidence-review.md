# JAK3 Y581C evidence review

Search date: 25 October 2026. Scientific evidence summary, not a formal clinical classification.

**Conclusion: exact-variant function is unresolved. No verified primary observation, functional experiment, or drug-response result for JAK3 Y581C was located. It cannot presently be assigned GOF or LOF from this search.** Sequence identity and computational annotations were verified. Nearby mutations have different biological effects and cannot substitute for exact-variant evidence.

## Identity

- Protein: JAK3 p.Tyr581Cys / Y581C, tyrosine replaced by cysteine.
- Transcript-based change checked with Ensembl VEP: NM_000215.4:c.1742A>G; codon TAC to TGC.
- GRCh37 genomic coordinate: chr19:17947982 T>C.
- GRCh38 genomic coordinate: chr19:17837173 T>C.
- JAK3 is on the reverse strand; genomic T>C and coding A>G therefore describe the same substitution.
- UniProt P52333 contains Tyr at position 581. Local reference sequence, residues 571–591: EAASLMSQVSYRHLVLLHGVC.
- Residue 581 lies in JH2, the regulatory pseudokinase domain (UniProt protein kinase 1, residues 521–781), rather than JH1, the main catalytic domain (822–1111).
- No natural-variant or modified-residue feature specifically at 581 was found in the retrieved UniProt record. This does not prove that phosphorylation never occurs there.

Sources: [UniProt record](https://rest.uniprot.org/uniprotkb/P52333.json); [Ensembl VEP query](https://rest.ensembl.org/vep/human/hgvs/NM_000215.4:c.1742A%3EG?content-type=application/json); [MyVariant.info record](https://myvariant.info/v1/variant/chr19:g.17947982T%3EC).

## Direct database and literature checks

| Source and query | Result | Interpretation |
|---|---|---|
| NLM COSMIC index, JAK3 Y581C, GRCh37 and GRCh38 | Zero results in both | No match in this index, not proof of worldwide absence. A JAK3 A572V control query returned records. |
| NLM ClinVar index, JAK3 Tyr581Cys | Zero results | No retrieved clinical classification. JAK3 Tyr100Cys control returned ClinVar 9360. |
| CCLE Broad 2019 mutations, JAK3/Entrez 3718 | No Y581C match; no returned protein-change match containing 581 | Negative in this particular cell-line dataset only. |
| UniProt P52333 | Reference residue/domain confirmed; no exact natural-variant feature | Protein context, not disease classification. |
| gnomAD r4 GraphQL, 19-17837173-T-C | Exome AC=0, AN=1,420,402, AF=0; genome=null | No alternate copies in the returned exome data. AN counts assessed allele copies, not patients. Genome null is unavailable data, not a zero count. |
| MyVariant.info/dbNSFP | Exact allele has computational annotations | A precomputed annotation record is not proof that a person has been observed with the allele. |
| LOVD public JAK3 full-data page | No text match for 581 | Bounded negative page search. |
| Indexed OncoKB, CIViC and CKB searches | No exact-variant evidence page located | No confirmed therapeutic annotation; not an authenticated exhaustive export. |
| Patent and ClinicalTrials.gov indexed searches | No exact JAK3 Y581C hit located | No exact-variant patent experiment or trial found by these searches. |

The gnomAD API request was POST https://gnomad.broadinstitute.org/api with query:

```graphql
{ variant(variantId: "19-17837173-T-C", dataset: gnomad_r4) {
  variant_id exome { ac an af } genome { ac an af }
} }
```

A literature-index search snippet for Bibliome listed Y581C with three references. However, the live variant pages said the variant was not in the database, and the live gene page differed substantially from the indexed version. The references could not be identified and verified; **do not count this as three papers, patients or validations**.

Europe PMC query `JAK3 AND (Y581C OR Tyr581Cys OR "1742A>G")` returned PMID 24446311, a 2014 BRAF/CMML paper. Full-text inspection showed that its c.1742A>G entry is **BRAF N581S**, not JAK3 Y581C. It is excluded as a false match. This illustrates why gene and transcript must be verified, not merely the nucleotide string.

## What the predictions say

The tools disagree. These are algorithm outputs, not experimental measurements and not clinical classifications.

| Method/source | Retrieved value | Meaning/qualification |
|---|---|---|
| AlphaMissense through dbNSFP | 0.0972, 0.0993, 0.1409 across returned protein/transcript entries; B labels | Benign prediction category for all returned entries; not proof of normal function. |
| SIFT, Ensembl VEP | 0.00, deleterious | Predicts an effect on protein function; does not determine GOF versus LOF. |
| PolyPhen-2, Ensembl VEP | 0.82 possibly damaging for ENST00000458235/ENST00000527670; 0.92 probably damaging for ENST00000534444 | Transcript-dependent output. |
| REVEL through dbNSFP | 0.369 | Intermediate numerical score; no clinical classification assigned here. |
| CADD through MyVariant.info | PHRED 22.2 | Computational prioritization score, not an activity measurement. |
| PROVEAN through dbNSFP | -5.09 to -5.22, D labels | Deleterious prediction category. |

Provenance matters: the older CADD-embedded PolyPhen field reports 0.082/benign, whereas VEP and dbNSFP report different PolyPhen values. These should not be silently mixed. The saved raw annotations preserve the distinctions. Counting algorithms as independent votes is inappropriate because their inputs and training information overlap.

Tyrosine-to-cysteine removes an aromatic ring and hydroxyl group and introduces a smaller sulfur-containing side chain. This is a substantial chemical change, but its functional direction depends on structural context. It could affect packing, stability or interactions. No exact-Y581C structural experiment was found. Being a tyrosine does not establish that Y581 is a regulatory phosphosite; the JAK2 Tyr570 mechanism discussed earlier cannot be transferred to JAK3 Tyr581 by analogy alone.

## The most informative nearby primary evidence

**Sim et al., 2017 — Novel JAK3-Activating Mutations in Extranodal NK/T-Cell Lymphoma, Nasal Type.** PMID 28284718; DOI 10.1016/j.ajpath.2017.01.004. [Primary paper](https://pubmed.ncbi.nlm.nih.gov/28284718/).

The study identified A573V, H583Y and G589D in lymphoma samples. H583Y is two residues from Y581; G589D is eight residues away. H583Y and G589D supported IL-3-independent Ba/F3 growth and showed cellular tofacitinib IC50 values of 85 ± 10 nM and 54 ± 9 nM, respectively. This establishes an experimentally important region, but those numbers do not apply to Y581C.

**Adjacent R582W has immunodeficiency-associated evidence.** UniProt annotates R582W with T-negative/B-positive/NK-negative severe combined immunodeficiency and cites PMID 9753072. [UniProt](https://www.uniprot.org/uniprotkb/P52333/entry); [ClinVar disease record](https://www.ncbi.nlm.nih.gov/clinvar/RCV001852597.10/). This is disease association for R582W, not direct proof of Y581C loss of function.

**G589S is also associated with SCID**, including a homozygous patient reported by Roberts et al. 2004, PMID 14615376. [Primary paper PDF](https://ashpublications.org/blood/article-pdf/103/6/2009/1696577/zh800604002009.pdf). This is a different substitution from the activating G589D above. Even the same residue can have different consequences depending on the replacement.

**Walters et al., 2006 — Activating alleles of JAK3 in acute megakaryoblastic leukemia.** PMID 16843266; DOI 10.1016/j.ccr.2006.06.002. A572V, nine residues from Y581, was activating in cellular and murine models. [Primary paper](https://pubmed.ncbi.nlm.nih.gov/16843266/).

**Transforming Mutations of Jak3 (A573V and M511I) Show Differential Sensitivity to Selective Jak3 Inhibitors.** Demonstrates activity and inhibitor sensitivity for the named mutants, not Y581C. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5642970/).

**Losdyck et al., 2015 — Distinct ALL-associated JAK3 mutants exhibit different cytokine-receptor requirements and JAK inhibitor specificities.** Shows why mutation and cellular context matter when interpreting JAK inhibitors. [Primary paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC4661414/).

## Cancer, immunity, and drugs

JAK3 normally transmits cytokine signals in immune cells. Deficient JAK3 function can cause severe immunodeficiency, while particular activating variants contribute to leukemia/lymphoma. Thus, the gene name alone does not distinguish an immune-deficiency mechanism from an oncogenic mechanism. [NCBI Gene](https://www.ncbi.nlm.nih.gov/gene/3718).

For **Y581C itself**, no verified patient diagnosis, somatic/germline origin, inheritance pattern, functional class, drug IC50, clinical response or resistance result was established by this search.

Tofacitinib is a research lead because nearby experimentally activating mutants respond in cell assays. That does not make Y581C a sensitivity biomarker. Ruxolitinib is principally a JAK1/JAK2 inhibitor; some activating JAK3 mutants depend on partner JAK1 signaling, explaining responses in particular models without implying direct Y581C targeting. No Y581C-specific evidence for ritlecitinib, other JAK inhibitors, or checkpoint immunotherapy was located.

A clinical caution supported by a primary case report: **Failure of tofacitinib to achieve an objective response in a DDX3X-MLLT10 T-lymphoblastic leukemia with activating JAK3 mutations** (2020) describes lack of objective response in a case carrying other activating JAK3 mutations. Even experimentally activating JAK3 status does not guarantee clinical response. [Case report](https://pmc.ncbi.nlm.nih.gov/articles/PMC7476415/).

## Suggested annotation

| Gene | Variant | GOF/LOF | Disease association | Drug evidence |
|---|---|---|---|---|
| JAK3 | Y581C | Unknown; not experimentally established in sources located | No exact-variant association verified | No exact-variant sensitivity/resistance evidence located |

Additional note: regulatory pseudokinase-domain missense variant, absent from the returned gnomAD r4 exome allele counts; computational predictions conflict; nearby activating and immunodeficiency-associated substitutions provide context only. This is an evidence-status description, not an ACMG classification.

The most useful missing information is where this variant came from: a tumour sample, germline immune-disease panel, cell line, or computational variant list; its transcript, allele fraction, matched-normal status and co-occurring variants. A direct comparison of wild-type and Y581C signaling under relevant receptor/cytokine conditions would be needed to resolve function.

## Reproducible endpoints and scope

- [COSMIC GRCh38 query](https://clinicaltables.nlm.nih.gov/api/cosmic/v4/search?terms=JAK3%20Y581C&grchv=38&ef=PubmedPMID,LegacyMutationID,GenomicMutationID,PrimarySite,PrimaryHistology)
- [ClinVar query](https://clinicaltables.nlm.nih.gov/api/variants/v4/search?terms=JAK3%20Tyr581Cys&df=VariationID,GeneSymbol,HGVS_c,AminoAcidChange)
- [CCLE JAK3 mutation query](https://www.cbioportal.org/api/molecular-profiles/ccle_broad_2019_mutations/mutations?sampleListId=ccle_broad_2019_all&entrezGeneId=3718&projection=DETAILED&pageSize=10000)
- [gnomAD allele page](https://gnomad.broadinstitute.org/variant/19-17837173-T-C?dataset=gnomad_r4)
- [LOVD JAK3](https://databases.lovd.nl/shared/view/JAK3)

Search terms included JAK3 with Y581C, Tyr581Cys, Tyr581, 1742A>G and both genomic coordinates; functional, phosphorylation, inhibitor, patent and clinical-trial queries; and follow-up searches for nearby residues. Some sources were accessible only via indexed snippets or API records. Licensed HGMD/COSMIC exports and all unindexed supplements were not searched. Negative results do not prove novelty. Raw successful query results accompany this report.
