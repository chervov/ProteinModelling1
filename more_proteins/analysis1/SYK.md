# SYK — variant-effect analysis

*Tyrosine-protein kinase SYK* · UniProt `P43405` · 635 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 15–107 | 93 |
| SH2 2 | 168–259 | 92 |
| Protein kinase | 371–631 | 261 |

**Pair analysed:** SH2 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **8.79 Å**, intra-module **3.52 Å**, **ratio 2.49**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 35.5 | 15 | 100% / 100% |
| 4fl2.1.A (100.0% id) | 35.3 | 15 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P43405.pdb`, centroid distance **35.5 Å**, **15 residue pairs** in contact within 5 Å.

**Domain A interface residues (9):** `22, 23, 45, 46, 48, 63, 65, 67, 77`

**Domain B interface residues (8):** `469, 600, 624, 625, 627, 628, 629, 631`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 323 | 11,742 | 0.81 | 0.861 | 0.098 |
| ESM-1v | 323 | 11,742 | -9.156 | -9.821 | 0.00061 |
| FoldX ΔΔG | 323 | 10,507 | 1.229 | 1.334 | 0.11 |
| ThermoMPNN ΔΔG | 323 | 11,742 | 0.615 | 0.735 | 0.002 |
| REVEL | 100 | 3,641 | 0.516 | 0.464 | 0.9 |
| CADD phred | 106 | 3,856 | 25.8 | 24.6 | 4.5e-05 |
| SIFT | 100 | 3,641 | 0.072 | 0.032 | 0.14 |
| PolyPhen-2 HVAR | 100 | 3,641 | 0.996 | 0.861 | 6.6e-06 |
| MetaRNN | 100 | 3,641 | 0.773 | 0.669 | 0.33 |
| VEST4 | 106 | 3,856 | 0.647 | 0.609 | 0.66 |
| PrimateAI | 100 | 3,635 | 0.761 | 0.691 | 7.5e-06 |
| MutationAssessor | 100 | 3,635 | 1.485 | 1.78 | 0.19 |
| PROVEAN | 100 | 3,641 | -1.905 | -2.29 | 0.32 |
| ESM1b | 100 | 3,641 | -8.845 | -9.365 | 0.047 |
| AlphaMissense (dbNSFP) | 100 | 3,635 | 0.618 | 0.641 | 0.88 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,065 |
| ESM-1v | 12,065 |
| FoldX ΔΔG (ProtVar) | 10,830 |
| ThermoMPNN ΔΔG | 12,065 |
| revel | 3,741 |
| cadd | 3,962 |
| sift | 3,741 |
| polyphen | 3,741 |
| metarnn | 3,741 |
| vest4 | 3,962 |
| primateai | 3,735 |
| mutassessor | 3,735 |
| provean | 3,741 |
| esm1b | 3,741 |
| am_dbnsfp | 3,735 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.884 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.521 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.567 |
| AlphaMissense vs revel | +0.782 |
| AlphaMissense vs cadd | +0.772 |
| AlphaMissense vs sift | -0.741 |
| AlphaMissense vs polyphen | +0.789 |
| AlphaMissense vs metarnn | +0.865 |
| AlphaMissense vs vest4 | +0.849 |
| AlphaMissense vs primateai | +0.720 |
| AlphaMissense vs mutassessor | +0.655 |
| AlphaMissense vs provean | -0.757 |
| AlphaMissense vs esm1b | -0.788 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.468 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.557 |
| ESM-1v vs revel | -0.777 |
| ESM-1v vs cadd | -0.749 |
| ESM-1v vs sift | +0.785 |
| ESM-1v vs polyphen | -0.769 |
| ESM-1v vs metarnn | -0.851 |
| ESM-1v vs vest4 | -0.790 |
| ESM-1v vs primateai | -0.640 |
| ESM-1v vs mutassessor | -0.704 |
| ESM-1v vs provean | +0.824 |
| ESM-1v vs esm1b | +0.869 |
| ESM-1v vs am_dbnsfp | -0.869 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.703 |
| FoldX ΔΔG (ProtVar) vs revel | +0.411 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.373 |
| FoldX ΔΔG (ProtVar) vs sift | -0.434 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.402 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.493 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.469 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.311 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.428 |
| FoldX ΔΔG (ProtVar) vs provean | -0.458 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.461 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.520 |
| ThermoMPNN ΔΔG vs revel | +0.510 |
| ThermoMPNN ΔΔG vs cadd | +0.469 |
| ThermoMPNN ΔΔG vs sift | -0.513 |
| ThermoMPNN ΔΔG vs polyphen | +0.480 |
| ThermoMPNN ΔΔG vs metarnn | +0.560 |
| ThermoMPNN ΔΔG vs vest4 | +0.505 |
| ThermoMPNN ΔΔG vs primateai | +0.370 |
| ThermoMPNN ΔΔG vs mutassessor | +0.512 |
| ThermoMPNN ΔΔG vs provean | -0.537 |
| ThermoMPNN ΔΔG vs esm1b | -0.557 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.576 |
| revel vs cadd | +0.738 |
| revel vs sift | -0.702 |
| revel vs polyphen | +0.763 |
| revel vs metarnn | +0.880 |
| revel vs vest4 | +0.785 |
| revel vs primateai | +0.601 |
| revel vs mutassessor | +0.643 |
| revel vs provean | -0.732 |
| revel vs esm1b | -0.721 |
| revel vs am_dbnsfp | +0.783 |
| cadd vs sift | -0.742 |
| cadd vs polyphen | +0.757 |
| cadd vs metarnn | +0.787 |
| cadd vs vest4 | +0.771 |
| cadd vs primateai | +0.648 |
| cadd vs mutassessor | +0.561 |
| cadd vs provean | -0.725 |
| cadd vs esm1b | -0.660 |
| cadd vs am_dbnsfp | +0.771 |
| sift vs polyphen | -0.703 |
| sift vs metarnn | -0.790 |
| sift vs vest4 | -0.726 |
| sift vs primateai | -0.513 |
| sift vs mutassessor | -0.692 |
| sift vs provean | +0.823 |
| sift vs esm1b | +0.693 |
| sift vs am_dbnsfp | -0.742 |
| polyphen vs metarnn | +0.859 |
| polyphen vs vest4 | +0.785 |
| polyphen vs primateai | +0.718 |
| polyphen vs mutassessor | +0.555 |
| polyphen vs provean | -0.720 |
| polyphen vs esm1b | -0.677 |
| polyphen vs am_dbnsfp | +0.788 |
| metarnn vs vest4 | +0.919 |
| metarnn vs primateai | +0.694 |
| metarnn vs mutassessor | +0.695 |
| metarnn vs provean | -0.812 |
| metarnn vs esm1b | -0.760 |
| metarnn vs am_dbnsfp | +0.868 |
| vest4 vs primateai | +0.713 |
| vest4 vs mutassessor | +0.638 |
| vest4 vs provean | -0.763 |
| vest4 vs esm1b | -0.694 |
| vest4 vs am_dbnsfp | +0.848 |
| primateai vs mutassessor | +0.354 |
| primateai vs provean | -0.550 |
| primateai vs esm1b | -0.533 |
| primateai vs am_dbnsfp | +0.721 |
| mutassessor vs provean | -0.662 |
| mutassessor vs esm1b | -0.653 |
| mutassessor vs am_dbnsfp | +0.655 |
| provean vs esm1b | +0.746 |
| provean vs am_dbnsfp | -0.758 |
| esm1b vs am_dbnsfp | -0.791 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 12 |
| likely_benign | 2 |
| likely_pathogenic | 2 |
| benign | 1 |
| conflict | 1 |
| pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 560

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,360** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,353 | 2,007 |
| mean AlphaMissense | 0.26 | 0.864 |
| mean ESM-1v | 5.696 | 11.287 |
| mean FoldX ΔΔG | 0.667 | 2.894 |
| mean ThermoMPNN ΔΔG | 0.444 | 1.329 |
| mean REVEL | 0.278 | 0.687 |
| mean CADD phred | 16.373 | 26.842 |
| mean SIFT | -0.288 | -0.028 |
| mean PolyPhen-2 HVAR | 0.286 | 0.929 |
| mean MetaRNN | 0.296 | 0.859 |
| mean VEST4 | 0.309 | 0.772 |
| mean PrimateAI | 0.579 | 0.764 |
| mean PROVEAN | 1.181 | 4.072 |
| **fraction seen in gnomAD** | **21.29%** (288) | **10.66%** (214) |
| fraction at the interface | 2.66% | 3.19% |

**Validation:** the damaging cluster is **depleted** in the population — 10.66% of it appears in gnomAD against 21.29% of the tolerant cluster (a 2.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 10,830**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,635 | 6,195 |
| mean AlphaMissense | 0.411 | 0.954 |
| mean ESM-1v | 6.826 | 13.183 |
| mean FoldX ΔΔG | 0.619 | 3.789 |
| mean ThermoMPNN ΔΔG | 0.419 | 1.557 |
| **fraction seen in gnomAD** | **7.68%** (356) | **2.36%** (146) |

Depletion **3.3×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.73% | 2.42% |

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
