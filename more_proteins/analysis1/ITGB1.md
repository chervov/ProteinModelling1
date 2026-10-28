# ITGB1 — variant-effect analysis

*Integrin beta-1* · UniProt `P05556` · 798 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PSI | 26–76 | 51 |
| VWFA | 140–378 | 239 |
| I-EGF 1 | 466–501 | 36 |
| I-EGF 2 | 502–554 | 53 |
| I-EGF 3 | 555–591 | 37 |
| I-EGF 4 | 592–631 | 40 |

**Pair analysed:** PSI ↔ I-EGF 2

**AlphaFold PAE:** inter-module mean **8.01 Å**, intra-module **3.8 Å**, **ratio 2.11**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 20.2 | 15 | 100% / 100% |
| SWISSMODEL_7nxd-1-B_23-723 | 23.0 | 7 | 100% / 100% |
| SWISSMODEL_7usl-1-B_27-724 | 21.1 | 10 | 98% / 100% |
| SWISSMODEL_8xei-1-B_25-722 | 22.0 | 6 | 100% / 100% |
| SWISSMODEL_8xen-1-B_25-632 | 31.8 | 0 | 100% / 100% |
| SWISSMODEL_8xez-1-B_23-633 | 22.5 | 12 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P05556.pdb`, centroid distance **20.2 Å**, **15 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `28, 31, 56, 57, 59, 61, 62, 72`

**Domain B interface residues (8):** `536, 537, 538, 540, 544, 545, 550, 551`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 14,858 | 0.601 | 0.83 | 9.4e-06 |
| ESM-1v | 304 | 14,858 | -7.854 | -11.003 | 3.1e-17 |
| FoldX ΔΔG | 304 | 14,649 | 1.1 | 0.929 | 0.16 |
| ThermoMPNN ΔΔG | 304 | 14,858 | 0.461 | 0.591 | 0.0019 |
| REVEL | 94 | 4,649 | 0.547 | 0.685 | 0.056 |
| CADD phred | 102 | 4,949 | 24.0 | 25.8 | 0.039 |
| SIFT | 94 | 4,649 | 0.077 | 0.018 | 0.049 |
| PolyPhen-2 HVAR | 94 | 4,649 | 0.487 | 0.888 | 0.028 |
| MetaRNN | 94 | 4,649 | 0.48 | 0.787 | 0.00024 |
| VEST4 | 102 | 4,950 | 0.501 | 0.682 | 0.002 |
| PrimateAI | 94 | 4,642 | 0.652 | 0.712 | 0.016 |
| MutationAssessor | 94 | 4,642 | 1.717 | 2.632 | 0.0014 |
| PROVEAN | 94 | 4,649 | -1.545 | -2.46 | 0.047 |
| ESM1b | 94 | 4,649 | -7.013 | -9.234 | 0.00023 |
| AlphaMissense (dbNSFP) | 94 | 4,643 | 0.216 | 0.536 | 0.00024 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 15,162 |
| ESM-1v | 15,162 |
| FoldX ΔΔG (ProtVar) | 14,953 |
| ThermoMPNN ΔΔG | 15,162 |
| revel | 4,743 |
| cadd | 5,051 |
| sift | 4,743 |
| polyphen | 4,743 |
| metarnn | 4,743 |
| vest4 | 5,052 |
| primateai | 4,736 |
| mutassessor | 4,736 |
| provean | 4,743 |
| esm1b | 4,743 |
| am_dbnsfp | 4,737 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.877 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.520 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.434 |
| AlphaMissense vs revel | +0.826 |
| AlphaMissense vs cadd | +0.761 |
| AlphaMissense vs sift | -0.741 |
| AlphaMissense vs polyphen | +0.782 |
| AlphaMissense vs metarnn | +0.866 |
| AlphaMissense vs vest4 | +0.869 |
| AlphaMissense vs primateai | +0.677 |
| AlphaMissense vs mutassessor | +0.814 |
| AlphaMissense vs provean | -0.797 |
| AlphaMissense vs esm1b | -0.836 |
| AlphaMissense vs am_dbnsfp | +0.992 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.401 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.352 |
| ESM-1v vs revel | -0.832 |
| ESM-1v vs cadd | -0.767 |
| ESM-1v vs sift | +0.779 |
| ESM-1v vs polyphen | -0.760 |
| ESM-1v vs metarnn | -0.857 |
| ESM-1v vs vest4 | -0.840 |
| ESM-1v vs primateai | -0.678 |
| ESM-1v vs mutassessor | -0.833 |
| ESM-1v vs provean | +0.816 |
| ESM-1v vs esm1b | +0.905 |
| ESM-1v vs am_dbnsfp | -0.888 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.613 |
| FoldX ΔΔG (ProtVar) vs revel | +0.450 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.360 |
| FoldX ΔΔG (ProtVar) vs sift | -0.440 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.433 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.499 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.486 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.176 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.514 |
| FoldX ΔΔG (ProtVar) vs provean | -0.502 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.456 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.524 |
| ThermoMPNN ΔΔG vs revel | +0.364 |
| ThermoMPNN ΔΔG vs cadd | +0.269 |
| ThermoMPNN ΔΔG vs sift | -0.313 |
| ThermoMPNN ΔΔG vs polyphen | +0.273 |
| ThermoMPNN ΔΔG vs metarnn | +0.377 |
| ThermoMPNN ΔΔG vs vest4 | +0.362 |
| ThermoMPNN ΔΔG vs primateai | +0.112 |
| ThermoMPNN ΔΔG vs mutassessor | +0.390 |
| ThermoMPNN ΔΔG vs provean | -0.362 |
| ThermoMPNN ΔΔG vs esm1b | -0.361 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.379 |
| revel vs cadd | +0.755 |
| revel vs sift | -0.745 |
| revel vs polyphen | +0.776 |
| revel vs metarnn | +0.915 |
| revel vs vest4 | +0.848 |
| revel vs primateai | +0.664 |
| revel vs mutassessor | +0.812 |
| revel vs provean | -0.779 |
| revel vs esm1b | -0.784 |
| revel vs am_dbnsfp | +0.837 |
| cadd vs sift | -0.714 |
| cadd vs polyphen | +0.764 |
| cadd vs metarnn | +0.764 |
| cadd vs vest4 | +0.743 |
| cadd vs primateai | +0.627 |
| cadd vs mutassessor | +0.727 |
| cadd vs provean | -0.711 |
| cadd vs esm1b | -0.710 |
| cadd vs am_dbnsfp | +0.765 |
| sift vs polyphen | -0.684 |
| sift vs metarnn | -0.773 |
| sift vs vest4 | -0.709 |
| sift vs primateai | -0.476 |
| sift vs mutassessor | -0.779 |
| sift vs provean | +0.843 |
| sift vs esm1b | +0.770 |
| sift vs am_dbnsfp | -0.747 |
| polyphen vs metarnn | +0.820 |
| polyphen vs vest4 | +0.800 |
| polyphen vs primateai | +0.641 |
| polyphen vs mutassessor | +0.759 |
| polyphen vs provean | -0.706 |
| polyphen vs esm1b | -0.699 |
| polyphen vs am_dbnsfp | +0.785 |
| metarnn vs vest4 | +0.919 |
| metarnn vs primateai | +0.650 |
| metarnn vs mutassessor | +0.856 |
| metarnn vs provean | -0.807 |
| metarnn vs esm1b | -0.799 |
| metarnn vs am_dbnsfp | +0.873 |
| vest4 vs primateai | +0.675 |
| vest4 vs mutassessor | +0.799 |
| vest4 vs provean | -0.763 |
| vest4 vs esm1b | -0.784 |
| vest4 vs am_dbnsfp | +0.870 |
| primateai vs mutassessor | +0.525 |
| primateai vs provean | -0.494 |
| primateai vs esm1b | -0.588 |
| primateai vs am_dbnsfp | +0.706 |
| mutassessor vs provean | -0.840 |
| mutassessor vs esm1b | -0.810 |
| mutassessor vs am_dbnsfp | +0.817 |
| provean vs esm1b | +0.819 |
| provean vs am_dbnsfp | -0.799 |
| esm1b vs am_dbnsfp | -0.846 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 18 |
| likely_benign | 1 |

**gnomAD r4 missense variants mapped:** 765

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,669** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,958 | 2,711 |
| mean AlphaMissense | 0.212 | 0.822 |
| mean ESM-1v | 5.933 | 11.95 |
| mean FoldX ΔΔG | 0.495 | 3.483 |
| mean ThermoMPNN ΔΔG | 0.36 | 0.945 |
| mean REVEL | 0.39 | 0.826 |
| mean CADD phred | 18.648 | 28.767 |
| mean SIFT | -0.289 | -0.033 |
| mean PolyPhen-2 HVAR | 0.284 | 0.918 |
| mean MetaRNN | 0.371 | 0.891 |
| mean VEST4 | 0.358 | 0.799 |
| mean PrimateAI | 0.547 | 0.777 |
| mean PROVEAN | 0.995 | 4.911 |
| **fraction seen in gnomAD** | **19.05%** (373) | **11.07%** (300) |
| fraction at the interface | 3.06% | 1.25% |

**Validation:** the damaging cluster is **depleted** in the population — 11.07% of it appears in gnomAD against 19.05% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 14,953**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 6,612 | 8,341 |
| mean AlphaMissense | 0.344 | 0.943 |
| mean ESM-1v | 7.21 | 14.004 |
| mean FoldX ΔΔG | 0.502 | 3.971 |
| mean ThermoMPNN ΔΔG | 0.375 | 1.152 |
| **fraction seen in gnomAD** | **7.50%** (496) | **2.60%** (217) |

Depletion **2.9×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.93% | 1.32% |

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
