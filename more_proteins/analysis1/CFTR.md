# CFTR — variant-effect analysis

*Cystic fibrosis transmembrane conductance regulator* · UniProt `P13569` · 1480 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 81–365 | 285 |
| ABC transporter 1 | 423–646 | 224 |
| ABC transmembrane type-1 2 | 859–1155 | 297 |
| ABC transporter 2 | 1210–1443 | 234 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **13.06 Å**, intra-module **6.2 Å**, **ratio 2.11**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 30.0 | 14 | 100% / 100% |
| SWISSMODEL_6d3r-1-A_42-1439 | 40.3 | 0 | 100% / 98% |
| SWISSMODEL_9dw5-1-A_3-1436 | 46.1 | 0 | 100% / 97% |
| SWISSMODEL_9dw9-1-A_1-1451 | 27.1 | 64 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `CFTR_P13569_SWISSMODEL_9dw9-1-A_1-1451.pdb`, centroid distance **27.1 Å**, **64 residue pairs** in contact within 5 Å.

**Domain A interface residues (28):** `458, 459, 460, 461, 493, 494, 525, 528, 529, 549, 550, 551, 552, 553, 555, 573, 576, 577, 578, 579, 580, 581, 582, 584, 585, 605, 608, 611`

**Domain B interface residues (26):** `1244, 1245, 1246, 1247, 1291, 1292, 1347, 1348, 1349, 1350, 1371, 1374, 1375, 1376, 1377, 1378, 1380, 1402, 1404, 1436, 1437, 1439, 1440, 1441, 1442, 1443`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,026 | 27,094 | 0.727 | 0.535 | 5.5e-24 |
| ESM-1v | 1,026 | 27,094 | -6.788 | -5.128 | 6.9e-50 |
| FoldX ΔΔG | 1,026 | 22,363 | 0.573 | 1.094 | 1.6e-20 |
| ThermoMPNN ΔΔG | 1,026 | 27,094 | 0.489 | 0.539 | 0.0017 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 28,120 |
| ESM-1v | 28,120 |
| FoldX ΔΔG (ProtVar) | 23,389 |
| ThermoMPNN ΔΔG | 28,120 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.623 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.491 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.524 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.381 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.465 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.662 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 2,127

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 23,389** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 14,023 | 9,366 |
| mean AlphaMissense | 0.416 | 0.884 |
| mean ESM-1v | 4.583 | 8.362 |
| mean FoldX ΔΔG | 0.53 | 3.899 |
| mean ThermoMPNN ΔΔG | 0.407 | 1.738 |
| **fraction seen in gnomAD** | **9.64%** (1,352) | **4.94%** (463) |
| fraction at the interface | 4.08% | 4.85% |

**Validation:** the damaging cluster is **depleted** in the population — 4.94% of it appears in gnomAD against 9.64% of the tolerant cluster (a 2.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
