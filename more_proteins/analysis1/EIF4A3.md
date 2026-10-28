# EIF4A3 — variant-effect analysis

*Eukaryotic initiation factor 4A-III* · UniProt `P38919` · 411 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 69–239 | 171 |
| Helicase C-terminal | 250–411 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **6.15 Å**, intra-module **3.71 Å**, **ratio 1.66**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 29.4 | 52 | 100% / 100% |
| SWISSMODEL_4c9b-1-A_21-411 | 47.5 | 3 | 100% / 100% |
| SWISSMODEL_7a5p-1-k_22-411 | 29.3 | 56 | 100% / 100% |
| SWISSMODEL_8xxn-1-a_31-406 | 37.2 | 3 | 100% / 97% |

## 2. The inter-domain interface

Most compact structure: `EIF4A3_P38919_SWISSMODEL_7a5p-1-k_22-411.pdb`, centroid distance **29.3 Å**, **56 residue pairs** in contact within 5 Å.

**Domain A interface residues (25):** `84, 85, 86, 87, 88, 114, 115, 116, 117, 118, 120, 121, 124, 141, 142, 143, 144, 188, 190, 191, 218, 219, 220, 222, 223`

**Domain B interface residues (22):** `307, 313, 316, 317, 320, 324, 336, 337, 339, 340, 341, 342, 359, 360, 362, 363, 366, 367, 370, 371, 395, 396`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 893 | 6,916 | 0.993 | 0.958 | 1.2e-55 |
| ESM-1v | 893 | 6,916 | -13.754 | -10.022 | 4.2e-90 |
| FoldX ΔΔG | 893 | 6,479 | 1.318 | 1.285 | 0.21 |
| ThermoMPNN ΔΔG | 893 | 6,916 | 0.733 | 0.759 | 0.078 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 7,809 |
| ESM-1v | 7,809 |
| FoldX ΔΔG (ProtVar) | 7,372 |
| ThermoMPNN ΔΔG | 7,809 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.848 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.477 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.536 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.444 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.492 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.689 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 8 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 245

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,372** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,876 | 3,496 |
| mean AlphaMissense | 0.753 | 0.984 |
| mean ESM-1v | 8.023 | 13.652 |
| mean FoldX ΔΔG | 0.529 | 4.46 |
| mean ThermoMPNN ΔΔG | 0.409 | 1.701 |
| **fraction seen in gnomAD** | **4.23%** (164) | **1.26%** (44) |
| fraction at the interface | 8.20% | 16.45% |

**Validation:** the damaging cluster is **depleted** in the population — 1.26% of it appears in gnomAD against 4.23% of the tolerant cluster (a 3.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
