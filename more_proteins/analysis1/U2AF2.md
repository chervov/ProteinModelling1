# U2AF2 — variant-effect analysis

*Splicing factor U2AF 65 kDa subunit* · UniProt `P26368` · 475 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| RRM 1 | 149–231 | 83 |
| RRM 2 | 259–337 | 79 |
| RRM 3 | 385–466 | 82 |

**Pair analysed:** RRM 1 ↔ RRM 2

**AlphaFold PAE:** inter-module mean **7.51 Å**, intra-module **2.96 Å**, **ratio 2.53**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 26.7 | 5 | 100% / 100% |
| SWISSMODEL_6tr0-1-A_140-342 | 37.5 | 0 | 100% / 100% |
| SWISSMODEL_7s3a-1-A_142-340 | 25.8 | 16 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `U2AF2_P26368_SWISSMODEL_7s3a-1-A_142-340.pdb`, centroid distance **25.8 Å**, **16 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `155, 216, 218, 220, 221, 222, 223, 225`

**Domain B interface residues (8):** `271, 272, 273, 276, 288, 289, 290, 292`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 8,721 | 0.983 | 0.906 | 1.5e-13 |
| ESM-1v | 304 | 8,721 | -13.292 | -11.353 | 1.4e-16 |
| FoldX ΔΔG | 304 | 7,087 | 0.99 | 0.932 | 0.96 |
| ThermoMPNN ΔΔG | 304 | 8,721 | 0.664 | 0.467 | 0.13 |
| REVEL | 99 | 2,668 | 0.326 | 0.228 | 1.4e-10 |
| CADD phred | 105 | 2,783 | 26.4 | 24.1 | 0.00044 |
| SIFT | 99 | 2,668 | 0.02 | 0.028 | 0.41 |
| PolyPhen-2 HVAR | 99 | 2,668 | 0.886 | 0.475 | 0.0046 |
| MetaRNN | 99 | 2,668 | 0.725 | 0.378 | 5.2e-12 |
| VEST4 | 105 | 2,778 | 0.729 | 0.572 | 1.9e-13 |
| PrimateAI | 99 | 2,662 | 0.833 | 0.844 | 0.3 |
| MutationAssessor | 99 | 2,662 | 2.12 | 2.192 | 0.89 |
| PROVEAN | 99 | 2,668 | -4.63 | -3.425 | 3.8e-05 |
| ESM1b | 99 | 2,668 | -13.375 | -11.774 | 0.0055 |
| AlphaMissense (dbNSFP) | 99 | 2,662 | 0.965 | 0.774 | 6e-05 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 9,025 |
| ESM-1v | 9,025 |
| FoldX ΔΔG (ProtVar) | 7,391 |
| ThermoMPNN ΔΔG | 9,025 |
| revel | 2,767 |
| cadd | 2,888 |
| sift | 2,767 |
| polyphen | 2,767 |
| metarnn | 2,767 |
| vest4 | 2,883 |
| primateai | 2,761 |
| mutassessor | 2,761 |
| provean | 2,767 |
| esm1b | 2,767 |
| am_dbnsfp | 2,761 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.878 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.499 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.611 |
| AlphaMissense vs revel | +0.783 |
| AlphaMissense vs cadd | +0.744 |
| AlphaMissense vs sift | -0.681 |
| AlphaMissense vs polyphen | +0.773 |
| AlphaMissense vs metarnn | +0.816 |
| AlphaMissense vs vest4 | +0.755 |
| AlphaMissense vs primateai | +0.282 |
| AlphaMissense vs mutassessor | +0.677 |
| AlphaMissense vs provean | -0.751 |
| AlphaMissense vs esm1b | -0.729 |
| AlphaMissense vs am_dbnsfp | +0.986 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.437 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.587 |
| ESM-1v vs revel | -0.765 |
| ESM-1v vs cadd | -0.720 |
| ESM-1v vs sift | +0.661 |
| ESM-1v vs polyphen | -0.723 |
| ESM-1v vs metarnn | -0.812 |
| ESM-1v vs vest4 | -0.738 |
| ESM-1v vs primateai | -0.241 |
| ESM-1v vs mutassessor | -0.677 |
| ESM-1v vs provean | +0.772 |
| ESM-1v vs esm1b | +0.839 |
| ESM-1v vs am_dbnsfp | -0.850 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.703 |
| FoldX ΔΔG (ProtVar) vs revel | +0.483 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.442 |
| FoldX ΔΔG (ProtVar) vs sift | -0.420 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.465 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.508 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.481 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.237 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.478 |
| FoldX ΔΔG (ProtVar) vs provean | -0.488 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.349 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.477 |
| ThermoMPNN ΔΔG vs revel | +0.574 |
| ThermoMPNN ΔΔG vs cadd | +0.503 |
| ThermoMPNN ΔΔG vs sift | -0.461 |
| ThermoMPNN ΔΔG vs polyphen | +0.512 |
| ThermoMPNN ΔΔG vs metarnn | +0.591 |
| ThermoMPNN ΔΔG vs vest4 | +0.563 |
| ThermoMPNN ΔΔG vs primateai | +0.156 |
| ThermoMPNN ΔΔG vs mutassessor | +0.510 |
| ThermoMPNN ΔΔG vs provean | -0.502 |
| ThermoMPNN ΔΔG vs esm1b | -0.471 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.590 |
| revel vs cadd | +0.706 |
| revel vs sift | -0.638 |
| revel vs polyphen | +0.716 |
| revel vs metarnn | +0.879 |
| revel vs vest4 | +0.819 |
| revel vs primateai | +0.162 |
| revel vs mutassessor | +0.641 |
| revel vs provean | -0.729 |
| revel vs esm1b | -0.621 |
| revel vs am_dbnsfp | +0.784 |
| cadd vs sift | -0.802 |
| cadd vs polyphen | +0.794 |
| cadd vs metarnn | +0.784 |
| cadd vs vest4 | +0.701 |
| cadd vs primateai | +0.237 |
| cadd vs mutassessor | +0.679 |
| cadd vs provean | -0.683 |
| cadd vs esm1b | -0.607 |
| cadd vs am_dbnsfp | +0.748 |
| sift vs polyphen | -0.771 |
| sift vs metarnn | -0.719 |
| sift vs vest4 | -0.608 |
| sift vs primateai | -0.211 |
| sift vs mutassessor | -0.705 |
| sift vs provean | +0.647 |
| sift vs esm1b | +0.561 |
| sift vs am_dbnsfp | -0.697 |
| polyphen vs metarnn | +0.825 |
| polyphen vs vest4 | +0.687 |
| polyphen vs primateai | +0.235 |
| polyphen vs mutassessor | +0.728 |
| polyphen vs provean | -0.709 |
| polyphen vs esm1b | -0.589 |
| polyphen vs am_dbnsfp | +0.778 |
| metarnn vs vest4 | +0.902 |
| metarnn vs primateai | +0.245 |
| metarnn vs mutassessor | +0.729 |
| metarnn vs provean | -0.771 |
| metarnn vs esm1b | -0.655 |
| metarnn vs am_dbnsfp | +0.824 |
| vest4 vs primateai | +0.272 |
| vest4 vs mutassessor | +0.619 |
| vest4 vs provean | -0.681 |
| vest4 vs esm1b | -0.592 |
| vest4 vs am_dbnsfp | +0.759 |
| primateai vs mutassessor | +0.210 |
| primateai vs provean | -0.194 |
| primateai vs esm1b | -0.178 |
| primateai vs am_dbnsfp | +0.285 |
| mutassessor vs provean | -0.654 |
| mutassessor vs esm1b | -0.545 |
| mutassessor vs am_dbnsfp | +0.680 |
| provean vs esm1b | +0.629 |
| provean vs am_dbnsfp | -0.735 |
| esm1b vs am_dbnsfp | -0.731 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 10 |
| likely_pathogenic | 6 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 256

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,274** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,081 | 1,193 |
| mean AlphaMissense | 0.488 | 0.949 |
| mean ESM-1v | 7.941 | 13.275 |
| mean FoldX ΔΔG | 0.483 | 2.659 |
| mean ThermoMPNN ΔΔG | 0.38 | 1.354 |
| mean REVEL | 0.173 | 0.405 |
| mean CADD phred | 20.202 | 28.177 |
| mean SIFT | -0.217 | -0.02 |
| mean PolyPhen-2 HVAR | 0.227 | 0.87 |
| mean MetaRNN | 0.275 | 0.736 |
| mean VEST4 | 0.459 | 0.741 |
| mean PrimateAI | 0.813 | 0.849 |
| mean PROVEAN | 2.404 | 5.556 |
| **fraction seen in gnomAD** | **10.64%** (115) | **2.60%** (31) |
| fraction at the interface | 2.50% | 6.04% |

**Validation:** the damaging cluster is **depleted** in the population — 2.60% of it appears in gnomAD against 10.64% of the tolerant cluster (a 4.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 7,391**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,856 | 3,535 |
| mean AlphaMissense | 0.657 | 0.983 |
| mean ESM-1v | 9.7 | 15.391 |
| mean FoldX ΔΔG | 0.385 | 3.522 |
| mean ThermoMPNN ΔΔG | 0.313 | 1.697 |
| **fraction seen in gnomAD** | **3.45%** (133) | **0.42%** (15) |

Depletion **8.2×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 4.10% | 4.13% |

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
