# SRC — variant-effect analysis

*Proto-oncogene tyrosine-protein kinase Src* · UniProt `P12931` · 536 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH3 | 84–145 | 62 |
| SH2 | 151–248 | 98 |
| Protein kinase | 270–523 | 254 |

**Pair analysed:** SH3 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **8.44 Å**, intra-module **3.84 Å**, **ratio 2.2**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 36.2 | 8 | 100% / 100% |
| 8jn9.1.A (100.0% id) | 35.9 | 8 | 97% / 100% |
| 1y57.1.A (100.0% id) | 37.3 | 9 | 97% / 100% |

## 2. The inter-domain interface

Most compact structure: `P12931_1y57-1-A.pdb`, centroid distance **37.3 Å**, **9 residue pairs** in contact within 5 Å.

**Domain A interface residues (4):** `97, 98, 99, 100`

**Domain B interface residues (5):** `308, 311, 315, 318, 333`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 171 | 10,013 | 0.952 | 0.958 | 0.77 |
| ESM-1v | 171 | 10,013 | -9.551 | -9.268 | 0.33 |
| FoldX ΔΔG | 171 | 8,379 | 0.578 | 1.303 | 1.2e-09 |
| ThermoMPNN ΔΔG | 171 | 10,013 | 0.668 | 0.755 | 0.092 |
| REVEL | 51 | 3,086 | 0.463 | 0.508 | 0.62 |
| CADD phred | 56 | 3,240 | 26.15 | 26.35 | 0.64 |
| SIFT | 51 | 3,086 | 0.021 | 0.004 | 0.22 |
| PolyPhen-2 HVAR | 51 | 3,086 | 0.88 | 0.96 | 0.77 |
| MetaRNN | 51 | 3,086 | 0.744 | 0.773 | 0.34 |
| VEST4 | 56 | 3,240 | 0.663 | 0.727 | 0.12 |
| PrimateAI | 51 | 3,080 | 0.849 | 0.839 | 0.46 |
| MutationAssessor | 51 | 3,080 | 1.35 | 1.462 | 0.14 |
| PROVEAN | 51 | 3,086 | -2.91 | -3.21 | 0.38 |
| ESM1b | 51 | 3,086 | -10.816 | -10.204 | 0.31 |
| AlphaMissense (dbNSFP) | 51 | 3,080 | 0.805 | 0.884 | 0.94 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 10,184 |
| ESM-1v | 10,184 |
| FoldX ΔΔG (ProtVar) | 8,550 |
| ThermoMPNN ΔΔG | 10,184 |
| revel | 3,137 |
| cadd | 3,296 |
| sift | 3,137 |
| polyphen | 3,137 |
| metarnn | 3,137 |
| vest4 | 3,296 |
| primateai | 3,131 |
| mutassessor | 3,131 |
| provean | 3,137 |
| esm1b | 3,137 |
| am_dbnsfp | 3,131 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.862 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.535 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.638 |
| AlphaMissense vs revel | +0.747 |
| AlphaMissense vs cadd | +0.744 |
| AlphaMissense vs sift | -0.785 |
| AlphaMissense vs polyphen | +0.668 |
| AlphaMissense vs metarnn | +0.869 |
| AlphaMissense vs vest4 | +0.854 |
| AlphaMissense vs primateai | +0.678 |
| AlphaMissense vs mutassessor | +0.692 |
| AlphaMissense vs provean | -0.802 |
| AlphaMissense vs esm1b | -0.853 |
| AlphaMissense vs am_dbnsfp | +0.999 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.546 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.647 |
| ESM-1v vs revel | -0.734 |
| ESM-1v vs cadd | -0.712 |
| ESM-1v vs sift | +0.782 |
| ESM-1v vs polyphen | -0.640 |
| ESM-1v vs metarnn | -0.866 |
| ESM-1v vs vest4 | -0.822 |
| ESM-1v vs primateai | -0.579 |
| ESM-1v vs mutassessor | -0.757 |
| ESM-1v vs provean | +0.806 |
| ESM-1v vs esm1b | +0.891 |
| ESM-1v vs am_dbnsfp | -0.853 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.693 |
| FoldX ΔΔG (ProtVar) vs revel | +0.420 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.356 |
| FoldX ΔΔG (ProtVar) vs sift | -0.423 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.407 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.550 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.498 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.248 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.499 |
| FoldX ΔΔG (ProtVar) vs provean | -0.504 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.480 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.526 |
| ThermoMPNN ΔΔG vs revel | +0.548 |
| ThermoMPNN ΔΔG vs cadd | +0.540 |
| ThermoMPNN ΔΔG vs sift | -0.556 |
| ThermoMPNN ΔΔG vs polyphen | +0.528 |
| ThermoMPNN ΔΔG vs metarnn | +0.652 |
| ThermoMPNN ΔΔG vs vest4 | +0.623 |
| ThermoMPNN ΔΔG vs primateai | +0.391 |
| ThermoMPNN ΔΔG vs mutassessor | +0.641 |
| ThermoMPNN ΔΔG vs provean | -0.609 |
| ThermoMPNN ΔΔG vs esm1b | -0.624 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.638 |
| revel vs cadd | +0.708 |
| revel vs sift | -0.696 |
| revel vs polyphen | +0.676 |
| revel vs metarnn | +0.843 |
| revel vs vest4 | +0.745 |
| revel vs primateai | +0.575 |
| revel vs mutassessor | +0.582 |
| revel vs provean | -0.736 |
| revel vs esm1b | -0.724 |
| revel vs am_dbnsfp | +0.747 |
| cadd vs sift | -0.762 |
| cadd vs polyphen | +0.721 |
| cadd vs metarnn | +0.767 |
| cadd vs vest4 | +0.726 |
| cadd vs primateai | +0.546 |
| cadd vs mutassessor | +0.638 |
| cadd vs provean | -0.746 |
| cadd vs esm1b | -0.727 |
| cadd vs am_dbnsfp | +0.744 |
| sift vs polyphen | -0.611 |
| sift vs metarnn | -0.798 |
| sift vs vest4 | -0.733 |
| sift vs primateai | -0.531 |
| sift vs mutassessor | -0.668 |
| sift vs provean | +0.795 |
| sift vs esm1b | +0.772 |
| sift vs am_dbnsfp | -0.787 |
| polyphen vs metarnn | +0.750 |
| polyphen vs vest4 | +0.707 |
| polyphen vs primateai | +0.572 |
| polyphen vs mutassessor | +0.558 |
| polyphen vs provean | -0.658 |
| polyphen vs esm1b | -0.629 |
| polyphen vs am_dbnsfp | +0.667 |
| metarnn vs vest4 | +0.933 |
| metarnn vs primateai | +0.651 |
| metarnn vs mutassessor | +0.738 |
| metarnn vs provean | -0.825 |
| metarnn vs esm1b | -0.836 |
| metarnn vs am_dbnsfp | +0.872 |
| vest4 vs primateai | +0.671 |
| vest4 vs mutassessor | +0.703 |
| vest4 vs provean | -0.785 |
| vest4 vs esm1b | -0.805 |
| vest4 vs am_dbnsfp | +0.854 |
| primateai vs mutassessor | +0.454 |
| primateai vs provean | -0.576 |
| primateai vs esm1b | -0.566 |
| primateai vs am_dbnsfp | +0.675 |
| mutassessor vs provean | -0.693 |
| mutassessor vs esm1b | -0.677 |
| mutassessor vs am_dbnsfp | +0.691 |
| provean vs esm1b | +0.791 |
| provean vs am_dbnsfp | -0.802 |
| esm1b vs am_dbnsfp | -0.854 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 11 |
| likely_benign | 1 |
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 496

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,630** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 900 | 1,730 |
| mean AlphaMissense | 0.436 | 0.937 |
| mean ESM-1v | 5.61 | 11.222 |
| mean FoldX ΔΔG | 0.478 | 2.762 |
| mean ThermoMPNN ΔΔG | 0.461 | 1.429 |
| mean REVEL | 0.317 | 0.69 |
| mean CADD phred | 22.367 | 29.154 |
| mean SIFT | -0.172 | -0.008 |
| mean PolyPhen-2 HVAR | 0.454 | 0.909 |
| mean MetaRNN | 0.468 | 0.892 |
| mean VEST4 | 0.525 | 0.832 |
| mean PrimateAI | 0.778 | 0.864 |
| mean PROVEAN | 1.78 | 5.349 |
| **fraction seen in gnomAD** | **19.00%** (171) | **10.46%** (181) |
| fraction at the interface | 2.33% | 1.73% |

**Validation:** the damaging cluster is **depleted** in the population — 10.46% of it appears in gnomAD against 19.00% of the tolerant cluster (a 1.8-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 8,550**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,232 | 4,318 |
| mean AlphaMissense | 0.675 | 0.988 |
| mean ESM-1v | 7.34 | 14.02 |
| mean FoldX ΔΔG | 0.499 | 4.16 |
| mean ThermoMPNN ΔΔG | 0.509 | 1.854 |
| **fraction seen in gnomAD** | **6.52%** (276) | **1.78%** (77) |

Depletion **3.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.79% | 1.23% |

## 6. ProteinGym

**Present**, so published experimental data and precomputed baseline scores exist:

| DMS_id | mutants | selection | region |
|---|--:|---|---|
| `SRC_HUMAN_Ahler_2019` | 3,372 | Activity | 270-519 |
| `SRC_HUMAN_Chakraborty_2023_binding-DAS_25uM` | 3,637 | Activity | 270-519 |
| `SRC_HUMAN_Nguyen_2022` | 3,366 | OrganismalFitness | 270-519 |

Fold definitions (`fold_random_5`, `fold_modulo_5`, `fold_contiguous_5`) ship with the benchmark; `fold_modulo_5` is the by-position split and the honest one. See `external_data/ddg_study.md` §8 and the ProteinGym notes in `external_data/ddg_docs_review.md`.

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
