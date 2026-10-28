# PTPN6 — variant-effect analysis

*Tyrosine-protein phosphatase non-receptor type 6* · UniProt `P29350` · 595 aa · debug case

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 4–100 | 97 |
| SH2 2 | 110–213 | 104 |
| Tyrosine-protein phosphatase | 244–515 | 272 |

**Pair analysed:** SH2 1 ↔ Tyrosine-protein phosphatase

**AlphaFold PAE:** inter-module mean **12.88 Å**, intra-module **3.27 Å**, **ratio 3.94**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 40.8 | 16 | 100% / 100% |
| 3ps5.1.A (99.8% id) | 41.1 | 13 | 100% / 100% |
| 2b3o.1.A (100.0% id) | 30.2 | 77 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P29350_2b3o-1-A.pdb`, centroid distance **30.2 Å**, **77 residue pairs** in contact within 5 Å.

**Domain A interface residues (25):** `4, 5, 7, 31, 33, 36, 39, 56, 57, 58, 59, 60, 61, 62, 67, 68, 69, 70, 71, 72, 73, 74, 77, 78, 83`

**Domain B interface residues (30):** `245, 246, 248, 249, 252, 255, 256, 259, 262, 276, 277, 278, 279, 282, 358, 360, 419, 420, 421, 454, 455, 457, 458, 459, 496, 497, 500, 501, 502, 504`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,045 | 10,260 | 0.994 | 0.78 | 7.9e-140 |
| ESM-1v | 1,045 | 10,260 | -11.929 | -8.368 | 1.8e-109 |
| FoldX ΔΔG | 1,045 | 9,177 | 0.871 | 1.168 | 2.4e-10 |
| ThermoMPNN ΔΔG | 1,045 | 10,260 | 0.814 | 0.719 | 0.27 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 11,305 |
| ESM-1v | 11,305 |
| FoldX ΔΔG (ProtVar) | 10,222 |
| ThermoMPNN ΔΔG | 11,305 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.893 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.533 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.587 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.504 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.591 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.705 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 13 |
| likely_benign | 1 |

**gnomAD r4 missense variants mapped:** 664

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 10,222** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,807 | 5,415 |
| mean AlphaMissense | 0.409 | 0.964 |
| mean ESM-1v | 6.123 | 12.536 |
| mean FoldX ΔΔG | 0.472 | 3.765 |
| mean ThermoMPNN ΔΔG | 0.412 | 1.614 |
| **fraction seen in gnomAD** | **7.80%** (375) | **2.88%** (156) |
| fraction at the interface | 4.91% | 14.94% |

**Validation:** the damaging cluster is **depleted** in the population — 2.88% of it appears in gnomAD against 7.80% of the tolerant cluster (a 2.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
