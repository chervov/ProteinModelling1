# ABCB1 — variant-effect analysis

*ATP-dependent translocase ABCB1* · UniProt `P08183` · 1280 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 51–357 | 307 |
| ABC transporter 1 | 392–628 | 237 |
| ABC transmembrane type-1 2 | 711–1000 | 290 |
| ABC transporter 2 | 1035–1273 | 239 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **14.97 Å**, intra-module **4.38 Å**, **ratio 3.42**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 44.4 | 0 | 100% / 100% |
| SWISSMODEL_6s7p-1-A_36-1252 | 28.0 | 78 | 100% / 91% |
| SWISSMODEL_9ctc-1-A_30-1272 | 34.4 | 15 | 100% / 100% |
| SWISSMODEL_9oe2-1-A_30-1276 | 62.2 | 0 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `ABCB1_P08183_SWISSMODEL_6s7p-1-A_36-1252.pdb`, centroid distance **28.0 Å**, **78 residue pairs** in contact within 5 Å.

**Domain A interface residues (36):** `403, 404, 407, 427, 428, 429, 430, 475, 476, 477, 515, 516, 517, 522, 523, 527, 530, 531, 532, 533, 534, 535, 536, 538, 556, 559, 560, 561, 562, 563, 565, 566, 587, 588, 625, 628`

**Domain B interface residues (38):** `1046, 1047, 1049, 1050, 1070, 1071, 1072, 1073, 1118, 1119, 1120, 1121, 1157, 1161, 1162, 1167, 1168, 1172, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1201, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1212, 1232`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,406 | 22,914 | 0.969 | 0.653 | 1.8e-181 |
| ESM-1v | 1,406 | 22,914 | -12.965 | -8.179 | 1.3e-211 |
| FoldX ΔΔG | 1,406 | 21,223 | 0.562 | 1.184 | 1.7e-30 |
| ThermoMPNN ΔΔG | 1,406 | 22,914 | 0.575 | 0.73 | 1.3e-10 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 24,320 |
| ESM-1v | 24,320 |
| FoldX ΔΔG (ProtVar) | 22,629 |
| ThermoMPNN ΔΔG | 24,320 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.847 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.452 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.512 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.430 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.513 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.661 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| other | 103 |
| VUS | 23 |
| likely_benign | 5 |
| benign | 3 |
| pathogenic | 1 |
| likely_pathogenic | 1 |
| conflict | 1 |

**gnomAD r4 missense variants mapped:** 1,459

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 22,629** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 11,535 | 11,094 |
| mean AlphaMissense | 0.378 | 0.912 |
| mean ESM-1v | 6.112 | 12.434 |
| mean FoldX ΔΔG | 0.609 | 4.13 |
| mean ThermoMPNN ΔΔG | 0.404 | 1.516 |
| **fraction seen in gnomAD** | **8.48%** (978) | **3.31%** (367) |
| fraction at the interface | 3.42% | 9.12% |

**Validation:** the damaging cluster is **depleted** in the population — 3.31% of it appears in gnomAD against 8.48% of the tolerant cluster (a 2.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

## 6. ProteinGym

**Absent** from the 217 ProteinGym DMS substitution assays, so no published experimental variant data and no precomputed baselines for this protein.

## 7. Sources

| value | source |
|---|---|
| FoldX ΔΔG, pLDDT | EBI ProtVar, FoldX v5 on AlphaFold2, 208,792,558 rows (`external_data/protvar_foldx_jak_src.csv` for the JAKs) |
| ThermoMPNN ΔΔG, ESM-1v, AlphaMissense, RASA, pLDDT, secondary structure, disorder, ClinVar | Liao & Lehner 2026, Zenodo 18386427 |
| gnomAD allele frequencies | gnomAD r4 GraphQL API, missense with HGVS protein notation |
| domain boundaries | UniProt |
| structures | AlphaFold DB v6, SWISS-MODEL Repository, RCSB PDB, ModelArchive |
| interface contacts | `more_proteins/interface.py` (heavy atoms within 5 Å) |
| ProteinGym membership | `reference_files/DMS_substitutions.csv`, 217 assays |

### Caveats carried from the method work

- **ΔΔG magnitudes are unreliable**; ranks are usable. FoldX and ThermoMPNN disagree by a factor of ~40 on the equilibrium shift for a single variant (`PTPN2/jeanpierre2024_variant_analysis.md` §2.1b).
- **ΔΔG is a mechanism channel, not a pathogenicity score** — ρ ≈ 0.26–0.28 against DMS data against ≈ 0.35–0.40 for sequence predictors (`external_data/ddg_study.md` §5).
- **A ΔΔG near zero with AlphaMissense near 1 identifies a functional-site variant** with no structural cost — the PTPN2 C216S pattern.
- **Interface residues come from the most compact structure available.** Where that is an AlphaFold model rather than an experiment, the interface is predicted, not observed.
