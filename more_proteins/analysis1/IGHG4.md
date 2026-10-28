# IGHG4 — variant-effect analysis

*Immunoglobulin heavy constant gamma 4* · UniProt `P01861` · 396 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Ig-like 1 | 6–99 | 94 |
| Ig-like 2 | 118–217 | 100 |
| Ig-like 3 | 226–322 | 97 |

**Pair analysed:** Ig-like 1 ↔ Ig-like 3

**AlphaFold PAE:** inter-module mean **28.05 Å**, intra-module **3.42 Å**, **ratio 8.2**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 61.9 | 0 | 100% / 100% |
| 6gfe.1.A (99.7% id) | 56.2 | 0 | 100% / 100% |
| 6hyg.1.A (74.8% id) | 17.0 | 66 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P01861_6hyg-1-A.pdb`, centroid distance **17.0 Å**, **66 residue pairs** in contact within 5 Å.

**Domain A interface residues (29):** `7, 9, 10, 11, 12, 13, 14, 16, 17, 20, 24, 25, 26, 28, 30, 31, 51, 52, 53, 54, 56, 57, 58, 59, 64, 66, 67, 68, 96`

**Domain B interface residues (31):** `227, 228, 229, 230, 231, 232, 233, 234, 236, 237, 240, 244, 246, 248, 250, 270, 272, 273, 274, 275, 276, 277, 278, 279, 280, 285, 286, 287, 289, 319, 320`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,140 | 5,073 | 0.468 | 0.427 | 0.16 |
| ESM-1v | 1,140 | 5,073 | -10.737 | -9.778 | 1.2e-18 |
| FoldX ΔΔG | 1,140 | 4,978 | 0.739 | 0.822 | 1.7e-06 |
| ThermoMPNN ΔΔG | 1,140 | 5,073 | 0.624 | 0.719 | 0.001 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 6,213 |
| ESM-1v | 6,213 |
| FoldX ΔΔG (ProtVar) | 6,118 |
| ThermoMPNN ΔΔG | 6,213 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.788 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.539 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.554 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.464 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.532 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.692 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 763

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,118** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,798 | 2,320 |
| mean AlphaMissense | 0.3 | 0.837 |
| mean ESM-1v | 8.248 | 13.046 |
| mean FoldX ΔΔG | 0.463 | 4.131 |
| mean ThermoMPNN ΔΔG | 0.458 | 1.776 |
| **fraction seen in gnomAD** | **13.56%** (515) | **5.73%** (133) |
| fraction at the interface | 18.80% | 18.36% |

**Validation:** the damaging cluster is **depleted** in the population — 5.73% of it appears in gnomAD against 13.56% of the tolerant cluster (a 2.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
