# DNM1 — variant-effect analysis

*Dynamin-1* · UniProt `Q05193` · 864 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 28–294 | 267 |
| PH | 519–625 | 107 |
| GED | 659–750 | 92 |

**Pair analysed:** Dynamin-type G ↔ GED

**AlphaFold PAE:** inter-module mean **19.04 Å**, intra-module **7.0 Å**, **ratio 2.72**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 61.9 | 5 | 100% / 100% |
| 5a3f.1.A (84.5% id) | 59.2 | 4 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `Q05193.pdb`, centroid distance **61.9 Å**, **5 residue pairs** in contact within 5 Å.

**Domain A interface residues (3):** `287, 290, 293`

**Domain B interface residues (4):** `742, 745, 749, 750`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 133 | 16,283 | 0.985 | 0.964 | 0.065 |
| ESM-1v | 133 | 16,283 | -14.787 | -13.341 | 5.8e-06 |
| FoldX ΔΔG | 133 | 13,908 | 1.066 | 0.935 | 0.63 |
| ThermoMPNN ΔΔG | 133 | 16,283 | 0.654 | 0.49 | 0.18 |
| REVEL | 42 | 5,087 | 0.752 | 0.671 | 0.19 |
| CADD phred | 42 | 5,319 | 28.65 | 25.9 | 0.062 |
| SIFT | 42 | 5,087 | 0.001 | 0.011 | 0.014 |
| PolyPhen-2 HVAR | 42 | 5,062 | 0.974 | 0.908 | 0.037 |
| MetaRNN | 42 | 5,107 | 0.875 | 0.764 | 0.0069 |
| VEST4 | 42 | 5,339 | 0.743 | 0.705 | 0.22 |
| PrimateAI | 42 | 5,057 | 0.822 | 0.841 | 0.34 |
| MutationAssessor | 42 | 5,057 | 2.86 | 2.585 | 0.048 |
| PROVEAN | 42 | 5,087 | -4.445 | -3.63 | 0.16 |
| ESM1b | 42 | 5,087 | -12.073 | -11.366 | 0.11 |
| AlphaMissense (dbNSFP) | 42 | 5,101 | 0.883 | 0.9 | 0.85 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 16,416 |
| ESM-1v | 16,416 |
| FoldX ΔΔG (ProtVar) | 14,041 |
| ThermoMPNN ΔΔG | 16,416 |
| revel | 5,129 |
| cadd | 5,361 |
| sift | 5,129 |
| polyphen | 5,104 |
| metarnn | 5,149 |
| vest4 | 5,381 |
| primateai | 5,099 |
| mutassessor | 5,099 |
| provean | 5,129 |
| esm1b | 5,129 |
| am_dbnsfp | 5,143 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.868 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.437 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.526 |
| AlphaMissense vs revel | +0.687 |
| AlphaMissense vs cadd | +0.674 |
| AlphaMissense vs sift | -0.674 |
| AlphaMissense vs polyphen | +0.551 |
| AlphaMissense vs metarnn | +0.790 |
| AlphaMissense vs vest4 | +0.735 |
| AlphaMissense vs primateai | +0.427 |
| AlphaMissense vs mutassessor | +0.688 |
| AlphaMissense vs provean | -0.715 |
| AlphaMissense vs esm1b | -0.784 |
| AlphaMissense vs am_dbnsfp | +0.998 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.361 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.467 |
| ESM-1v vs revel | -0.738 |
| ESM-1v vs cadd | -0.714 |
| ESM-1v vs sift | +0.714 |
| ESM-1v vs polyphen | -0.577 |
| ESM-1v vs metarnn | -0.798 |
| ESM-1v vs vest4 | -0.726 |
| ESM-1v vs primateai | -0.383 |
| ESM-1v vs mutassessor | -0.711 |
| ESM-1v vs provean | +0.751 |
| ESM-1v vs esm1b | +0.869 |
| ESM-1v vs am_dbnsfp | -0.858 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.681 |
| FoldX ΔΔG (ProtVar) vs revel | +0.377 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.298 |
| FoldX ΔΔG (ProtVar) vs sift | -0.365 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.264 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.415 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.371 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.239 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.373 |
| FoldX ΔΔG (ProtVar) vs provean | -0.370 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.360 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.433 |
| ThermoMPNN ΔΔG vs revel | +0.508 |
| ThermoMPNN ΔΔG vs cadd | +0.444 |
| ThermoMPNN ΔΔG vs sift | -0.487 |
| ThermoMPNN ΔΔG vs polyphen | +0.355 |
| ThermoMPNN ΔΔG vs metarnn | +0.545 |
| ThermoMPNN ΔΔG vs vest4 | +0.498 |
| ThermoMPNN ΔΔG vs primateai | +0.176 |
| ThermoMPNN ΔΔG vs mutassessor | +0.482 |
| ThermoMPNN ΔΔG vs provean | -0.460 |
| ThermoMPNN ΔΔG vs esm1b | -0.518 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.540 |
| revel vs cadd | +0.740 |
| revel vs sift | -0.738 |
| revel vs polyphen | +0.633 |
| revel vs metarnn | +0.863 |
| revel vs vest4 | +0.696 |
| revel vs primateai | +0.269 |
| revel vs mutassessor | +0.665 |
| revel vs provean | -0.694 |
| revel vs esm1b | -0.688 |
| revel vs am_dbnsfp | +0.688 |
| cadd vs sift | -0.764 |
| cadd vs polyphen | +0.610 |
| cadd vs metarnn | +0.751 |
| cadd vs vest4 | +0.669 |
| cadd vs primateai | +0.285 |
| cadd vs mutassessor | +0.666 |
| cadd vs provean | -0.691 |
| cadd vs esm1b | -0.660 |
| cadd vs am_dbnsfp | +0.673 |
| sift vs polyphen | -0.510 |
| sift vs metarnn | -0.765 |
| sift vs vest4 | -0.621 |
| sift vs primateai | -0.235 |
| sift vs mutassessor | -0.771 |
| sift vs provean | +0.691 |
| sift vs esm1b | +0.660 |
| sift vs am_dbnsfp | -0.675 |
| polyphen vs metarnn | +0.672 |
| polyphen vs vest4 | +0.590 |
| polyphen vs primateai | +0.277 |
| polyphen vs mutassessor | +0.501 |
| polyphen vs provean | -0.554 |
| polyphen vs esm1b | -0.537 |
| polyphen vs am_dbnsfp | +0.554 |
| metarnn vs vest4 | +0.885 |
| metarnn vs primateai | +0.337 |
| metarnn vs mutassessor | +0.760 |
| metarnn vs provean | -0.756 |
| metarnn vs esm1b | -0.756 |
| metarnn vs am_dbnsfp | +0.793 |
| vest4 vs primateai | +0.332 |
| vest4 vs mutassessor | +0.627 |
| vest4 vs provean | -0.682 |
| vest4 vs esm1b | -0.694 |
| vest4 vs am_dbnsfp | +0.737 |
| primateai vs mutassessor | +0.336 |
| primateai vs provean | -0.303 |
| primateai vs esm1b | -0.320 |
| primateai vs am_dbnsfp | +0.426 |
| mutassessor vs provean | -0.646 |
| mutassessor vs esm1b | -0.673 |
| mutassessor vs am_dbnsfp | +0.687 |
| provean vs esm1b | +0.733 |
| provean vs am_dbnsfp | -0.713 |
| esm1b vs am_dbnsfp | -0.785 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 796

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,390** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,324 | 3,066 |
| mean AlphaMissense | 0.46 | 0.924 |
| mean ESM-1v | 8.216 | 13.205 |
| mean FoldX ΔΔG | 0.401 | 1.896 |
| mean ThermoMPNN ΔΔG | 0.294 | 1.047 |
| mean REVEL | 0.412 | 0.784 |
| mean CADD phred | 20.133 | 28.556 |
| mean SIFT | -0.219 | -0.017 |
| mean PolyPhen-2 HVAR | 0.4 | 0.858 |
| mean MetaRNN | 0.411 | 0.856 |
| mean VEST4 | 0.47 | 0.782 |
| mean PrimateAI | 0.769 | 0.846 |
| mean PROVEAN | 2.023 | 5.106 |
| **fraction seen in gnomAD** | **18.58%** (246) | **11.25%** (345) |
| fraction at the interface | 0.76% | 1.04% |

**Validation:** the damaging cluster is **depleted** in the population — 11.25% of it appears in gnomAD against 18.58% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 14,041**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,705 | 5,336 |
| mean AlphaMissense | 0.783 | 0.988 |
| mean ESM-1v | 12.112 | 16.191 |
| mean FoldX ΔΔG | 0.418 | 3.994 |
| mean ThermoMPNN ΔΔG | 0.349 | 1.794 |
| **fraction seen in gnomAD** | **5.95%** (518) | **1.71%** (91) |

Depletion **3.5×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 0.95% | 0.94% |

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
