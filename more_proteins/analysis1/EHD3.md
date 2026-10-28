# EHD3 — variant-effect analysis

*EH domain-containing protein 3* · UniProt `Q9NZN3` · 535 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 55–286 | 232 |
| EH | 444–532 | 89 |
| EF-hand | 476–511 | 36 |

**Pair analysed:** Dynamin-type G ↔ EH

**AlphaFold PAE:** inter-module mean **22.35 Å**, intra-module **3.4 Å**, **ratio 6.58**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 48.3 | 0 | 100% / 100% |
| 2qpt.1.B (71.3% id) | 52.3 | 0 | 100% / 100% |
| 7sox.1.A (76.8% id) | 35.4 | 21 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q9NZN3_7sox-1-A.pdb`, centroid distance **35.4 Å**, **21 residue pairs** in contact within 5 Å.

**Domain A interface residues (14):** `76, 77, 80, 82, 83, 86, 87, 88, 258, 259, 260, 261, 262, 268`

**Domain B interface residues (8):** `490, 492, 519, 520, 521, 522, 523, 532`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 418 | 9,747 | 0.78 | 0.912 | 2.5e-15 |
| ESM-1v | 418 | 9,747 | -10.617 | -11.268 | 7.4e-06 |
| FoldX ΔΔG | 418 | 9,424 | 0.693 | 1.161 | 2.1e-06 |
| ThermoMPNN ΔΔG | 418 | 9,747 | 0.704 | 0.733 | 0.034 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 10,165 |
| ESM-1v | 10,165 |
| FoldX ΔΔG (ProtVar) | 9,842 |
| ThermoMPNN ΔΔG | 10,165 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.851 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.469 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.519 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.410 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.481 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.730 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 20 |

**gnomAD r4 missense variants mapped:** 630

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 9,842** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,112 | 5,730 |
| mean AlphaMissense | 0.429 | 0.954 |
| mean ESM-1v | 7.85 | 13.736 |
| mean FoldX ΔΔG | 0.421 | 3.217 |
| mean ThermoMPNN ΔΔG | 0.349 | 1.467 |
| **fraction seen in gnomAD** | **9.63%** (396) | **3.73%** (214) |
| fraction at the interface | 5.23% | 3.54% |

**Validation:** the damaging cluster is **depleted** in the population — 3.73% of it appears in gnomAD against 9.63% of the tolerant cluster (a 2.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
