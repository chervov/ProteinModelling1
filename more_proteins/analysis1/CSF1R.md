# CSF1R — variant-effect analysis

*Macrophage colony-stimulating factor 1 receptor* · UniProt `P07333` · 972 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Ig-like C2-type 1 | 21–104 | 84 |
| Ig-like C2-type 2 | 107–197 | 91 |
| Ig-like C2-type 3 | 203–290 | 88 |
| Ig-like C2-type 4 | 299–399 | 101 |
| Ig-like C2-type 5 | 402–502 | 101 |
| Protein kinase | 582–910 | 329 |

**Pair analysed:** Ig-like C2-type 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **28.91 Å**, intra-module **7.42 Å**, **ratio 3.9**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 51.5 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 18,468 |
| ESM-1v | 18,468 |
| FoldX ΔΔG (ProtVar) | 15,238 |
| ThermoMPNN ΔΔG | 18,468 |
| revel | 5,736 |
| cadd | 5,999 |
| sift | 5,736 |
| polyphen | 5,716 |
| metarnn | 5,736 |
| vest4 | 5,999 |
| primateai | 5,710 |
| mutassessor | 5,710 |
| provean | 5,736 |
| esm1b | 5,736 |
| am_dbnsfp | 5,730 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.845 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.512 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.514 |
| AlphaMissense vs revel | +0.747 |
| AlphaMissense vs cadd | +0.763 |
| AlphaMissense vs sift | -0.758 |
| AlphaMissense vs polyphen | +0.780 |
| AlphaMissense vs metarnn | +0.838 |
| AlphaMissense vs vest4 | +0.833 |
| AlphaMissense vs primateai | +0.737 |
| AlphaMissense vs mutassessor | +0.455 |
| AlphaMissense vs provean | -0.762 |
| AlphaMissense vs esm1b | -0.781 |
| AlphaMissense vs am_dbnsfp | +0.996 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.425 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.408 |
| ESM-1v vs revel | -0.805 |
| ESM-1v vs cadd | -0.794 |
| ESM-1v vs sift | +0.793 |
| ESM-1v vs polyphen | -0.780 |
| ESM-1v vs metarnn | -0.846 |
| ESM-1v vs vest4 | -0.818 |
| ESM-1v vs primateai | -0.721 |
| ESM-1v vs mutassessor | -0.367 |
| ESM-1v vs provean | +0.795 |
| ESM-1v vs esm1b | +0.884 |
| ESM-1v vs am_dbnsfp | -0.825 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.697 |
| FoldX ΔΔG (ProtVar) vs revel | +0.331 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.340 |
| FoldX ΔΔG (ProtVar) vs sift | -0.386 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.433 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.435 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.439 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.278 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.415 |
| FoldX ΔΔG (ProtVar) vs provean | -0.444 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.442 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.518 |
| ThermoMPNN ΔΔG vs revel | +0.323 |
| ThermoMPNN ΔΔG vs cadd | +0.344 |
| ThermoMPNN ΔΔG vs sift | -0.379 |
| ThermoMPNN ΔΔG vs polyphen | +0.413 |
| ThermoMPNN ΔΔG vs metarnn | +0.445 |
| ThermoMPNN ΔΔG vs vest4 | +0.435 |
| ThermoMPNN ΔΔG vs primateai | +0.272 |
| ThermoMPNN ΔΔG vs mutassessor | +0.413 |
| ThermoMPNN ΔΔG vs provean | -0.452 |
| ThermoMPNN ΔΔG vs esm1b | -0.468 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.531 |
| revel vs cadd | +0.833 |
| revel vs sift | -0.744 |
| revel vs polyphen | +0.792 |
| revel vs metarnn | +0.889 |
| revel vs vest4 | +0.849 |
| revel vs primateai | +0.797 |
| revel vs mutassessor | +0.258 |
| revel vs provean | -0.698 |
| revel vs esm1b | -0.713 |
| revel vs am_dbnsfp | +0.749 |
| cadd vs sift | -0.805 |
| cadd vs polyphen | +0.817 |
| cadd vs metarnn | +0.861 |
| cadd vs vest4 | +0.828 |
| cadd vs primateai | +0.768 |
| cadd vs mutassessor | +0.299 |
| cadd vs provean | -0.712 |
| cadd vs esm1b | -0.707 |
| cadd vs am_dbnsfp | +0.761 |
| sift vs polyphen | -0.798 |
| sift vs metarnn | -0.821 |
| sift vs vest4 | -0.781 |
| sift vs primateai | -0.681 |
| sift vs mutassessor | -0.379 |
| sift vs provean | +0.789 |
| sift vs esm1b | +0.724 |
| sift vs am_dbnsfp | -0.752 |
| polyphen vs metarnn | +0.879 |
| polyphen vs vest4 | +0.836 |
| polyphen vs primateai | +0.724 |
| polyphen vs mutassessor | +0.427 |
| polyphen vs provean | -0.742 |
| polyphen vs esm1b | -0.712 |
| polyphen vs am_dbnsfp | +0.780 |
| metarnn vs vest4 | +0.936 |
| metarnn vs primateai | +0.805 |
| metarnn vs mutassessor | +0.432 |
| metarnn vs provean | -0.793 |
| metarnn vs esm1b | -0.773 |
| metarnn vs am_dbnsfp | +0.841 |
| vest4 vs primateai | +0.788 |
| vest4 vs mutassessor | +0.429 |
| vest4 vs provean | -0.755 |
| vest4 vs esm1b | -0.749 |
| vest4 vs am_dbnsfp | +0.835 |
| primateai vs mutassessor | +0.196 |
| primateai vs provean | -0.611 |
| primateai vs esm1b | -0.630 |
| primateai vs am_dbnsfp | +0.737 |
| mutassessor vs provean | -0.488 |
| mutassessor vs esm1b | -0.419 |
| mutassessor vs am_dbnsfp | +0.455 |
| provean vs esm1b | +0.747 |
| provean vs am_dbnsfp | -0.762 |
| esm1b vs am_dbnsfp | -0.784 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 206 |
| likely_benign | 55 |
| conflict | 33 |
| likely_pathogenic | 25 |
| benign | 14 |
| pathogenic | 12 |

**gnomAD r4 missense variants mapped:** 1,129

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,697** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,632 | 2,065 |
| mean AlphaMissense | 0.145 | 0.699 |
| mean ESM-1v | 4.791 | 11.194 |
| mean FoldX ΔΔG | 0.783 | 3.248 |
| mean ThermoMPNN ΔΔG | 0.562 | 1.423 |
| mean REVEL | 0.12 | 0.647 |
| mean CADD phred | 11.812 | 27.088 |
| mean SIFT | -0.288 | -0.012 |
| mean PolyPhen-2 HVAR | 0.259 | 0.931 |
| mean MetaRNN | 0.235 | 0.879 |
| mean VEST4 | 0.261 | 0.753 |
| mean PrimateAI | 0.36 | 0.647 |
| mean PROVEAN | 1.254 | 4.764 |
| **fraction seen in gnomAD** | **24.81%** (653) | **11.19%** (231) |

**Validation:** the damaging cluster is **depleted** in the population — 11.19% of it appears in gnomAD against 24.81% of the tolerant cluster (a 2.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 12 pathogenic / 1 benign, cluster 0 has 0 / 11; OR = inf, p = 9.6e-06.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 15,238**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 9,292 | 5,946 |
| mean AlphaMissense | 0.25 | 0.882 |
| mean ESM-1v | 5.898 | 13.4 |
| mean FoldX ΔΔG | 0.744 | 4.64 |
| mean ThermoMPNN ΔΔG | 0.545 | 1.763 |
| **fraction seen in gnomAD** | **8.37%** (778) | **1.93%** (115) |

Depletion **4.3×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.

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
