# SMARCAD1 — variant-effect analysis

*SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A containing DEAD/H box 1* · UniProt `Q9H4L7` · 1026 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| CUE 1 | 157–199 | 43 |
| CUE 2 | 251–294 | 44 |
| Helicase ATP-binding | 509–677 | 169 |
| Helicase C-terminal | 858–1010 | 153 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **8.88 Å**, intra-module **5.0 Å**, **ratio 1.78**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 29.3 | 36 | 100% / 100% |
| SWISSMODEL_8oop-1-G_487-1005 | 130.8 | 0 | 100% / 97% |
| SWISSMODEL_8qyv-1-I_486-1006 | 104.9 | 0 | 100% / 97% |
| SWISSMODEL_9c9t-1-K_498-1001 | 133.4 | 0 | 100% / 94% |
| SWISSMODEL_9gcg-1-H_497-1003 | 70.8 | 0 | 100% / 95% |
| SWISSMODEL_9jao-1-A_375-1003 | 28.4 | 53 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `SMARCAD1_Q9H4L7_SWISSMODEL_9jao-1-A_375-1003.pdb`, centroid distance **28.4 Å**, **53 residue pairs** in contact within 5 Å.

**Domain A interface residues (22):** `523, 524, 525, 526, 553, 554, 555, 556, 557, 558, 559, 562, 577, 629, 631, 632, 657, 658, 660, 661, 662, 664`

**Domain B interface residues (25):** `900, 906, 907, 909, 910, 913, 914, 931, 934, 935, 936, 937, 952, 953, 954, 957, 958, 961, 962, 964, 965, 966, 994, 998, 1001`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 893 | 18,601 | 0.99 | 0.447 | 1.1e-241 |
| ESM-1v | 893 | 18,601 | -14.43 | -6.002 | 7e-286 |
| FoldX ΔΔG | 893 | 12,901 | 0.8 | 1.052 | 3.3e-09 |
| ThermoMPNN ΔΔG | 893 | 18,601 | 0.535 | 0.285 | 1.1e-08 |
| REVEL | 276 | 5,742 | 0.869 | 0.34 | 2.8e-78 |
| CADD phred | 290 | 6,111 | 29.35 | 23.6 | 1.9e-48 |
| SIFT | 276 | 5,742 | 0.0 | 0.034 | 1.4e-61 |
| PolyPhen-2 HVAR | 276 | 5,742 | 0.998 | 0.39 | 4.9e-68 |
| MetaRNN | 276 | 5,742 | 0.961 | 0.274 | 1.4e-90 |
| VEST4 | 290 | 6,111 | 0.853 | 0.405 | 1.8e-76 |
| PrimateAI | 276 | 5,734 | 0.826 | 0.65 | 5.2e-80 |
| MutationAssessor | 276 | 5,734 | 3.32 | 1.062 | 1.4e-37 |
| PROVEAN | 276 | 5,742 | -5.1 | -1.52 | 5.7e-62 |
| ESM1b | 276 | 5,742 | -12.35 | -5.947 | 2e-64 |
| AlphaMissense (dbNSFP) | 276 | 5,736 | 0.973 | 0.225 | 2.5e-75 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 19,494 |
| ESM-1v | 19,494 |
| FoldX ΔΔG (ProtVar) | 13,794 |
| ThermoMPNN ΔΔG | 19,494 |
| revel | 6,018 |
| cadd | 6,401 |
| sift | 6,018 |
| polyphen | 6,018 |
| metarnn | 6,018 |
| vest4 | 6,401 |
| primateai | 6,010 |
| mutassessor | 6,010 |
| provean | 6,018 |
| esm1b | 6,018 |
| am_dbnsfp | 6,012 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.798 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.508 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.587 |
| AlphaMissense vs revel | +0.730 |
| AlphaMissense vs cadd | +0.785 |
| AlphaMissense vs sift | -0.697 |
| AlphaMissense vs polyphen | +0.711 |
| AlphaMissense vs metarnn | +0.832 |
| AlphaMissense vs vest4 | +0.820 |
| AlphaMissense vs primateai | +0.748 |
| AlphaMissense vs mutassessor | +0.686 |
| AlphaMissense vs provean | -0.802 |
| AlphaMissense vs esm1b | -0.772 |
| AlphaMissense vs am_dbnsfp | +0.993 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.465 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.558 |
| ESM-1v vs revel | -0.754 |
| ESM-1v vs cadd | -0.766 |
| ESM-1v vs sift | +0.708 |
| ESM-1v vs polyphen | -0.723 |
| ESM-1v vs metarnn | -0.825 |
| ESM-1v vs vest4 | -0.758 |
| ESM-1v vs primateai | -0.617 |
| ESM-1v vs mutassessor | -0.722 |
| ESM-1v vs provean | +0.827 |
| ESM-1v vs esm1b | +0.905 |
| ESM-1v vs am_dbnsfp | -0.755 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.716 |
| FoldX ΔΔG (ProtVar) vs revel | +0.404 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.398 |
| FoldX ΔΔG (ProtVar) vs sift | -0.425 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.396 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.444 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.454 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.269 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.409 |
| FoldX ΔΔG (ProtVar) vs provean | -0.442 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.470 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.496 |
| ThermoMPNN ΔΔG vs revel | +0.522 |
| ThermoMPNN ΔΔG vs cadd | +0.508 |
| ThermoMPNN ΔΔG vs sift | -0.452 |
| ThermoMPNN ΔΔG vs polyphen | +0.450 |
| ThermoMPNN ΔΔG vs metarnn | +0.559 |
| ThermoMPNN ΔΔG vs vest4 | +0.550 |
| ThermoMPNN ΔΔG vs primateai | +0.446 |
| ThermoMPNN ΔΔG vs mutassessor | +0.499 |
| ThermoMPNN ΔΔG vs provean | -0.554 |
| ThermoMPNN ΔΔG vs esm1b | -0.597 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.596 |
| revel vs cadd | +0.665 |
| revel vs sift | -0.540 |
| revel vs polyphen | +0.663 |
| revel vs metarnn | +0.879 |
| revel vs vest4 | +0.782 |
| revel vs primateai | +0.678 |
| revel vs mutassessor | +0.773 |
| revel vs provean | -0.788 |
| revel vs esm1b | -0.760 |
| revel vs am_dbnsfp | +0.726 |
| cadd vs sift | -0.805 |
| cadd vs polyphen | +0.799 |
| cadd vs metarnn | +0.824 |
| cadd vs vest4 | +0.716 |
| cadd vs primateai | +0.652 |
| cadd vs mutassessor | +0.656 |
| cadd vs provean | -0.798 |
| cadd vs esm1b | -0.753 |
| cadd vs am_dbnsfp | +0.786 |
| sift vs polyphen | -0.785 |
| sift vs metarnn | -0.722 |
| sift vs vest4 | -0.688 |
| sift vs primateai | -0.513 |
| sift vs mutassessor | -0.634 |
| sift vs provean | +0.749 |
| sift vs esm1b | +0.684 |
| sift vs am_dbnsfp | -0.697 |
| polyphen vs metarnn | +0.834 |
| polyphen vs vest4 | +0.755 |
| polyphen vs primateai | +0.612 |
| polyphen vs mutassessor | +0.683 |
| polyphen vs provean | -0.726 |
| polyphen vs esm1b | -0.700 |
| polyphen vs am_dbnsfp | +0.706 |
| metarnn vs vest4 | +0.921 |
| metarnn vs primateai | +0.753 |
| metarnn vs mutassessor | +0.779 |
| metarnn vs provean | -0.853 |
| metarnn vs esm1b | -0.814 |
| metarnn vs am_dbnsfp | +0.829 |
| vest4 vs primateai | +0.733 |
| vest4 vs mutassessor | +0.689 |
| vest4 vs provean | -0.787 |
| vest4 vs esm1b | -0.753 |
| vest4 vs am_dbnsfp | +0.819 |
| primateai vs mutassessor | +0.540 |
| primateai vs provean | -0.625 |
| primateai vs esm1b | -0.627 |
| primateai vs am_dbnsfp | +0.752 |
| mutassessor vs provean | -0.764 |
| mutassessor vs esm1b | -0.725 |
| mutassessor vs am_dbnsfp | +0.679 |
| provean vs esm1b | +0.833 |
| provean vs am_dbnsfp | -0.794 |
| esm1b vs am_dbnsfp | -0.768 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 24 |
| benign | 5 |
| likely_benign | 1 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 887

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,222** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,219 | 2,003 |
| mean AlphaMissense | 0.271 | 0.834 |
| mean ESM-1v | 4.759 | 10.796 |
| mean FoldX ΔΔG | 0.532 | 2.596 |
| mean ThermoMPNN ΔΔG | 0.358 | 1.22 |
| mean REVEL | 0.314 | 0.792 |
| mean CADD phred | 20.0 | 29.161 |
| mean SIFT | -0.215 | -0.011 |
| mean PolyPhen-2 HVAR | 0.26 | 0.9 |
| mean MetaRNN | 0.253 | 0.825 |
| mean VEST4 | 0.34 | 0.772 |
| mean PrimateAI | 0.621 | 0.778 |
| mean PROVEAN | 1.289 | 4.875 |
| **fraction seen in gnomAD** | **16.90%** (375) | **6.84%** (137) |
| fraction at the interface | 1.67% | 11.93% |

**Validation:** the damaging cluster is **depleted** in the population — 6.84% of it appears in gnomAD against 16.90% of the tolerant cluster (a 2.5-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 13,794**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 7,707 | 6,087 |
| mean AlphaMissense | 0.435 | 0.949 |
| mean ESM-1v | 5.848 | 12.693 |
| mean FoldX ΔΔG | 0.448 | 3.634 |
| mean ThermoMPNN ΔΔG | 0.332 | 1.566 |
| **fraction seen in gnomAD** | **5.81%** (448) | **1.20%** (73) |

Depletion **4.8×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.52% | 11.48% |

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
