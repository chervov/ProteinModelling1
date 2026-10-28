# SRC — variant-effect analysis

*Proto-oncogene tyrosine-protein kinase Src* · UniProt `P12931` · 536 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH3 | 84–145 | 62 |
| SH2 | 151–248 | 98 |
| Protein kinase | 270–523 | 254 |

**Pair analysed:** SH3 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **8.44 Å**, intra-module **3.84 Å**, **ratio 2.2**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 36.2 | 8 | 100% / 100% |
| 8jn9.1.A (100.0% id) | 35.9 | 8 | 97% / 100% |
| 1y57.1.A (100.0% id) | 37.3 | 9 | 97% / 100% |

## 2. The inter-domain interface

Most compact structure: `P12931_1y57-1-A.pdb`, centroid distance **37.3 Å**, **9 residue pairs** in contact within 5 Å.

**Domain A interface residues (4):** `97, 98, 99, 100`

**Domain B interface residues (5):** `308, 311, 315, 318, 333`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 171 | 10,013 | 0.952 | 0.958 | 0.77 |
| ESM-1v | 171 | 10,013 | -9.551 | -9.268 | 0.33 |
| FoldX ΔΔG | 171 | 8,379 | 0.578 | 1.303 | 1.2e-09 |
| ThermoMPNN ΔΔG | 171 | 10,013 | 0.668 | 0.755 | 0.092 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 10,184 |
| ESM-1v | 10,184 |
| FoldX ΔΔG (ProtVar) | 8,550 |
| ThermoMPNN ΔΔG | 10,184 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.862 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.535 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.638 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.546 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.647 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.693 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 11 |
| likely_benign | 1 |
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 496

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 8,550** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,232 | 4,318 |
| mean AlphaMissense | 0.675 | 0.988 |
| mean ESM-1v | 7.34 | 14.02 |
| mean FoldX ΔΔG | 0.499 | 4.16 |
| mean ThermoMPNN ΔΔG | 0.509 | 1.854 |
| **fraction seen in gnomAD** | **6.52%** (276) | **1.78%** (77) |
| fraction at the interface | 2.79% | 1.23% |

**Validation:** the damaging cluster is **depleted** in the population — 1.78% of it appears in gnomAD against 6.52% of the tolerant cluster (a 3.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

## 6. ProteinGym

**Present**, so published experimental data and precomputed baseline scores exist:

| DMS_id | mutants | selection | region |
|---|--:|---|---|
| `SRC_HUMAN_Ahler_2019` | 3,372 | Activity | 270-519 |
| `SRC_HUMAN_Chakraborty_2023_binding-DAS_25uM` | 3,637 | Activity | 270-519 |
| `SRC_HUMAN_Nguyen_2022` | 3,366 | OrganismalFitness | 270-519 |

Fold definitions (`fold_random_5`, `fold_modulo_5`, `fold_contiguous_5`) ship with the benchmark; `fold_modulo_5` is the by-position split and the honest one. See `external_data/ddg_study.md` §8 and the ProteinGym notes in `external_data/ddg_docs_review.md`.

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
