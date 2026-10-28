# ABL1 — variant-effect analysis

*Tyrosine-protein kinase ABL1* · UniProt `P00519` · 1130 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH3 | 61–121 | 61 |
| SH2 | 127–217 | 91 |
| Protein kinase | 242–493 | 252 |

**Pair analysed:** SH3 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **8.58 Å**, intra-module **3.48 Å**, **ratio 2.46**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.6 | 8 | 100% / 100% |
| 1opl.1.A (99.4% id) | 34.8 | 5 | 98% / 100% |
| 1y57.1.A (43.1% id) | 37.4 | 4 | 95% / 100% |

## 2. The inter-domain interface

Most compact structure: `P00519.pdb`, centroid distance **34.6 Å**, **8 residue pairs** in contact within 5 Å.

**Domain A interface residues (6):** `74, 75, 76, 77, 96, 98`

**Domain B interface residues (3):** `263, 264, 294`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 171 | 21,299 | 0.988 | 0.555 | 5.7e-28 |
| ESM-1v | 171 | 21,299 | -9.549 | -5.501 | 1.6e-22 |
| FoldX ΔΔG | 171 | 10,450 | 0.274 | 1.017 | 1.3e-12 |
| ThermoMPNN ΔΔG | 171 | 21,299 | 0.832 | 0.192 | 2.1e-11 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 21,470 |
| ESM-1v | 21,470 |
| FoldX ΔΔG (ProtVar) | 10,621 |
| ThermoMPNN ΔΔG | 21,470 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.742 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.486 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.571 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.483 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.541 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.683 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 113 |
| likely_benign | 103 |
| benign | 39 |
| likely_pathogenic | 35 |
| conflict | 11 |
| pathogenic | 4 |

**gnomAD r4 missense variants mapped:** 1,217

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 10,621** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,891 | 5,730 |
| mean AlphaMissense | 0.619 | 0.985 |
| mean ESM-1v | 6.307 | 13.799 |
| mean FoldX ΔΔG | 0.307 | 3.117 |
| mean ThermoMPNN ΔΔG | 0.331 | 1.624 |
| **fraction seen in gnomAD** | **6.36%** (311) | **1.59%** (91) |
| fraction at the interface | 1.82% | 1.43% |

**Validation:** the damaging cluster is **depleted** in the population — 1.59% of it appears in gnomAD against 6.36% of the tolerant cluster (a 4.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 2 pathogenic / 0 benign, cluster 0 has 2 / 6; OR = inf, p = 0.13.

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
