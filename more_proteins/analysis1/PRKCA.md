# PRKCA — variant-effect analysis

*Protein kinase C alpha type* · UniProt `P17252` · 672 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| C2 | 158–275 | 118 |
| Protein kinase | 339–597 | 259 |
| AGC-kinase C-terminal | 598–668 | 71 |

**Pair analysed:** C2 ↔ AGC-kinase C-terminal

**AlphaFold PAE:** inter-module mean **27.85 Å**, intra-module **5.54 Å**, **ratio 5.03**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 41.1 | 16 | 100% / 100% |
| 8se1.2.A (80.7% id) | 46.1 | 2 | 100% / 99% |
| 8se4.2.A (80.5% id) | 47.4 | 11 | 100% / 94% |
| 8se3.1.A (80.5% id) | 42.2 | 17 | 100% / 94% |
| 3pfq.1.A (80.6% id) | 64.2 | 0 | 100% / 97% |

## 2. The inter-domain interface

Most compact structure: `P17252_8se3-1-A.pdb`, centroid distance **42.2 Å**, **17 residue pairs** in contact within 5 Å.

**Domain A interface residues (10):** `236, 237, 238, 239, 262, 263, 264, 265, 268, 269`

**Domain B interface residues (8):** `604, 609, 610, 611, 612, 613, 614, 615`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 342 | 12,426 | 0.968 | 0.964 | 0.52 |
| ESM-1v | 342 | 12,426 | -9.49 | -10.545 | 2.8e-06 |
| FoldX ΔΔG | 342 | 11,628 | 1.401 | 1.211 | 0.59 |
| ThermoMPNN ΔΔG | 342 | 12,426 | 0.78 | 0.738 | 0.55 |
| REVEL | 103 | 3,890 | 0.352 | 0.487 | 6e-07 |
| CADD phred | 114 | 4,102 | 25.65 | 25.8 | 0.24 |
| SIFT | 103 | 3,890 | 0.022 | 0.016 | 0.64 |
| PolyPhen-2 HVAR | 103 | 3,890 | 0.287 | 0.588 | 0.00085 |
| MetaRNN | 103 | 3,890 | 0.758 | 0.804 | 0.039 |
| VEST4 | 114 | 4,102 | 0.784 | 0.739 | 0.03 |
| PrimateAI | 103 | 3,884 | 0.784 | 0.833 | 3.1e-08 |
| MutationAssessor | 103 | 3,884 | 2.73 | 1.83 | 7.1e-05 |
| PROVEAN | 103 | 3,890 | -4.03 | -3.705 | 0.13 |
| ESM1b | 103 | 3,890 | -11.774 | -12.059 | 0.59 |
| AlphaMissense (dbNSFP) | 103 | 3,884 | 0.841 | 0.887 | 0.71 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,768 |
| ESM-1v | 12,768 |
| FoldX ΔΔG (ProtVar) | 11,970 |
| ThermoMPNN ΔΔG | 12,768 |
| revel | 3,993 |
| cadd | 4,216 |
| sift | 3,993 |
| polyphen | 3,993 |
| metarnn | 3,993 |
| vest4 | 4,216 |
| primateai | 3,987 |
| mutassessor | 3,987 |
| provean | 3,993 |
| esm1b | 3,993 |
| am_dbnsfp | 3,987 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.860 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.449 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.486 |
| AlphaMissense vs revel | +0.779 |
| AlphaMissense vs cadd | +0.723 |
| AlphaMissense vs sift | -0.743 |
| AlphaMissense vs polyphen | +0.804 |
| AlphaMissense vs metarnn | +0.825 |
| AlphaMissense vs vest4 | +0.747 |
| AlphaMissense vs primateai | +0.608 |
| AlphaMissense vs mutassessor | +0.558 |
| AlphaMissense vs provean | -0.771 |
| AlphaMissense vs esm1b | -0.780 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.453 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.535 |
| ESM-1v vs revel | -0.793 |
| ESM-1v vs cadd | -0.751 |
| ESM-1v vs sift | +0.821 |
| ESM-1v vs polyphen | -0.829 |
| ESM-1v vs metarnn | -0.852 |
| ESM-1v vs vest4 | -0.767 |
| ESM-1v vs primateai | -0.503 |
| ESM-1v vs mutassessor | -0.556 |
| ESM-1v vs provean | +0.778 |
| ESM-1v vs esm1b | +0.850 |
| ESM-1v vs am_dbnsfp | -0.850 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.694 |
| FoldX ΔΔG (ProtVar) vs revel | +0.404 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.397 |
| FoldX ΔΔG (ProtVar) vs sift | -0.408 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.427 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.448 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.412 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.201 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.377 |
| FoldX ΔΔG (ProtVar) vs provean | -0.442 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.418 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.438 |
| ThermoMPNN ΔΔG vs revel | +0.446 |
| ThermoMPNN ΔΔG vs cadd | +0.458 |
| ThermoMPNN ΔΔG vs sift | -0.464 |
| ThermoMPNN ΔΔG vs polyphen | +0.484 |
| ThermoMPNN ΔΔG vs metarnn | +0.513 |
| ThermoMPNN ΔΔG vs vest4 | +0.501 |
| ThermoMPNN ΔΔG vs primateai | +0.210 |
| ThermoMPNN ΔΔG vs mutassessor | +0.403 |
| ThermoMPNN ΔΔG vs provean | -0.487 |
| ThermoMPNN ΔΔG vs esm1b | -0.507 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.470 |
| revel vs cadd | +0.733 |
| revel vs sift | -0.739 |
| revel vs polyphen | +0.775 |
| revel vs metarnn | +0.881 |
| revel vs vest4 | +0.742 |
| revel vs primateai | +0.533 |
| revel vs mutassessor | +0.612 |
| revel vs provean | -0.758 |
| revel vs esm1b | -0.720 |
| revel vs am_dbnsfp | +0.779 |
| cadd vs sift | -0.798 |
| cadd vs polyphen | +0.814 |
| cadd vs metarnn | +0.790 |
| cadd vs vest4 | +0.747 |
| cadd vs primateai | +0.462 |
| cadd vs mutassessor | +0.480 |
| cadd vs provean | -0.735 |
| cadd vs esm1b | -0.712 |
| cadd vs am_dbnsfp | +0.723 |
| sift vs polyphen | -0.825 |
| sift vs metarnn | -0.808 |
| sift vs vest4 | -0.701 |
| sift vs primateai | -0.454 |
| sift vs mutassessor | -0.554 |
| sift vs provean | +0.730 |
| sift vs esm1b | +0.713 |
| sift vs am_dbnsfp | -0.743 |
| polyphen vs metarnn | +0.863 |
| polyphen vs vest4 | +0.745 |
| polyphen vs primateai | +0.520 |
| polyphen vs mutassessor | +0.508 |
| polyphen vs provean | -0.755 |
| polyphen vs esm1b | -0.737 |
| polyphen vs am_dbnsfp | +0.804 |
| metarnn vs vest4 | +0.883 |
| metarnn vs primateai | +0.553 |
| metarnn vs mutassessor | +0.615 |
| metarnn vs provean | -0.789 |
| metarnn vs esm1b | -0.747 |
| metarnn vs am_dbnsfp | +0.828 |
| vest4 vs primateai | +0.538 |
| vest4 vs mutassessor | +0.463 |
| vest4 vs provean | -0.727 |
| vest4 vs esm1b | -0.694 |
| vest4 vs am_dbnsfp | +0.748 |
| primateai vs mutassessor | +0.280 |
| primateai vs provean | -0.462 |
| primateai vs esm1b | -0.431 |
| primateai vs am_dbnsfp | +0.608 |
| mutassessor vs provean | -0.542 |
| mutassessor vs esm1b | -0.465 |
| mutassessor vs am_dbnsfp | +0.558 |
| provean vs esm1b | +0.735 |
| provean vs am_dbnsfp | -0.771 |
| esm1b vs am_dbnsfp | -0.780 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 9 |
| likely_benign | 2 |

**gnomAD r4 missense variants mapped:** 555

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,733** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,431 | 2,302 |
| mean AlphaMissense | 0.387 | 0.924 |
| mean ESM-1v | 5.888 | 11.781 |
| mean FoldX ΔΔG | 0.542 | 2.998 |
| mean ThermoMPNN ΔΔG | 0.427 | 1.22 |
| mean REVEL | 0.261 | 0.665 |
| mean CADD phred | 19.989 | 28.516 |
| mean SIFT | -0.253 | -0.014 |
| mean PolyPhen-2 HVAR | 0.128 | 0.826 |
| mean MetaRNN | 0.427 | 0.886 |
| mean VEST4 | 0.512 | 0.824 |
| mean PrimateAI | 0.751 | 0.846 |
| mean PROVEAN | 2.033 | 5.594 |
| **fraction seen in gnomAD** | **18.17%** (260) | **10.60%** (244) |
| fraction at the interface | 3.07% | 2.56% |

**Validation:** the damaging cluster is **depleted** in the population — 10.60% of it appears in gnomAD against 18.17% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 11,970**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 5,393 | 6,577 |
| mean AlphaMissense | 0.585 | 0.978 |
| mean ESM-1v | 7.453 | 13.953 |
| mean FoldX ΔΔG | 0.485 | 3.977 |
| mean ThermoMPNN ΔΔG | 0.363 | 1.57 |
| **fraction seen in gnomAD** | **6.53%** (352) | **2.31%** (152) |

Depletion **2.8×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.06% | 2.69% |

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
