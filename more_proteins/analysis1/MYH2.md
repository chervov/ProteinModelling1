# MYH2 — variant-effect analysis

*Myosin-2* · UniProt `Q9UKX2` · 1941 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Myosin N-terminal SH3-like | 33–82 | 50 |
| Myosin motor | 86–784 | 699 |
| IQ | 787–816 | 30 |

**Pair analysed:** Myosin motor ↔ IQ

**AlphaFold PAE:** inter-module mean **14.93 Å**, intra-module **6.33 Å**, **ratio 2.36**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 50.6 | 6 | 100% / 100% |
| 8q6t.1.A (81.3% id) | 59.6 | 5 | 100% / 100% |
| 3dtp.1.A (52.6% id) | 63.1 | 4 | 100% / 100% |
| 5tby.1.B (81.2% id) | 51.7 | 16 | 100% / 100% |
| 9tpl.1.A (81.2% id) | 47.8 | 6 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `MYH2_Q9UKX2_SWISSMODEL_2w4g-1-C_4-847.pdb`, centroid distance **69.2 Å**, **25 residue pairs** in contact within 5 Å.

**Domain A interface residues (13):** `727, 730, 731, 732, 733, 734, 735, 755, 756, 779, 780, 781, 784`

**Domain B interface residues (9):** `787, 788, 790, 791, 793, 794, 795, 797, 798`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 418 | 36,461 | 0.881 | 0.808 | 0.00042 |
| ESM-1v | 418 | 36,461 | -11.342 | -11.44 | 0.92 |
| FoldX ΔΔG | 418 | 34,675 | 0.524 | 0.453 | 0.16 |
| ThermoMPNN ΔΔG | 418 | 36,461 | 0.344 | 0.262 | 0.094 |
| REVEL | 97 | 8,314 | 0.65 | 0.691 | 0.43 |
| CADD phred | 102 | 8,841 | 24.8 | 24.8 | 0.51 |
| SIFT | 97 | 8,314 | 0.002 | 0.001 | 0.0093 |
| PolyPhen-2 HVAR | 97 | 8,314 | 0.81 | 0.819 | 0.32 |
| MetaRNN | 97 | 8,314 | 0.829 | 0.813 | 0.76 |
| VEST4 | 102 | 8,841 | 0.744 | 0.709 | 0.074 |
| PrimateAI | 97 | 8,308 | 0.768 | 0.754 | 0.86 |
| MutationAssessor | 97 | 8,308 | 2.58 | 2.955 | 0.021 |
| PROVEAN | 97 | 8,314 | -3.28 | -3.24 | 0.61 |
| ESM1b | 97 | 8,314 | -12.072 | -12.242 | 0.33 |
| AlphaMissense (dbNSFP) | 97 | 8,308 | 0.669 | 0.578 | 0.23 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 36,879 |
| ESM-1v | 36,879 |
| FoldX ΔΔG (ProtVar) | 35,093 |
| ThermoMPNN ΔΔG | 36,879 |
| revel | 8,411 |
| cadd | 8,943 |
| sift | 8,411 |
| polyphen | 8,411 |
| metarnn | 8,411 |
| vest4 | 8,943 |
| primateai | 8,405 |
| mutassessor | 8,405 |
| provean | 8,411 |
| esm1b | 8,411 |
| am_dbnsfp | 8,405 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.783 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.335 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.374 |
| AlphaMissense vs revel | +0.715 |
| AlphaMissense vs cadd | +0.613 |
| AlphaMissense vs sift | -0.628 |
| AlphaMissense vs polyphen | +0.535 |
| AlphaMissense vs metarnn | +0.743 |
| AlphaMissense vs vest4 | +0.705 |
| AlphaMissense vs primateai | +0.595 |
| AlphaMissense vs mutassessor | +0.521 |
| AlphaMissense vs provean | -0.633 |
| AlphaMissense vs esm1b | -0.659 |
| AlphaMissense vs am_dbnsfp | +0.994 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.323 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.374 |
| ESM-1v vs revel | -0.709 |
| ESM-1v vs cadd | -0.626 |
| ESM-1v vs sift | +0.595 |
| ESM-1v vs polyphen | -0.515 |
| ESM-1v vs metarnn | -0.735 |
| ESM-1v vs vest4 | -0.668 |
| ESM-1v vs primateai | -0.397 |
| ESM-1v vs mutassessor | -0.542 |
| ESM-1v vs provean | +0.602 |
| ESM-1v vs esm1b | +0.695 |
| ESM-1v vs am_dbnsfp | -0.758 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.635 |
| FoldX ΔΔG (ProtVar) vs revel | +0.293 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.174 |
| FoldX ΔΔG (ProtVar) vs sift | -0.200 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.169 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.312 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.271 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.138 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.152 |
| FoldX ΔΔG (ProtVar) vs provean | -0.259 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.198 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.351 |
| ThermoMPNN ΔΔG vs revel | +0.335 |
| ThermoMPNN ΔΔG vs cadd | +0.236 |
| ThermoMPNN ΔΔG vs sift | -0.267 |
| ThermoMPNN ΔΔG vs polyphen | +0.184 |
| ThermoMPNN ΔΔG vs metarnn | +0.357 |
| ThermoMPNN ΔΔG vs vest4 | +0.307 |
| ThermoMPNN ΔΔG vs primateai | +0.169 |
| ThermoMPNN ΔΔG vs mutassessor | +0.169 |
| ThermoMPNN ΔΔG vs provean | -0.289 |
| ThermoMPNN ΔΔG vs esm1b | -0.250 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.429 |
| revel vs cadd | +0.711 |
| revel vs sift | -0.673 |
| revel vs polyphen | +0.646 |
| revel vs metarnn | +0.879 |
| revel vs vest4 | +0.796 |
| revel vs primateai | +0.542 |
| revel vs mutassessor | +0.628 |
| revel vs provean | -0.719 |
| revel vs esm1b | -0.659 |
| revel vs am_dbnsfp | +0.718 |
| cadd vs sift | -0.645 |
| cadd vs polyphen | +0.627 |
| cadd vs metarnn | +0.694 |
| cadd vs vest4 | +0.660 |
| cadd vs primateai | +0.448 |
| cadd vs mutassessor | +0.603 |
| cadd vs provean | -0.565 |
| cadd vs esm1b | -0.540 |
| cadd vs am_dbnsfp | +0.615 |
| sift vs polyphen | -0.553 |
| sift vs metarnn | -0.668 |
| sift vs vest4 | -0.594 |
| sift vs primateai | -0.413 |
| sift vs mutassessor | -0.540 |
| sift vs provean | +0.625 |
| sift vs esm1b | +0.553 |
| sift vs am_dbnsfp | -0.631 |
| polyphen vs metarnn | +0.664 |
| polyphen vs vest4 | +0.581 |
| polyphen vs primateai | +0.420 |
| polyphen vs mutassessor | +0.538 |
| polyphen vs provean | -0.487 |
| polyphen vs esm1b | -0.466 |
| polyphen vs am_dbnsfp | +0.538 |
| metarnn vs vest4 | +0.897 |
| metarnn vs primateai | +0.538 |
| metarnn vs mutassessor | +0.654 |
| metarnn vs provean | -0.685 |
| metarnn vs esm1b | -0.632 |
| metarnn vs am_dbnsfp | +0.748 |
| vest4 vs primateai | +0.584 |
| vest4 vs mutassessor | +0.618 |
| vest4 vs provean | -0.640 |
| vest4 vs esm1b | -0.587 |
| vest4 vs am_dbnsfp | +0.709 |
| primateai vs mutassessor | +0.317 |
| primateai vs provean | -0.452 |
| primateai vs esm1b | -0.385 |
| primateai vs am_dbnsfp | +0.597 |
| mutassessor vs provean | -0.499 |
| mutassessor vs esm1b | -0.569 |
| mutassessor vs am_dbnsfp | +0.519 |
| provean vs esm1b | +0.609 |
| provean vs am_dbnsfp | -0.633 |
| esm1b vs am_dbnsfp | -0.658 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 624 |
| conflict | 19 |
| likely_benign | 10 |
| pathogenic | 3 |
| likely_pathogenic | 3 |

**gnomAD r4 missense variants mapped:** 2,062

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 8,029** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,535 | 5,494 |
| mean AlphaMissense | 0.231 | 0.729 |
| mean ESM-1v | 6.57 | 11.274 |
| mean FoldX ΔΔG | 0.373 | 1.368 |
| mean ThermoMPNN ΔΔG | 0.215 | 0.623 |
| mean REVEL | 0.381 | 0.758 |
| mean CADD phred | 16.49 | 26.023 |
| mean SIFT | -0.146 | -0.005 |
| mean PolyPhen-2 HVAR | 0.245 | 0.814 |
| mean MetaRNN | 0.357 | 0.849 |
| mean VEST4 | 0.386 | 0.767 |
| mean PrimateAI | 0.625 | 0.778 |
| mean PROVEAN | 1.778 | 4.169 |
| **fraction seen in gnomAD** | **20.47%** (519) | **16.64%** (914) |
| fraction at the interface | 1.14% | 1.24% |

**Validation:** the damaging cluster is **depleted** in the population — 16.64% of it appears in gnomAD against 20.47% of the tolerant cluster (a 1.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 35,093**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 18,764 | 16,329 |
| mean AlphaMissense | 0.486 | 0.932 |
| mean ESM-1v | 8.674 | 14.522 |
| mean FoldX ΔΔG | 0.239 | 2.227 |
| mean ThermoMPNN ΔΔG | 0.157 | 0.948 |
| **fraction seen in gnomAD** | **7.65%** (1,436) | **3.15%** (515) |

Depletion **2.4×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 1.03% | 1.37% |

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
