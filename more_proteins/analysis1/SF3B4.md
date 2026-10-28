# SF3B4 — variant-effect analysis

*Splicing factor 3B subunit 4* · UniProt `Q15427` · 424 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| RRM 1 | 13–91 | 79 |
| RRM 2 | 100–179 | 80 |

**Pair analysed:** RRM 1 ↔ RRM 2

**AlphaFold PAE:** inter-module mean **8.77 Å**, intra-module **2.72 Å**, **ratio 3.23**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 25.3 | 17 | 100% / 100% |
| SWISSMODEL_6tr0-1-A_6-182 | 37.2 | 0 | 100% / 100% |
| SWISSMODEL_6xlx-1-A_9-181 | 24.8 | 23 | 100% / 100% |
| SWISSMODEL_8hk1-1-E_11-181 | 23.8 | 43 | 100% / 100% |
| SWISSMODEL_8i0p-1-9_13-180 | 26.9 | 7 | 100% / 100% |
| SWISSMODEL_9f4k-1-A_7-179 | 31.0 | 11 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `SF3B4_Q15427_SWISSMODEL_8hk1-1-E_11-181.pdb`, centroid distance **23.8 Å**, **43 residue pairs** in contact within 5 Å.

**Domain A interface residues (17):** `16, 17, 18, 19, 45, 56, 58, 75, 76, 77, 78, 82, 83, 85, 87, 89, 91`

**Domain B interface residues (18):** `107, 108, 109, 110, 112, 115, 134, 135, 137, 138, 139, 140, 141, 142, 143, 168, 169, 170`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 665 | 7,391 | 0.999 | 0.639 | 1.8e-128 |
| ESM-1v | 665 | 7,391 | -16.291 | -9.752 | 5.8e-153 |
| FoldX ΔΔG | 665 | 7,372 | 1.037 | 0.51 | 4e-09 |
| ThermoMPNN ΔΔG | 665 | 7,391 | 0.853 | 0.263 | 5.7e-57 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 8,056 |
| ESM-1v | 8,056 |
| FoldX ΔΔG (ProtVar) | 8,037 |
| ThermoMPNN ΔΔG | 8,056 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.891 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.345 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.510 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.323 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.511 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.559 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 17 |
| likely_benign | 3 |
| conflict | 3 |
| pathogenic | 2 |
| benign | 1 |

**gnomAD r4 missense variants mapped:** 332

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 8,037** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,162 | 3,875 |
| mean AlphaMissense | 0.331 | 0.98 |
| mean ESM-1v | 6.784 | 15.376 |
| mean FoldX ΔΔG | 0.359 | 2.13 |
| mean ThermoMPNN ΔΔG | 0.196 | 1.019 |
| **fraction seen in gnomAD** | **6.37%** (265) | **1.73%** (67) |
| fraction at the interface | 0.70% | 16.41% |

**Validation:** the damaging cluster is **depleted** in the population — 1.73% of it appears in gnomAD against 6.37% of the tolerant cluster (a 3.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
