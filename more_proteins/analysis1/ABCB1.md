# ABCB1 — variant-effect analysis

*ATP-dependent translocase ABCB1* · UniProt `P08183` · 1280 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 51–357 | 307 |
| ABC transporter 1 | 392–628 | 237 |
| ABC transmembrane type-1 2 | 711–1000 | 290 |
| ABC transporter 2 | 1035–1273 | 239 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **14.97 Å**, intra-module **4.38 Å**, **ratio 3.42**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 44.4 | 0 | 100% / 100% |
| SWISSMODEL_6s7p-1-A_36-1252 | 28.0 | 78 | 100% / 91% |
| SWISSMODEL_9ctc-1-A_30-1272 | 34.4 | 15 | 100% / 100% |
| SWISSMODEL_9oe2-1-A_30-1276 | 62.2 | 0 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `ABCB1_P08183_SWISSMODEL_6s7p-1-A_36-1252.pdb`, centroid distance **28.0 Å**, **78 residue pairs** in contact within 5 Å.

**Domain A interface residues (36):** `403, 404, 407, 427, 428, 429, 430, 475, 476, 477, 515, 516, 517, 522, 523, 527, 530, 531, 532, 533, 534, 535, 536, 538, 556, 559, 560, 561, 562, 563, 565, 566, 587, 588, 625, 628`

**Domain B interface residues (38):** `1046, 1047, 1049, 1050, 1070, 1071, 1072, 1073, 1118, 1119, 1120, 1121, 1157, 1161, 1162, 1167, 1168, 1172, 1175, 1176, 1177, 1178, 1179, 1180, 1181, 1182, 1183, 1201, 1203, 1204, 1205, 1206, 1207, 1208, 1209, 1210, 1212, 1232`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,406 | 22,914 | 0.969 | 0.653 | 1.8e-181 |
| ESM-1v | 1,406 | 22,914 | -12.965 | -8.179 | 1.3e-211 |
| FoldX ΔΔG | 1,406 | 21,223 | 0.562 | 1.184 | 1.7e-30 |
| ThermoMPNN ΔΔG | 1,406 | 22,914 | 0.575 | 0.73 | 1.3e-10 |
| REVEL | 431 | 7,068 | 0.853 | 0.607 | 2.9e-55 |
| CADD phred | 458 | 7,436 | 28.4 | 24.2 | 6.2e-44 |
| SIFT | 431 | 7,068 | 0.001 | 0.019 | 3.3e-61 |
| PolyPhen-2 HVAR | 431 | 7,068 | 0.977 | 0.774 | 2.1e-20 |
| MetaRNN | 431 | 7,068 | 0.962 | 0.619 | 7.7e-80 |
| VEST4 | 458 | 7,436 | 0.854 | 0.59 | 2.4e-53 |
| PrimateAI | 431 | 7,062 | 0.711 | 0.515 | 9e-95 |
| MutationAssessor | 431 | 7,062 | 2.285 | 2.07 | 4.4e-05 |
| PROVEAN | 431 | 7,068 | -4.71 | -3.29 | 6.8e-32 |
| ESM1b | 431 | 7,068 | -13.014 | -10.122 | 2.3e-33 |
| AlphaMissense (dbNSFP) | 431 | 7,062 | 0.927 | 0.338 | 2e-66 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 24,320 |
| ESM-1v | 24,320 |
| FoldX ΔΔG (ProtVar) | 22,629 |
| ThermoMPNN ΔΔG | 24,320 |
| revel | 7,499 |
| cadd | 7,894 |
| sift | 7,499 |
| polyphen | 7,499 |
| metarnn | 7,499 |
| vest4 | 7,894 |
| primateai | 7,493 |
| mutassessor | 7,493 |
| provean | 7,499 |
| esm1b | 7,499 |
| am_dbnsfp | 7,493 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.847 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.452 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.512 |
| AlphaMissense vs revel | +0.815 |
| AlphaMissense vs cadd | +0.780 |
| AlphaMissense vs sift | -0.759 |
| AlphaMissense vs polyphen | +0.726 |
| AlphaMissense vs metarnn | +0.852 |
| AlphaMissense vs vest4 | +0.829 |
| AlphaMissense vs primateai | +0.679 |
| AlphaMissense vs mutassessor | +0.693 |
| AlphaMissense vs provean | -0.736 |
| AlphaMissense vs esm1b | -0.843 |
| AlphaMissense vs am_dbnsfp | +0.999 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.430 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.513 |
| ESM-1v vs revel | -0.786 |
| ESM-1v vs cadd | -0.762 |
| ESM-1v vs sift | +0.801 |
| ESM-1v vs polyphen | -0.705 |
| ESM-1v vs metarnn | -0.828 |
| ESM-1v vs vest4 | -0.781 |
| ESM-1v vs primateai | -0.599 |
| ESM-1v vs mutassessor | -0.681 |
| ESM-1v vs provean | +0.717 |
| ESM-1v vs esm1b | +0.848 |
| ESM-1v vs am_dbnsfp | -0.820 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.661 |
| FoldX ΔΔG (ProtVar) vs revel | +0.443 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.380 |
| FoldX ΔΔG (ProtVar) vs sift | -0.427 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.393 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.447 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.437 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.277 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.386 |
| FoldX ΔΔG (ProtVar) vs provean | -0.436 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.446 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.477 |
| ThermoMPNN ΔΔG vs revel | +0.534 |
| ThermoMPNN ΔΔG vs cadd | +0.463 |
| ThermoMPNN ΔΔG vs sift | -0.509 |
| ThermoMPNN ΔΔG vs polyphen | +0.471 |
| ThermoMPNN ΔΔG vs metarnn | +0.549 |
| ThermoMPNN ΔΔG vs vest4 | +0.531 |
| ThermoMPNN ΔΔG vs primateai | +0.345 |
| ThermoMPNN ΔΔG vs mutassessor | +0.448 |
| ThermoMPNN ΔΔG vs provean | -0.487 |
| ThermoMPNN ΔΔG vs esm1b | -0.550 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.566 |
| revel vs cadd | +0.832 |
| revel vs sift | -0.800 |
| revel vs polyphen | +0.815 |
| revel vs metarnn | +0.915 |
| revel vs vest4 | +0.878 |
| revel vs primateai | +0.745 |
| revel vs mutassessor | +0.703 |
| revel vs provean | -0.779 |
| revel vs esm1b | -0.792 |
| revel vs am_dbnsfp | +0.815 |
| cadd vs sift | -0.821 |
| cadd vs polyphen | +0.772 |
| cadd vs metarnn | +0.850 |
| cadd vs vest4 | +0.817 |
| cadd vs primateai | +0.704 |
| cadd vs mutassessor | +0.623 |
| cadd vs provean | -0.749 |
| cadd vs esm1b | -0.769 |
| cadd vs am_dbnsfp | +0.778 |
| sift vs polyphen | -0.725 |
| sift vs metarnn | -0.829 |
| sift vs vest4 | -0.774 |
| sift vs primateai | -0.610 |
| sift vs mutassessor | -0.627 |
| sift vs provean | +0.752 |
| sift vs esm1b | +0.773 |
| sift vs am_dbnsfp | -0.759 |
| polyphen vs metarnn | +0.817 |
| polyphen vs vest4 | +0.770 |
| polyphen vs primateai | +0.689 |
| polyphen vs mutassessor | +0.583 |
| polyphen vs provean | -0.728 |
| polyphen vs esm1b | -0.722 |
| polyphen vs am_dbnsfp | +0.726 |
| metarnn vs vest4 | +0.935 |
| metarnn vs primateai | +0.750 |
| metarnn vs mutassessor | +0.684 |
| metarnn vs provean | -0.792 |
| metarnn vs esm1b | -0.816 |
| metarnn vs am_dbnsfp | +0.851 |
| vest4 vs primateai | +0.747 |
| vest4 vs mutassessor | +0.669 |
| vest4 vs provean | -0.778 |
| vest4 vs esm1b | -0.795 |
| vest4 vs am_dbnsfp | +0.829 |
| primateai vs mutassessor | +0.453 |
| primateai vs provean | -0.600 |
| primateai vs esm1b | -0.613 |
| primateai vs am_dbnsfp | +0.678 |
| mutassessor vs provean | -0.607 |
| mutassessor vs esm1b | -0.682 |
| mutassessor vs am_dbnsfp | +0.694 |
| provean vs esm1b | +0.763 |
| provean vs am_dbnsfp | -0.734 |
| esm1b vs am_dbnsfp | -0.842 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| other | 103 |
| VUS | 23 |
| likely_benign | 5 |
| benign | 3 |
| pathogenic | 1 |
| likely_pathogenic | 1 |
| conflict | 1 |

**gnomAD r4 missense variants mapped:** 1,459

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,977** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,962 | 4,015 |
| mean AlphaMissense | 0.195 | 0.719 |
| mean ESM-1v | 4.81 | 10.091 |
| mean FoldX ΔΔG | 0.546 | 2.706 |
| mean ThermoMPNN ΔΔG | 0.387 | 1.21 |
| mean REVEL | 0.369 | 0.796 |
| mean CADD phred | 15.678 | 28.15 |
| mean SIFT | -0.254 | -0.012 |
| mean PolyPhen-2 HVAR | 0.284 | 0.894 |
| mean MetaRNN | 0.275 | 0.859 |
| mean VEST4 | 0.303 | 0.779 |
| mean PrimateAI | 0.418 | 0.617 |
| mean PROVEAN | 1.906 | 4.992 |
| **fraction seen in gnomAD** | **22.38%** (663) | **16.99%** (682) |
| fraction at the interface | 2.36% | 8.99% |

**Validation:** the damaging cluster is **depleted** in the population — 16.99% of it appears in gnomAD against 22.38% of the tolerant cluster (a 1.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 22,629**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 11,535 | 11,094 |
| mean AlphaMissense | 0.378 | 0.912 |
| mean ESM-1v | 6.112 | 12.434 |
| mean FoldX ΔΔG | 0.609 | 4.13 |
| mean ThermoMPNN ΔΔG | 0.404 | 1.516 |
| **fraction seen in gnomAD** | **8.48%** (978) | **3.31%** (367) |

Depletion **2.6×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.42% | 9.12% |

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
