# CAPN1 — variant-effect analysis

*Calpain-1 catalytic subunit* · UniProt `P07384` · 714 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Calpain catalytic | 55–354 | 300 |
| EF-hand 1 | 541–576 | 36 |
| EF-hand 2 | 585–618 | 34 |
| EF-hand 3 | 615–650 | 36 |
| EF-hand 4 | 680–714 | 35 |

**Pair analysed:** Calpain catalytic ↔ EF-hand 4

**AlphaFold PAE:** inter-module mean **13.37 Å**, intra-module **4.19 Å**, **ratio 3.19**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 55.8 | 0 | 100% / 100% |
| 1df0.1.A (61.7% id) | 55.3 | 0 | 100% / 97% |
| 3bow.1.A (61.7% id) | 47.7 | 0 | 100% / 97% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 13,566 |
| ESM-1v | 13,566 |
| FoldX ΔΔG (ProtVar) | 13,338 |
| ThermoMPNN ΔΔG | 13,566 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.805 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.553 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.549 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.531 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.535 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.694 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 94 |
| pathogenic | 4 |
| likely_benign | 4 |
| benign | 3 |
| conflict | 2 |

**gnomAD r4 missense variants mapped:** 903

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 13,338** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 6,911 | 6,427 |
| mean AlphaMissense | 0.461 | 0.953 |
| mean ESM-1v | 5.744 | 11.632 |
| mean FoldX ΔΔG | 0.612 | 4.707 |
| mean ThermoMPNN ΔΔG | 0.485 | 1.777 |
| **fraction seen in gnomAD** | **8.61%** (595) | **4.48%** (288) |

**Validation:** the damaging cluster is **depleted** in the population — 4.48% of it appears in gnomAD against 8.61% of the tolerant cluster (a 1.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
