# DDX3Y — variant-effect analysis

*ATP-dependent RNA helicase DDX3Y* · UniProt `O15523` · 660 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 209–401 | 193 |
| Helicase C-terminal | 412–573 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **12.36 Å**, intra-module **3.96 Å**, **ratio 3.12**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 31.6 | 35 | 100% / 100% |
| SWISSMODEL_8ark-2-A_125-573 | 42.2 | 18 | 100% / 100% |
| SWISSMODEL_8arp-1-A_118-573 | 31.4 | 44 | 100% / 100% |
| SWISSMODEL_8ssw-1-A_132-578 | 50.7 | 0 | 100% / 100% |
| SWISSMODEL_9e2c-1-A_132-572 | 31.9 | 38 | 100% / 99% |

## 2. The inter-domain interface

Most compact structure: `DDX3Y_O15523_SWISSMODEL_8arp-1-A_118-573.pdb`, centroid distance **31.4 Å**, **44 residue pairs** in contact within 5 Å.

**Domain A interface residues (22):** `223, 224, 225, 229, 273, 274, 275, 276, 278, 279, 282, 285, 299, 300, 301, 302, 346, 349, 352, 353, 381, 382`

**Domain B interface residues (19):** `447, 448, 449, 450, 470, 471, 472, 475, 478, 496, 498, 499, 501, 518, 519, 521, 522, 525, 549`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 779 | 11,761 | 0.998 | 0.728 | 7.3e-169 |
| ESM-1v | 779 | 11,761 | -16.623 | -11.83 | 7.9e-171 |
| FoldX ΔΔG | 779 | 8,265 | 0.336 | 1.357 | 2.2e-52 |
| ThermoMPNN ΔΔG | 779 | 11,761 | 0.452 | 0.363 | 0.6 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,540 |
| ESM-1v | 12,540 |
| FoldX ΔΔG (ProtVar) | 9,044 |
| ThermoMPNN ΔΔG | 12,540 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.886 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.499 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.558 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.405 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.533 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.692 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 165

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 9,044** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,171 | 5,873 |
| mean AlphaMissense | 0.389 | 0.962 |
| mean ESM-1v | 9.714 | 15.662 |
| mean FoldX ΔΔG | 0.47 | 3.36 |
| mean ThermoMPNN ΔΔG | 0.338 | 1.3 |
| **fraction seen in gnomAD** | **2.59%** (82) | **0.17%** (10) |
| fraction at the interface | 2.49% | 11.92% |

**Validation:** the damaging cluster is **depleted** in the population — 0.17% of it appears in gnomAD against 2.59% of the tolerant cluster (a 15.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
