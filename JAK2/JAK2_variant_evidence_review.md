# JAK2 variants: direct evidence, JAK-family comparisons and distant homologs

## Summary of the main findings

- **Follow-up findings (sections 8–10).** V617F stabilizes a JH2 dimer, while V625F, R867Q and T875N have residue-specific mechanistic studies. Among seven additional disease-associated alleles, K539L and R683S have experimental mutant structures and distinct activation mechanisms. R564Q has familial and cellular GOF evidence with conflicting germline ClinVar classifications. [Structural study](https://pmc.ncbi.nlm.nih.gov/articles/PMC10923518/) · [R564Q record](https://www.ncbi.nlm.nih.gov/clinvar/variation/2136730/)
- **The ten variants in the lower half of the figure were labeled “identified in this study.”** That label establishes neither pathogenicity nor gain of function. The search found a prior human JAK2 observation for **G571R**, an osteosarcoma cell-line record for **L805I**, and a renal-cancer database entry for **P37A**. An independent primary report for the other seven exact JAK2 alleles was not verified. The publication containing the screenshot was not identified.
- **H380Y and R426X have the strongest functional evidence at corresponding positions in other JAKs.** TYK2 **S431G** impaired interferon signaling. JAK3 **R402H** reduced STAT5 signaling. Both are different substitutions from the JAK2 inputs. For **C427R**, wild-type JAK3 already has Arg403, and the reverse substitution **JAK3 R403C** has been reported. [TYK2 study](https://pubmed.ncbi.nlm.nih.gov/33260630/) · [JAK3 study](https://doi.org/10.3389/fgene.2026.1624523) · [R403C in ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/2138258/)
- **V578I is the cleanest positional comparison among the ten missense/stop inputs.** An exact Val→Ile three residues before the ATP-site lysine occurs in the EGFR and FGFR3 records. FGFR3 V505I failed to increase growth-factor-independent proliferation in the reported MCF10A assay. MEK1 M94I, at the same offset but with a different starting residue, behaved similarly to wild type in proliferation and transformation assays. These observations do not supply positive evidence that JAK2 V578I is activating. [FGFR3 experiment](https://doi.org/10.1038/s41588-025-02482-x) · [EGFR ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/134026/) · [MEK1 experiment](https://pubmed.ncbi.nlm.nih.gov/36442478/)
- **R426X is a truncation.** Any protein ending at residue 425 would lack both JH2 and JH1. PTPN11 R138* is a human disease allele with an Arg→stop at the corresponding conserved SH2 arginine. PTPN2 lacks that SH2 domain. [PTPN11 family study](https://doi.org/10.1371/journal.pgen.1000991) · [JAK2 FERM–SH2 structure](https://doi.org/10.1371/journal.pone.0156218)
- **L805I, I1065T and V1110E illustrate three different limits of homology.** JAK1 and BRAF already have Ile at the site aligned to JAK2 L805. BRAF I659T is indexed, but four runs put JAK2 I1065 at BRAF I659 and four at Y656. All eight runs mapped JAK2 V1110 to BRAF R701, yet the wild-type residues differ, and no activating R701E experiment was verified. **The comparisons do not establish activation by JAK2 V1110E.**
- **V617F is the positive benchmark, outside the ten study variants.** Human JAK1 V658F has patient, functional and crystal-structure evidence. Engineered TYK2 V678F activated signaling, whereas JAK3 M592F alone did not in the original assay. Thus even paralogs can respond differently. [Cross-JAK experiment](https://pubmed.ncbi.nlm.nih.gov/16239216/) · [JAK1 structure](https://doi.org/10.1038/nsmb.2673)

**How to read the tables.** “Projected” means the target residue was aligned to the JAK2 site and given the same mutant amino acid. It can be a hypothetical variant. “Same site” may involve a different substitution. Clinical observations, database submissions, experiments and structural hypotheses are described separately. VUS means variant of uncertain significance. This consolidates the searches discussed through **1 November 2026**. Records can change. Full supporting tables, including search and coverage logs, appear in the appendices.

## 1. The ten study variants: JAK2 and its three paralogs

Coordinates are one-based human protein positions. The JAK2, JAK1, JAK3 and TYK2 sequences used for the family comparisons correspond to O60674, P23458, P52333 and P29597, respectively. No functional study of an **exact counterpart** of these ten was verified in the other three JAKs.

| JAK2 | Direct evidence for this JAK2 allele | JAK1 projection | JAK3 projection | TYK2 projection | Interpretation within the family |
|---|---|---|---|---|---|
| P37A | [CanProVar JAK2](https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?id=JAK2) lists it in renal cancer. No underlying primary paper verified. A frequently retrieved P37A paper concerns KIT. | P34A | P31A | G27A or gap | TYK2 N-terminal placement is sensitive to alignment settings. |
| F240V | No independent primary report verified. | F251V | V224 already WT | F245V | JAK3 naturally has the mutant amino acid. |
| H380Y | No independent primary report verified. | H420Y | Q356Y | S431Y | **S431G**, a different TYK2 substitution, was tested and impaired signaling. |
| R426X (R426*) | No independent primary report verified. | R466* | R402* | H474* | JAK3 **R402H**, found in trans with Q1007*, reduced STAT5 signaling when tested separately. The JAK2 allele creates a stop. |
| C427R | No independent primary report verified. | W467R | R403 already WT | W475R | The reverse JAK3 change, **R403C**, has been reported in SCID and has a VUS submission. |
| G571R | [Ma et al., 2009](https://pmc.ncbi.nlm.nih.gov/articles/PMC2607565/) found heterozygous c.1711G>C in one individual. G571S was a separate finding. | G610R or S612R | G546R | G634R | The proposed effect on adjacent inhibitory phosphosite Y570 remains a hypothesis. JAK1 placement is ambiguous. |
| V578I | No independent primary report verified. | V619I | V553I | V639I | All preserve Val. No exact counterpart assay was verified in the JAK family. |
| L805I | [Diaz et al.](https://www.nature.com/articles/s41417-026-01024-9): [supplementary table](https://assets-eu.researchsquare.com/files/rs-7187015/v1/00b0974abe7c53eedb7b8471.pdf) lists SARC9371_BONE osteosarcoma cells and AlphaMissense 0.1504. No L805I-specific assay verified. | I845 already WT | L777I | L866I | Natural JAK1 Ile provides a packing comparison. |
| I1065T | No independent primary report verified. | I1092T | M1038T | I1112T | JAK1 and TYK2 preserve Ile. No exact functional result verified. |
| V1110E | No independent primary report verified. | P1136E | P1082E | A1156E | None has Val at the aligned site. No direct family evidence for an activating effect. |

## 2. Upper half of the figure: previously reported GOF group

The two halves of the figure are separate lists. In transcribing it, **p.R755S/R938Q** was the literal label. The primary family paper reports **p.S755R and p.R938Q in cis**, and the JAK2 reference sequence supports Ser755. All analytical tables use the corrected direction. There are 14 upper-group changes and ten lower-group changes, making 24 changes at 23 positions (V617I and V617F share a codon).

| JAK2 variant | Primary evidence discussed |
|---|---|
| T108A | Germline T108A in polycythemia vera with somatic V617F; cell models showed altered erythropoietin responsiveness. [Lanikova et al., 2016](https://pubmed.ncbi.nlm.nih.gov/27647865/) |
| Y317H | FERM-domain variant in myelofibrosis with a CALR mutation; cellular gain of function. [Eder-Azanza et al., 2017](https://pubmed.ncbi.nlm.nih.gov/28473624/) |
| H345L | Somatic variant with constitutive JAK/STAT activation and increased Ba/F3 proliferation. [Maslah et al., 2019](https://pubmed.ncbi.nlm.nih.gov/30259120/) |
| H608N | Two relatives with thrombocytosis and a younger carrier with platelets in the normal range. Increased IL-3-stimulated STAT5 phosphorylation in cells. [Rumi et al., 2014](https://doi.org/10.1002/ajh.23614) |
| L611S | Constitutive activity and tumorigenicity in an experimental model; later reported as germline in a child with thrombocytosis. [Functional study](https://pubmed.ncbi.nlm.nih.gov/19289461/) · [Aral et al., 2018](https://pubmed.ncbi.nlm.nih.gov/29567786/) |
| V617I | Hereditary thrombocytosis; signaling stronger than wild type and weaker than V617F in the comparisons reported. [Mead et al., 2013](https://pubmed.ncbi.nlm.nih.gov/23535062/) |
| V617F | Somatic myeloproliferative disease driver with functional growth and survival evidence. [Kralovics et al., 2005](https://pubmed.ncbi.nlm.nih.gov/15858187/) |
| V625F | Identified in triple-negative myeloproliferative neoplasms and tested in cellular signaling assays. [Milosevic Feenstra et al., 2016](https://doi.org/10.1182/blood-2015-07-661835) |
| E846D and R1063H | Inherited from different parents (**in trans**) in erythrocytosis. Each weakly enhanced signaling in the erythropoietin receptor context. [Kapralova et al., 2016](https://pubmed.ncbi.nlm.nih.gov/27389715/) · [E846D family report](https://pubmed.ncbi.nlm.nih.gov/35764421/) |
| R867Q; S755R + R938Q | R867Q in one family; the S755R/R938Q double allele in another. Reported longer protein half-lives than V617F and receptor-dependent cellular effects. [Marty et al., 2014](https://pubmed.ncbi.nlm.nih.gov/24398328/) |
| T875N | Identified in megakaryoblastic leukemia cells, with disease induction in a mouse transplant model. Also reported as germline in essential thrombocytosis. [Mercher et al., 2006](https://pubmed.ncbi.nlm.nih.gov/16804112/) · [Germline study](https://pubmed.ncbi.nlm.nih.gov/31428969/) |

## 3. Cross-family experiments and structures

| JAK2 input | Counterpart or comparison | Experimental or clinical finding |
|---|---|---|
| V617F | JAK1 V658F | Found in human leukemia. In JAK1 JH2, Phe658 displaces Phe575 and remodels the SH2–JH2 linker. One wild-type crystal copy adopted a similar local arrangement. This supports a local conformational preference, without measuring full-length open/closed populations. [Patient report](https://pubmed.ncbi.nlm.nih.gov/18559588/) · [Toms et al.](https://doi.org/10.1038/nsmb.2673) |
| V617F | TYK2 V678F; JAK3 M592F | The engineered TYK2 mutant activated signaling. JAK3 M592F did not in the original assay. JAK3 M592F + L570F activated STAT5 with JAK1 present in a later study. [Single mutants](https://pubmed.ncbi.nlm.nih.gov/16239216/) · [Double mutant](https://pmc.ncbi.nlm.nih.gov/articles/PMC7016850/) |
| V617I | JAK1 V658I | Patient MPN and factor-independent cellular growth. [Clinical study](https://haematologica.org/article/view/8178) · [Functional study](https://pmc.ncbi.nlm.nih.gov/articles/PMC3105646/) |
| L611S | JAK3 L586S; JAK1 Y652H | Exact JAK3 change recovered in 6/50 growth-factor-independent murine TS1 clones (human numbering), also in TS2. JAK1 Y652H is a different substitution at the aligned position with leukemia/experimental evidence. [TS1](https://doi.org/10.1182/blood-2014-06-576652) · [TS2](https://pmc.ncbi.nlm.nih.gov/articles/PMC11108519/) · [JAK1](https://pmc.ncbi.nlm.nih.gov/articles/PMC3105646/) |
| T875N | JAK1 T901G/R; JAK3 T848A | JAK1 T901G was found in pediatric T-ALL and modeled in a JH1 loop contacting JH2. T901R and JAK3 T848A were recovered in mutant screens. None is the projected Thr→Asn change. [JAK1 structural study](https://haematologica.org/article/view/7720) · [JAK1 screen](https://pmc.ncbi.nlm.nih.gov/articles/PMC3105646/) · [JAK3 screen](https://pmc.ncbi.nlm.nih.gov/articles/PMC11108519/) |
| Y317H; V625F | JAK3 F292V; V599G | Same-site variants in different SCID patients with other alleles in trans. Phenotype cannot be attributed to either change alone. [Di Matteo et al.](https://pubmed.ncbi.nlm.nih.gov/30032486/) |
| R867Q | JAK3 R840C | Activating result in a family with CTLA4 haploinsufficiency. Different replacement at conserved Arg. [Sic et al.](https://doi.org/10.3389/fimmu.2017.01824) |
| R938Q | TYK2 R987Q | [Patent](https://patents.google.com/patent/WO2022175674A1/en) describes R987Q and adjacent D988N editing. No isolated peer-reviewed R987Q phenotype verified. |

Useful structure pairs: human JAK1 JH2 wild type [4L00](https://www.rcsb.org/structure/4L00) and V658F [4L01](https://www.rcsb.org/structure/4L01); JAK2 JH2 wild type [4FVP](https://www.rcsb.org/structure/4FVP) (apo), [4FVQ](https://www.rcsb.org/structure/4FVQ) (Mg–ATP), and V617F [4FVR](https://www.rcsb.org/structure/4FVR) (Mg–ATP). [JAK2 structure paper](https://doi.org/10.1038/nsmb.2348)

## 4. Distant kinases: what the alignments establish

### The initial four-protein comparison

The first panel compared SRC, ABL1, EGFR and PTK2/FAK separately by domain. For V617F, the projections were **SRC V332F, ABL1 T306F, EGFR L782F and PTK2 T491F or I490F**. SRC was the only member of this panel with an aligned wild-type Val. No exact clinical record or functional experiment establishing activation by these four changes was verified. A computed landscape listing EGFR L782F is insufficient evidence for a patient observation.

| JAK2 | Initial lead | Interpretation |
|---|---|---|
| V578I | EGFR V742I | Both valines lie three residues before the ATP-site lysine (JAK2 K581; EGFR K745). This is a sequence landmark, not a measurement of a Val–ATP contact. ClinVar has conflicting germline submissions (VUS and likely benign). [ClinVar 134026](https://www.ncbi.nlm.nih.gov/clinvar/variation/134026/) |
| H608N | EGFR H773N | Identical His→Asn at an aligned position; germline VUS, one submitter in the examined record. [ClinVar 4247349](https://www.ncbi.nlm.nih.gov/clinvar/variation/4247349/) |
| L611S | EGFR R776S projected; R776H tested | **This comparison is separate from V578I.** R776H preferentially acted as the acceptor in the asymmetric EGFR kinase dimer. Dimer dependence was tested in cells; an effect on αC-helix capping was proposed from modeling. Later searching identified R776S together with G719A in a tumor. Neither observation proves a dimer mechanism for JAK2 L611S. [Ruan & Kannan, 2015](https://pubmed.ncbi.nlm.nih.gov/26101090/) · [Compound R776S](https://doi.org/10.1371/journal.pone.0307161.t001) |
| R426* | SRC R178; ABL1 R152 | The conserved phosphotyrosine-coordinating arginine helps anchor the SH2 alignment. Src R175L (traditional numbering) nearly abolished phosphopeptide binding; ABL SH2 motif mutagenesis impaired binding. In JAK2, F436 obstructs the canonical phosphotyrosine pocket. [Src](https://pubmed.ncbi.nlm.nih.gov/7504171/) · [Abl](https://pubmed.ncbi.nlm.nih.gov/1370711/) · [JAK2 crystal structure](https://doi.org/10.1371/journal.pone.0156218) |
| V625F | EGFR I789, immediately before T790 | The unconstrained alignment incorrectly placed V625 at T790. JAK2 JH2 **Q626** is the gatekeeper. Anchoring Q626 to T790 places V625 at I789. ClinVar contains I789L/V; no exact I789F record verified. Do not use EGFR T790M as evidence for JAK2 V625F. [JH2 structure](https://doi.org/10.1038/nsmb.2348) · [I789L](https://www.ncbi.nlm.nih.gov/clinvar/variation/1380650/) · [I789V](https://www.ncbi.nlm.nih.gov/clinvar/variation/3224656/) |

### Ranking the 87 non-JAK tyrosine kinase/kinase-like candidates

Rank is by Smith–Waterman/BLOSUM62 score for each fixed-length JAK2 query (JH1 849–1124; JH2 536–812). These are two rankings within the sampled 87 sequences. Seven genes overlap; 33 distinct genes enter the combined analysis. The 597 rows comprise 24 inputs for the 20 JH1-selected genes plus nine JH2 changes for 13 additional genes. This was an independent sequence analysis. The published 497-domain KinCore alignment was not obtained in machine-readable form or used for these rankings.

| Rank | JH1, in order | JH2, in order |
|---|---|---|
| 1–5 | TNK2, FRK, ABL1, NTRK1, FGFR1 | PTK2B, FES, FRK, ABL1, TXK |
| 6–10 | DDR2, NTRK3, FGFR2, NTRK2, ERBB4 | NTRK2, RET, FER, TEC, SYK |
| 11–15 | PTK7, ABL2, SYK, FGFR3, RET | ROS1, EPHB1, NTRK3, EPHA1, ZAP70 |
| 16–20 | TIE1, EGFR, CSK, FGFR4, PTK2 | EPHA7, NTRK1, EPHA5, IGF1R, BTK |

| JAK2 | Strongest additional finding | What limits the inference |
|---|---|---|
| V578I | **FGFR3 V505I** preserves the change and the lysine offset (K508). Predicted GOF was not validated by growth-factor-independent proliferation in MCF10A cells. [Tagore et al., Fig. 5d and Table S4](https://doi.org/10.1038/s41588-025-02482-x) · [ClinVar condition record](https://www.ncbi.nlm.nih.gov/clinvar/RCV001726365/) | Negative in this system; not proof of a neutral JAK2 allele. |
| L611S | **FGFR3 N540S** segregates with skeletal disease and increases autophosphorylation. **FGFR2 N549S** has cell transformation and tumor-cohort evidence (also N550S on another transcript). **FGFR1 N546S** was seen with K656E. [FGFR3 ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/variation/16349/) · [FGFR biochemical study](https://pubmed.ncbi.nlm.nih.gov/26992226/) · [FGFR2 cohort](https://www.jcga-scc.jp/en/gene/FGFR2) · [FGFR1 report](https://pmc.ncbi.nlm.nih.gov/articles/PMC6989446/) | The FGFRs start from Asn, JAK2 from Leu. The FGFR molecular brake is structurally supported in FGFRs. [Structural study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2094128/) |
| R938Q | **RET R813Q** reduced signaling, migration and colony formation in cells and was reported in Hirschsprung disease. FGFR1 R570Q and FGFR3 R564Q are indexed VUSs. ABL1 L324Q was observed in a CML clone before imatinib. [RET functional study](https://pubmed.ncbi.nlm.nih.gov/22837065/) · [MEN2 VUS record](https://www.ncbi.nlm.nih.gov/clinvar/RCV000796744/) · [ABL1 report](https://haematologica.org/article/view/4738) | RET's loss of function does not assign an effect to isolated JAK2 R938Q; the JAK2 family carried a double allele. |
| V617F/I | **TNK2 V196F, NTRK2 V608F, CSK V256F** preserve Val→Phe in the selected panel. NTRK3 **G608S**, a different substitution, retained apoptosis induction in RKO cells. [NTRK3 experiment](https://doi.org/10.1371/journal.pgen.1003552) | No functional demonstration verified for the three distant exact Val→Phe projections. |
| G571R | RET G748D is indexed as uncertain; G748C appears in CanProVar. | Same-site leads, different replacements; loop correspondence is less secure than for V578I. |

### Further comparisons restricted to the ten study variants

The final panel included twelve serine/threonine or dual-specificity kinases, four SH2-containing proteins and five FERM-containing proteins. Eight runs combined four gap settings with and without landmarks. Agreement measures sensitivity to these choices; none of these comparisons was a local 3D superposition.

| JAK2 | More distant protein result |
|---|---|
| P37A | No reliable FERM counterpart in ezrin, radixin, moesin, merlin/NF2 or EPB41. |
| F240V | Incompatible FERM placements; exclude raw projections from biological interpretation. |
| H380Y | No reliable distant FERM assignment. TYK2 S431G remains the more informative comparison. |
| R426X | **PTPN11 R138*** segregated with metachondromatosis in a three-generation family. SH2D1A R32T is a missense clinical example at the conserved SH2 Arg. [Family paper](https://doi.org/10.1371/journal.pgen.1000991) · [ClinVar 13348](https://www.ncbi.nlm.nih.gov/clinvar/variation/13348/) · [ClinVar 10901](https://www.ncbi.nlm.nih.gov/clinvar/variation/10901/) |
| C427R | Immediately after PTPN11 Arg138, **E139D** is a Noonan-associated allele with a mutant crystal structure and altered local hydrogen bonding. The start and endpoint differ from JAK2 C427R. [Structure](https://pmc.ncbi.nlm.nih.gov/articles/PMC4007598/) · [ClinVar 40513](https://www.ncbi.nlm.nih.gov/clinvar/variation/40513/) |
| G571R | JH2 β2–β3 loop frequently aligns to a gap or changes register. Direct JAK2 evidence takes priority. |
| V578I | At lysine minus three: BRAF V480, RAF1 V372, CDK2 V30, CDK4 V32, MAPK1 V51, MAPK14 V50. **MEK1 M94I** was tested and was similar to wild type; starting residue differs. [Mizuno et al.](https://pubmed.ncbi.nlm.nih.gov/36442478/) |
| L805I | BRAF already has I714 in all eight runs. BRAF I714V, the reverse change, is indexed as a VUS. |
| I1065T | BRAF **I659T** appears in ClinVar Miner as NM_004333.6:c.1976T>C, rs2128994327, uncertain significance. Four runs select I659, four Y656. **The numeric NCBI ClinVar Variation ID was not verified.** The following is a precise search, not a direct VCV record: [NCBI ClinVar rsID search](https://www.ncbi.nlm.nih.gov/clinvar/?term=rs2128994327) · [ClinVar Miner index](https://clinvarminer.genetics.utah.edu/variants-by-gene/BRAF/condition/not%20provided/uncertain%20significance). |
| V1110E | BRAF R701 in 8/8 runs. R701G is indexed as uncertain; no isolated functional result verified for projected R701E. Across panels, JAK1/JAK3 have Pro; TYK2/EGFR have Ala. A testable hypothesis is a hydrophobic contact specific to JAK2 V1110 in its closed state. Contact geometry and the sign of any conformational shift remain unmeasured here. |

## 5. Paper review: TYK2 variants in B-cell precursor acute lymphoblastic leukemia

[Turrubiartes-Martínez et al., Genes 2020;11:1434](https://doi.org/10.3390/genes11121434) · [Full text, Table 1 and Figures 2–5](https://pmc.ncbi.nlm.nih.gov/articles/PMC7761059/). Seven distinct variants occurred in 16 of 62 patients; the P1104A carriers also carried I684S. No matched non-tumor tissue was available to settle somatic versus germline status. No association with survival or principal clinical characteristics was established.

| TYK2 | Domain | Patients | Functional evidence |
|---|---|---:|---|
| R425H · rs150601734 | FERM | 1 | Tested here. No detectable basal autophosphorylation or STAT3 activation in the transfected-cell assay. IFNα stimulated STAT2; STAT1 phosphorylation required 500 pM. IRF1 induction resembled WT, OAS1 induction was reduced. |
| S431G · novel in this study | FERM | 1 | Strongest impairment. Isolated mutant lacked detectable autophosphorylation and phosphorylation of recombinant STAT3. At 500 pM IFNα, intact cells retained detectable STAT1/2 phosphorylation, but IRF1/OAS1 induction resembled the kinase-dead control. |
| I684S · rs12720356 | JH2 | 11 | Not newly tested here. Prior overexpression studies indicated impairment; an endogenous edited-cell model showed no detectable difference in the stated phosphorylation or abundance readouts. Previously associated with protection against autoimmune disease. |
| R703W · rs55882956 | JH2 | 1 | Not newly tested. Prior study found no detectable decrease in expression or phosphorylation under the tested conditions. |
| R832W · rs144995884 | JH2 | 1 | Isolated kinase assay showed impairment; intact cells nevertheless induced IRF1 early, OAS1 near WT at 3 h, and SOCS3 at 1 h after IFNα. The biochemical and transcriptional phenotypes differ. |
| P1104A · rs34536443 | JH1 | 2 | Prior functional impairment; previously associated with autoimmune protection and, in homozygotes, mycobacterial susceptibility. Both carriers also had I684S; combined effect not established. |
| E1163G · rs55886939 | JH1 | 1 | Previously observed in a T-ALL cell line. No variant-specific assay in this paper. |

**Controls and other alleles:** V678F was the engineered hyperactive control and K930R the engineered kinase-dead control. P760L and G761V were germline activating alleles from a separate study, absent from this cohort. [Earlier primary study](https://pubmed.ncbi.nlm.nih.gov/27733777/). Table 1 gives the rsIDs used above; the abstract appears to misassign the R832W identifier.

**Assay and structure caveats:** Figure 4 directly tested immunoprecipitated S431G and R832W, not R425H. Fifty-nanosecond simulations starting from [4PO6](https://www.rcsb.org/structure/4PO6) retained binding of the IFNAR1 peptide to WT, R425H and S431G; R832W was outside the modeled fragment. Retained binding in those simulations does not establish the affinity in cells or explain a full-length JAK conformational shift. The separate expression comparison used B-ALL marrow and healthy peripheral blood cells, with age and specimen differences; it cannot assign expression changes to individual variants.

## 6. The Imagine PTPN papers and the limits of the alignment

| Paper | Finding relevant to the discussion |
|---|---|
| [Jeanpierre, Cognard et al., JEM 2024](https://doi.org/10.1084/jem.20232337) · [PMID 39028869](https://pubmed.ncbi.nlm.nih.gov/39028869/) | Marie Jeanpierre, Jade Cognard, Frédéric Rieux-Laucat and colleagues identified six monoallelic **PTPN2** mutations in pediatric systemic autoimmunity. Loss of phosphatase regulation can increase JAK/STAT signaling. |
| [Rowbotham et al., Thorax 2026](https://doi.org/10.1136/thorax-2025-224469) · [PMID 41545210](https://pubmed.ncbi.nlm.nih.gov/41545210/) | New pathogenic PTPN2 variant leading to childhood interstitial lung disease. Marie Jeanpierre and Frédéric Rieux-Laucat are coauthors. |

**Why PTPN11 but not PTPN2?** The JAK2 R426/C427 comparison uses the second **SH2 domain** of PTPN11. PTPN2 comprises a phosphatase domain and a regulatory tail and has no corresponding SH2, FERM, JH2 or JH1 domain. PTPN2 and PTPN11 can be aligned to one another in their phosphatase domains; this does not extend the JAK2 SH2 alignment. [PTPN2 structural study](https://doi.org/10.1038/s41467-021-27633-6).

## 7. Scope, reproducibility and source archives

The screens distinguished patient reports from cell-line observations, engineered alleles, same-site substitutions and computational predictions. No comparison in this report constitutes a new clinical classification. Especially relevant outstanding work includes a local structural superposition for I1065, a JAK2-specific open/closed contact analysis for V1110, and retrieval of variant-level assay matrices. The FGFR saturation study and [MaveDB deposit](https://www.mavedb.org/search?search=urn:mavedb:00001220-a) were identified, but a complete score join was not performed. Likewise the [MAPK variant-effect atlas](https://mapk.gs.washington.edu/index.html) covers relevant proteins without individually verified scores here for every projected allele.

- [Family alignments, source sequences and notes](variant_evidence/JAK_family_variant_alignments.zip) · [Browse files](variant_evidence/JAK_family_variant_alignments/)
- [Four distant tyrosine kinases](variant_evidence/JAK2_distant_kinase_comparison.zip) · [Browse files](variant_evidence/JAK2_distant_kinase_comparison/)
- [Two top-20 panels, literature, database coverage and code](variant_evidence/JAK2_top20_kinases_evidence.zip) · [Browse files](variant_evidence/JAK2_top20_kinases_evidence/)
- [Ten variants in the more distant domain panel](variant_evidence/JAK2_ten_distant_domain_comparisons.zip) · [Browse files](variant_evidence/JAK2_ten_distant_domain_comparisons/)

## 8. Follow-up evidence for the previously reported JAK2 variants

The upper half of the figure contains 13 entries representing 14 substitutions. This table answers the follow-up question about pathogenicity, gain of function (GOF), and loss of function (LOF). All have some evidence of increased signaling, cytokine sensitivity, or cell survival, sometimes only for a combined allele. None of the cited studies establishes predominant LOF for these entries. A cellular GOF result alone cannot establish that a germline variant causes disease in a carrier. The references are the principal papers identified in the discussion, not an exhaustive bibliography of V617F.

### Variant-by-variant assessment

The clinical column below is my interpretation of the published evidence. Formal ClinVar classifications, where verified, are listed separately. **PV** = polycythemia vera; **ET** = essential thrombocythemia; **MPN** = myeloproliferative neoplasm; **MPL** = thrombopoietin receptor; **EPOR** = erythropoietin receptor.

| JAK2 variant | Functional effect (GOF or LOF) | Clinical interpretation, evidence and primary references |
|---|---|---|
| T108A | Weak GOF or modifier of EPO responsiveness | Germline in a patient with polycythemia vera (PV). Granulocyte cDNA showed somatic V617F on the same allele. T108A alone enhanced low-dose EPO signaling in cells, and an engineered double mutant enhanced reporter activity. Independent causation of PV remains unresolved. [Lanikova et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC5095759/) |
| Y317H | Cellular GOF | Found in myelofibrosis with a co-occurring CALR mutation. The functional study supports altered signaling but cannot assign the patient's disease to Y317H alone. [Eder-Azanza et al.](https://haematologica.org/article/view/8179) |
| H345L | Cellular GOF | Somatic FERM-domain substitution in a patient with myelofibrosis and a CALR mutation. The cell experiments showed increased STAT5 signaling and EPO-responsive proliferation. [Maslah et al.](https://pubmed.ncbi.nlm.nih.gov/30259120/) |
| H608N | Mild, cytokine-dependent GOF | Germline in relatives with thrombocytosis. A younger carrier had a platelet count within the normal range. [Rumi et al., Fig. 2](https://doi.org/10.1002/ajh.23614) |
| L611S | Experimental GOF | Constitutive activity and tumorigenicity in experimental models. A germline finding in a child with thrombocytosis is separate clinical evidence. [Functional study](https://pubmed.ncbi.nlm.nih.gov/19289461/) · [Childhood case](https://pubmed.ncbi.nlm.nih.gov/29567786/) |
| V617I | Inherited GOF, predominantly cytokine hypersensitivity | Human carriers had hereditary thrombocytosis. The direct mouse comparison showed a weaker phenotype than V617F and no overt myeloproliferative disorder in that model. [Human carrier study](https://pubmed.ncbi.nlm.nih.gov/23535062/) · [Mouse comparison](https://pubmed.ncbi.nlm.nih.gov/26458983/) |
| V617F | Established somatic oncogenic GOF | Recurrent driver of PV, essential thrombocythemia, and primary myelofibrosis. Independent 2005 reports linked the acquired allele to disease and characterized its signaling or growth effects. [James](https://pubmed.ncbi.nlm.nih.gov/15793561/) · [Baxter](https://pubmed.ncbi.nlm.nih.gov/15781101/) · [Levine](https://pubmed.ncbi.nlm.nih.gov/15837627/) · [Kralovics](https://pubmed.ncbi.nlm.nih.gov/15858187/) · [Zhao](https://pubmed.ncbi.nlm.nih.gov/15863514/) |
| V625F | Experimental GOF | Identified in a triple-negative myeloproliferative neoplasm (MPN) cohort. The original functional study and a subsequent mutagenesis study support activation. [Clinical and functional study](https://pubmed.ncbi.nlm.nih.gov/26423830/) · [Wu et al.](https://pubmed.ncbi.nlm.nih.gov/29782975/) |
| E846D | Weak, context-dependent GOF. Standalone germline pathogenicity disputed | In one patient with erythrocytosis, E846D and R1063H were inherited from different parents. A later family report implicated E846D, while a population-based reassessment questioned its sufficiency. Germline ClinVar submissions conflict. [Compound heterozygote](https://pubmed.ncbi.nlm.nih.gov/27389715/) · [Family report](https://pubmed.ncbi.nlm.nih.gov/35764421/) · [Population reassessment](https://pubmed.ncbi.nlm.nih.gov/37239426/) · [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/314871696/) |
| R867Q | Receptor-dependent GOF associated with hereditary thrombocytosis | Germline in one family. The receptor comparison and later mutagenesis study establish distinct lines of functional evidence. [Marty et al.](https://pubmed.ncbi.nlm.nih.gov/24398328/) · [Wu et al.](https://doi.org/10.1016/j.ijbiomac.2019.06.068) |
| T875N | Experimental GOF | Identified in megakaryoblastic leukemia cells. The mutant induced myeloproliferative disease in a mouse transplant model. A separate paper reported a germline case with thrombocytosis. [Mercher et al.](https://pubmed.ncbi.nlm.nih.gov/16804112/) · [Germline report](https://pubmed.ncbi.nlm.nih.gov/31428969/) |
| S755R + R938Q | GOF of the inherited double allele | The figure reads R755S/R938Q. The primary family study reports **S755R/R938Q in cis**. R938Q alone produced constitutive signaling in the assay. Isolated S755R had little activity beyond weak STAT5 signaling. The family observation applies to the combined allele. [Marty et al., Fig. 4](https://doi.org/10.1182/blood-2013-05-504555) |
| R1063H | Weak or context-dependent GOF and possible modifier | The compound-heterozygous erythrocytosis observation and later model studies support biological effects. Standalone high-penetrance disease causation remains unresolved. The cited condition-specific ClinVar record lists benign/likely benign germline interpretations. [Erythrocytosis study](https://pubmed.ncbi.nlm.nih.gov/27389715/) · [Hematopoiesis and thrombosis study](https://pubmed.ncbi.nlm.nih.gov/40841769/) · [Further mechanistic follow-up](https://doi.org/10.1038/s41375-026-02937-y) · [ClinVar condition record](https://www.ncbi.nlm.nih.gov/clinvar/RCV000892279/) |

### ClinVar records and clinical interpretation

| Variant | Record and interpretation |
|---|---|
| V617I | Germline pathogenic, one submission without assertion criteria. Familial segregation and functional work provide independent evidence. [ClinVar 29763](https://www.ncbi.nlm.nih.gov/clinvar/variation/29763/) · [Original family report](https://pubmed.ncbi.nlm.nih.gov/22397670/) |
| V617F | ClinVar has submissions across several conditions and origins. The established somatic driver interpretation in PV, ET and myelofibrosis rests on the human and functional studies above. [ClinVar 14662](https://www.ncbi.nlm.nih.gov/clinvar/variation/14662/) |
| E846D | Reported conflicting germline classifications. The weak effect in EPO-receptor assays and the observation in a compound heterozygote leave standalone disease causation unresolved. [ClinVar](https://www.ncbi.nlm.nih.gov/clinvar/314871696/) |
| R1063H | Benign/likely benign in the cited condition-specific record. Modifier effects remain a separate research question. [ClinVar RCV000892279](https://www.ncbi.nlm.nih.gov/clinvar/RCV000892279/) |

## 9. Which activation mechanisms have been tested?

JH2 is the regulatory pseudokinase domain. JH1 is the catalytic kinase domain. A contact within JH2, a contact between JH2 and JH1 in one molecule, and a contact between two receptor-associated JAK2 molecules require different structural comparisons. PMID 33260630 concerns TYK2. The evidence below comes from studies of JAK2 itself.

### V617F and V617I at the same position

**V617F.** In a JH2 crystallographic dimer (6D2I), the aromatic ring introduced at F617 stacks against F595 on the partner JAK2. This stabilizes a pair of receptor-associated JAK2 molecules and brings their kinase domains into position to phosphorylate each other. F595A suppressed abnormal receptor dimerization and signaling in cells. A simulated reversal from F617 to V617 destabilized the interface. [Abraham et al., Fig. 5A–D](https://pmc.ncbi.nlm.nih.gov/articles/PMC10923518/) · [F595 suppressor study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2886835/)

**V617I.** Isoleucine lacks the aromatic ring needed for the F617–F595 stacking contact. Human carrier cells were cytokine-hypersensitive. In the direct mouse comparison, unstimulated V617F marrow showed STAT3/STAT5 phosphorylation, while V617I marrow required stimulation. A shared residue number therefore does not establish a shared dimer mechanism. [Human study](https://pubmed.ncbi.nlm.nih.gov/23535062/) · [Direct comparison](https://pubmed.ncbi.nlm.nih.gov/26458983/)

### Mechanistic evidence for the remaining variants

| JAK2 variant | What the experiments showed | What is known about the mechanism |
|---|---|---|
| **T108A** | Cells showed stronger JAK2 and STAT5 phosphorylation at low erythropoietin (EPO). In the reported patient, sequencing placed T108A and V617F **in cis**, on the same allele. | T108A increases sensitivity to EPO in the assay. The study did not identify a specific contact altered by T108A in the receptor-binding FERM domain. [Lanikova et al., Fig. 2](https://pmc.ncbi.nlm.nih.gov/articles/PMC5095759/) |
| **Y317H** | Following IL-3 stimulation, mutant cells displayed enhanced STAT3 and AKT signaling and retained STAT5 activation. Deleting the FERM domain produced a different result, including loss of STAT5 activation. | The deletion comparison led the authors to propose that Y317H changes the conformation of the FERM domain and thereby changes which pathways respond. They did not resolve a mutant structure. [Eder-Azanza et al.](https://haematologica.org/article/view/8179) |
| **H345L** | In cells expressing the EPO receptor, investigators observed basal STAT5 phosphorylation, stronger phosphorylation after EPO, and increased EPO-responsive proliferation. | The data support an activating effect in this receptor context. The specific FERM-domain contact or conformational change responsible remains unresolved. [Maslah et al.](https://pubmed.ncbi.nlm.nih.gov/30259120/) |
| **H608N** | After cytokine stimulation, H608N produced more STAT5 phosphorylation than wild-type JAK2. | The authors implicated altered regulation by JH2, where H608 resides. The signaling assay did not establish which molecular interaction changed. [Rumi et al., Fig. 2](https://doi.org/10.1002/ajh.23614) |
| **L611S** | JAK2 was partially active at baseline, yet EPO failed to activate it further in the tested cells. | L611 lies near the **JH2 hinge**. The authors proposed that this hinge transmits receptor movement to the kinase. L611S appears to impair both restraint at baseline and the ability to respond further to EPO. The hinge movement itself was modeled. [Interdomain-linker study, Fig. 4](https://pmc.ncbi.nlm.nih.gov/articles/PMC2785384/) |
| **V625F** | Mutations designed to disrupt a proposed **F625–Y613** contact reduced activation. Engineering a replacement interaction restored it. V625F also increased STAT5 signaling and cell proliferation. | The proposed mechanism is that the new contact **within JH2** disturbs the inhibitory interaction between JH2 and JH1. The disruption-and-rescue experiments support the importance of these residues. Their precise geometry comes from modeling. [Wu et al.](https://pubmed.ncbi.nlm.nih.gov/29782975/) |
| **E846D** | E846D and R1063H were studied in hereditary erythrocytosis. They occurred **in trans**, on separate alleles, and showed cooperative effects on EPO-receptor signaling. | In active JH1, E846 forms a salt bridge with **K926**. The authors proposed that the shorter aspartate side chain strengthens this active-state contact and prolongs activation. This is a structural prediction. [Kapralova et al., supplementary Fig. S7](https://doi.org/10.1182/blood-2016-02-698951) |
| **R1063H** | The same study found a weak activating effect in the EPO-receptor system and examined its cooperation with E846D. | The proposed effect concerns the **inactive** state. R1063 forms a salt bridge with **E1060** in inactive JH1. Substitution with histidine may weaken that contact, making the inactive state less stable. The mutant contact was modeled. [Kapralova et al., supplementary Fig. S7](https://doi.org/10.1182/blood-2016-02-698951) |
| **R867Q** | A dedicated study tested the role of **R867 and Y613** in JAK2 activation. Separately, R867Q supported growth without cytokine in cells expressing MPL, while cells expressing the EPO receptor lacked that growth response. | The structural study proposed that loss of the **R867–Y613 contact between JH1 and JH2** favors an open, active kinase. The receptor experiments help explain why a germline allele can preferentially affect platelet production. [Wu et al.](https://doi.org/10.1016/j.ijbiomac.2019.06.068) · [Marty et al.](https://pubmed.ncbi.nlm.nih.gov/24398328/) |
| **T875N** | The original study demonstrated activation and myeloproliferative disease in transplanted mice. A later study tested the interaction between **T875 and D873** and measured changes in STAT5 binding and signaling. | The authors proposed that losing this local contact makes JH1 less compact and improves substrate access. Mutagenesis and biochemical measurements support the model. The original paper’s Fig. 2F is a modeled substitution into a wild-type crystal structure. [Original structural model and mouse study](https://pmc.ncbi.nlm.nih.gov/articles/PMC1895587/) · [Biochemical follow-up](https://pubmed.ncbi.nlm.nih.gov/31299252/) |
| **S755R/R938Q** | The published hereditary thrombocytosis allele is **S755R/R938Q**, with both changes in the same JAK2 protein. Like R867Q, the double mutant supported spontaneous growth in MPL-expressing cells. Its protein half-life was longer than V617F’s and correlated with increased HSP90 binding and higher surface MPL. | The paper directly demonstrates **receptor dependence** and measures **protein stability**. It does not establish a specific atomic contact between residues 755 and 938. The first substitution in the supplied list was written in the reverse direction. [Marty et al.](https://pubmed.ncbi.nlm.nih.gov/24398328/) |

**Structural comparison.** Y613 links two testable hypotheses. V625F introduces a proposed contact with Y613 inside JH2. R867Q disrupts a proposed Y613 contact across the JH1–JH2 boundary. Compare those intramolecular contacts with the experimentally observed F617–F595 contact across the JAK2 dimer. The last comparison requires two JAK2 chains. [V625F](https://pubmed.ncbi.nlm.nih.gov/29782975/) · [R867Q](https://doi.org/10.1016/j.ijbiomac.2019.06.068) · [V617F](https://pmc.ncbi.nlm.nih.gov/articles/PMC10923518/)

## 10. Additional disease-associated JAK2 alleles outside both original lists

| Additional allele | Disease and origin | Functional or structural evidence |
|---|---|---|
| K539L | Somatic driver in PV | Patient-derived exon 12 allele with cellular GOF. The mutation promoted EPO-receptor dimerization and moderately increased purified kinase activity. Replacing Lys539 with leucine allows tighter hydrophobic packing at the JH2 dimer interface. Mutant human JH2 crystal structure at 2.20 Å. [Scott et al.](https://pubmed.ncbi.nlm.nih.gov/17267906/) · [Abraham et al., Fig. 6](https://pmc.ncbi.nlm.nih.gov/articles/PMC10923518/) · [PDB 8C08](https://www.rcsb.org/structure/8C08) |
| R683S | Somatic activating variant in B-cell precursor acute lymphoblastic leukemia (B-ALL) | Purified mutant JH2–JH1 showed increased catalytic turnover. The isolated JH2 structure at 1.70 Å resembles wild type. The results support weakened inhibition at the JH2–JH1 interface. [Patient study](https://pmc.ncbi.nlm.nih.gov/articles/PMC5685720/) · [Mechanism and kinetics](https://pmc.ncbi.nlm.nih.gov/articles/PMC10923518/) · [PDB 8C0A](https://www.rcsb.org/structure/8C0A) |
| R683G | Recurrent somatic activating variant in Down syndrome–associated B-ALL | The exact R683G substitution produced constitutive JAK/STAT signaling and growth-factor independence in Ba/F3 cells. This is independent evidence for substitution of glycine at the same codon. [Primary functional study](https://pubmed.ncbi.nlm.nih.gov/18927438/) |
| R564Q | Germline GOF associated with hereditary thrombocytosis | The allele segregated with elevated platelets. MPL-expressing cells showed reduced apoptosis after cytokine withdrawal. Further families and unrelated carriers were reported. The ClinVar aggregate reviewed had conflicting germline submissions, one pathogenic and one uncertain significance. [Etheridge et al.](https://pubmed.ncbi.nlm.nih.gov/24381227/) · [Further families](https://pmc.ncbi.nlm.nih.gov/articles/PMC11985050/) · [Three unrelated carriers](https://pubmed.ncbi.nlm.nih.gov/41053421/) · [ClinVar 2136730](https://www.ncbi.nlm.nih.gov/clinvar/variation/2136730/) |
| N542_E543del | Recurrent somatic exon 12 driver in PV | The two-residue deletion recurred in independent cohorts and conferred growth-factor independence in cells expressing the EPO receptor. [Original functional study](https://pmc.ncbi.nlm.nih.gov/articles/PMC2873834/) · [Independent cohort](https://pubmed.ncbi.nlm.nih.gov/17984312/) |
| F537_K539delinsL | Somatic exon 12 driver in PV | Three residues are replaced by a single leucine. The patient allele supported growth-factor-independent proliferation in receptor-expressing cells. [Scott et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC2873834/) |
| H538Q + K539L in cis | Somatic exon 12 driver in the PV/erythrocytosis series | Both substitutions occurred on one allele. The tested double mutant showed GOF. H538Q's independent contribution remains unresolved. [Scott et al.](https://pmc.ncbi.nlm.nih.gov/articles/PMC2873834/) |

**Implication for open/closed modeling.** For R683S, compare the contacts of Arg683 with JH1 in a closed tandem-domain model and in an open model. PDB 8C0A contains isolated JH2 and cannot display its contacts with JH1. For K539L, inspect the two JH2 chains at the dimer interface illustrated in the structural paper. A monomer comparison alone omits the relevant partner. These are proposed modeling comparisons. [Abraham et al., Figs. 4–6](https://pmc.ncbi.nlm.nih.gov/articles/PMC10923518/)

## Appendices: complete numerical and evidence tables

These tables are embedded in the Markdown file. Expand a table in a compatible viewer or search the plain text for a variant. Repeated source records and query matches are retained for audit; a query hit is not a verified clinical observation. Blank cells reproduce missing or inapplicable source values.

### A. Full JAK-family projections

<details>
<summary>variant_map.tsv — 24 rows</summary>

| JAK2_variant | figure_group | JAK1_projected | JAK3_projected | TYK2_projected | evidence_note | sources |
| --- | --- | --- | --- | --- | --- | --- |
| P37A | study | P34A | P31A | G27A / gap | No exact JAK3 or TYK2 primary report verified in this search. |  |
| F240V | study | F251V | V224 (already WT) | F245V | No exact JAK3 or TYK2 primary report verified in this search. |  |
| H380Y | study | H420Y | Q356Y | S431Y | TYK2 S431G was reported in a B-ALL patient; impaired activity in a biochemical assay. The projected substitution is S431Y. | https://pubmed.ncbi.nlm.nih.gov/33260630/ |
| R426* | study | R466* | R402* | H474* | JAK3 R402H occurred in trans with Q1007Ter in suspected SCID and reduced STAT5 signaling. R402H differs from the projected stop. | https://www.frontiersin.org/journals/genetics/articles/10.3389/fgene.2026.1624523/full |
| C427R | study | W467R | R403 (already WT) | W475R | Wild-type JAK3 already carries Arg403. A case report cites JAK3 R403C in SCID (reverse change; secondary citation). | https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2024.1472957/full |
| G571R | study | G610R / S612R | G546R | G634R | No exact JAK3 or TYK2 primary report verified in this search. |  |
| V578I | study | V619I | V553I | V639I | No exact JAK3 or TYK2 primary report verified in this search. |  |
| L805I | study | I845 (already WT) | L777I | L866I | No exact JAK3 or TYK2 primary report verified in this search. |  |
| I1065T | study | I1092T | M1038T | I1112T | No exact JAK3 or TYK2 primary report verified in this search. |  |
| V1110E | study | P1136E | P1082E | A1156E | No exact JAK3 or TYK2 primary report verified in this search. |  |
| T108A | previous | M101A | S94A | A97 (already WT) | No exact JAK3 or TYK2 primary report verified in this search. |  |
| Y317H | previous | F366H | F292H | Y376H / F377H | JAK3 F292V reported in a compound heterozygous SCID patient; different substitution. | https://pubmed.ncbi.nlm.nih.gov/30032486/ |
| H345L | previous | N385L | T321L | H396L | No exact JAK3 or TYK2 primary report verified in this search. |  |
| H608N | previous | H649N | H583N | H669N | No exact JAK3 or TYK2 primary report verified in this search. |  |
| L611S | previous | Y652S | L586S | F672S | JAK3 L586S is an exact counterpart recovered in growth-factor-independent murine TS1 and TS2 clones; human numbering. | https://www.sciencedirect.com/science/article/pii/S0006497120395586 https://pmc.ncbi.nlm.nih.gov/articles/PMC11108519/ |
| V617I | previous | V658I | M592I | V678I | JAK1 V658I reported in a patient with MPN. No verified JAK3 M592I or TYK2 V678I primary study. | https://haematologica.org/article/view/8178 |
| V617F | previous | V658F | M592F | V678F | JAK1 V658F and engineered TYK2 V678F activate signaling. JAK3 M592F did not activate in the original assay. JAK3 M592F + L570F could activate STAT5 with JAK1 present. | https://pubmed.ncbi.nlm.nih.gov/16239216/ https://pmc.ncbi.nlm.nih.gov/articles/PMC7016850/ https://www.nature.com/articles/nsmb.2673 |
| V625F | previous | V666F | V599F | V686F | JAK3 V599G reported with W709R in compound heterozygous SCID; different substitution, genotype-level evidence. | https://pubmed.ncbi.nlm.nih.gov/30032486/ |
| E846D | previous | K872D | E819D | K894D | No exact JAK3 or TYK2 primary report verified in this search. |  |
| R867Q | previous | R893Q | R840Q | C915Q | JAK3 R840C reported with CTLA4 haploinsufficiency; activating in functional studies. Different substitution. | https://www.frontiersin.org/journals/immunology/articles/10.3389/fimmu.2017.01824/full |
| T875N | previous | T901N | T848N | T923N | JAK3 T848A recovered in growth-factor-independent murine clones; different substitution. | https://www.sciencedirect.com/science/article/pii/S0006497120395586 https://pmc.ncbi.nlm.nih.gov/articles/PMC11108519/ |
| S755R | previous | K795R | S727R | Q816R | Component of JAK2 S755R/R938Q in cis. | https://doi.org/10.1182/blood-2013-05-504555 |
| R938Q | previous | K965Q | R911Q | R987Q | TYK2 R987Q appears in a patent describing R987Q and D988N editing in Jurkat cells. No isolated R987Q functional conclusion. JAK2 R938Q originally in cis with S755R. | https://patents.google.com/patent/WO2022175674A1/en https://doi.org/10.1182/blood-2013-05-504555 |
| R1063H | previous | K1090H | R1036H | E1110H | No exact JAK3 or TYK2 primary report verified in this search. |  |

</details>

### B. Initial four-kinase comparison

<details>
<summary>variant_map.tsv — 96 rows</summary>

| group | JAK2 | domain | target_gene | unconstrained_sites_4_penalties | anchored_site | projected_change | interpretation | verified_evidence | sources |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| study | P37A | N-terminal | SRC |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | P37A | N-terminal | ABL1 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | P37A | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | P37A | FERM | PTK2 | - |  |  | unresolved; do not transfer | No verified record or paper entered; not a database-wide negative. |  |
| study | F240V | N-terminal | SRC |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | F240V | N-terminal | ABL1 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | F240V | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | F240V | FERM | PTK2 | -/F231/F137 |  |  | unresolved; do not transfer | No verified record or paper entered; not a database-wide negative. |  |
| study | H380Y | N-terminal | SRC |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | H380Y | N-terminal | ABL1 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | H380Y | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | H380Y | FERM | PTK2 | - |  |  | unresolved; do not transfer | No verified record or paper entered; not a database-wide negative. |  |
| study | R426* | SH2 | SRC | R178 |  | R178* | sequence projection; not a structural superposition | Human R178 in SH2 FLVRES corresponds to R175 in traditional chicken Src numbering. R175L impaired phosphotyrosine binding. The JAK2 input is a stop. | https://pubmed.ncbi.nlm.nih.gov/7504171/ https://pmc.ncbi.nlm.nih.gov/articles/PMC4881981/ |
| study | R426* | SH2 | ABL1 | R152/- |  | R152* | gap-penalty sensitive | Conserved FLVRES motif; motif-supported R152 although some local alignments exclude it. Abl SH2 motif mutagenesis affected binding and transforming activity; not an exact stop assay. | https://pubmed.ncbi.nlm.nih.gov/1370711/ |
| study | R426* | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | R426* | N-terminal | PTK2 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | C427R | SH2 | SRC | E179 |  | E179R | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | C427R | SH2 | ABL1 | E153/- |  | E153R | gap-penalty sensitive | No verified record or paper entered; not a database-wide negative. |  |
| study | C427R | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | C427R | N-terminal | PTK2 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| study | G571R | JH2 | SRC | - | - |  | unmapped | No verified record or paper entered; not a database-wide negative. |  |
| study | G571R | JH2 | ABL1 | - | - |  | unmapped | No verified record or paper entered; not a database-wide negative. |  |
| study | G571R | JH2 | EGFR | V738 | V738 | V738R | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | G571R | JH2 | PTK2 | - | P444 | P444R | anchor-corrected; inspect locally | No verified record or paper entered; not a database-wide negative. |  |
| study | V578I | JH2 | SRC | V295 | V295 | V295I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | V578I | JH2 | ABL1 | V268 | V268 | V268I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | V578I | JH2 | EGFR | V742 | V742 | V742I | sequence projection; not a structural superposition | Exact chemical change V742I; conflicting germline submissions (2 VUS, 2 likely benign); no somatic oncogenicity submitted. Computational drug binding study; no isolated gain-of-function assay verified. | https://www.ncbi.nlm.nih.gov/clinvar/variation/134026/ https://www.jto.org/article/S1556086418300042/pdf |
| study | V578I | JH2 | PTK2 | P447 | V451 | V451I | anchor-corrected; inspect locally | No verified record or paper entered; not a database-wide negative. |  |
| study | L805I | JH2 | SRC | L519 | L519 | L519I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | L805I | JH2 | ABL1 | F493 | F493 | F493I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | L805I | JH2 | EGFR | F968 | F968 | F968I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | L805I | JH2 | PTK2 | L676 | L676 | L676I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | I1065T | JH1 | SRC | V470/- | V470 | V470T | gap-penalty sensitive | No verified record or paper entered; not a database-wide negative. |  |
| study | I1065T | JH1 | ABL1 | -/P441 | - |  | gap-penalty sensitive | No verified record or paper entered; not a database-wide negative. |  |
| study | I1065T | JH1 | EGFR | - | - |  | unmapped | No verified record or paper entered; not a database-wide negative. |  |
| study | I1065T | JH1 | PTK2 | K627 | K627 | K627T | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | V1110E | JH1 | SRC | P506 | P506 | P506E | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | V1110E | JH1 | ABL1 | P480 | P480 | P480E | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | V1110E | JH1 | EGFR | A955 | A955 | A955E | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| study | V1110E | JH1 | PTK2 | P663 | P663 | P663E | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | T108A | N-terminal | SRC |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | T108A | N-terminal | ABL1 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | T108A | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | T108A | FERM | PTK2 | V107/- |  |  | unresolved; do not transfer | No verified record or paper entered; not a database-wide negative. |  |
| previous | Y317H | N-terminal | SRC |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | Y317H | N-terminal | ABL1 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | Y317H | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | Y317H | FERM | PTK2 | - |  |  | unresolved; do not transfer | No verified record or paper entered; not a database-wide negative. |  |
| previous | H345L | N-terminal | SRC |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | H345L | N-terminal | ABL1 |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | H345L | N-terminal | EGFR |  |  |  | no corresponding domain in this comparison | No verified record or paper entered; not a database-wide negative. |  |
| previous | H345L | FERM | PTK2 | - |  |  | unresolved; do not transfer | No verified record or paper entered; not a database-wide negative. |  |
| previous | H608N | JH2 | SRC | K324 | K324 | K324N | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | H608N | JH2 | ABL1 | N297 | N297 | N297 (target already has endpoint) | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | H608N | JH2 | EGFR | H773 | H773 | H773N | sequence projection; not a structural superposition | Exact chemical change H773N; germline VUS, one submitter. | https://www.ncbi.nlm.nih.gov/clinvar/variation/4247349/ |
| previous | H608N | JH2 | PTK2 | H482 | H482 | H482N | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | L611S | JH2 | SRC | Q327 | Q327 | Q327S | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | L611S | JH2 | ABL1 | Q300 | Q300 | Q300S | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | L611S | JH2 | EGFR | R776 | R776 | R776S | sequence projection; not a structural superposition | R776H has clinical submissions and dimer-dependent activation demonstrated experimentally. Different residue change from projected R776S. | https://www.ncbi.nlm.nih.gov/clinvar/variation/126515/ https://pmc.ncbi.nlm.nih.gov/articles/PMC5937138/ |
| previous | L611S | JH2 | PTK2 | K485 | K485 | K485S | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617I | JH2 | SRC | V332 | V332 | V332I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617I | JH2 | ABL1 | T306 | T306 | T306I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617I | JH2 | EGFR | L782 | L782 | L782I | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617I | JH2 | PTK2 | T491/I490 | T491 | T491I | gap-penalty sensitive | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617F | JH2 | SRC | V332 | V332 | V332F | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617F | JH2 | ABL1 | T306 | T306 | T306F | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617F | JH2 | EGFR | L782 | L782 | L782F | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V617F | JH2 | PTK2 | T491/I490 | T491 | T491F | gap-penalty sensitive | No verified record or paper entered; not a database-wide negative. |  |
| previous | V625F | JH2 | SRC | V340 | V340 | V340F | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V625F | JH2 | ABL1 | I314 | I314 | I314F | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | V625F | JH2 | EGFR | T790 | I789 | I789F | anchor-corrected; inspect locally | Anchor-corrected site I789. Same-site I789L and I789V in ClinVar; no exact I789F VCV verified. | https://www.ncbi.nlm.nih.gov/clinvar/variation/1380650/ https://www.ncbi.nlm.nih.gov/clinvar/variation/3224656/ |
| previous | V625F | JH2 | PTK2 | I498 | I498 | I498F | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | E846D | JH1 | SRC | R267 | R267 | R267D | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | E846D | JH1 | ABL1 | R239 | R239 | R239D | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | E846D | JH1 | EGFR | E709 | E709 | E709D | sequence projection; not a structural superposition | E709D c.2127A>C, germline VUS as indexed by Sugi (not independently verified on NCBI). Domain-edge correspondence. Do not conflate with E709_T710delinsD. | https://www.ncbi.nlm.nih.gov/clinvar/variation/1393019/ https://sugi.bio/variant/egfr-p-glu709asp |
| previous | E846D | JH1 | PTK2 | R419 | R419 | R419D | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R867Q | JH1 | SRC | T288 | T288 | T288Q | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R867Q | JH1 | ABL1 | - | - |  | unmapped | No verified record or paper entered; not a database-wide negative. |  |
| previous | R867Q | JH1 | EGFR | L730 | L730 | L730Q | sequence projection; not a structural superposition | Site-only: L730R in ClinVar (germline VUS submission). N-lobe loop projection. | https://www.ncbi.nlm.nih.gov/clinvar/variation/962310/ |
| previous | R867Q | JH1 | PTK2 | I440 | I440 | I440Q | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | T875N | JH1 | SRC | G291 | G291 | G291N | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | T875N | JH1 | ABL1 | Y264 | Y264 | Y264N | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | T875N | JH1 | EGFR | V738 | V738 | V738N | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | T875N | JH1 | PTK2 | P447 | P447 | P447N | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | S755R | JH2 | SRC | P467 | P467 | P467R | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | S755R | JH2 | ABL1 | P441 | P441 | P441R | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | S755R | JH2 | EGFR | D916 | D916 | D916R | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | S755R | JH2 | PTK2 | Q624 | Q624 | Q624R | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R938Q | JH1 | SRC | L350 | L350 | L350Q | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R938Q | JH1 | ABL1 | L324 | L324 | L324Q | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R938Q | JH1 | EGFR | L799 | L799 | L799Q | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R938Q | JH1 | PTK2 | R508 | R508 | R508Q | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |
| previous | R1063H | JH1 | SRC | G468/- | G468 | G468H | gap-penalty sensitive | No verified record or paper entered; not a database-wide negative. |  |
| previous | R1063H | JH1 | ABL1 | - | - |  | unmapped | No verified record or paper entered; not a database-wide negative. |  |
| previous | R1063H | JH1 | EGFR | - | - |  | unmapped | No verified record or paper entered; not a database-wide negative. |  |
| previous | R1063H | JH1 | PTK2 | G625 | G625 | G625H | sequence projection; not a structural superposition | No verified record or paper entered; not a database-wide negative. |  |

</details>

### C. Ranked kinase panels

<details>
<summary>ranking.tsv — 87 rows</summary>

| gene | KEGG_Entrez_ID | sequence_source | length | JH1_rank | JH1_score | JH1_identity_pct_paired | JH1_query_coverage_pct | target_start | target_end | JH2_rank | JH2_score | JH2_identity_pct_paired | JH2_query_coverage_pct |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TNK2 | 10188 | https://www.kegg.jp/entry/hsa:10188 | 1038 | 1 | 499 | 45.45 | 91.67 | 126 | 382 | 35 | 246 | 31.4 | 93.14 |
| FRK | 2444 | https://www.kegg.jp/entry/hsa:2444 | 505 | 2 | 473 | 41.11 | 91.67 | 234 | 488 | 3 | 287.5 | 30.74 | 88.09 |
| ABL1 | 25 | https://www.kegg.jp/entry/hsa:25 | 1130 | 3 | 461 | 42.32 | 87.32 | 247 | 489 | 4 | 284.5 | 28.85 | 91.34 |
| NTRK1 | 4914 | https://www.kegg.jp/entry/hsa:4914 | 796 | 4 | 455 | 41.27 | 91.3 | 515 | 781 | 17 | 264.5 | 31.2 | 90.25 |
| FGFR1 | 2260 | https://www.kegg.jp/entry/hsa:2260 | 822 | 5 | 454.5 | 42.06 | 91.3 | 484 | 755 | 57 | 218.5 | 26.25 | 93.5 |
| DDR2 | 4921 | https://www.kegg.jp/entry/hsa:4921 | 855 | 6 | 447 | 38.46 | 94.2 | 563 | 847 | 59 | 213 | 32.75 | 82.67 |
| NTRK3 | 4916 | https://www.kegg.jp/entry/hsa:4916 | 839 | 7 | 446.5 | 41.7 | 89.49 | 542 | 820 | 13 | 268.5 | 30.71 | 91.7 |
| FGFR2 | 2263 | https://www.kegg.jp/entry/hsa:2263 | 821 | 8 | 446.5 | 40.87 | 91.3 | 487 | 758 | 62 | 211.5 | 28.11 | 89.89 |
| NTRK2 | 4915 | https://www.kegg.jp/entry/hsa:4915 | 822 | 9 | 445 | 41.39 | 88.41 | 542 | 803 | 6 | 280 | 30.98 | 92.06 |
| ERBB4 | 2066 | https://www.kegg.jp/entry/hsa:2066 | 1308 | 10 | 445 | 38.74 | 91.67 | 718 | 971 | 28 | 250.5 | 30.0 | 86.64 |
| PTK7 | 5754 | https://www.kegg.jp/entry/hsa:5754 | 1070 | 11 | 440 | 37.01 | 92.03 | 796 | 1058 | 46 | 235.5 | 29.54 | 85.56 |
| ABL2 | 27 | https://www.kegg.jp/entry/hsa:27 | 1182 | 12 | 439.5 | 43.16 | 84.78 | 293 | 534 | 21 | 261.5 | 27.67 | 91.34 |
| SYK | 6850 | https://www.kegg.jp/entry/hsa:6850 | 635 | 13 | 439.5 | 39.27 | 89.49 | 375 | 626 | 10 | 271 | 32.19 | 84.12 |
| FGFR3 | 2261 | https://www.kegg.jp/entry/hsa:2261 | 806 | 14 | 439 | 40.08 | 91.3 | 478 | 749 | 61 | 212.5 | 26.67 | 92.06 |
| RET | 5979 | https://www.kegg.jp/entry/hsa:5979 | 1114 | 15 | 436 | 39.92 | 89.86 | 730 | 1002 | 7 | 278 | 32.66 | 89.53 |
| TIE1 | 7075 | https://www.kegg.jp/entry/hsa:7075 | 1138 | 16 | 435 | 40.8 | 90.58 | 839 | 1107 | 77 | 192.5 | 25.3 | 91.34 |
| EGFR | 1956 | https://www.kegg.jp/entry/hsa:1956 | 1210 | 17 | 435 | 38.4 | 90.58 | 713 | 966 | 40 | 239.5 | 27.89 | 90.61 |
| CSK | 1445 | https://www.kegg.jp/entry/hsa:1445 | 450 | 18 | 434.5 | 39.0 | 87.32 | 195 | 436 | 49 | 230 | 34.04 | 84.84 |
| FGFR4 | 2264 | https://www.kegg.jp/entry/hsa:2264 | 802 | 19 | 432.5 | 39.29 | 91.3 | 473 | 744 | 70 | 200 | 27.76 | 88.45 |
| PTK2 | 5747 | https://www.kegg.jp/entry/hsa:5747 | 1052 | 20 | 431 | 39.51 | 88.04 | 428 | 672 | 32 | 247.5 | 29.92 | 88.09 |
| LYN | 4067 | https://www.kegg.jp/entry/hsa:4067 | 512 | 21 | 429.5 | 43.22 | 85.51 | 247 | 490 | 68 | 201 | 27.38 | 90.97 |
| PTK2B | 2185 | https://www.kegg.jp/entry/hsa:2185 | 1009 | 22 | 429 | 41.91 | 87.32 | 431 | 675 | 1 | 319.5 | 32.02 | 91.34 |
| MET | 4233 | https://www.kegg.jp/entry/hsa:4233 | 1390 | 23 | 427.5 | 37.94 | 91.67 | 1080 | 1337 | 78 | 191.5 | 25.1 | 87.73 |
| HCK | 3055 | https://www.kegg.jp/entry/hsa:3055 | 526 | 24 | 426 | 40.08 | 87.68 | 262 | 504 | 48 | 232 | 29.64 | 91.34 |
| TEK | 7010 | https://www.kegg.jp/entry/hsa:7010 | 1124 | 25 | 426 | 39.68 | 91.3 | 824 | 1093 | 76 | 194.5 | 28.97 | 90.97 |
| EPHA3 | 2042 | https://www.kegg.jp/entry/hsa:2042 | 983 | 26 | 424.5 | 37.85 | 90.94 | 627 | 879 | 33 | 246.5 | 30.77 | 89.17 |
| ZAP70 | 7535 | https://www.kegg.jp/entry/hsa:7535 | 619 | 27 | 421 | 40.24 | 89.13 | 343 | 593 | 15 | 265.5 | 30.68 | 90.61 |
| ROR2 | 4920 | https://www.kegg.jp/entry/hsa:4920 | 943 | 28 | 418.5 | 37.74 | 93.12 | 473 | 746 | 60 | 212.5 | 29.17 | 86.64 |
| DDR1 | 780 | https://www.kegg.jp/entry/hsa:780 | 913 | 29 | 418 | 39.92 | 93.48 | 610 | 901 | 64 | 209 | 32.1 | 87.73 |
| ROR1 | 4919 | https://www.kegg.jp/entry/hsa:4919 | 937 | 30 | 414.5 | 38.15 | 90.22 | 473 | 746 | 26 | 250.5 | 33.61 | 85.92 |
| EPHA5 | 2044 | https://www.kegg.jp/entry/hsa:2044 | 1037 | 31 | 413 | 38.68 | 88.04 | 681 | 933 | 18 | 263.5 | 32.64 | 86.28 |
| MATK | 4145 | https://www.kegg.jp/entry/hsa:4145 | 507 | 32 | 409.5 | 38.3 | 85.14 | 240 | 475 | 44 | 236 | 29.63 | 87.73 |
| EPHA2 | 1969 | https://www.kegg.jp/entry/hsa:1969 | 976 | 33 | 407 | 39.76 | 90.22 | 619 | 872 | 38 | 243 | 31.84 | 88.45 |
| EPHA4 | 2043 | https://www.kegg.jp/entry/hsa:2043 | 986 | 34 | 405.5 | 38.06 | 89.49 | 621 | 879 | 25 | 251.5 | 31.38 | 86.28 |
| ERBB2 | 2064 | https://www.kegg.jp/entry/hsa:2064 | 1255 | 35 | 405.5 | 37.05 | 90.94 | 720 | 972 | 63 | 210 | 25.73 | 87.0 |
| BTK | 695 | https://www.kegg.jp/entry/hsa:695 | 659 | 36 | 405.5 | 36.59 | 89.13 | 402 | 647 | 20 | 261.5 | 30.12 | 89.89 |
| SRMS | 6725 | https://www.kegg.jp/entry/hsa:6725 | 488 | 37 | 405 | 37.6 | 87.68 | 234 | 476 | 54 | 222 | 28.63 | 89.53 |
| EPHA8 | 2046 | https://www.kegg.jp/entry/hsa:2046 | 1005 | 38 | 401.5 | 38.0 | 90.58 | 641 | 893 | 41 | 238.5 | 31.54 | 87.0 |
| MUSK | 4593 | https://www.kegg.jp/entry/hsa:4593 | 869 | 39 | 399 | 38.31 | 89.86 | 575 | 852 | 31 | 248 | 29.69 | 92.42 |
| IGF1R | 3480 | https://www.kegg.jp/entry/hsa:3480 | 1367 | 40 | 398.5 | 36.14 | 90.22 | 1003 | 1262 | 19 | 263 | 27.97 | 94.22 |
| EPHA7 | 2045 | https://www.kegg.jp/entry/hsa:2045 | 998 | 41 | 398 | 35.57 | 91.67 | 633 | 886 | 16 | 264.5 | 33.33 | 87.73 |
| EPHB2 | 2048 | https://www.kegg.jp/entry/hsa:2048 | 1055 | 42 | 397 | 36.19 | 93.12 | 621 | 881 | 27 | 250.5 | 30.42 | 86.64 |
| INSR | 3643 | https://www.kegg.jp/entry/hsa:3643 | 1382 | 43 | 396.5 | 35.18 | 91.67 | 1023 | 1286 | 29 | 250 | 27.52 | 93.14 |
| FES | 2242 | https://www.kegg.jp/entry/hsa:2242 | 822 | 44 | 396 | 40.93 | 85.87 | 565 | 807 | 2 | 293.5 | 32.02 | 91.34 |
| TXK | 7294 | https://www.kegg.jp/entry/hsa:7294 | 527 | 45 | 396 | 40.59 | 86.59 | 271 | 516 | 5 | 281.5 | 29.76 | 90.97 |
| EPHB3 | 2049 | https://www.kegg.jp/entry/hsa:2049 | 998 | 46 | 392 | 36.58 | 93.12 | 633 | 893 | 34 | 246.5 | 30.45 | 87.73 |
| EPHB1 | 2047 | https://www.kegg.jp/entry/hsa:2047 | 984 | 47 | 391.5 | 34.88 | 93.48 | 619 | 879 | 12 | 269 | 32.64 | 87.36 |
| LCK | 3932 | https://www.kegg.jp/entry/hsa:3932 | 509 | 48 | 391 | 38.84 | 87.68 | 245 | 487 | 45 | 235.5 | 32.65 | 88.45 |
| ERBB3 | 2065 | https://www.kegg.jp/entry/hsa:2065 | 1342 | 49 | 391 | 34.78 | 91.67 | 709 | 962 | 39 | 241 | 28.98 | 88.45 |
| MST1R | 4486 | https://www.kegg.jp/entry/hsa:4486 | 1400 | 50 | 388 | 36.4 | 90.58 | 1088 | 1342 | 71 | 199 | 24.18 | 88.09 |
| ROS1 | 6098 | https://www.kegg.jp/entry/hsa:6098 | 2347 | 51 | 387.5 | 39.92 | 86.23 | 1951 | 2208 | 11 | 269.5 | 27.97 | 94.22 |
| AXL | 558 | https://www.kegg.jp/entry/hsa:558 | 894 | 52 | 382 | 36.59 | 89.13 | 542 | 799 | 56 | 221 | 27.94 | 89.17 |
| FER | 2241 | https://www.kegg.jp/entry/hsa:2241 | 822 | 53 | 381.5 | 39.0 | 87.32 | 569 | 810 | 8 | 273.5 | 28.11 | 89.89 |
| MERTK | 10461 | https://www.kegg.jp/entry/hsa:10461 | 999 | 54 | 380.5 | 37.75 | 90.22 | 593 | 855 | 50 | 227.5 | 28.35 | 91.7 |
| BLK | 640 | https://www.kegg.jp/entry/hsa:640 | 505 | 55 | 378.5 | 37.7 | 88.41 | 241 | 486 | 72 | 198 | 27.27 | 91.34 |
| EPHB4 | 2050 | https://www.kegg.jp/entry/hsa:2050 | 987 | 56 | 378.5 | 35.34 | 90.22 | 615 | 875 | 37 | 244.5 | 30.38 | 85.56 |
| TEC | 7006 | https://www.kegg.jp/entry/hsa:7006 | 631 | 57 | 377 | 33.73 | 90.22 | 370 | 620 | 9 | 272 | 31.73 | 89.89 |
| BMX | 660 | https://www.kegg.jp/entry/hsa:660 | 675 | 58 | 376 | 33.86 | 90.94 | 417 | 667 | 24 | 252 | 28.91 | 92.42 |
| FYN | 2534 | https://www.kegg.jp/entry/hsa:2534 | 537 | 59 | 375.5 | 37.14 | 88.77 | 271 | 516 | 43 | 237.5 | 30.04 | 91.34 |
| KDR | 3791 | https://www.kegg.jp/entry/hsa:3791 | 1356 | 60 | 373 | 40.64 | 90.94 | 834 | 1156 | 67 | 201 | 35.74 | 84.84 |
| FLT1 | 2321 | https://www.kegg.jp/entry/hsa:2321 | 1338 | 61 | 372.5 | 38.04 | 92.39 | 827 | 1150 | 83 | 186.5 | 32.92 | 86.64 |
| INSRR | 3645 | https://www.kegg.jp/entry/hsa:3645 | 1297 | 62 | 370.5 | 35.66 | 88.41 | 979 | 1239 | 47 | 233 | 26.92 | 93.86 |
| EPHA1 | 2041 | https://www.kegg.jp/entry/hsa:2041 | 976 | 63 | 366.5 | 35.77 | 89.13 | 630 | 881 | 14 | 266 | 28.97 | 90.97 |
| FLT3 | 2322 | https://www.kegg.jp/entry/hsa:2322 | 993 | 64 | 363 | 39.13 | 91.67 | 610 | 939 | 66 | 203 | 31.51 | 85.92 |
| YES1 | 7525 | https://www.kegg.jp/entry/hsa:7525 | 543 | 65 | 361.5 | 38.49 | 86.59 | 277 | 519 | 42 | 238.5 | 30.83 | 91.34 |
| ITK | 3702 | https://www.kegg.jp/entry/hsa:3702 | 620 | 66 | 360 | 37.5 | 86.96 | 363 | 613 | 22 | 260.5 | 30.33 | 88.09 |
| CSF1R | 1436 | https://www.kegg.jp/entry/hsa:1436 | 972 | 67 | 359.5 | 38.65 | 90.94 | 582 | 906 | 51 | 225.5 | 36.32 | 84.48 |
| TNK1 | 8711 | https://www.kegg.jp/entry/hsa:8711 | 666 | 68 | 359 | 38.79 | 84.06 | 122 | 373 | 53 | 223 | 36.32 | 80.51 |
| SRC | 6714 | https://www.kegg.jp/entry/hsa:6714 | 536 | 69 | 355 | 35.66 | 88.41 | 270 | 515 | 52 | 225.5 | 29.64 | 91.34 |
| KIT | 3815 | https://www.kegg.jp/entry/hsa:3815 | 976 | 70 | 351.5 | 38.13 | 93.12 | 589 | 925 | 65 | 208.5 | 33.2 | 87.0 |
| PDGFRA | 5156 | https://www.kegg.jp/entry/hsa:5156 | 1089 | 71 | 347.5 | 39.67 | 87.68 | 599 | 947 | 69 | 200 | 35.53 | 82.31 |
| FGR | 2268 | https://www.kegg.jp/entry/hsa:2268 | 529 | 72 | 346.5 | 37.24 | 86.59 | 267 | 508 | 74 | 195.5 | 28.46 | 91.34 |
| TYRO3 | 7301 | https://www.kegg.jp/entry/hsa:7301 | 890 | 73 | 346.5 | 33.33 | 92.39 | 522 | 787 | 73 | 196.5 | 26.67 | 92.06 |
| PTK6 | 5753 | https://www.kegg.jp/entry/hsa:5753 | 451 | 74 | 345.5 | 38.33 | 86.96 | 195 | 441 | 30 | 248 | 30.08 | 88.81 |
| LTK | 4058 | https://www.kegg.jp/entry/hsa:4058 | 864 | 75 | 345 | 36.14 | 90.22 | 513 | 777 | 23 | 257.5 | 31.71 | 88.81 |
| EPHA10 | 284656 | https://www.kegg.jp/entry/hsa:284656 | 1008 | 76 | 341 | 33.74 | 89.13 | 649 | 896 | 55 | 221 | 28.99 | 85.92 |
| ALK | 238 | https://www.kegg.jp/entry/hsa:238 | 1620 | 77 | 337 | 37.04 | 88.04 | 1116 | 1384 | 36 | 244.5 | 30.49 | 88.81 |
| RYK | 6259 | https://www.kegg.jp/entry/hsa:6259 | 607 | 78 | 337 | 36.02 | 85.51 | 336 | 592 | 58 | 217 | 26.67 | 92.06 |
| FLT4 | 2324 | https://www.kegg.jp/entry/hsa:2324 | 1363 | 79 | 333 | 37.1 | 89.86 | 851 | 1165 | 75 | 194.5 | 35.17 | 85.2 |
| PDGFRB | 5159 | https://www.kegg.jp/entry/hsa:5159 | 1106 | 80 | 331.5 | 38.96 | 90.22 | 606 | 959 | 79 | 191 | 31.58 | 89.17 |
| EPHB6 | 2051 | https://www.kegg.jp/entry/hsa:2051 | 729 | 81 | 297 | 29.39 | 88.77 | 378 | 624 | 80 | 190.5 | 25.12 | 74.73 |
| LMTK3 | 114783 | https://www.kegg.jp/entry/hsa:114783 | 1460 | 82 | 294.5 | 38.15 | 90.22 | 133 | 408 | 84 | 171 | 30.34 | 84.48 |
| STYK1 | 55359 | https://www.kegg.jp/entry/hsa:55359 | 422 | 83 | 265.5 | 34.6 | 85.87 | 117 | 381 | 85 | 160 | 29.82 | 82.31 |
| AATK | 9625 | https://www.kegg.jp/entry/hsa:9625 | 1374 | 84 | 255 | 33.06 | 88.77 | 125 | 393 | 81 | 187.5 | 30.97 | 81.59 |
| LMTK2 | 22853 | https://www.kegg.jp/entry/hsa:22853 | 1503 | 85 | 246.5 | 33.75 | 86.96 | 137 | 403 | 82 | 187.5 | 30.68 | 90.61 |
| EPHA6 | 285220 | https://www.kegg.jp/entry/hsa:285220 | 398 | 86 | 228.5 | 40.1 | 71.38 | 123 | 390 | 86 | 122 | 30.72 | 55.23 |
| PRAG1 | 157285 | https://www.kegg.jp/entry/hsa:157285 | 1406 | 87 | 76.5 | 30.66 | 49.64 | 1079 | 1264 | 87 | 57 | 37.04 | 9.75 |

</details>

<details>
<summary>variant_map.tsv — 597 rows</summary>

| JAK2_variant | figure_group | domain | target_gene | JH1_rank | JH2_rank | projected_target_change | reference_residue_conserved | all_four_local_positions | alignment_status | curated_notes | matched_exact_database_alleles | other_alleles_at_site |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| I1065T | study | JH1 | TNK2 | 1 | 35 | I332T | 1 | 332,335 | sensitive: do not treat as established |  |  |  |
| V1110E | study | JH1 | TNK2 | 1 | 35 | P372E | 0 | 372 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | TNK2 | 1 | 35 | E123D | 1 | 123 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | TNK2 | 1 | 35 | E144Q | 0 | 144 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | TNK2 | 1 | 35 | T152N | 1 | 152 | agreement of all settings |  |  | T152M Sugi (ClinVar index) |
| R938Q | previous | JH1 | TNK2 | 1 | 35 | L214Q | 0 | 214 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | TNK2 | 1 | 35 |  |  | gap,333 | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | TNK2 | 1 | 35 | P148R | 0 | 148 | agreement of all settings |  |  | P148= Sugi (ClinVar index); P148H Sugi (ClinVar index) |
| V578I | study | JH2 | TNK2 | 1 | 35 | V155I | 1 | 155 | agreement of all settings |  |  |  |
| L805I | study | JH2 | TNK2 | 1 | 35 | M393I | 0 | gap | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | TNK2 | 1 | 35 | N188N | 0 | 188 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | TNK2 | 1 | 35 | R191S | 0 | 191 | agreement of all settings |  |  | R191P Sugi (ClinVar index); R191H Sugi (ClinVar index) |
| V617I | previous | JH2 | TNK2 | 1 | 35 | V196I | 1 | 196 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | TNK2 | 1 | 35 | V196F | 1 | 196 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | TNK2 | 1 | 35 | V204F | 1 | 204 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | TNK2 | 1 | 35 | I332R | 0 | 332 | agreement of all settings |  |  |  |
| R426* | study | SH2 | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | TNK2 | 1 | 35 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | FRK | 2 | 3 | T438T | 0 | 438,gap | sensitive: do not treat as established; already WT |  |  |  |
| V1110E | study | JH1 | FRK | 2 | 3 | P474E | 0 | 474 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | FRK | 2 | 3 | R231D | 0 | 231 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | FRK | 2 | 3 |  |  | gap | gap/outside local aligned core |  |  |  |
| T875N | previous | JH1 | FRK | 2 | 3 | T256N | 1 | 256 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | FRK | 2 | 3 | Q315Q | 0 | 315 | agreement of all settings; already WT |  |  |  |
| R1063H | previous | JH1 | FRK | 2 | 3 | G436H | 0 | 436,gap | sensitive: do not treat as established |  |  |  |
| G571R | study | JH2 | FRK | 2 | 3 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | FRK | 2 | 3 | V259I | 1 | 259 | agreement of all settings |  |  |  |
| L805I | study | JH2 | FRK | 2 | 3 | L487I | 1 | 487 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | FRK | 2 | 3 | K288N | 0 | 288 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | FRK | 2 | 3 | Q291S | 0 | 291 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | FRK | 2 | 3 | T297I | 0 | 297 | agreement of all settings |  |  | T297S Sugi (ClinVar index) |
| V617F | previous | JH2 | FRK | 2 | 3 | T297F | 0 | 297 | agreement of all settings |  |  | T297S Sugi (ClinVar index) |
| V625F | previous | JH2 | FRK | 2 | 3 | I305F | 0 | 305 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | FRK | 2 | 3 | S435R | 1 | 435 | agreement of all settings |  |  |  |
| R426* | study | SH2 | FRK | 2 | 3 | R143* | 1 | 143 | agreement of all settings |  |  | R143G Sugi (ClinVar index) |
| C427R | study | SH2 | FRK | 2 | 3 | E144R | 0 | 144 | agreement of all settings |  |  |  |
| P37A | study | FERM | FRK | 2 | 3 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | FRK | 2 | 3 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | FRK | 2 | 3 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | FRK | 2 | 3 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | FRK | 2 | 3 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | FRK | 2 | 3 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | ABL1 | 3 | 4 |  |  | gap,441 | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | ABL1 | 3 | 4 | P480E | 0 | 480 | agreement of all settings |  |  | P480= Sugi (ClinVar index) |
| E846D | previous | JH1 | ABL1 | 3 | 4 | R239D | 0 | 239 | agreement of all settings; N-terminal extension/domain edge |  |  | R239C Sugi (ClinVar index); R239H Sugi (ClinVar index) |
| R867Q | previous | JH1 | ABL1 | 3 | 4 |  |  | gap | gap/outside local aligned core |  |  |  |
| T875N | previous | JH1 | ABL1 | 3 | 4 | Y264N | 0 | 264 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | ABL1 | 3 | 4 | L324Q | 0 | 324 | agreement of all settings | L324Q: A small BCR::ABL1-mutant clone was detected in a chronic-phase CML patient before imatinib, without an isolated biochemical result inferred. |  |  |
| R1063H | previous | JH1 | ABL1 | 3 | 4 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | ABL1 | 3 | 4 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | ABL1 | 3 | 4 | V268I | 1 | 268 | agreement of all settings |  |  |  |
| L805I | study | JH2 | ABL1 | 3 | 4 | F493I | 0 | 493 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | ABL1 | 3 | 4 | N297N | 0 | 297 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | ABL1 | 3 | 4 | Q300S | 0 | 300 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | ABL1 | 3 | 4 | T306I | 0 | 306 | agreement of all settings | T306I: BCR::ABL1 T306I reported in patient 29. Thesis-level evidence only. |  |  |
| V617F | previous | JH2 | ABL1 | 3 | 4 | T306F | 0 | 306 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | ABL1 | 3 | 4 | I314F | 0 | 314 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | ABL1 | 3 | 4 | P441R | 0 | 441 | agreement of all settings |  |  | P441= Sugi (ClinVar index) |
| R426* | study | SH2 | ABL1 | 3 | 4 | R152* | 1 | 152,gap | sensitive: do not treat as established |  |  | R152H Sugi (ClinVar index) |
| C427R | study | SH2 | ABL1 | 3 | 4 | E153R | 0 | 153,gap | sensitive: do not treat as established |  |  | E153Q Sugi (ClinVar index) |
| P37A | study | FERM | ABL1 | 3 | 4 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | ABL1 | 3 | 4 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | ABL1 | 3 | 4 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | ABL1 | 3 | 4 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | ABL1 | 3 | 4 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | ABL1 | 3 | 4 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | NTRK1 | 4 | 17 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | NTRK1 | 4 | 17 | P768E | 0 | 768 | agreement of all settings |  |  | P768H Sugi (ClinVar index); P768L Sugi (ClinVar index); P768S CanProVar |
| E846D | previous | JH1 | NTRK1 | 4 | 17 | R507D | 0 | 507 | agreement of all settings; N-terminal extension/domain edge |  |  | R507C Sugi (ClinVar index); R507C CanProVar |
| R867Q | previous | JH1 | NTRK1 | 4 | 17 | E528Q | 0 | 528 | agreement of all settings |  |  | E528* Sugi (ClinVar index) |
| T875N | previous | JH1 | NTRK1 | 4 | 17 | D537N | 0 | 537 | agreement of all settings |  |  | D537E Sugi (ClinVar index); D537E CanProVar |
| R938Q | previous | JH1 | NTRK1 | 4 | 17 | N598Q | 0 | 598 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | NTRK1 | 4 | 17 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | NTRK1 | 4 | 17 |  |  | gap,534 | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | NTRK1 | 4 | 17 | V541I | 1 | 541 | agreement of all settings | V541L: Sugi indexes a germline VUS at the same codon for Val-to-Leu. It is not Val-to-Ile. |  | V541L Sugi (ClinVar index) |
| L805I | study | JH2 | NTRK1 | 4 | 17 | L781I | 1 | 781 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | NTRK1 | 4 | 17 | H571N | 1 | 571 | agreement of all settings |  |  | H571Q Sugi (ClinVar index) |
| L611S | previous | JH2 | NTRK1 | 4 | 17 | R574S | 0 | 574 | agreement of all settings | R574S: VUS in a ClinVar-derived index; distinct from the differently numbered alternative NTRK1 alleles. | R574S Sugi (ClinVar index) | R574H Sugi (ClinVar index); R574C Sugi (ClinVar index) |
| V617I | previous | JH2 | NTRK1 | 4 | 17 | T580I | 0 | 580 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | NTRK1 | 4 | 17 | T580F | 0 | 580 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | NTRK1 | 4 | 17 | V588F | 1 | 588 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | NTRK1 | 4 | 17 | Y729R | 0 | 729 | agreement of all settings |  |  |  |
| R426* | study | SH2 | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | NTRK1 | 4 | 17 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | FGFR1 | 5 | 57 | L696T | 0 | 696 | agreement of all settings |  |  | L696= Sugi (ClinVar index) |
| V1110E | study | JH1 | FGFR1 | 5 | 57 | P741E | 0 | 741 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | FGFR1 | 5 | 57 | R475D | 0 | gap | sensitive: do not treat as established; N-terminal extension/domain edge |  |  | R475Q Sugi (ClinVar index); R475W Sugi (ClinVar index) |
| R867Q | previous | JH1 | FGFR1 | 5 | 57 | G499Q | 0 | 499 | agreement of all settings |  |  | G499R Sugi (ClinVar index) |
| T875N | previous | JH1 | FGFR1 | 5 | 57 | R507N | 0 | 507 | agreement of all settings |  |  | R507H ClinVar Miner (index); R507L Sugi (ClinVar index); R507C Sugi (ClinVar index); R507H Sugi (ClinVar index) |
| R938Q | previous | JH1 | FGFR1 | 5 | 57 | R570Q | 1 | 570 | agreement of all settings | R570Q: Indexed as VUS (VCV2580728); reported rare in gnomAD v4.1, not a functional assay. | R570Q Sugi (ClinVar index) | R570W Sugi (ClinVar index); R570= Sugi (ClinVar index) |
| R1063H | previous | JH1 | FGFR1 | 5 | 57 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | FGFR1 | 5 | 57 | D503R | 0 | 503,504 | sensitive: do not treat as established |  |  | D503E Sugi (ClinVar index); D503= Sugi (ClinVar index) |
| V578I | study | JH2 | FGFR1 | 5 | 57 | V511I | 1 | 511 | agreement of all settings |  |  |  |
| L805I | study | JH2 | FGFR1 | 5 | 57 | L754I | 1 | 754 | agreement of all settings |  |  | L754= ClinVar Miner (index); L754= Sugi (ClinVar index) |
| H608N | previous | JH2 | FGFR1 | 5 | 57 | N543N | 0 | 543 | agreement of all settings; already WT |  |  | N543D Sugi (ClinVar index) |
| L611S | previous | JH2 | FGFR1 | 5 | 57 | N546S | 0 | 546 | agreement of all settings | N546S: Reported in a pediatric spinal glioblastoma together with FGFR1 K656E. This observation alone cannot isolate the effect. |  | N546K Sugi (ClinVar index) |
| V617I | previous | JH2 | FGFR1 | 5 | 57 | T552I | 0 | 552 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | FGFR1 | 5 | 57 | T552F | 0 | 552 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | FGFR1 | 5 | 57 | I560F | 0 | 560 | agreement of all settings |  |  | I560= Sugi (ClinVar index) |
| S755R | previous | JH2 | FGFR1 | 5 | 57 | P702R | 0 | 702 | agreement of all settings |  |  | P702= ClinVar Miner (index); P702= Sugi (ClinVar index) |
| R426* | study | SH2 | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | FGFR1 | 5 | 57 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | DDR2 | 6 | 59 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | DDR2 | 6 | 59 | T836E | 0 | 836 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | DDR2 | 6 | 59 | R560D | 0 | 560 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | DDR2 | 6 | 59 | E581Q | 0 | 581 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | DDR2 | 6 | 59 | Q601N | 0 | 601 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | DDR2 | 6 | 59 | N663Q | 0 | 663 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | DDR2 | 6 | 59 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | DDR2 | 6 | 59 | G575R | 1 | 575,598 | sensitive: do not treat as established |  |  |  |
| V578I | study | JH2 | DDR2 | 6 | 59 | V605I | 1 | 584,605 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | DDR2 | 6 | 59 | I845I | 0 | gap | sensitive: do not treat as established; already WT |  |  |  |
| H608N | previous | JH2 | DDR2 | 6 | 59 | N636N | 0 | 636 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | DDR2 | 6 | 59 | H639S | 0 | 639 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | DDR2 | 6 | 59 | I645I | 0 | 645 | agreement of all settings; already WT |  |  |  |
| V617F | previous | JH2 | DDR2 | 6 | 59 | I645F | 0 | 645 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | DDR2 | 6 | 59 | I653F | 0 | 653 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | DDR2 | 6 | 59 | S790R | 1 | 790 | agreement of all settings |  |  |  |
| R426* | study | SH2 | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | DDR2 | 6 | 59 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | NTRK3 | 7 | 13 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | NTRK3 | 7 | 13 | P811E | 0 | 811 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | NTRK3 | 7 | 13 | R535D | 0 | 535 | agreement of all settings; N-terminal extension/domain edge |  |  | R535M CanProVar |
| R867Q | previous | JH1 | NTRK3 | 7 | 13 | N559Q | 0 | 559 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | NTRK3 | 7 | 13 | M567N | 0 | 567 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | NTRK3 | 7 | 13 | N626Q | 0 | 626 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | NTRK3 | 7 | 13 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | NTRK3 | 7 | 13 | Y558R | 0 | 558 | agreement of all settings |  |  |  |
| V578I | study | JH2 | NTRK3 | 7 | 13 | V569I | 1 | 565 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | NTRK3 | 7 | 13 | L824I | 1 | 824 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | NTRK3 | 7 | 13 | H599N | 1 | 599 | agreement of all settings |  |  | H599Y CanProVar |
| L611S | previous | JH2 | NTRK3 | 7 | 13 | K602S | 0 | 602 | agreement of all settings |  |  | K602R CanProVar; K602T CanProVar |
| V617I | previous | JH2 | NTRK3 | 7 | 13 | G608I | 0 | 608 | agreement of all settings | G608S: Colorectal cancer mutant retained the ability to induce apoptosis when transfected into RKO cells. No phenylalanine result inferred. |  | G608S CanProVar; G608C CanProVar |
| V617F | previous | JH2 | NTRK3 | 7 | 13 | G608F | 0 | 608 | agreement of all settings | G608S: Colorectal cancer mutant retained the ability to induce apoptosis when transfected into RKO cells. No phenylalanine result inferred. |  | G608S CanProVar; G608C CanProVar |
| V625F | previous | JH2 | NTRK3 | 7 | 13 | V616F | 1 | 616 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | NTRK3 | 7 | 13 | F772R | 0 | 772 | agreement of all settings |  |  |  |
| R426* | study | SH2 | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | NTRK3 | 7 | 13 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | FGFR2 | 8 | 62 | L699T | 0 | 699 | agreement of all settings |  |  |  |
| V1110E | study | JH1 | FGFR2 | 8 | 62 | P744E | 0 | 744 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | FGFR2 | 8 | 62 | R478D | 0 | 478 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | FGFR2 | 8 | 62 | E499Q | 0 | 499 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | FGFR2 | 8 | 62 | E510N | 0 | 510 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | FGFR2 | 8 | 62 | R573Q | 1 | 573 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | FGFR2 | 8 | 62 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | FGFR2 | 8 | 62 | D506R | 0 | 506,507 | sensitive: do not treat as established |  |  |  |
| V578I | study | JH2 | FGFR2 | 8 | 62 | V514I | 1 | 514 | agreement of all settings |  |  |  |
| L805I | study | JH2 | FGFR2 | 8 | 62 | L757I | 1 | 757 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | FGFR2 | 8 | 62 | N546N | 0 | 546 | agreement of all settings; already WT |  |  | N546K CanProVar; N546D CanProVar; N546S CanProVar |
| L611S | previous | JH2 | FGFR2 | 8 | 62 | N549S | 0 | 549 | agreement of all settings | N549S: JCGA lists this somatic allele as COSV60645338; CKB traces increased transforming activity and growth factor independence to experimental studies. p.N550S is the same genomic allele on an alternative transcript. | N549S CanProVar; N549S JCGA | N549K CanProVar; N549H CanProVar; N549K JCGA; N549H JCGA |
| V617I | previous | JH2 | FGFR2 | 8 | 62 | T555I | 0 | 555 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | FGFR2 | 8 | 62 | T555F | 0 | 555 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | FGFR2 | 8 | 62 | I563F | 0 | 563 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | FGFR2 | 8 | 62 | P705R | 0 | 705 | agreement of all settings |  |  |  |
| R426* | study | SH2 | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | FGFR2 | 8 | 62 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | NTRK2 | 9 | 6 | S758T | 0 | 758,gap | sensitive: do not treat as established |  |  |  |
| V1110E | study | JH1 | NTRK2 | 9 | 6 | P794E | 0 | 794 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | NTRK2 | 9 | 6 | K534D | 0 | 534,gap | sensitive: do not treat as established; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | NTRK2 | 9 | 6 |  |  | gap,559,556 | gap/outside local aligned core |  |  |  |
| T875N | previous | JH1 | NTRK2 | 9 | 6 | I567N | 0 | 567,565 | sensitive: do not treat as established |  |  |  |
| R938Q | previous | JH1 | NTRK2 | 9 | 6 | N626Q | 0 | 626 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | NTRK2 | 9 | 6 | Q756H | 0 | 756,gap | sensitive: do not treat as established |  |  |  |
| G571R | study | JH2 | NTRK2 | 9 | 6 | N559R | 0 | 559,562 | sensitive: do not treat as established |  |  |  |
| V578I | study | JH2 | NTRK2 | 9 | 6 | V569I | 1 | 569 | agreement of all settings |  |  |  |
| L805I | study | JH2 | NTRK2 | 9 | 6 | L810I | 1 | 807 | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | NTRK2 | 9 | 6 | H599N | 1 | 599 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | NTRK2 | 9 | 6 | K602S | 0 | 602 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | NTRK2 | 9 | 6 | V608I | 1 | 608 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | NTRK2 | 9 | 6 | V608F | 1 | 608 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | NTRK2 | 9 | 6 | V616F | 1 | 616 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | NTRK2 | 9 | 6 | Y755R | 0 | 755 | agreement of all settings |  |  |  |
| R426* | study | SH2 | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | NTRK2 | 9 | 6 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | ERBB4 | 10 | 28 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | ERBB4 | 10 | 28 | A961E | 0 | 961 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | ERBB4 | 10 | 28 | E715D | 1 | 715 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | ERBB4 | 10 | 28 | I736Q | 0 | 736 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | ERBB4 | 10 | 28 | V744N | 0 | 744 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | ERBB4 | 10 | 28 | L805Q | 0 | 805 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | ERBB4 | 10 | 28 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | ERBB4 | 10 | 28 | V744R | 0 | 744 | agreement of all settings |  |  |  |
| V578I | study | JH2 | ERBB4 | 10 | 28 | V748I | 1 | 748 | agreement of all settings |  |  |  |
| L805I | study | JH2 | ERBB4 | 10 | 28 | F974I | 0 | 974 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | ERBB4 | 10 | 28 | H779N | 1 | 779 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | ERBB4 | 10 | 28 | R782S | 0 | 782 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | ERBB4 | 10 | 28 | L788I | 0 | 788 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | ERBB4 | 10 | 28 | L788F | 0 | 788 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | ERBB4 | 10 | 28 | V795F | 1 | 795 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | ERBB4 | 10 | 28 | D922R | 0 | 922 | agreement of all settings |  |  |  |
| R426* | study | SH2 | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | ERBB4 | 10 | 28 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | PTK7 | 11 | 46 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | PTK7 | 11 | 46 | P1048E | 0 | 1048 | agreement of all settings |  |  | P1048L Sugi (ClinVar index) |
| E846D | previous | JH1 | PTK7 | 11 | 46 | R793D | 0 | 793 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | PTK7 | 11 | 46 | K814Q | 0 | 814 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | PTK7 | 11 | 46 | V822N | 0 | 822 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | PTK7 | 11 | 46 | K884Q | 0 | 884 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | PTK7 | 11 | 46 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | PTK7 | 11 | 46 |  |  | gap,820 | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | PTK7 | 11 | 46 | V827I | 1 | 827 | agreement of all settings |  |  |  |
| L805I | study | JH2 | PTK7 | 11 | 46 | L1061I | 1 | gap | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | PTK7 | 11 | 46 | N857N | 0 | 857 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | PTK7 | 11 | 46 | R860S | 0 | 860 | agreement of all settings |  |  | R860Q Sugi (ClinVar index) |
| V617I | previous | JH2 | PTK7 | 11 | 46 | R866I | 0 | 866 | agreement of all settings |  |  | R866Q Sugi (ClinVar index) |
| V617F | previous | JH2 | PTK7 | 11 | 46 | R866F | 0 | 866 | agreement of all settings |  |  | R866Q Sugi (ClinVar index) |
| V625F | previous | JH2 | PTK7 | 11 | 46 | V874F | 1 | 874 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | PTK7 | 11 | 46 | G1008R | 0 | 1008 | agreement of all settings |  |  |  |
| R426* | study | SH2 | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | PTK7 | 11 | 46 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | ABL2 | 12 | 21 |  |  | gap,487 | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | ABL2 | 12 | 21 | P526E | 0 | 526 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | ABL2 | 12 | 21 | R285D | 0 | 285 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | ABL2 | 12 | 21 |  |  | gap | gap/outside local aligned core |  |  |  |
| T875N | previous | JH1 | ABL2 | 12 | 21 | Y310N | 0 | 310 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | ABL2 | 12 | 21 | L370Q | 0 | 370 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | ABL2 | 12 | 21 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | ABL2 | 12 | 21 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | ABL2 | 12 | 21 | V314I | 1 | 314 | agreement of all settings |  |  |  |
| L805I | study | JH2 | ABL2 | 12 | 21 | F539I | 0 | 539 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | ABL2 | 12 | 21 | N343N | 0 | 343 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | ABL2 | 12 | 21 | Q346S | 0 | 346 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | ABL2 | 12 | 21 | T352I | 0 | 352 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | ABL2 | 12 | 21 | T352F | 0 | 352 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | ABL2 | 12 | 21 | V360F | 1 | 360 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | ABL2 | 12 | 21 | P487R | 0 | 487 | agreement of all settings |  |  |  |
| R426* | study | SH2 | ABL2 | 12 | 21 | R198* | 1 | 198,gap | sensitive: do not treat as established |  |  |  |
| C427R | study | SH2 | ABL2 | 12 | 21 | E199R | 0 | 199,gap | sensitive: do not treat as established |  |  |  |
| P37A | study | FERM | ABL2 | 12 | 21 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | ABL2 | 12 | 21 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | ABL2 | 12 | 21 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | ABL2 | 12 | 21 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | ABL2 | 12 | 21 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | ABL2 | 12 | 21 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | SYK | 13 | 10 | K577T | 0 | 577 | agreement of all settings |  |  |  |
| V1110E | study | JH1 | SYK | 13 | 10 | V613E | 1 | 613 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | SYK | 13 | 10 | D366D | 0 | 366,gap | sensitive: do not treat as established; N-terminal extension/domain edge; already WT |  |  |  |
| R867Q | previous | JH1 | SYK | 13 | 10 | Y389Q | 0 | 389 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | SYK | 13 | 10 | V395N | 0 | 395 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | SYK | 13 | 10 | N457Q | 0 | 457 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | SYK | 13 | 10 | G575H | 0 | 575 | agreement of all settings |  |  |  |
| G571R | study | JH2 | SYK | 13 | 10 | Y390R | 0 | 390 | agreement of all settings |  |  |  |
| V578I | study | JH2 | SYK | 13 | 10 | V399I | 1 | 399 | agreement of all settings |  |  |  |
| L805I | study | JH2 | SYK | 13 | 10 | L626I | 1 | gap | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | SYK | 13 | 10 | Y431N | 0 | 431 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | SYK | 13 | 10 | R434S | 0 | 434 | agreement of all settings |  |  | R434Q Sugi (ClinVar index); R434= Sugi (ClinVar index) |
| V617I | previous | JH2 | SYK | 13 | 10 | E440I | 0 | 440 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | SYK | 13 | 10 | E440F | 0 | 440 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | SYK | 13 | 10 | V447F | 1 | 447 | agreement of all settings |  |  | V447I Sugi (ClinVar index) |
| S755R | previous | JH2 | SYK | 13 | 10 | R574R | 0 | 574 | agreement of all settings; already WT |  |  |  |
| R426* | study | SH2 | SYK | 13 | 10 | R42* | 1 | 42 | agreement of all settings; tandem SH2; best local match only |  |  | R42H CanProVar |
| C427R | study | SH2 | SYK | 13 | 10 | Q43R | 0 | 43 | agreement of all settings; tandem SH2; best local match only |  |  | Q43= Sugi (ClinVar index) |
| P37A | study | FERM | SYK | 13 | 10 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | SYK | 13 | 10 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | SYK | 13 | 10 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | SYK | 13 | 10 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | SYK | 13 | 10 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | SYK | 13 | 10 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | FGFR3 | 14 | 61 | L690T | 0 | 690 | agreement of all settings |  |  |  |
| V1110E | study | JH1 | FGFR3 | 14 | 61 | P735E | 0 | 735 | agreement of all settings |  |  | P735= Sugi (ClinVar index) |
| E846D | previous | JH1 | FGFR3 | 14 | 61 | R469D | 0 | gap | sensitive: do not treat as established; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | FGFR3 | 14 | 61 | E490Q | 0 | 490 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | FGFR3 | 14 | 61 | A499N | 0 | 499,498 | sensitive: do not treat as established |  |  | A499P Sugi (ClinVar index); A499= Sugi (ClinVar index) |
| R938Q | previous | JH1 | FGFR3 | 14 | 61 | R564Q | 1 | 564 | agreement of all settings | R564Q: Single-submitter VUS indexed by Sugi. | R564Q Sugi (ClinVar index) | R564W Sugi (ClinVar index) |
| R1063H | previous | JH1 | FGFR3 | 14 | 61 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | FGFR3 | 14 | 61 | R498R | 0 | 498 | agreement of all settings; already WT |  |  | R498Q Sugi (ClinVar index); R498W Sugi (ClinVar index); R498= Sugi (ClinVar index) |
| V578I | study | JH2 | FGFR3 | 14 | 61 | V505I | 1 | 505 | agreement of all settings | V505I: An MCF10A proliferation assay failed to validate the predicted gain of function. The ClinVar condition record has conflicting germline classifications. | V505I Sugi (ClinVar index) |  |
| L805I | study | JH2 | FGFR3 | 14 | 61 | L748I | 1 | 748 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | FGFR3 | 14 | 61 | N537N | 0 | 537 | agreement of all settings; already WT |  |  | N537= Sugi (ClinVar index) |
| L611S | previous | JH2 | FGFR3 | 14 | 61 | N540S | 0 | 540 | agreement of all settings | N540S: Pathogenic/likely pathogenic in ClinVar; reported in hypochondroplasia families. Experimentally activating, with weaker activation than N540K in the cited assay. | N540S Sugi (ClinVar index) | N540K Sugi (ClinVar index); N540D Sugi (ClinVar index); N540T Sugi (ClinVar index); N540H Sugi (ClinVar index); N540= Sugi (ClinVar index) |
| V617I | previous | JH2 | FGFR3 | 14 | 61 | T546I | 0 | 546 | agreement of all settings |  |  | T546K Sugi (ClinVar index) |
| V617F | previous | JH2 | FGFR3 | 14 | 61 | T546F | 0 | 546 | agreement of all settings |  |  | T546K Sugi (ClinVar index) |
| V625F | previous | JH2 | FGFR3 | 14 | 61 | L554F | 0 | 554 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | FGFR3 | 14 | 61 | P696R | 0 | 696 | agreement of all settings |  |  | P696= Sugi (ClinVar index) |
| R426* | study | SH2 | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | FGFR3 | 14 | 61 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | RET | 15 | 7 | L947T | 0 | 947 | agreement of all settings |  |  | L947= Sugi (ClinVar index) |
| V1110E | study | JH1 | RET | 15 | 7 | P992E | 0 | 992 | agreement of all settings |  |  | P992L CanProVar |
| E846D | previous | JH1 | RET | 15 | 7 | R721D | 0 | 721 | agreement of all settings; N-terminal extension/domain edge |  |  | R721Q Sugi (ClinVar index); R721W CanProVar; R721Q CanProVar |
| R867Q | previous | JH1 | RET | 15 | 7 | T742Q | 0 | 742 | agreement of all settings |  |  | T742= Sugi (ClinVar index) |
| T875N | previous | JH1 | RET | 15 | 7 | A750N | 0 | 750 | agreement of all settings |  |  | A750G Sugi (ClinVar index); A750V CanProVar |
| R938Q | previous | JH1 | RET | 15 | 7 | R813Q | 1 | 813 | agreement of all settings | R813Q: Reduced RET signaling, migration and colony formation versus wild type in cell assays. Reported in Hirschsprung disease. The cited MEN2 ClinVar record is VUS. JAK2 R938Q was inherited in cis with S755R. | R813Q Sugi (ClinVar index) | R813G Sugi (ClinVar index); R813W Sugi (ClinVar index); R813= Sugi (ClinVar index) |
| R1063H | previous | JH1 | RET | 15 | 7 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | RET | 15 | 7 | G748R | 1 | 748 | agreement of all settings | G748D: Hirschsprung disease index lists Gly-to-Asp as uncertain significance, rs1314127008. JH2 beta2-beta3 loop site is a sequence projection. |  | G748D Sugi (ClinVar index); G748C CanProVar |
| V578I | study | JH2 | RET | 15 | 7 | V755I | 1 | 755 | agreement of all settings |  |  |  |
| L805I | study | JH2 | RET | 15 | 7 | L1005I | 1 | 1005 | agreement of all settings |  |  | L1005= Sugi (ClinVar index) |
| H608N | previous | JH2 | RET | 15 | 7 | H786N | 1 | 786 | agreement of all settings |  |  | H786Y Sugi (ClinVar index); H786= Sugi (ClinVar index) |
| L611S | previous | JH2 | RET | 15 | 7 | K789S | 0 | 789 | agreement of all settings |  |  | K789E Sugi (ClinVar index); K789E CanProVar |
| V617I | previous | JH2 | RET | 15 | 7 | S795I | 0 | 795 | agreement of all settings |  |  | S795= Sugi (ClinVar index) |
| V617F | previous | JH2 | RET | 15 | 7 | S795F | 0 | 795 | agreement of all settings |  |  | S795= Sugi (ClinVar index) |
| V625F | previous | JH2 | RET | 15 | 7 | I803F | 0 | 803 | agreement of all settings |  |  | I803= Sugi (ClinVar index) |
| S755R | previous | JH2 | RET | 15 | 7 | P953R | 0 | 953 | agreement of all settings |  |  |  |
| R426* | study | SH2 | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | RET | 15 | 7 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | TIE1 | 16 | 77 | L1049T | 0 | 1049 | agreement of all settings |  |  |  |
| V1110E | study | JH1 | TIE1 | 16 | 77 | P1094E | 0 | 1094 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | TIE1 | 16 | 77 | W836D | 0 | 836 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | TIE1 | 16 | 77 | K859Q | 0 | 859 | agreement of all settings |  |  | K859N Sugi (ClinVar index) |
| T875N | previous | JH1 | TIE1 | 16 | 77 |  |  | gap | gap/outside local aligned core |  |  |  |
| R938Q | previous | JH1 | TIE1 | 16 | 77 | L926Q | 0 | 926 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | TIE1 | 16 | 77 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | TIE1 | 16 | 77 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | TIE1 | 16 | 77 | A867I | 0 | 868 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | TIE1 | 16 | 77 | L1107I | 1 | 1107 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | TIE1 | 16 | 77 | P898N | 0 | 898 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | TIE1 | 16 | 77 | I901S | 0 | 901 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | TIE1 | 16 | 77 | K908I | 0 | 908 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | TIE1 | 16 | 77 | K908F | 0 | 908 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | TIE1 | 16 | 77 | A916F | 0 | 916 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | TIE1 | 16 | 77 | C1055R | 0 | 1055 | agreement of all settings |  |  |  |
| R426* | study | SH2 | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | TIE1 | 16 | 77 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | EGFR | 17 | 40 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | EGFR | 17 | 40 | A955E | 0 | 955 | agreement of all settings |  |  | A955T Sugi (ClinVar index) |
| E846D | previous | JH1 | EGFR | 17 | 40 | E709D | 1 | 709 | agreement of all settings; N-terminal extension/domain edge | E709D: c.2127A>C indexed as germline VUS. Different allele from E709_T710delinsD. | E709D Sugi (ClinVar index) | E709K JCGA; E709A JCGA; E709V JCGA; E709G JCGA |
| R867Q | previous | JH1 | EGFR | 17 | 40 | L730Q | 0 | 730 | agreement of all settings |  |  | L730R Sugi (ClinVar index) |
| T875N | previous | JH1 | EGFR | 17 | 40 | V738N | 0 | 738 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | EGFR | 17 | 40 | L799Q | 0 | 799 | agreement of all settings |  |  | L799= Sugi (ClinVar index) |
| R1063H | previous | JH1 | EGFR | 17 | 40 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | EGFR | 17 | 40 | V738R | 0 | 738 | agreement of all settings |  |  |  |
| V578I | study | JH2 | EGFR | 17 | 40 | V742I | 1 | 742 | agreement of all settings | V742I: Conflicting germline submissions (VUS and likely benign). No somatic oncogenicity submission in the cited record. | V742I Sugi (ClinVar index) | V742= Sugi (ClinVar index) |
| L805I | study | JH2 | EGFR | 17 | 40 | F968I | 0 | 968 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | EGFR | 17 | 40 | H773N | 1 | 773 | agreement of all settings | H773N: Single-submitter uncertain significance. |  | H773= Sugi (ClinVar index); H773L JCGA |
| L611S | previous | JH2 | EGFR | 17 | 40 | R776S | 0 | 776 | agreement of all settings | R776S: Table 1 reports G719A+R776S. Clinical observation of compound mutations; do not attribute a single-mutant phenotype. \| R776H: Dimer-dependent activation; mutants preferentially occupied the acceptor position. Germline classifications conflict. |  | R776H Sugi (ClinVar index); R776C Sugi (ClinVar index); R776= Sugi (ClinVar index); R776H JCGA |
| V617I | previous | JH2 | EGFR | 17 | 40 | L782I | 0 | 782 | agreement of all settings |  |  | L782= Sugi (ClinVar index) |
| V617F | previous | JH2 | EGFR | 17 | 40 | L782F | 0 | 782 | agreement of all settings |  |  | L782= Sugi (ClinVar index) |
| V625F | previous | JH2 | EGFR | 17 | 40 | I789F | 0 | 790 | sensitive: do not treat as established | I789L / I789V: Anchored site lies immediately before gatekeeper T790. ClinVar records for Leu and Val. Do not count T790M. |  |  |
| S755R | previous | JH2 | EGFR | 17 | 40 | D916R | 0 | 916 | agreement of all settings |  |  | D916= Sugi (ClinVar index); D916N Sugi (ClinVar index) |
| R426* | study | SH2 | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | EGFR | 17 | 40 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | CSK | 18 | 49 |  |  | gap | gap/outside local aligned core |  |  |  |
| V1110E | study | JH1 | CSK | 18 | 49 | A427E | 0 | 427 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | CSK | 18 | 49 | M192D | 0 | gap | sensitive: do not treat as established; N-terminal extension/domain edge |  |  | M192T Sugi (ClinVar index) |
| R867Q | previous | JH1 | CSK | 18 | 49 |  |  | gap | gap/outside local aligned core |  |  |  |
| T875N | previous | JH1 | CSK | 18 | 49 | R215N | 0 | 215 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | CSK | 18 | 49 | V275Q | 0 | 275 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | CSK | 18 | 49 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | CSK | 18 | 49 |  |  | 216,gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | CSK | 18 | 49 | V219I | 1 | gap | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | CSK | 18 | 49 | L440I | 1 | 440 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | CSK | 18 | 49 | N247N | 0 | 247 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | CSK | 18 | 49 | Q250S | 0 | 250 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | CSK | 18 | 49 | V256I | 1 | 256 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | CSK | 18 | 49 | V256F | 1 | 256 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | CSK | 18 | 49 | V265F | 1 | 265 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | CSK | 18 | 49 | P388R | 0 | 388 | agreement of all settings |  |  |  |
| R426* | study | SH2 | CSK | 18 | 49 | R107* | 1 | 107 | agreement of all settings |  |  |  |
| C427R | study | SH2 | CSK | 18 | 49 | E108R | 0 | 108,gap | sensitive: do not treat as established |  |  |  |
| P37A | study | FERM | CSK | 18 | 49 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | CSK | 18 | 49 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | CSK | 18 | 49 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | CSK | 18 | 49 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | CSK | 18 | 49 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | CSK | 18 | 49 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | FGFR4 | 19 | 70 | L685T | 0 | 685 | agreement of all settings |  |  |  |
| V1110E | study | JH1 | FGFR4 | 19 | 70 | P730E | 0 | 730 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | FGFR4 | 19 | 70 | R464D | 0 | 464 | agreement of all settings; N-terminal extension/domain edge |  |  | R464P Sugi (ClinVar index) |
| R867Q | previous | JH1 | FGFR4 | 19 | 70 | G488Q | 0 | 488 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | FGFR4 | 19 | 70 | Q496N | 0 | 496 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | FGFR4 | 19 | 70 | R559Q | 1 | 559 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | FGFR4 | 19 | 70 |  |  | gap | gap/outside local aligned core |  |  |  |
| G571R | study | JH2 | FGFR4 | 19 | 70 | G488R | 1 | 488,490,493 | sensitive: do not treat as established |  |  |  |
| V578I | study | JH2 | FGFR4 | 19 | 70 | V500I | 1 | 500,497 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | FGFR4 | 19 | 70 | L743I | 1 | 743 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | FGFR4 | 19 | 70 | N532N | 0 | 532 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | FGFR4 | 19 | 70 | N535S | 0 | 535 | agreement of all settings | N535K: JCGA lists a somatic Lys change at the same site. No quantitative isolated Ser result verified here. |  | N535K JCGA |
| V617I | previous | JH2 | FGFR4 | 19 | 70 | T541I | 0 | 541 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | FGFR4 | 19 | 70 | T541F | 0 | 541 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | FGFR4 | 19 | 70 | I549F | 0 | 549 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | FGFR4 | 19 | 70 | P691R | 0 | 691 | agreement of all settings |  |  |  |
| R426* | study | SH2 | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| F240V | study | FERM | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| H380Y | study | FERM | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| T108A | previous | FERM | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| Y317H | previous | FERM | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| H345L | previous | FERM | FGFR4 | 19 | 70 |  |  |  | absent domain or not applicable |  |  |  |
| I1065T | study | JH1 | PTK2 | 20 | 32 | K627T | 0 | 627 | agreement of all settings |  |  |  |
| V1110E | study | JH1 | PTK2 | 20 | 32 | P663E | 0 | 663 | agreement of all settings |  |  |  |
| E846D | previous | JH1 | PTK2 | 20 | 32 | R419D | 0 | 419 | agreement of all settings; N-terminal extension/domain edge |  |  |  |
| R867Q | previous | JH1 | PTK2 | 20 | 32 | I440Q | 0 | 440 | agreement of all settings |  |  |  |
| T875N | previous | JH1 | PTK2 | 20 | 32 | P447N | 0 | 447 | agreement of all settings |  |  |  |
| R938Q | previous | JH1 | PTK2 | 20 | 32 | R508Q | 1 | 508 | agreement of all settings |  |  |  |
| R1063H | previous | JH1 | PTK2 | 20 | 32 | G625H | 0 | 625 | agreement of all settings |  |  |  |
| G571R | study | JH2 | PTK2 | 20 | 32 | P444R | 0 | gap | sensitive: do not treat as established |  |  |  |
| V578I | study | JH2 | PTK2 | 20 | 32 | V451I | 1 | 447 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | PTK2 | 20 | 32 | L676I | 1 | 676 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | PTK2 | 20 | 32 | H482N | 1 | 482 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | PTK2 | 20 | 32 | K485S | 0 | 485 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | PTK2 | 20 | 32 | T491I | 0 | 491,490 | sensitive: do not treat as established |  |  |  |
| V617F | previous | JH2 | PTK2 | 20 | 32 | T491F | 0 | 491,490 | sensitive: do not treat as established |  |  |  |
| V625F | previous | JH2 | PTK2 | 20 | 32 | I498F | 0 | 498 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | PTK2 | 20 | 32 | Q624R | 0 | 624 | agreement of all settings |  |  |  |
| R426* | study | SH2 | PTK2 | 20 | 32 |  |  |  | absent domain or not applicable |  |  |  |
| C427R | study | SH2 | PTK2 | 20 | 32 |  |  |  | absent domain or not applicable |  |  |  |
| P37A | study | FERM | PTK2 | 20 | 32 |  |  | gap | unresolved FERM |  |  |  |
| F240V | study | FERM | PTK2 | 20 | 32 |  |  | gap,231,137 | unresolved FERM |  |  |  |
| H380Y | study | FERM | PTK2 | 20 | 32 |  |  | gap | unresolved FERM |  |  |  |
| T108A | previous | FERM | PTK2 | 20 | 32 |  |  | 107,gap | unresolved FERM |  |  |  |
| Y317H | previous | FERM | PTK2 | 20 | 32 |  |  | gap | unresolved FERM |  |  |  |
| H345L | previous | FERM | PTK2 | 20 | 32 |  |  | gap | unresolved FERM |  |  |  |
| G571R | study | JH2 | PTK2B | 22 | 1 |  |  | gap,449,447 | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | PTK2B | 22 | 1 | V454I | 1 | 454 | agreement of all settings |  |  |  |
| L805I | study | JH2 | PTK2B | 22 | 1 | L679I | 1 | 679 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | PTK2B | 22 | 1 | H485N | 1 | 485 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | PTK2B | 22 | 1 | K488S | 0 | 488 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | PTK2B | 22 | 1 | I493I | 0 | 493 | agreement of all settings; already WT |  |  |  |
| V617F | previous | JH2 | PTK2B | 22 | 1 | I493F | 0 | 493 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | PTK2B | 22 | 1 | I501F | 0 | 501 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | PTK2B | 22 | 1 | F627R | 0 | 627 | agreement of all settings |  |  |  |
| G571R | study | JH2 | ZAP70 | 27 | 15 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | ZAP70 | 27 | 15 | V366I | 1 | 366 | agreement of all settings |  |  |  |
| L805I | study | JH2 | ZAP70 | 27 | 15 | L600I | 1 | 593 | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | ZAP70 | 27 | 15 | Y397N | 0 | 397 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | ZAP70 | 27 | 15 | R400S | 0 | 400 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | ZAP70 | 27 | 15 | Q406I | 0 | 406 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | ZAP70 | 27 | 15 | Q406F | 0 | 406 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | ZAP70 | 27 | 15 | V413F | 1 | 413 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | ZAP70 | 27 | 15 | K541R | 0 | 541 | agreement of all settings |  |  |  |
| G571R | study | JH2 | EPHA5 | 31 | 18 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | EPHA5 | 31 | 18 | V704I | 1 | 704 | agreement of all settings |  |  |  |
| L805I | study | JH2 | EPHA5 | 31 | 18 | P939I | 0 | 932 | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | EPHA5 | 31 | 18 | N735N | 0 | 735 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | EPHA5 | 31 | 18 | H738S | 0 | 738 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | EPHA5 | 31 | 18 | T744I | 0 | 744 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | EPHA5 | 31 | 18 | T744F | 0 | 744 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | EPHA5 | 31 | 18 | V752F | 1 | 752 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | EPHA5 | 31 | 18 | W880R | 0 | 880 | agreement of all settings |  |  |  |
| G571R | study | JH2 | BTK | 36 | 20 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | BTK | 36 | 20 | V427I | 1 | 427 | agreement of all settings |  |  |  |
| L805I | study | JH2 | BTK | 36 | 20 | L652I | 1 | 651 | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | BTK | 36 | 20 | K456N | 0 | 456 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | BTK | 36 | 20 | Q459S | 0 | 459 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | BTK | 36 | 20 | T465I | 0 | 465 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | BTK | 36 | 20 | T465F | 0 | 465 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | BTK | 36 | 20 | I473F | 0 | 473 | agreement of all settings | I473N: VUS, VCV000835039. Codon 473 precedes the BTK gatekeeper. |  |  |
| S755R | previous | JH2 | BTK | 36 | 20 | E599R | 0 | 599 | agreement of all settings |  |  |  |
| G571R | study | JH2 | IGF1R | 40 | 19 | K1023R | 0 | 1023 | agreement of all settings |  |  |  |
| V578I | study | JH2 | IGF1R | 40 | 19 | V1030I | 1 | 1030 | agreement of all settings |  |  |  |
| L805I | study | JH2 | IGF1R | 40 | 19 | I1266I | 0 | 1266 | agreement of all settings; already WT |  |  |  |
| H608N | previous | JH2 | IGF1R | 40 | 19 | H1061N | 1 | 1061 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | IGF1R | 40 | 19 | R1064S | 0 | 1064 | agreement of all settings |  |  | R1064* Sugi (ClinVar index) |
| V617I | previous | JH2 | IGF1R | 40 | 19 | S1070I | 0 | 1070 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | IGF1R | 40 | 19 | S1070F | 0 | 1070 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | IGF1R | 40 | 19 | I1078F | 0 | 1078 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | IGF1R | 40 | 19 | Q1214R | 0 | 1214 | agreement of all settings |  |  |  |
| G571R | study | JH2 | EPHA7 | 41 | 16 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | EPHA7 | 41 | 16 | V662I | 1 | 662 | agreement of all settings |  |  |  |
| L805I | study | JH2 | EPHA7 | 41 | 16 | P897I | 0 | 897,890 | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | EPHA7 | 41 | 16 | N693N | 0 | 693 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | EPHA7 | 41 | 16 | H696S | 0 | 696 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | EPHA7 | 41 | 16 | T702I | 0 | 702 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | EPHA7 | 41 | 16 | T702F | 0 | 702 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | EPHA7 | 41 | 16 | V710F | 1 | 710 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | EPHA7 | 41 | 16 | W838R | 0 | 838 | agreement of all settings |  |  |  |
| G571R | study | JH2 | FES | 44 | 2 |  |  | 578,gap,587 | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | FES | 44 | 2 | V587I | 1 | 585,587,594 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | FES | 44 | 2 | L814I | 1 | 814 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | FES | 44 | 2 | N618N | 0 | 618 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | FES | 44 | 2 | R621S | 0 | 621 | agreement of all settings |  |  | R621H Sugi (ClinVar index) |
| V617I | previous | JH2 | FES | 44 | 2 | T627I | 0 | 627 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | FES | 44 | 2 | T627F | 0 | 627 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | FES | 44 | 2 | V635F | 1 | 635 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | FES | 44 | 2 | P762R | 0 | 762 | agreement of all settings |  |  |  |
| G571R | study | JH2 | TXK | 45 | 5 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | TXK | 45 | 5 | V296I | 1 | 296 | agreement of all settings |  |  |  |
| L805I | study | JH2 | TXK | 45 | 5 | V520I | 0 | 520 | agreement of all settings |  |  | V520D Sugi (ClinVar index) |
| H608N | previous | JH2 | TXK | 45 | 5 | K325N | 0 | 325 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | TXK | 45 | 5 | Q328S | 0 | 328 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | TXK | 45 | 5 | I334I | 0 | 334 | agreement of all settings; already WT |  |  |  |
| V617F | previous | JH2 | TXK | 45 | 5 | I334F | 0 | 334 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | TXK | 45 | 5 | V342F | 1 | 342 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | TXK | 45 | 5 | E468R | 0 | 468 | agreement of all settings |  |  |  |
| G571R | study | JH2 | EPHB1 | 47 | 12 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | EPHB1 | 47 | 12 | V648I | 1 | 648 | agreement of all settings |  |  |  |
| L805I | study | JH2 | EPHB1 | 47 | 12 | L878I | 1 | 878 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | EPHB1 | 47 | 12 | N679N | 0 | 679 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | EPHB1 | 47 | 12 | R682S | 0 | 682 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | EPHB1 | 47 | 12 | T688I | 0 | 688 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | EPHB1 | 47 | 12 | T688F | 0 | 688 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | EPHB1 | 47 | 12 | I696F | 0 | 696 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | EPHB1 | 47 | 12 | W826R | 0 | 826 | agreement of all settings |  |  |  |
| G571R | study | JH2 | ROS1 | 51 | 11 | G1971R | 1 | 1971 | agreement of all settings |  |  |  |
| V578I | study | JH2 | ROS1 | 51 | 11 | V1977I | 1 | 1977 | agreement of all settings |  |  | V1977A CanProVar |
| L805I | study | JH2 | ROS1 | 51 | 11 | L2215I | 1 | 2214,gap | sensitive: do not treat as established |  |  |  |
| H608N | previous | JH2 | ROS1 | 51 | 11 | N2008N | 0 | 2008 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | ROS1 | 51 | 11 | K2011S | 0 | 2011 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | ROS1 | 51 | 11 | L2017I | 0 | 2017 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | ROS1 | 51 | 11 | L2017F | 0 | 2017 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | ROS1 | 51 | 11 | I2025F | 0 | 2025 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | ROS1 | 51 | 11 | P2163R | 0 | 2163 | agreement of all settings |  |  |  |
| G571R | study | JH2 | FER | 53 | 8 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | FER | 53 | 8 | V588I | 1 | 588 | agreement of all settings |  |  |  |
| L805I | study | JH2 | FER | 53 | 8 | L814I | 1 | 814 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | FER | 53 | 8 | N619N | 0 | 619 | agreement of all settings; already WT |  |  |  |
| L611S | previous | JH2 | FER | 53 | 8 | K622S | 0 | 622 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | FER | 53 | 8 | T628I | 0 | 628 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | FER | 53 | 8 | T628F | 0 | 628 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | FER | 53 | 8 | I636F | 0 | 636 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | FER | 53 | 8 | P762R | 0 | 762 | agreement of all settings |  |  |  |
| G571R | study | JH2 | TEC | 57 | 9 |  |  | gap | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | TEC | 57 | 9 | V395I | 1 | 391,395 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | TEC | 57 | 9 | I619I | 0 | 619 | agreement of all settings; already WT |  |  | I619M Sugi (ClinVar index) |
| H608N | previous | JH2 | TEC | 57 | 9 | K424N | 0 | 424 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | TEC | 57 | 9 | Q427S | 0 | 427 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | TEC | 57 | 9 | T433I | 0 | 433 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | TEC | 57 | 9 | T433F | 0 | 433 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | TEC | 57 | 9 | V441F | 1 | 441 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | TEC | 57 | 9 | E567R | 0 | 567 | agreement of all settings |  |  |  |
| G571R | study | JH2 | EPHA1 | 63 | 14 |  |  | 647 | gap/outside local aligned core |  |  |  |
| V578I | study | JH2 | EPHA1 | 63 | 14 | V653I | 1 | 654 | sensitive: do not treat as established |  |  |  |
| L805I | study | JH2 | EPHA1 | 63 | 14 | L880I | 1 | 880 | agreement of all settings |  |  |  |
| H608N | previous | JH2 | EPHA1 | 63 | 14 | H684N | 1 | 684 | agreement of all settings |  |  |  |
| L611S | previous | JH2 | EPHA1 | 63 | 14 | H687S | 0 | 687 | agreement of all settings |  |  |  |
| V617I | previous | JH2 | EPHA1 | 63 | 14 | T693I | 0 | 693 | agreement of all settings |  |  |  |
| V617F | previous | JH2 | EPHA1 | 63 | 14 | T693F | 0 | 693 | agreement of all settings |  |  |  |
| V625F | previous | JH2 | EPHA1 | 63 | 14 | I701F | 0 | 701 | agreement of all settings |  |  |  |
| S755R | previous | JH2 | EPHA1 | 63 | 14 | G828R | 0 | 828 | agreement of all settings |  |  |  |

</details>

<details>
<summary>curated_evidence.tsv — 21 rows</summary>

| JAK2_input | gene | observed_allele | alignment_relationship | evidence_type | finding | source_URLs |
| --- | --- | --- | --- | --- | --- | --- |
| V578I | FGFR3 | V505I | same substitution | functional experiment; germline ClinVar | An MCF10A proliferation assay failed to validate the predicted gain of function. The ClinVar condition record has conflicting germline classifications. | https://www.nature.com/articles/s41588-025-02482-x https://www.ncbi.nlm.nih.gov/clinvar/RCV001726365/ https://www.ncbi.nlm.nih.gov/clinvar/variation/719200/ |
| V578I | EGFR | V742I | same substitution | germline ClinVar | Conflicting germline submissions (VUS and likely benign). No somatic oncogenicity submission in the cited record. | https://www.ncbi.nlm.nih.gov/clinvar/variation/134026/ |
| V578I | NTRK1 | V541L | different endpoint | ClinVar index | Sugi indexes a germline VUS at the same codon for Val-to-Leu. It is not Val-to-Ile. | https://sugi.bio/variant/ntrk1-p-val541leu |
| G571R | RET | G748D | different endpoint | ClinVar index | Hirschsprung disease index lists Gly-to-Asp as uncertain significance, rs1314127008. JH2 beta2-beta3 loop site is a sequence projection. | https://clinvarminer.genetics.utah.edu/variants-by-mondo-condition/18309/gene/RET/uncertain%20significance |
| L611S | FGFR1 | N546S | projected endpoint, different starting residue | tumor observation | Reported in a pediatric spinal glioblastoma together with FGFR1 K656E. This observation alone cannot isolate the effect. | https://pmc.ncbi.nlm.nih.gov/articles/PMC6989446/ |
| L611S | FGFR2 | N549S | projected endpoint, different starting residue | tumor observation and experimental activation | JCGA lists this somatic allele as COSV60645338; CKB traces increased transforming activity and growth factor independence to experimental studies. p.N550S is the same genomic allele on an alternative transcript. | https://www.jcga-scc.jp/en/gene/FGFR2 https://ckb.genomenon.com/geneVariant/show?geneVariantId=43162 https://ckb.genomenon.com/geneVariant/show?geneVariantId=9524 https://pubmed.ncbi.nlm.nih.gov/34272467/ https://pubmed.ncbi.nlm.nih.gov/41361008/ |
| L611S | FGFR3 | N540S | projected endpoint, different starting residue | germline ClinVar and functional experiment | Pathogenic/likely pathogenic in ClinVar; reported in hypochondroplasia families. Experimentally activating, with weaker activation than N540K in the cited assay. | https://www.ncbi.nlm.nih.gov/clinvar/variation/16349/ https://www.ncbi.nlm.nih.gov/clinvar/RCV006713126.1/ https://www.oncotarget.com/article/8132/text/ |
| L611S | FGFR4 | N535K | different endpoint and starting residue | tumor database | JCGA lists a somatic Lys change at the same site. No quantitative isolated Ser result verified here. | https://www.jcga-scc.jp/en/gene/FGFR4 |
| L611S | EGFR | R776S | projected endpoint, different starting residue | tumor observation | Table 1 reports G719A+R776S. Clinical observation of compound mutations; do not attribute a single-mutant phenotype. | https://doi.org/10.1371/journal.pone.0307161.t001 |
| L611S | EGFR | R776H | different endpoint and starting residue | mechanistic experiment; ClinVar | Dimer-dependent activation; mutants preferentially occupied the acceptor position. Germline classifications conflict. | https://pmc.ncbi.nlm.nih.gov/articles/PMC5937138/ https://www.ncbi.nlm.nih.gov/clinvar/variation/126515/ |
| L611S | NTRK1 | R574S | projected endpoint, different starting residue | ClinVar index | VUS in a ClinVar-derived index; distinct from the differently numbered alternative NTRK1 alleles. | https://sugi.bio/variant/ntrk1-p-arg574ser https://www.ncbi.nlm.nih.gov/clinvar/variation/1037825/ |
| R938Q | RET | R813Q | same substitution | clinical observation, functional experiment and CKB | Reduced RET signaling, migration and colony formation versus wild type in cell assays. Reported in Hirschsprung disease. The cited MEN2 ClinVar record is VUS. JAK2 R938Q was inherited in cis with S755R. | https://pubmed.ncbi.nlm.nih.gov/22837065/ https://pubmed.ncbi.nlm.nih.gov/22729463/ https://ckb.genomenon.com/geneVariant/show?geneVariantId=25584 https://www.ncbi.nlm.nih.gov/clinvar/RCV000796744/ https://pubmed.ncbi.nlm.nih.gov/24398328/ |
| R938Q | FGFR1 | R570Q | same substitution | ClinVar index and gnomAD index | Indexed as VUS (VCV2580728); reported rare in gnomAD v4.1, not a functional assay. | https://sugi.bio/variant/fgfr1-p-arg570gln https://www.ncbi.nlm.nih.gov/clinvar/variation/2580728/ |
| R938Q | FGFR3 | R564Q | same substitution | ClinVar index | Single-submitter VUS indexed by Sugi. | https://sugi.bio/variant/gene/FGFR3 |
| R938Q | ABL1 | L324Q | projected endpoint, different starting residue | patient observation | A small BCR::ABL1-mutant clone was detected in a chronic-phase CML patient before imatinib, without an isolated biochemical result inferred. | https://haematologica.org/article/view/4738 |
| V617I | ABL1 | T306I | projected endpoint, different starting residue | doctoral thesis | BCR::ABL1 T306I reported in patient 29. Thesis-level evidence only. | https://www.db-thueringen.de/servlets/MCRFileNodeServlet/dbt_derivate_00067185/Dissertation_CarstenLipp.pdf |
| V617F / V617I | NTRK3 | G608S | different endpoint and starting residue | tumor observation and experiment | Colorectal cancer mutant retained the ability to induce apoptosis when transfected into RKO cells. No phenylalanine result inferred. | https://doi.org/10.1371/journal.pgen.1003552 |
| H608N | EGFR | H773N | same substitution | germline ClinVar | Single-submitter uncertain significance. | https://www.ncbi.nlm.nih.gov/clinvar/variation/4247349/ |
| E846D | EGFR | E709D | same substitution but uncertain domain-edge alignment | ClinVar index | c.2127A>C indexed as germline VUS. Different allele from E709_T710delinsD. | https://sugi.bio/variant/egfr-p-glu709asp https://www.ncbi.nlm.nih.gov/clinvar/variation/1393019/ |
| V625F | BTK | I473N | different starting residue and endpoint | germline ClinVar | VUS, VCV000835039. Codon 473 precedes the BTK gatekeeper. | https://www.ncbi.nlm.nih.gov/clinvar/variation/835039/ |
| V625F | EGFR | I789L / I789V | different starting residue and endpoint | germline ClinVar | Anchored site lies immediately before gatekeeper T790. ClinVar records for Leu and Val. Do not count T790M. | https://www.ncbi.nlm.nih.gov/clinvar/variation/1380650/ https://www.ncbi.nlm.nih.gov/clinvar/variation/3224656/ |

</details>

<details>
<summary>database_site_hits.tsv — 136 rows</summary>

| target_gene | observed_variant | resource | source_URL | example_record | relationship_to_JAK2 |
| --- | --- | --- | --- | --- | --- |
| ABL1 | E153Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | ABL1 p.Glu153Gln Uncertain significance Single submitter | C427R same site |
| ABL1 | P441= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | p.Pro441= Single submitter | S755R same site |
| ABL1 | P480= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | p.Pro480= Multiple submitters | V1110E same site |
| ABL1 | R152H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | ABL1 p.Arg152His Uncertain significance Single submitter | R426* same site |
| ABL1 | R239C | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | ABL1 p.Arg239Cys Uncertain significance Single submitter | E846D same site |
| ABL1 | R239H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | ABL1 p.Arg239His Uncertain significance Single submitter | E846D same site |
| CSK | M192T | Sugi (ClinVar index) | https://sugi.bio/variant/gene/CSK | CSK p.Met192Thr Uncertain significance Single submitter | E846D same site |
| EGFR | A955T | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | EGFR p.Ala955Thr Uncertain significance Multiple submitters | V1110E same site |
| EGFR | D916= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Asp916= Multiple submitters lung cancer | S755R same site |
| EGFR | D916N | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Asp916Asn Multiple submitters EGFR-related lung cancer | S755R same site |
| EGFR | E709A | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | chr7:55241678 \| A \| C \| 18 / 28 \| p.E709A \| c.2126A>C \| COSV51772956 \| Tier1 \| 2 / 355 | E846D same site |
| EGFR | E709D | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | EGFR p.Glu709Asp Uncertain significance Multiple submitters | E846D projected allele |
| EGFR | E709G | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | chr7:55241678 \| A \| G \| 18 / 28 \| p.E709G \| c.2126A>G \| COSV51765252 \| Tier2 \| 3 / 355 | E846D same site |
| EGFR | E709K | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | chr7:55241677 \| G \| A \| 18 / 28 \| p.E709K \| c.2125G>A \| COSV51767260 \| Tier1 \| 4 / 355 | E846D same site |
| EGFR | E709V | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | chr7:55241678 \| A \| T \| 18 / 28 \| p.E709V \| c.2126A>T \| COSV51766584 \| Tier2 \| 1 / 355 | E846D same site |
| EGFR | H773= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.His773= Multiple submitters hereditary neoplastic syndrome | H608N same site |
| EGFR | H773L | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | chr7:55249020 \| A \| T \| 20 / 28 \| p.H773L \| c.2318A>T \| COSV51792805 \| Tier1 \| 1 / 355 | H608N same site |
| EGFR | L730R | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | EGFR p.Leu730Arg Conflicting Single submitter | R867Q same site |
| EGFR | L782= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Leu782= Multiple submitters lung cancer | V617I same site; V617F same site |
| EGFR | L799= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Leu799= Single submitter lung cancer | R938Q same site |
| EGFR | R776= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Arg776= Multiple submitters EGFR-related lung cancer | L611S same site |
| EGFR | R776C | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | EGFR p.Arg776Cys Uncertain significance Multiple submitters | L611S same site |
| EGFR | R776H | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | chr7:55249029 \| G \| A \| 20 / 28 \| p.R776H \| c.2327G>A \| COSV51780730 \| Tier2 \| 1 / 355 | L611S same site |
| EGFR | R776H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | EGFR p.Arg776His Conflicting Single submitter | L611S same site |
| EGFR | V742= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Val742= Multiple submitters hereditary neoplastic syndrome | V578I same site |
| EGFR | V742I | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | p.Val742Ile Single submitter diffuse midline glioma, H3 K27-altered ⚠ | V578I projected allele |
| FES | R621H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FES | FES p.Arg621His Uncertain significance Single submitter | L611S same site |
| FGFR1 | D503= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Asp503= Single submitter Pfeiffer syndrome | G571R same site |
| FGFR1 | D503E | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Asp503Glu Uncertain significance Single submitter | G571R same site |
| FGFR1 | G499R | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Gly499Arg Uncertain significance Multiple submitters | R867Q same site |
| FGFR1 | I560= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Ile560= Single submitter Pfeiffer syndrome | V625F same site |
| FGFR1 | L696= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Leu696= Single submitter Pfeiffer syndrome | I1065T same site |
| FGFR1 | L754= | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR1/significance/any |  NM_023110. 3 (FGFR1) : c. 2262G>A (p. Leu754=) rs56341011 0.00711 | L805I same site |
| FGFR1 | L754= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Leu754= Multiple submitters osteoglophonic dysplasia | L805I same site |
| FGFR1 | N543D | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Asn543Asp Uncertain significance Single submitter | H608N same site |
| FGFR1 | N546K | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Asn546Lys Multiple submitters encephalocraniocutaneous lipomatosis | L611S same site |
| FGFR1 | P702= | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR1/significance/any |  NM_023110. 3 (FGFR1) : c. 2106C>T (p. Pro702=) rs777061347 0.00003 | S755R same site |
| FGFR1 | P702= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Pro702= Multiple submitters hypogonadotropic hypogonadism 2 with or without anosmia | S755R same site |
| FGFR1 | R475Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg475Gln Uncertain significance Multiple submitters | E846D same site |
| FGFR1 | R475W | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg475Trp Uncertain significance Multiple submitters | E846D same site |
| FGFR1 | R507C | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg507Cys Uncertain significance Single submitter | T875N same site |
| FGFR1 | R507H | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR1/significance/any |  NM_023110. 3 (FGFR1) : c. 1520G>A (p. Arg507His) rs369356672 0.00007 | T875N same site |
| FGFR1 | R507H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg507His Conflicting Single submitter | T875N same site |
| FGFR1 | R507L | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg507Leu Uncertain significance Multiple submitters | T875N same site |
| FGFR1 | R570= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | p.Arg570= Single submitter Jackson-Weiss syndrome | R938Q same site |
| FGFR1 | R570Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg570Gln Uncertain significance Single submitter | R938Q projected allele |
| FGFR1 | R570W | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | FGFR1 p.Arg570Trp Uncertain significance Multiple submitters | R938Q same site |
| FGFR2 | N546D | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 172 \| cs40009 \| N546D \| 1 \| PF07714 PF00069 \| Gastric Cancer \| \| COSMIC \| | H608N same site |
| FGFR2 | N546K | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 171 \| cs12323 \| N546K \| 0 \| PF07714 PF00069 \| Head and Neck Cancer \| 25252913 \| COSMIC \| | H608N same site |
| FGFR2 | N546S | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 173 \| cs76992 \| N546S \| 1 \| PF07714 PF00069 \| Intestines Cancer \| \| COSMIC \| | H608N same site |
| FGFR2 | N549H | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 180 \| cs52069 \| N549H \| 1 \| PF07714 PF00069 \| Uterine Cancer \| 22383975†www.ncbi.nlm.nih.gov \| COSMIC \| | L611S same site |
| FGFR2 | N549H | JCGA | https://www.jcga-scc.jp/en/gene/FGFR2 | chr10:123258036 \| T \| G \| 12 / 18 \| p.N549H \| c.1645A>C \| COSV60640393 \| Tier1 \| 2 / 86 | L611S same site |
| FGFR2 | N549K | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 181 \| cs27634 \| N549K \| 0 \| PF07714 PF00069 \| Breast Cancer \| \| COSMIC \| | L611S same site |
| FGFR2 | N549K | JCGA | https://www.jcga-scc.jp/en/gene/FGFR2 | chr10:123258034 \| A \| T \| 12 / 18 \| p.N549K \| c.1647T>A \| COSV60639738 \| Tier1 \| 1 / 86 | L611S same site |
| FGFR2 | N549S | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 182 \| cs36071 \| N549S \| 1 \| PF07714 PF00069 \| Liver Cancer \| \| COSMIC \| | L611S projected allele |
| FGFR2 | N549S | JCGA | https://www.jcga-scc.jp/en/gene/FGFR2 | chr10:123258035 \| T \| C \| 12 / 18 \| p.N549S \| c.1646A>G \| COSV60645338 \| Tier1 \| 1 / 86 | L611S projected allele |
| FGFR3 | A499= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Ala499= Single submitter | T875N same site |
| FGFR3 | A499P | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Ala499Pro Uncertain significance Single submitter | T875N same site |
| FGFR3 | N537= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Asn537= Single submitter | H608N same site |
| FGFR3 | N540= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Asn540= Multiple submitters | L611S same site |
| FGFR3 | N540D | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Asn540Asp Multiple submitters camptodactyly-tall stature-scoliosis-hearing loss syndrome | L611S same site |
| FGFR3 | N540H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Asn540His Single submitter Short stature | L611S same site |
| FGFR3 | N540K | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Asn540Lys Multiple submitters FGFR3-related chondrodysplasia | L611S same site |
| FGFR3 | N540S | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Asn540Ser Pathogenic/Likely pathogenic Multiple submitters | L611S projected allele |
| FGFR3 | N540T | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Asn540Thr Multiple submitters FGFR3-related disorder | L611S same site |
| FGFR3 | P696= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Pro696= Multiple submitters | S755R same site |
| FGFR3 | P735= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Pro735= Multiple submitters | V1110E same site |
| FGFR3 | R498= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Arg498= Single submitter | G571R same site |
| FGFR3 | R498Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Arg498Gln Uncertain significance Single submitter | G571R same site |
| FGFR3 | R498W | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Arg498Trp Uncertain significance Multiple submitters | G571R same site |
| FGFR3 | R564Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Arg564Gln Uncertain significance Single submitter | R938Q projected allele |
| FGFR3 | R564W | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Arg564Trp Uncertain significance Single submitter | R938Q same site |
| FGFR3 | T546K | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | p.Thr546Lys Single submitter FGFR3-related chondrodysplasia | V617I same site; V617F same site |
| FGFR3 | V505I | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | FGFR3 p.Val505Ile Conflicting Single submitter | V578I projected allele |
| FGFR4 | N535K | JCGA | https://www.jcga-scc.jp/en/gene/FGFR4 | chr5:176522416 \| C \| A \| 12 / 18 \| p.N535K \| c.1605C>A \| COSV52801581 \| Tier1 \| 1 / 81 | L611S same site |
| FGFR4 | R464P | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR4 | FGFR4 p.Arg464Pro Uncertain significance Single submitter | E846D same site |
| FRK | R143G | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FRK | FRK p.Arg143Gly Uncertain significance Single submitter | R426* same site |
| FRK | T297S | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FRK | FRK p.Thr297Ser Uncertain significance Single submitter | V617I same site; V617F same site |
| IGF1R | R1064* | Sugi (ClinVar index) | https://sugi.bio/variant/gene/IGF1R | p.Arg1064Ter Single submitter | L611S same site |
| NTRK1 | D537E | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK1 | 91 cs26426 D537E 2PF00069†pfam.sanger.ac.uk PF07714†pfam.sanger.ac.uk Ovarian Cancer21720365†www.ncbi.nlm.nih.gov COSMIC†cancer.sanger.ac.ukSHC1, SHC2, PLCG1, GRB2, | T875N same site |
| NTRK1 | D537E | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Asp537Glu Uncertain significance Single submitter | T875N same site |
| NTRK1 | E528* | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | p.Glu528Ter Single submitter hereditary sensory and autonomic neuropathy type 4 | R867Q same site |
| NTRK1 | H571Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | p.His571Gln Single submitter hereditary sensory and autonomic neuropathy type 4 ⚠ | H608N same site |
| NTRK1 | P768H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Pro768His Uncertain significance Single submitter | V1110E same site |
| NTRK1 | P768L | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | p.Pro768Leu Multiple submitters hereditary sensory and autonomic neuropathy type 4 | V1110E same site |
| NTRK1 | P768S | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK1 | 136 \| cs17994 \| P768S \| -1 \| PF00069†pfam.sanger.ac.uk PF07714†pfam.sanger.ac.uk \| Uterine Cancer \| 23104009†www.ncbi.nlm.nih.gov \| COSMIC†cancer.sanger.ac.uk \| SHC1, SHC2, PLCG1, GRB2, | V1110E same site |
| NTRK1 | R507C | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK1 | 84 cs43779 R507C-3 Urinary Bladder Cancer COSMIC†cancer.sanger.ac.uk | E846D same site |
| NTRK1 | R507C | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Arg507Cys Uncertain significance Multiple submitters | E846D same site |
| NTRK1 | R574C | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Arg574Cys Uncertain significance Single submitter | L611S same site |
| NTRK1 | R574H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Arg574His Uncertain significance Multiple submitters | L611S same site |
| NTRK1 | R574S | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Arg574Ser Uncertain significance Single submitter | L611S projected allele |
| NTRK1 | V541L | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | NTRK1 p.Val541Leu Uncertain significance Multiple submitters | V578I same site |
| NTRK3 | G608C | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 172 \| cs76628 \| G608C \| -3 \| PF07714†pfam.sanger.ac.uk PF00069†pfam.sanger.ac.uk \| Lung Cancer \| \| COSMIC†cancer.sanger.ac.uk \| MAPK1 | V617I same site; V617F same site |
| NTRK3 | G608S | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 170 \| cs11530 \| G608S \| 0 \| PF07714†pfam.sanger.ac.uk PF00069†pfam.sanger.ac.uk \| Intestines Cancer \| 12738854†www.ncbi.nlm.nih.gov \| COSMIC†cancer.sanger.ac.uk \| MAPK1 | V617I same site; V617F same site |
| NTRK3 | H599Y | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 166 \| cs50987 \| H599Y \| 2 \| PF07714†pfam.sanger.ac.uk PF00069†pfam.sanger.ac.uk \| Pancreatic Cancer \| 16941478†www.ncbi.nlm.nih.gov \| COSMIC†cancer.sanger.ac.uk \| MAPK1 | H608N same site |
| NTRK3 | K602R | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 167 \| cs93242 \| K602R \| 2 \| PF07714†pfam.sanger.ac.uk PF00069†pfam.sanger.ac.uk \| Intestines Cancer \| 22895193†www.ncbi.nlm.nih.gov \| COSMIC†cancer.sanger.ac.uk \| MAPK1 | L611S same site |
| NTRK3 | K602T | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 168 \| cs34357 \| K602T \| -1 \| PF07714†pfam.sanger.ac.uk PF00069†pfam.sanger.ac.uk \| Skin Cancer(Melanoma) \| 22842228†www.ncbi.nlm.nih.gov \| COSMIC†cancer.sanger.ac.uk \| MAPK1 | L611S same site |
| NTRK3 | R535M | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 145 \| cs95025 \| R535M \| -1 \| \| Lung Cancer \| \| COSMIC†cancer.sanger.ac.uk \| | E846D same site |
| PTK7 | P1048L | Sugi (ClinVar index) | https://sugi.bio/variant/gene/PTK7 | PTK7 p.Pro1048Leu Uncertain significance Single submitter | V1110E same site |
| PTK7 | R860Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/PTK7 | PTK7 p.Arg860Gln Uncertain significance Single submitter | L611S same site |
| PTK7 | R866Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/PTK7 | PTK7 p.Arg866Gln Uncertain significance Single submitter | V617I same site; V617F same site |
| RET | A750G | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Ala750Gly Uncertain significance Multiple submitters | T875N same site |
| RET | A750V | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 183 \| cs64164 \| A750V \| 0 \| PF07714 PF00069 \| Ovarian Cancer \| \| COSMIC \| STAT3, SHC1, GRB10, RET, | T875N same site |
| RET | G748C | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 182 \| cs1409 \| G748C \| -3 \| PF07714 PF00069 \| Thyroid Carcinoma \| 10622534 \| COSMIC \| STAT3, SHC1, GRB10, RET, | G571R same site |
| RET | G748D | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Gly748Asp Uncertain significance Multiple submitters | G571R same site |
| RET | H786= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.His786= Multiple submitters hereditary neoplastic syndrome | H608N same site |
| RET | H786Y | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.His786Tyr Uncertain significance Multiple submitters | H608N same site |
| RET | I803= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.Ile803= Multiple submitters hereditary neoplastic syndrome | V625F same site |
| RET | K789E | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 196 \| cs37412 \| K789E \| 1 \| PF07714 PF00069 \| Intestines Cancer \| \| COSMIC \| STAT3, SHC1, GRB10, RET, | L611S same site |
| RET | K789E | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Lys789Glu Conflicting Single submitter | L611S same site |
| RET | L1005= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.Leu1005= Multiple submitters multiple endocrine neoplasia type 2 | L805I same site |
| RET | L947= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.Leu947= Multiple submitters hereditary neoplastic syndrome | I1065T same site |
| RET | P992L | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 276 \| cs89530 \| P992L \| -3 \| PF07714 PF00069 \| Liver Cancer \| \| COSMIC \| STAT3, SHC1, GRB10, RET, | V1110E same site |
| RET | R721Q | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 178 \| cs18851 \| R721Q \| 1 \| \| Gastric Cancer \| \| COSMIC \| | E846D same site |
| RET | R721Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Arg721Gln Uncertain significance Multiple submitters | E846D same site |
| RET | R721W | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 177 \| cs10517 \| R721W \| -3 \| \| Uterine Cancer \| \| COSMIC \| | E846D same site |
| RET | R813= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.Arg813= Multiple submitters hereditary neoplastic syndrome | R938Q same site |
| RET | R813G | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Arg813Gly Uncertain significance Multiple submitters | R938Q same site |
| RET | R813Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Arg813Gln Uncertain significance Multiple submitters | R938Q projected allele |
| RET | R813W | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | RET p.Arg813Trp Uncertain significance Multiple submitters | R938Q same site |
| RET | S795= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.Ser795= Multiple submitters multiple endocrine neoplasia type 2A | V617I same site; V617F same site |
| RET | T742= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | p.Thr742= Multiple submitters hereditary neoplastic syndrome | R867Q same site |
| ROS1 | V1977A | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=ROS1 | 75 \| rs145889490 \| V1977A \| Cluster,1000Genome | V578I same site |
| SYK | Q43= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/SYK | p.Gln43= Multiple submitters | C427R same site |
| SYK | R42H | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=SYK | 3 \| cs16557 \| R42H \| 0 \| PF00017†pfam.sanger.ac.uk \| Prostate Cancer \| \| COSMIC†cancer.sanger.ac.uk \| PTK2, STAT3, SHC1, PLCG2, | R426* same site |
| SYK | R434= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/SYK | p.Arg434= Multiple submitters | L611S same site |
| SYK | R434Q | Sugi (ClinVar index) | https://sugi.bio/variant/gene/SYK | SYK p.Arg434Gln Uncertain significance Single submitter | L611S same site |
| SYK | V447I | Sugi (ClinVar index) | https://sugi.bio/variant/gene/SYK | SYK p.Val447Ile Uncertain significance Single submitter | V625F same site |
| TEC | I619M | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TEC | TEC p.Ile619Met Uncertain significance Single submitter | L805I same site |
| TIE1 | K859N | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TIE1 | TIE1 p.Lys859Asn Uncertain significance Single submitter | R867Q same site |
| TNK2 | P148= | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TNK2 | p.Pro148= Single submitter | G571R same site |
| TNK2 | P148H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TNK2 | p.Pro148His Single submitter ⚠ | G571R same site |
| TNK2 | R191H | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TNK2 | TNK2 p.Arg191His Uncertain significance Single submitter | L611S same site |
| TNK2 | R191P | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TNK2 | TNK2 p.Arg191Pro Uncertain significance Multiple submitters | L611S same site |
| TNK2 | T152M | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TNK2 | p.Thr152Met Single submitter ⚠ | T875N same site |
| TXK | V520D | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TXK | TXK p.Val520Asp Uncertain significance Single submitter | L805I same site |

</details>

<details>
<summary>coverage.tsv — 119 rows</summary>

| gene | resource | reference | lines_retrieved | available_page_lines | matched_rows_before_dedup |
| --- | --- | --- | --- | --- | --- |
| TNK2 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/TNK2/significance/any | 0 | 0 | 0 |
| FRK | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FRK/significance/any | 0 | 0 | 0 |
| ABL1 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/ABL1/significance/any | 0 | 0 | 0 |
| NTRK1 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/NTRK1/significance/any | 0 | 0 | 0 |
| FGFR1 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR1/significance/any | 191 | 1137 | 3 |
| DDR2 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/DDR2/significance/any | 0 | 0 | 0 |
| NTRK3 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/NTRK3/significance/any | 0 | 0 | 0 |
| FGFR2 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR2/significance/any | 0 | 0 | 0 |
| NTRK2 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/NTRK2/significance/any | 0 | 0 | 0 |
| ERBB4 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/ERBB4/significance/any | 0 | 0 | 0 |
| PTK7 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/PTK7/significance/any | 0 | 0 | 0 |
| ABL2 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/ABL2/significance/any | 0 | 0 | 0 |
| SYK | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/SYK/significance/any | 0 | 0 | 0 |
| FGFR3 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR3/significance/any | 0 | 0 | 0 |
| RET | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/RET/significance/any | 0 | 0 | 0 |
| TIE1 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/TIE1/significance/any | 0 | 0 | 0 |
| EGFR | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/EGFR/significance/any | 0 | 0 | 0 |
| CSK | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/CSK/significance/any | 0 | 0 | 0 |
| FGFR4 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/FGFR4/significance/any | 0 | 0 | 0 |
| PTK2 | ClinVar Miner (index) | https://clinvarminer.genetics.utah.edu/variants-by-gene/PTK2/significance/any | 0 | 0 | 0 |
| TNK2 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TNK2 | 715 | 715 | 7 |
| FRK | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FRK | 115 | 115 | 4 |
| ABL1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL1 | 1369 | 1369 | 10 |
| NTRK1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK1 | 2208 | 2208 | 16 |
| FGFR1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR1 | 2022 | 2022 | 27 |
| DDR2 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/DDR2 | 0 | 0 | 0 |
| NTRK3 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK3 | 213 | 213 | 0 |
| FGFR2 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR2 | 0 | 0 | 0 |
| NTRK2 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/NTRK2 | 1180 | 1180 | 0 |
| ERBB4 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ERBB4 | 0 | 0 | 0 |
| PTK7 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/PTK7 | 267 | 267 | 6 |
| ABL2 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ABL2 | 262 | 262 | 0 |
| SYK | Sugi (ClinVar index) | https://sugi.bio/variant/gene/SYK | 222 | 222 | 6 |
| FGFR3 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR3 | 1679 | 1679 | 25 |
| RET | Sugi (ClinVar index) | https://sugi.bio/variant/gene/RET | 3138 | 3138 | 21 |
| TIE1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TIE1 | 373 | 373 | 2 |
| EGFR | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EGFR | 2985 | 2985 | 19 |
| CSK | Sugi (ClinVar index) | https://sugi.bio/variant/gene/CSK | 91 | 91 | 2 |
| FGFR4 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FGFR4 | 254 | 254 | 2 |
| PTK2 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/PTK2 | 247 | 247 | 0 |
| TNK2 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=TNK2 | 114 | 114 | 0 |
| FRK | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FRK | 0 | 0 | 0 |
| ABL1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=ABL1 | 0 | 0 | 0 |
| NTRK1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK1 | 226 | 237 | 3 |
| FGFR1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR1 | 0 | 0 | 0 |
| DDR2 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=DDR2 | 0 | 0 | 0 |
| NTRK3 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK3 | 315 | 315 | 7 |
| FGFR2 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR2 | 353 | 353 | 11 |
| NTRK2 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=NTRK2 | 75 | 75 | 0 |
| ERBB4 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=ERBB4 | 115 | 115 | 0 |
| PTK7 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=PTK7 | 0 | 0 | 0 |
| ABL2 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=ABL2 | 0 | 0 | 0 |
| SYK | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=SYK | 148 | 148 | 1 |
| FGFR3 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR3 | 0 | 0 | 0 |
| RET | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RET | 493 | 493 | 6 |
| TIE1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=TIE1 | 0 | 0 | 0 |
| EGFR | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=EGFR | 0 | 0 | 0 |
| CSK | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=CSK | 0 | 0 | 0 |
| FGFR4 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FGFR4 | 0 | 0 | 0 |
| PTK2 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=PTK2 | 0 | 0 | 0 |
| TNK2 | JCGA | https://www.jcga-scc.jp/en/gene/TNK2 | 89 | 89 | 0 |
| FRK | JCGA | https://www.jcga-scc.jp/en/gene/FRK | 0 | 0 | 0 |
| ABL1 | JCGA | https://www.jcga-scc.jp/en/gene/ABL1 | 87 | 87 | 0 |
| NTRK1 | JCGA | https://www.jcga-scc.jp/en/gene/NTRK1 | 92 | 92 | 0 |
| FGFR1 | JCGA | https://www.jcga-scc.jp/en/gene/FGFR1 | 93 | 93 | 0 |
| DDR2 | JCGA | https://www.jcga-scc.jp/en/gene/DDR2 | 99 | 99 | 0 |
| NTRK3 | JCGA | https://www.jcga-scc.jp/en/gene/NTRK3 | 93 | 93 | 0 |
| FGFR2 | JCGA | https://www.jcga-scc.jp/en/gene/FGFR2 | 106 | 106 | 4 |
| NTRK2 | JCGA | https://www.jcga-scc.jp/en/gene/NTRK2 | 93 | 93 | 0 |
| ERBB4 | JCGA | https://www.jcga-scc.jp/en/gene/ERBB4 | 100 | 100 | 0 |
| PTK7 | JCGA | https://www.jcga-scc.jp/en/gene/PTK7 | 0 | 0 | 0 |
| ABL2 | JCGA | https://www.jcga-scc.jp/en/gene/ABL2 | 85 | 85 | 0 |
| SYK | JCGA | https://www.jcga-scc.jp/en/gene/SYK | 85 | 85 | 0 |
| FGFR3 | JCGA | https://www.jcga-scc.jp/en/gene/FGFR3 | 101 | 101 | 0 |
| RET | JCGA | https://www.jcga-scc.jp/en/gene/RET | 99 | 99 | 0 |
| TIE1 | JCGA | https://www.jcga-scc.jp/en/gene/TIE1 | 0 | 0 | 0 |
| EGFR | JCGA | https://www.jcga-scc.jp/en/gene/EGFR | 147 | 147 | 6 |
| CSK | JCGA | https://www.jcga-scc.jp/en/gene/CSK | 0 | 0 | 0 |
| FGFR4 | JCGA | https://www.jcga-scc.jp/en/gene/FGFR4 | 100 | 100 | 1 |
| PTK2 | JCGA | https://www.jcga-scc.jp/en/gene/PTK2 | 0 | 0 | 0 |
| PTK2B | Sugi (ClinVar index) | https://sugi.bio/variant/gene/PTK2B | 0 | 0 | 0 |
| ZAP70 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ZAP70 | 0 | 0 | 0 |
| EPHA5 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EPHA5 | 0 | 0 | 0 |
| BTK | Sugi (ClinVar index) | https://sugi.bio/variant/gene/BTK | 0 | 0 | 0 |
| IGF1R | Sugi (ClinVar index) | https://sugi.bio/variant/gene/IGF1R | 1440 | 1440 | 1 |
| EPHA7 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EPHA7 | 226 | 226 | 0 |
| FES | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FES | 274 | 274 | 2 |
| TXK | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TXK | 159 | 159 | 2 |
| EPHB1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EPHB1 | 240 | 240 | 0 |
| ROS1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/ROS1 | 505 | 578 | 0 |
| FER | Sugi (ClinVar index) | https://sugi.bio/variant/gene/FER | 0 | 0 | 0 |
| TEC | Sugi (ClinVar index) | https://sugi.bio/variant/gene/TEC | 124 | 124 | 2 |
| EPHA1 | Sugi (ClinVar index) | https://sugi.bio/variant/gene/EPHA1 | 370 | 370 | 0 |
| PTK2B | JCGA | https://www.jcga-scc.jp/en/gene/PTK2B | 0 | 0 | 0 |
| ZAP70 | JCGA | https://www.jcga-scc.jp/en/gene/ZAP70 | 0 | 0 | 0 |
| EPHA5 | JCGA | https://www.jcga-scc.jp/en/gene/EPHA5 | 0 | 0 | 0 |
| BTK | JCGA | https://www.jcga-scc.jp/en/gene/BTK | 88 | 88 | 0 |
| IGF1R | JCGA | https://www.jcga-scc.jp/en/gene/IGF1R | 94 | 94 | 0 |
| EPHA7 | JCGA | https://www.jcga-scc.jp/en/gene/EPHA7 | 0 | 0 | 0 |
| FES | JCGA | https://www.jcga-scc.jp/en/gene/FES | 0 | 0 | 0 |
| TXK | JCGA | https://www.jcga-scc.jp/en/gene/TXK | 0 | 0 | 0 |
| EPHB1 | JCGA | https://www.jcga-scc.jp/en/gene/EPHB1 | 90 | 90 | 0 |
| ROS1 | JCGA | https://www.jcga-scc.jp/en/gene/ROS1 | 93 | 93 | 0 |
| FER | JCGA | https://www.jcga-scc.jp/en/gene/FER | 0 | 0 | 0 |
| TEC | JCGA | https://www.jcga-scc.jp/en/gene/TEC | 0 | 0 | 0 |
| EPHA1 | JCGA | https://www.jcga-scc.jp/en/gene/EPHA1 | 0 | 0 | 0 |
| PTK2B | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=PTK2B | 0 | 0 | 0 |
| ZAP70 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=ZAP70 | 0 | 0 | 0 |
| EPHA5 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=EPHA5 | 0 | 0 | 0 |
| BTK | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=BTK | 0 | 0 | 0 |
| IGF1R | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=IGF1R | 114 | 114 | 0 |
| EPHA7 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=EPHA7 | 0 | 0 | 0 |
| FES | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FES | 0 | 0 | 0 |
| TXK | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=TXK | 0 | 0 | 0 |
| EPHB1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=EPHB1 | 0 | 0 | 0 |
| ROS1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=ROS1 | 542 | 544 | 1 |
| FER | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=FER | 72 | 72 | 0 |
| TEC | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=TEC | 71 | 71 | 0 |
| EPHA1 | CanProVar | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=EPHA1 | 0 | 0 | 0 |

</details>

<details>
<summary>query_log.tsv — 742 rows</summary>

| gene | projection | search_type | query | candidate_text_matches |
| --- | --- | --- | --- | --- |
| TNK2 | I332T | cv | TNK2 "Ile332Thr" ClinVar "TNK2" | 0 |
| TNK2 | I332T | lit | "TNK2" "I332T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | P372E | cv | TNK2 "Pro372Glu" ClinVar "TNK2" | 0 |
| TNK2 | P372E | lit | "TNK2" "P372E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | E123D | cv | TNK2 "Glu123Asp" ClinVar "TNK2" | 0 |
| TNK2 | E123D | lit | "TNK2" "E123D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | E144Q | cv | TNK2 "Glu144Gln" ClinVar "TNK2" | 0 |
| TNK2 | E144Q | lit | "TNK2" "E144Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | T152N | cv | TNK2 "Thr152Asn" ClinVar "TNK2" | 0 |
| TNK2 | T152N | lit | "TNK2" "T152N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | L214Q | cv | TNK2 "Leu214Gln" ClinVar "TNK2" | 0 |
| TNK2 | L214Q | lit | "TNK2" "L214Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | P148R | cv | TNK2 "Pro148Arg" ClinVar "TNK2" | 0 |
| TNK2 | P148R | lit | "TNK2" "P148R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | V155I | cv | TNK2 "Val155Ile" ClinVar "TNK2" | 0 |
| TNK2 | V155I | lit | "TNK2" "V155I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | M393I | cv | TNK2 "Met393Ile" ClinVar "TNK2" | 0 |
| TNK2 | M393I | lit | "TNK2" "M393I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 3 |
| TNK2 | R191S | cv | TNK2 "Arg191Ser" ClinVar "TNK2" | 0 |
| TNK2 | R191S | lit | "TNK2" "R191S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | V196I | cv | TNK2 "Val196Ile" ClinVar "TNK2" | 0 |
| TNK2 | V196I | lit | "TNK2" "V196I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | V196F | cv | TNK2 "Val196Phe" ClinVar "TNK2" | 0 |
| TNK2 | V196F | lit | "TNK2" "V196F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | V204F | cv | TNK2 "Val204Phe" ClinVar "TNK2" | 0 |
| TNK2 | V204F | lit | "TNK2" "V204F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TNK2 | I332R | cv | TNK2 "Ile332Arg" ClinVar "TNK2" | 0 |
| TNK2 | I332R | lit | "TNK2" "I332R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | P474E | cv | FRK "Pro474Glu" ClinVar "FRK" | 0 |
| FRK | P474E | lit | "FRK" "P474E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | R231D | cv | FRK "Arg231Asp" ClinVar "FRK" | 0 |
| FRK | R231D | lit | "FRK" "R231D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | T256N | cv | FRK "Thr256Asn" ClinVar "FRK" | 0 |
| FRK | T256N | lit | "FRK" "T256N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | G436H | cv | FRK "Gly436His" ClinVar "FRK" | 0 |
| FRK | G436H | lit | "FRK" "G436H" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | V259I | cv | FRK "Val259Ile" ClinVar "FRK" | 0 |
| FRK | V259I | lit | "FRK" "V259I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | L487I | cv | FRK "Leu487Ile" ClinVar "FRK" | 0 |
| FRK | L487I | lit | "FRK" "L487I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | K288N | cv | FRK "Lys288Asn" ClinVar "FRK" | 0 |
| FRK | K288N | lit | "FRK" "K288N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | Q291S | cv | FRK "Gln291Ser" ClinVar "FRK" | 0 |
| FRK | Q291S | lit | "FRK" "Q291S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | T297I | cv | FRK "Thr297Ile" ClinVar "FRK" | 0 |
| FRK | T297I | lit | "FRK" "T297I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | T297F | cv | FRK "Thr297Phe" ClinVar "FRK" | 0 |
| FRK | T297F | lit | "FRK" "T297F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | I305F | cv | FRK "Ile305Phe" ClinVar "FRK" | 0 |
| FRK | I305F | lit | "FRK" "I305F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | S435R | cv | FRK "Ser435Arg" ClinVar "FRK" | 0 |
| FRK | S435R | lit | "FRK" "S435R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | R143* | cv | FRK "Arg143Ter" ClinVar "FRK" | 0 |
| FRK | R143* | lit | "FRK" "R143X" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FRK | E144R | cv | FRK "Glu144Arg" ClinVar "FRK" | 0 |
| FRK | E144R | lit | "FRK" "E144R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | P480E | cv | ABL1 "Pro480Glu" ClinVar "ABL1" | 0 |
| ABL1 | P480E | lit | "ABL1" "P480E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | R239D | cv | ABL1 "Arg239Asp" ClinVar "ABL1" | 0 |
| ABL1 | R239D | lit | "ABL1" "R239D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | Y264N | cv | ABL1 "Tyr264Asn" ClinVar "ABL1" | 0 |
| ABL1 | Y264N | lit | "ABL1" "Y264N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | L324Q | cv | ABL1 "Leu324Gln" ClinVar "ABL1" | 0 |
| ABL1 | L324Q | lit | "ABL1" "L324Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 10 |
| ABL1 | V268I | cv | ABL1 "Val268Ile" ClinVar "ABL1" | 0 |
| ABL1 | V268I | lit | "ABL1" "V268I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | F493I | cv | ABL1 "Phe493Ile" ClinVar "ABL1" | 0 |
| ABL1 | F493I | lit | "ABL1" "F493I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | Q300S | cv | ABL1 "Gln300Ser" ClinVar "ABL1" | 0 |
| ABL1 | Q300S | lit | "ABL1" "Q300S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | T306I | cv | ABL1 "Thr306Ile" ClinVar "ABL1" | 1 |
| ABL1 | T306I | lit | "ABL1" "T306I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 6 |
| ABL1 | T306F | cv | ABL1 "Thr306Phe" ClinVar "ABL1" | 0 |
| ABL1 | T306F | lit | "ABL1" "T306F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | I314F | cv | ABL1 "Ile314Phe" ClinVar "ABL1" | 0 |
| ABL1 | I314F | lit | "ABL1" "I314F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | P441R | cv | ABL1 "Pro441Arg" ClinVar "ABL1" | 0 |
| ABL1 | P441R | lit | "ABL1" "P441R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | R152* | cv | ABL1 "Arg152Ter" ClinVar "ABL1" | 0 |
| ABL1 | R152* | lit | "ABL1" "R152X" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL1 | E153R | cv | ABL1 "Glu153Arg" ClinVar "ABL1" | 0 |
| ABL1 | E153R | lit | "ABL1" "E153R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | P768E | cv | NTRK1 "Pro768Glu" ClinVar "NTRK1" | 0 |
| NTRK1 | P768E | lit | "NTRK1" "P768E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | R507D | cv | NTRK1 "Arg507Asp" ClinVar "NTRK1" | 0 |
| NTRK1 | R507D | lit | "NTRK1" "R507D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | E528Q | cv | NTRK1 "Glu528Gln" ClinVar "NTRK1" | 0 |
| NTRK1 | E528Q | lit | "NTRK1" "E528Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| NTRK1 | D537N | cv | NTRK1 "Asp537Asn" ClinVar "NTRK1" | 0 |
| NTRK1 | D537N | lit | "NTRK1" "D537N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | N598Q | cv | NTRK1 "Asn598Gln" ClinVar "NTRK1" | 0 |
| NTRK1 | N598Q | lit | "NTRK1" "N598Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | V541I | cv | NTRK1 "Val541Ile" ClinVar "NTRK1" | 0 |
| NTRK1 | V541I | lit | "NTRK1" "V541I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | L781I | cv | NTRK1 "Leu781Ile" ClinVar "NTRK1" | 0 |
| NTRK1 | L781I | lit | "NTRK1" "L781I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | H571N | cv | NTRK1 "His571Asn" ClinVar "NTRK1" | 0 |
| NTRK1 | H571N | lit | "NTRK1" "H571N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | R574S | cv | NTRK1 "Arg574Ser" ClinVar "NTRK1" | 0 |
| NTRK1 | R574S | lit | "NTRK1" "R574S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | T580I | cv | NTRK1 "Thr580Ile" ClinVar "NTRK1" | 0 |
| NTRK1 | T580I | lit | "NTRK1" "T580I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | T580F | cv | NTRK1 "Thr580Phe" ClinVar "NTRK1" | 0 |
| NTRK1 | T580F | lit | "NTRK1" "T580F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | V588F | cv | NTRK1 "Val588Phe" ClinVar "NTRK1" | 0 |
| NTRK1 | V588F | lit | "NTRK1" "V588F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK1 | Y729R | cv | NTRK1 "Tyr729Arg" ClinVar "NTRK1" | 0 |
| NTRK1 | Y729R | lit | "NTRK1" "Y729R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | L696T | cv | FGFR1 "Leu696Thr" ClinVar "FGFR1" | 0 |
| FGFR1 | L696T | lit | "FGFR1" "L696T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | P741E | cv | FGFR1 "Pro741Glu" ClinVar "FGFR1" | 0 |
| FGFR1 | P741E | lit | "FGFR1" "P741E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | R475D | cv | FGFR1 "Arg475Asp" ClinVar "FGFR1" | 0 |
| FGFR1 | R475D | lit | "FGFR1" "R475D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | G499Q | cv | FGFR1 "Gly499Gln" ClinVar "FGFR1" | 0 |
| FGFR1 | G499Q | lit | "FGFR1" "G499Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | R507N | cv | FGFR1 "Arg507Asn" ClinVar "FGFR1" | 0 |
| FGFR1 | R507N | lit | "FGFR1" "R507N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | R570Q | cv | FGFR1 "Arg570Gln" ClinVar "FGFR1" | 0 |
| FGFR1 | R570Q | lit | "FGFR1" "R570Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | D503R | cv | FGFR1 "Asp503Arg" ClinVar "FGFR1" | 0 |
| FGFR1 | D503R | lit | "FGFR1" "D503R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | V511I | cv | FGFR1 "Val511Ile" ClinVar "FGFR1" | 0 |
| FGFR1 | V511I | lit | "FGFR1" "V511I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | L754I | cv | FGFR1 "Leu754Ile" ClinVar "FGFR1" | 0 |
| FGFR1 | L754I | lit | "FGFR1" "L754I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | N546S | cv | FGFR1 "Asn546Ser" ClinVar "FGFR1" | 5 |
| FGFR1 | N546S | lit | "FGFR1" "N546S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 10 |
| FGFR1 | T552I | cv | FGFR1 "Thr552Ile" ClinVar "FGFR1" | 0 |
| FGFR1 | T552I | lit | "FGFR1" "T552I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | T552F | cv | FGFR1 "Thr552Phe" ClinVar "FGFR1" | 0 |
| FGFR1 | T552F | lit | "FGFR1" "T552F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | I560F | cv | FGFR1 "Ile560Phe" ClinVar "FGFR1" | 0 |
| FGFR1 | I560F | lit | "FGFR1" "I560F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR1 | P702R | cv | FGFR1 "Pro702Arg" ClinVar "FGFR1" | 0 |
| FGFR1 | P702R | lit | "FGFR1" "P702R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| DDR2 | T836E | cv | DDR2 "Thr836Glu" ClinVar "DDR2" | 0 |
| DDR2 | T836E | lit | "DDR2" "T836E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | R560D | cv | DDR2 "Arg560Asp" ClinVar "DDR2" | 0 |
| DDR2 | R560D | lit | "DDR2" "R560D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | E581Q | cv | DDR2 "Glu581Gln" ClinVar "DDR2" | 0 |
| DDR2 | E581Q | lit | "DDR2" "E581Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | Q601N | cv | DDR2 "Gln601Asn" ClinVar "DDR2" | 0 |
| DDR2 | Q601N | lit | "DDR2" "Q601N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | N663Q | cv | DDR2 "Asn663Gln" ClinVar "DDR2" | 0 |
| DDR2 | N663Q | lit | "DDR2" "N663Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | G575R | cv | DDR2 "Gly575Arg" ClinVar "DDR2" | 0 |
| DDR2 | G575R | lit | "DDR2" "G575R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | V605I | cv | DDR2 "Val605Ile" ClinVar "DDR2" | 0 |
| DDR2 | V605I | lit | "DDR2" "V605I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | H639S | cv | DDR2 "His639Ser" ClinVar "DDR2" | 0 |
| DDR2 | H639S | lit | "DDR2" "H639S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | I645F | cv | DDR2 "Ile645Phe" ClinVar "DDR2" | 0 |
| DDR2 | I645F | lit | "DDR2" "I645F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | I653F | cv | DDR2 "Ile653Phe" ClinVar "DDR2" | 0 |
| DDR2 | I653F | lit | "DDR2" "I653F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| DDR2 | S790R | cv | DDR2 "Ser790Arg" ClinVar "DDR2" | 0 |
| DDR2 | S790R | lit | "DDR2" "S790R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| NTRK3 | P811E | cv | NTRK3 "Pro811Glu" ClinVar "NTRK3" | 0 |
| NTRK3 | P811E | lit | "NTRK3" "P811E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | R535D | cv | NTRK3 "Arg535Asp" ClinVar "NTRK3" | 0 |
| NTRK3 | R535D | lit | "NTRK3" "R535D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | N559Q | cv | NTRK3 "Asn559Gln" ClinVar "NTRK3" | 0 |
| NTRK3 | N559Q | lit | "NTRK3" "N559Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | M567N | cv | NTRK3 "Met567Asn" ClinVar "NTRK3" | 0 |
| NTRK3 | M567N | lit | "NTRK3" "M567N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | N626Q | cv | NTRK3 "Asn626Gln" ClinVar "NTRK3" | 0 |
| NTRK3 | N626Q | lit | "NTRK3" "N626Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | Y558R | cv | NTRK3 "Tyr558Arg" ClinVar "NTRK3" | 0 |
| NTRK3 | Y558R | lit | "NTRK3" "Y558R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | V569I | cv | NTRK3 "Val569Ile" ClinVar "NTRK3" | 0 |
| NTRK3 | V569I | lit | "NTRK3" "V569I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| NTRK3 | L824I | cv | NTRK3 "Leu824Ile" ClinVar "NTRK3" | 0 |
| NTRK3 | L824I | lit | "NTRK3" "L824I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | H599N | cv | NTRK3 "His599Asn" ClinVar "NTRK3" | 0 |
| NTRK3 | H599N | lit | "NTRK3" "H599N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | K602S | cv | NTRK3 "Lys602Ser" ClinVar "NTRK3" | 0 |
| NTRK3 | K602S | lit | "NTRK3" "K602S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | G608I | cv | NTRK3 "Gly608Ile" ClinVar "NTRK3" | 0 |
| NTRK3 | G608I | lit | "NTRK3" "G608I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | G608F | cv | NTRK3 "Gly608Phe" ClinVar "NTRK3" | 0 |
| NTRK3 | G608F | lit | "NTRK3" "G608F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | V616F | cv | NTRK3 "Val616Phe" ClinVar "NTRK3" | 0 |
| NTRK3 | V616F | lit | "NTRK3" "V616F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK3 | F772R | cv | NTRK3 "Phe772Arg" ClinVar "NTRK3" | 0 |
| NTRK3 | F772R | lit | "NTRK3" "F772R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | L699T | cv | FGFR2 "Leu699Thr" ClinVar "FGFR2" | 0 |
| FGFR2 | L699T | lit | "FGFR2" "L699T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | P744E | cv | FGFR2 "Pro744Glu" ClinVar "FGFR2" | 0 |
| FGFR2 | P744E | lit | "FGFR2" "P744E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | R478D | cv | FGFR2 "Arg478Asp" ClinVar "FGFR2" | 0 |
| FGFR2 | R478D | lit | "FGFR2" "R478D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | E499Q | cv | FGFR2 "Glu499Gln" ClinVar "FGFR2" | 0 |
| FGFR2 | E499Q | lit | "FGFR2" "E499Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| FGFR2 | E510N | cv | FGFR2 "Glu510Asn" ClinVar "FGFR2" | 0 |
| FGFR2 | E510N | lit | "FGFR2" "E510N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | R573Q | cv | FGFR2 "Arg573Gln" ClinVar "FGFR2" | 0 |
| FGFR2 | R573Q | lit | "FGFR2" "R573Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| FGFR2 | D506R | cv | FGFR2 "Asp506Arg" ClinVar "FGFR2" | 0 |
| FGFR2 | D506R | lit | "FGFR2" "D506R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | V514I | cv | FGFR2 "Val514Ile" ClinVar "FGFR2" | 0 |
| FGFR2 | V514I | lit | "FGFR2" "V514I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | L757I | cv | FGFR2 "Leu757Ile" ClinVar "FGFR2" | 0 |
| FGFR2 | L757I | lit | "FGFR2" "L757I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | N549S | cv | FGFR2 "Asn549Ser" ClinVar "FGFR2" | 7 |
| FGFR2 | N549S | lit | "FGFR2" "N549S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | T555I | cv | FGFR2 "Thr555Ile" ClinVar "FGFR2" | 0 |
| FGFR2 | T555I | lit | "FGFR2" "T555I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | T555F | cv | FGFR2 "Thr555Phe" ClinVar "FGFR2" | 0 |
| FGFR2 | T555F | lit | "FGFR2" "T555F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | I563F | cv | FGFR2 "Ile563Phe" ClinVar "FGFR2" | 0 |
| FGFR2 | I563F | lit | "FGFR2" "I563F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR2 | P705R | cv | FGFR2 "Pro705Arg" ClinVar "FGFR2" | 0 |
| FGFR2 | P705R | lit | "FGFR2" "P705R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 2 |
| NTRK2 | S758T | cv | NTRK2 "Ser758Thr" ClinVar "NTRK2" | 0 |
| NTRK2 | S758T | lit | "NTRK2" "S758T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | P794E | cv | NTRK2 "Pro794Glu" ClinVar "NTRK2" | 0 |
| NTRK2 | P794E | lit | "NTRK2" "P794E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | K534D | cv | NTRK2 "Lys534Asp" ClinVar "NTRK2" | 0 |
| NTRK2 | K534D | lit | "NTRK2" "K534D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | I567N | cv | NTRK2 "Ile567Asn" ClinVar "NTRK2" | 0 |
| NTRK2 | I567N | lit | "NTRK2" "I567N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | N626Q | cv | NTRK2 "Asn626Gln" ClinVar "NTRK2" | 0 |
| NTRK2 | N626Q | lit | "NTRK2" "N626Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | Q756H | cv | NTRK2 "Gln756His" ClinVar "NTRK2" | 0 |
| NTRK2 | Q756H | lit | "NTRK2" "Q756H" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | N559R | cv | NTRK2 "Asn559Arg" ClinVar "NTRK2" | 0 |
| NTRK2 | N559R | lit | "NTRK2" "N559R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | V569I | cv | NTRK2 "Val569Ile" ClinVar "NTRK2" | 0 |
| NTRK2 | V569I | lit | "NTRK2" "V569I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | L810I | cv | NTRK2 "Leu810Ile" ClinVar "NTRK2" | 0 |
| NTRK2 | L810I | lit | "NTRK2" "L810I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | H599N | cv | NTRK2 "His599Asn" ClinVar "NTRK2" | 0 |
| NTRK2 | H599N | lit | "NTRK2" "H599N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | K602S | cv | NTRK2 "Lys602Ser" ClinVar "NTRK2" | 0 |
| NTRK2 | K602S | lit | "NTRK2" "K602S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | V608I | cv | NTRK2 "Val608Ile" ClinVar "NTRK2" | 0 |
| NTRK2 | V608I | lit | "NTRK2" "V608I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | V608F | cv | NTRK2 "Val608Phe" ClinVar "NTRK2" | 0 |
| NTRK2 | V608F | lit | "NTRK2" "V608F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | V616F | cv | NTRK2 "Val616Phe" ClinVar "NTRK2" | 0 |
| NTRK2 | V616F | lit | "NTRK2" "V616F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| NTRK2 | Y755R | cv | NTRK2 "Tyr755Arg" ClinVar "NTRK2" | 0 |
| NTRK2 | Y755R | lit | "NTRK2" "Y755R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | A961E | cv | ERBB4 "Ala961Glu" ClinVar "ERBB4" | 0 |
| ERBB4 | A961E | lit | "ERBB4" "A961E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | E715D | cv | ERBB4 "Glu715Asp" ClinVar "ERBB4" | 0 |
| ERBB4 | E715D | lit | "ERBB4" "E715D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | I736Q | cv | ERBB4 "Ile736Gln" ClinVar "ERBB4" | 0 |
| ERBB4 | I736Q | lit | "ERBB4" "I736Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | V744N | cv | ERBB4 "Val744Asn" ClinVar "ERBB4" | 0 |
| ERBB4 | V744N | lit | "ERBB4" "V744N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | L805Q | cv | ERBB4 "Leu805Gln" ClinVar "ERBB4" | 0 |
| ERBB4 | L805Q | lit | "ERBB4" "L805Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | V744R | cv | ERBB4 "Val744Arg" ClinVar "ERBB4" | 0 |
| ERBB4 | V744R | lit | "ERBB4" "V744R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | V748I | cv | ERBB4 "Val748Ile" ClinVar "ERBB4" | 0 |
| ERBB4 | V748I | lit | "ERBB4" "V748I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| ERBB4 | F974I | cv | ERBB4 "Phe974Ile" ClinVar "ERBB4" | 0 |
| ERBB4 | F974I | lit | "ERBB4" "F974I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | H779N | cv | ERBB4 "His779Asn" ClinVar "ERBB4" | 0 |
| ERBB4 | H779N | lit | "ERBB4" "H779N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | R782S | cv | ERBB4 "Arg782Ser" ClinVar "ERBB4" | 0 |
| ERBB4 | R782S | lit | "ERBB4" "R782S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | L788I | cv | ERBB4 "Leu788Ile" ClinVar "ERBB4" | 0 |
| ERBB4 | L788I | lit | "ERBB4" "L788I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| ERBB4 | L788F | cv | ERBB4 "Leu788Phe" ClinVar "ERBB4" | 0 |
| ERBB4 | L788F | lit | "ERBB4" "L788F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | V795F | cv | ERBB4 "Val795Phe" ClinVar "ERBB4" | 0 |
| ERBB4 | V795F | lit | "ERBB4" "V795F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ERBB4 | D922R | cv | ERBB4 "Asp922Arg" ClinVar "ERBB4" | 0 |
| ERBB4 | D922R | lit | "ERBB4" "D922R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | P1048E | cv | PTK7 "Pro1048Glu" ClinVar "PTK7" | 0 |
| PTK7 | P1048E | lit | "PTK7" "P1048E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | R793D | cv | PTK7 "Arg793Asp" ClinVar "PTK7" | 0 |
| PTK7 | R793D | lit | "PTK7" "R793D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | K814Q | cv | PTK7 "Lys814Gln" ClinVar "PTK7" | 0 |
| PTK7 | K814Q | lit | "PTK7" "K814Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | V822N | cv | PTK7 "Val822Asn" ClinVar "PTK7" | 0 |
| PTK7 | V822N | lit | "PTK7" "V822N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | K884Q | cv | PTK7 "Lys884Gln" ClinVar "PTK7" | 0 |
| PTK7 | K884Q | lit | "PTK7" "K884Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | V827I | cv | PTK7 "Val827Ile" ClinVar "PTK7" | 0 |
| PTK7 | V827I | lit | "PTK7" "V827I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | L1061I | cv | PTK7 "Leu1061Ile" ClinVar "PTK7" | 0 |
| PTK7 | L1061I | lit | "PTK7" "L1061I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | R860S | cv | PTK7 "Arg860Ser" ClinVar "PTK7" | 0 |
| PTK7 | R860S | lit | "PTK7" "R860S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | R866I | cv | PTK7 "Arg866Ile" ClinVar "PTK7" | 0 |
| PTK7 | R866I | lit | "PTK7" "R866I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | R866F | cv | PTK7 "Arg866Phe" ClinVar "PTK7" | 0 |
| PTK7 | R866F | lit | "PTK7" "R866F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | V874F | cv | PTK7 "Val874Phe" ClinVar "PTK7" | 0 |
| PTK7 | V874F | lit | "PTK7" "V874F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK7 | G1008R | cv | PTK7 "Gly1008Arg" ClinVar "PTK7" | 0 |
| PTK7 | G1008R | lit | "PTK7" "G1008R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | P526E | cv | ABL2 "Pro526Glu" ClinVar "ABL2" | 0 |
| ABL2 | P526E | lit | "ABL2" "P526E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | R285D | cv | ABL2 "Arg285Asp" ClinVar "ABL2" | 0 |
| ABL2 | R285D | lit | "ABL2" "R285D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | Y310N | cv | ABL2 "Tyr310Asn" ClinVar "ABL2" | 0 |
| ABL2 | Y310N | lit | "ABL2" "Y310N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | L370Q | cv | ABL2 "Leu370Gln" ClinVar "ABL2" | 0 |
| ABL2 | L370Q | lit | "ABL2" "L370Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | V314I | cv | ABL2 "Val314Ile" ClinVar "ABL2" | 0 |
| ABL2 | V314I | lit | "ABL2" "V314I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | F539I | cv | ABL2 "Phe539Ile" ClinVar "ABL2" | 0 |
| ABL2 | F539I | lit | "ABL2" "F539I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | Q346S | cv | ABL2 "Gln346Ser" ClinVar "ABL2" | 0 |
| ABL2 | Q346S | lit | "ABL2" "Q346S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | T352I | cv | ABL2 "Thr352Ile" ClinVar "ABL2" | 0 |
| ABL2 | T352I | lit | "ABL2" "T352I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | T352F | cv | ABL2 "Thr352Phe" ClinVar "ABL2" | 0 |
| ABL2 | T352F | lit | "ABL2" "T352F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | V360F | cv | ABL2 "Val360Phe" ClinVar "ABL2" | 0 |
| ABL2 | V360F | lit | "ABL2" "V360F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | P487R | cv | ABL2 "Pro487Arg" ClinVar "ABL2" | 0 |
| ABL2 | P487R | lit | "ABL2" "P487R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | R198* | cv | ABL2 "Arg198Ter" ClinVar "ABL2" | 0 |
| ABL2 | R198* | lit | "ABL2" "R198X" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ABL2 | E199R | cv | ABL2 "Glu199Arg" ClinVar "ABL2" | 0 |
| ABL2 | E199R | lit | "ABL2" "E199R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | K577T | cv | SYK "Lys577Thr" ClinVar "SYK" | 0 |
| SYK | K577T | lit | "SYK" "K577T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | V613E | cv | SYK "Val613Glu" ClinVar "SYK" | 0 |
| SYK | V613E | lit | "SYK" "V613E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | Y389Q | cv | SYK "Tyr389Gln" ClinVar "SYK" | 0 |
| SYK | Y389Q | lit | "SYK" "Y389Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | V395N | cv | SYK "Val395Asn" ClinVar "SYK" | 0 |
| SYK | V395N | lit | "SYK" "V395N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | N457Q | cv | SYK "Asn457Gln" ClinVar "SYK" | 0 |
| SYK | N457Q | lit | "SYK" "N457Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | G575H | cv | SYK "Gly575His" ClinVar "SYK" | 0 |
| SYK | G575H | lit | "SYK" "G575H" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | Y390R | cv | SYK "Tyr390Arg" ClinVar "SYK" | 0 |
| SYK | Y390R | lit | "SYK" "Y390R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | V399I | cv | SYK "Val399Ile" ClinVar "SYK" | 0 |
| SYK | V399I | lit | "SYK" "V399I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | L626I | cv | SYK "Leu626Ile" ClinVar "SYK" | 0 |
| SYK | L626I | lit | "SYK" "L626I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | Y431N | cv | SYK "Tyr431Asn" ClinVar "SYK" | 0 |
| SYK | Y431N | lit | "SYK" "Y431N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | R434S | cv | SYK "Arg434Ser" ClinVar "SYK" | 0 |
| SYK | R434S | lit | "SYK" "R434S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | E440I | cv | SYK "Glu440Ile" ClinVar "SYK" | 0 |
| SYK | E440I | lit | "SYK" "E440I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | E440F | cv | SYK "Glu440Phe" ClinVar "SYK" | 0 |
| SYK | E440F | lit | "SYK" "E440F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| SYK | V447F | cv | SYK "Val447Phe" ClinVar "SYK" | 0 |
| SYK | V447F | lit | "SYK" "V447F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | R42* | cv | SYK "Arg42Ter" ClinVar "SYK" | 0 |
| SYK | R42* | lit | "SYK" "R42X" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| SYK | Q43R | cv | SYK "Gln43Arg" ClinVar "SYK" | 0 |
| SYK | Q43R | lit | "SYK" "Q43R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | L690T | cv | FGFR3 "Leu690Thr" ClinVar "FGFR3" | 0 |
| FGFR3 | L690T | lit | "FGFR3" "L690T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | P735E | cv | FGFR3 "Pro735Glu" ClinVar "FGFR3" | 0 |
| FGFR3 | P735E | lit | "FGFR3" "P735E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | R469D | cv | FGFR3 "Arg469Asp" ClinVar "FGFR3" | 0 |
| FGFR3 | R469D | lit | "FGFR3" "R469D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | E490Q | cv | FGFR3 "Glu490Gln" ClinVar "FGFR3" | 0 |
| FGFR3 | E490Q | lit | "FGFR3" "E490Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | A499N | cv | FGFR3 "Ala499Asn" ClinVar "FGFR3" | 0 |
| FGFR3 | A499N | lit | "FGFR3" "A499N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | R564Q | cv | FGFR3 "Arg564Gln" ClinVar "FGFR3" | 0 |
| FGFR3 | R564Q | lit | "FGFR3" "R564Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | V505I | cv | FGFR3 "Val505Ile" ClinVar "FGFR3" | 0 |
| FGFR3 | V505I | lit | "FGFR3" "V505I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 7 |
| FGFR3 | L748I | cv | FGFR3 "Leu748Ile" ClinVar "FGFR3" | 0 |
| FGFR3 | L748I | lit | "FGFR3" "L748I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | N540S | cv | FGFR3 "Asn540Ser" ClinVar "FGFR3" | 18 |
| FGFR3 | N540S | lit | "FGFR3" "N540S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 16 |
| FGFR3 | T546I | cv | FGFR3 "Thr546Ile" ClinVar "FGFR3" | 0 |
| FGFR3 | T546I | lit | "FGFR3" "T546I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | T546F | cv | FGFR3 "Thr546Phe" ClinVar "FGFR3" | 0 |
| FGFR3 | T546F | lit | "FGFR3" "T546F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | L554F | cv | FGFR3 "Leu554Phe" ClinVar "FGFR3" | 2 |
| FGFR3 | L554F | lit | "FGFR3" "L554F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR3 | P696R | cv | FGFR3 "Pro696Arg" ClinVar "FGFR3" | 0 |
| FGFR3 | P696R | lit | "FGFR3" "P696R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | L947T | cv | RET "Leu947Thr" ClinVar "RET" | 0 |
| RET | L947T | lit | "RET" "L947T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| RET | P992E | cv | RET "Pro992Glu" ClinVar "RET" | 0 |
| RET | P992E | lit | "RET" "P992E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | R721D | cv | RET "Arg721Asp" ClinVar "RET" | 0 |
| RET | R721D | lit | "RET" "R721D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | T742Q | cv | RET "Thr742Gln" ClinVar "RET" | 0 |
| RET | T742Q | lit | "RET" "T742Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | A750N | cv | RET "Ala750Asn" ClinVar "RET" | 0 |
| RET | A750N | lit | "RET" "A750N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | R813Q | cv | RET "Arg813Gln" ClinVar "RET" | 0 |
| RET | R813Q | lit | "RET" "R813Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 15 |
| RET | G748R | cv | RET "Gly748Arg" ClinVar "RET" | 0 |
| RET | G748R | lit | "RET" "G748R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | V755I | cv | RET "Val755Ile" ClinVar "RET" | 0 |
| RET | V755I | lit | "RET" "V755I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | L1005I | cv | RET "Leu1005Ile" ClinVar "RET" | 0 |
| RET | L1005I | lit | "RET" "L1005I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | H786N | cv | RET "His786Asn" ClinVar "RET" | 0 |
| RET | H786N | lit | "RET" "H786N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | K789S | cv | RET "Lys789Ser" ClinVar "RET" | 0 |
| RET | K789S | lit | "RET" "K789S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | S795I | cv | RET "Ser795Ile" ClinVar "RET" | 0 |
| RET | S795I | lit | "RET" "S795I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 2 |
| RET | S795F | cv | RET "Ser795Phe" ClinVar "RET" | 0 |
| RET | S795F | lit | "RET" "S795F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| RET | I803F | cv | RET "Ile803Phe" ClinVar "RET" | 0 |
| RET | I803F | lit | "RET" "I803F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| RET | P953R | cv | RET "Pro953Arg" ClinVar "RET" | 0 |
| RET | P953R | lit | "RET" "P953R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| TIE1 | L1049T | cv | TIE1 "Leu1049Thr" ClinVar "TIE1" | 0 |
| TIE1 | L1049T | lit | "TIE1" "L1049T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | P1094E | cv | TIE1 "Pro1094Glu" ClinVar "TIE1" | 0 |
| TIE1 | P1094E | lit | "TIE1" "P1094E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | W836D | cv | TIE1 "Trp836Asp" ClinVar "TIE1" | 0 |
| TIE1 | W836D | lit | "TIE1" "W836D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | K859Q | cv | TIE1 "Lys859Gln" ClinVar "TIE1" | 0 |
| TIE1 | K859Q | lit | "TIE1" "K859Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | L926Q | cv | TIE1 "Leu926Gln" ClinVar "TIE1" | 0 |
| TIE1 | L926Q | lit | "TIE1" "L926Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | A867I | cv | TIE1 "Ala867Ile" ClinVar "TIE1" | 0 |
| TIE1 | A867I | lit | "TIE1" "A867I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | L1107I | cv | TIE1 "Leu1107Ile" ClinVar "TIE1" | 0 |
| TIE1 | L1107I | lit | "TIE1" "L1107I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | P898N | cv | TIE1 "Pro898Asn" ClinVar "TIE1" | 0 |
| TIE1 | P898N | lit | "TIE1" "P898N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | I901S | cv | TIE1 "Ile901Ser" ClinVar "TIE1" | 0 |
| TIE1 | I901S | lit | "TIE1" "I901S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | K908I | cv | TIE1 "Lys908Ile" ClinVar "TIE1" | 0 |
| TIE1 | K908I | lit | "TIE1" "K908I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | K908F | cv | TIE1 "Lys908Phe" ClinVar "TIE1" | 0 |
| TIE1 | K908F | lit | "TIE1" "K908F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | A916F | cv | TIE1 "Ala916Phe" ClinVar "TIE1" | 0 |
| TIE1 | A916F | lit | "TIE1" "A916F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TIE1 | C1055R | cv | TIE1 "Cys1055Arg" ClinVar "TIE1" | 0 |
| TIE1 | C1055R | lit | "TIE1" "C1055R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | A955E | cv | EGFR "Ala955Glu" ClinVar "EGFR" | 0 |
| EGFR | A955E | lit | "EGFR" "A955E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | E709D | cv | EGFR "Glu709Asp" ClinVar "EGFR" | 3 |
| EGFR | E709D | lit | "EGFR" "E709D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | L730Q | cv | EGFR "Leu730Gln" ClinVar "EGFR" | 0 |
| EGFR | L730Q | lit | "EGFR" "L730Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | V738N | cv | EGFR "Val738Asn" ClinVar "EGFR" | 0 |
| EGFR | V738N | lit | "EGFR" "V738N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | L799Q | cv | EGFR "Leu799Gln" ClinVar "EGFR" | 0 |
| EGFR | L799Q | lit | "EGFR" "L799Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | V738R | cv | EGFR "Val738Arg" ClinVar "EGFR" | 0 |
| EGFR | V738R | lit | "EGFR" "V738R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | V742I | cv | EGFR "Val742Ile" ClinVar "EGFR" | 3 |
| EGFR | V742I | lit | "EGFR" "V742I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | F968I | cv | EGFR "Phe968Ile" ClinVar "EGFR" | 0 |
| EGFR | F968I | lit | "EGFR" "F968I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | H773N | cv | EGFR "His773Asn" ClinVar "EGFR" | 1 |
| EGFR | H773N | lit | "EGFR" "H773N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 9 |
| EGFR | R776S | cv | EGFR "Arg776Ser" ClinVar "EGFR" | 0 |
| EGFR | R776S | lit | "EGFR" "R776S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 15 |
| EGFR | L782I | cv | EGFR "Leu782Ile" ClinVar "EGFR" | 0 |
| EGFR | L782I | lit | "EGFR" "L782I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | L782F | cv | EGFR "Leu782Phe" ClinVar "EGFR" | 0 |
| EGFR | L782F | lit | "EGFR" "L782F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | I789F | cv | EGFR "Ile789Phe" ClinVar "EGFR" | 0 |
| EGFR | I789F | lit | "EGFR" "I789F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EGFR | D916R | cv | EGFR "Asp916Arg" ClinVar "EGFR" | 0 |
| EGFR | D916R | lit | "EGFR" "D916R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | A427E | cv | CSK "Ala427Glu" ClinVar "CSK" | 0 |
| CSK | A427E | lit | "CSK" "A427E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | M192D | cv | CSK "Met192Asp" ClinVar "CSK" | 0 |
| CSK | M192D | lit | "CSK" "M192D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | R215N | cv | CSK "Arg215Asn" ClinVar "CSK" | 0 |
| CSK | R215N | lit | "CSK" "R215N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | V275Q | cv | CSK "Val275Gln" ClinVar "CSK" | 0 |
| CSK | V275Q | lit | "CSK" "V275Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | V219I | cv | CSK "Val219Ile" ClinVar "CSK" | 0 |
| CSK | V219I | lit | "CSK" "V219I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | L440I | cv | CSK "Leu440Ile" ClinVar "CSK" | 0 |
| CSK | L440I | lit | "CSK" "L440I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | Q250S | cv | CSK "Gln250Ser" ClinVar "CSK" | 0 |
| CSK | Q250S | lit | "CSK" "Q250S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | V256I | cv | CSK "Val256Ile" ClinVar "CSK" | 0 |
| CSK | V256I | lit | "CSK" "V256I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | V256F | cv | CSK "Val256Phe" ClinVar "CSK" | 0 |
| CSK | V256F | lit | "CSK" "V256F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | V265F | cv | CSK "Val265Phe" ClinVar "CSK" | 0 |
| CSK | V265F | lit | "CSK" "V265F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | P388R | cv | CSK "Pro388Arg" ClinVar "CSK" | 0 |
| CSK | P388R | lit | "CSK" "P388R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | R107* | cv | CSK "Arg107Ter" ClinVar "CSK" | 0 |
| CSK | R107* | lit | "CSK" "R107X" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| CSK | E108R | cv | CSK "Glu108Arg" ClinVar "CSK" | 0 |
| CSK | E108R | lit | "CSK" "E108R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | L685T | cv | FGFR4 "Leu685Thr" ClinVar "FGFR4" | 0 |
| FGFR4 | L685T | lit | "FGFR4" "L685T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | P730E | cv | FGFR4 "Pro730Glu" ClinVar "FGFR4" | 0 |
| FGFR4 | P730E | lit | "FGFR4" "P730E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | R464D | cv | FGFR4 "Arg464Asp" ClinVar "FGFR4" | 0 |
| FGFR4 | R464D | lit | "FGFR4" "R464D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | G488Q | cv | FGFR4 "Gly488Gln" ClinVar "FGFR4" | 0 |
| FGFR4 | G488Q | lit | "FGFR4" "G488Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | Q496N | cv | FGFR4 "Gln496Asn" ClinVar "FGFR4" | 0 |
| FGFR4 | Q496N | lit | "FGFR4" "Q496N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | R559Q | cv | FGFR4 "Arg559Gln" ClinVar "FGFR4" | 5 |
| FGFR4 | R559Q | lit | "FGFR4" "R559Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| FGFR4 | G488R | cv | FGFR4 "Gly488Arg" ClinVar "FGFR4" | 0 |
| FGFR4 | G488R | lit | "FGFR4" "G488R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| FGFR4 | V500I | cv | FGFR4 "Val500Ile" ClinVar "FGFR4" | 0 |
| FGFR4 | V500I | lit | "FGFR4" "V500I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | L743I | cv | FGFR4 "Leu743Ile" ClinVar "FGFR4" | 0 |
| FGFR4 | L743I | lit | "FGFR4" "L743I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | N535S | cv | FGFR4 "Asn535Ser" ClinVar "FGFR4" | 0 |
| FGFR4 | N535S | lit | "FGFR4" "N535S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 2 |
| FGFR4 | T541I | cv | FGFR4 "Thr541Ile" ClinVar "FGFR4" | 0 |
| FGFR4 | T541I | lit | "FGFR4" "T541I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | T541F | cv | FGFR4 "Thr541Phe" ClinVar "FGFR4" | 0 |
| FGFR4 | T541F | lit | "FGFR4" "T541F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | I549F | cv | FGFR4 "Ile549Phe" ClinVar "FGFR4" | 0 |
| FGFR4 | I549F | lit | "FGFR4" "I549F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FGFR4 | P691R | cv | FGFR4 "Pro691Arg" ClinVar "FGFR4" | 0 |
| FGFR4 | P691R | lit | "FGFR4" "P691R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | K627T | cv | PTK2 "Lys627Thr" ClinVar "PTK2" | 0 |
| PTK2 | K627T | lit | "PTK2" "K627T" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | P663E | cv | PTK2 "Pro663Glu" ClinVar "PTK2" | 0 |
| PTK2 | P663E | lit | "PTK2" "P663E" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | R419D | cv | PTK2 "Arg419Asp" ClinVar "PTK2" | 0 |
| PTK2 | R419D | lit | "PTK2" "R419D" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | I440Q | cv | PTK2 "Ile440Gln" ClinVar "PTK2" | 0 |
| PTK2 | I440Q | lit | "PTK2" "I440Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | P447N | cv | PTK2 "Pro447Asn" ClinVar "PTK2" | 0 |
| PTK2 | P447N | lit | "PTK2" "P447N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | R508Q | cv | PTK2 "Arg508Gln" ClinVar "PTK2" | 0 |
| PTK2 | R508Q | lit | "PTK2" "R508Q" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | G625H | cv | PTK2 "Gly625His" ClinVar "PTK2" | 0 |
| PTK2 | G625H | lit | "PTK2" "G625H" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | P444R | cv | PTK2 "Pro444Arg" ClinVar "PTK2" | 0 |
| PTK2 | P444R | lit | "PTK2" "P444R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | V451I | cv | PTK2 "Val451Ile" ClinVar "PTK2" | 0 |
| PTK2 | V451I | lit | "PTK2" "V451I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | L676I | cv | PTK2 "Leu676Ile" ClinVar "PTK2" | 0 |
| PTK2 | L676I | lit | "PTK2" "L676I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | H482N | cv | PTK2 "His482Asn" ClinVar "PTK2" | 0 |
| PTK2 | H482N | lit | "PTK2" "H482N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | K485S | cv | PTK2 "Lys485Ser" ClinVar "PTK2" | 0 |
| PTK2 | K485S | lit | "PTK2" "K485S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | T491I | cv | PTK2 "Thr491Ile" ClinVar "PTK2" | 0 |
| PTK2 | T491I | lit | "PTK2" "T491I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | T491F | cv | PTK2 "Thr491Phe" ClinVar "PTK2" | 0 |
| PTK2 | T491F | lit | "PTK2" "T491F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | I498F | cv | PTK2 "Ile498Phe" ClinVar "PTK2" | 0 |
| PTK2 | I498F | lit | "PTK2" "I498F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2 | Q624R | cv | PTK2 "Gln624Arg" ClinVar "PTK2" | 0 |
| PTK2 | Q624R | lit | "PTK2" "Q624R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | V454I | cv | PTK2B "Val454Ile" ClinVar "PTK2B" | 0 |
| PTK2B | V454I | lit | "PTK2B" "V454I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | L679I | cv | PTK2B "Leu679Ile" ClinVar "PTK2B" | 0 |
| PTK2B | L679I | lit | "PTK2B" "L679I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | H485N | cv | PTK2B "His485Asn" ClinVar "PTK2B" | 0 |
| PTK2B | H485N | lit | "PTK2B" "H485N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | K488S | cv | PTK2B "Lys488Ser" ClinVar "PTK2B" | 0 |
| PTK2B | K488S | lit | "PTK2B" "K488S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | I493F | cv | PTK2B "Ile493Phe" ClinVar "PTK2B" | 0 |
| PTK2B | I493F | lit | "PTK2B" "I493F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | I501F | cv | PTK2B "Ile501Phe" ClinVar "PTK2B" | 0 |
| PTK2B | I501F | lit | "PTK2B" "I501F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| PTK2B | F627R | cv | PTK2B "Phe627Arg" ClinVar "PTK2B" | 0 |
| PTK2B | F627R | lit | "PTK2B" "F627R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | V366I | cv | ZAP70 "Val366Ile" ClinVar "ZAP70" | 0 |
| ZAP70 | V366I | lit | "ZAP70" "V366I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | L600I | cv | ZAP70 "Leu600Ile" ClinVar "ZAP70" | 0 |
| ZAP70 | L600I | lit | "ZAP70" "L600I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | Y397N | cv | ZAP70 "Tyr397Asn" ClinVar "ZAP70" | 0 |
| ZAP70 | Y397N | lit | "ZAP70" "Y397N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | R400S | cv | ZAP70 "Arg400Ser" ClinVar "ZAP70" | 0 |
| ZAP70 | R400S | lit | "ZAP70" "R400S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | Q406I | cv | ZAP70 "Gln406Ile" ClinVar "ZAP70" | 0 |
| ZAP70 | Q406I | lit | "ZAP70" "Q406I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | Q406F | cv | ZAP70 "Gln406Phe" ClinVar "ZAP70" | 0 |
| ZAP70 | Q406F | lit | "ZAP70" "Q406F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | V413F | cv | ZAP70 "Val413Phe" ClinVar "ZAP70" | 0 |
| ZAP70 | V413F | lit | "ZAP70" "V413F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ZAP70 | K541R | cv | ZAP70 "Lys541Arg" ClinVar "ZAP70" | 0 |
| ZAP70 | K541R | lit | "ZAP70" "K541R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | V704I | cv | EPHA5 "Val704Ile" ClinVar "EPHA5" | 0 |
| EPHA5 | V704I | lit | "EPHA5" "V704I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | P939I | cv | EPHA5 "Pro939Ile" ClinVar "EPHA5" | 0 |
| EPHA5 | P939I | lit | "EPHA5" "P939I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | H738S | cv | EPHA5 "His738Ser" ClinVar "EPHA5" | 0 |
| EPHA5 | H738S | lit | "EPHA5" "H738S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | T744I | cv | EPHA5 "Thr744Ile" ClinVar "EPHA5" | 0 |
| EPHA5 | T744I | lit | "EPHA5" "T744I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | T744F | cv | EPHA5 "Thr744Phe" ClinVar "EPHA5" | 0 |
| EPHA5 | T744F | lit | "EPHA5" "T744F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | V752F | cv | EPHA5 "Val752Phe" ClinVar "EPHA5" | 0 |
| EPHA5 | V752F | lit | "EPHA5" "V752F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA5 | W880R | cv | EPHA5 "Trp880Arg" ClinVar "EPHA5" | 0 |
| EPHA5 | W880R | lit | "EPHA5" "W880R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| BTK | V427I | cv | BTK "Val427Ile" ClinVar "BTK" | 0 |
| BTK | V427I | lit | "BTK" "V427I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| BTK | L652I | cv | BTK "Leu652Ile" ClinVar "BTK" | 0 |
| BTK | L652I | lit | "BTK" "L652I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| BTK | K456N | cv | BTK "Lys456Asn" ClinVar "BTK" | 0 |
| BTK | K456N | lit | "BTK" "K456N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| BTK | Q459S | cv | BTK "Gln459Ser" ClinVar "BTK" | 0 |
| BTK | Q459S | lit | "BTK" "Q459S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| BTK | T465I | cv | BTK "Thr465Ile" ClinVar "BTK" | 0 |
| BTK | T465I | lit | "BTK" "T465I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| BTK | T465F | cv | BTK "Thr465Phe" ClinVar "BTK" | 0 |
| BTK | T465F | lit | "BTK" "T465F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| BTK | I473F | cv | BTK "Ile473Phe" ClinVar "BTK" | 0 |
| BTK | I473F | lit | "BTK" "I473F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| BTK | E599R | cv | BTK "Glu599Arg" ClinVar "BTK" | 0 |
| BTK | E599R | lit | "BTK" "E599R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | K1023R | cv | IGF1R "Lys1023Arg" ClinVar "IGF1R" | 0 |
| IGF1R | K1023R | lit | "IGF1R" "K1023R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | V1030I | cv | IGF1R "Val1030Ile" ClinVar "IGF1R" | 0 |
| IGF1R | V1030I | lit | "IGF1R" "V1030I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | H1061N | cv | IGF1R "His1061Asn" ClinVar "IGF1R" | 0 |
| IGF1R | H1061N | lit | "IGF1R" "H1061N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | R1064S | cv | IGF1R "Arg1064Ser" ClinVar "IGF1R" | 0 |
| IGF1R | R1064S | lit | "IGF1R" "R1064S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | S1070I | cv | IGF1R "Ser1070Ile" ClinVar "IGF1R" | 0 |
| IGF1R | S1070I | lit | "IGF1R" "S1070I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | S1070F | cv | IGF1R "Ser1070Phe" ClinVar "IGF1R" | 0 |
| IGF1R | S1070F | lit | "IGF1R" "S1070F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | I1078F | cv | IGF1R "Ile1078Phe" ClinVar "IGF1R" | 0 |
| IGF1R | I1078F | lit | "IGF1R" "I1078F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| IGF1R | Q1214R | cv | IGF1R "Gln1214Arg" ClinVar "IGF1R" | 0 |
| IGF1R | Q1214R | lit | "IGF1R" "Q1214R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA7 | V662I | cv | EPHA7 "Val662Ile" ClinVar "EPHA7" | 0 |
| EPHA7 | V662I | lit | "EPHA7" "V662I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| EPHA7 | P897I | cv | EPHA7 "Pro897Ile" ClinVar "EPHA7" | 0 |
| EPHA7 | P897I | lit | "EPHA7" "P897I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA7 | H696S | cv | EPHA7 "His696Ser" ClinVar "EPHA7" | 0 |
| EPHA7 | H696S | lit | "EPHA7" "H696S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA7 | T702I | cv | EPHA7 "Thr702Ile" ClinVar "EPHA7" | 0 |
| EPHA7 | T702I | lit | "EPHA7" "T702I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA7 | T702F | cv | EPHA7 "Thr702Phe" ClinVar "EPHA7" | 0 |
| EPHA7 | T702F | lit | "EPHA7" "T702F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA7 | V710F | cv | EPHA7 "Val710Phe" ClinVar "EPHA7" | 0 |
| EPHA7 | V710F | lit | "EPHA7" "V710F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA7 | W838R | cv | EPHA7 "Trp838Arg" ClinVar "EPHA7" | 0 |
| EPHA7 | W838R | lit | "EPHA7" "W838R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FES | V587I | cv | FES "Val587Ile" ClinVar "FES" | 0 |
| FES | V587I | lit | "FES" "V587I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FES | L814I | cv | FES "Leu814Ile" ClinVar "FES" | 0 |
| FES | L814I | lit | "FES" "L814I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FES | R621S | cv | FES "Arg621Ser" ClinVar "FES" | 0 |
| FES | R621S | lit | "FES" "R621S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FES | T627I | cv | FES "Thr627Ile" ClinVar "FES" | 0 |
| FES | T627I | lit | "FES" "T627I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 1 |
| FES | T627F | cv | FES "Thr627Phe" ClinVar "FES" | 0 |
| FES | T627F | lit | "FES" "T627F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FES | V635F | cv | FES "Val635Phe" ClinVar "FES" | 0 |
| FES | V635F | lit | "FES" "V635F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FES | P762R | cv | FES "Pro762Arg" ClinVar "FES" | 0 |
| FES | P762R | lit | "FES" "P762R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | V296I | cv | TXK "Val296Ile" ClinVar "TXK" | 0 |
| TXK | V296I | lit | "TXK" "V296I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | V520I | cv | TXK "Val520Ile" ClinVar "TXK" | 0 |
| TXK | V520I | lit | "TXK" "V520I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | K325N | cv | TXK "Lys325Asn" ClinVar "TXK" | 1 |
| TXK | K325N | lit | "TXK" "K325N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | Q328S | cv | TXK "Gln328Ser" ClinVar "TXK" | 0 |
| TXK | Q328S | lit | "TXK" "Q328S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | I334F | cv | TXK "Ile334Phe" ClinVar "TXK" | 0 |
| TXK | I334F | lit | "TXK" "I334F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | V342F | cv | TXK "Val342Phe" ClinVar "TXK" | 0 |
| TXK | V342F | lit | "TXK" "V342F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TXK | E468R | cv | TXK "Glu468Arg" ClinVar "TXK" | 0 |
| TXK | E468R | lit | "TXK" "E468R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | V648I | cv | EPHB1 "Val648Ile" ClinVar "EPHB1" | 0 |
| EPHB1 | V648I | lit | "EPHB1" "V648I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | L878I | cv | EPHB1 "Leu878Ile" ClinVar "EPHB1" | 0 |
| EPHB1 | L878I | lit | "EPHB1" "L878I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | R682S | cv | EPHB1 "Arg682Ser" ClinVar "EPHB1" | 0 |
| EPHB1 | R682S | lit | "EPHB1" "R682S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | T688I | cv | EPHB1 "Thr688Ile" ClinVar "EPHB1" | 0 |
| EPHB1 | T688I | lit | "EPHB1" "T688I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | T688F | cv | EPHB1 "Thr688Phe" ClinVar "EPHB1" | 0 |
| EPHB1 | T688F | lit | "EPHB1" "T688F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | I696F | cv | EPHB1 "Ile696Phe" ClinVar "EPHB1" | 0 |
| EPHB1 | I696F | lit | "EPHB1" "I696F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHB1 | W826R | cv | EPHB1 "Trp826Arg" ClinVar "EPHB1" | 0 |
| EPHB1 | W826R | lit | "EPHB1" "W826R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | G1971R | cv | ROS1 "Gly1971Arg" ClinVar "ROS1" | 0 |
| ROS1 | G1971R | lit | "ROS1" "G1971R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | V1977I | cv | ROS1 "Val1977Ile" ClinVar "ROS1" | 0 |
| ROS1 | V1977I | lit | "ROS1" "V1977I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | L2215I | cv | ROS1 "Leu2215Ile" ClinVar "ROS1" | 0 |
| ROS1 | L2215I | lit | "ROS1" "L2215I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | K2011S | cv | ROS1 "Lys2011Ser" ClinVar "ROS1" | 0 |
| ROS1 | K2011S | lit | "ROS1" "K2011S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | L2017I | cv | ROS1 "Leu2017Ile" ClinVar "ROS1" | 0 |
| ROS1 | L2017I | lit | "ROS1" "L2017I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | L2017F | cv | ROS1 "Leu2017Phe" ClinVar "ROS1" | 0 |
| ROS1 | L2017F | lit | "ROS1" "L2017F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | I2025F | cv | ROS1 "Ile2025Phe" ClinVar "ROS1" | 0 |
| ROS1 | I2025F | lit | "ROS1" "I2025F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| ROS1 | P2163R | cv | ROS1 "Pro2163Arg" ClinVar "ROS1" | 0 |
| ROS1 | P2163R | lit | "ROS1" "P2163R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | V588I | cv | FER "Val588Ile" ClinVar "FER" | 0 |
| FER | V588I | lit | "FER" "V588I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | L814I | cv | FER "Leu814Ile" ClinVar "FER" | 0 |
| FER | L814I | lit | "FER" "L814I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | K622S | cv | FER "Lys622Ser" ClinVar "FER" | 0 |
| FER | K622S | lit | "FER" "K622S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | T628I | cv | FER "Thr628Ile" ClinVar "FER" | 0 |
| FER | T628I | lit | "FER" "T628I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | T628F | cv | FER "Thr628Phe" ClinVar "FER" | 0 |
| FER | T628F | lit | "FER" "T628F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | I636F | cv | FER "Ile636Phe" ClinVar "FER" | 0 |
| FER | I636F | lit | "FER" "I636F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| FER | P762R | cv | FER "Pro762Arg" ClinVar "FER" | 0 |
| FER | P762R | lit | "FER" "P762R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | V395I | cv | TEC "Val395Ile" ClinVar "TEC" | 0 |
| TEC | V395I | lit | "TEC" "V395I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | K424N | cv | TEC "Lys424Asn" ClinVar "TEC" | 0 |
| TEC | K424N | lit | "TEC" "K424N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | Q427S | cv | TEC "Gln427Ser" ClinVar "TEC" | 0 |
| TEC | Q427S | lit | "TEC" "Q427S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | T433I | cv | TEC "Thr433Ile" ClinVar "TEC" | 1 |
| TEC | T433I | lit | "TEC" "T433I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | T433F | cv | TEC "Thr433Phe" ClinVar "TEC" | 0 |
| TEC | T433F | lit | "TEC" "T433F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | V441F | cv | TEC "Val441Phe" ClinVar "TEC" | 0 |
| TEC | V441F | lit | "TEC" "V441F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| TEC | E567R | cv | TEC "Glu567Arg" ClinVar "TEC" | 3 |
| TEC | E567R | lit | "TEC" "E567R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 2 |
| EPHA1 | V653I | cv | EPHA1 "Val653Ile" ClinVar "EPHA1" | 0 |
| EPHA1 | V653I | lit | "EPHA1" "V653I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | L880I | cv | EPHA1 "Leu880Ile" ClinVar "EPHA1" | 0 |
| EPHA1 | L880I | lit | "EPHA1" "L880I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | H684N | cv | EPHA1 "His684Asn" ClinVar "EPHA1" | 0 |
| EPHA1 | H684N | lit | "EPHA1" "H684N" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | H687S | cv | EPHA1 "His687Ser" ClinVar "EPHA1" | 0 |
| EPHA1 | H687S | lit | "EPHA1" "H687S" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | T693I | cv | EPHA1 "Thr693Ile" ClinVar "EPHA1" | 0 |
| EPHA1 | T693I | lit | "EPHA1" "T693I" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | T693F | cv | EPHA1 "Thr693Phe" ClinVar "EPHA1" | 0 |
| EPHA1 | T693F | lit | "EPHA1" "T693F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | I701F | cv | EPHA1 "Ile701Phe" ClinVar "EPHA1" | 0 |
| EPHA1 | I701F | lit | "EPHA1" "I701F" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |
| EPHA1 | G828R | cv | EPHA1 "Gly828Arg" ClinVar "EPHA1" | 0 |
| EPHA1 | G828R | lit | "EPHA1" "G828R" kinase mutation variant study cancer gnomAD COSMIC OncoKB | 0 |

</details>

### D. Distant proteins for the ten study variants

<details>
<summary>projections.tsv — 87 rows</summary>

| JAK2_input | protein | domain | raw_projected_change | all_8_positions | assessment |
| --- | --- | --- | --- | --- | --- |
| I1065T | BRAF | JH1 | I659T | 659,656,659,656,659,656,659,656 | depends on alignment or anchor; see positions |
| V1110E | BRAF | JH1 | R701E | 701,701,701,701,701,701,701,701 | eight settings agree |
| G571R | BRAF | JH2 |  | -,-,-,483,-,-,-,- | no numerical mapping |
| V578I | BRAF | JH2 | V480I | 480,480,480,490,480,480,480,480 | depends on alignment or anchor; see positions |
| L805I | BRAF | JH2 | I714I | 714,714,714,714,714,714,714,714 | eight settings agree; endpoint already present |
| I1065T | RAF1 | JH1 | I551T | 551,551,561,-,551,551,561,- | depends on alignment or anchor; see positions |
| V1110E | RAF1 | JH1 | K593E | 593,593,593,-,593,593,593,- | depends on alignment or anchor; see positions |
| G571R | RAF1 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| V578I | RAF1 | JH2 | V372I | 375,375,375,375,372,372,372,372 | depends on alignment or anchor; see positions |
| L805I | RAF1 | JH2 | I606I | 606,606,606,-,606,606,606,- | depends on alignment or anchor; see positions; endpoint already present |
| I1065T | MAP2K1 | JH1 | M274T | 274,274,300,-,274,274,300,- | depends on alignment or anchor; see positions |
| V1110E | MAP2K1 | JH1 | P346E | 346,346,346,-,346,346,346,- | depends on alignment or anchor; see positions |
| G571R | MAP2K1 | JH2 |  | -,91,91,-,-,-,-,- | no numerical mapping |
| V578I | MAP2K1 | JH2 | M94I | 97,98,98,-,94,94,94,94 | depends on alignment or anchor; see positions |
| L805I | MAP2K1 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| I1065T | MAP2K2 | JH1 | H308T | 308,308,283,-,308,308,283,- | depends on alignment or anchor; see positions |
| V1110E | MAP2K2 | JH1 | P354E | 354,354,-,-,354,354,-,- | depends on alignment or anchor; see positions |
| G571R | MAP2K2 | JH2 |  | 95,-,95,-,-,-,-,- | no numerical mapping |
| V578I | MAP2K2 | JH2 | M98I | 102,-,102,-,98,98,-,- | depends on alignment or anchor; see positions |
| L805I | MAP2K2 | JH2 | L322I | 322,-,-,-,322,-,-,- | depends on alignment or anchor; see positions |
| I1065T | AKT1 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| V1110E | AKT1 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| G571R | AKT1 | JH2 |  | 178,-,-,-,-,-,-,- | no numerical mapping |
| V578I | AKT1 | JH2 | Y176I | 185,180,180,180,176,176,176,176 | depends on alignment or anchor; see positions |
| L805I | AKT1 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| I1065T | PRKACA | JH1 | F262T | 262,262,-,-,262,262,-,- | depends on alignment or anchor; see positions |
| V1110E | PRKACA | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| G571R | PRKACA | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| V578I | PRKACA | JH2 | Y70I | 70,70,70,70,70,70,70,70 | eight settings agree |
| L805I | PRKACA | JH2 | V289I | 289,-,-,-,289,-,-,- | depends on alignment or anchor; see positions |
| I1065T | CDK2 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| V1110E | CDK2 | JH1 | P234E | 234,-,-,-,234,-,-,- | depends on alignment or anchor; see positions |
| G571R | CDK2 | JH2 |  | -,-,-,30,-,-,-,- | no numerical mapping |
| V578I | CDK2 | JH2 | V30I | 31,31,31,-,30,30,30,30 | depends on alignment or anchor; see positions |
| L805I | CDK2 | JH2 | F248I | 248,-,248,-,248,-,248,- | depends on alignment or anchor; see positions |
| I1065T | CDK4 | JH1 | C215T | 215,-,215,-,215,-,215,- | depends on alignment or anchor; see positions |
| V1110E | CDK4 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| G571R | CDK4 | JH2 | G18R | 32,-,-,-,18,18,18,18 | depends on alignment or anchor; see positions |
| V578I | CDK4 | JH2 | V32I | 39,-,-,-,32,32,32,32 | depends on alignment or anchor; see positions |
| L805I | CDK4 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| I1065T | MAPK1 | JH1 | I255T | 255,-,-,-,255,-,-,- | depends on alignment or anchor; see positions |
| V1110E | MAPK1 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| G571R | MAPK1 | JH2 | D44R | 44,44,44,-,44,44,44,44 | depends on alignment or anchor; see positions |
| V578I | MAPK1 | JH2 | V51I | 51,51,51,-,51,51,51,51 | depends on alignment or anchor; see positions |
| L805I | MAPK1 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| I1065T | MAPK14 | JH1 | I250T | 250,250,250,-,250,250,250,- | depends on alignment or anchor; see positions |
| V1110E | MAPK14 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| G571R | MAPK14 | JH2 |  | 36,-,-,-,-,-,-,- | no numerical mapping |
| V578I | MAPK14 | JH2 | V50I | 46,-,-,-,50,50,50,50 | depends on alignment or anchor; see positions |
| L805I | MAPK14 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| I1065T | AURKA | JH1 |  | -,335,-,-,-,335,-,- | no numerical mapping |
| V1110E | AURKA | JH1 | P368E | 368,368,368,-,368,368,368,- | depends on alignment or anchor; see positions |
| G571R | AURKA | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| V578I | AURKA | JH2 | L159I | 159,159,159,159,159,159,159,159 | eight settings agree |
| L805I | AURKA | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| I1065T | STK11 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| V1110E | STK11 | JH1 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| G571R | STK11 | JH2 | E70R | 70,70,70,-,70,70,70,70 | depends on alignment or anchor; see positions |
| V578I | STK11 | JH2 | V77I | 77,77,77,-,77,77,77,77 | depends on alignment or anchor; see positions |
| L805I | STK11 | JH2 |  | -,-,-,-,-,-,-,- | no numerical mapping |
| R426* | PTPN11 | SH2-1 | R32* | 35,35,35,-,32,32,32,32 | depends on alignment or anchor; see positions |
| C427R | PTPN11 | SH2-1 | P33R | 36,36,36,-,33,33,-,- | depends on alignment or anchor; see positions |
| R426* | PTPN11 | SH2-2 | R138* | 138,138,138,-,138,138,138,138 | depends on alignment or anchor; see positions |
| C427R | PTPN11 | SH2-2 | E139R | 139,139,139,-,139,139,139,139 | depends on alignment or anchor; see positions |
| R426* | PTPN6 | SH2-1 | R30* | 30,30,30,-,30,30,30,30 | depends on alignment or anchor; see positions |
| C427R | PTPN6 | SH2-1 | P31R | 31,31,31,-,31,31,31,31 | depends on alignment or anchor; see positions |
| R426* | PTPN6 | SH2-2 | R136* | -,-,-,-,136,136,136,136 | depends on alignment or anchor; see positions |
| C427R | PTPN6 | SH2-2 | E137R | -,-,-,-,137,137,137,137 | depends on alignment or anchor; see positions |
| R426* | GRB2 | SH2-1 | R86* | 86,86,86,-,86,86,86,86 | depends on alignment or anchor; see positions |
| C427R | GRB2 | SH2-1 | S90R | 90,90,90,-,90,90,90,90 | depends on alignment or anchor; see positions |
| R426* | SH2D1A | SH2-1 | R32* | 32,32,32,-,32,32,32,32 | depends on alignment or anchor; see positions |
| C427R | SH2D1A | SH2-1 | C42R | 42,42,33,-,42,42,33,33 | depends on alignment or anchor; see positions |
| P37A | NF2 | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| F240V | NF2 | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| H380Y | NF2 | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| P37A | EZR | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| F240V | EZR | FERM | A177V | 177,302,177,-,177,302,177,- | unresolved FERM; suppress residue transfer |
| H380Y | EZR | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| P37A | MSN | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| F240V | MSN | FERM | V302V | 302,-,-,-,302,-,-,- | unresolved FERM; suppress residue transfer; endpoint already present |
| H380Y | MSN | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| P37A | RDX | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| F240V | RDX | FERM | V302V | 302,-,-,-,302,-,-,- | unresolved FERM; suppress residue transfer; endpoint already present |
| H380Y | RDX | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| P37A | EPB41 | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |
| F240V | EPB41 | FERM | Y289V | 289,-,-,-,289,-,-,- | unresolved FERM; suppress residue transfer |
| H380Y | EPB41 | FERM |  | -,-,-,-,-,-,-,- | unresolved FERM; suppress residue transfer |

</details>

<details>
<summary>evidence.tsv — 9 rows</summary>

| JAK2 | other_gene | other_allele | relationship | evidence | reference |
| --- | --- | --- | --- | --- | --- |
| R426* | PTPN11 | R138* | conserved SH2 Arg; same truncation | Segregated with metachondromatosis; disease mechanism in PTPN11 is loss of function. A stop has consequences beyond loss of the Arg side chain. | https://doi.org/10.1371/journal.pgen.1000991 https://www.ncbi.nlm.nih.gov/clinvar/variation/13348/ |
| R426* | SH2D1A | R32T | same motif position; different allele | Clinical XLP allele at the invariant Arg; this is a missense comparison. | https://www.ncbi.nlm.nih.gov/clinvar/variation/10901/ |
| C427R | PTPN11 | E139D | same site after aligning SH2 Arg138; different starting residue and endpoint | Noonan-associated substitution; mutant crystal structure and analysis of altered ligand specificity. No transfer of pathogenicity to JAK2. | https://pmc.ncbi.nlm.nih.gov/articles/PMC4007598/ https://www.ncbi.nlm.nih.gov/clinvar/variation/40513/ |
| C427R | GRB2 | S90R | uncertain loop correspondence | Experimental Grb2 S90R showed minimal binding to a particular inhibitor peptide; not established as JAK2 C427-equivalent. | https://doi.org/10.3389/fmolb.2017.00064 |
| V578I | MAP2K1 | M94I | different starting residue, identical endpoint, three residues before ATP-site lysine | Isolated variant tested in cell competition and transformation assays. Both resembled wild-type MEK1. | https://pubmed.ncbi.nlm.nih.gov/36442478/ https://ckb.genomenon.com/geneVariant/show?geneVariantId=46611 |
| V578I | BRAF / RAF1 / CDK2 / CDK4 / MAPK1 / MAPK14 | V480I / V372I / V30I / V32I / V51I / V50I | Val-to-Ile at homologous beta3 lysine minus 3 | Sequence projections only. No individual functional score verified for these exact alleles. | https://mapk.gs.washington.edu/index.html |
| L805I | BRAF | I714 (WT); I714V reported | wild type already Ile; other allele is reverse change | All settings select I714. I714V indexed as uncertain significance; does not establish effect of JAK2 L805I. | https://sugi.bio/variant/gene/BRAF |
| I1065T | BRAF | I659T | exact chemistry but competing placement Y656 | ClinVar Miner lists NM_004333.6:c.1976T>C, rs2128994327. Sequence projection changes with gap penalties. | https://clinvarminer.genetics.utah.edu/variants-by-gene/BRAF/significance/any |
| V1110E | BRAF | R701G reported; R701E projected | same aligned column only | R701G is indexed as a VUS. Arg-to-Gly cannot establish the effect of introducing Glu at JAK2 Val1110. No R701E functional result verified. | https://sugi.bio/variant/gene/BRAF |

</details>

<details>
<summary>db_coverage.tsv — 48 rows</summary>

| gene | index_url | page_length_if_accessible | same_site_leads |
| --- | --- | --- | --- |
| BRAF | https://sugi.bio/variant/gene/BRAF | 2020 | R701G,I714V |
| RAF1 | https://sugi.bio/variant/gene/RAF1 | 0 |  |
| MAP2K1 | https://sugi.bio/variant/gene/MAP2K1 | 1474 | M94V,P346= |
| AKT1 | https://sugi.bio/variant/gene/AKT1 | 1634 | Y176= |
| PRKACA | https://sugi.bio/variant/gene/PRKACA | 183 | Y70C,Y70H |
| CDK2 | https://sugi.bio/variant/gene/CDK2 | 53 |  |
| MAPK1 | https://sugi.bio/variant/gene/MAPK1 | 0 |  |
| MAPK14 | https://sugi.bio/variant/gene/MAPK14 | 80 |  |
| AURKA | https://sugi.bio/variant/gene/AURKA | 106 |  |
| STK11 | https://sugi.bio/variant/gene/STK11 | 3134 | E70Q,V77=,E70=,E70G |
| MAP2K2 | https://sugi.bio/variant/gene/MAP2K2 | 0 |  |
| CDK4 | https://sugi.bio/variant/gene/CDK4 | 2002 | C215S,C215R,V32=,C215=,G18= |
| PTPN11 | https://sugi.bio/variant/gene/PTPN11 | 2186 | E139D,R138*,E139G,R32= |
| PTPN6 | https://sugi.bio/variant/gene/PTPN6 | 149 |  |
| GRB2 | https://sugi.bio/variant/gene/GRB2 | 0 |  |
| SH2D1A | https://sugi.bio/variant/gene/SH2D1A | 0 |  |
| BRAF | https://www.jcga-scc.jp/en/gene/BRAF | 124 |  |
| RAF1 | https://www.jcga-scc.jp/en/gene/RAF1 | 101 |  |
| MAP2K1 | https://www.jcga-scc.jp/en/gene/MAP2K1 | 107 |  |
| AKT1 | https://www.jcga-scc.jp/en/gene/AKT1 | 100 |  |
| PRKACA | https://www.jcga-scc.jp/en/gene/PRKACA | 0 |  |
| CDK2 | https://www.jcga-scc.jp/en/gene/CDK2 | 0 |  |
| MAPK1 | https://www.jcga-scc.jp/en/gene/MAPK1 | 98 |  |
| MAPK14 | https://www.jcga-scc.jp/en/gene/MAPK14 | 0 |  |
| AURKA | https://www.jcga-scc.jp/en/gene/AURKA | 87 |  |
| STK11 | https://www.jcga-scc.jp/en/gene/STK11 | 112 |  |
| MAP2K2 | https://www.jcga-scc.jp/en/gene/MAP2K2 | 100 |  |
| CDK4 | https://www.jcga-scc.jp/en/gene/CDK4 | 94 |  |
| PTPN11 | https://www.jcga-scc.jp/en/gene/PTPN11 | 94 |  |
| PTPN6 | https://www.jcga-scc.jp/en/gene/PTPN6 | 0 |  |
| GRB2 | https://www.jcga-scc.jp/en/gene/GRB2 | 0 |  |
| SH2D1A | https://www.jcga-scc.jp/en/gene/SH2D1A | 90 |  |
| BRAF | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=BRAF | 0 |  |
| RAF1 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=RAF1 | 162 |  |
| MAP2K1 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=MAP2K1 | 142 |  |
| AKT1 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=AKT1 | 152 |  |
| PRKACA | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=PRKACA | 0 |  |
| CDK2 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=CDK2 | 0 |  |
| MAPK1 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=MAPK1 | 0 |  |
| MAPK14 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=MAPK14 | 0 |  |
| AURKA | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=AURKA | 0 |  |
| STK11 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=STK11 | 0 |  |
| MAP2K2 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=MAP2K2 | 88 |  |
| CDK4 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=CDK4 | 12 |  |
| PTPN11 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=PTPN11 | 326 | P33L |
| PTPN6 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=PTPN6 | 0 |  |
| GRB2 | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=GRB2 | 0 |  |
| SH2D1A | https://lilab.life.sjtu.edu.cn/canprovar2/inforprotein.php?display%5B1%5D=snp&display%5B2%5D=DEP&display%5B3%5D=COSMIC&display%5B4%5D=TCGA&display%5B5%5D=HPI&display%5B6%5D=OMIM&display%5B7%5D=Biomart&id=SH2D1A | 0 |  |

</details>

<details>
<summary>searches.tsv — 44 rows</summary>

| gene | JAK2 | query_allele | search |
| --- | --- | --- | --- |
| BRAF | I1065T | I659T | "BRAF" ("I659T" OR "Ile659Thr") mutation ClinVar functional |
| BRAF | V1110E | R701E | "BRAF" ("R701E" OR "Arg701Glu") mutation ClinVar functional |
| BRAF | V578I | V480I | "BRAF" ("V480I" OR "Val480Ile") mutation ClinVar functional |
| RAF1 | I1065T | I551T | "RAF1" ("I551T" OR "Ile551Thr") mutation ClinVar functional |
| RAF1 | V1110E | K593E | "RAF1" ("K593E" OR "Lys593Glu") mutation ClinVar functional |
| RAF1 | V578I | V372I | "RAF1" ("V372I" OR "Val372Ile") mutation ClinVar functional |
| MAP2K1 | I1065T | M274T | "MAP2K1" ("M274T" OR "Met274Thr") mutation ClinVar functional |
| MAP2K1 | V1110E | P346E | "MAP2K1" ("P346E" OR "Pro346Glu") mutation ClinVar functional |
| MAP2K1 | V578I | M94I | "MAP2K1" ("M94I" OR "Met94Ile") mutation ClinVar functional |
| MAP2K2 | I1065T | H308T | "MAP2K2" ("H308T" OR "His308Thr") mutation ClinVar functional |
| MAP2K2 | V1110E | P354E | "MAP2K2" ("P354E" OR "Pro354Glu") mutation ClinVar functional |
| MAP2K2 | V578I | M98I | "MAP2K2" ("M98I" OR "Met98Ile") mutation ClinVar functional |
| MAP2K2 | L805I | L322I | "MAP2K2" ("L322I" OR "Leu322Ile") mutation ClinVar functional |
| AKT1 | V578I | Y176I | "AKT1" ("Y176I" OR "Tyr176Ile") mutation ClinVar functional |
| PRKACA | I1065T | F262T | "PRKACA" ("F262T" OR "Phe262Thr") mutation ClinVar functional |
| PRKACA | V578I | Y70I | "PRKACA" ("Y70I" OR "Tyr70Ile") mutation ClinVar functional |
| PRKACA | L805I | V289I | "PRKACA" ("V289I" OR "Val289Ile") mutation ClinVar functional |
| CDK2 | V1110E | P234E | "CDK2" ("P234E" OR "Pro234Glu") mutation ClinVar functional |
| CDK2 | V578I | V30I | "CDK2" ("V30I" OR "Val30Ile") mutation ClinVar functional |
| CDK2 | L805I | F248I | "CDK2" ("F248I" OR "Phe248Ile") mutation ClinVar functional |
| CDK4 | I1065T | C215T | "CDK4" ("C215T" OR "Cys215Thr") mutation ClinVar functional |
| CDK4 | G571R | G18R | "CDK4" ("G18R" OR "Gly18Arg") mutation ClinVar functional |
| CDK4 | V578I | V32I | "CDK4" ("V32I" OR "Val32Ile") mutation ClinVar functional |
| MAPK1 | I1065T | I255T | "MAPK1" ("I255T" OR "Ile255Thr") mutation ClinVar functional |
| MAPK1 | G571R | D44R | "MAPK1" ("D44R" OR "Asp44Arg") mutation ClinVar functional |
| MAPK1 | V578I | V51I | "MAPK1" ("V51I" OR "Val51Ile") mutation ClinVar functional |
| MAPK14 | I1065T | I250T | "MAPK14" ("I250T" OR "Ile250Thr") mutation ClinVar functional |
| MAPK14 | V578I | V50I | "MAPK14" ("V50I" OR "Val50Ile") mutation ClinVar functional |
| AURKA | V1110E | P368E | "AURKA" ("P368E" OR "Pro368Glu") mutation ClinVar functional |
| AURKA | V578I | L159I | "AURKA" ("L159I" OR "Leu159Ile") mutation ClinVar functional |
| STK11 | G571R | E70R | "STK11" ("E70R" OR "Glu70Arg") mutation ClinVar functional |
| STK11 | V578I | V77I | "STK11" ("V77I" OR "Val77Ile") mutation ClinVar functional |
| PTPN11 | R426* | R32* | "PTPN11" ("R32X" OR "Arg32Ter") mutation ClinVar functional |
| PTPN11 | C427R | P33R | "PTPN11" ("P33R" OR "Pro33Arg") mutation ClinVar functional |
| PTPN11 | R426* | R138* | "PTPN11" ("R138X" OR "Arg138Ter") mutation ClinVar functional |
| PTPN11 | C427R | E139R | "PTPN11" ("E139R" OR "Glu139Arg") mutation ClinVar functional |
| PTPN6 | R426* | R30* | "PTPN6" ("R30X" OR "Arg30Ter") mutation ClinVar functional |
| PTPN6 | C427R | P31R | "PTPN6" ("P31R" OR "Pro31Arg") mutation ClinVar functional |
| PTPN6 | R426* | R136* | "PTPN6" ("R136X" OR "Arg136Ter") mutation ClinVar functional |
| PTPN6 | C427R | E137R | "PTPN6" ("E137R" OR "Glu137Arg") mutation ClinVar functional |
| GRB2 | R426* | R86* | "GRB2" ("R86X" OR "Arg86Ter") mutation ClinVar functional |
| GRB2 | C427R | S90R | "GRB2" ("S90R" OR "Ser90Arg") mutation ClinVar functional |
| SH2D1A | R426* | R32* | "SH2D1A" ("R32X" OR "Arg32Ter") mutation ClinVar functional |
| SH2D1A | C427R | C42R | "SH2D1A" ("C42R" OR "Cys42Arg") mutation ClinVar functional |

</details>

<details>
<summary>source_sequences.tsv — 22 rows</summary>

| gene | source | length |
| --- | --- | --- |
| JAK2 | https://www.kegg.jp/entry/hsa:3717 | 1132 |
| BRAF | https://www.kegg.jp/entry/hsa:673 | 766 |
| RAF1 | https://www.kegg.jp/entry/hsa:5894 | 648 |
| MAP2K1 | https://www.kegg.jp/entry/hsa:5604 | 393 |
| AKT1 | https://www.kegg.jp/entry/hsa:207 | 480 |
| PRKACA | https://www.kegg.jp/entry/hsa:5566 | 351 |
| CDK2 | https://www.kegg.jp/entry/hsa:1017 | 298 |
| MAPK1 | https://www.kegg.jp/entry/hsa:5594 | 360 |
| MAPK14 | https://www.kegg.jp/entry/hsa:1432 | 360 |
| AURKA | https://www.kegg.jp/entry/hsa:6790 | 403 |
| STK11 | https://www.kegg.jp/entry/hsa:6794 | 433 |
| MAP2K2 | https://www.kegg.jp/entry/hsa:5605 | 400 |
| CDK4 | https://www.kegg.jp/entry/hsa:1019 | 303 |
| PTPN11 | https://www.kegg.jp/entry/hsa:5781 | 593 |
| PTPN6 | https://www.kegg.jp/entry/hsa:5777 | 595 |
| GRB2 | https://www.kegg.jp/entry/hsa:2885 | 217 |
| SH2D1A | https://www.kegg.jp/entry/hsa:4068 | 128 |
| MSN | https://www.kegg.jp/entry/hsa:4478 | 577 |
| EZR | https://www.kegg.jp/entry/hsa:7430 | 586 |
| RDX | https://www.kegg.jp/entry/hsa:5962 | 583 |
| NF2 | https://www.kegg.jp/entry/hsa:4771 | 595 |
| EPB41 | https://www.kegg.jp/entry/hsa:2035 | 864 |

</details>
