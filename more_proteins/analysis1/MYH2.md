# MYH2 — variant-effect analysis

*Myosin-2* · UniProt `Q9UKX2` · 1941 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Myosin N-terminal SH3-like | 33–82 | 50 |
| Myosin motor | 86–784 | 699 |
| IQ | 787–816 | 30 |

**Pair analysed:** Myosin motor ↔ IQ

**AlphaFold PAE:** inter-module mean **14.93 Å**, intra-module **6.33 Å**, **ratio 2.36**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 50.6 | 6 | 100% / 100% |
| 8q6t.1.A (81.3% id) | 59.6 | 5 | 100% / 100% |
| 3dtp.1.A (52.6% id) | 63.1 | 4 | 100% / 100% |
| 5tby.1.B (81.2% id) | 51.7 | 16 | 100% / 100% |
| 9tpl.1.A (81.2% id) | 47.8 | 6 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `MYH2_Q9UKX2_SWISSMODEL_2w4g-1-C_4-847.pdb`, centroid distance **69.2 Å**, **25 residue pairs** in contact within 5 Å.

**Domain A interface residues (13):** `727, 730, 731, 732, 733, 734, 735, 755, 756, 779, 780, 781, 784`

**Domain B interface residues (9):** `787, 788, 790, 791, 793, 794, 795, 797, 798`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 418 | 36,461 | 0.881 | 0.808 | 0.00042 |
| ESM-1v | 418 | 36,461 | -11.342 | -11.44 | 0.92 |
| FoldX ΔΔG | 418 | 34,675 | 0.524 | 0.453 | 0.16 |
| ThermoMPNN ΔΔG | 418 | 36,461 | 0.344 | 0.262 | 0.094 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 36,879 |
| ESM-1v | 36,879 |
| FoldX ΔΔG (ProtVar) | 35,093 |
| ThermoMPNN ΔΔG | 36,879 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.783 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.335 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.374 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.323 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.374 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.635 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 624 |
| conflict | 19 |
| likely_benign | 10 |
| pathogenic | 3 |
| likely_pathogenic | 3 |

**gnomAD r4 missense variants mapped:** 2,062

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 35,093** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 18,764 | 16,329 |
| mean AlphaMissense | 0.486 | 0.932 |
| mean ESM-1v | 8.674 | 14.522 |
| mean FoldX ΔΔG | 0.239 | 2.227 |
| mean ThermoMPNN ΔΔG | 0.157 | 0.948 |
| **fraction seen in gnomAD** | **7.65%** (1,436) | **3.15%** (515) |
| fraction at the interface | 1.03% | 1.37% |

**Validation:** the damaging cluster is **depleted** in the population — 3.15% of it appears in gnomAD against 7.65% of the tolerant cluster (a 2.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
