# VCL — variant-effect analysis

*Vinculin* · UniProt `P18206` · 1134 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

No UniProt `Domain` features — nothing measurable. See the InterPro note in `more_proteins/jak_analogue_search_proposal.md` §2.


## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 21,546 |
| ESM-1v | 21,546 |
| FoldX ΔΔG (ProtVar) | 20,729 |
| ThermoMPNN ΔΔG | 21,546 |
| revel | 6,663 |
| cadd | 7,015 |
| sift | 6,663 |
| polyphen | 6,663 |
| metarnn | 6,663 |
| vest4 | 7,015 |
| primateai | 6,657 |
| mutassessor | 6,657 |
| provean | 6,663 |
| esm1b | 6,663 |
| am_dbnsfp | 6,657 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.563 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.413 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.451 |
| AlphaMissense vs revel | +0.683 |
| AlphaMissense vs cadd | +0.618 |
| AlphaMissense vs sift | -0.647 |
| AlphaMissense vs polyphen | +0.540 |
| AlphaMissense vs metarnn | +0.741 |
| AlphaMissense vs vest4 | +0.696 |
| AlphaMissense vs primateai | +0.629 |
| AlphaMissense vs mutassessor | +0.637 |
| AlphaMissense vs provean | -0.639 |
| AlphaMissense vs esm1b | -0.699 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.308 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.319 |
| ESM-1v vs revel | -0.520 |
| ESM-1v vs cadd | -0.526 |
| ESM-1v vs sift | +0.563 |
| ESM-1v vs polyphen | -0.383 |
| ESM-1v vs metarnn | -0.523 |
| ESM-1v vs vest4 | -0.441 |
| ESM-1v vs primateai | -0.300 |
| ESM-1v vs mutassessor | -0.460 |
| ESM-1v vs provean | +0.557 |
| ESM-1v vs esm1b | +0.737 |
| ESM-1v vs am_dbnsfp | -0.522 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.699 |
| FoldX ΔΔG (ProtVar) vs revel | +0.386 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.279 |
| FoldX ΔΔG (ProtVar) vs sift | -0.348 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.264 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.394 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.347 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.157 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.321 |
| FoldX ΔΔG (ProtVar) vs provean | -0.349 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.369 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.411 |
| ThermoMPNN ΔΔG vs revel | +0.452 |
| ThermoMPNN ΔΔG vs cadd | +0.349 |
| ThermoMPNN ΔΔG vs sift | -0.378 |
| ThermoMPNN ΔΔG vs polyphen | +0.291 |
| ThermoMPNN ΔΔG vs metarnn | +0.457 |
| ThermoMPNN ΔΔG vs vest4 | +0.405 |
| ThermoMPNN ΔΔG vs primateai | +0.217 |
| ThermoMPNN ΔΔG vs mutassessor | +0.375 |
| ThermoMPNN ΔΔG vs provean | -0.387 |
| ThermoMPNN ΔΔG vs esm1b | -0.430 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.474 |
| revel vs cadd | +0.671 |
| revel vs sift | -0.659 |
| revel vs polyphen | +0.627 |
| revel vs metarnn | +0.855 |
| revel vs vest4 | +0.751 |
| revel vs primateai | +0.488 |
| revel vs mutassessor | +0.664 |
| revel vs provean | -0.708 |
| revel vs esm1b | -0.621 |
| revel vs am_dbnsfp | +0.683 |
| cadd vs sift | -0.702 |
| cadd vs polyphen | +0.552 |
| cadd vs metarnn | +0.668 |
| cadd vs vest4 | +0.628 |
| cadd vs primateai | +0.398 |
| cadd vs mutassessor | +0.621 |
| cadd vs provean | -0.627 |
| cadd vs esm1b | -0.567 |
| cadd vs am_dbnsfp | +0.618 |
| sift vs polyphen | -0.452 |
| sift vs metarnn | -0.664 |
| sift vs vest4 | -0.525 |
| sift vs primateai | -0.392 |
| sift vs mutassessor | -0.695 |
| sift vs provean | +0.773 |
| sift vs esm1b | +0.639 |
| sift vs am_dbnsfp | -0.647 |
| polyphen vs metarnn | +0.660 |
| polyphen vs vest4 | +0.572 |
| polyphen vs primateai | +0.429 |
| polyphen vs mutassessor | +0.530 |
| polyphen vs provean | -0.495 |
| polyphen vs esm1b | -0.443 |
| polyphen vs am_dbnsfp | +0.541 |
| metarnn vs vest4 | +0.882 |
| metarnn vs primateai | +0.551 |
| metarnn vs mutassessor | +0.709 |
| metarnn vs provean | -0.695 |
| metarnn vs esm1b | -0.636 |
| metarnn vs am_dbnsfp | +0.742 |
| vest4 vs primateai | +0.567 |
| vest4 vs mutassessor | +0.571 |
| vest4 vs provean | -0.572 |
| vest4 vs esm1b | -0.556 |
| vest4 vs am_dbnsfp | +0.696 |
| primateai vs mutassessor | +0.463 |
| primateai vs provean | -0.454 |
| primateai vs esm1b | -0.496 |
| primateai vs am_dbnsfp | +0.629 |
| mutassessor vs provean | -0.730 |
| mutassessor vs esm1b | -0.609 |
| mutassessor vs am_dbnsfp | +0.637 |
| provean vs esm1b | +0.713 |
| provean vs am_dbnsfp | -0.638 |
| esm1b vs am_dbnsfp | -0.700 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 585 |
| conflict | 21 |
| likely_benign | 3 |
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 1,149

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,399** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,908 | 3,491 |
| mean AlphaMissense | 0.327 | 0.818 |
| mean ESM-1v | 4.096 | 6.386 |
| mean FoldX ΔΔG | 0.55 | 2.171 |
| mean ThermoMPNN ΔΔG | 0.378 | 1.115 |
| mean REVEL | 0.208 | 0.492 |
| mean CADD phred | 22.971 | 28.942 |
| mean SIFT | -0.267 | -0.027 |
| mean PolyPhen-2 HVAR | 0.515 | 0.918 |
| mean MetaRNN | 0.403 | 0.807 |
| mean VEST4 | 0.572 | 0.825 |
| mean PrimateAI | 0.734 | 0.836 |
| mean PROVEAN | 0.938 | 3.761 |
| **fraction seen in gnomAD** | **20.56%** (598) | **14.15%** (494) |

**Validation:** the damaging cluster is **depleted** in the population — 14.15% of it appears in gnomAD against 20.56% of the tolerant cluster (a 1.5-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 20,729**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 14,423 | 6,306 |
| mean AlphaMissense | 0.614 | 0.953 |
| mean ESM-1v | 5.213 | 8.147 |
| mean FoldX ΔΔG | 0.488 | 4.763 |
| mean ThermoMPNN ΔΔG | 0.388 | 1.839 |
| **fraction seen in gnomAD** | **6.43%** (928) | **2.60%** (164) |

Depletion **2.5×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
