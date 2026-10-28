# ACTN4 — variant-effect analysis

*Alpha-actinin-4* · UniProt `O43707` · 911 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Calponin-homology (CH) 1 | 50–154 | 105 |
| Calponin-homology (CH) 2 | 163–269 | 107 |
| EF-hand 1 | 765–800 | 36 |
| EF-hand 2 | 806–841 | 36 |

**Pair analysed:** Calponin-homology (CH) 1 ↔ Calponin-homology (CH) 2

**AlphaFold PAE:** inter-module mean **6.44 Å**, intra-module **3.03 Å**, **ratio 2.13**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 27.0 | 38 | 100% / 100% |
| SWISSMODEL_1sjj-1-A_44-911 | 46.0 | 0 | 100% / 100% |
| SWISSMODEL_6sl3-1-B_48-483 | 27.3 | 33 | 100% / 100% |
| SWISSMODEL_6sl7-1-B_48-483 | 26.7 | 38 | 100% / 100% |
| SWISSMODEL_7ank-1-A_47-519 | 26.5 | 46 | 100% / 100% |
| SWISSMODEL_9sis-1-B_46-909 | 26.9 | 45 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `ACTN4_O43707_SWISSMODEL_7ank-1-A_47-519.pdb`, centroid distance **26.5 Å**, **46 residue pairs** in contact within 5 Å.

**Domain A interface residues (16):** `50, 51, 52, 54, 55, 56, 58, 59, 62, 65, 144, 147, 150, 151, 153, 154`

**Domain B interface residues (21):** `165, 236, 238, 239, 240, 241, 242, 245, 246, 249, 251, 252, 253, 255, 256, 258, 259, 260, 262, 263, 266`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 703 | 16,606 | 0.998 | 0.905 | 3e-146 |
| ESM-1v | 703 | 16,606 | -16.638 | -14.806 | 8.3e-54 |
| FoldX ΔΔG | 703 | 15,751 | 1.844 | 0.907 | 3.6e-17 |
| ThermoMPNN ΔΔG | 703 | 16,606 | 1.103 | 0.572 | 1.6e-29 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 17,309 |
| ESM-1v | 17,309 |
| FoldX ΔΔG (ProtVar) | 16,454 |
| ThermoMPNN ΔΔG | 17,309 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.762 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.445 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.487 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.353 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.421 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.713 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 76 |
| likely_benign | 12 |
| likely_pathogenic | 6 |
| other | 5 |
| pathogenic | 5 |
| conflict | 5 |
| benign | 2 |

**gnomAD r4 missense variants mapped:** 859

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 16,454** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 5,866 | 10,588 |
| mean AlphaMissense | 0.398 | 0.945 |
| mean ESM-1v | 11.889 | 16.416 |
| mean FoldX ΔΔG | 0.401 | 2.613 |
| mean ThermoMPNN ΔΔG | 0.309 | 1.212 |
| **fraction seen in gnomAD** | **9.41%** (552) | **2.27%** (240) |
| fraction at the interface | 0.99% | 6.09% |

**Validation:** the damaging cluster is **depleted** in the population — 2.27% of it appears in gnomAD against 9.41% of the tolerant cluster (a 4.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
