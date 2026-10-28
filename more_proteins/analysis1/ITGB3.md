# ITGB3 — variant-effect analysis

*Integrin beta-3* · UniProt `P05106` · 788 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PSI | 30–76 | 47 |
| VWFA | 135–377 | 243 |
| I-EGF 1 | 463–498 | 36 |
| I-EGF 2 | 499–548 | 50 |
| I-EGF 3 | 549–585 | 37 |
| I-EGF 4 | 586–625 | 40 |

**Pair analysed:** PSI ↔ I-EGF 4

**AlphaFold PAE:** inter-module mean **13.48 Å**, intra-module **2.62 Å**, **ratio 5.14**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 46.4 | 0 | 100% / 100% |
| 6bxj.1.A (78.3% id) | 45.4 | 0 | 100% / 100% |
| 8xei.1.B (100.0% id) | 46.4 | 0 | 100% / 100% |
| 8xez.1.B (100.0% id) | 51.0 | 0 | 100% / 100% |
| 8xen.1.B (100.0% id) | 77.1 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 14,972 |
| ESM-1v | 14,972 |
| FoldX ΔΔG (ProtVar) | 14,440 |
| ThermoMPNN ΔΔG | 14,972 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.827 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.565 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.454 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.470 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.388 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.616 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 168 |
| likely_pathogenic | 43 |
| pathogenic | 16 |
| benign | 6 |
| likely_benign | 5 |
| conflict | 2 |

**gnomAD r4 missense variants mapped:** 957

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 14,440** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 7,663 | 6,777 |
| mean AlphaMissense | 0.333 | 0.922 |
| mean ESM-1v | 5.281 | 11.123 |
| mean FoldX ΔΔG | 0.567 | 4.635 |
| mean ThermoMPNN ΔΔG | 0.453 | 1.358 |
| **fraction seen in gnomAD** | **8.27%** (634) | **3.90%** (264) |

**Validation:** the damaging cluster is **depleted** in the population — 3.90% of it appears in gnomAD against 8.27% of the tolerant cluster (a 2.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 13 pathogenic / 0 benign, cluster 0 has 2 / 5; OR = inf, p = 0.0014.

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
