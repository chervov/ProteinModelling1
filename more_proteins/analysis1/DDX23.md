# DDX23 — variant-effect analysis

*Probable ATP-dependent RNA helicase DDX23* · UniProt `Q9BUQ8` · 820 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 422–627 | 206 |
| Helicase C-terminal | 651–799 | 149 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **17.1 Å**, intra-module **3.92 Å**, **ratio 4.36**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.6 | 15 | 100% / 100% |
| SWISSMODEL_2hxy-3-A_392-781 | 34.0 | 33 | 100% / 88% |
| SWISSMODEL_4c9b-1-A_392-781 | 46.7 | 1 | 100% / 88% |
| SWISSMODEL_4kbf-1-A_393-779 | 35.2 | 35 | 100% / 87% |
| SWISSMODEL_4kbf-2-A_393-779 | 56.3 | 0 | 100% / 87% |
| SWISSMODEL_6ah0-1-s_352-790 | 43.1 | 0 | 100% / 94% |
| SWISSMODEL_6o5f-1-A_375-803 | 45.7 | 0 | 100% / 100% |
| SWISSMODEL_6qw6-1-X_158-806 | 41.6 | 5 | 100% / 100% |
| SWISSMODEL_8y6o-1-I_158-806 | 35.5 | 18 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `DDX23_Q9BUQ8_SWISSMODEL_4kbf-1-A_393-779.pdb`, centroid distance **35.2 Å**, **35 residue pairs** in contact within 5 Å.

**Domain A interface residues (14):** `436, 437, 476, 477, 480, 483, 550, 552, 553, 556, 607, 608, 609, 610`

**Domain B interface residues (16):** `711, 712, 728, 729, 730, 731, 732, 753, 754, 755, 756, 757, 758, 759, 760, 761`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 570 | 15,010 | 0.999 | 0.936 | 9.1e-92 |
| ESM-1v | 570 | 15,010 | -17.258 | -11.855 | 1.4e-131 |
| FoldX ΔΔG | 570 | 12,331 | 0.897 | 0.757 | 0.5 |
| ThermoMPNN ΔΔG | 570 | 15,010 | 0.581 | 0.347 | 2.4e-06 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 15,580 |
| ESM-1v | 15,580 |
| FoldX ΔΔG (ProtVar) | 12,901 |
| ThermoMPNN ΔΔG | 15,580 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.846 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.380 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.433 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.382 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.459 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.668 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 44 |
| likely_pathogenic | 3 |
| conflict | 2 |
| likely_benign | 1 |

**gnomAD r4 missense variants mapped:** 738

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 12,901** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,716 | 4,185 |
| mean AlphaMissense | 0.763 | 0.985 |
| mean ESM-1v | 11.27 | 16.563 |
| mean FoldX ΔΔG | 0.442 | 4.404 |
| mean ThermoMPNN ΔΔG | 0.313 | 1.681 |
| **fraction seen in gnomAD** | **5.42%** (472) | **1.39%** (58) |
| fraction at the interface | 3.14% | 7.07% |

**Validation:** the damaging cluster is **depleted** in the population — 1.39% of it appears in gnomAD against 5.42% of the tolerant cluster (a 3.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
