# BTK — variant-effect analysis

*Tyrosine-protein kinase BTK* · UniProt `Q06187` · 659 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PH | 3–133 | 131 |
| SH3 | 214–274 | 61 |
| SH2 | 281–377 | 97 |
| Protein kinase | 402–655 | 254 |

**Pair analysed:** PH ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **26.38 Å**, intra-module **5.1 Å**, **ratio 5.17**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 43.0 | 3 | 100% / 100% |
| 8s93.1.A (92.3% id) | 44.4 | 14 | 100% / 100% |
| 4y93.1.A (96.0% id) | 39.5 | 13 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q06187_8s93-1-A.pdb`, centroid distance **44.4 Å**, **14 residue pairs** in contact within 5 Å.

**Domain A interface residues (9):** `3, 5, 34, 35, 58, 59, 130, 131, 133`

**Domain B interface residues (5):** `421, 422, 424, 425, 461`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 266 | 12,255 | 0.485 | 0.902 | 1.1e-24 |
| ESM-1v | 266 | 12,255 | -8.356 | -9.833 | 8.4e-10 |
| FoldX ΔΔG | 266 | 11,514 | 0.618 | 1.205 | 7.1e-09 |
| ThermoMPNN ΔΔG | 266 | 12,255 | 0.696 | 0.836 | 0.024 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,521 |
| ESM-1v | 12,521 |
| FoldX ΔΔG (ProtVar) | 11,780 |
| ThermoMPNN ΔΔG | 12,521 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.867 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.537 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.563 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.502 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.547 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.703 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 266

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 11,780** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 5,108 | 6,672 |
| mean AlphaMissense | 0.437 | 0.96 |
| mean ESM-1v | 6.62 | 12.993 |
| mean FoldX ΔΔG | 0.491 | 3.534 |
| mean ThermoMPNN ΔΔG | 0.446 | 1.652 |
| **fraction seen in gnomAD** | **3.45%** (176) | **0.94%** (63) |
| fraction at the interface | 3.43% | 1.36% |

**Validation:** the damaging cluster is **depleted** in the population — 0.94% of it appears in gnomAD against 3.45% of the tolerant cluster (a 3.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
