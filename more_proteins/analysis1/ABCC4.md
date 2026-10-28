# ABCC4 — variant-effect analysis

*ATP-binding cassette sub-family C member 4* · UniProt `O15439` · 1325 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 93–377 | 285 |
| ABC transporter 1 | 410–633 | 224 |
| ABC transmembrane type-1 2 | 711–1005 | 295 |
| ABC transporter 2 | 1041–1274 | 234 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **18.03 Å**, intra-module **5.16 Å**, **ratio 3.49**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 38.5 | 1 | 100% / 100% |
| SWISSMODEL_8i4a-1-A_9-1298 | 50.3 | 0 | 100% / 100% |
| SWISSMODEL_8swn-1-A_47-1298 | 27.5 | 60 | 100% / 100% |
| SWISSMODEL_9dw9-1-A_9-1266 | 28.0 | 50 | 100% / 97% |
| SWISSMODEL_9y1q-1-A_53-1265 | 70.2 | 0 | 100% / 96% |

## 2. The inter-domain interface

Most compact structure: `ABCC4_O15439_SWISSMODEL_8swn-1-A_47-1298.pdb`, centroid distance **27.5 Å**, **60 residue pairs** in contact within 5 Å.

**Domain A interface residues (26):** `445, 446, 447, 448, 480, 481, 512, 515, 516, 519, 521, 536, 537, 538, 539, 540, 542, 560, 563, 564, 565, 566, 567, 569, 592, 594`

**Domain B interface residues (26):** `1055, 1075, 1076, 1077, 1078, 1122, 1123, 1124, 1178, 1179, 1180, 1181, 1182, 1184, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1233, 1234, 1248, 1249, 1272`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 988 | 24,187 | 0.947 | 0.565 | 9.5e-136 |
| ESM-1v | 988 | 24,187 | -12.806 | -8.567 | 1.2e-145 |
| FoldX ΔΔG | 988 | 22,420 | 0.796 | 1.194 | 2.3e-05 |
| ThermoMPNN ΔΔG | 988 | 24,187 | 0.57 | 0.728 | 1.1e-07 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 25,175 |
| ESM-1v | 25,175 |
| FoldX ΔΔG (ProtVar) | 23,408 |
| ThermoMPNN ΔΔG | 25,175 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.848 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.487 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.511 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.449 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.522 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.678 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 30 |
| benign | 4 |
| likely_benign | 2 |

**gnomAD r4 missense variants mapped:** 1,579

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 23,408** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 12,097 | 11,311 |
| mean AlphaMissense | 0.325 | 0.877 |
| mean ESM-1v | 6.44 | 12.396 |
| mean FoldX ΔΔG | 0.551 | 3.744 |
| mean ThermoMPNN ΔΔG | 0.435 | 1.559 |
| **fraction seen in gnomAD** | **8.92%** (1,079) | **3.25%** (368) |
| fraction at the interface | 2.27% | 6.30% |

**Validation:** the damaging cluster is **depleted** in the population — 3.25% of it appears in gnomAD against 8.92% of the tolerant cluster (a 2.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
