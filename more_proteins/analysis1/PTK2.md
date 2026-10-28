# PTK2 — variant-effect analysis

*Focal adhesion kinase 1* · UniProt `Q05397` · 1052 aa · **reference**

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| FERM | 35–355 | 321 |
| Protein kinase | 422–680 | 259 |
| Focal AT | 914–1045 | 132 |

**Pair analysed:** FERM ↔ Protein kinase

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 44.4 | 43 | 100% / 100% |
| 2J0J (X-ray, autoinhibited FERM-kinase) | 45.0 | 42 | 100% / 96% |

## 2. The inter-domain interface

Most compact structure: `Q05397.pdb`, centroid distance **44.4 Å**, **43 residue pairs** in contact within 5 Å.

**Domain A interface residues (19):** `44, 45, 46, 180, 182, 183, 184, 186, 187, 188, 190, 192, 193, 196, 197, 200, 201, 205, 236`

**Domain B interface residues (21):** `575, 576, 578, 579, 580, 581, 592, 594, 595, 596, 597, 598, 629, 630, 632, 633, 636, 637, 661, 662, 663`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 760 | 19,228 | 0.964 | 0.777 | 1.2e-41 |
| ESM-1v | 760 | 19,228 | -14.082 | -12.338 | 3.3e-42 |
| FoldX ΔΔG | 665 | 14,326 | 1.256 | 1.001 | 0.0092 |
| ThermoMPNN ΔΔG | 760 | 19,228 | 0.633 | 0.378 | 1.3e-12 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 19,988 |
| ESM-1v | 19,988 |
| FoldX ΔΔG (ProtVar) | 14,991 |
| ThermoMPNN ΔΔG | 19,988 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.750 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.447 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.521 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.342 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.441 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.715 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 22 |
| likely_benign | 2 |

**gnomAD r4 missense variants mapped:** 1,215

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 14,991** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,095 | 6,896 |
| mean AlphaMissense | 0.544 | 0.959 |
| mean ESM-1v | 10.416 | 15.516 |
| mean FoldX ΔΔG | 0.47 | 3.701 |
| mean ThermoMPNN ΔΔG | 0.331 | 1.625 |
| **fraction seen in gnomAD** | **7.67%** (621) | **2.65%** (183) |
| fraction at the interface | 3.68% | 5.32% |

**Validation:** the damaging cluster is **depleted** in the population — 2.65% of it appears in gnomAD against 7.67% of the tolerant cluster (a 2.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
