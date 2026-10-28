# ABCC2 — variant-effect analysis

*ATP-binding cassette sub-family C member 2* · UniProt `Q92887` · 1545 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 322–605 | 284 |
| ABC transporter 1 | 637–861 | 225 |
| ABC transmembrane type-1 2 | 979–1264 | 286 |
| ABC transporter 2 | 1300–1534 | 235 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **14.86 Å**, intra-module **5.06 Å**, **ratio 2.94**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.1 | 6 | 100% / 100% |
| SWISSMODEL_7w4o-1-H_24-1530 | 27.7 | 40 | 100% / 98% |
| SWISSMODEL_8rq3-1-A_2-1534 | 49.5 | 0 | 100% / 100% |
| SWISSMODEL_9dw9-1-A_192-1535 | 27.6 | 63 | 100% / 100% |
| SWISSMODEL_9jn1-1-A_1-1516 | 46.6 | 0 | 100% / 92% |

## 2. The inter-domain interface

Most compact structure: `ABCC2_Q92887_SWISSMODEL_9dw9-1-A_192-1535.pdb`, centroid distance **27.6 Å**, **63 residue pairs** in contact within 5 Å.

**Domain A interface residues (30):** `671, 672, 673, 674, 706, 738, 741, 742, 747, 757, 760, 762, 763, 764, 765, 766, 768, 786, 789, 790, 791, 792, 793, 794, 795, 797, 820, 821, 822, 823`

**Domain B interface residues (27):** `1310, 1314, 1334, 1335, 1336, 1337, 1382, 1383, 1418, 1438, 1439, 1440, 1441, 1462, 1465, 1466, 1467, 1468, 1470, 1471, 1493, 1495, 1527, 1528, 1530, 1531, 1533`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,083 | 28,272 | 0.913 | 0.482 | 7e-138 |
| ESM-1v | 1,083 | 28,272 | -11.918 | -6.15 | 1.1e-223 |
| FoldX ΔΔG | 1,083 | 25,973 | 0.751 | 1.102 | 2.3e-11 |
| ThermoMPNN ΔΔG | 1,083 | 28,272 | 0.563 | 0.683 | 9.6e-08 |
| REVEL | 305 | 7,946 | 0.854 | 0.448 | 2.7e-51 |
| CADD phred | 315 | 8,343 | 27.2 | 23.9 | 7.1e-32 |
| SIFT | 305 | 7,946 | 0.0 | 0.022 | 1.3e-52 |
| PolyPhen-2 HVAR | 305 | 7,946 | 0.997 | 0.598 | 3.9e-40 |
| MetaRNN | 305 | 7,946 | 0.957 | 0.582 | 2.7e-57 |
| VEST4 | 315 | 8,343 | 0.876 | 0.519 | 1.5e-42 |
| PrimateAI | 305 | 7,940 | 0.603 | 0.444 | 8.1e-51 |
| MutationAssessor | 305 | 7,940 | 2.235 | 2.0 | 3.3e-05 |
| PROVEAN | 305 | 7,946 | -4.58 | -2.49 | 4.4e-34 |
| ESM1b | 305 | 7,946 | -11.066 | -6.5 | 3.3e-49 |
| AlphaMissense (dbNSFP) | 305 | 7,940 | 0.8 | 0.22 | 1e-43 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 29,355 |
| ESM-1v | 29,355 |
| FoldX ΔΔG (ProtVar) | 27,056 |
| ThermoMPNN ΔΔG | 29,355 |
| revel | 8,251 |
| cadd | 8,658 |
| sift | 8,251 |
| polyphen | 8,251 |
| metarnn | 8,251 |
| vest4 | 8,658 |
| primateai | 8,245 |
| mutassessor | 8,245 |
| provean | 8,251 |
| esm1b | 8,251 |
| am_dbnsfp | 8,245 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.748 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.469 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.512 |
| AlphaMissense vs revel | +0.754 |
| AlphaMissense vs cadd | +0.762 |
| AlphaMissense vs sift | -0.735 |
| AlphaMissense vs polyphen | +0.763 |
| AlphaMissense vs metarnn | +0.832 |
| AlphaMissense vs vest4 | +0.841 |
| AlphaMissense vs primateai | +0.705 |
| AlphaMissense vs mutassessor | +0.674 |
| AlphaMissense vs provean | -0.763 |
| AlphaMissense vs esm1b | -0.792 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.385 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.448 |
| ESM-1v vs revel | -0.751 |
| ESM-1v vs cadd | -0.714 |
| ESM-1v vs sift | +0.758 |
| ESM-1v vs polyphen | -0.709 |
| ESM-1v vs metarnn | -0.787 |
| ESM-1v vs vest4 | -0.725 |
| ESM-1v vs primateai | -0.551 |
| ESM-1v vs mutassessor | -0.631 |
| ESM-1v vs provean | +0.734 |
| ESM-1v vs esm1b | +0.887 |
| ESM-1v vs am_dbnsfp | -0.720 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.663 |
| FoldX ΔΔG (ProtVar) vs revel | +0.402 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.351 |
| FoldX ΔΔG (ProtVar) vs sift | -0.401 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.369 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.435 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.424 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.310 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.371 |
| FoldX ΔΔG (ProtVar) vs provean | -0.438 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.425 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.476 |
| ThermoMPNN ΔΔG vs revel | +0.447 |
| ThermoMPNN ΔΔG vs cadd | +0.404 |
| ThermoMPNN ΔΔG vs sift | -0.451 |
| ThermoMPNN ΔΔG vs polyphen | +0.416 |
| ThermoMPNN ΔΔG vs metarnn | +0.498 |
| ThermoMPNN ΔΔG vs vest4 | +0.488 |
| ThermoMPNN ΔΔG vs primateai | +0.340 |
| ThermoMPNN ΔΔG vs mutassessor | +0.413 |
| ThermoMPNN ΔΔG vs provean | -0.460 |
| ThermoMPNN ΔΔG vs esm1b | -0.508 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.539 |
| revel vs cadd | +0.788 |
| revel vs sift | -0.757 |
| revel vs polyphen | +0.821 |
| revel vs metarnn | +0.903 |
| revel vs vest4 | +0.813 |
| revel vs primateai | +0.728 |
| revel vs mutassessor | +0.618 |
| revel vs provean | -0.776 |
| revel vs esm1b | -0.791 |
| revel vs am_dbnsfp | +0.755 |
| cadd vs sift | -0.801 |
| cadd vs polyphen | +0.827 |
| cadd vs metarnn | +0.841 |
| cadd vs vest4 | +0.819 |
| cadd vs primateai | +0.731 |
| cadd vs mutassessor | +0.624 |
| cadd vs provean | -0.780 |
| cadd vs esm1b | -0.762 |
| cadd vs am_dbnsfp | +0.762 |
| sift vs polyphen | -0.747 |
| sift vs metarnn | -0.806 |
| sift vs vest4 | -0.746 |
| sift vs primateai | -0.604 |
| sift vs mutassessor | -0.611 |
| sift vs provean | +0.812 |
| sift vs esm1b | +0.800 |
| sift vs am_dbnsfp | -0.735 |
| polyphen vs metarnn | +0.881 |
| polyphen vs vest4 | +0.846 |
| polyphen vs primateai | +0.755 |
| polyphen vs mutassessor | +0.655 |
| polyphen vs provean | -0.769 |
| polyphen vs esm1b | -0.757 |
| polyphen vs am_dbnsfp | +0.763 |
| metarnn vs vest4 | +0.882 |
| metarnn vs primateai | +0.771 |
| metarnn vs mutassessor | +0.703 |
| metarnn vs provean | -0.826 |
| metarnn vs esm1b | -0.830 |
| metarnn vs am_dbnsfp | +0.833 |
| vest4 vs primateai | +0.773 |
| vest4 vs mutassessor | +0.690 |
| vest4 vs provean | -0.793 |
| vest4 vs esm1b | -0.776 |
| vest4 vs am_dbnsfp | +0.842 |
| primateai vs mutassessor | +0.517 |
| primateai vs provean | -0.653 |
| primateai vs esm1b | -0.608 |
| primateai vs am_dbnsfp | +0.705 |
| mutassessor vs provean | -0.660 |
| mutassessor vs esm1b | -0.681 |
| mutassessor vs am_dbnsfp | +0.674 |
| provean vs esm1b | +0.809 |
| provean vs am_dbnsfp | -0.763 |
| esm1b vs am_dbnsfp | -0.792 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 190 |
| conflict | 31 |
| likely_benign | 14 |
| benign | 6 |
| likely_pathogenic | 5 |
| pathogenic | 4 |

**gnomAD r4 missense variants mapped:** 1,952

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,579** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,575 | 4,004 |
| mean AlphaMissense | 0.157 | 0.619 |
| mean ESM-1v | 4.097 | 8.512 |
| mean FoldX ΔΔG | 0.565 | 2.441 |
| mean ThermoMPNN ΔΔG | 0.428 | 1.221 |
| mean REVEL | 0.256 | 0.761 |
| mean CADD phred | 13.671 | 27.595 |
| mean SIFT | -0.282 | -0.015 |
| mean PolyPhen-2 HVAR | 0.208 | 0.9 |
| mean MetaRNN | 0.262 | 0.878 |
| mean VEST4 | 0.275 | 0.78 |
| mean PrimateAI | 0.365 | 0.562 |
| mean PROVEAN | 1.162 | 4.845 |
| **fraction seen in gnomAD** | **22.46%** (803) | **20.65%** (827) |
| fraction at the interface | 1.43% | 6.34% |

**Validation:** the damaging cluster is **depleted** in the population — 20.65% of it appears in gnomAD against 22.46% of the tolerant cluster (a 1.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 3 pathogenic / 1 benign, cluster 0 has 1 / 3; OR = 9.0, p = 0.49.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 27,056**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 15,917 | 11,139 |
| mean AlphaMissense | 0.329 | 0.867 |
| mean ESM-1v | 5.11 | 10.712 |
| mean FoldX ΔΔG | 0.608 | 3.707 |
| mean ThermoMPNN ΔΔG | 0.465 | 1.653 |
| **fraction seen in gnomAD** | **8.32%** (1,324) | **4.26%** (475) |

Depletion **2.0×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.27% | 6.48% |

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
