# SOS1 — variant-effect analysis

*Son of sevenless homolog 1* · UniProt `Q07889` · 1333 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| DH | 200–390 | 191 |
| PH | 444–548 | 105 |
| N-terminal Ras-GEF | 597–741 | 145 |
| Ras-GEF | 780–1019 | 240 |

**Pair analysed:** DH ↔ Ras-GEF

**AlphaFold PAE:** inter-module mean **14.55 Å**, intra-module **3.14 Å**, **ratio 4.63**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 62.8 | 0 | 100% / 100% |
| 3ksy.1.A (100.0% id) | 64.0 | 0 | 100% / 100% |
| 1xdv.1.A (100.0% id) | 61.8 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 25,327 |
| ESM-1v | 25,327 |
| FoldX ΔΔG (ProtVar) | 19,665 |
| ThermoMPNN ΔΔG | 25,327 |
| revel | 7,848 |
| cadd | 8,324 |
| sift | 7,848 |
| polyphen | 7,847 |
| metarnn | 7,848 |
| vest4 | 8,324 |
| primateai | 7,841 |
| mutassessor | 7,841 |
| provean | 7,848 |
| esm1b | 7,847 |
| am_dbnsfp | 7,842 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.480 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.480 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.511 |
| AlphaMissense vs revel | +0.687 |
| AlphaMissense vs cadd | +0.725 |
| AlphaMissense vs sift | -0.652 |
| AlphaMissense vs polyphen | +0.704 |
| AlphaMissense vs metarnn | +0.799 |
| AlphaMissense vs vest4 | +0.749 |
| AlphaMissense vs primateai | +0.615 |
| AlphaMissense vs mutassessor | +0.688 |
| AlphaMissense vs provean | -0.739 |
| AlphaMissense vs esm1b | -0.709 |
| AlphaMissense vs am_dbnsfp | +0.997 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.293 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.286 |
| ESM-1v vs revel | -0.390 |
| ESM-1v vs cadd | -0.439 |
| ESM-1v vs sift | +0.462 |
| ESM-1v vs polyphen | -0.391 |
| ESM-1v vs metarnn | -0.480 |
| ESM-1v vs vest4 | -0.392 |
| ESM-1v vs primateai | -0.277 |
| ESM-1v vs mutassessor | -0.446 |
| ESM-1v vs provean | +0.456 |
| ESM-1v vs esm1b | +0.496 |
| ESM-1v vs am_dbnsfp | -0.436 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.714 |
| FoldX ΔΔG (ProtVar) vs revel | +0.426 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.332 |
| FoldX ΔΔG (ProtVar) vs sift | -0.430 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.409 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.467 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.399 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.235 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.401 |
| FoldX ΔΔG (ProtVar) vs provean | -0.410 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.332 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.470 |
| ThermoMPNN ΔΔG vs revel | +0.441 |
| ThermoMPNN ΔΔG vs cadd | +0.399 |
| ThermoMPNN ΔΔG vs sift | -0.389 |
| ThermoMPNN ΔΔG vs polyphen | +0.398 |
| ThermoMPNN ΔΔG vs metarnn | +0.528 |
| ThermoMPNN ΔΔG vs vest4 | +0.468 |
| ThermoMPNN ΔΔG vs primateai | +0.306 |
| ThermoMPNN ΔΔG vs mutassessor | +0.454 |
| ThermoMPNN ΔΔG vs provean | -0.483 |
| ThermoMPNN ΔΔG vs esm1b | -0.509 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.512 |
| revel vs cadd | +0.621 |
| revel vs sift | -0.627 |
| revel vs polyphen | +0.705 |
| revel vs metarnn | +0.797 |
| revel vs vest4 | +0.713 |
| revel vs primateai | +0.537 |
| revel vs mutassessor | +0.708 |
| revel vs provean | -0.681 |
| revel vs esm1b | -0.535 |
| revel vs am_dbnsfp | +0.692 |
| cadd vs sift | -0.733 |
| cadd vs polyphen | +0.732 |
| cadd vs metarnn | +0.750 |
| cadd vs vest4 | +0.698 |
| cadd vs primateai | +0.470 |
| cadd vs mutassessor | +0.656 |
| cadd vs provean | -0.753 |
| cadd vs esm1b | -0.593 |
| cadd vs am_dbnsfp | +0.724 |
| sift vs polyphen | -0.646 |
| sift vs metarnn | -0.647 |
| sift vs vest4 | -0.548 |
| sift vs primateai | -0.372 |
| sift vs mutassessor | -0.668 |
| sift vs provean | +0.744 |
| sift vs esm1b | +0.509 |
| sift vs am_dbnsfp | -0.650 |
| polyphen vs metarnn | +0.761 |
| polyphen vs vest4 | +0.679 |
| polyphen vs primateai | +0.482 |
| polyphen vs mutassessor | +0.675 |
| polyphen vs provean | -0.669 |
| polyphen vs esm1b | -0.539 |
| polyphen vs am_dbnsfp | +0.707 |
| metarnn vs vest4 | +0.923 |
| metarnn vs primateai | +0.612 |
| metarnn vs mutassessor | +0.759 |
| metarnn vs provean | -0.776 |
| metarnn vs esm1b | -0.712 |
| metarnn vs am_dbnsfp | +0.806 |
| vest4 vs primateai | +0.605 |
| vest4 vs mutassessor | +0.669 |
| vest4 vs provean | -0.683 |
| vest4 vs esm1b | -0.670 |
| vest4 vs am_dbnsfp | +0.758 |
| primateai vs mutassessor | +0.482 |
| primateai vs provean | -0.451 |
| primateai vs esm1b | -0.430 |
| primateai vs am_dbnsfp | +0.620 |
| mutassessor vs provean | -0.718 |
| mutassessor vs esm1b | -0.592 |
| mutassessor vs am_dbnsfp | +0.689 |
| provean vs esm1b | +0.664 |
| provean vs am_dbnsfp | -0.739 |
| esm1b vs am_dbnsfp | -0.711 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 635 |
| conflict | 86 |
| likely_benign | 37 |
| likely_pathogenic | 36 |
| pathogenic | 21 |
| benign | 11 |

**gnomAD r4 missense variants mapped:** 1,428

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,097** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,486 | 3,611 |
| mean AlphaMissense | 0.259 | 0.811 |
| mean ESM-1v | 3.733 | 5.595 |
| mean FoldX ΔΔG | 0.535 | 2.366 |
| mean ThermoMPNN ΔΔG | 0.372 | 1.118 |
| mean REVEL | 0.259 | 0.626 |
| mean CADD phred | 18.223 | 27.167 |
| mean SIFT | -0.266 | -0.023 |
| mean PolyPhen-2 HVAR | 0.225 | 0.863 |
| mean MetaRNN | 0.37 | 0.816 |
| mean VEST4 | 0.471 | 0.812 |
| mean PrimateAI | 0.71 | 0.817 |
| mean PROVEAN | 1.302 | 4.783 |
| **fraction seen in gnomAD** | **22.57%** (561) | **11.41%** (412) |

**Validation:** the damaging cluster is **depleted** in the population — 11.41% of it appears in gnomAD against 22.57% of the tolerant cluster (a 2.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 20 pathogenic / 1 benign, cluster 0 has 1 / 8; OR = 160.0, p = 1.3e-05.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 19,665**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 12,613 | 7,052 |
| mean AlphaMissense | 0.568 | 0.948 |
| mean ESM-1v | 4.414 | 7.278 |
| mean FoldX ΔΔG | 0.566 | 4.456 |
| mean ThermoMPNN ΔΔG | 0.41 | 1.852 |
| **fraction seen in gnomAD** | **6.53%** (823) | **2.34%** (165) |

Depletion **2.8×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
