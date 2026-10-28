# CAPN1 — variant-effect analysis

*Calpain-1 catalytic subunit* · UniProt `P07384` · 714 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Calpain catalytic | 55–354 | 300 |
| EF-hand 1 | 541–576 | 36 |
| EF-hand 2 | 585–618 | 34 |
| EF-hand 3 | 615–650 | 36 |
| EF-hand 4 | 680–714 | 35 |

**Pair analysed:** Calpain catalytic ↔ EF-hand 4

**AlphaFold PAE:** inter-module mean **13.37 Å**, intra-module **4.19 Å**, **ratio 3.19**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 55.8 | 0 | 100% / 100% |
| 1df0.1.A (61.7% id) | 55.3 | 0 | 100% / 97% |
| 3bow.1.A (61.7% id) | 47.7 | 0 | 100% / 97% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 13,566 |
| ESM-1v | 13,566 |
| FoldX ΔΔG (ProtVar) | 13,338 |
| ThermoMPNN ΔΔG | 13,566 |
| revel | 4,188 |
| cadd | 4,388 |
| sift | 4,188 |
| polyphen | 4,188 |
| metarnn | 4,188 |
| vest4 | 4,388 |
| primateai | 4,182 |
| mutassessor | 4,182 |
| provean | 4,188 |
| esm1b | 4,188 |
| am_dbnsfp | 4,182 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.805 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.553 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.549 |
| AlphaMissense vs revel | +0.707 |
| AlphaMissense vs cadd | +0.747 |
| AlphaMissense vs sift | -0.719 |
| AlphaMissense vs polyphen | +0.747 |
| AlphaMissense vs metarnn | +0.831 |
| AlphaMissense vs vest4 | +0.844 |
| AlphaMissense vs primateai | +0.670 |
| AlphaMissense vs mutassessor | +0.758 |
| AlphaMissense vs provean | -0.731 |
| AlphaMissense vs esm1b | -0.819 |
| AlphaMissense vs am_dbnsfp | +0.995 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.531 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.535 |
| ESM-1v vs revel | -0.700 |
| ESM-1v vs cadd | -0.728 |
| ESM-1v vs sift | +0.787 |
| ESM-1v vs polyphen | -0.692 |
| ESM-1v vs metarnn | -0.840 |
| ESM-1v vs vest4 | -0.782 |
| ESM-1v vs primateai | -0.554 |
| ESM-1v vs mutassessor | -0.833 |
| ESM-1v vs provean | +0.778 |
| ESM-1v vs esm1b | +0.863 |
| ESM-1v vs am_dbnsfp | -0.798 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.694 |
| FoldX ΔΔG (ProtVar) vs revel | +0.428 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.446 |
| FoldX ΔΔG (ProtVar) vs sift | -0.489 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.450 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.517 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.490 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.369 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.516 |
| FoldX ΔΔG (ProtVar) vs provean | -0.497 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.508 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.547 |
| ThermoMPNN ΔΔG vs revel | +0.436 |
| ThermoMPNN ΔΔG vs cadd | +0.450 |
| ThermoMPNN ΔΔG vs sift | -0.509 |
| ThermoMPNN ΔΔG vs polyphen | +0.456 |
| ThermoMPNN ΔΔG vs metarnn | +0.530 |
| ThermoMPNN ΔΔG vs vest4 | +0.486 |
| ThermoMPNN ΔΔG vs primateai | +0.335 |
| ThermoMPNN ΔΔG vs mutassessor | +0.547 |
| ThermoMPNN ΔΔG vs provean | -0.526 |
| ThermoMPNN ΔΔG vs esm1b | -0.548 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.556 |
| revel vs cadd | +0.671 |
| revel vs sift | -0.670 |
| revel vs polyphen | +0.689 |
| revel vs metarnn | +0.846 |
| revel vs vest4 | +0.759 |
| revel vs primateai | +0.615 |
| revel vs mutassessor | +0.705 |
| revel vs provean | -0.678 |
| revel vs esm1b | -0.664 |
| revel vs am_dbnsfp | +0.716 |
| cadd vs sift | -0.757 |
| cadd vs polyphen | +0.774 |
| cadd vs metarnn | +0.779 |
| cadd vs vest4 | +0.745 |
| cadd vs primateai | +0.543 |
| cadd vs mutassessor | +0.738 |
| cadd vs provean | -0.723 |
| cadd vs esm1b | -0.726 |
| cadd vs am_dbnsfp | +0.752 |
| sift vs polyphen | -0.678 |
| sift vs metarnn | -0.779 |
| sift vs vest4 | -0.715 |
| sift vs primateai | -0.487 |
| sift vs mutassessor | -0.789 |
| sift vs provean | +0.748 |
| sift vs esm1b | +0.762 |
| sift vs am_dbnsfp | -0.733 |
| polyphen vs metarnn | +0.810 |
| polyphen vs vest4 | +0.791 |
| polyphen vs primateai | +0.640 |
| polyphen vs mutassessor | +0.745 |
| polyphen vs provean | -0.715 |
| polyphen vs esm1b | -0.700 |
| polyphen vs am_dbnsfp | +0.746 |
| metarnn vs vest4 | +0.894 |
| metarnn vs primateai | +0.687 |
| metarnn vs mutassessor | +0.832 |
| metarnn vs provean | -0.799 |
| metarnn vs esm1b | -0.797 |
| metarnn vs am_dbnsfp | +0.840 |
| vest4 vs primateai | +0.707 |
| vest4 vs mutassessor | +0.770 |
| vest4 vs provean | -0.742 |
| vest4 vs esm1b | -0.772 |
| vest4 vs am_dbnsfp | +0.847 |
| primateai vs mutassessor | +0.566 |
| primateai vs provean | -0.547 |
| primateai vs esm1b | -0.547 |
| primateai vs am_dbnsfp | +0.674 |
| mutassessor vs provean | -0.774 |
| mutassessor vs esm1b | -0.806 |
| mutassessor vs am_dbnsfp | +0.768 |
| provean vs esm1b | +0.785 |
| provean vs am_dbnsfp | -0.741 |
| esm1b vs am_dbnsfp | -0.826 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 94 |
| pathogenic | 4 |
| likely_benign | 4 |
| benign | 3 |
| conflict | 2 |

**gnomAD r4 missense variants mapped:** 903

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,117** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,665 | 2,452 |
| mean AlphaMissense | 0.247 | 0.829 |
| mean ESM-1v | 4.566 | 9.436 |
| mean FoldX ΔΔG | 0.559 | 3.143 |
| mean ThermoMPNN ΔΔG | 0.481 | 1.371 |
| mean REVEL | 0.229 | 0.689 |
| mean CADD phred | 18.689 | 28.457 |
| mean SIFT | -0.27 | -0.017 |
| mean PolyPhen-2 HVAR | 0.23 | 0.889 |
| mean MetaRNN | 0.323 | 0.886 |
| mean VEST4 | 0.316 | 0.798 |
| mean PrimateAI | 0.509 | 0.69 |
| mean PROVEAN | 1.68 | 5.438 |
| **fraction seen in gnomAD** | **23.24%** (387) | **20.23%** (496) |

**Validation:** the damaging cluster is **depleted** in the population — 20.23% of it appears in gnomAD against 23.24% of the tolerant cluster (a 1.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 13,338**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 6,911 | 6,427 |
| mean AlphaMissense | 0.461 | 0.953 |
| mean ESM-1v | 5.744 | 11.632 |
| mean FoldX ΔΔG | 0.612 | 4.707 |
| mean ThermoMPNN ΔΔG | 0.485 | 1.777 |
| **fraction seen in gnomAD** | **8.61%** (595) | **4.48%** (288) |

Depletion **1.9×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
