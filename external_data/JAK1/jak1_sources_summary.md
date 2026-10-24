# JAK1 variants: external data sources

Data retrieved 24 Oct 2026. All protein positions use the canonical JAK1 transcript (NM_002227 / ENST00000342505, UniProt P23458).
The per-variant table is in [`jak1_variants_inf.csv`](jak1_variants_inf.csv).

## 1. Sources and what each gave

| # | Source | What it is | What we got | Added to the table |
|---|---|---|---|---|
| 1 | Curated table (Sheet3) | Literature curation of JAK1 variants | 79 rows, 63 named variants | Starting point |
| 2 | Dataset EV1 (Jeanpierre et al. 2025, supplement) | Structural clusters for 21,926 JAK1 variants | Clusters for 27 "Pending lookup" variants; all 36 existing values confirmed | `Cluster` completed, also for new variants |
| 3 | ClinVar | Clinical variant classifications | 928 records = 396 protein changes; only 4 pathogenic or likely pathogenic (S703I, H596D, A634D, L783F) | 7 ClinVar columns; 370 new variant rows |
| 4 | gnomAD v4 | Population frequencies (~800,000 people) | 5,104 variants, 971 protein-changing; JAK1 very intolerant of loss of function (pLI = 1, LOEUF 0.18, missense Z 6.6) | 3 frequency columns plus `gnomAD` call (1 = probably benign: 15 variants) |
| 5 | cBioPortal | Tumour sequencing studies | 8,632 calls from 348 studies, about 4,000 patient-mutation pairs, 1,454 protein changes | 3 columns, 181 rows filled |
| 6 | COSMIC v104 | Catalogue of somatic mutations in cancer | 3,230 records from 2,558 tumour samples, 843 protein changes | Not included in the public CSV (COSMIC licence) |
| 7 | OncoKB | Expert cancer annotation | 18 curated variants (17 gain-of-function) plus the truncating class; no therapeutic levels for JAK1 | Not included in the public CSV (OncoKB terms) |
| 8 | CIViC | Variant-drug evidence | 16 evidence items on 11 variants, mostly preclinical or single case reports | `CIViC evidence` column; 9 new rows |
| 9 | LOVD (shared) | Diagnostic-lab variant database | 40 entries, all unclassified | 2 columns, 8 rows filled |
| 10 | DECIPHER | Patients with developmental disorders | 1 open-access sequence variant (M842V, de novo); ClinGen rates JAK1 to AIIDE as definitive | Gene-level only |
| 11 | ProteinGym | Variant-effect benchmark | No deep mutational scan of JAK1; clinical set has 10 JAK1 variants (2 pathogenic, 8 benign), all also in ClinVar | Not added |
| 12 | IntOGen | Cancer driver genes | JAK1 is a driver in 8 cancer types, mostly endometrial carcinoma | Gene-level only |
| 13 | StructMAn web server | Structural annotation | A634D is buried in the JH2 pseudokinase core at a JAK1 homodimer contact; the server does not score substitutions | Not added |
| 14 | MaveDB | Deep mutational scan data | TYK2: 11 datasets of about 23,700 variants each; JAK1: 1 small base-editing screen (24 variants) | Not added yet |
| - | HGMD | Literature disease variants | Not accessed (licence required) | - |

## 2. Main findings

1. **Few JAK1 variants are classified as pathogenic.** 93% of ClinVar protein changes are of uncertain significance.
2. **Some literature variants are too common to be strong disease causes.** V651M, R506C and N833S each have gnomAD AF of at least 1E-04 and homozygotes. A634D, H596D and S703I are absent from gnomAD.
3. **Two patterns in tumours.** Loss-of-function frameshifts dominate in endometrial and colorectal cancers (e.g. K860Nfs\*16). Gain-of-function missense variants cluster in haematological cancers (R724H, V658F, A634D) and liver cancer (S703I, L910P).
4. **Database drug evidence is weak.** JAK-inhibitor sensitivity is preclinical only; truncating variants are linked to anti-PD-1 resistance in case reports. The curated `DRUG` column (patient papers) has more.
5. **16 curated variants are in no database**, e.g. R879G, C787F, K908A, M1099I.

## 3. Columns in `jak1_variants_inf.csv`

| Group | Columns |
|---|---|
| Curation | Variant, Domain, Cluster (Dataset EV1), Conclusions, Brief evidence, Reference, DRUG |
| CIViC | CIViC evidence (drug or functional claim, disease, evidence level A-E, review status, EID) |
| ClinVar | ClinVar, Review status, Condition, Last evaluated, Somatic clinical impact, ClinVar DNA change (NM_002227), ClinVar variation ID |
| gnomAD v4 | gnomAD allele count, gnomAD AF, gnomAD homozygotes, gnomAD (1 = probably benign, 2 = rare/absent, not informative) |
| cBioPortal | cBioPortal patients, cBioPortal studies, cBioPortal top cancer types |
| LOVD / DECIPHER | LOVD entries, LOVD reported effect, DECIPHER |

Rows are grouped by `SECTION:` header rows: the original curated sections, then ClinVar-only protein variants, then CIViC-only entries.

## 4. Methods notes

- **gnomAD call:** 1 if AF >= 1E-04 or at least one homozygote, else 2. This follows ACMG/AMP BS1 practice for rare dominant disease (Richards et al. 2015; Whiffin et al. 2017). There is no ClinGen expert-panel threshold for JAK1. A "2" is not evidence of pathogenicity.
- **cBioPortal:** patients were deduplicated by patient ID across overlapping studies. "mixed" is the study-level label of pan-cancer cohorts.
- **ClinVar:** matched by protein change. Where one protein change has several DNA-level records, values are joined with ` | `.
- **Dataset EV1:** cluster assignments from Jeanpierre et al. 2025, supplementary Dataset EV1 (21,926 JAK1 variants in two clusters).
