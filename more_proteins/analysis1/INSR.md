# INSR — variant-effect analysis

*Insulin receptor* · UniProt `P06213` · 1382 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Fibronectin type-III 1 | 624–726 | 103 |
| Fibronectin type-III 2 | 757–842 | 86 |
| Fibronectin type-III 3 | 853–947 | 95 |
| Protein kinase | 1023–1298 | 276 |

**Pair analysed:** Fibronectin type-III 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **28.52 Å**, intra-module **10.95 Å**, **ratio 2.6**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 49.5 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 26,258 |
| ESM-1v | 26,258 |
| FoldX ΔΔG (ProtVar) | 22,211 |
| ThermoMPNN ΔΔG | 26,258 |
| revel | 7,999 |
| cadd | 8,403 |
| sift | 7,999 |
| polyphen | 7,999 |
| metarnn | 8,002 |
| vest4 | 8,403 |
| primateai | 7,991 |
| mutassessor | 7,986 |
| provean | 7,999 |
| esm1b | 7,999 |
| am_dbnsfp | 7,996 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.612 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.565 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.574 |
| AlphaMissense vs revel | +0.804 |
| AlphaMissense vs cadd | +0.731 |
| AlphaMissense vs sift | -0.743 |
| AlphaMissense vs polyphen | +0.768 |
| AlphaMissense vs metarnn | +0.832 |
| AlphaMissense vs vest4 | +0.827 |
| AlphaMissense vs primateai | +0.620 |
| AlphaMissense vs mutassessor | +0.635 |
| AlphaMissense vs provean | -0.768 |
| AlphaMissense vs esm1b | -0.785 |
| AlphaMissense vs am_dbnsfp | +0.974 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.412 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.435 |
| ESM-1v vs revel | -0.648 |
| ESM-1v vs cadd | -0.585 |
| ESM-1v vs sift | +0.626 |
| ESM-1v vs polyphen | -0.653 |
| ESM-1v vs metarnn | -0.669 |
| ESM-1v vs vest4 | -0.580 |
| ESM-1v vs primateai | -0.383 |
| ESM-1v vs mutassessor | -0.500 |
| ESM-1v vs provean | +0.563 |
| ESM-1v vs esm1b | +0.638 |
| ESM-1v vs am_dbnsfp | -0.589 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.679 |
| FoldX ΔΔG (ProtVar) vs revel | +0.507 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.384 |
| FoldX ΔΔG (ProtVar) vs sift | -0.456 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.524 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.534 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.494 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.295 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.471 |
| FoldX ΔΔG (ProtVar) vs provean | -0.505 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.488 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.549 |
| ThermoMPNN ΔΔG vs revel | +0.526 |
| ThermoMPNN ΔΔG vs cadd | +0.429 |
| ThermoMPNN ΔΔG vs sift | -0.460 |
| ThermoMPNN ΔΔG vs polyphen | +0.478 |
| ThermoMPNN ΔΔG vs metarnn | +0.533 |
| ThermoMPNN ΔΔG vs vest4 | +0.505 |
| ThermoMPNN ΔΔG vs primateai | +0.291 |
| ThermoMPNN ΔΔG vs mutassessor | +0.460 |
| ThermoMPNN ΔΔG vs provean | -0.482 |
| ThermoMPNN ΔΔG vs esm1b | -0.544 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.542 |
| revel vs cadd | +0.781 |
| revel vs sift | -0.792 |
| revel vs polyphen | +0.830 |
| revel vs metarnn | +0.926 |
| revel vs vest4 | +0.856 |
| revel vs primateai | +0.527 |
| revel vs mutassessor | +0.671 |
| revel vs provean | -0.801 |
| revel vs esm1b | -0.750 |
| revel vs am_dbnsfp | +0.808 |
| cadd vs sift | -0.769 |
| cadd vs polyphen | +0.781 |
| cadd vs metarnn | +0.787 |
| cadd vs vest4 | +0.763 |
| cadd vs primateai | +0.515 |
| cadd vs mutassessor | +0.575 |
| cadd vs provean | -0.744 |
| cadd vs esm1b | -0.691 |
| cadd vs am_dbnsfp | +0.736 |
| sift vs polyphen | -0.829 |
| sift vs metarnn | -0.806 |
| sift vs vest4 | -0.729 |
| sift vs primateai | -0.489 |
| sift vs mutassessor | -0.633 |
| sift vs provean | +0.803 |
| sift vs esm1b | +0.718 |
| sift vs am_dbnsfp | -0.750 |
| polyphen vs metarnn | +0.857 |
| polyphen vs vest4 | +0.771 |
| polyphen vs primateai | +0.500 |
| polyphen vs mutassessor | +0.712 |
| polyphen vs provean | -0.771 |
| polyphen vs esm1b | -0.711 |
| polyphen vs am_dbnsfp | +0.776 |
| metarnn vs vest4 | +0.913 |
| metarnn vs primateai | +0.568 |
| metarnn vs mutassessor | +0.720 |
| metarnn vs provean | -0.827 |
| metarnn vs esm1b | -0.769 |
| metarnn vs am_dbnsfp | +0.842 |
| vest4 vs primateai | +0.619 |
| vest4 vs mutassessor | +0.674 |
| vest4 vs provean | -0.788 |
| vest4 vs esm1b | -0.751 |
| vest4 vs am_dbnsfp | +0.841 |
| primateai vs mutassessor | +0.354 |
| primateai vs provean | -0.492 |
| primateai vs esm1b | -0.499 |
| primateai vs am_dbnsfp | +0.642 |
| mutassessor vs provean | -0.680 |
| mutassessor vs esm1b | -0.609 |
| mutassessor vs am_dbnsfp | +0.661 |
| provean vs esm1b | +0.753 |
| provean vs am_dbnsfp | -0.776 |
| esm1b vs am_dbnsfp | -0.795 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 139 |
| pathogenic | 22 |
| conflict | 17 |
| likely_benign | 8 |
| likely_pathogenic | 7 |
| benign | 1 |

**gnomAD r4 missense variants mapped:** 1,352

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,798** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,134 | 3,664 |
| mean AlphaMissense | 0.266 | 0.834 |
| mean ESM-1v | 4.009 | 7.791 |
| mean FoldX ΔΔG | 0.649 | 3.347 |
| mean ThermoMPNN ΔΔG | 0.469 | 1.371 |
| mean REVEL | 0.303 | 0.763 |
| mean CADD phred | 17.84 | 27.63 |
| mean SIFT | -0.276 | -0.014 |
| mean PolyPhen-2 HVAR | 0.125 | 0.831 |
| mean MetaRNN | 0.362 | 0.892 |
| mean VEST4 | 0.387 | 0.82 |
| mean PrimateAI | 0.607 | 0.761 |
| mean PROVEAN | 1.642 | 5.203 |
| **fraction seen in gnomAD** | **19.30%** (605) | **11.76%** (431) |

**Validation:** the damaging cluster is **depleted** in the population — 11.76% of it appears in gnomAD against 19.30% of the tolerant cluster (a 1.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 19 pathogenic / 0 benign, cluster 0 has 1 / 0; OR = nan, p = 1.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 22,211**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 13,392 | 8,819 |
| mean AlphaMissense | 0.502 | 0.962 |
| mean ESM-1v | 4.73 | 9.921 |
| mean FoldX ΔΔG | 0.699 | 5.021 |
| mean ThermoMPNN ΔΔG | 0.518 | 1.902 |
| **fraction seen in gnomAD** | **6.41%** (859) | **2.39%** (211) |

Depletion **2.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
