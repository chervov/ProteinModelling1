# SMARCA4 — variant-effect analysis

*SWI/SNF-related matrix-associated actin-dependent regulator of chromatin subfamily A member 4* · UniProt `P51532` · 1647 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| QLQ | 171–206 | 36 |
| HSA | 460–532 | 73 |
| Helicase ATP-binding | 766–931 | 166 |
| Helicase C-terminal | 1084–1246 | 163 |
| Bromo | 1453–1564 | 112 |

**Pair analysed:** HSA ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **23.34 Å**, intra-module **6.88 Å**, **ratio 3.39**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 71.1 | 0 | 100% / 100% |
| SWISSMODEL_7y8r-1-J_365-1345 | 71.4 | 0 | 100% / 100% |
| SWISSMODEL_9rl4-1-I_350-1400 | 65.2 | 0 | 100% / 100% |
| SWISSMODEL_9rn1-1-I_350-1382 | 67.7 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 31,293 |
| ESM-1v | 31,293 |
| FoldX ΔΔG (ProtVar) | 19,779 |
| ThermoMPNN ΔΔG | 31,293 |
| revel | 7,774 |
| cadd | 8,190 |
| sift | 7,781 |
| polyphen | 7,777 |
| metarnn | 7,793 |
| vest4 | 8,204 |
| primateai | 7,773 |
| mutassessor | 7,767 |
| provean | 7,781 |
| esm1b | 7,774 |
| am_dbnsfp | 7,789 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.552 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.383 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.473 |
| AlphaMissense vs revel | +0.643 |
| AlphaMissense vs cadd | +0.715 |
| AlphaMissense vs sift | -0.625 |
| AlphaMissense vs polyphen | +0.679 |
| AlphaMissense vs metarnn | +0.769 |
| AlphaMissense vs vest4 | +0.727 |
| AlphaMissense vs primateai | +0.729 |
| AlphaMissense vs mutassessor | +0.629 |
| AlphaMissense vs provean | -0.787 |
| AlphaMissense vs esm1b | -0.794 |
| AlphaMissense vs am_dbnsfp | +0.986 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.413 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.387 |
| ESM-1v vs revel | -0.538 |
| ESM-1v vs cadd | -0.475 |
| ESM-1v vs sift | +0.580 |
| ESM-1v vs polyphen | -0.560 |
| ESM-1v vs metarnn | -0.624 |
| ESM-1v vs vest4 | -0.574 |
| ESM-1v vs primateai | -0.435 |
| ESM-1v vs mutassessor | -0.447 |
| ESM-1v vs provean | +0.557 |
| ESM-1v vs esm1b | +0.560 |
| ESM-1v vs am_dbnsfp | -0.535 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.681 |
| FoldX ΔΔG (ProtVar) vs revel | +0.403 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.248 |
| FoldX ΔΔG (ProtVar) vs sift | -0.381 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.336 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.451 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.412 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.201 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.351 |
| FoldX ΔΔG (ProtVar) vs provean | -0.366 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.304 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.394 |
| ThermoMPNN ΔΔG vs revel | +0.439 |
| ThermoMPNN ΔΔG vs cadd | +0.366 |
| ThermoMPNN ΔΔG vs sift | -0.390 |
| ThermoMPNN ΔΔG vs polyphen | +0.371 |
| ThermoMPNN ΔΔG vs metarnn | +0.492 |
| ThermoMPNN ΔΔG vs vest4 | +0.439 |
| ThermoMPNN ΔΔG vs primateai | +0.337 |
| ThermoMPNN ΔΔG vs mutassessor | +0.399 |
| ThermoMPNN ΔΔG vs provean | -0.439 |
| ThermoMPNN ΔΔG vs esm1b | -0.455 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.476 |
| revel vs cadd | +0.599 |
| revel vs sift | -0.696 |
| revel vs polyphen | +0.674 |
| revel vs metarnn | +0.875 |
| revel vs vest4 | +0.713 |
| revel vs primateai | +0.531 |
| revel vs mutassessor | +0.492 |
| revel vs provean | -0.691 |
| revel vs esm1b | -0.563 |
| revel vs am_dbnsfp | +0.639 |
| cadd vs sift | -0.655 |
| cadd vs polyphen | +0.713 |
| cadd vs metarnn | +0.730 |
| cadd vs vest4 | +0.662 |
| cadd vs primateai | +0.543 |
| cadd vs mutassessor | +0.587 |
| cadd vs provean | -0.727 |
| cadd vs esm1b | -0.663 |
| cadd vs am_dbnsfp | +0.707 |
| sift vs polyphen | -0.735 |
| sift vs metarnn | -0.753 |
| sift vs vest4 | -0.628 |
| sift vs primateai | -0.452 |
| sift vs mutassessor | -0.565 |
| sift vs provean | +0.699 |
| sift vs esm1b | +0.570 |
| sift vs am_dbnsfp | -0.621 |
| polyphen vs metarnn | +0.787 |
| polyphen vs vest4 | +0.653 |
| polyphen vs primateai | +0.567 |
| polyphen vs mutassessor | +0.583 |
| polyphen vs provean | -0.695 |
| polyphen vs esm1b | -0.603 |
| polyphen vs am_dbnsfp | +0.673 |
| metarnn vs vest4 | +0.816 |
| metarnn vs primateai | +0.658 |
| metarnn vs mutassessor | +0.654 |
| metarnn vs provean | -0.813 |
| metarnn vs esm1b | -0.710 |
| metarnn vs am_dbnsfp | +0.782 |
| vest4 vs primateai | +0.632 |
| vest4 vs mutassessor | +0.577 |
| vest4 vs provean | -0.702 |
| vest4 vs esm1b | -0.642 |
| vest4 vs am_dbnsfp | +0.738 |
| primateai vs mutassessor | +0.442 |
| primateai vs provean | -0.611 |
| primateai vs esm1b | -0.612 |
| primateai vs am_dbnsfp | +0.728 |
| mutassessor vs provean | -0.629 |
| mutassessor vs esm1b | -0.583 |
| mutassessor vs am_dbnsfp | +0.624 |
| provean vs esm1b | +0.735 |
| provean vs am_dbnsfp | -0.782 |
| esm1b vs am_dbnsfp | -0.793 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1857 |
| conflict | 186 |
| likely_pathogenic | 43 |
| pathogenic | 13 |
| likely_benign | 6 |
| benign | 2 |

**gnomAD r4 missense variants mapped:** 1,415

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,934** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,693 | 3,241 |
| mean AlphaMissense | 0.575 | 0.954 |
| mean ESM-1v | 4.787 | 9.317 |
| mean FoldX ΔΔG | 0.391 | 1.875 |
| mean ThermoMPNN ΔΔG | 0.268 | 0.942 |
| mean REVEL | 0.351 | 0.746 |
| mean CADD phred | 22.592 | 28.909 |
| mean SIFT | -0.21 | -0.014 |
| mean PolyPhen-2 HVAR | 0.265 | 0.88 |
| mean MetaRNN | 0.431 | 0.861 |
| mean VEST4 | 0.538 | 0.821 |
| mean PrimateAI | 0.797 | 0.869 |
| mean PROVEAN | 2.021 | 5.056 |
| **fraction seen in gnomAD** | **14.47%** (245) | **7.00%** (227) |

**Validation:** the damaging cluster is **depleted** in the population — 7.00% of it appears in gnomAD against 14.47% of the tolerant cluster (a 2.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 9 pathogenic / 0 benign, cluster 0 has 0 / 2; OR = inf, p = 0.018.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 19,779**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 13,636 | 6,143 |
| mean AlphaMissense | 0.838 | 0.991 |
| mean ESM-1v | 6.775 | 13.306 |
| mean FoldX ΔΔG | 0.441 | 4.098 |
| mean ThermoMPNN ΔΔG | 0.326 | 1.756 |
| **fraction seen in gnomAD** | **4.31%** (588) | **1.27%** (78) |

Depletion **3.4×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
