# EIF4A1 — variant-effect analysis

*Eukaryotic initiation factor 4A-I* · UniProt `P60842` · 406 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 63–234 | 172 |
| Helicase C-terminal | 245–406 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **9.66 Å**, intra-module **3.95 Å**, **ratio 2.44**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 30.1 | 49 | 100% / 100% |
| SWISSMODEL_2hxy-1-A_32-406 | 36.7 | 27 | 100% / 100% |
| SWISSMODEL_3eiq-1-A_22-400 | 36.4 | 5 | 100% / 96% |
| SWISSMODEL_4c9b-1-A_15-406 | 47.6 | 3 | 100% / 100% |
| SWISSMODEL_9avr-1-A_30-402 | 29.2 | 54 | 100% / 98% |

## 2. The inter-domain interface

Most compact structure: `EIF4A1_P60842_SWISSMODEL_9avr-1-A_30-402.pdb`, centroid distance **29.2 Å**, **54 residue pairs** in contact within 5 Å.

**Domain A interface residues (21):** `78, 79, 80, 81, 108, 109, 110, 111, 112, 114, 115, 135, 136, 137, 183, 185, 186, 213, 214, 215, 217`

**Domain B interface residues (21):** `302, 308, 311, 312, 315, 319, 331, 332, 334, 335, 336, 337, 354, 355, 357, 358, 361, 362, 365, 366, 391`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 798 | 6,916 | 0.999 | 0.968 | 5.8e-142 |
| ESM-1v | 798 | 6,916 | -15.515 | -11.219 | 7.5e-143 |
| FoldX ΔΔG | 798 | 6,479 | 1.986 | 1.244 | 1.9e-07 |
| ThermoMPNN ΔΔG | 798 | 6,916 | 0.577 | 0.751 | 3e-09 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 7,714 |
| ESM-1v | 7,714 |
| FoldX ΔΔG (ProtVar) | 7,277 |
| ThermoMPNN ΔΔG | 7,714 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.870 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.496 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.491 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.468 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.472 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.694 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 275

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,277** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,662 | 3,615 |
| mean AlphaMissense | 0.736 | 0.988 |
| mean ESM-1v | 9.079 | 14.9 |
| mean FoldX ΔΔG | 0.457 | 4.282 |
| mean ThermoMPNN ΔΔG | 0.365 | 1.58 |
| **fraction seen in gnomAD** | **4.59%** (168) | **1.24%** (45) |
| fraction at the interface | 5.46% | 16.54% |

**Validation:** the damaging cluster is **depleted** in the population — 1.24% of it appears in gnomAD against 4.59% of the tolerant cluster (a 3.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
