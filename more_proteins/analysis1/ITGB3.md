# ITGB3 — variant-effect analysis

*Integrin beta-3* · UniProt `P05106` · 788 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PSI | 30–76 | 47 |
| VWFA | 135–377 | 243 |
| I-EGF 1 | 463–498 | 36 |
| I-EGF 2 | 499–548 | 50 |
| I-EGF 3 | 549–585 | 37 |
| I-EGF 4 | 586–625 | 40 |

**Pair analysed:** PSI ↔ I-EGF 4

**AlphaFold PAE:** inter-module mean **13.48 Å**, intra-module **2.62 Å**, **ratio 5.14**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 46.4 | 0 | 100% / 100% |
| 6bxj.1.A (78.3% id) | 45.4 | 0 | 100% / 100% |
| 8xei.1.B (100.0% id) | 46.4 | 0 | 100% / 100% |
| 8xez.1.B (100.0% id) | 51.0 | 0 | 100% / 100% |
| 8xen.1.B (100.0% id) | 77.1 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 14,972 |
| ESM-1v | 14,972 |
| FoldX ΔΔG (ProtVar) | 14,440 |
| ThermoMPNN ΔΔG | 14,972 |
| revel | 0 |
| cadd | 4,913 |
| sift | 4,664 |
| polyphen | 4,664 |
| metarnn | 4,665 |
| vest4 | 4,915 |
| primateai | 4,658 |
| mutassessor | 4,658 |
| provean | 4,664 |
| esm1b | 4,664 |
| am_dbnsfp | 4,659 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.827 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.565 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.454 |
| AlphaMissense vs cadd | +0.733 |
| AlphaMissense vs sift | -0.751 |
| AlphaMissense vs polyphen | +0.785 |
| AlphaMissense vs metarnn | +0.866 |
| AlphaMissense vs vest4 | +0.858 |
| AlphaMissense vs primateai | +0.619 |
| AlphaMissense vs mutassessor | +0.774 |
| AlphaMissense vs provean | -0.804 |
| AlphaMissense vs esm1b | -0.805 |
| AlphaMissense vs am_dbnsfp | +0.999 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.470 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.388 |
| ESM-1v vs cadd | -0.692 |
| ESM-1v vs sift | +0.821 |
| ESM-1v vs polyphen | -0.674 |
| ESM-1v vs metarnn | -0.810 |
| ESM-1v vs vest4 | -0.763 |
| ESM-1v vs primateai | -0.491 |
| ESM-1v vs mutassessor | -0.787 |
| ESM-1v vs provean | +0.839 |
| ESM-1v vs esm1b | +0.871 |
| ESM-1v vs am_dbnsfp | -0.821 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.616 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.358 |
| FoldX ΔΔG (ProtVar) vs sift | -0.463 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.466 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.521 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.522 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.351 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.477 |
| FoldX ΔΔG (ProtVar) vs provean | -0.525 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.477 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.569 |
| ThermoMPNN ΔΔG vs cadd | +0.290 |
| ThermoMPNN ΔΔG vs sift | -0.346 |
| ThermoMPNN ΔΔG vs polyphen | +0.343 |
| ThermoMPNN ΔΔG vs metarnn | +0.376 |
| ThermoMPNN ΔΔG vs vest4 | +0.371 |
| ThermoMPNN ΔΔG vs primateai | +0.124 |
| ThermoMPNN ΔΔG vs mutassessor | +0.362 |
| ThermoMPNN ΔΔG vs provean | -0.372 |
| ThermoMPNN ΔΔG vs esm1b | -0.398 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.404 |
| cadd vs sift | -0.728 |
| cadd vs polyphen | +0.766 |
| cadd vs metarnn | +0.777 |
| cadd vs vest4 | +0.764 |
| cadd vs primateai | +0.530 |
| cadd vs mutassessor | +0.711 |
| cadd vs provean | -0.724 |
| cadd vs esm1b | -0.692 |
| cadd vs am_dbnsfp | +0.733 |
| sift vs polyphen | -0.679 |
| sift vs metarnn | -0.796 |
| sift vs vest4 | -0.736 |
| sift vs primateai | -0.456 |
| sift vs mutassessor | -0.744 |
| sift vs provean | +0.829 |
| sift vs esm1b | +0.754 |
| sift vs am_dbnsfp | -0.755 |
| polyphen vs metarnn | +0.827 |
| polyphen vs vest4 | +0.817 |
| polyphen vs primateai | +0.569 |
| polyphen vs mutassessor | +0.766 |
| polyphen vs provean | -0.736 |
| polyphen vs esm1b | -0.690 |
| polyphen vs am_dbnsfp | +0.783 |
| metarnn vs vest4 | +0.937 |
| metarnn vs primateai | +0.582 |
| metarnn vs mutassessor | +0.835 |
| metarnn vs provean | -0.837 |
| metarnn vs esm1b | -0.789 |
| metarnn vs am_dbnsfp | +0.872 |
| vest4 vs primateai | +0.635 |
| vest4 vs mutassessor | +0.792 |
| vest4 vs provean | -0.799 |
| vest4 vs esm1b | -0.762 |
| vest4 vs am_dbnsfp | +0.861 |
| primateai vs mutassessor | +0.434 |
| primateai vs provean | -0.487 |
| primateai vs esm1b | -0.465 |
| primateai vs am_dbnsfp | +0.618 |
| mutassessor vs provean | -0.794 |
| mutassessor vs esm1b | -0.768 |
| mutassessor vs am_dbnsfp | +0.774 |
| provean vs esm1b | +0.791 |
| provean vs am_dbnsfp | -0.804 |
| esm1b vs am_dbnsfp | -0.805 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 168 |
| likely_pathogenic | 43 |
| pathogenic | 16 |
| benign | 6 |
| likely_benign | 5 |
| conflict | 2 |

**gnomAD r4 missense variants mapped:** 957

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,512** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,992 | 2,520 |
| mean AlphaMissense | 0.171 | 0.739 |
| mean ESM-1v | 4.368 | 9.173 |
| mean FoldX ΔΔG | 0.556 | 3.695 |
| mean ThermoMPNN ΔΔG | 0.415 | 1.071 |
| mean CADD phred | 18.424 | 27.779 |
| mean SIFT | -0.274 | -0.019 |
| mean PolyPhen-2 HVAR | 0.285 | 0.94 |
| mean MetaRNN | 0.373 | 0.901 |
| mean VEST4 | 0.342 | 0.807 |
| mean PrimateAI | 0.489 | 0.693 |
| mean PROVEAN | 1.273 | 5.353 |
| **fraction seen in gnomAD** | **21.79%** (434) | **17.82%** (449) |

**Validation:** the damaging cluster is **depleted** in the population — 17.82% of it appears in gnomAD against 21.79% of the tolerant cluster (a 1.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 15 pathogenic / 0 benign, cluster 0 has 0 / 5; OR = inf, p = 6.4e-05.


### The same split on all variants, using only the four full-coverage features

The table above uses 11 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 14,440**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 7,663 | 6,777 |
| mean AlphaMissense | 0.333 | 0.922 |
| mean ESM-1v | 5.281 | 11.123 |
| mean FoldX ΔΔG | 0.567 | 4.635 |
| mean ThermoMPNN ΔΔG | 0.453 | 1.358 |
| **fraction seen in gnomAD** | **8.27%** (634) | **3.90%** (264) |

Depletion **2.1×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
