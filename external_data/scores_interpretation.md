# How to read the scores in the variant tables

Applies to all gene folders (`JAK1/`, `JAK2/`, `JAK3/`, `TYK2/`): `*_variants_inf.csv`, `*_variants_inf_predict.csv`, `*_variants_inf_predict_ext.csv`.

## 1. Prediction scores (`_predict` and `_ext` files)

| Score | Range | Damaging | Uncertain | Tolerated / benign | Direction |
|---|---|---|---|---|---|
| **AlphaMissense** | 0-1 | **> 0.564** (likely pathogenic) | 0.34-0.564 (ambiguous) | < 0.34 (likely benign) | higher = worse |
| **REVEL** | 0-1 | **>= 0.644** (>= 0.773 stronger, >= 0.932 strongest) | 0.29-0.644 | <= 0.29 | higher = worse |
| **CADD phred** | 0-~50 | **>= 25** (>= 30 = top 0.1% of all genome changes) | 20-25 | < 20 | higher = worse |
| **SIFT** | 0-1 | **<= 0.05** | - | > 0.05 | **lower = worse** |
| **PolyPhen-2 HVAR** | 0-1 | **> 0.909** (probably damaging) | 0.447-0.909 (possibly damaging) | < 0.447 (benign) | higher = worse |
| **MetaRNN** | 0-1 | **> 0.5** | - | < 0.5 | higher = worse |
| **ESM1b** | negative log-likelihood ratio | **< -7.5** | - | > -7.5 (closer to 0 = tolerated) | **lower = worse** |

Example (JAK1 A634D): AlphaMissense 0.72, REVEL 0.70, CADD 29.9, SIFT 0.001, PolyPhen-2 0.999, MetaRNN 0.92, ESM1b -9.6 - all damaging.

**How to use them**

1. **Look for agreement.** Most tools agreeing is more convincing than any single score.
2. **REVEL and AlphaMissense are the most reliable.** REVEL thresholds are calibrated by ClinGen (Pejaver et al. 2022). SIFT and PolyPhen-2 are older and call many variants damaging.
3. **In ACMG/AMP terms predictions are weak evidence:** a damaging consensus is PP3 (supporting pathogenic), a benign one BP4 (supporting benign). Only very high calibrated REVEL scores count for more.
4. **They cannot separate gain- from loss-of-function.** "Damaging" means the change disrupts the protein; for JAKs that can mean overactive (JAK1 A634D, JAK2 V617F) or inactive (JAK1 K908A).
5. **Population and experimental data outrank predictions.** Example: JAK1 V651M is "damaging" by several tools but common in gnomAD with homozygotes.
6. **Coverage differs.** dbNSFP scores (REVEL, CADD, SIFT, PolyPhen-2, MetaRNN, ESM1b, all `dbNSFP ...` columns) exist only for substitutions reachable by one DNA change (~1/3 of the 19 per position). AlphaMissense covers all 19.

AlphaMissense and SIFT/PolyPhen-2 cut-offs are the tools' published defaults; the CADD cut-off of ~25 approximates ClinGen's calibration.

## 2. Population frequency (gnomAD v4)

| Column | Meaning |
|---|---|
| `gnomAD allele count` | Copies of the variant seen in ~800,000 people (2 copies per person) |
| `gnomAD AF` | Allele count / allele number (copies sequenced at that position, up to ~1.6 million). `1.00E-004` = 1 in 10,000 copies |
| `gnomAD homozygotes` | People carrying the variant on both copies |
| `gnomAD` | **1** = probably benign (AF >= 1E-04 **or** >= 1 homozygote); **2** = rare or absent (not informative) |

- Basis: ACMG/AMP BS1 ("frequency greater than expected for the disorder"), which must be set per disease (Richards et al. 2015; Whiffin et al. 2017). ClinGen expert panels use values of this order for rare dominant disorders; none exists for the JAK genes, so 1E-04 is a conservative choice.
- **A "2" is not evidence of pathogenicity.** Most rare variants are benign (ClinGen downgraded PM2 to supporting).
- **Recessive disorders** (JAK3 SCID, TYK2 immunodeficiency 35): heterozygous carriers are expected in gnomAD; homozygotes are the stronger benign signal.
- **Clonal haematopoiesis** (especially JAK2 V617F) can put somatic variants into gnomAD blood samples.

## 3. Experimental data

| Column | Where | Meaning |
|---|---|---|
| `Cluster` | JAK1 only | Structural cluster 1 or 2 from Jeanpierre et al. 2025, Dataset EV1. Cluster 2 is enriched for variants with functional effects but does **not** by itself mean gain-of-function (the kinase-dead K908A is cluster 2). Blank where not applicable |
| `DMS signalling (IFN-a 100U/mL)` | TYK2 only | Deep mutational scan (MaveDB urn:mavedb:00001270-a-6): log2 fold change vs wild type of the IFN-alpha response (stimulated minus unstimulated). **Negative = loss of function**, positive = more signalling. Stop codons score strongly negative (e.g. V678* -1.64, G1051* -2.43). Compare with the standard error; differences within about 2 SE of 0 are not clearly different from wild type. Because the score is a stimulated-minus-baseline contrast, constitutively active variants may not score high (TYK2 V678F, the JAK2 V617F equivalent, scores -0.12) |
| `DMS abundance (VAMP-seq)` | TYK2 only | Protein abundance vs wild type (MaveDB urn:mavedb:00001271-a-1). **Negative = less stable / lower abundance**; ~0 = like wild type |

## 4. Clinical and cancer annotations

| Column | How to read |
|---|---|
| `ClinVar` | Pathogenic / Likely pathogenic / Uncertain significance (VUS) / Likely benign / Benign / Conflicting. Values for several DNA-level records of the same protein change are joined with ` \| ` |
| `Review status` | Strength of the ClinVar call, strongest first: practice guideline > reviewed by expert panel > criteria provided, multiple submitters, no conflicts > criteria provided, single submitter > no assertion criteria provided (weakest) |
| `Somatic clinical impact` | ClinVar somatic tiers (Tier I strong, Tier II potential clinical significance) |
| `cBioPortal patients` | Distinct tumour patients carrying the change. Recurrence across many patients suggests a hotspot; "mixed" = pan-cancer cohort label |
| `CIViC evidence` | Evidence level A (validated) > B (clinical) > C (case study) > D (preclinical) > E (inferential); "accepted" entries are curator-reviewed, "submitted" are not |
| `LOVD reported effect` | Submitter's call (e.g. functionProbablyNotAffected); most entries are unclassified |

## 5. Putting it together

| Evidence | Points to benign | Points to pathogenic |
|---|---|---|
| Population | gnomAD = 1 (common or homozygotes) | absent / very rare (weak) |
| Experiment | DMS ~0, normal reporter assays | DMS strongly negative (LoF) or functional gain in assays |
| Prediction | consensus tolerated (BP4) | consensus damaging (PP3) |
| Clinical | ClinVar benign, well reviewed | ClinVar pathogenic, well reviewed; recurrent in patients |

No single column decides. Strong experimental or segregation evidence outweighs predictions, and frequency can rule a variant out but never in.
