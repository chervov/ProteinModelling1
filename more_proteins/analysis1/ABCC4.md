# ABCC4 — variant-effect analysis

*ATP-binding cassette sub-family C member 4* · UniProt `O15439` · 1325 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 93–377 | 285 |
| ABC transporter 1 | 410–633 | 224 |
| ABC transmembrane type-1 2 | 711–1005 | 295 |
| ABC transporter 2 | 1041–1274 | 234 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **18.03 Å**, intra-module **5.16 Å**, **ratio 3.49**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 38.5 | 1 | 100% / 100% |
| SWISSMODEL_8i4a-1-A_9-1298 | 50.3 | 0 | 100% / 100% |
| SWISSMODEL_8swn-1-A_47-1298 | 27.5 | 60 | 100% / 100% |
| SWISSMODEL_9dw9-1-A_9-1266 | 28.0 | 50 | 100% / 97% |
| SWISSMODEL_9y1q-1-A_53-1265 | 70.2 | 0 | 100% / 96% |

## 2. The inter-domain interface

Most compact structure: `ABCC4_O15439_SWISSMODEL_8swn-1-A_47-1298.pdb`, centroid distance **27.5 Å**, **60 residue pairs** in contact within 5 Å.

**Domain A interface residues (26):** `445, 446, 447, 448, 480, 481, 512, 515, 516, 519, 521, 536, 537, 538, 539, 540, 542, 560, 563, 564, 565, 566, 567, 569, 592, 594`

**Domain B interface residues (26):** `1055, 1075, 1076, 1077, 1078, 1122, 1123, 1124, 1178, 1179, 1180, 1181, 1182, 1184, 1205, 1206, 1207, 1208, 1209, 1210, 1211, 1233, 1234, 1248, 1249, 1272`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 988 | 24,187 | 0.947 | 0.565 | 9.5e-136 |
| ESM-1v | 988 | 24,187 | -12.806 | -8.567 | 1.2e-145 |
| FoldX ΔΔG | 988 | 22,420 | 0.796 | 1.194 | 2.3e-05 |
| ThermoMPNN ΔΔG | 988 | 24,187 | 0.57 | 0.728 | 1.1e-07 |
| REVEL | 294 | 7,398 | 0.883 | 0.59 | 9.3e-54 |
| CADD phred | 314 | 7,814 | 28.2 | 24.1 | 5.4e-45 |
| SIFT | 294 | 7,398 | 0.001 | 0.027 | 1.5e-55 |
| PolyPhen-2 HVAR | 294 | 7,390 | 0.97 | 0.399 | 4e-49 |
| MetaRNN | 294 | 7,401 | 0.963 | 0.663 | 4.9e-74 |
| VEST4 | 314 | 7,822 | 0.903 | 0.62 | 3.7e-54 |
| PrimateAI | 294 | 7,384 | 0.694 | 0.541 | 5.1e-59 |
| MutationAssessor | 294 | 7,384 | 2.583 | 2.035 | 5e-10 |
| PROVEAN | 294 | 7,398 | -4.685 | -2.89 | 6.3e-34 |
| ESM1b | 294 | 7,398 | -12.184 | -9.384 | 2.8e-32 |
| AlphaMissense (dbNSFP) | 294 | 7,395 | 0.898 | 0.275 | 5.1e-51 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 25,175 |
| ESM-1v | 25,175 |
| FoldX ΔΔG (ProtVar) | 23,408 |
| ThermoMPNN ΔΔG | 25,175 |
| revel | 7,692 |
| cadd | 8,128 |
| sift | 7,692 |
| polyphen | 7,684 |
| metarnn | 7,695 |
| vest4 | 8,136 |
| primateai | 7,678 |
| mutassessor | 7,678 |
| provean | 7,692 |
| esm1b | 7,692 |
| am_dbnsfp | 7,689 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.848 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.487 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.511 |
| AlphaMissense vs revel | +0.809 |
| AlphaMissense vs cadd | +0.755 |
| AlphaMissense vs sift | -0.713 |
| AlphaMissense vs polyphen | +0.770 |
| AlphaMissense vs metarnn | +0.841 |
| AlphaMissense vs vest4 | +0.821 |
| AlphaMissense vs primateai | +0.649 |
| AlphaMissense vs mutassessor | +0.700 |
| AlphaMissense vs provean | -0.734 |
| AlphaMissense vs esm1b | -0.785 |
| AlphaMissense vs am_dbnsfp | +0.999 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.449 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.522 |
| ESM-1v vs revel | -0.790 |
| ESM-1v vs cadd | -0.727 |
| ESM-1v vs sift | +0.739 |
| ESM-1v vs polyphen | -0.761 |
| ESM-1v vs metarnn | -0.838 |
| ESM-1v vs vest4 | -0.779 |
| ESM-1v vs primateai | -0.539 |
| ESM-1v vs mutassessor | -0.752 |
| ESM-1v vs provean | +0.762 |
| ESM-1v vs esm1b | +0.821 |
| ESM-1v vs am_dbnsfp | -0.826 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.678 |
| FoldX ΔΔG (ProtVar) vs revel | +0.457 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.372 |
| FoldX ΔΔG (ProtVar) vs sift | -0.390 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.404 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.460 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.438 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.312 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.418 |
| FoldX ΔΔG (ProtVar) vs provean | -0.451 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.439 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.488 |
| ThermoMPNN ΔΔG vs revel | +0.498 |
| ThermoMPNN ΔΔG vs cadd | +0.420 |
| ThermoMPNN ΔΔG vs sift | -0.437 |
| ThermoMPNN ΔΔG vs polyphen | +0.442 |
| ThermoMPNN ΔΔG vs metarnn | +0.512 |
| ThermoMPNN ΔΔG vs vest4 | +0.476 |
| ThermoMPNN ΔΔG vs primateai | +0.318 |
| ThermoMPNN ΔΔG vs mutassessor | +0.444 |
| ThermoMPNN ΔΔG vs provean | -0.467 |
| ThermoMPNN ΔΔG vs esm1b | -0.500 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.530 |
| revel vs cadd | +0.816 |
| revel vs sift | -0.739 |
| revel vs polyphen | +0.822 |
| revel vs metarnn | +0.921 |
| revel vs vest4 | +0.855 |
| revel vs primateai | +0.680 |
| revel vs mutassessor | +0.681 |
| revel vs provean | -0.754 |
| revel vs esm1b | -0.754 |
| revel vs am_dbnsfp | +0.811 |
| cadd vs sift | -0.730 |
| cadd vs polyphen | +0.815 |
| cadd vs metarnn | +0.834 |
| cadd vs vest4 | +0.799 |
| cadd vs primateai | +0.678 |
| cadd vs mutassessor | +0.614 |
| cadd vs provean | -0.736 |
| cadd vs esm1b | -0.687 |
| cadd vs am_dbnsfp | +0.755 |
| sift vs polyphen | -0.746 |
| sift vs metarnn | -0.772 |
| sift vs vest4 | -0.683 |
| sift vs primateai | -0.518 |
| sift vs mutassessor | -0.653 |
| sift vs provean | +0.734 |
| sift vs esm1b | +0.679 |
| sift vs am_dbnsfp | -0.713 |
| polyphen vs metarnn | +0.849 |
| polyphen vs vest4 | +0.782 |
| polyphen vs primateai | +0.646 |
| polyphen vs mutassessor | +0.692 |
| polyphen vs provean | -0.704 |
| polyphen vs esm1b | -0.706 |
| polyphen vs am_dbnsfp | +0.771 |
| metarnn vs vest4 | +0.869 |
| metarnn vs primateai | +0.710 |
| metarnn vs mutassessor | +0.713 |
| metarnn vs provean | -0.782 |
| metarnn vs esm1b | -0.773 |
| metarnn vs am_dbnsfp | +0.842 |
| vest4 vs primateai | +0.703 |
| vest4 vs mutassessor | +0.664 |
| vest4 vs provean | -0.754 |
| vest4 vs esm1b | -0.735 |
| vest4 vs am_dbnsfp | +0.822 |
| primateai vs mutassessor | +0.410 |
| primateai vs provean | -0.538 |
| primateai vs esm1b | -0.509 |
| primateai vs am_dbnsfp | +0.649 |
| mutassessor vs provean | -0.665 |
| mutassessor vs esm1b | -0.673 |
| mutassessor vs am_dbnsfp | +0.700 |
| provean vs esm1b | +0.712 |
| provean vs am_dbnsfp | -0.734 |
| esm1b vs am_dbnsfp | -0.787 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 30 |
| benign | 4 |
| likely_benign | 2 |

**gnomAD r4 missense variants mapped:** 1,579

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,146** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,213 | 3,933 |
| mean AlphaMissense | 0.17 | 0.67 |
| mean ESM-1v | 5.1 | 10.125 |
| mean FoldX ΔΔG | 0.528 | 2.587 |
| mean ThermoMPNN ΔΔG | 0.418 | 1.243 |
| mean REVEL | 0.346 | 0.797 |
| mean CADD phred | 15.454 | 27.52 |
| mean SIFT | -0.267 | -0.024 |
| mean PolyPhen-2 HVAR | 0.149 | 0.799 |
| mean MetaRNN | 0.317 | 0.873 |
| mean VEST4 | 0.327 | 0.793 |
| mean PrimateAI | 0.438 | 0.64 |
| mean PROVEAN | 1.79 | 4.689 |
| **fraction seen in gnomAD** | **23.28%** (748) | **17.19%** (676) |
| fraction at the interface | 1.00% | 6.66% |

**Validation:** the damaging cluster is **depleted** in the population — 17.19% of it appears in gnomAD against 23.28% of the tolerant cluster (a 1.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 23,408**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 12,097 | 11,311 |
| mean AlphaMissense | 0.325 | 0.877 |
| mean ESM-1v | 6.44 | 12.396 |
| mean FoldX ΔΔG | 0.551 | 3.744 |
| mean ThermoMPNN ΔΔG | 0.435 | 1.559 |
| **fraction seen in gnomAD** | **8.92%** (1,079) | **3.25%** (368) |

Depletion **2.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.27% | 6.30% |

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
