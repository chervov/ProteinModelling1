# CSF1R — variant-effect analysis

*Macrophage colony-stimulating factor 1 receptor* · UniProt `P07333` · 972 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Ig-like C2-type 1 | 21–104 | 84 |
| Ig-like C2-type 2 | 107–197 | 91 |
| Ig-like C2-type 3 | 203–290 | 88 |
| Ig-like C2-type 4 | 299–399 | 101 |
| Ig-like C2-type 5 | 402–502 | 101 |
| Protein kinase | 582–910 | 329 |

**Pair analysed:** Ig-like C2-type 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **28.91 Å**, intra-module **7.42 Å**, **ratio 3.9**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 51.5 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 18,468 |
| ESM-1v | 18,468 |
| FoldX ΔΔG (ProtVar) | 15,238 |
| ThermoMPNN ΔΔG | 18,468 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.845 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.512 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.514 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.425 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.408 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.697 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 206 |
| likely_benign | 55 |
| conflict | 33 |
| likely_pathogenic | 25 |
| benign | 14 |
| pathogenic | 12 |

**gnomAD r4 missense variants mapped:** 1,129

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 15,238** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 9,292 | 5,946 |
| mean AlphaMissense | 0.25 | 0.882 |
| mean ESM-1v | 5.898 | 13.4 |
| mean FoldX ΔΔG | 0.744 | 4.64 |
| mean ThermoMPNN ΔΔG | 0.545 | 1.763 |
| **fraction seen in gnomAD** | **8.37%** (778) | **1.93%** (115) |

**Validation:** the damaging cluster is **depleted** in the population — 1.93% of it appears in gnomAD against 8.37% of the tolerant cluster (a 4.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 12 pathogenic / 0 benign, cluster 0 has 0 / 12; OR = inf, p = 7.4e-07.

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
