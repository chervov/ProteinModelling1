# SMARCAD1 — variant-effect analysis

*SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A containing DEAD/H box 1* · UniProt `Q9H4L7` · 1026 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| CUE 1 | 157–199 | 43 |
| CUE 2 | 251–294 | 44 |
| Helicase ATP-binding | 509–677 | 169 |
| Helicase C-terminal | 858–1010 | 153 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **8.88 Å**, intra-module **5.0 Å**, **ratio 1.78**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 29.3 | 36 | 100% / 100% |
| SWISSMODEL_8oop-1-G_487-1005 | 130.8 | 0 | 100% / 97% |
| SWISSMODEL_8qyv-1-I_486-1006 | 104.9 | 0 | 100% / 97% |
| SWISSMODEL_9c9t-1-K_498-1001 | 133.4 | 0 | 100% / 94% |
| SWISSMODEL_9gcg-1-H_497-1003 | 70.8 | 0 | 100% / 95% |
| SWISSMODEL_9jao-1-A_375-1003 | 28.4 | 53 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `SMARCAD1_Q9H4L7_SWISSMODEL_9jao-1-A_375-1003.pdb`, centroid distance **28.4 Å**, **53 residue pairs** in contact within 5 Å.

**Domain A interface residues (22):** `523, 524, 525, 526, 553, 554, 555, 556, 557, 558, 559, 562, 577, 629, 631, 632, 657, 658, 660, 661, 662, 664`

**Domain B interface residues (25):** `900, 906, 907, 909, 910, 913, 914, 931, 934, 935, 936, 937, 952, 953, 954, 957, 958, 961, 962, 964, 965, 966, 994, 998, 1001`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 893 | 18,601 | 0.99 | 0.447 | 1.1e-241 |
| ESM-1v | 893 | 18,601 | -14.43 | -6.002 | 7e-286 |
| FoldX ΔΔG | 893 | 12,901 | 0.8 | 1.052 | 3.3e-09 |
| ThermoMPNN ΔΔG | 893 | 18,601 | 0.535 | 0.285 | 1.1e-08 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 19,494 |
| ESM-1v | 19,494 |
| FoldX ΔΔG (ProtVar) | 13,794 |
| ThermoMPNN ΔΔG | 19,494 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.798 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.508 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.587 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.465 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.558 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.716 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 24 |
| benign | 5 |
| likely_benign | 1 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 887

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 13,794** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 7,707 | 6,087 |
| mean AlphaMissense | 0.435 | 0.949 |
| mean ESM-1v | 5.848 | 12.693 |
| mean FoldX ΔΔG | 0.448 | 3.634 |
| mean ThermoMPNN ΔΔG | 0.332 | 1.566 |
| **fraction seen in gnomAD** | **5.81%** (448) | **1.20%** (73) |
| fraction at the interface | 2.52% | 11.48% |

**Validation:** the damaging cluster is **depleted** in the population — 1.20% of it appears in gnomAD against 5.81% of the tolerant cluster (a 4.8-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
