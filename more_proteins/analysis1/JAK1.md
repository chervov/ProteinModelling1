# JAK1 — variant-effect analysis

*Tyrosine-protein kinase JAK1* · UniProt `P23458` · 1154 aa · **reference**

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| FERM | 34–420 | 387 |
| SH2 | 439–544 | 106 |
| Protein kinase 1 | 583–855 | 273 |
| Protein kinase 2 | 875–1153 | 279 |

**Pair analysed:** FERM ↔ Protein kinase 2

**AlphaFold PAE:** inter-module mean **25.79 Å**, intra-module **7.1 Å**, **ratio 3.63**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 92.5 | 0 | 100% / 100% |
| ma-l9b1f (Jeanpierre, closed) | 39.8 | 7 | 100% / 100% |
| ma-a1sai (Jeanpierre, open) | 92.9 | 0 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `JAK1_closed_ma-l9b1f.pdb`, centroid distance **39.8 Å**, **7 residue pairs** in contact within 5 Å.

**Domain A interface residues (5):** `297, 298, 362, 365, 366`

**Domain B interface residues (6):** `894, 901, 902, 903, 933, 997`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 209 | 21,717 | 0.678 | 0.684 | 0.55 |
| ESM-1v | 209 | 21,717 | -4.535 | -4.541 | 0.91 |
| FoldX ΔΔG | 209 | 20,596 | 0.632 | 1.146 | 0.038 |
| ThermoMPNN ΔΔG | 209 | 21,717 | 0.548 | 0.764 | 0.3 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 21,926 |
| ESM-1v | 21,926 |
| FoldX ΔΔG (ProtVar) | 20,805 |
| ThermoMPNN ΔΔG | 21,926 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.508 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.525 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.560 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.346 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.384 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.690 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 984

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 20,805** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 12,788 | 8,017 |
| mean AlphaMissense | 0.43 | 0.939 |
| mean ESM-1v | 4.182 | 7.84 |
| mean FoldX ΔΔG | 0.601 | 4.592 |
| mean ThermoMPNN ΔΔG | 0.483 | 1.892 |
| **fraction seen in gnomAD** | **5.97%** (764) | **1.95%** (156) |
| fraction at the interface | 1.13% | 0.81% |

**Validation:** the damaging cluster is **depleted** in the population — 1.95% of it appears in gnomAD against 5.97% of the tolerant cluster (a 3.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
