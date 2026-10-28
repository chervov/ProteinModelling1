# DNM2 — variant-effect analysis

*Dynamin-2* · UniProt `P50570` · 870 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 28–294 | 267 |
| PH | 519–625 | 107 |
| GED | 653–744 | 92 |

**Pair analysed:** Dynamin-type G ↔ GED

**AlphaFold PAE:** inter-module mean **19.07 Å**, intra-module **6.98 Å**, **ratio 2.73**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 58.1 | 5 | 100% / 100% |
| 8v8t.1.A (41.4% id) | 60.4 | 13 | 100% / 99% |
| 4bej.2.A (46.8% id) | 64.3 | 2 | 100% / 95% |
| 5a3f.1.A (84.2% id) | 59.2 | 4 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `P50570_8v8t-1-A.pdb`, centroid distance **60.4 Å**, **13 residue pairs** in contact within 5 Å.

**Domain A interface residues (9):** `28, 29, 30, 31, 286, 287, 289, 290, 293`

**Domain B interface residues (8):** `725, 728, 729, 732, 736, 739, 742, 743`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 323 | 16,207 | 0.912 | 0.924 | 0.41 |
| ESM-1v | 323 | 16,207 | -15.171 | -14.005 | 2.5e-06 |
| FoldX ΔΔG | 323 | 13,699 | 1.537 | 0.917 | 0.0074 |
| ThermoMPNN ΔΔG | 323 | 16,207 | 0.847 | 0.472 | 2.2e-13 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 16,530 |
| ESM-1v | 16,530 |
| FoldX ΔΔG (ProtVar) | 14,022 |
| ThermoMPNN ΔΔG | 16,530 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.839 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.464 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.535 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.349 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.444 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.698 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 1,050

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 14,022** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,106 | 9,916 |
| mean AlphaMissense | 0.452 | 0.957 |
| mean ESM-1v | 10.526 | 15.814 |
| mean FoldX ΔΔG | 0.299 | 2.431 |
| mean ThermoMPNN ΔΔG | 0.276 | 1.146 |
| **fraction seen in gnomAD** | **11.81%** (485) | **3.79%** (376) |
| fraction at the interface | 2.51% | 2.22% |

**Validation:** the damaging cluster is **depleted** in the population — 3.79% of it appears in gnomAD against 11.81% of the tolerant cluster (a 3.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
