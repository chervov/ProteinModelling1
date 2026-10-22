# Variant effects by source matrix

Prepared 2026-10-22. This is the requested **gene × variant × source** table. Each source column corresponds to one primary, direct-evidence study from `01_direct_experimental_papers.md`.

## How to read the cells

- `GOF` = experimental evidence supports gain/hyperactivation/transforming activity in the stated model.
- `LOF` = experimental evidence supports reduced/absent protein, catalytic, scaffold, or signalling function.
- `Mixed` = different axes or alleles differ; do not collapse to a single mechanism.
- `Mech.` = engineered mechanistic mutant(s), not necessarily a clinically observed allele.
- `Panel` = a multi-variant study; exact per-allele calls require its tables/supplements. This prevents inventing variant-level calls from a title/abstract.
- A blank means the source did not test that row; it does **not** mean a neutral result.

## JAK1

| Variant / panel | S01 | S02 | S03 | S04 | S05 | S06 | S07 | S08 | S09 |
|---|---|---|---|---|---|---|---|---|---|
| Transforming-mutant panel | Panel: differential GOF signalling / FERM dependence |  |  |  |  |  |  |  |  |
| V658F |  | GOF cellular phenotype; isolated enzyme activity not increased |  |  |  |  |  |  |  |
| S703I |  |  | GOF: constitutive/hyperresponsive STAT signalling |  |  |  |  |  |  |
| R629_S632delinsSA |  |  |  | GOF: Ba/F3 factor independence and JAK-STAT activation |  |  |  |  |  |
| Germline JAK1-GOF panel |  |  |  |  | Panel: GOF disease modelling | Panel: familial GOF / treatment response | Panel: multiple germline GOF candidates | Panel: heterogeneous cell-line hyperactivation | Panel: novel patient GOF, cytokine-specific | 

## JAK2

| Variant / panel | S10 | S11 | S12 | S13 | S14 | S15 | S16 | S17 | S18 | S19 | S20 | S21 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| V617F | GOF: MPN proliferation/survival | GOF; requires functional FERM domain |  | GOF depends on F595 | GOF mechanism tested with F594/F595 perturbation | GOF-related JH2 structure | GOF JH1-JH2 model | GOF / alpha-C-helix dynamics | GOF suppression map | Receptor Tyr requirements for tumour phenotype | GOF suppressor map |  |
| JH2/linker GOF screen |  |  | Panel: 13 functional GOF missense alleles |  |  |  |  |  |  |  |  |  |
| V617F + F595 perturbation |  |  |  | Suppressed GOF |  |  |  |  |  |  |  |  |
| V617F + F594/F595 perturbation |  |  |  |  | Reduced GOF readouts |  |  |  |  |  |  |  |
| V617F + E596A |  |  |  |  |  |  |  |  | Suppressed oncogenic proliferation |  |  |  |
| Atypical exon 13/15 MPN alleles |  |  |  |  |  |  |  |  |  |  |  | Panel: individual effects require paper tables |

## JAK3

| Variant / panel | S22 | S23 | S24 | S25 | S26 | S27 | S28 | S29 |
|---|---|---|---|---|---|---|---|---|
| Patient JAK3 defects with residual T cells | LOF / residual function phenotype |  |  |  |  |  |  |  |
| Kinase-domain Tyr mutants |  | Mech.: positive and negative phosphoregulatory sites |  |  |  |  |  |  |
| SCID JH2 alleles |  |  | LOF / dysregulated JH2-JH1 regulation | Structural interpretation / mutation map |  |  |  |  |
| Patient-derived FERM alleles |  |  |  |  | LOF / altered catalytic regulation |  |  |  |
| T-ALL JAK3-mutant panel |  |  |  |  |  | GOF transformation through JAK1 |  |  |
| Q988P |  |  |  |  |  |  | GOF; ruxolitinib-resistance phenotype |  |
| Recent SCID/carrier-screening panel |  |  |  |  |  |  |  | Panel: some LOF, some VUS/neutral by tested assays |

## TYK2

| Variant / panel | S30 | S31 | S32 | S33 | S34 | S35 | S36 | S37 | S38 | S39 | S40 | S41 | S42 | S43 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Wild-type activation / early pathway context | TYK2 activated by IFN-alpha/beta |  |  |  |  |  |  |  |  |  |  |  |  |  |
| K930R (kinase-dead) |  | Mech.: catalytic loss; can still be phosphorylated |  |  |  |  |  |  |  |  |  |  |  |  |
| Y1054/Y1055 activation-loop mutants |  | Mech.: reduced signalling; combination abolishes signalling |  |  |  |  |  |  |  |  |  |  |  |  |
| N-terminal mutant panel |  |  | Mech.: receptor stability/scaffolding effects |  |  |  |  |  |  |  |  |  |  |  |
| Homozygous TYK2-deficiency allele |  |  |  | LOF: multi-cytokine signalling defect |  |  |  |  |  |  |  |  |  |  |
| ATP-pocket kinase-dead knock-in |  |  |  |  | Mech.: LOF type-I IFN response in vivo |  |  |  |  |  |  |  |  |  |
| I684S |  |  |  |  |  | Catalytically impaired but signalling competent |  |  |  |  |  |  |  |  |
| P1104A |  |  |  |  |  | Catalytically impaired but signalling competent | Human partial LOF / IL-23-IFN-gamma disease mechanism | MD-supported inactive-state model |  |  |  | Inherited deficiency: compound genotype context |  | DMS functional score available |
| rs2304256 / related splice-dose alleles |  |  |  |  |  |  |  |  | Splicing/dosage effect; coding substitution alone not defective in tested systems |  |  |  |  | DMS may contain missense component |
| B-ALL S431G, R425H, R832W |  |  |  |  |  |  |  |  |  | Functional cancer panel |  |  |  | DMS may contain substitutions |
| Patient TYK2-deficiency panels |  |  |  |  |  |  |  |  |  |  | Panel: divergent clinical phenotypes | Panel: R864C, G996R, G634E, G1010D, A928V/P1104A partial/complete LOF | Panel: complete-deficiency allele, LOF + scaffold defect | DMS may contain substitutions |
| Saturation / deep-mutational panel |  |  |  |  |  |  |  |  |  |  |  |  |  | Panel: abundance, IFN-alpha signalling, inhibitor interactions |

## Source key

| ID | PMID | Direct study |
|---|---:|---|
| S01 | [20868368](https://pubmed.ncbi.nlm.nih.gov/20868368/) | Transforming JAK1 mutations: signalling, FERM dependence, IFN-gamma response |
| S02 | [31683831](https://pubmed.ncbi.nlm.nih.gov/31683831/) | JAK1 wild-type and V658F enzymology |
| S03 | [32750333](https://pubmed.ncbi.nlm.nih.gov/32750333/) | JAK1 S703I autoinflammatory syndrome |
| S04 | [34496019](https://pubmed.ncbi.nlm.nih.gov/34496019/) | JAK1 R629_S632delinsSA in eosinophilic leukemia |
| S05 | [36546480](https://pubmed.ncbi.nlm.nih.gov/36546480/) | Human JAK1 GOF and allergic inflammation |
| S06 | [37343845](https://pubmed.ncbi.nlm.nih.gov/37343845/) | JAK1-associated inflammatory disease |
| S07 | [38563820](https://pubmed.ncbi.nlm.nih.gov/38563820/) | Syndromic JAK1 variants |
| S08 | [41136770](https://pubmed.ncbi.nlm.nih.gov/41136770/) | In-silico and cell-line study of JAK1 variants |
| S09 | [42379330](https://pubmed.ncbi.nlm.nih.gov/42379330/) | Novel JAK1 allele in atopic dermatitis |
| S10 | [15858187](https://pubmed.ncbi.nlm.nih.gov/15858187/) | JAK2 V617F MPN GOF |
| S11 | [18216297](https://pubmed.ncbi.nlm.nih.gov/18216297/) | JAK2 V617F FERM requirement |
| S12 | [19638629](https://pubmed.ncbi.nlm.nih.gov/19638629/) | JAK2 interdomain-linker GOF screen |
| S13 | [20585391](https://pubmed.ncbi.nlm.nih.gov/20585391/) | JAK2 V617F/F595 mechanism |
| S14 | [20958061](https://pubmed.ncbi.nlm.nih.gov/20958061/) | JAK2 V617F aromatic stacking mechanism |
| S15 | [22820988](https://pubmed.ncbi.nlm.nih.gov/22820988/) | JAK2 JH2/V617F structures |
| S16 | [23592968](https://pubmed.ncbi.nlm.nih.gov/23592968/) | JAK2 JH1-JH2 complex model and tests |
| S17 | [23863170](https://pubmed.ncbi.nlm.nih.gov/23863170/) | JAK2 JH2 functional/MD analysis |
| S18 | [27029346](https://pubmed.ncbi.nlm.nih.gov/27029346/) | JAK2 V617F suppression with JH2 alpha-C changes |
| S19 | [27998978](https://pubmed.ncbi.nlm.nih.gov/27998978/) | EpoR tyrosines in JAK2 V617F tumourigenesis |
| S20 | [30092288](https://pubmed.ncbi.nlm.nih.gov/30092288/) | JAK2 suppressing-mutation map |
| S21 | [33244866](https://pubmed.ncbi.nlm.nih.gov/33244866/) | Atypical JAK2 MPN alleles |
| S22 | [9446656](https://pubmed.ncbi.nlm.nih.gov/9446656/) | JAK3-deficient SCID with residual T cells |
| S23 | [9391116](https://pubmed.ncbi.nlm.nih.gov/9391116/) | JAK3 regulatory tyrosine mutants |
| S24 | [10629052](https://pubmed.ncbi.nlm.nih.gov/10629052/) | Naturally occurring JAK3 JH2 mutations |
| S25 | [10900158](https://pubmed.ncbi.nlm.nih.gov/10900158/) | JAK3 modelling and SCID mutation map |
| S26 | [11741532](https://pubmed.ncbi.nlm.nih.gov/11741532/) | JAK3 FERM-domain patient mutations |
| S27 | [25215497](https://pubmed.ncbi.nlm.nih.gov/25215497/) | JAK3 mutants transform through JAK1 |
| S28 | [37712558](https://pubmed.ncbi.nlm.nih.gov/37712558/) | JAK3 Q988P and ruxolitinib response |
| S29 | [42299341](https://pubmed.ncbi.nlm.nih.gov/42299341/) | JAK3 SCID/carrier-screening variants |
| S30 | [8055912](https://pubmed.ncbi.nlm.nih.gov/8055912/) | TYK2 activation by IFN-alpha/beta |
| S31 | [8702790](https://pubmed.ncbi.nlm.nih.gov/8702790/) | TYK2 activation-loop/catalytic mutants |
| S32 | [9342324](https://pubmed.ncbi.nlm.nih.gov/9342324/) | TYK2 N-terminal mutants and IFNAR1 stability |
| S33 | [17088085](https://pubmed.ncbi.nlm.nih.gov/17088085/) | Human TYK2 deficiency |
| S34 | [22723949](https://pubmed.ncbi.nlm.nih.gov/22723949/) | TYK2 kinase-dead mouse |
| S35 | [23359498](https://pubmed.ncbi.nlm.nih.gov/23359498/) | TYK2 I684S/P1104A functional study |
| S36 | [30578352](https://pubmed.ncbi.nlm.nih.gov/30578352/) | TYK2 P1104A and tuberculosis |
| S37 | [30423093](https://pubmed.ncbi.nlm.nih.gov/30423093/) | TYK2 P1104A molecular dynamics |
| S38 | [31961910](https://pubmed.ncbi.nlm.nih.gov/31961910/) | TYK2 splice/dosage alleles |
| S39 | [33260630](https://pubmed.ncbi.nlm.nih.gov/33260630/) | TYK2 variants in B-ALL |
| S40 | [34569645](https://pubmed.ncbi.nlm.nih.gov/34569645/) | TYK2 mutations and divergent phenotypes |
| S41 | [36094518](https://pubmed.ncbi.nlm.nih.gov/36094518/) | Inherited TYK2 deficiency and IL-23/IFN-gamma |
| S42 | [37695435](https://pubmed.ncbi.nlm.nih.gov/37695435/) | Complete TYK2 deficiency case |
| S43 | [42268925](https://pubmed.ncbi.nlm.nih.gov/42268925/) | TYK2 deep mutational scan |

## Important limitation

This is a **source matrix**, not a completed per-substitution evidence database. Several sources test numerous alleles, and the source abstract does not enumerate every variant or its score. For an allele-level matrix suitable for classification/model training, I must extract each study’s full-text tables and supplementary data (especially S01, S05–S09, S12, S21, S27, S29, S39–S43). I have deliberately used `Panel` rather than assigning unverified effects.
