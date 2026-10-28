# SMARCA2 — variant-effect analysis

*SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 2* · UniProt `P51531` · 1590 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| QLQ | 173–208 | 36 |
| HSA | 436–508 | 73 |
| Helicase ATP-binding | 736–901 | 166 |
| Helicase C-terminal | 1054–1216 | 163 |
| Bromo | 1378–1506 | 129 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **8.66 Å**, intra-module **5.08 Å**, **ratio 1.7**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 28.5 | 31 | 100% / 100% |
| 9rl4.1.I (78.7% id) | 33.7 | 16 | 100% / 100% |
| 9rn1.1.I (78.7% id) | 30.2 | 23 | 100% / 100% |
| 7egp.1.H (47.5% id) | 26.3 | 61 | 100% / 100% |
| 7y8r.1.J (78.7% id) | 26.2 | 51 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P51531_7egp-1-H.pdb`, centroid distance **26.3 Å**, **61 residue pairs** in contact within 5 Å.

**Domain A interface residues (27):** `750, 751, 752, 753, 781, 782, 783, 784, 786, 787, 790, 791, 805, 806, 807, 852, 854, 855, 880, 881, 882, 883, 884, 885, 886, 887, 888`

**Domain B interface residues (29):** `1101, 1102, 1105, 1106, 1109, 1110, 1127, 1128, 1129, 1131, 1132, 1133, 1134, 1148, 1149, 1150, 1151, 1154, 1155, 1158, 1159, 1161, 1162, 1163, 1191, 1194, 1195, 1198, 1199`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,064 | 29,146 | 0.998 | 0.88 | 1.1e-222 |
| ESM-1v | 1,064 | 29,146 | -15.169 | -6.245 | <1e-300 |
| FoldX ΔΔG | 1,064 | 19,475 | 0.855 | 0.711 | 0.025 |
| ThermoMPNN ΔΔG | 1,064 | 29,146 | 0.575 | 0.232 | 1.4e-38 |
| REVEL | 274 | 7,379 | 0.908 | 0.472 | 5.3e-93 |
| CADD phred | 287 | 7,813 | 26.1 | 24.5 | 1.4e-16 |
| SIFT | 274 | 7,380 | 0.0 | 0.02 | 1.9e-65 |
| PolyPhen-2 HVAR | 274 | 7,379 | 0.987 | 0.927 | 9.2e-14 |
| MetaRNN | 274 | 7,403 | 0.964 | 0.558 | 6.2e-93 |
| VEST4 | 287 | 7,814 | 0.912 | 0.678 | 8.7e-69 |
| PrimateAI | 274 | 7,365 | 0.888 | 0.834 | 1.5e-34 |
| MutationAssessor | 274 | 7,365 | 3.513 | 1.765 | 3.6e-43 |
| PROVEAN | 274 | 7,380 | -5.55 | -2.75 | 9.4e-42 |
| ESM1b | 274 | 7,367 | -14.018 | -10.634 | 2.8e-34 |
| AlphaMissense (dbNSFP) | 274 | 7,402 | 0.993 | 0.722 | 2.7e-60 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 30,210 |
| ESM-1v | 30,210 |
| FoldX ΔΔG (ProtVar) | 20,539 |
| ThermoMPNN ΔΔG | 30,210 |
| revel | 7,653 |
| cadd | 8,100 |
| sift | 7,654 |
| polyphen | 7,653 |
| metarnn | 7,677 |
| vest4 | 8,101 |
| primateai | 7,639 |
| mutassessor | 7,639 |
| provean | 7,654 |
| esm1b | 7,641 |
| am_dbnsfp | 7,676 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.567 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.390 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.463 |
| AlphaMissense vs revel | +0.716 |
| AlphaMissense vs cadd | +0.540 |
| AlphaMissense vs sift | -0.681 |
| AlphaMissense vs polyphen | +0.604 |
| AlphaMissense vs metarnn | +0.812 |
| AlphaMissense vs vest4 | +0.785 |
| AlphaMissense vs primateai | +0.736 |
| AlphaMissense vs mutassessor | +0.640 |
| AlphaMissense vs provean | -0.789 |
| AlphaMissense vs esm1b | -0.795 |
| AlphaMissense vs am_dbnsfp | +0.953 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.405 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.405 |
| ESM-1v vs revel | -0.547 |
| ESM-1v vs cadd | -0.383 |
| ESM-1v vs sift | +0.578 |
| ESM-1v vs polyphen | -0.342 |
| ESM-1v vs metarnn | -0.605 |
| ESM-1v vs vest4 | -0.551 |
| ESM-1v vs primateai | -0.433 |
| ESM-1v vs mutassessor | -0.431 |
| ESM-1v vs provean | +0.545 |
| ESM-1v vs esm1b | +0.590 |
| ESM-1v vs am_dbnsfp | -0.550 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.665 |
| FoldX ΔΔG (ProtVar) vs revel | +0.384 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.248 |
| FoldX ΔΔG (ProtVar) vs sift | -0.362 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.199 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.408 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.372 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.201 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.328 |
| FoldX ΔΔG (ProtVar) vs provean | -0.344 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.314 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.378 |
| ThermoMPNN ΔΔG vs revel | +0.451 |
| ThermoMPNN ΔΔG vs cadd | +0.296 |
| ThermoMPNN ΔΔG vs sift | -0.389 |
| ThermoMPNN ΔΔG vs polyphen | +0.243 |
| ThermoMPNN ΔΔG vs metarnn | +0.479 |
| ThermoMPNN ΔΔG vs vest4 | +0.437 |
| ThermoMPNN ΔΔG vs primateai | +0.329 |
| ThermoMPNN ΔΔG vs mutassessor | +0.378 |
| ThermoMPNN ΔΔG vs provean | -0.431 |
| ThermoMPNN ΔΔG vs esm1b | -0.471 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.469 |
| revel vs cadd | +0.541 |
| revel vs sift | -0.716 |
| revel vs polyphen | +0.589 |
| revel vs metarnn | +0.897 |
| revel vs vest4 | +0.776 |
| revel vs primateai | +0.608 |
| revel vs mutassessor | +0.604 |
| revel vs provean | -0.741 |
| revel vs esm1b | -0.676 |
| revel vs am_dbnsfp | +0.743 |
| cadd vs sift | -0.610 |
| cadd vs polyphen | +0.545 |
| cadd vs metarnn | +0.617 |
| cadd vs vest4 | +0.592 |
| cadd vs primateai | +0.395 |
| cadd vs mutassessor | +0.492 |
| cadd vs provean | -0.617 |
| cadd vs esm1b | -0.512 |
| cadd vs am_dbnsfp | +0.541 |
| sift vs polyphen | -0.524 |
| sift vs metarnn | -0.773 |
| sift vs vest4 | -0.676 |
| sift vs primateai | -0.504 |
| sift vs mutassessor | -0.662 |
| sift vs provean | +0.724 |
| sift vs esm1b | +0.621 |
| sift vs am_dbnsfp | -0.674 |
| polyphen vs metarnn | +0.670 |
| polyphen vs vest4 | +0.642 |
| polyphen vs primateai | +0.507 |
| polyphen vs mutassessor | +0.531 |
| polyphen vs provean | -0.583 |
| polyphen vs esm1b | -0.515 |
| polyphen vs am_dbnsfp | +0.603 |
| metarnn vs vest4 | +0.897 |
| metarnn vs primateai | +0.687 |
| metarnn vs mutassessor | +0.696 |
| metarnn vs provean | -0.814 |
| metarnn vs esm1b | -0.743 |
| metarnn vs am_dbnsfp | +0.833 |
| vest4 vs primateai | +0.669 |
| vest4 vs mutassessor | +0.637 |
| vest4 vs provean | -0.731 |
| vest4 vs esm1b | -0.695 |
| vest4 vs am_dbnsfp | +0.803 |
| primateai vs mutassessor | +0.451 |
| primateai vs provean | -0.627 |
| primateai vs esm1b | -0.627 |
| primateai vs am_dbnsfp | +0.731 |
| mutassessor vs provean | -0.643 |
| mutassessor vs esm1b | -0.583 |
| mutassessor vs am_dbnsfp | +0.613 |
| provean vs esm1b | +0.760 |
| provean vs am_dbnsfp | -0.786 |
| esm1b vs am_dbnsfp | -0.784 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 229 |
| likely_benign | 62 |
| likely_pathogenic | 53 |
| pathogenic | 38 |
| conflict | 21 |
| benign | 15 |

**gnomAD r4 missense variants mapped:** 1,613

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 5,247** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,909 | 3,338 |
| mean AlphaMissense | 0.448 | 0.929 |
| mean ESM-1v | 4.717 | 9.127 |
| mean FoldX ΔΔG | 0.401 | 1.792 |
| mean ThermoMPNN ΔΔG | 0.298 | 0.924 |
| mean REVEL | 0.325 | 0.736 |
| mean CADD phred | 22.524 | 27.19 |
| mean SIFT | -0.213 | -0.017 |
| mean PolyPhen-2 HVAR | 0.482 | 0.88 |
| mean MetaRNN | 0.371 | 0.832 |
| mean VEST4 | 0.509 | 0.817 |
| mean PrimateAI | 0.791 | 0.875 |
| mean PROVEAN | 1.918 | 5.183 |
| **fraction seen in gnomAD** | **17.18%** (328) | **7.82%** (261) |
| fraction at the interface | 1.15% | 7.55% |

**Validation:** the damaging cluster is **depleted** in the population — 7.82% of it appears in gnomAD against 17.18% of the tolerant cluster (a 2.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 31 pathogenic / 0 benign, cluster 0 has 0 / 2; OR = inf, p = 0.0019.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 20,539**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 14,049 | 6,490 |
| mean AlphaMissense | 0.768 | 0.987 |
| mean ESM-1v | 6.503 | 13.136 |
| mean FoldX ΔΔG | 0.401 | 3.928 |
| mean ThermoMPNN ΔΔG | 0.315 | 1.702 |
| **fraction seen in gnomAD** | **4.61%** (648) | **1.17%** (76) |

Depletion **3.9×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.80% | 10.32% |

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
