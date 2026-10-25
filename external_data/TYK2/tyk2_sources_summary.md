# TYK2 variants: external data sources

Data retrieved 24-25 Oct 2026. All protein positions use the canonical TYK2 transcript (NM_003331 / ENST00000525621, UniProt P29597).
Tables: [`tyk2_variants_inf.csv`](tyk2_variants_inf.csv) (annotations), [`tyk2_variants_inf_predict.csv`](tyk2_variants_inf_predict.csv) (+ predictor scores), [`tyk2_variants_inf_predict_ext.csv`](tyk2_variants_inf_predict_ext.csv) (+ all dbNSFP scores).

TYK2 transduces type I interferon, IL-12 and IL-23 signalling. Biallelic loss of function causes immunodeficiency 35 (autosomal recessive). The JH2 pseudokinase is the target of the allosteric inhibitor deucravacitinib.

## 1. Priority variants (top of each table)

| Variant | Domain | DMS signalling | DMS abundance | AlphaMissense | REVEL | CADD | ClinVar | gnomAD AF | cBioPortal patients |
|---|---|---|---|---|---|---|---|---|---|
| V678M | JH2 | 0.29 | 0.002 | 0.3054 (likely benign) | 0.564 | 31 | Uncertain significance | 0.00E+000 | 1 |
| P982A | JH1 | -0.466 | -0.23 | 0.526 (ambiguous) | 0.702 | 27.9 | - | - | - |

## 2. Sources and what each gave

| # | Source | What it is | What we got | In the tables |
|---|---|---|---|---|
| 1 | ClinVar | Clinical variant classifications | 1183 records = 529 protein changes; 449 of uncertain significance; pathogenic or likely pathogenic: 32 (30 truncating or indel; missense: L757V, L1014P) | 7 ClinVar columns |
| 2 | gnomAD v4 | Population frequencies (~800,000 people) | 7371 variants, 2103 protein-changing; pLI 0.00, LOEUF 0.61, missense Z 2.5 | 3 frequency columns plus `gnomAD` call (1 = probably benign: 50 variants); 2029 rows |
| 3 | cBioPortal | Tumour sequencing studies | 1959 calls from 224 studies, about 1288 patient-mutation pairs, 768 protein changes | 3 columns, 731 rows filled |
| 4 | COSMIC v104 | Catalogue of somatic mutations in cancer | 3682 records from 3341 tumour samples, 467 protein changes; top missense: V362F (32), P553H (6), A928V (6); 467 table rows matched | Not included in the public CSVs (COSMIC licence) |
| 5 | OncoKB | Expert cancer annotation | 7 curated alterations (6 gain-of-function); diagnostic level only (TYK2 fusions in BCR-ABL1-like B-ALL); no therapeutic level | Not included in the public CSVs (OncoKB terms) |
| 6 | CIViC | Variant-drug evidence | 2 evidence items on 2 variants | `CIViC evidence` column |
| 7 | LOVD (shared) | Diagnostic-lab variant database | 116 entries | 2 columns, 42 rows filled |
| 8 | DECIPHER | Patients with developmental disorders | No open-access sequence variants (20 copy-number variants); GenCC strong, autosomal recessive | Gene-level only |
| 9 | AlphaMissense (AlphaFold DB) | Predicted pathogenicity, all 19 substitutions per position | 22553 substitutions | `AlphaMissense`, `AlphaMissense class` |
| 10 | dbNSFP (via myvariant.info) | Dozens of predictors per single-nucleotide change | 7190 protein changes reachable by one DNA change | 6 core scores (predict file), ~60 more (ext file) |
| 11 | ProteinGym | Variant-effect benchmark | Not in the clinical set; no deep mutational scan | Not added |
| 12 | IntOGen | Cancer driver genes | Not detected as a cancer driver | Gene-level only |
| 13 | MaveDB | Deep mutational scan data | **Deep mutational scan available** (Deep mutational scanning reveals pharmacologically relevant insights into TYK2 signaling and disease, bioRxiv 2025, doi:10.1101/2025.10.11.681520): IFN-alpha signalling (~23,700 variants; also with allosteric inhibitors BMS-986202 and NDI-034858) and VAMP-seq abundance | 2 DMS columns |
| 14 | OMIM (MIM 176941) | Curated, literature-backed disease variants | 12 allelic variants (7 with a simple protein change) | `OMIM allelic variant` column |
| - | Dataset EV1 (Jeanpierre 2025) | Structural clusters | JAK1 only | `Cluster` left blank |
| - | HGMD | Literature disease variants | Not accessed (licence required) | - |

## 3. Main findings

1. **Experimental data exist for almost every substitution.** The DMS signalling and abundance columns give measured effects (negative = loss of function), which outrank the computational predictors.
2. **TYK2 is not a cancer driver** (IntOGen) and has few curated cancer variants; the main clinical relevance is recessive immunodeficiency and common partial loss-of-function alleles in autoimmunity.
3. **Most frequent changes in tumours (cBioPortal patients):** T1106Hfs*5 (20), T1106Rfs*7 (18), R1027H (11), R224W (8), V362F (8), G422S (8).
4. **Common in the population (gnomAD AF >= 1E-04 or homozygotes):** V362F (2.76E-001), I684S (7.97E-002), G363S (7.03E-002), P1104A (3.71E-002), A53T (9.29E-003), A928V (6.35E-003), E1163G (3.88E-003), R703W (2.98E-003). Such variants are unlikely to cause a fully penetrant dominant disease.

## 4. Columns

| Group | Columns |
|---|---|
| Curation | Variant, Domain (UniProt: FERM, SH2-like, JH2 = pseudokinase, JH1 = kinase), Cluster (blank: EV1 covers JAK1 only), Conclusions, Brief evidence, Reference, DRUG (blank, for curation) |
| MaveDB DMS | DMS signalling (IFN-a 100U/mL): log2 fold change vs WT of IFN-alpha-induced signalling (negative = loss of function, positive = gain); DMS abundance (VAMP-seq): protein abundance vs WT (negative = less stable) |
| Predictors (predict, ext) | AlphaMissense (> 0.564 likely pathogenic, < 0.34 likely benign), REVEL (>= 0.644 damaging), CADD phred (>= 25), SIFT (<= 0.05 damaging), PolyPhen-2 HVAR (> 0.909 probably damaging), MetaRNN (> 0.5), ESM1b (< -7.5) |
| dbNSFP (ext only) | `dbNSFP <tool>.score` / `.pred` for ~30 further predictors and conservation scores; `dbNSFP DNA change (hg19)` |
| CIViC | CIViC evidence (drug or functional claim, disease, evidence level A-E, review status, EID) |
| ClinVar | ClinVar, Review status, Condition, Last evaluated, Somatic clinical impact, ClinVar DNA change, ClinVar variation ID |
| gnomAD v4 | gnomAD allele count, gnomAD AF, gnomAD homozygotes, gnomAD (1 = probably benign, 2 = rare/absent, not informative) |
| cBioPortal | cBioPortal patients, cBioPortal studies, cBioPortal top cancer types |
| LOVD / DECIPHER | LOVD entries, LOVD reported effect, DECIPHER |

| Provenance | Seen in (which public sources report the variant) |

Rows (2510 variants in the public files) are grouped by `SECTION:` header rows: priority variants, then ClinVar protein changes, then all other protein changes observed in gnomAD, cBioPortal, LOVD, CIViC or DECIPHER (both sorted by position). Variants known only from COSMIC or OncoKB are kept in the local tables but left out of the public files.

## 5. Methods notes

- Same pipeline as [JAK1](../JAK1/jak1_sources_summary.md); scripts query NCBI E-utilities, the gnomAD GraphQL API, the cBioPortal API, CIViC GraphQL, the LOVD shared API, AlphaFold DB and myvariant.info.
- **gnomAD call:** 1 if AF >= 1E-04 or at least one homozygote, else 2 (ACMG/AMP BS1 practice; no ClinGen threshold for this gene). A "2" is not evidence of pathogenicity. For a recessive disorder, heterozygous carriers are expected in gnomAD; homozygotes are the stronger benign signal.
- **Predictors** score damaging versus tolerated; they cannot separate gain-of-function from loss-of-function.
- **dbNSFP** covers only substitutions reachable by a single DNA change (~1/3 of all 19-per-position substitutions); AlphaMissense covers all. Where two DNA changes give the same protein change, the most damaging core score is kept (ext file: values joined with ` | `).
- **cBioPortal:** patients deduplicated by patient ID across overlapping studies; "mixed" is the study-level label of pan-cancer cohorts.
