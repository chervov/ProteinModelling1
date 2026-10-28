# U2AF2 — variant-effect analysis

*Splicing factor U2AF 65 kDa subunit* · UniProt `P26368` · 475 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| RRM 1 | 149–231 | 83 |
| RRM 2 | 259–337 | 79 |
| RRM 3 | 385–466 | 82 |

**Pair analysed:** RRM 1 ↔ RRM 2

**AlphaFold PAE:** inter-module mean **7.51 Å**, intra-module **2.96 Å**, **ratio 2.53**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 26.7 | 5 | 100% / 100% |
| SWISSMODEL_6tr0-1-A_140-342 | 37.5 | 0 | 100% / 100% |
| SWISSMODEL_7s3a-1-A_142-340 | 25.8 | 16 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `U2AF2_P26368_SWISSMODEL_7s3a-1-A_142-340.pdb`, centroid distance **25.8 Å**, **16 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `155, 216, 218, 220, 221, 222, 223, 225`

**Domain B interface residues (8):** `271, 272, 273, 276, 288, 289, 290, 292`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 8,721 | 0.983 | 0.906 | 1.5e-13 |
| ESM-1v | 304 | 8,721 | -13.292 | -11.353 | 1.4e-16 |
| FoldX ΔΔG | 304 | 7,087 | 0.99 | 0.932 | 0.96 |
| ThermoMPNN ΔΔG | 304 | 8,721 | 0.664 | 0.467 | 0.13 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 9,025 |
| ESM-1v | 9,025 |
| FoldX ΔΔG (ProtVar) | 7,391 |
| ThermoMPNN ΔΔG | 9,025 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.878 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.499 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.611 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.437 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.587 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.703 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 10 |
| likely_pathogenic | 6 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 256

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,391** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,856 | 3,535 |
| mean AlphaMissense | 0.657 | 0.983 |
| mean ESM-1v | 9.7 | 15.391 |
| mean FoldX ΔΔG | 0.385 | 3.522 |
| mean ThermoMPNN ΔΔG | 0.313 | 1.697 |
| **fraction seen in gnomAD** | **3.45%** (133) | **0.42%** (15) |
| fraction at the interface | 4.10% | 4.13% |

**Validation:** the damaging cluster is **depleted** in the population — 0.42% of it appears in gnomAD against 3.45% of the tolerant cluster (a 8.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
