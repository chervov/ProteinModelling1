# ITGB1 — variant-effect analysis

*Integrin beta-1* · UniProt `P05556` · 798 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PSI | 26–76 | 51 |
| VWFA | 140–378 | 239 |
| I-EGF 1 | 466–501 | 36 |
| I-EGF 2 | 502–554 | 53 |
| I-EGF 3 | 555–591 | 37 |
| I-EGF 4 | 592–631 | 40 |

**Pair analysed:** PSI ↔ I-EGF 2

**AlphaFold PAE:** inter-module mean **8.01 Å**, intra-module **3.8 Å**, **ratio 2.11**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 20.2 | 15 | 100% / 100% |
| SWISSMODEL_7nxd-1-B_23-723 | 23.0 | 7 | 100% / 100% |
| SWISSMODEL_7usl-1-B_27-724 | 21.1 | 10 | 98% / 100% |
| SWISSMODEL_8xei-1-B_25-722 | 22.0 | 6 | 100% / 100% |
| SWISSMODEL_8xen-1-B_25-632 | 31.8 | 0 | 100% / 100% |
| SWISSMODEL_8xez-1-B_23-633 | 22.5 | 12 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P05556.pdb`, centroid distance **20.2 Å**, **15 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `28, 31, 56, 57, 59, 61, 62, 72`

**Domain B interface residues (8):** `536, 537, 538, 540, 544, 545, 550, 551`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 14,858 | 0.601 | 0.83 | 9.4e-06 |
| ESM-1v | 304 | 14,858 | -7.854 | -11.003 | 3.1e-17 |
| FoldX ΔΔG | 304 | 14,649 | 1.1 | 0.929 | 0.16 |
| ThermoMPNN ΔΔG | 304 | 14,858 | 0.461 | 0.591 | 0.0019 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 15,162 |
| ESM-1v | 15,162 |
| FoldX ΔΔG (ProtVar) | 14,953 |
| ThermoMPNN ΔΔG | 15,162 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.877 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.520 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.434 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.401 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.352 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.613 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 18 |
| likely_benign | 1 |

**gnomAD r4 missense variants mapped:** 765

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 14,953** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 6,612 | 8,341 |
| mean AlphaMissense | 0.344 | 0.943 |
| mean ESM-1v | 7.21 | 14.004 |
| mean FoldX ΔΔG | 0.502 | 3.971 |
| mean ThermoMPNN ΔΔG | 0.375 | 1.152 |
| **fraction seen in gnomAD** | **7.50%** (496) | **2.60%** (217) |
| fraction at the interface | 2.93% | 1.32% |

**Validation:** the damaging cluster is **depleted** in the population — 2.60% of it appears in gnomAD against 7.50% of the tolerant cluster (a 2.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
