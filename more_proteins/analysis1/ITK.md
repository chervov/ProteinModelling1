# ITK — variant-effect analysis

*Tyrosine-protein kinase ITK/TSK* · UniProt `Q08881` · 620 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PH | 4–111 | 108 |
| SH3 | 171–231 | 61 |
| SH2 | 239–338 | 100 |
| Protein kinase | 363–615 | 253 |

**Pair analysed:** PH ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **29.79 Å**, intra-module **4.48 Å**, **ratio 6.65**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 41.4 | 1 | 100% / 100% |
| 4y93.1.A (55.3% id) | 39.0 | 13 | 100% / 100% |
| 8s93.1.A (53.0% id) | 42.3 | 14 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q08881_8s93-1-A.pdb`, centroid distance **42.3 Å**, **14 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `35, 36, 56, 57, 107, 108, 109, 111`

**Domain B interface residues (8):** `382, 383, 384, 385, 386, 411, 422, 423`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 11,476 | 0.386 | 0.698 | 5.1e-13 |
| ESM-1v | 304 | 11,476 | -7.608 | -8.372 | 0.00041 |
| FoldX ΔΔG | 304 | 11,229 | 0.753 | 1.156 | 0.0011 |
| ThermoMPNN ΔΔG | 304 | 11,476 | 0.533 | 0.832 | 2.9e-05 |
| REVEL | 96 | 3,512 | 0.48 | 0.499 | 0.24 |
| CADD phred | 104 | 3,715 | 24.0 | 25.4 | 0.13 |
| SIFT | 96 | 3,512 | 0.036 | 0.011 | 0.013 |
| PolyPhen-2 HVAR | 96 | 3,512 | 0.387 | 0.721 | 0.0066 |
| MetaRNN | 96 | 3,512 | 0.603 | 0.73 | 0.0088 |
| VEST4 | 104 | 3,715 | 0.548 | 0.607 | 0.048 |
| PrimateAI | 96 | 3,512 | 0.684 | 0.667 | 0.22 |
| MutationAssessor | 96 | 3,512 | 1.383 | 1.865 | 6.1e-05 |
| PROVEAN | 96 | 3,512 | -2.375 | -2.95 | 0.077 |
| ESM1b | 96 | 3,512 | -7.324 | -8.303 | 0.031 |
| AlphaMissense (dbNSFP) | 96 | 3,512 | 0.176 | 0.439 | 5.7e-06 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 11,780 |
| ESM-1v | 11,780 |
| FoldX ΔΔG (ProtVar) | 11,533 |
| ThermoMPNN ΔΔG | 11,780 |
| revel | 3,608 |
| cadd | 3,819 |
| sift | 3,608 |
| polyphen | 3,608 |
| metarnn | 3,608 |
| vest4 | 3,819 |
| primateai | 3,608 |
| mutassessor | 3,608 |
| provean | 3,608 |
| esm1b | 3,608 |
| am_dbnsfp | 3,608 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.879 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.525 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.552 |
| AlphaMissense vs revel | +0.758 |
| AlphaMissense vs cadd | +0.770 |
| AlphaMissense vs sift | -0.755 |
| AlphaMissense vs polyphen | +0.716 |
| AlphaMissense vs metarnn | +0.831 |
| AlphaMissense vs vest4 | +0.763 |
| AlphaMissense vs primateai | +0.572 |
| AlphaMissense vs mutassessor | +0.705 |
| AlphaMissense vs provean | -0.759 |
| AlphaMissense vs esm1b | -0.842 |
| AlphaMissense vs am_dbnsfp | +0.988 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.511 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.556 |
| ESM-1v vs revel | -0.758 |
| ESM-1v vs cadd | -0.796 |
| ESM-1v vs sift | +0.802 |
| ESM-1v vs polyphen | -0.707 |
| ESM-1v vs metarnn | -0.845 |
| ESM-1v vs vest4 | -0.747 |
| ESM-1v vs primateai | -0.515 |
| ESM-1v vs mutassessor | -0.758 |
| ESM-1v vs provean | +0.825 |
| ESM-1v vs esm1b | +0.918 |
| ESM-1v vs am_dbnsfp | -0.850 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.726 |
| FoldX ΔΔG (ProtVar) vs revel | +0.421 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.425 |
| FoldX ΔΔG (ProtVar) vs sift | -0.433 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.400 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.490 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.441 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.273 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.458 |
| FoldX ΔΔG (ProtVar) vs provean | -0.464 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.491 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.517 |
| ThermoMPNN ΔΔG vs revel | +0.434 |
| ThermoMPNN ΔΔG vs cadd | +0.439 |
| ThermoMPNN ΔΔG vs sift | -0.461 |
| ThermoMPNN ΔΔG vs polyphen | +0.419 |
| ThermoMPNN ΔΔG vs metarnn | +0.531 |
| ThermoMPNN ΔΔG vs vest4 | +0.487 |
| ThermoMPNN ΔΔG vs primateai | +0.292 |
| ThermoMPNN ΔΔG vs mutassessor | +0.519 |
| ThermoMPNN ΔΔG vs provean | -0.468 |
| ThermoMPNN ΔΔG vs esm1b | -0.562 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.548 |
| revel vs cadd | +0.740 |
| revel vs sift | -0.727 |
| revel vs polyphen | +0.793 |
| revel vs metarnn | +0.859 |
| revel vs vest4 | +0.758 |
| revel vs primateai | +0.533 |
| revel vs mutassessor | +0.701 |
| revel vs provean | -0.736 |
| revel vs esm1b | -0.733 |
| revel vs am_dbnsfp | +0.761 |
| cadd vs sift | -0.794 |
| cadd vs polyphen | +0.729 |
| cadd vs metarnn | +0.822 |
| cadd vs vest4 | +0.763 |
| cadd vs primateai | +0.520 |
| cadd vs mutassessor | +0.652 |
| cadd vs provean | -0.763 |
| cadd vs esm1b | -0.766 |
| cadd vs am_dbnsfp | +0.772 |
| sift vs polyphen | -0.674 |
| sift vs metarnn | -0.790 |
| sift vs vest4 | -0.693 |
| sift vs primateai | -0.425 |
| sift vs mutassessor | -0.706 |
| sift vs provean | +0.803 |
| sift vs esm1b | +0.770 |
| sift vs am_dbnsfp | -0.763 |
| polyphen vs metarnn | +0.845 |
| polyphen vs vest4 | +0.781 |
| polyphen vs primateai | +0.556 |
| polyphen vs mutassessor | +0.636 |
| polyphen vs provean | -0.667 |
| polyphen vs esm1b | -0.685 |
| polyphen vs am_dbnsfp | +0.723 |
| metarnn vs vest4 | +0.892 |
| metarnn vs primateai | +0.592 |
| metarnn vs mutassessor | +0.744 |
| metarnn vs provean | -0.803 |
| metarnn vs esm1b | -0.823 |
| metarnn vs am_dbnsfp | +0.829 |
| vest4 vs primateai | +0.621 |
| vest4 vs mutassessor | +0.646 |
| vest4 vs provean | -0.721 |
| vest4 vs esm1b | -0.736 |
| vest4 vs am_dbnsfp | +0.775 |
| primateai vs mutassessor | +0.400 |
| primateai vs provean | -0.437 |
| primateai vs esm1b | -0.528 |
| primateai vs am_dbnsfp | +0.574 |
| mutassessor vs provean | -0.718 |
| mutassessor vs esm1b | -0.720 |
| mutassessor vs am_dbnsfp | +0.711 |
| provean vs esm1b | +0.791 |
| provean vs am_dbnsfp | -0.766 |
| esm1b vs am_dbnsfp | -0.841 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 167 |
| likely_benign | 6 |
| conflict | 5 |
| pathogenic | 2 |

**gnomAD r4 missense variants mapped:** 644

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,532** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,611 | 1,921 |
| mean AlphaMissense | 0.201 | 0.765 |
| mean ESM-1v | 4.82 | 9.871 |
| mean FoldX ΔΔG | 0.593 | 2.804 |
| mean ThermoMPNN ΔΔG | 0.461 | 1.382 |
| mean REVEL | 0.269 | 0.713 |
| mean CADD phred | 18.292 | 28.459 |
| mean SIFT | -0.275 | -0.019 |
| mean PolyPhen-2 HVAR | 0.237 | 0.863 |
| mean MetaRNN | 0.365 | 0.884 |
| mean VEST4 | 0.359 | 0.748 |
| mean PrimateAI | 0.569 | 0.727 |
| mean PROVEAN | 1.217 | 5.209 |
| **fraction seen in gnomAD** | **21.79%** (351) | **14.37%** (276) |
| fraction at the interface | 3.35% | 2.19% |

**Validation:** the damaging cluster is **depleted** in the population — 14.37% of it appears in gnomAD against 21.79% of the tolerant cluster (a 1.5-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 11,533**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 6,402 | 5,131 |
| mean AlphaMissense | 0.375 | 0.928 |
| mean ESM-1v | 6.113 | 11.983 |
| mean FoldX ΔΔG | 0.573 | 4.124 |
| mean ThermoMPNN ΔΔG | 0.453 | 1.827 |
| **fraction seen in gnomAD** | **7.54%** (483) | **2.86%** (147) |

Depletion **2.6×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.31% | 1.79% |

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
