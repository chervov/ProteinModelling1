# DDX23 — variant-effect analysis

*Probable ATP-dependent RNA helicase DDX23* · UniProt `Q9BUQ8` · 820 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 422–627 | 206 |
| Helicase C-terminal | 651–799 | 149 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **17.1 Å**, intra-module **3.92 Å**, **ratio 4.36**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.6 | 15 | 100% / 100% |
| SWISSMODEL_2hxy-3-A_392-781 | 34.0 | 33 | 100% / 88% |
| SWISSMODEL_4c9b-1-A_392-781 | 46.7 | 1 | 100% / 88% |
| SWISSMODEL_4kbf-1-A_393-779 | 35.2 | 35 | 100% / 87% |
| SWISSMODEL_4kbf-2-A_393-779 | 56.3 | 0 | 100% / 87% |
| SWISSMODEL_6ah0-1-s_352-790 | 43.1 | 0 | 100% / 94% |
| SWISSMODEL_6o5f-1-A_375-803 | 45.7 | 0 | 100% / 100% |
| SWISSMODEL_6qw6-1-X_158-806 | 41.6 | 5 | 100% / 100% |
| SWISSMODEL_8y6o-1-I_158-806 | 35.5 | 18 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `DDX23_Q9BUQ8_SWISSMODEL_4kbf-1-A_393-779.pdb`, centroid distance **35.2 Å**, **35 residue pairs** in contact within 5 Å.

**Domain A interface residues (14):** `436, 437, 476, 477, 480, 483, 550, 552, 553, 556, 607, 608, 609, 610`

**Domain B interface residues (16):** `711, 712, 728, 729, 730, 731, 732, 753, 754, 755, 756, 757, 758, 759, 760, 761`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 570 | 15,010 | 0.999 | 0.936 | 9.1e-92 |
| ESM-1v | 570 | 15,010 | -17.258 | -11.855 | 1.4e-131 |
| FoldX ΔΔG | 570 | 12,331 | 0.897 | 0.757 | 0.5 |
| ThermoMPNN ΔΔG | 570 | 15,010 | 0.581 | 0.347 | 2.4e-06 |
| REVEL | 178 | 4,681 | 0.649 | 0.265 | 9.9e-46 |
| CADD phred | 187 | 4,970 | 29.8 | 25.1 | 1.5e-22 |
| SIFT | 178 | 4,681 | 0.001 | 0.022 | 1.8e-26 |
| PolyPhen-2 HVAR | 178 | 4,643 | 0.993 | 0.737 | 1.3e-34 |
| MetaRNN | 178 | 4,681 | 0.952 | 0.493 | 3.9e-50 |
| VEST4 | 187 | 4,929 | 0.824 | 0.576 | 7e-22 |
| PrimateAI | 178 | 4,637 | 0.85 | 0.835 | 0.00088 |
| MutationAssessor | 178 | 4,628 | 3.223 | 1.835 | 8.4e-25 |
| PROVEAN | 178 | 4,681 | -4.99 | -2.77 | 5.3e-19 |
| ESM1b | 178 | 4,643 | -13.499 | -9.596 | 8.2e-22 |
| AlphaMissense (dbNSFP) | 178 | 4,675 | 0.997 | 0.8 | 7.4e-29 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 15,580 |
| ESM-1v | 15,580 |
| FoldX ΔΔG (ProtVar) | 12,901 |
| ThermoMPNN ΔΔG | 15,580 |
| revel | 4,859 |
| cadd | 5,157 |
| sift | 4,859 |
| polyphen | 4,821 |
| metarnn | 4,859 |
| vest4 | 5,116 |
| primateai | 4,815 |
| mutassessor | 4,806 |
| provean | 4,859 |
| esm1b | 4,821 |
| am_dbnsfp | 4,853 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.846 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.380 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.433 |
| AlphaMissense vs revel | +0.744 |
| AlphaMissense vs cadd | +0.715 |
| AlphaMissense vs sift | -0.621 |
| AlphaMissense vs polyphen | +0.687 |
| AlphaMissense vs metarnn | +0.792 |
| AlphaMissense vs vest4 | +0.740 |
| AlphaMissense vs primateai | +0.584 |
| AlphaMissense vs mutassessor | +0.575 |
| AlphaMissense vs provean | -0.760 |
| AlphaMissense vs esm1b | -0.758 |
| AlphaMissense vs am_dbnsfp | +0.986 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.382 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.459 |
| ESM-1v vs revel | -0.784 |
| ESM-1v vs cadd | -0.755 |
| ESM-1v vs sift | +0.672 |
| ESM-1v vs polyphen | -0.693 |
| ESM-1v vs metarnn | -0.841 |
| ESM-1v vs vest4 | -0.753 |
| ESM-1v vs primateai | -0.497 |
| ESM-1v vs mutassessor | -0.554 |
| ESM-1v vs provean | +0.833 |
| ESM-1v vs esm1b | +0.895 |
| ESM-1v vs am_dbnsfp | -0.834 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.668 |
| FoldX ΔΔG (ProtVar) vs revel | +0.431 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.304 |
| FoldX ΔΔG (ProtVar) vs sift | -0.380 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.342 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.415 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.402 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.182 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.293 |
| FoldX ΔΔG (ProtVar) vs provean | -0.398 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.415 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.380 |
| ThermoMPNN ΔΔG vs revel | +0.472 |
| ThermoMPNN ΔΔG vs cadd | +0.381 |
| ThermoMPNN ΔΔG vs sift | -0.386 |
| ThermoMPNN ΔΔG vs polyphen | +0.379 |
| ThermoMPNN ΔΔG vs metarnn | +0.489 |
| ThermoMPNN ΔΔG vs vest4 | +0.481 |
| ThermoMPNN ΔΔG vs primateai | +0.254 |
| ThermoMPNN ΔΔG vs mutassessor | +0.290 |
| ThermoMPNN ΔΔG vs provean | -0.463 |
| ThermoMPNN ΔΔG vs esm1b | -0.469 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.446 |
| revel vs cadd | +0.722 |
| revel vs sift | -0.609 |
| revel vs polyphen | +0.754 |
| revel vs metarnn | +0.915 |
| revel vs vest4 | +0.845 |
| revel vs primateai | +0.581 |
| revel vs mutassessor | +0.460 |
| revel vs provean | -0.781 |
| revel vs esm1b | -0.725 |
| revel vs am_dbnsfp | +0.749 |
| cadd vs sift | -0.715 |
| cadd vs polyphen | +0.736 |
| cadd vs metarnn | +0.777 |
| cadd vs vest4 | +0.491 |
| cadd vs primateai | +0.425 |
| cadd vs mutassessor | +0.505 |
| cadd vs provean | -0.740 |
| cadd vs esm1b | -0.712 |
| cadd vs am_dbnsfp | +0.705 |
| sift vs polyphen | -0.642 |
| sift vs metarnn | -0.653 |
| sift vs vest4 | -0.581 |
| sift vs primateai | -0.263 |
| sift vs mutassessor | -0.635 |
| sift vs provean | +0.637 |
| sift vs esm1b | +0.671 |
| sift vs am_dbnsfp | -0.621 |
| polyphen vs metarnn | +0.783 |
| polyphen vs vest4 | +0.647 |
| polyphen vs primateai | +0.406 |
| polyphen vs mutassessor | +0.516 |
| polyphen vs provean | -0.702 |
| polyphen vs esm1b | -0.655 |
| polyphen vs am_dbnsfp | +0.688 |
| metarnn vs vest4 | +0.907 |
| metarnn vs primateai | +0.575 |
| metarnn vs mutassessor | +0.516 |
| metarnn vs provean | -0.820 |
| metarnn vs esm1b | -0.773 |
| metarnn vs am_dbnsfp | +0.801 |
| vest4 vs primateai | +0.591 |
| vest4 vs mutassessor | +0.446 |
| vest4 vs provean | -0.719 |
| vest4 vs esm1b | -0.693 |
| vest4 vs am_dbnsfp | +0.744 |
| primateai vs mutassessor | +0.233 |
| primateai vs provean | -0.501 |
| primateai vs esm1b | -0.443 |
| primateai vs am_dbnsfp | +0.583 |
| mutassessor vs provean | -0.508 |
| mutassessor vs esm1b | -0.534 |
| mutassessor vs am_dbnsfp | +0.575 |
| provean vs esm1b | +0.796 |
| provean vs am_dbnsfp | -0.769 |
| esm1b vs am_dbnsfp | -0.761 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 44 |
| likely_pathogenic | 3 |
| conflict | 2 |
| likely_benign | 1 |

**gnomAD r4 missense variants mapped:** 738

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,999** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,723 | 2,276 |
| mean AlphaMissense | 0.5 | 0.941 |
| mean ESM-1v | 8.037 | 13.736 |
| mean FoldX ΔΔG | 0.472 | 2.235 |
| mean ThermoMPNN ΔΔG | 0.332 | 0.986 |
| mean REVEL | 0.189 | 0.514 |
| mean CADD phred | 21.828 | 29.402 |
| mean SIFT | -0.235 | -0.022 |
| mean PolyPhen-2 HVAR | 0.286 | 0.894 |
| mean MetaRNN | 0.335 | 0.811 |
| mean VEST4 | 0.484 | 0.783 |
| mean PrimateAI | 0.805 | 0.864 |
| mean PROVEAN | 1.726 | 5.22 |
| **fraction seen in gnomAD** | **16.31%** (281) | **7.16%** (163) |
| fraction at the interface | 1.51% | 6.68% |

**Validation:** the damaging cluster is **depleted** in the population — 7.16% of it appears in gnomAD against 16.31% of the tolerant cluster (a 2.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 12,901**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,716 | 4,185 |
| mean AlphaMissense | 0.763 | 0.985 |
| mean ESM-1v | 11.27 | 16.563 |
| mean FoldX ΔΔG | 0.442 | 4.404 |
| mean ThermoMPNN ΔΔG | 0.313 | 1.681 |
| **fraction seen in gnomAD** | **5.42%** (472) | **1.39%** (58) |

Depletion **3.9×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.14% | 7.07% |

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
