# PTPRC — variant-effect analysis

*Receptor-type tyrosine-protein phosphatase C* · UniProt `P08575` · 1306 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Fibronectin type-III 1 | 391–483 | 93 |
| Fibronectin type-III 2 | 484–576 | 93 |
| Tyrosine-protein phosphatase 1 | 653–912 | 260 |
| Tyrosine-protein phosphatase 2 | 944–1228 | 285 |

**Pair analysed:** Fibronectin type-III 1 ↔ Tyrosine-protein phosphatase 2

**AlphaFold PAE:** inter-module mean **28.74 Å**, intra-module **5.76 Å**, **ratio 4.99**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 56.5 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 24,814 |
| ESM-1v | 24,814 |
| FoldX ΔΔG (ProtVar) | 18,658 |
| ThermoMPNN ΔΔG | 24,814 |
| revel | 7,278 |
| cadd | 7,690 |
| sift | 542 |
| polyphen | 0 |
| metarnn | 7,289 |
| vest4 | 7,704 |
| primateai | 7,265 |
| mutassessor | 0 |
| provean | 542 |
| esm1b | 7,275 |
| am_dbnsfp | 7,283 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.620 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.538 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.607 |
| AlphaMissense vs revel | +0.695 |
| AlphaMissense vs cadd | +0.688 |
| AlphaMissense vs sift | -0.440 |
| AlphaMissense vs metarnn | +0.763 |
| AlphaMissense vs vest4 | +0.767 |
| AlphaMissense vs primateai | +0.768 |
| AlphaMissense vs provean | -0.677 |
| AlphaMissense vs esm1b | -0.724 |
| AlphaMissense vs am_dbnsfp | +0.938 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.406 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.456 |
| ESM-1v vs revel | -0.600 |
| ESM-1v vs cadd | -0.558 |
| ESM-1v vs sift | +0.480 |
| ESM-1v vs metarnn | -0.641 |
| ESM-1v vs vest4 | -0.614 |
| ESM-1v vs primateai | -0.480 |
| ESM-1v vs provean | +0.538 |
| ESM-1v vs esm1b | +0.730 |
| ESM-1v vs am_dbnsfp | -0.575 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.695 |
| FoldX ΔΔG (ProtVar) vs revel | +0.360 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.281 |
| FoldX ΔΔG (ProtVar) vs sift | -0.272 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.409 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.438 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.311 |
| FoldX ΔΔG (ProtVar) vs provean | -0.444 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.364 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.531 |
| ThermoMPNN ΔΔG vs revel | +0.506 |
| ThermoMPNN ΔΔG vs cadd | +0.407 |
| ThermoMPNN ΔΔG vs sift | -0.305 |
| ThermoMPNN ΔΔG vs metarnn | +0.517 |
| ThermoMPNN ΔΔG vs vest4 | +0.527 |
| ThermoMPNN ΔΔG vs primateai | +0.480 |
| ThermoMPNN ΔΔG vs provean | -0.529 |
| ThermoMPNN ΔΔG vs esm1b | -0.518 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.598 |
| revel vs cadd | +0.767 |
| revel vs sift | -0.445 |
| revel vs metarnn | +0.862 |
| revel vs vest4 | +0.801 |
| revel vs primateai | +0.696 |
| revel vs provean | -0.673 |
| revel vs esm1b | -0.704 |
| revel vs am_dbnsfp | +0.653 |
| cadd vs sift | -0.429 |
| cadd vs metarnn | +0.887 |
| cadd vs vest4 | +0.842 |
| cadd vs primateai | +0.780 |
| cadd vs provean | -0.645 |
| cadd vs esm1b | -0.728 |
| cadd vs am_dbnsfp | +0.659 |
| sift vs metarnn | -0.520 |
| sift vs vest4 | -0.452 |
| sift vs primateai | -0.364 |
| sift vs provean | +0.615 |
| sift vs esm1b | +0.406 |
| sift vs am_dbnsfp | -0.406 |
| metarnn vs vest4 | +0.900 |
| metarnn vs primateai | +0.795 |
| metarnn vs provean | -0.715 |
| metarnn vs esm1b | -0.761 |
| metarnn vs am_dbnsfp | +0.750 |
| vest4 vs primateai | +0.782 |
| vest4 vs provean | -0.663 |
| vest4 vs esm1b | -0.749 |
| vest4 vs am_dbnsfp | +0.761 |
| primateai vs provean | -0.605 |
| primateai vs esm1b | -0.685 |
| primateai vs am_dbnsfp | +0.734 |
| provean vs esm1b | +0.667 |
| provean vs am_dbnsfp | -0.611 |
| esm1b vs am_dbnsfp | -0.681 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 299 |
| conflict | 10 |
| likely_benign | 8 |
| benign | 3 |
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 1,600

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 331** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 187 | 144 |
| mean AlphaMissense | 0.266 | 0.824 |
| mean ESM-1v | 4.428 | 8.882 |
| mean FoldX ΔΔG | 0.613 | 4.166 |
| mean ThermoMPNN ΔΔG | 0.454 | 1.558 |
| mean REVEL | 0.197 | 0.568 |
| mean CADD phred | 16.51 | 29.058 |
| mean SIFT | -0.149 | -0.038 |
| mean MetaRNN | 0.256 | 0.776 |
| mean VEST4 | 0.269 | 0.77 |
| mean PrimateAI | 0.432 | 0.659 |
| mean PROVEAN | 2.708 | 5.073 |
| **fraction seen in gnomAD** | **24.60%** (46) | **12.50%** (18) |

**Validation:** the damaging cluster is **depleted** in the population — 12.50% of it appears in gnomAD against 24.60% of the tolerant cluster (a 2.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 11 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 18,658**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 11,646 | 7,012 |
| mean AlphaMissense | 0.398 | 0.91 |
| mean ESM-1v | 4.578 | 9.197 |
| mean FoldX ΔΔG | 0.673 | 5.041 |
| mean ThermoMPNN ΔΔG | 0.448 | 1.909 |
| **fraction seen in gnomAD** | **7.44%** (867) | **3.29%** (231) |

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
