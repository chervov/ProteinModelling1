# PRKCA — variant-effect analysis

*Protein kinase C alpha type* · UniProt `P17252` · 672 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| C2 | 158–275 | 118 |
| Protein kinase | 339–597 | 259 |
| AGC-kinase C-terminal | 598–668 | 71 |

**Pair analysed:** C2 ↔ AGC-kinase C-terminal

**AlphaFold PAE:** inter-module mean **27.85 Å**, intra-module **5.54 Å**, **ratio 5.03**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 41.1 | 16 | 100% / 100% |
| 8se1.2.A (80.7% id) | 46.1 | 2 | 100% / 99% |
| 8se4.2.A (80.5% id) | 47.4 | 11 | 100% / 94% |
| 8se3.1.A (80.5% id) | 42.2 | 17 | 100% / 94% |
| 3pfq.1.A (80.6% id) | 64.2 | 0 | 100% / 97% |

## 2. The inter-domain interface

Most compact structure: `P17252_8se3-1-A.pdb`, centroid distance **42.2 Å**, **17 residue pairs** in contact within 5 Å.

**Domain A interface residues (10):** `236, 237, 238, 239, 262, 263, 264, 265, 268, 269`

**Domain B interface residues (8):** `604, 609, 610, 611, 612, 613, 614, 615`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 342 | 12,426 | 0.968 | 0.964 | 0.52 |
| ESM-1v | 342 | 12,426 | -9.49 | -10.545 | 2.8e-06 |
| FoldX ΔΔG | 342 | 11,628 | 1.401 | 1.211 | 0.59 |
| ThermoMPNN ΔΔG | 342 | 12,426 | 0.78 | 0.738 | 0.55 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,768 |
| ESM-1v | 12,768 |
| FoldX ΔΔG (ProtVar) | 11,970 |
| ThermoMPNN ΔΔG | 12,768 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.860 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.449 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.486 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.453 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.535 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.694 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 9 |
| likely_benign | 2 |

**gnomAD r4 missense variants mapped:** 555

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 11,970** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 5,393 | 6,577 |
| mean AlphaMissense | 0.585 | 0.978 |
| mean ESM-1v | 7.453 | 13.953 |
| mean FoldX ΔΔG | 0.485 | 3.977 |
| mean ThermoMPNN ΔΔG | 0.363 | 1.57 |
| **fraction seen in gnomAD** | **6.53%** (352) | **2.31%** (152) |
| fraction at the interface | 3.06% | 2.69% |

**Validation:** the damaging cluster is **depleted** in the population — 2.31% of it appears in gnomAD against 6.53% of the tolerant cluster (a 2.8-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
