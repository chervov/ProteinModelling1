# PTPN6 — variant-effect analysis

*Tyrosine-protein phosphatase non-receptor type 6* · UniProt `P29350` · 595 aa · debug case

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 4–100 | 97 |
| SH2 2 | 110–213 | 104 |
| Tyrosine-protein phosphatase | 244–515 | 272 |

**Pair analysed:** SH2 1 ↔ Tyrosine-protein phosphatase

**AlphaFold PAE:** inter-module mean **12.88 Å**, intra-module **3.27 Å**, **ratio 3.94**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 40.8 | 16 | 100% / 100% |
| 3ps5.1.A (99.8% id) | 41.1 | 13 | 100% / 100% |
| 2b3o.1.A (100.0% id) | 30.2 | 77 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P29350_2b3o-1-A.pdb`, centroid distance **30.2 Å**, **77 residue pairs** in contact within 5 Å.

**Domain A interface residues (25):** `4, 5, 7, 31, 33, 36, 39, 56, 57, 58, 59, 60, 61, 62, 67, 68, 69, 70, 71, 72, 73, 74, 77, 78, 83`

**Domain B interface residues (30):** `245, 246, 248, 249, 252, 255, 256, 259, 262, 276, 277, 278, 279, 282, 358, 360, 419, 420, 421, 454, 455, 457, 458, 459, 496, 497, 500, 501, 502, 504`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,045 | 10,260 | 0.994 | 0.78 | 7.9e-140 |
| ESM-1v | 1,045 | 10,260 | -11.929 | -8.368 | 1.8e-109 |
| FoldX ΔΔG | 1,045 | 9,177 | 0.871 | 1.168 | 2.4e-10 |
| ThermoMPNN ΔΔG | 1,045 | 10,260 | 0.814 | 0.719 | 0.27 |
| REVEL | 315 | 2,978 | 0.812 | 0.424 | 5.8e-33 |
| CADD phred | 338 | 3,037 | 27.75 | 24.6 | 3e-17 |
| SIFT | 315 | 2,978 | 0.002 | 0.024 | 1.5e-12 |
| PolyPhen-2 HVAR | 315 | 2,896 | 0.971 | 0.423 | 7.5e-21 |
| MetaRNN | 315 | 2,978 | 0.899 | 0.561 | 8.2e-32 |
| VEST4 | 338 | 3,073 | 0.804 | 0.585 | 1.6e-22 |
| PrimateAI | 315 | 2,882 | 0.782 | 0.658 | 4.4e-50 |
| MutationAssessor | 315 | 2,811 | 2.705 | 2.065 | 1.8e-08 |
| PROVEAN | 315 | 2,978 | -5.11 | -2.63 | 2e-35 |
| ESM1b | 315 | 2,923 | -9.636 | -6.809 | 2.6e-26 |
| AlphaMissense (dbNSFP) | 315 | 2,976 | 0.973 | 0.454 | 8.9e-47 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 11,305 |
| ESM-1v | 11,305 |
| FoldX ΔΔG (ProtVar) | 10,222 |
| ThermoMPNN ΔΔG | 11,305 |
| revel | 3,293 |
| cadd | 3,375 |
| sift | 3,293 |
| polyphen | 3,211 |
| metarnn | 3,293 |
| vest4 | 3,411 |
| primateai | 3,197 |
| mutassessor | 3,126 |
| provean | 3,293 |
| esm1b | 3,238 |
| am_dbnsfp | 3,291 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.893 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.533 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.587 |
| AlphaMissense vs revel | +0.767 |
| AlphaMissense vs cadd | +0.727 |
| AlphaMissense vs sift | -0.694 |
| AlphaMissense vs polyphen | +0.828 |
| AlphaMissense vs metarnn | +0.825 |
| AlphaMissense vs vest4 | +0.818 |
| AlphaMissense vs primateai | +0.722 |
| AlphaMissense vs mutassessor | +0.743 |
| AlphaMissense vs provean | -0.753 |
| AlphaMissense vs esm1b | -0.805 |
| AlphaMissense vs am_dbnsfp | +0.955 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.504 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.591 |
| ESM-1v vs revel | -0.807 |
| ESM-1v vs cadd | -0.732 |
| ESM-1v vs sift | +0.724 |
| ESM-1v vs polyphen | -0.848 |
| ESM-1v vs metarnn | -0.847 |
| ESM-1v vs vest4 | -0.799 |
| ESM-1v vs primateai | -0.662 |
| ESM-1v vs mutassessor | -0.789 |
| ESM-1v vs provean | +0.819 |
| ESM-1v vs esm1b | +0.894 |
| ESM-1v vs am_dbnsfp | -0.849 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.705 |
| FoldX ΔΔG (ProtVar) vs revel | +0.478 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.418 |
| FoldX ΔΔG (ProtVar) vs sift | -0.453 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.510 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.495 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.492 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.348 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.509 |
| FoldX ΔΔG (ProtVar) vs provean | -0.440 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.494 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.513 |
| ThermoMPNN ΔΔG vs revel | +0.551 |
| ThermoMPNN ΔΔG vs cadd | +0.455 |
| ThermoMPNN ΔΔG vs sift | -0.430 |
| ThermoMPNN ΔΔG vs polyphen | +0.564 |
| ThermoMPNN ΔΔG vs metarnn | +0.566 |
| ThermoMPNN ΔΔG vs vest4 | +0.554 |
| ThermoMPNN ΔΔG vs primateai | +0.372 |
| ThermoMPNN ΔΔG vs mutassessor | +0.522 |
| ThermoMPNN ΔΔG vs provean | -0.503 |
| ThermoMPNN ΔΔG vs esm1b | -0.578 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.557 |
| revel vs cadd | +0.663 |
| revel vs sift | -0.610 |
| revel vs polyphen | +0.840 |
| revel vs metarnn | +0.911 |
| revel vs vest4 | +0.809 |
| revel vs primateai | +0.645 |
| revel vs mutassessor | +0.682 |
| revel vs provean | -0.773 |
| revel vs esm1b | -0.757 |
| revel vs am_dbnsfp | +0.788 |
| cadd vs sift | -0.691 |
| cadd vs polyphen | +0.769 |
| cadd vs metarnn | +0.735 |
| cadd vs vest4 | +0.730 |
| cadd vs primateai | +0.588 |
| cadd vs mutassessor | +0.705 |
| cadd vs provean | -0.705 |
| cadd vs esm1b | -0.707 |
| cadd vs am_dbnsfp | +0.734 |
| sift vs polyphen | -0.775 |
| sift vs metarnn | -0.693 |
| sift vs vest4 | -0.656 |
| sift vs primateai | -0.497 |
| sift vs mutassessor | -0.796 |
| sift vs provean | +0.668 |
| sift vs esm1b | +0.747 |
| sift vs am_dbnsfp | -0.718 |
| polyphen vs metarnn | +0.881 |
| polyphen vs vest4 | +0.822 |
| polyphen vs primateai | +0.677 |
| polyphen vs mutassessor | +0.796 |
| polyphen vs provean | -0.799 |
| polyphen vs esm1b | -0.812 |
| polyphen vs am_dbnsfp | +0.847 |
| metarnn vs vest4 | +0.899 |
| metarnn vs primateai | +0.676 |
| metarnn vs mutassessor | +0.788 |
| metarnn vs provean | -0.820 |
| metarnn vs esm1b | -0.798 |
| metarnn vs am_dbnsfp | +0.846 |
| vest4 vs primateai | +0.692 |
| vest4 vs mutassessor | +0.740 |
| vest4 vs provean | -0.770 |
| vest4 vs esm1b | -0.741 |
| vest4 vs am_dbnsfp | +0.832 |
| primateai vs mutassessor | +0.501 |
| primateai vs provean | -0.615 |
| primateai vs esm1b | -0.555 |
| primateai vs am_dbnsfp | +0.713 |
| mutassessor vs provean | -0.723 |
| mutassessor vs esm1b | -0.808 |
| mutassessor vs am_dbnsfp | +0.776 |
| provean vs esm1b | +0.797 |
| provean vs am_dbnsfp | -0.782 |
| esm1b vs am_dbnsfp | -0.831 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 13 |
| likely_benign | 1 |

**gnomAD r4 missense variants mapped:** 664

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,913** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,249 | 1,664 |
| mean AlphaMissense | 0.256 | 0.874 |
| mean ESM-1v | 5.093 | 10.635 |
| mean FoldX ΔΔG | 0.522 | 2.786 |
| mean ThermoMPNN ΔΔG | 0.445 | 1.344 |
| mean REVEL | 0.246 | 0.765 |
| mean CADD phred | 19.825 | 28.02 |
| mean SIFT | -0.28 | -0.021 |
| mean PolyPhen-2 HVAR | 0.132 | 0.875 |
| mean MetaRNN | 0.298 | 0.859 |
| mean VEST4 | 0.353 | 0.78 |
| mean PrimateAI | 0.553 | 0.743 |
| mean PROVEAN | 1.244 | 5.295 |
| **fraction seen in gnomAD** | **20.74%** (259) | **11.78%** (196) |
| fraction at the interface | 4.00% | 15.93% |

**Validation:** the damaging cluster is **depleted** in the population — 11.78% of it appears in gnomAD against 20.74% of the tolerant cluster (a 1.8-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 10,222**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,807 | 5,415 |
| mean AlphaMissense | 0.409 | 0.964 |
| mean ESM-1v | 6.123 | 12.536 |
| mean FoldX ΔΔG | 0.472 | 3.765 |
| mean ThermoMPNN ΔΔG | 0.412 | 1.614 |
| **fraction seen in gnomAD** | **7.80%** (375) | **2.88%** (156) |

Depletion **2.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 4.91% | 14.94% |

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
