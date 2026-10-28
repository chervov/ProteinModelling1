# DDX3X — variant-effect analysis

*ATP-dependent RNA helicase DDX3X* · UniProt `O00571` · 662 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 211–403 | 193 |
| Helicase C-terminal | 414–575 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **12.59 Å**, intra-module **3.76 Å**, **ratio 3.35**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 31.8 | 36 | 100% / 100% |
| SWISSMODEL_8q7x-1-C_169-552 | 32.3 | 31 | 100% / 86% |
| SWISSMODEL_8ssw-1-A_134-580 | 50.7 | 0 | 100% / 100% |
| SWISSMODEL_9e2c-1-A_134-574 | 32.0 | 38 | 100% / 99% |

## 2. The inter-domain interface

Most compact structure: `DDX3X_O00571_SWISSMODEL_9e2c-1-A_134-574.pdb`, centroid distance **32.0 Å**, **38 residue pairs** in contact within 5 Å.

**Domain A interface residues (18):** `225, 226, 275, 276, 277, 301, 302, 303, 323, 326, 351, 353, 354, 355, 356, 357, 360, 388`

**Domain B interface residues (18):** `414, 488, 502, 503, 504, 505, 506, 507, 508, 509, 526, 527, 528, 530, 531, 533, 534, 535`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 684 | 11,894 | 0.999 | 0.87 | 2.4e-179 |
| ESM-1v | 684 | 11,894 | -16.561 | -12.589 | 1.5e-131 |
| FoldX ΔΔG | 684 | 8,417 | 1.004 | 1.199 | 6e-06 |
| ThermoMPNN ΔΔG | 684 | 11,894 | 0.675 | 0.343 | 7.3e-08 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,578 |
| ESM-1v | 12,578 |
| FoldX ΔΔG (ProtVar) | 9,101 |
| ThermoMPNN ΔΔG | 12,578 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.867 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.471 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.529 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.378 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.500 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.697 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 125 |
| likely_pathogenic | 65 |
| pathogenic | 30 |
| conflict | 11 |
| likely_benign | 4 |
| other | 3 |
| benign | 1 |

**gnomAD r4 missense variants mapped:** 406

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 9,101** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,732 | 6,369 |
| mean AlphaMissense | 0.436 | 0.97 |
| mean ESM-1v | 9.862 | 15.857 |
| mean FoldX ΔΔG | 0.444 | 3.038 |
| mean ThermoMPNN ΔΔG | 0.332 | 1.224 |
| **fraction seen in gnomAD** | **5.01%** (137) | **1.33%** (85) |
| fraction at the interface | 1.65% | 10.03% |

**Validation:** the damaging cluster is **depleted** in the population — 1.33% of it appears in gnomAD against 5.01% of the tolerant cluster (a 3.8-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 27 pathogenic / 0 benign, cluster 0 has 0 / 0; OR = nan, p = 1.

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
