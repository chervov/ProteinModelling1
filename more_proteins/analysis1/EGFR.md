# EGFR — variant-effect analysis

*Epidermal growth factor receptor* · UniProt `P00533` · 1210 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Protein kinase | 712–979 | 268 |


## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 22,990 |
| ESM-1v | 22,990 |
| FoldX ΔΔG (ProtVar) | 18,582 |
| ThermoMPNN ΔΔG | 22,990 |
| revel | 6,914 |
| cadd | 7,260 |
| sift | 6,914 |
| polyphen | 6,914 |
| metarnn | 6,914 |
| vest4 | 7,267 |
| primateai | 6,897 |
| mutassessor | 6,897 |
| provean | 6,914 |
| esm1b | 6,911 |
| am_dbnsfp | 6,908 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.784 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.519 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.536 |
| AlphaMissense vs revel | +0.794 |
| AlphaMissense vs cadd | +0.745 |
| AlphaMissense vs sift | -0.718 |
| AlphaMissense vs polyphen | +0.772 |
| AlphaMissense vs metarnn | +0.848 |
| AlphaMissense vs vest4 | +0.848 |
| AlphaMissense vs primateai | +0.710 |
| AlphaMissense vs mutassessor | +0.514 |
| AlphaMissense vs provean | -0.755 |
| AlphaMissense vs esm1b | -0.809 |
| AlphaMissense vs am_dbnsfp | +0.970 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.410 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.457 |
| ESM-1v vs revel | -0.702 |
| ESM-1v vs cadd | -0.640 |
| ESM-1v vs sift | +0.720 |
| ESM-1v vs polyphen | -0.686 |
| ESM-1v vs metarnn | -0.784 |
| ESM-1v vs vest4 | -0.747 |
| ESM-1v vs primateai | -0.621 |
| ESM-1v vs mutassessor | -0.459 |
| ESM-1v vs provean | +0.747 |
| ESM-1v vs esm1b | +0.840 |
| ESM-1v vs am_dbnsfp | -0.743 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.651 |
| FoldX ΔΔG (ProtVar) vs revel | +0.458 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.356 |
| FoldX ΔΔG (ProtVar) vs sift | -0.453 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.510 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.502 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.457 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.224 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.458 |
| FoldX ΔΔG (ProtVar) vs provean | -0.507 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.444 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.511 |
| ThermoMPNN ΔΔG vs revel | +0.443 |
| ThermoMPNN ΔΔG vs cadd | +0.386 |
| ThermoMPNN ΔΔG vs sift | -0.420 |
| ThermoMPNN ΔΔG vs polyphen | +0.449 |
| ThermoMPNN ΔΔG vs metarnn | +0.501 |
| ThermoMPNN ΔΔG vs vest4 | +0.466 |
| ThermoMPNN ΔΔG vs primateai | +0.278 |
| ThermoMPNN ΔΔG vs mutassessor | +0.346 |
| ThermoMPNN ΔΔG vs provean | -0.448 |
| ThermoMPNN ΔΔG vs esm1b | -0.494 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.508 |
| revel vs cadd | +0.770 |
| revel vs sift | -0.738 |
| revel vs polyphen | +0.798 |
| revel vs metarnn | +0.888 |
| revel vs vest4 | +0.821 |
| revel vs primateai | +0.675 |
| revel vs mutassessor | +0.595 |
| revel vs provean | -0.761 |
| revel vs esm1b | -0.741 |
| revel vs am_dbnsfp | +0.804 |
| cadd vs sift | -0.731 |
| cadd vs polyphen | +0.752 |
| cadd vs metarnn | +0.798 |
| cadd vs vest4 | +0.776 |
| cadd vs primateai | +0.654 |
| cadd vs mutassessor | +0.521 |
| cadd vs provean | -0.726 |
| cadd vs esm1b | -0.711 |
| cadd vs am_dbnsfp | +0.744 |
| sift vs polyphen | -0.773 |
| sift vs metarnn | -0.781 |
| sift vs vest4 | -0.717 |
| sift vs primateai | -0.518 |
| sift vs mutassessor | -0.571 |
| sift vs provean | +0.777 |
| sift vs esm1b | +0.742 |
| sift vs am_dbnsfp | -0.728 |
| polyphen vs metarnn | +0.835 |
| polyphen vs vest4 | +0.769 |
| polyphen vs primateai | +0.533 |
| polyphen vs mutassessor | +0.686 |
| polyphen vs provean | -0.736 |
| polyphen vs esm1b | -0.712 |
| polyphen vs am_dbnsfp | +0.783 |
| metarnn vs vest4 | +0.899 |
| metarnn vs primateai | +0.712 |
| metarnn vs mutassessor | +0.613 |
| metarnn vs provean | -0.817 |
| metarnn vs esm1b | -0.812 |
| metarnn vs am_dbnsfp | +0.858 |
| vest4 vs primateai | +0.740 |
| vest4 vs mutassessor | +0.547 |
| vest4 vs provean | -0.778 |
| vest4 vs esm1b | -0.803 |
| vest4 vs am_dbnsfp | +0.854 |
| primateai vs mutassessor | +0.279 |
| primateai vs provean | -0.550 |
| primateai vs esm1b | -0.661 |
| primateai vs am_dbnsfp | +0.717 |
| mutassessor vs provean | -0.577 |
| mutassessor vs esm1b | -0.523 |
| mutassessor vs am_dbnsfp | +0.550 |
| provean vs esm1b | +0.782 |
| provean vs am_dbnsfp | -0.761 |
| esm1b vs am_dbnsfp | -0.816 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| likely_pathogenic | 3 |

**gnomAD r4 missense variants mapped:** 1,530

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 5,580** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,608 | 2,972 |
| mean AlphaMissense | 0.226 | 0.812 |
| mean ESM-1v | 4.511 | 9.416 |
| mean FoldX ΔΔG | 0.657 | 3.317 |
| mean ThermoMPNN ΔΔG | 0.438 | 1.201 |
| mean REVEL | 0.247 | 0.686 |
| mean CADD phred | 16.428 | 27.924 |
| mean SIFT | -0.278 | -0.016 |
| mean PolyPhen-2 HVAR | 0.129 | 0.792 |
| mean MetaRNN | 0.324 | 0.871 |
| mean VEST4 | 0.362 | 0.811 |
| mean PrimateAI | 0.486 | 0.721 |
| mean PROVEAN | 1.467 | 5.235 |
| **fraction seen in gnomAD** | **23.35%** (609) | **14.74%** (438) |

**Validation:** the damaging cluster is **depleted** in the population — 14.74% of it appears in gnomAD against 23.35% of the tolerant cluster (a 1.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 18,582**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 9,665 | 8,917 |
| mean AlphaMissense | 0.4 | 0.944 |
| mean ESM-1v | 5.44 | 11.268 |
| mean FoldX ΔΔG | 0.658 | 4.323 |
| mean ThermoMPNN ΔΔG | 0.452 | 1.513 |
| **fraction seen in gnomAD** | **8.84%** (854) | **3.20%** (285) |

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
