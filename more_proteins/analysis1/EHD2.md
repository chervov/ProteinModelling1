# EHD2 — variant-effect analysis

*EH domain-containing protein 2* · UniProt `Q9NZN4` · 543 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 55–286 | 232 |
| EH | 449–537 | 89 |
| EF-hand | 481–516 | 36 |

**Pair analysed:** Dynamin-type G ↔ EH

**AlphaFold PAE:** inter-module mean **16.84 Å**, intra-module **3.53 Å**, **ratio 4.78**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 52.1 | 0 | 100% / 100% |
| SWISSMODEL_4cid-1-B_6-539 | 52.5 | 0 | 100% / 100% |
| SWISSMODEL_9rbu-1-A_1-536 | 35.7 | 21 | 100% / 99% |

## 2. The inter-domain interface

Most compact structure: `EHD2_Q9NZN4_SWISSMODEL_9rbu-1-A_1-536.pdb`, centroid distance **35.7 Å**, **21 residue pairs** in contact within 5 Å.

**Domain A interface residues (10):** `80, 258, 259, 260, 261, 262, 263, 265, 268, 272`

**Domain B interface residues (9):** `477, 480, 481, 482, 483, 484, 485, 488, 516`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 361 | 9,956 | 0.751 | 0.846 | 0.029 |
| ESM-1v | 361 | 9,956 | -9.586 | -9.783 | 0.9 |
| FoldX ΔΔG | 361 | 9,272 | 0.488 | 1.148 | 5.1e-19 |
| ThermoMPNN ΔΔG | 361 | 9,956 | 0.275 | 0.682 | 1.4e-20 |
| REVEL | 109 | 3,101 | 0.307 | 0.454 | 0.00035 |
| CADD phred | 116 | 3,231 | 24.35 | 24.4 | 0.97 |
| SIFT | 109 | 3,101 | 0.009 | 0.011 | 0.9 |
| PolyPhen-2 HVAR | 109 | 3,101 | 0.535 | 0.53 | 0.91 |
| MetaRNN | 109 | 3,101 | 0.736 | 0.721 | 0.34 |
| VEST4 | 116 | 3,231 | 0.716 | 0.709 | 0.47 |
| PrimateAI | 109 | 3,095 | 0.724 | 0.759 | 0.0027 |
| MutationAssessor | 109 | 3,091 | 2.08 | 2.185 | 0.75 |
| PROVEAN | 109 | 3,101 | -3.85 | -3.56 | 0.051 |
| ESM1b | 109 | 3,101 | -10.104 | -10.027 | 0.45 |
| AlphaMissense (dbNSFP) | 109 | 3,095 | 0.556 | 0.622 | 0.34 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 10,317 |
| ESM-1v | 10,317 |
| FoldX ΔΔG (ProtVar) | 9,633 |
| ThermoMPNN ΔΔG | 10,317 |
| revel | 3,210 |
| cadd | 3,347 |
| sift | 3,210 |
| polyphen | 3,210 |
| metarnn | 3,210 |
| vest4 | 3,347 |
| primateai | 3,204 |
| mutassessor | 3,200 |
| provean | 3,210 |
| esm1b | 3,210 |
| am_dbnsfp | 3,204 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.849 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.516 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.584 |
| AlphaMissense vs revel | +0.692 |
| AlphaMissense vs cadd | +0.750 |
| AlphaMissense vs sift | -0.751 |
| AlphaMissense vs polyphen | +0.779 |
| AlphaMissense vs metarnn | +0.810 |
| AlphaMissense vs vest4 | +0.811 |
| AlphaMissense vs primateai | +0.662 |
| AlphaMissense vs mutassessor | +0.756 |
| AlphaMissense vs provean | -0.727 |
| AlphaMissense vs esm1b | -0.786 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.442 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.526 |
| ESM-1v vs revel | -0.769 |
| ESM-1v vs cadd | -0.792 |
| ESM-1v vs sift | +0.810 |
| ESM-1v vs polyphen | -0.799 |
| ESM-1v vs metarnn | -0.847 |
| ESM-1v vs vest4 | -0.810 |
| ESM-1v vs primateai | -0.613 |
| ESM-1v vs mutassessor | -0.771 |
| ESM-1v vs provean | +0.795 |
| ESM-1v vs esm1b | +0.902 |
| ESM-1v vs am_dbnsfp | -0.832 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.721 |
| FoldX ΔΔG (ProtVar) vs revel | +0.376 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.382 |
| FoldX ΔΔG (ProtVar) vs sift | -0.412 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.407 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.440 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.440 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.298 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.434 |
| FoldX ΔΔG (ProtVar) vs provean | -0.395 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.418 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.502 |
| ThermoMPNN ΔΔG vs revel | +0.453 |
| ThermoMPNN ΔΔG vs cadd | +0.465 |
| ThermoMPNN ΔΔG vs sift | -0.505 |
| ThermoMPNN ΔΔG vs polyphen | +0.487 |
| ThermoMPNN ΔΔG vs metarnn | +0.523 |
| ThermoMPNN ΔΔG vs vest4 | +0.526 |
| ThermoMPNN ΔΔG vs primateai | +0.336 |
| ThermoMPNN ΔΔG vs mutassessor | +0.530 |
| ThermoMPNN ΔΔG vs provean | -0.461 |
| ThermoMPNN ΔΔG vs esm1b | -0.519 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.582 |
| revel vs cadd | +0.709 |
| revel vs sift | -0.711 |
| revel vs polyphen | +0.721 |
| revel vs metarnn | +0.881 |
| revel vs vest4 | +0.777 |
| revel vs primateai | +0.698 |
| revel vs mutassessor | +0.630 |
| revel vs provean | -0.668 |
| revel vs esm1b | -0.711 |
| revel vs am_dbnsfp | +0.692 |
| cadd vs sift | -0.810 |
| cadd vs polyphen | +0.845 |
| cadd vs metarnn | +0.793 |
| cadd vs vest4 | +0.729 |
| cadd vs primateai | +0.588 |
| cadd vs mutassessor | +0.721 |
| cadd vs provean | -0.703 |
| cadd vs esm1b | -0.757 |
| cadd vs am_dbnsfp | +0.750 |
| sift vs polyphen | -0.840 |
| sift vs metarnn | -0.795 |
| sift vs vest4 | -0.725 |
| sift vs primateai | -0.563 |
| sift vs mutassessor | -0.756 |
| sift vs provean | +0.744 |
| sift vs esm1b | +0.761 |
| sift vs am_dbnsfp | -0.751 |
| polyphen vs metarnn | +0.827 |
| polyphen vs vest4 | +0.758 |
| polyphen vs primateai | +0.620 |
| polyphen vs mutassessor | +0.785 |
| polyphen vs provean | -0.734 |
| polyphen vs esm1b | -0.755 |
| polyphen vs am_dbnsfp | +0.780 |
| metarnn vs vest4 | +0.923 |
| metarnn vs primateai | +0.712 |
| metarnn vs mutassessor | +0.751 |
| metarnn vs provean | -0.783 |
| metarnn vs esm1b | -0.784 |
| metarnn vs am_dbnsfp | +0.812 |
| vest4 vs primateai | +0.719 |
| vest4 vs mutassessor | +0.736 |
| vest4 vs provean | -0.741 |
| vest4 vs esm1b | -0.745 |
| vest4 vs am_dbnsfp | +0.813 |
| primateai vs mutassessor | +0.539 |
| primateai vs provean | -0.534 |
| primateai vs esm1b | -0.558 |
| primateai vs am_dbnsfp | +0.662 |
| mutassessor vs provean | -0.735 |
| mutassessor vs esm1b | -0.713 |
| mutassessor vs am_dbnsfp | +0.756 |
| provean vs esm1b | +0.731 |
| provean vs am_dbnsfp | -0.727 |
| esm1b vs am_dbnsfp | -0.787 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 21 |

**gnomAD r4 missense variants mapped:** 714

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,995** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,224 | 1,771 |
| mean AlphaMissense | 0.276 | 0.832 |
| mean ESM-1v | 5.633 | 10.652 |
| mean FoldX ΔΔG | 0.537 | 2.365 |
| mean ThermoMPNN ΔΔG | 0.373 | 1.27 |
| mean REVEL | 0.233 | 0.695 |
| mean CADD phred | 17.736 | 26.899 |
| mean SIFT | -0.229 | -0.01 |
| mean PolyPhen-2 HVAR | 0.132 | 0.809 |
| mean MetaRNN | 0.308 | 0.849 |
| mean VEST4 | 0.384 | 0.825 |
| mean PrimateAI | 0.653 | 0.801 |
| mean PROVEAN | 1.579 | 5.38 |
| **fraction seen in gnomAD** | **27.12%** (332) | **18.97%** (336) |
| fraction at the interface | 4.17% | 3.27% |

**Validation:** the damaging cluster is **depleted** in the population — 18.97% of it appears in gnomAD against 27.12% of the tolerant cluster (a 1.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 9,633**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,386 | 5,247 |
| mean AlphaMissense | 0.439 | 0.945 |
| mean ESM-1v | 7.005 | 12.614 |
| mean FoldX ΔΔG | 0.426 | 3.274 |
| mean ThermoMPNN ΔΔG | 0.315 | 1.543 |
| **fraction seen in gnomAD** | **10.03%** (440) | **4.35%** (228) |

Depletion **2.3×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 5.27% | 2.48% |

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
