# SYK — variant-effect analysis

*Tyrosine-protein kinase SYK* · UniProt `P43405` · 635 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 15–107 | 93 |
| SH2 2 | 168–259 | 92 |
| Protein kinase | 371–631 | 261 |

**Pair analysed:** SH2 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **8.79 Å**, intra-module **3.52 Å**, **ratio 2.49**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 35.5 | 15 | 100% / 100% |
| 4fl2.1.A (100.0% id) | 35.3 | 15 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P43405.pdb`, centroid distance **35.5 Å**, **15 residue pairs** in contact within 5 Å.

**Domain A interface residues (9):** `22, 23, 45, 46, 48, 63, 65, 67, 77`

**Domain B interface residues (8):** `469, 600, 624, 625, 627, 628, 629, 631`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 323 | 11,742 | 0.81 | 0.861 | 0.098 |
| ESM-1v | 323 | 11,742 | -9.156 | -9.821 | 0.00061 |
| FoldX ΔΔG | 323 | 10,507 | 1.229 | 1.334 | 0.11 |
| ThermoMPNN ΔΔG | 323 | 11,742 | 0.615 | 0.735 | 0.002 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,065 |
| ESM-1v | 12,065 |
| FoldX ΔΔG (ProtVar) | 10,830 |
| ThermoMPNN ΔΔG | 12,065 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.884 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.521 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.567 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.468 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.557 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.703 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 12 |
| likely_benign | 2 |
| likely_pathogenic | 2 |
| benign | 1 |
| conflict | 1 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 560

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 10,830** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,635 | 6,195 |
| mean AlphaMissense | 0.411 | 0.954 |
| mean ESM-1v | 6.826 | 13.183 |
| mean FoldX ΔΔG | 0.619 | 3.789 |
| mean ThermoMPNN ΔΔG | 0.419 | 1.557 |
| **fraction seen in gnomAD** | **7.68%** (356) | **2.36%** (146) |
| fraction at the interface | 3.73% | 2.42% |

**Validation:** the damaging cluster is **depleted** in the population — 2.36% of it appears in gnomAD against 7.68% of the tolerant cluster (a 3.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
