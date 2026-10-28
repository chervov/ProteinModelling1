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
| REVEL | 220 | 6,721 | 0.547 | 0.306 | 1.3e-14 |
| CADD phred | 232 | 7,070 | 27.1 | 23.6 | 3.5e-18 |
| SIFT | 220 | 6,721 | 0.008 | 0.022 | 0.28 |
| PolyPhen-2 HVAR | 220 | 6,674 | 0.875 | 0.57 | 5.9e-08 |
| MetaRNN | 220 | 6,791 | 0.683 | 0.429 | 1.5e-05 |
| VEST4 | 232 | 6,969 | 0.609 | 0.469 | 1.1e-06 |
| PrimateAI | 220 | 6,655 | 0.625 | 0.469 | 5.3e-29 |
| MutationAssessor | 220 | 6,655 | 1.22 | 1.935 | 1.8e-13 |
| PROVEAN | 220 | 6,721 | -3.265 | -2.35 | 1e-05 |
| ESM1b | 220 | 6,661 | -10.547 | -8.689 | 3.5e-07 |
| AlphaMissense (dbNSFP) | 220 | 6,783 | 0.365 | 0.187 | 3.1e-06 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 22,553 |
| ESM-1v | 22,553 |
| FoldX ΔΔG (ProtVar) | 20,178 |
| ThermoMPNN ΔΔG | 22,553 |
| revel | 6,941 |
| cadd | 7,302 |
| sift | 6,941 |
| polyphen | 6,894 |
| metarnn | 7,011 |
| vest4 | 7,201 |
| primateai | 6,875 |
| mutassessor | 6,875 |
| provean | 6,941 |
| esm1b | 6,881 |
| am_dbnsfp | 7,003 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.543 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.536 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.591 |
| AlphaMissense vs revel | +0.753 |
| AlphaMissense vs cadd | +0.806 |
| AlphaMissense vs sift | -0.709 |
| AlphaMissense vs polyphen | +0.773 |
| AlphaMissense vs metarnn | +0.843 |
| AlphaMissense vs vest4 | +0.846 |
| AlphaMissense vs primateai | +0.764 |
| AlphaMissense vs mutassessor | +0.532 |
| AlphaMissense vs provean | -0.752 |
| AlphaMissense vs esm1b | -0.769 |
| AlphaMissense vs am_dbnsfp | +0.981 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.359 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.384 |
| ESM-1v vs revel | -0.530 |
| ESM-1v vs cadd | -0.535 |
| ESM-1v vs sift | +0.499 |
| ESM-1v vs polyphen | -0.526 |
| ESM-1v vs metarnn | -0.562 |
| ESM-1v vs vest4 | -0.504 |
| ESM-1v vs primateai | -0.420 |
| ESM-1v vs mutassessor | -0.360 |
| ESM-1v vs provean | +0.493 |
| ESM-1v vs esm1b | +0.532 |
| ESM-1v vs am_dbnsfp | -0.507 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.689 |
| FoldX ΔΔG (ProtVar) vs revel | +0.434 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.400 |
| FoldX ΔΔG (ProtVar) vs sift | -0.409 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.419 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.520 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.508 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.356 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.401 |
| FoldX ΔΔG (ProtVar) vs provean | -0.464 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.450 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.536 |
| ThermoMPNN ΔΔG vs revel | +0.473 |
| ThermoMPNN ΔΔG vs cadd | +0.480 |
| ThermoMPNN ΔΔG vs sift | -0.481 |
| ThermoMPNN ΔΔG vs polyphen | +0.486 |
| ThermoMPNN ΔΔG vs metarnn | +0.576 |
| ThermoMPNN ΔΔG vs vest4 | +0.578 |
| ThermoMPNN ΔΔG vs primateai | +0.440 |
| ThermoMPNN ΔΔG vs mutassessor | +0.464 |
| ThermoMPNN ΔΔG vs provean | -0.506 |
| ThermoMPNN ΔΔG vs esm1b | -0.549 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.602 |
| revel vs cadd | +0.800 |
| revel vs sift | -0.673 |
| revel vs polyphen | +0.799 |
| revel vs metarnn | +0.857 |
| revel vs vest4 | +0.809 |
| revel vs primateai | +0.739 |
| revel vs mutassessor | +0.393 |
| revel vs provean | -0.733 |
| revel vs esm1b | -0.661 |
| revel vs am_dbnsfp | +0.759 |
| cadd vs sift | -0.746 |
| cadd vs polyphen | +0.832 |
| cadd vs metarnn | +0.847 |
| cadd vs vest4 | +0.831 |
| cadd vs primateai | +0.745 |
| cadd vs mutassessor | +0.453 |
| cadd vs provean | -0.749 |
| cadd vs esm1b | -0.724 |
| cadd vs am_dbnsfp | +0.796 |
| sift vs polyphen | -0.754 |
| sift vs metarnn | -0.767 |
| sift vs vest4 | -0.725 |
| sift vs primateai | -0.590 |
| sift vs mutassessor | -0.573 |
| sift vs provean | +0.773 |
| sift vs esm1b | +0.639 |
| sift vs am_dbnsfp | -0.705 |
| polyphen vs metarnn | +0.848 |
| polyphen vs vest4 | +0.813 |
| polyphen vs primateai | +0.729 |
| polyphen vs mutassessor | +0.536 |
| polyphen vs provean | -0.753 |
| polyphen vs esm1b | -0.695 |
| polyphen vs am_dbnsfp | +0.779 |
| metarnn vs vest4 | +0.919 |
| metarnn vs primateai | +0.762 |
| metarnn vs mutassessor | +0.578 |
| metarnn vs provean | -0.837 |
| metarnn vs esm1b | -0.755 |
| metarnn vs am_dbnsfp | +0.852 |
| vest4 vs primateai | +0.764 |
| vest4 vs mutassessor | +0.553 |
| vest4 vs provean | -0.790 |
| vest4 vs esm1b | -0.751 |
| vest4 vs am_dbnsfp | +0.851 |
| primateai vs mutassessor | +0.357 |
| primateai vs provean | -0.622 |
| primateai vs esm1b | -0.594 |
| primateai vs am_dbnsfp | +0.762 |
| mutassessor vs provean | -0.575 |
| mutassessor vs esm1b | -0.510 |
| mutassessor vs am_dbnsfp | +0.533 |
| provean vs esm1b | +0.737 |
| provean vs am_dbnsfp | -0.759 |
| esm1b vs am_dbnsfp | -0.767 |

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

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,144** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,138 | 3,006 |
| mean AlphaMissense | 0.152 | 0.624 |
| mean ESM-1v | 3.891 | 6.511 |
| mean FoldX ΔΔG | 0.736 | 3.136 |
| mean ThermoMPNN ΔΔG | 0.54 | 1.473 |
| mean REVEL | 0.195 | 0.621 |
| mean CADD phred | 14.442 | 27.685 |
| mean SIFT | -0.25 | -0.016 |
| mean PolyPhen-2 HVAR | 0.256 | 0.901 |
| mean MetaRNN | 0.251 | 0.832 |
| mean VEST4 | 0.301 | 0.737 |
| mean PrimateAI | 0.401 | 0.619 |
| mean PROVEAN | 1.427 | 4.892 |
| **fraction seen in gnomAD** | **24.12%** (757) | **18.53%** (557) |
| fraction at the interface | 2.23% | 4.62% |

**Validation:** the damaging cluster is **depleted** in the population — 18.53% of it appears in gnomAD against 24.12% of the tolerant cluster (a 1.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 20,178**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 13,204 | 6,974 |
| mean AlphaMissense | 0.321 | 0.865 |
| mean ESM-1v | 4.421 | 8.341 |
| mean FoldX ΔΔG | 0.818 | 4.964 |
| mean ThermoMPNN ΔΔG | 0.597 | 2.011 |
| **fraction seen in gnomAD** | **8.77%** (1,158) | **4.12%** (287) |

Depletion **2.1×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.10% | 3.67% |

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
