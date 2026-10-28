# DDX3X — variant-effect analysis

*ATP-dependent RNA helicase DDX3X* · UniProt `O00571` · 662 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 211–403 | 193 |
| Helicase C-terminal | 414–575 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **12.59 Å**, intra-module **3.76 Å**, **ratio 3.35**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 31.8 | 36 | 100% / 100% |
| SWISSMODEL_8q7x-1-C_169-552 | 32.3 | 31 | 100% / 86% |
| SWISSMODEL_8ssw-1-A_134-580 | 50.7 | 0 | 100% / 100% |
| SWISSMODEL_9e2c-1-A_134-574 | 32.0 | 38 | 100% / 99% |

## 2. The inter-domain interface

Most compact structure: `DDX3X_O00571_SWISSMODEL_9e2c-1-A_134-574.pdb`, centroid distance **32.0 Å**, **38 residue pairs** in contact within 5 Å.

**Domain A interface residues (18):** `225, 226, 275, 276, 277, 301, 302, 303, 323, 326, 351, 353, 354, 355, 356, 357, 360, 388`

**Domain B interface residues (18):** `414, 488, 502, 503, 504, 505, 506, 507, 508, 509, 526, 527, 528, 530, 531, 533, 534, 535`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 684 | 11,894 | 0.999 | 0.87 | 2.4e-179 |
| ESM-1v | 684 | 11,894 | -16.561 | -12.589 | 1.5e-131 |
| FoldX ΔΔG | 684 | 8,417 | 1.004 | 1.199 | 6e-06 |
| ThermoMPNN ΔΔG | 684 | 11,894 | 0.675 | 0.343 | 7.3e-08 |
| REVEL | 207 | 3,649 | 0.649 | 0.309 | 2.4e-53 |
| CADD phred | 218 | 3,871 | 28.65 | 24.4 | 9.7e-34 |
| SIFT | 207 | 3,559 | 0.0 | 0.016 | 2.4e-47 |
| PolyPhen-2 HVAR | 207 | 3,649 | 0.992 | 0.49 | 2.6e-36 |
| MetaRNN | 207 | 3,660 | 0.963 | 0.528 | 3.6e-72 |
| VEST4 | 218 | 3,864 | 0.897 | 0.619 | 8.1e-59 |
| PrimateAI | 207 | 3,643 | 0.867 | 0.782 | 1.4e-47 |
| MutationAssessor | 207 | 3,635 | 3.12 | 1.935 | 5.1e-26 |
| PROVEAN | 207 | 3,649 | -5.84 | -3.0 | 2.1e-35 |
| ESM1b | 207 | 3,649 | -13.284 | -10.821 | 9.8e-21 |
| AlphaMissense (dbNSFP) | 207 | 3,654 | 0.999 | 0.778 | 4.6e-66 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,578 |
| ESM-1v | 12,578 |
| FoldX ΔΔG (ProtVar) | 9,101 |
| ThermoMPNN ΔΔG | 12,578 |
| revel | 3,856 |
| cadd | 4,089 |
| sift | 3,766 |
| polyphen | 3,856 |
| metarnn | 3,867 |
| vest4 | 4,082 |
| primateai | 3,850 |
| mutassessor | 3,842 |
| provean | 3,856 |
| esm1b | 3,856 |
| am_dbnsfp | 3,861 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.867 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.471 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.529 |
| AlphaMissense vs revel | +0.811 |
| AlphaMissense vs cadd | +0.772 |
| AlphaMissense vs sift | -0.796 |
| AlphaMissense vs polyphen | +0.762 |
| AlphaMissense vs metarnn | +0.816 |
| AlphaMissense vs vest4 | +0.805 |
| AlphaMissense vs primateai | +0.664 |
| AlphaMissense vs mutassessor | +0.497 |
| AlphaMissense vs provean | -0.767 |
| AlphaMissense vs esm1b | -0.724 |
| AlphaMissense vs am_dbnsfp | +0.970 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.378 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.500 |
| ESM-1v vs revel | -0.830 |
| ESM-1v vs cadd | -0.768 |
| ESM-1v vs sift | +0.786 |
| ESM-1v vs polyphen | -0.747 |
| ESM-1v vs metarnn | -0.822 |
| ESM-1v vs vest4 | -0.796 |
| ESM-1v vs primateai | -0.637 |
| ESM-1v vs mutassessor | -0.447 |
| ESM-1v vs provean | +0.783 |
| ESM-1v vs esm1b | +0.821 |
| ESM-1v vs am_dbnsfp | -0.837 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.697 |
| FoldX ΔΔG (ProtVar) vs revel | +0.436 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.394 |
| FoldX ΔΔG (ProtVar) vs sift | -0.394 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.457 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.442 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.420 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.278 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.367 |
| FoldX ΔΔG (ProtVar) vs provean | -0.402 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.368 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.427 |
| ThermoMPNN ΔΔG vs revel | +0.514 |
| ThermoMPNN ΔΔG vs cadd | +0.473 |
| ThermoMPNN ΔΔG vs sift | -0.472 |
| ThermoMPNN ΔΔG vs polyphen | +0.505 |
| ThermoMPNN ΔΔG vs metarnn | +0.519 |
| ThermoMPNN ΔΔG vs vest4 | +0.521 |
| ThermoMPNN ΔΔG vs primateai | +0.391 |
| ThermoMPNN ΔΔG vs mutassessor | +0.306 |
| ThermoMPNN ΔΔG vs provean | -0.455 |
| ThermoMPNN ΔΔG vs esm1b | -0.495 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.504 |
| revel vs cadd | +0.782 |
| revel vs sift | -0.780 |
| revel vs polyphen | +0.787 |
| revel vs metarnn | +0.927 |
| revel vs vest4 | +0.865 |
| revel vs primateai | +0.702 |
| revel vs mutassessor | +0.455 |
| revel vs provean | -0.794 |
| revel vs esm1b | -0.712 |
| revel vs am_dbnsfp | +0.810 |
| cadd vs sift | -0.839 |
| cadd vs polyphen | +0.811 |
| cadd vs metarnn | +0.818 |
| cadd vs vest4 | +0.756 |
| cadd vs primateai | +0.584 |
| cadd vs mutassessor | +0.475 |
| cadd vs provean | -0.751 |
| cadd vs esm1b | -0.675 |
| cadd vs am_dbnsfp | +0.774 |
| sift vs polyphen | -0.794 |
| sift vs metarnn | -0.814 |
| sift vs vest4 | -0.728 |
| sift vs primateai | -0.552 |
| sift vs mutassessor | -0.559 |
| sift vs provean | +0.765 |
| sift vs esm1b | +0.686 |
| sift vs am_dbnsfp | -0.792 |
| polyphen vs metarnn | +0.790 |
| polyphen vs vest4 | +0.745 |
| polyphen vs primateai | +0.587 |
| polyphen vs mutassessor | +0.475 |
| polyphen vs provean | -0.712 |
| polyphen vs esm1b | -0.638 |
| polyphen vs am_dbnsfp | +0.759 |
| metarnn vs vest4 | +0.874 |
| metarnn vs primateai | +0.705 |
| metarnn vs mutassessor | +0.512 |
| metarnn vs provean | -0.824 |
| metarnn vs esm1b | -0.722 |
| metarnn vs am_dbnsfp | +0.834 |
| vest4 vs primateai | +0.739 |
| vest4 vs mutassessor | +0.425 |
| vest4 vs provean | -0.748 |
| vest4 vs esm1b | -0.681 |
| vest4 vs am_dbnsfp | +0.808 |
| primateai vs mutassessor | +0.251 |
| primateai vs provean | -0.599 |
| primateai vs esm1b | -0.552 |
| primateai vs am_dbnsfp | +0.669 |
| mutassessor vs provean | -0.444 |
| mutassessor vs esm1b | -0.335 |
| mutassessor vs am_dbnsfp | +0.518 |
| provean vs esm1b | +0.718 |
| provean vs am_dbnsfp | -0.764 |
| esm1b vs am_dbnsfp | -0.716 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 125 |
| likely_pathogenic | 65 |
| pathogenic | 30 |
| conflict | 11 |
| likely_benign | 4 |
| other | 3 |
| benign | 1 |

**gnomAD r4 missense variants mapped:** 406

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,732** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 992 | 1,740 |
| mean AlphaMissense | 0.376 | 0.935 |
| mean ESM-1v | 9.011 | 13.929 |
| mean FoldX ΔΔG | 0.475 | 2.568 |
| mean ThermoMPNN ΔΔG | 0.369 | 1.139 |
| mean REVEL | 0.211 | 0.575 |
| mean CADD phred | 20.34 | 28.199 |
| mean SIFT | -0.238 | -0.007 |
| mean PolyPhen-2 HVAR | 0.224 | 0.891 |
| mean MetaRNN | 0.379 | 0.827 |
| mean VEST4 | 0.479 | 0.802 |
| mean PrimateAI | 0.727 | 0.84 |
| mean PROVEAN | 2.01 | 5.556 |
| **fraction seen in gnomAD** | **11.19%** (111) | **3.05%** (53) |
| fraction at the interface | 1.31% | 11.15% |

**Validation:** the damaging cluster is **depleted** in the population — 3.05% of it appears in gnomAD against 11.19% of the tolerant cluster (a 3.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 26 pathogenic / 0 benign, cluster 0 has 0 / 0; OR = nan, p = 1.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 9,101**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,732 | 6,369 |
| mean AlphaMissense | 0.436 | 0.97 |
| mean ESM-1v | 9.862 | 15.857 |
| mean FoldX ΔΔG | 0.444 | 3.038 |
| mean ThermoMPNN ΔΔG | 0.332 | 1.224 |
| **fraction seen in gnomAD** | **5.01%** (137) | **1.33%** (85) |

Depletion **3.8×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 1.65% | 10.03% |

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
