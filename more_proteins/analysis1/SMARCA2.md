# SMARCA2 — variant-effect analysis

*SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 2* · UniProt `P51531` · 1590 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| QLQ | 173–208 | 36 |
| HSA | 436–508 | 73 |
| Helicase ATP-binding | 736–901 | 166 |
| Helicase C-terminal | 1054–1216 | 163 |
| Bromo | 1378–1506 | 129 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **8.66 Å**, intra-module **5.08 Å**, **ratio 1.7**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 28.5 | 31 | 100% / 100% |
| 9rl4.1.I (78.7% id) | 33.7 | 16 | 100% / 100% |
| 9rn1.1.I (78.7% id) | 30.2 | 23 | 100% / 100% |
| 7egp.1.H (47.5% id) | 26.3 | 61 | 100% / 100% |
| 7y8r.1.J (78.7% id) | 26.2 | 51 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P51531_7egp-1-H.pdb`, centroid distance **26.3 Å**, **61 residue pairs** in contact within 5 Å.

**Domain A interface residues (27):** `750, 751, 752, 753, 781, 782, 783, 784, 786, 787, 790, 791, 805, 806, 807, 852, 854, 855, 880, 881, 882, 883, 884, 885, 886, 887, 888`

**Domain B interface residues (29):** `1101, 1102, 1105, 1106, 1109, 1110, 1127, 1128, 1129, 1131, 1132, 1133, 1134, 1148, 1149, 1150, 1151, 1154, 1155, 1158, 1159, 1161, 1162, 1163, 1191, 1194, 1195, 1198, 1199`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,064 | 29,146 | 0.998 | 0.88 | 1.1e-222 |
| ESM-1v | 1,064 | 29,146 | -15.169 | -6.245 | <1e-300 |
| FoldX ΔΔG | 1,064 | 19,475 | 0.855 | 0.711 | 0.025 |
| ThermoMPNN ΔΔG | 1,064 | 29,146 | 0.575 | 0.232 | 1.4e-38 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 30,210 |
| ESM-1v | 30,210 |
| FoldX ΔΔG (ProtVar) | 20,539 |
| ThermoMPNN ΔΔG | 30,210 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.567 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.390 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.463 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.405 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.405 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.665 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 229 |
| likely_benign | 62 |
| likely_pathogenic | 53 |
| pathogenic | 38 |
| conflict | 21 |
| benign | 15 |

**gnomAD r4 missense variants mapped:** 1,613

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 20,539** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 14,049 | 6,490 |
| mean AlphaMissense | 0.768 | 0.987 |
| mean ESM-1v | 6.503 | 13.136 |
| mean FoldX ΔΔG | 0.401 | 3.928 |
| mean ThermoMPNN ΔΔG | 0.315 | 1.702 |
| **fraction seen in gnomAD** | **4.61%** (648) | **1.17%** (76) |
| fraction at the interface | 2.80% | 10.32% |

**Validation:** the damaging cluster is **depleted** in the population — 1.17% of it appears in gnomAD against 4.61% of the tolerant cluster (a 3.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 28 pathogenic / 0 benign, cluster 0 has 10 / 5; OR = inf, p = 0.0031.

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
