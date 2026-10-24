# JAK3 variants: external data sources

Data retrieved 24-25 Oct 2026. All protein positions use the canonical JAK3 transcript (NM_000215 / ENST00000458235, UniProt P52333).
Tables: [`jak3_variants_inf.csv`](jak3_variants_inf.csv) (annotations), [`jak3_variants_inf_predict.csv`](jak3_variants_inf_predict.csv) (+ predictor scores), [`jak3_variants_inf_predict_ext.csv`](jak3_variants_inf_predict_ext.csv) (+ all dbNSFP scores).

JAK3 pairs with the common gamma chain (IL-2, IL-4, IL-7, IL-9, IL-15, IL-21 receptors). Biallelic loss of function causes T-B+NK- severe combined immunodeficiency (ClinGen: definitive, autosomal recessive; a ClinGen SCID expert panel specification exists). Somatic gain-of-function variants occur in T-ALL and NK/T-cell lymphoma.

## 1. Priority variants (top of each table)

| Variant | Domain | AlphaMissense | REVEL | CADD | ClinVar | gnomAD AF | cBioPortal patients |
|---|---|---|---|---|---|---|---|
| Y581C | JH2 | 0.0993 (likely benign) | 0.369 | 22.2 | - | 0.00E+000 | - |

## 2. Sources and what each gave

| # | Source | What it is | What we got | In the tables |
|---|---|---|---|---|
| 1 | ClinVar | Clinical variant classifications | 1439 records = 479 protein changes; 325 of uncertain significance; pathogenic or likely pathogenic: 103 (81 truncating or indel; missense: Y100C, R101G, R103C, R103H, R142C, D144V, C193Y, R350W, L369P, G397V, R402H, R403H, I430T, G528D, R582W, G589S, R651W, T714M, R775H, D784N, L875H, E1019K) | 7 ClinVar columns; one row per protein change |
| 2 | gnomAD v4 | Population frequencies (~800,000 people) | 7302 variants, 2282 protein-changing; pLI 0.00, LOEUF 0.87, missense Z 2.7 | 3 frequency columns plus `gnomAD` call (1 = probably benign: 29 variants) |
| 3 | cBioPortal | Tumour sequencing studies | 5924 calls from 340 studies, about 2691 patient-mutation pairs, 1482 protein changes | 3 columns, 201 rows filled |
| 4 | COSMIC v104 | Catalogue of somatic mutations in cancer | 2355 records from 1973 tumour samples, 847 protein changes; top missense: M511I (102), V722I (67), R657Q (59); 149 table rows matched | Not included in the public CSVs (COSMIC licence) |
| 5 | OncoKB | Expert cancer annotation | 12 curated alterations (8 gain-of-function); diagnostic level only (early T-cell precursor ALL); no therapeutic level | Not included in the public CSVs (OncoKB terms) |
| 6 | CIViC | Variant-drug evidence | 3 evidence items on 3 variants | `CIViC evidence` column |
| 7 | LOVD (shared) | Diagnostic-lab variant database | 163 entries | 2 columns, 43 rows filled |
| 8 | DECIPHER | Patients with developmental disorders | 1 open-access patient: Q39Sfs*108, homozygous, classified pathogenic (SCID); GenCC definitive, autosomal recessive | Column |
| 9 | AlphaMissense (AlphaFold DB) | Predicted pathogenicity, all 19 substitutions per position | 21356 substitutions | `AlphaMissense`, `AlphaMissense class` |
| 10 | dbNSFP (via myvariant.info) | Dozens of predictors per single-nucleotide change | 6898 protein changes reachable by one DNA change | 6 core scores (predict file), ~60 more (ext file) |
| 11 | ProteinGym | Variant-effect benchmark | Clinical set: 28 variants (14 pathogenic, 14 benign); no deep mutational scan | Not added |
| 12 | IntOGen | Cancer driver genes | Driver in 1 cancer type (acute lymphoblastic leukaemia) | Gene-level only |
| 13 | MaveDB | Deep mutational scan data | No JAK3 deep mutational scan | Not available |
| - | Dataset EV1 (Jeanpierre 2025) | Structural clusters | JAK1 only | `Cluster` left blank |
| - | HGMD | Literature disease variants | Not accessed (licence required) | - |

## 3. Main findings

1. **Two disease mechanisms.** Germline biallelic loss of function (SCID; many pathogenic ClinVar entries) and somatic gain of function in leukaemia/lymphoma (OncoKB: M511I, A572T, A573V, R657Q/W, V674A, V678M, L857Q).
2. **ProteinGym clinical set** has 28 JAK3 variants (14 pathogenic) - the best-labelled of the four JAK genes.
3. **Most frequent changes in tumours (cBioPortal patients):** M511I (36), V722I (23), R657Q (20), R403H (19), T8M (13), S44F (13).
4. **Common in the population (gnomAD AF >= 1E-04 or homozygotes):** V722I (9.75E-003), P151R (7.77E-003), P132T (4.56E-003), T8M (7.33E-004), R925S (6.33E-004), V718L (3.74E-004), A1090T (3.70E-004), R615C (3.55E-004). Such variants are unlikely to cause a fully penetrant dominant disease.

## 4. Columns

| Group | Columns |
|---|---|
| Curation | Variant, Domain (UniProt: FERM, SH2-like, JH2 = pseudokinase, JH1 = kinase), Cluster (blank: EV1 covers JAK1 only), Conclusions, Brief evidence, Reference, DRUG (blank, for curation) |
| Predictors (predict, ext) | AlphaMissense (> 0.564 likely pathogenic, < 0.34 likely benign), REVEL (>= 0.644 damaging), CADD phred (>= 25), SIFT (<= 0.05 damaging), PolyPhen-2 HVAR (> 0.909 probably damaging), MetaRNN (> 0.5), ESM1b (< -7.5) |
| dbNSFP (ext only) | `dbNSFP <tool>.score` / `.pred` for ~30 further predictors and conservation scores; `dbNSFP DNA change (hg19)` |
| CIViC | CIViC evidence (drug or functional claim, disease, evidence level A-E, review status, EID) |
| ClinVar | ClinVar, Review status, Condition, Last evaluated, Somatic clinical impact, ClinVar DNA change, ClinVar variation ID |
| gnomAD v4 | gnomAD allele count, gnomAD AF, gnomAD homozygotes, gnomAD (1 = probably benign, 2 = rare/absent, not informative) |
| cBioPortal | cBioPortal patients, cBioPortal studies, cBioPortal top cancer types |
| LOVD / DECIPHER | LOVD entries, LOVD reported effect, DECIPHER |

Rows are grouped by `SECTION:` header rows: priority variants, then ClinVar protein changes (sorted by position), then CIViC-only entries.

## 5. Methods notes

- Same pipeline as [JAK1](../JAK1/jak1_sources_summary.md); scripts query NCBI E-utilities, the gnomAD GraphQL API, the cBioPortal API, CIViC GraphQL, the LOVD shared API, AlphaFold DB and myvariant.info.
- **gnomAD call:** 1 if AF >= 1E-04 or at least one homozygote, else 2 (ACMG/AMP BS1 practice; no ClinGen threshold for this gene). A "2" is not evidence of pathogenicity. For recessive SCID, heterozygous carriers are expected in gnomAD, so frequency alone argues for benign only at higher frequencies (homozygotes are the stronger signal).
- **Predictors** score damaging versus tolerated; they cannot separate gain-of-function from loss-of-function.
- **dbNSFP** covers only substitutions reachable by a single DNA change (~1/3 of all 19-per-position substitutions); AlphaMissense covers all. Where two DNA changes give the same protein change, the most damaging core score is kept (ext file: values joined with ` | `).
- **cBioPortal:** patients deduplicated by patient ID across overlapping studies; "mixed" is the study-level label of pan-cancer cohorts.
