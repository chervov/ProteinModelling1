# CSK — variant-effect analysis

*Tyrosine-protein kinase CSK* · UniProt `P41240` · 450 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH3 | 9–70 | 62 |
| SH2 | 82–171 | 90 |
| Protein kinase | 195–449 | 255 |

**Pair analysed:** SH3 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **11.09 Å**, intra-module **3.39 Å**, **ratio 3.27**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.4 | 11 | 100% / 100% |
| 1k9a.5.A (98.4% id) | 35.8 | 8 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P41240.pdb`, centroid distance **34.4 Å**, **11 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `13, 32, 33, 34, 53, 68, 69, 70`

**Domain B interface residues (8):** `215, 217, 241, 242, 244, 251, 252, 253`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 8,246 | 0.762 | 0.893 | 2e-05 |
| ESM-1v | 304 | 8,246 | -9.769 | -10.736 | 0.0017 |
| FoldX ΔΔG | 304 | 8,151 | 1.292 | 1.231 | 0.3 |
| ThermoMPNN ΔΔG | 304 | 8,246 | 1.083 | 0.971 | 0.03 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 8,550 |
| ESM-1v | 8,550 |
| FoldX ΔΔG (ProtVar) | 8,455 |
| ThermoMPNN ΔΔG | 8,550 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.903 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.532 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.597 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.497 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.576 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.736 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 4 |
| benign | 2 |

**gnomAD r4 missense variants mapped:** 323

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 8,455** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,899 | 4,556 |
| mean AlphaMissense | 0.433 | 0.96 |
| mean ESM-1v | 7.262 | 14.142 |
| mean FoldX ΔΔG | 0.541 | 3.931 |
| mean ThermoMPNN ΔΔG | 0.471 | 1.754 |
| **fraction seen in gnomAD** | **6.46%** (252) | **1.47%** (67) |
| fraction at the interface | 4.08% | 3.18% |

**Validation:** the damaging cluster is **depleted** in the population — 1.47% of it appears in gnomAD against 6.46% of the tolerant cluster (a 4.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
