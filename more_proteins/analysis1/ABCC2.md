# ABCC2 — variant-effect analysis

*ATP-binding cassette sub-family C member 2* · UniProt `Q92887` · 1545 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 322–605 | 284 |
| ABC transporter 1 | 637–861 | 225 |
| ABC transmembrane type-1 2 | 979–1264 | 286 |
| ABC transporter 2 | 1300–1534 | 235 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **14.86 Å**, intra-module **5.06 Å**, **ratio 2.94**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.1 | 6 | 100% / 100% |
| SWISSMODEL_7w4o-1-H_24-1530 | 27.7 | 40 | 100% / 98% |
| SWISSMODEL_8rq3-1-A_2-1534 | 49.5 | 0 | 100% / 100% |
| SWISSMODEL_9dw9-1-A_192-1535 | 27.6 | 63 | 100% / 100% |
| SWISSMODEL_9jn1-1-A_1-1516 | 46.6 | 0 | 100% / 92% |

## 2. The inter-domain interface

Most compact structure: `ABCC2_Q92887_SWISSMODEL_9dw9-1-A_192-1535.pdb`, centroid distance **27.6 Å**, **63 residue pairs** in contact within 5 Å.

**Domain A interface residues (30):** `671, 672, 673, 674, 706, 738, 741, 742, 747, 757, 760, 762, 763, 764, 765, 766, 768, 786, 789, 790, 791, 792, 793, 794, 795, 797, 820, 821, 822, 823`

**Domain B interface residues (27):** `1310, 1314, 1334, 1335, 1336, 1337, 1382, 1383, 1418, 1438, 1439, 1440, 1441, 1462, 1465, 1466, 1467, 1468, 1470, 1471, 1493, 1495, 1527, 1528, 1530, 1531, 1533`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,083 | 28,272 | 0.913 | 0.482 | 7e-138 |
| ESM-1v | 1,083 | 28,272 | -11.918 | -6.15 | 1.1e-223 |
| FoldX ΔΔG | 1,083 | 25,973 | 0.751 | 1.102 | 2.3e-11 |
| ThermoMPNN ΔΔG | 1,083 | 28,272 | 0.563 | 0.683 | 9.6e-08 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 29,355 |
| ESM-1v | 29,355 |
| FoldX ΔΔG (ProtVar) | 27,056 |
| ThermoMPNN ΔΔG | 29,355 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.748 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.469 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.512 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.385 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.448 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.663 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 190 |
| conflict | 31 |
| likely_benign | 14 |
| benign | 6 |
| likely_pathogenic | 5 |
| pathogenic | 4 |

**gnomAD r4 missense variants mapped:** 1,952

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 27,056** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 15,917 | 11,139 |
| mean AlphaMissense | 0.329 | 0.867 |
| mean ESM-1v | 5.11 | 10.712 |
| mean FoldX ΔΔG | 0.608 | 3.707 |
| mean ThermoMPNN ΔΔG | 0.465 | 1.653 |
| **fraction seen in gnomAD** | **8.32%** (1,324) | **4.26%** (475) |
| fraction at the interface | 2.27% | 6.48% |

**Validation:** the damaging cluster is **depleted** in the population — 4.26% of it appears in gnomAD against 8.32% of the tolerant cluster (a 2.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 3 pathogenic / 0 benign, cluster 0 has 1 / 5; OR = inf, p = 0.048.

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
