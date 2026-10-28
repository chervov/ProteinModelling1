# ZAP70 — variant-effect analysis

*Tyrosine-protein kinase ZAP-70* · UniProt `P43403` · 619 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 10–102 | 93 |
| SH2 2 | 163–254 | 92 |
| Protein kinase | 338–600 | 263 |

**Pair analysed:** SH2 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **13.22 Å**, intra-module **3.5 Å**, **ratio 3.77**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 42.9 | 0 | 100% / 100% |
| 4k2r.1.A (99.8% id) | 43.0 | 0 | 100% / 100% |
| 4fl2.1.A (56.9% id) | 35.0 | 17 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P43403_4fl2-1-A.pdb`, centroid distance **35.0 Å**, **17 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `17, 37, 40, 41, 43, 60, 62, 72`

**Domain B interface residues (9):** `567, 591, 592, 594, 595, 596, 598, 599, 600`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 323 | 11,438 | 0.619 | 0.856 | 3.6e-11 |
| ESM-1v | 323 | 11,438 | -9.245 | -10.357 | 0.00055 |
| FoldX ΔΔG | 323 | 10,412 | 0.543 | 1.376 | 5.4e-16 |
| ThermoMPNN ΔΔG | 323 | 11,438 | 0.546 | 0.788 | 0.00055 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 11,761 |
| ESM-1v | 11,761 |
| FoldX ΔΔG (ProtVar) | 10,735 |
| ThermoMPNN ΔΔG | 11,761 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.875 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.521 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.568 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.446 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.517 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.687 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 148 |
| conflict | 7 |
| pathogenic | 3 |
| likely_benign | 3 |
| benign | 1 |
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 739

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 10,735** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,666 | 6,069 |
| mean AlphaMissense | 0.416 | 0.949 |
| mean ESM-1v | 7.405 | 13.448 |
| mean FoldX ΔΔG | 0.616 | 3.664 |
| mean ThermoMPNN ΔΔG | 0.422 | 1.572 |
| **fraction seen in gnomAD** | **9.77%** (456) | **3.71%** (225) |
| fraction at the interface | 4.16% | 2.13% |

**Validation:** the damaging cluster is **depleted** in the population — 3.71% of it appears in gnomAD against 9.77% of the tolerant cluster (a 2.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
