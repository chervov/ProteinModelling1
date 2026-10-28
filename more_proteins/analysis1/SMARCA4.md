# SMARCA4 — variant-effect analysis

*SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 4* · UniProt `P51532` · 1647 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| QLQ | 171–206 | 36 |
| HSA | 460–532 | 73 |
| Helicase ATP-binding | 766–931 | 166 |
| Helicase C-terminal | 1084–1246 | 163 |
| Bromo | 1453–1564 | 112 |

**Pair analysed:** HSA ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **23.34 Å**, intra-module **6.88 Å**, **ratio 3.39**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 71.1 | 0 | 100% / 100% |
| SWISSMODEL_7y8r-1-J_365-1345 | 71.4 | 0 | 100% / 100% |
| SWISSMODEL_9rl4-1-I_350-1400 | 65.2 | 0 | 100% / 100% |
| SWISSMODEL_9rn1-1-I_350-1382 | 67.7 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 31,293 |
| ESM-1v | 31,293 |
| FoldX ΔΔG (ProtVar) | 19,779 |
| ThermoMPNN ΔΔG | 31,293 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.552 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.383 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.473 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.413 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.387 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.681 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1857 |
| conflict | 186 |
| likely_pathogenic | 43 |
| pathogenic | 13 |
| likely_benign | 6 |
| benign | 2 |

**gnomAD r4 missense variants mapped:** 1,415

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 19,779** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 13,636 | 6,143 |
| mean AlphaMissense | 0.838 | 0.991 |
| mean ESM-1v | 6.775 | 13.306 |
| mean FoldX ΔΔG | 0.441 | 4.098 |
| mean ThermoMPNN ΔΔG | 0.326 | 1.756 |
| **fraction seen in gnomAD** | **4.31%** (588) | **1.27%** (78) |

**Validation:** the damaging cluster is **depleted** in the population — 1.27% of it appears in gnomAD against 4.31% of the tolerant cluster (a 3.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 7 pathogenic / 0 benign, cluster 0 has 5 / 2; OR = inf, p = 0.46.

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
