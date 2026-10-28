# TYK2 — variant-effect analysis

*Non-receptor tyrosine-protein kinase TYK2* · UniProt `P29597` · 1187 aa · **reference**

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| FERM | 26–431 | 406 |
| SH2; atypical | 450–529 | 80 |
| Protein kinase 1 | 589–875 | 287 |
| Protein kinase 2 | 897–1176 | 280 |

**Pair analysed:** Protein kinase 1 ↔ Protein kinase 2

**AlphaFold PAE:** inter-module mean **14.62 Å**, intra-module **6.67 Å**, **ratio 2.19**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 37.9 | 44 | 100% / 100% |
| 4OLI (X-ray, closed JH2-JH1) | 39.6 | 38 | 89% / 95% |

## 2. The inter-domain interface

Most compact structure: `P29597.pdb`, centroid distance **37.9 Å**, **44 residue pairs** in contact within 5 Å.

**Domain A interface residues (18):** `610, 611, 613, 635, 637, 663, 664, 665, 666, 668, 672, 674, 688, 728, 743, 744, 754, 756`

**Domain B interface residues (19):** `898, 899, 900, 901, 902, 910, 913, 919, 921, 922, 923, 924, 926, 980, 982, 983, 1032, 1033, 1034`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 703 | 21,850 | 0.598 | 0.369 | 1.1e-13 |
| ESM-1v | 703 | 21,850 | -5.586 | -4.802 | 3e-11 |
| FoldX ΔΔG | 665 | 19,513 | 1.134 | 1.31 | 0.011 |
| ThermoMPNN ΔΔG | 703 | 21,850 | 1.074 | 0.77 | 0.00014 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 22,553 |
| ESM-1v | 22,553 |
| FoldX ΔΔG (ProtVar) | 20,178 |
| ThermoMPNN ΔΔG | 22,553 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.543 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.536 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.591 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.359 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.384 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.689 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 365 |
| likely_benign | 13 |
| conflict | 9 |
| benign | 7 |

**gnomAD r4 missense variants mapped:** 1,638

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 20,178** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 13,204 | 6,974 |
| mean AlphaMissense | 0.321 | 0.865 |
| mean ESM-1v | 4.421 | 8.341 |
| mean FoldX ΔΔG | 0.818 | 4.964 |
| mean ThermoMPNN ΔΔG | 0.597 | 2.011 |
| **fraction seen in gnomAD** | **8.77%** (1,158) | **4.12%** (287) |
| fraction at the interface | 3.10% | 3.67% |

**Validation:** the damaging cluster is **depleted** in the population — 4.12% of it appears in gnomAD against 8.77% of the tolerant cluster (a 2.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

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
