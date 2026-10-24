# JAK2 variants: external data sources

Data retrieved 24-25 Oct 2026. All protein positions use the canonical JAK2 transcript (NM_004972 / ENST00000381652, UniProt O60674).
Tables: [`jak2_variants_inf.csv`](jak2_variants_inf.csv) (annotations), [`jak2_variants_inf_predict.csv`](jak2_variants_inf_predict.csv) (+ predictor scores), [`jak2_variants_inf_predict_ext.csv`](jak2_variants_inf_predict_ext.csv) (+ all dbNSFP scores).

JAK2 is the main kinase downstream of EPO, TPO and GM-CSF receptors. Germline and somatic gain-of-function variants (V617F above all) drive myeloproliferative neoplasms; OMIM links JAK2 to thrombocythemia 3, familial erythrocytosis, polycythemia vera (somatic), myelofibrosis, AML and Budd-Chiari syndrome.

## 1. Priority variants (top of each table)

| Variant | Domain | AlphaMissense | REVEL | CADD | ClinVar | gnomAD AF | cBioPortal patients |
|---|---|---|---|---|---|---|---|
| V1110E | JH1 | 0.2891 (likely benign) | 0.477 | 23 | - | - | - |
| G571R | JH2 | 0.2686 (likely benign) | 0.874 | 33 | - | 6.58E-006 | - |
| V578I | JH2 | 0.2368 (likely benign) | 0.618 | 29.3 | - | 6.86E-007 | - |
| L805I | JH2 | 0.1504 (likely benign) | 0.439 | 25.6 | - | 1.04E-005 | 1 |

## 2. Sources and what each gave

| # | Source | What it is | What we got | In the tables |
|---|---|---|---|---|
| 1 | ClinVar | Clinical variant classifications | 828 records = 361 protein changes; 319 of uncertain significance; pathogenic or likely pathogenic: 7 (0 truncating or indel; missense: K539L, K607N, V617F, V617I, R867Q, R938Q, P1095L) | 7 ClinVar columns; one row per protein change |
| 2 | gnomAD v4 | Population frequencies (~800,000 people) | 6809 variants, 2197 protein-changing; pLI 0.00, LOEUF 0.74, missense Z -0.7 | 3 frequency columns plus `gnomAD` call (1 = probably benign: 26 variants) |
| 3 | cBioPortal | Tumour sequencing studies | 6189 calls from 331 studies, about 3223 patient-mutation pairs, 1346 protein changes | 3 columns, 134 rows filled |
| 4 | COSMIC v104 | Catalogue of somatic mutations in cancer | 55799 records from 54775 tumour samples, 831 protein changes; top missense: V617F (49426), R683G (115), V617I (89); 107 table rows matched | Not included in the public CSVs (COSMIC licence) |
| 5 | OncoKB | Expert cancer annotation | 38 curated alterations (19 gain-of-function); highest therapeutic level 4 (JAK2 fusions / PCM1-JAK2: ruxolitinib, fedratinib); 14 alterations annotated as JAK-inhibitor resistance | Not included in the public CSVs (OncoKB terms) |
| 6 | CIViC | Variant-drug evidence | 12 evidence items on 7 variants | `CIViC evidence` column |
| 7 | LOVD (shared) | Diagnostic-lab variant database | 88 entries | 2 columns, 24 rows filled |
| 8 | DECIPHER | Patients with developmental disorders | No open-access sequence variants (256 copy-number variants); GenCC strong/moderate, autosomal dominant; pGOF 0.63 | Gene-level only |
| 9 | AlphaMissense (AlphaFold DB) | Predicted pathogenicity, all 19 substitutions per position | 21508 substitutions | `AlphaMissense`, `AlphaMissense class` |
| 10 | dbNSFP (via myvariant.info) | Dozens of predictors per single-nucleotide change | 7114 protein changes reachable by one DNA change | 6 core scores (predict file), ~60 more (ext file) |
| 11 | ProteinGym | Variant-effect benchmark | Clinical set: 14 variants (2 pathogenic, 12 benign); no deep mutational scan | Not added |
| 12 | IntOGen | Cancer driver genes | Driver in 5 cancer types (breast, non-small-cell lung, AML, ALL, bladder) | Gene-level only |
| 13 | MaveDB | Deep mutational scan data | No JAK2 deep mutational scan | Not available |
| - | Dataset EV1 (Jeanpierre 2025) | Structural clusters | JAK1 only | `Cluster` left blank |
| - | HGMD | Literature disease variants | Not accessed (licence required) | - |

## 3. Main findings

1. **Gain-of-function is the key mechanism.** OncoKB annotates 26 oncogenic alterations (V617F, exon 12 changes, R683 substitutions, fusions, amplification).
2. **JAK2 tolerates loss of function in the population** (pLI 0.00, LOEUF 0.74; missense Z -0.7), consistent with disease by gain rather than loss of function.
3. **Most frequent changes in tumours (cBioPortal patients):** V617F (880), R683G (20), R1113H (18), R564Q (15), R234H (13), R683S (11).
4. **Common in the population (gnomAD AF >= 1E-04 or homozygotes):** L393V (6.47E-003), R1063H (5.39E-003), N1108S (3.28E-003), L113V (9.38E-004), E846D (8.55E-004), D1096E (6.69E-004), G127D (5.17E-004), G571S (3.55E-004). Such variants are unlikely to cause a fully penetrant dominant disease.

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
- **gnomAD call:** 1 if AF >= 1E-04 or at least one homozygote, else 2 (ACMG/AMP BS1 practice; no ClinGen threshold for this gene). A "2" is not evidence of pathogenicity. **Caution for JAK2:** somatic clonal haematopoiesis (e.g. V617F) can make tumour-type variants appear in gnomAD blood-derived samples, so gnomAD frequency is less reliable for this gene.
- **Predictors** score damaging versus tolerated; they cannot separate gain-of-function from loss-of-function.
- **dbNSFP** covers only substitutions reachable by a single DNA change (~1/3 of all 19-per-position substitutions); AlphaMissense covers all. Where two DNA changes give the same protein change, the most damaging core score is kept (ext file: values joined with ` | `).
- **cBioPortal:** patients deduplicated by patient ID across overlapping studies; "mixed" is the study-level label of pan-cancer cohorts.
