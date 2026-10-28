# DNM1 — variant-effect analysis

*Dynamin-1* · UniProt `Q05193` · 864 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 28–294 | 267 |
| PH | 519–625 | 107 |
| GED | 659–750 | 92 |

**Pair analysed:** Dynamin-type G ↔ GED

**AlphaFold PAE:** inter-module mean **19.04 Å**, intra-module **7.0 Å**, **ratio 2.72**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 61.9 | 5 | 100% / 100% |
| 5a3f.1.A (84.5% id) | 59.2 | 4 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `Q05193.pdb`, centroid distance **61.9 Å**, **5 residue pairs** in contact within 5 Å.

**Domain A interface residues (3):** `287, 290, 293`

**Domain B interface residues (4):** `742, 745, 749, 750`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 133 | 16,283 | 0.985 | 0.964 | 0.065 |
| ESM-1v | 133 | 16,283 | -14.787 | -13.341 | 5.8e-06 |
| FoldX ΔΔG | 133 | 13,908 | 1.066 | 0.935 | 0.63 |
| ThermoMPNN ΔΔG | 133 | 16,283 | 0.654 | 0.49 | 0.18 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 16,416 |
| ESM-1v | 16,416 |
| FoldX ΔΔG (ProtVar) | 14,041 |
| ThermoMPNN ΔΔG | 16,416 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.868 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.437 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.526 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.361 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.467 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.681 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 796

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 14,041** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,705 | 5,336 |
| mean AlphaMissense | 0.783 | 0.988 |
| mean ESM-1v | 12.112 | 16.191 |
| mean FoldX ΔΔG | 0.418 | 3.994 |
| mean ThermoMPNN ΔΔG | 0.349 | 1.794 |
| **fraction seen in gnomAD** | **5.95%** (518) | **1.71%** (91) |
| fraction at the interface | 0.95% | 0.94% |

**Validation:** the damaging cluster is **depleted** in the population — 1.71% of it appears in gnomAD against 5.95% of the tolerant cluster (a 3.5-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
