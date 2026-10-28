# DICER1 — variant-effect analysis

*Endoribonuclease Dicer* · UniProt `Q9UPY3` · 1922 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 51–227 | 177 |
| Helicase C-terminal | 433–602 | 170 |
| Dicer dsRNA-binding fold | 630–722 | 93 |
| PAZ | 895–1042 | 148 |
| RNase III 1 | 1276–1403 | 128 |
| RNase III 2 | 1666–1824 | 159 |
| DRBM | 1849–1914 | 66 |

**Pair analysed:** Helicase ATP-binding ↔ RNase III 2

**AlphaFold PAE:** inter-module mean **17.12 Å**, intra-module **6.04 Å**, **ratio 2.83**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 44.7 | 0 | 100% / 100% |
| SWISSMODEL_7v6c-1-A_44-1915 | 96.2 | 0 | 100% / 100% |
| SWISSMODEL_7w0e-1-C_40-1914 | 58.0 | 0 | 100% / 100% |
| SWISSMODEL_7xw3-1-A_39-1917 | 34.4 | 33 | 100% / 100% |
| SWISSMODEL_7zpj-1-A_46-1916 | 32.7 | 39 | 100% / 100% |
| SWISSMODEL_8hf0-1-A_40-1915 | 55.9 | 0 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `DICER1_Q9UPY3_SWISSMODEL_7zpj-1-A_46-1916.pdb`, centroid distance **32.7 Å**, **39 residue pairs** in contact within 5 Å.

**Domain A interface residues (14):** `52, 53, 56, 68, 72, 75, 76, 79, 80, 114, 115, 116, 117, 118`

**Domain B interface residues (19):** `1668, 1692, 1693, 1694, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1766, 1767, 1769, 1770, 1774, 1777`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 627 | 35,891 | 0.962 | 0.822 | 6e-19 |
| ESM-1v | 627 | 35,891 | -4.996 | -4.012 | 2.2e-24 |
| FoldX ΔΔG | 627 | 25,916 | 1.025 | 1.118 | 0.044 |
| ThermoMPNN ΔΔG | 627 | 35,891 | 0.695 | 0.418 | 2.7e-11 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 36,518 |
| ESM-1v | 36,518 |
| FoldX ΔΔG (ProtVar) | 26,543 |
| ThermoMPNN ΔΔG | 36,518 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.299 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.415 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.529 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.210 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.219 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.691 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 2736 |
| conflict | 119 |
| pathogenic | 23 |
| likely_benign | 19 |
| likely_pathogenic | 14 |
| benign | 8 |

**gnomAD r4 missense variants mapped:** 1,777

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 26,543** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 16,895 | 9,648 |
| mean AlphaMissense | 0.627 | 0.966 |
| mean ESM-1v | 4.062 | 6.776 |
| mean FoldX ΔΔG | 0.637 | 4.77 |
| mean ThermoMPNN ΔΔG | 0.467 | 1.919 |
| **fraction seen in gnomAD** | **5.63%** (952) | **2.12%** (205) |
| fraction at the interface | 2.35% | 2.38% |

**Validation:** the damaging cluster is **depleted** in the population — 2.12% of it appears in gnomAD against 5.63% of the tolerant cluster (a 2.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 16 pathogenic / 0 benign, cluster 0 has 7 / 3; OR = inf, p = 0.046.

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
