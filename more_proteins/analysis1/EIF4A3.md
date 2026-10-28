# EIF4A3 — variant-effect analysis

*Eukaryotic initiation factor 4A-III* · UniProt `P38919` · 411 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 69–239 | 171 |
| Helicase C-terminal | 250–411 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **6.15 Å**, intra-module **3.71 Å**, **ratio 1.66**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 29.4 | 52 | 100% / 100% |
| SWISSMODEL_4c9b-1-A_21-411 | 47.5 | 3 | 100% / 100% |
| SWISSMODEL_7a5p-1-k_22-411 | 29.3 | 56 | 100% / 100% |
| SWISSMODEL_8xxn-1-a_31-406 | 37.2 | 3 | 100% / 97% |

## 2. The inter-domain interface

Most compact structure: `EIF4A3_P38919_SWISSMODEL_7a5p-1-k_22-411.pdb`, centroid distance **29.3 Å**, **56 residue pairs** in contact within 5 Å.

**Domain A interface residues (25):** `84, 85, 86, 87, 88, 114, 115, 116, 117, 118, 120, 121, 124, 141, 142, 143, 144, 188, 190, 191, 218, 219, 220, 222, 223`

**Domain B interface residues (22):** `307, 313, 316, 317, 320, 324, 336, 337, 339, 340, 341, 342, 359, 360, 362, 363, 366, 367, 370, 371, 395, 396`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 893 | 6,916 | 0.993 | 0.958 | 1.2e-55 |
| ESM-1v | 893 | 6,916 | -13.754 | -10.022 | 4.2e-90 |
| FoldX ΔΔG | 893 | 6,479 | 1.318 | 1.285 | 0.21 |
| ThermoMPNN ΔΔG | 893 | 6,916 | 0.733 | 0.759 | 0.078 |
| REVEL | 269 | 2,167 | 0.587 | 0.323 | 3e-53 |
| CADD phred | 290 | 2,273 | 27.05 | 25.1 | 9.1e-12 |
| SIFT | 269 | 2,167 | 0.0 | 0.002 | 1e-15 |
| PolyPhen-2 HVAR | 269 | 2,167 | 0.992 | 0.544 | 1.2e-34 |
| MetaRNN | 269 | 2,167 | 0.947 | 0.673 | 9.6e-49 |
| VEST4 | 290 | 2,273 | 0.866 | 0.735 | 9.3e-24 |
| PrimateAI | 269 | 2,161 | 0.871 | 0.883 | 0.0044 |
| MutationAssessor | 269 | 2,161 | 3.38 | 1.65 | 1.1e-22 |
| PROVEAN | 269 | 2,167 | -5.34 | -3.67 | 8.7e-14 |
| ESM1b | 269 | 2,167 | -12.753 | -11.316 | 1.8e-12 |
| AlphaMissense (dbNSFP) | 269 | 2,161 | 0.984 | 0.88 | 7e-22 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 7,809 |
| ESM-1v | 7,809 |
| FoldX ΔΔG (ProtVar) | 7,372 |
| ThermoMPNN ΔΔG | 7,809 |
| revel | 2,436 |
| cadd | 2,563 |
| sift | 2,436 |
| polyphen | 2,436 |
| metarnn | 2,436 |
| vest4 | 2,563 |
| primateai | 2,430 |
| mutassessor | 2,430 |
| provean | 2,436 |
| esm1b | 2,436 |
| am_dbnsfp | 2,430 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.848 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.477 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.536 |
| AlphaMissense vs revel | +0.710 |
| AlphaMissense vs cadd | +0.700 |
| AlphaMissense vs sift | -0.764 |
| AlphaMissense vs polyphen | +0.777 |
| AlphaMissense vs metarnn | +0.794 |
| AlphaMissense vs vest4 | +0.755 |
| AlphaMissense vs primateai | +0.340 |
| AlphaMissense vs mutassessor | +0.659 |
| AlphaMissense vs provean | -0.764 |
| AlphaMissense vs esm1b | -0.769 |
| AlphaMissense vs am_dbnsfp | +0.999 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.444 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.492 |
| ESM-1v vs revel | -0.720 |
| ESM-1v vs cadd | -0.678 |
| ESM-1v vs sift | +0.795 |
| ESM-1v vs polyphen | -0.771 |
| ESM-1v vs metarnn | -0.837 |
| ESM-1v vs vest4 | -0.760 |
| ESM-1v vs primateai | -0.170 |
| ESM-1v vs mutassessor | -0.758 |
| ESM-1v vs provean | +0.738 |
| ESM-1v vs esm1b | +0.839 |
| ESM-1v vs am_dbnsfp | -0.841 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.689 |
| FoldX ΔΔG (ProtVar) vs revel | +0.416 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.313 |
| FoldX ΔΔG (ProtVar) vs sift | -0.388 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.430 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.468 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.430 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.151 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.403 |
| FoldX ΔΔG (ProtVar) vs provean | -0.377 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.357 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.439 |
| ThermoMPNN ΔΔG vs revel | +0.490 |
| ThermoMPNN ΔΔG vs cadd | +0.382 |
| ThermoMPNN ΔΔG vs sift | -0.460 |
| ThermoMPNN ΔΔG vs polyphen | +0.524 |
| ThermoMPNN ΔΔG vs metarnn | +0.524 |
| ThermoMPNN ΔΔG vs vest4 | +0.466 |
| ThermoMPNN ΔΔG vs primateai | +0.156 |
| ThermoMPNN ΔΔG vs mutassessor | +0.468 |
| ThermoMPNN ΔΔG vs provean | -0.420 |
| ThermoMPNN ΔΔG vs esm1b | -0.456 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.515 |
| revel vs cadd | +0.610 |
| revel vs sift | -0.688 |
| revel vs polyphen | +0.751 |
| revel vs metarnn | +0.870 |
| revel vs vest4 | +0.764 |
| revel vs primateai | +0.189 |
| revel vs mutassessor | +0.587 |
| revel vs provean | -0.684 |
| revel vs esm1b | -0.653 |
| revel vs am_dbnsfp | +0.710 |
| cadd vs sift | -0.710 |
| cadd vs polyphen | +0.704 |
| cadd vs metarnn | +0.701 |
| cadd vs vest4 | +0.614 |
| cadd vs primateai | +0.267 |
| cadd vs mutassessor | +0.595 |
| cadd vs provean | -0.677 |
| cadd vs esm1b | -0.623 |
| cadd vs am_dbnsfp | +0.696 |
| sift vs polyphen | -0.791 |
| sift vs metarnn | -0.778 |
| sift vs vest4 | -0.668 |
| sift vs primateai | -0.193 |
| sift vs mutassessor | -0.672 |
| sift vs provean | +0.739 |
| sift vs esm1b | +0.710 |
| sift vs am_dbnsfp | -0.770 |
| polyphen vs metarnn | +0.833 |
| polyphen vs vest4 | +0.683 |
| polyphen vs primateai | +0.162 |
| polyphen vs mutassessor | +0.688 |
| polyphen vs provean | -0.707 |
| polyphen vs esm1b | -0.678 |
| polyphen vs am_dbnsfp | +0.774 |
| metarnn vs vest4 | +0.817 |
| metarnn vs primateai | +0.228 |
| metarnn vs mutassessor | +0.738 |
| metarnn vs provean | -0.751 |
| metarnn vs esm1b | -0.710 |
| metarnn vs am_dbnsfp | +0.802 |
| vest4 vs primateai | +0.295 |
| vest4 vs mutassessor | +0.608 |
| vest4 vs provean | -0.703 |
| vest4 vs esm1b | -0.667 |
| vest4 vs am_dbnsfp | +0.759 |
| primateai vs mutassessor | +0.102 |
| primateai vs provean | -0.306 |
| primateai vs esm1b | -0.182 |
| primateai vs am_dbnsfp | +0.335 |
| mutassessor vs provean | -0.558 |
| mutassessor vs esm1b | -0.574 |
| mutassessor vs am_dbnsfp | +0.659 |
| provean vs esm1b | +0.702 |
| provean vs am_dbnsfp | -0.764 |
| esm1b vs am_dbnsfp | -0.769 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 8 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 245

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,305** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 978 | 1,327 |
| mean AlphaMissense | 0.556 | 0.946 |
| mean ESM-1v | 6.077 | 11.46 |
| mean FoldX ΔΔG | 0.545 | 2.713 |
| mean ThermoMPNN ΔΔG | 0.451 | 1.242 |
| mean REVEL | 0.238 | 0.515 |
| mean CADD phred | 21.263 | 27.854 |
| mean SIFT | -0.135 | -0.003 |
| mean PolyPhen-2 HVAR | 0.189 | 0.852 |
| mean MetaRNN | 0.422 | 0.853 |
| mean VEST4 | 0.595 | 0.836 |
| mean PrimateAI | 0.862 | 0.884 |
| mean PROVEAN | 2.352 | 5.505 |
| **fraction seen in gnomAD** | **12.47%** (122) | **6.48%** (86) |
| fraction at the interface | 5.21% | 16.43% |

**Validation:** the damaging cluster is **depleted** in the population — 6.48% of it appears in gnomAD against 12.47% of the tolerant cluster (a 1.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 7,372**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,876 | 3,496 |
| mean AlphaMissense | 0.753 | 0.984 |
| mean ESM-1v | 8.023 | 13.652 |
| mean FoldX ΔΔG | 0.529 | 4.46 |
| mean ThermoMPNN ΔΔG | 0.409 | 1.701 |
| **fraction seen in gnomAD** | **4.23%** (164) | **1.26%** (44) |

Depletion **3.4×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 8.20% | 16.45% |

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
