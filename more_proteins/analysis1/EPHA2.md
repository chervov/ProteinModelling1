# EPHA2 — variant-effect analysis

*Ephrin type-A receptor 2* · UniProt `P29317` · 976 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Eph LBD | 28–206 | 179 |
| Fibronectin type-III 1 | 328–432 | 105 |
| Fibronectin type-III 2 | 438–529 | 92 |
| Protein kinase | 613–875 | 263 |
| SAM | 904–968 | 65 |

**Pair analysed:** Eph LBD ↔ SAM

**AlphaFold PAE:** inter-module mean **21.09 Å**, intra-module **4.09 Å**, **ratio 5.15**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.4 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 18,544 |
| ESM-1v | 18,544 |
| FoldX ΔΔG (ProtVar) | 16,644 |
| ThermoMPNN ΔΔG | 18,544 |
| revel | 5,760 |
| cadd | 6,021 |
| sift | 5,760 |
| polyphen | 5,760 |
| metarnn | 5,760 |
| vest4 | 6,021 |
| primateai | 5,754 |
| mutassessor | 5,754 |
| provean | 5,760 |
| esm1b | 5,760 |
| am_dbnsfp | 5,754 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.830 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.545 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.507 |
| AlphaMissense vs revel | +0.755 |
| AlphaMissense vs cadd | +0.698 |
| AlphaMissense vs sift | -0.728 |
| AlphaMissense vs polyphen | +0.743 |
| AlphaMissense vs metarnn | +0.809 |
| AlphaMissense vs vest4 | +0.806 |
| AlphaMissense vs primateai | +0.604 |
| AlphaMissense vs mutassessor | +0.638 |
| AlphaMissense vs provean | -0.744 |
| AlphaMissense vs esm1b | -0.790 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.449 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.406 |
| ESM-1v vs revel | -0.799 |
| ESM-1v vs cadd | -0.749 |
| ESM-1v vs sift | +0.775 |
| ESM-1v vs polyphen | -0.732 |
| ESM-1v vs metarnn | -0.823 |
| ESM-1v vs vest4 | -0.797 |
| ESM-1v vs primateai | -0.612 |
| ESM-1v vs mutassessor | -0.658 |
| ESM-1v vs provean | +0.808 |
| ESM-1v vs esm1b | +0.907 |
| ESM-1v vs am_dbnsfp | -0.818 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.680 |
| FoldX ΔΔG (ProtVar) vs revel | +0.446 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.317 |
| FoldX ΔΔG (ProtVar) vs sift | -0.425 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.424 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.484 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.446 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.306 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.472 |
| FoldX ΔΔG (ProtVar) vs provean | -0.476 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.466 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.546 |
| ThermoMPNN ΔΔG vs revel | +0.432 |
| ThermoMPNN ΔΔG vs cadd | +0.319 |
| ThermoMPNN ΔΔG vs sift | -0.424 |
| ThermoMPNN ΔΔG vs polyphen | +0.372 |
| ThermoMPNN ΔΔG vs metarnn | +0.447 |
| ThermoMPNN ΔΔG vs vest4 | +0.412 |
| ThermoMPNN ΔΔG vs primateai | +0.247 |
| ThermoMPNN ΔΔG vs mutassessor | +0.462 |
| ThermoMPNN ΔΔG vs provean | -0.426 |
| ThermoMPNN ΔΔG vs esm1b | -0.428 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.500 |
| revel vs cadd | +0.742 |
| revel vs sift | -0.743 |
| revel vs polyphen | +0.786 |
| revel vs metarnn | +0.875 |
| revel vs vest4 | +0.794 |
| revel vs primateai | +0.646 |
| revel vs mutassessor | +0.563 |
| revel vs provean | -0.778 |
| revel vs esm1b | -0.748 |
| revel vs am_dbnsfp | +0.756 |
| cadd vs sift | -0.717 |
| cadd vs polyphen | +0.768 |
| cadd vs metarnn | +0.770 |
| cadd vs vest4 | +0.756 |
| cadd vs primateai | +0.596 |
| cadd vs mutassessor | +0.505 |
| cadd vs provean | -0.679 |
| cadd vs esm1b | -0.717 |
| cadd vs am_dbnsfp | +0.697 |
| sift vs polyphen | -0.672 |
| sift vs metarnn | -0.773 |
| sift vs vest4 | -0.706 |
| sift vs primateai | -0.499 |
| sift vs mutassessor | -0.646 |
| sift vs provean | +0.781 |
| sift vs esm1b | +0.752 |
| sift vs am_dbnsfp | -0.729 |
| polyphen vs metarnn | +0.849 |
| polyphen vs vest4 | +0.805 |
| polyphen vs primateai | +0.649 |
| polyphen vs mutassessor | +0.572 |
| polyphen vs provean | -0.702 |
| polyphen vs esm1b | -0.713 |
| polyphen vs am_dbnsfp | +0.743 |
| metarnn vs vest4 | +0.913 |
| metarnn vs primateai | +0.685 |
| metarnn vs mutassessor | +0.650 |
| metarnn vs provean | -0.803 |
| metarnn vs esm1b | -0.797 |
| metarnn vs am_dbnsfp | +0.812 |
| vest4 vs primateai | +0.680 |
| vest4 vs mutassessor | +0.618 |
| vest4 vs provean | -0.757 |
| vest4 vs esm1b | -0.767 |
| vest4 vs am_dbnsfp | +0.807 |
| primateai vs mutassessor | +0.366 |
| primateai vs provean | -0.510 |
| primateai vs esm1b | -0.578 |
| primateai vs am_dbnsfp | +0.604 |
| mutassessor vs provean | -0.678 |
| mutassessor vs esm1b | -0.640 |
| mutassessor vs am_dbnsfp | +0.638 |
| provean vs esm1b | +0.778 |
| provean vs am_dbnsfp | -0.744 |
| esm1b vs am_dbnsfp | -0.791 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 87 |
| likely_benign | 13 |
| conflict | 11 |
| benign | 8 |
| likely_pathogenic | 2 |
| pathogenic | 2 |

**gnomAD r4 missense variants mapped:** 1,205

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 5,176** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,413 | 2,763 |
| mean AlphaMissense | 0.227 | 0.773 |
| mean ESM-1v | 4.937 | 10.518 |
| mean FoldX ΔΔG | 0.619 | 3.163 |
| mean ThermoMPNN ΔΔG | 0.503 | 1.338 |
| mean REVEL | 0.171 | 0.594 |
| mean CADD phred | 16.735 | 27.795 |
| mean SIFT | -0.251 | -0.011 |
| mean PolyPhen-2 HVAR | 0.184 | 0.877 |
| mean MetaRNN | 0.306 | 0.882 |
| mean VEST4 | 0.364 | 0.795 |
| mean PrimateAI | 0.502 | 0.72 |
| mean PROVEAN | 1.539 | 5.087 |
| **fraction seen in gnomAD** | **24.29%** (586) | **17.30%** (478) |

**Validation:** the damaging cluster is **depleted** in the population — 17.30% of it appears in gnomAD against 24.29% of the tolerant cluster (a 1.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 2 pathogenic / 0 benign, cluster 0 has 0 / 8; OR = inf, p = 0.022.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 16,644**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 9,038 | 7,606 |
| mean AlphaMissense | 0.376 | 0.935 |
| mean ESM-1v | 6.326 | 12.656 |
| mean FoldX ΔΔG | 0.566 | 4.403 |
| mean ThermoMPNN ΔΔG | 0.484 | 1.716 |
| **fraction seen in gnomAD** | **8.59%** (776) | **3.79%** (288) |

Depletion **2.3×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
