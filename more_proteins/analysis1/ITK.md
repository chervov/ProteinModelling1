# ITK — variant-effect analysis

*Tyrosine-protein kinase ITK/TSK* · UniProt `Q08881` · 620 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PH | 4–111 | 108 |
| SH3 | 171–231 | 61 |
| SH2 | 239–338 | 100 |
| Protein kinase | 363–615 | 253 |

**Pair analysed:** PH ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **29.79 Å**, intra-module **4.48 Å**, **ratio 6.65**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 41.4 | 1 | 100% / 100% |
| 4y93.1.A (55.3% id) | 39.0 | 13 | 100% / 100% |
| 8s93.1.A (53.0% id) | 42.3 | 14 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q08881_8s93-1-A.pdb`, centroid distance **42.3 Å**, **14 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `35, 36, 56, 57, 107, 108, 109, 111`

**Domain B interface residues (8):** `382, 383, 384, 385, 386, 411, 422, 423`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 11,476 | 0.386 | 0.698 | 5.1e-13 |
| ESM-1v | 304 | 11,476 | -7.608 | -8.372 | 0.00041 |
| FoldX ΔΔG | 304 | 11,229 | 0.753 | 1.156 | 0.0011 |
| ThermoMPNN ΔΔG | 304 | 11,476 | 0.533 | 0.832 | 2.9e-05 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 11,780 |
| ESM-1v | 11,780 |
| FoldX ΔΔG (ProtVar) | 11,533 |
| ThermoMPNN ΔΔG | 11,780 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.879 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.525 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.552 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.511 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.556 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.726 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 167 |
| likely_benign | 6 |
| conflict | 5 |
| pathogenic | 2 |

**gnomAD r4 missense variants mapped:** 644

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 11,533** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 6,402 | 5,131 |
| mean AlphaMissense | 0.375 | 0.928 |
| mean ESM-1v | 6.113 | 11.983 |
| mean FoldX ΔΔG | 0.573 | 4.124 |
| mean ThermoMPNN ΔΔG | 0.453 | 1.827 |
| **fraction seen in gnomAD** | **7.54%** (483) | **2.86%** (147) |
| fraction at the interface | 3.31% | 1.79% |

**Validation:** the damaging cluster is **depleted** in the population — 2.86% of it appears in gnomAD against 7.54% of the tolerant cluster (a 2.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
