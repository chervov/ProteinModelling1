# DNM2 — variant-effect analysis

*Dynamin-2* · UniProt `P50570` · 870 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 28–294 | 267 |
| PH | 519–625 | 107 |
| GED | 653–744 | 92 |

**Pair analysed:** Dynamin-type G ↔ GED

**AlphaFold PAE:** inter-module mean **19.07 Å**, intra-module **6.98 Å**, **ratio 2.73**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 58.1 | 5 | 100% / 100% |
| 8v8t.1.A (41.4% id) | 60.4 | 13 | 100% / 99% |
| 4bej.2.A (46.8% id) | 64.3 | 2 | 100% / 95% |
| 5a3f.1.A (84.2% id) | 59.2 | 4 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `P50570_8v8t-1-A.pdb`, centroid distance **60.4 Å**, **13 residue pairs** in contact within 5 Å.

**Domain A interface residues (9):** `28, 29, 30, 31, 286, 287, 289, 290, 293`

**Domain B interface residues (8):** `725, 728, 729, 732, 736, 739, 742, 743`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 323 | 16,207 | 0.912 | 0.924 | 0.41 |
| ESM-1v | 323 | 16,207 | -15.171 | -14.005 | 2.5e-06 |
| FoldX ΔΔG | 323 | 13,699 | 1.537 | 0.917 | 0.0074 |
| ThermoMPNN ΔΔG | 323 | 16,207 | 0.847 | 0.472 | 2.2e-13 |
| REVEL | 102 | 5,065 | 0.728 | 0.668 | 0.3 |
| CADD phred | 102 | 5,202 | 24.7 | 25.3 | 0.078 |
| SIFT | 102 | 5,065 | 0.004 | 0.011 | 0.05 |
| PolyPhen-2 HVAR | 102 | 5,043 | 0.923 | 0.857 | 0.23 |
| MetaRNN | 102 | 5,087 | 0.867 | 0.808 | 0.03 |
| VEST4 | 102 | 5,294 | 0.806 | 0.758 | 0.18 |
| PrimateAI | 102 | 4,959 | 0.816 | 0.797 | 0.092 |
| MutationAssessor | 102 | 5,037 | 3.12 | 2.675 | 0.0013 |
| PROVEAN | 102 | 5,065 | -3.69 | -3.49 | 0.67 |
| ESM1b | 102 | 5,069 | -11.852 | -11.943 | 0.18 |
| AlphaMissense (dbNSFP) | 102 | 5,081 | 0.705 | 0.739 | 0.7 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 16,530 |
| ESM-1v | 16,530 |
| FoldX ΔΔG (ProtVar) | 14,022 |
| ThermoMPNN ΔΔG | 16,530 |
| revel | 5,167 |
| cadd | 5,304 |
| sift | 5,167 |
| polyphen | 5,145 |
| metarnn | 5,189 |
| vest4 | 5,396 |
| primateai | 5,061 |
| mutassessor | 5,139 |
| provean | 5,167 |
| esm1b | 5,171 |
| am_dbnsfp | 5,183 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.839 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.464 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.535 |
| AlphaMissense vs revel | +0.729 |
| AlphaMissense vs cadd | +0.699 |
| AlphaMissense vs sift | -0.683 |
| AlphaMissense vs polyphen | +0.486 |
| AlphaMissense vs metarnn | +0.776 |
| AlphaMissense vs vest4 | +0.750 |
| AlphaMissense vs primateai | +0.628 |
| AlphaMissense vs mutassessor | +0.686 |
| AlphaMissense vs provean | -0.714 |
| AlphaMissense vs esm1b | -0.756 |
| AlphaMissense vs am_dbnsfp | +0.979 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.349 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.444 |
| ESM-1v vs revel | -0.732 |
| ESM-1v vs cadd | -0.699 |
| ESM-1v vs sift | +0.694 |
| ESM-1v vs polyphen | -0.488 |
| ESM-1v vs metarnn | -0.747 |
| ESM-1v vs vest4 | -0.718 |
| ESM-1v vs primateai | -0.541 |
| ESM-1v vs mutassessor | -0.683 |
| ESM-1v vs provean | +0.719 |
| ESM-1v vs esm1b | +0.828 |
| ESM-1v vs am_dbnsfp | -0.824 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.698 |
| FoldX ΔΔG (ProtVar) vs revel | +0.389 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.313 |
| FoldX ΔΔG (ProtVar) vs sift | -0.371 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.311 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.403 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.361 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.248 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.377 |
| FoldX ΔΔG (ProtVar) vs provean | -0.353 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.343 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.441 |
| ThermoMPNN ΔΔG vs revel | +0.507 |
| ThermoMPNN ΔΔG vs cadd | +0.420 |
| ThermoMPNN ΔΔG vs sift | -0.465 |
| ThermoMPNN ΔΔG vs polyphen | +0.329 |
| ThermoMPNN ΔΔG vs metarnn | +0.527 |
| ThermoMPNN ΔΔG vs vest4 | +0.478 |
| ThermoMPNN ΔΔG vs primateai | +0.333 |
| ThermoMPNN ΔΔG vs mutassessor | +0.468 |
| ThermoMPNN ΔΔG vs provean | -0.445 |
| ThermoMPNN ΔΔG vs esm1b | -0.490 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.520 |
| revel vs cadd | +0.720 |
| revel vs sift | -0.735 |
| revel vs polyphen | +0.496 |
| revel vs metarnn | +0.852 |
| revel vs vest4 | +0.700 |
| revel vs primateai | +0.515 |
| revel vs mutassessor | +0.703 |
| revel vs provean | -0.716 |
| revel vs esm1b | -0.686 |
| revel vs am_dbnsfp | +0.707 |
| cadd vs sift | -0.744 |
| cadd vs polyphen | +0.548 |
| cadd vs metarnn | +0.741 |
| cadd vs vest4 | +0.659 |
| cadd vs primateai | +0.498 |
| cadd vs mutassessor | +0.692 |
| cadd vs provean | -0.707 |
| cadd vs esm1b | -0.630 |
| cadd vs am_dbnsfp | +0.687 |
| sift vs polyphen | -0.549 |
| sift vs metarnn | -0.761 |
| sift vs vest4 | -0.625 |
| sift vs primateai | -0.384 |
| sift vs mutassessor | -0.772 |
| sift vs provean | +0.680 |
| sift vs esm1b | +0.622 |
| sift vs am_dbnsfp | -0.680 |
| polyphen vs metarnn | +0.547 |
| polyphen vs vest4 | +0.453 |
| polyphen vs primateai | +0.254 |
| polyphen vs mutassessor | +0.595 |
| polyphen vs provean | -0.461 |
| polyphen vs esm1b | -0.376 |
| polyphen vs am_dbnsfp | +0.486 |
| metarnn vs vest4 | +0.849 |
| metarnn vs primateai | +0.549 |
| metarnn vs mutassessor | +0.781 |
| metarnn vs provean | -0.755 |
| metarnn vs esm1b | -0.706 |
| metarnn vs am_dbnsfp | +0.767 |
| vest4 vs primateai | +0.552 |
| vest4 vs mutassessor | +0.667 |
| vest4 vs provean | -0.707 |
| vest4 vs esm1b | -0.670 |
| vest4 vs am_dbnsfp | +0.732 |
| primateai vs mutassessor | +0.416 |
| primateai vs provean | -0.492 |
| primateai vs esm1b | -0.515 |
| primateai vs am_dbnsfp | +0.631 |
| mutassessor vs provean | -0.659 |
| mutassessor vs esm1b | -0.604 |
| mutassessor vs am_dbnsfp | +0.680 |
| provean vs esm1b | +0.703 |
| provean vs am_dbnsfp | -0.701 |
| esm1b vs am_dbnsfp | -0.743 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 1,050

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,298** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,269 | 3,029 |
| mean AlphaMissense | 0.341 | 0.875 |
| mean ESM-1v | 9.055 | 13.526 |
| mean FoldX ΔΔG | 0.405 | 1.932 |
| mean ThermoMPNN ΔΔG | 0.302 | 1.038 |
| mean REVEL | 0.409 | 0.79 |
| mean CADD phred | 18.65 | 27.446 |
| mean SIFT | -0.216 | -0.016 |
| mean PolyPhen-2 HVAR | 0.328 | 0.813 |
| mean MetaRNN | 0.449 | 0.879 |
| mean VEST4 | 0.493 | 0.823 |
| mean PrimateAI | 0.712 | 0.819 |
| mean PROVEAN | 1.907 | 4.972 |
| **fraction seen in gnomAD** | **22.70%** (288) | **13.44%** (407) |
| fraction at the interface | 2.44% | 2.34% |

**Validation:** the damaging cluster is **depleted** in the population — 13.44% of it appears in gnomAD against 22.70% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 14,022**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,106 | 9,916 |
| mean AlphaMissense | 0.452 | 0.957 |
| mean ESM-1v | 10.526 | 15.814 |
| mean FoldX ΔΔG | 0.299 | 2.431 |
| mean ThermoMPNN ΔΔG | 0.276 | 1.146 |
| **fraction seen in gnomAD** | **11.81%** (485) | **3.79%** (376) |

Depletion **3.1×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.51% | 2.22% |

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
