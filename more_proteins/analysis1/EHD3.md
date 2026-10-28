# EHD3 — variant-effect analysis

*EH domain-containing protein 3* · UniProt `Q9NZN3` · 535 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Dynamin-type G | 55–286 | 232 |
| EH | 444–532 | 89 |
| EF-hand | 476–511 | 36 |

**Pair analysed:** Dynamin-type G ↔ EH

**AlphaFold PAE:** inter-module mean **22.35 Å**, intra-module **3.4 Å**, **ratio 6.58**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 48.3 | 0 | 100% / 100% |
| 2qpt.1.B (71.3% id) | 52.3 | 0 | 100% / 100% |
| 7sox.1.A (76.8% id) | 35.4 | 21 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q9NZN3_7sox-1-A.pdb`, centroid distance **35.4 Å**, **21 residue pairs** in contact within 5 Å.

**Domain A interface residues (14):** `76, 77, 80, 82, 83, 86, 87, 88, 258, 259, 260, 261, 262, 268`

**Domain B interface residues (8):** `490, 492, 519, 520, 521, 522, 523, 532`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 418 | 9,747 | 0.78 | 0.912 | 2.5e-15 |
| ESM-1v | 418 | 9,747 | -10.617 | -11.268 | 7.4e-06 |
| FoldX ΔΔG | 418 | 9,424 | 0.693 | 1.161 | 2.1e-06 |
| ThermoMPNN ΔΔG | 418 | 9,747 | 0.704 | 0.733 | 0.034 |
| REVEL | 134 | 3,059 | 0.516 | 0.554 | 0.2 |
| CADD phred | 140 | 3,191 | 24.7 | 24.8 | 0.67 |
| SIFT | 134 | 3,059 | 0.018 | 0.011 | 0.33 |
| PolyPhen-2 HVAR | 134 | 3,059 | 0.52 | 0.688 | 0.49 |
| MetaRNN | 134 | 3,059 | 0.782 | 0.798 | 0.066 |
| VEST4 | 140 | 3,191 | 0.74 | 0.768 | 0.0055 |
| PrimateAI | 134 | 3,053 | 0.834 | 0.824 | 0.29 |
| MutationAssessor | 134 | 3,053 | 1.968 | 2.48 | 0.00018 |
| PROVEAN | 134 | 3,059 | -3.635 | -3.71 | 0.96 |
| ESM1b | 134 | 3,059 | -10.667 | -10.803 | 0.063 |
| AlphaMissense (dbNSFP) | 134 | 3,053 | 0.568 | 0.723 | 1.4e-06 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 10,165 |
| ESM-1v | 10,165 |
| FoldX ΔΔG (ProtVar) | 9,842 |
| ThermoMPNN ΔΔG | 10,165 |
| revel | 3,193 |
| cadd | 3,331 |
| sift | 3,193 |
| polyphen | 3,193 |
| metarnn | 3,193 |
| vest4 | 3,331 |
| primateai | 3,187 |
| mutassessor | 3,187 |
| provean | 3,193 |
| esm1b | 3,193 |
| am_dbnsfp | 3,187 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.851 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.469 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.519 |
| AlphaMissense vs revel | +0.744 |
| AlphaMissense vs cadd | +0.748 |
| AlphaMissense vs sift | -0.762 |
| AlphaMissense vs polyphen | +0.742 |
| AlphaMissense vs metarnn | +0.825 |
| AlphaMissense vs vest4 | +0.773 |
| AlphaMissense vs primateai | +0.593 |
| AlphaMissense vs mutassessor | +0.722 |
| AlphaMissense vs provean | -0.738 |
| AlphaMissense vs esm1b | -0.773 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.410 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.481 |
| ESM-1v vs revel | -0.759 |
| ESM-1v vs cadd | -0.786 |
| ESM-1v vs sift | +0.808 |
| ESM-1v vs polyphen | -0.754 |
| ESM-1v vs metarnn | -0.839 |
| ESM-1v vs vest4 | -0.796 |
| ESM-1v vs primateai | -0.558 |
| ESM-1v vs mutassessor | -0.743 |
| ESM-1v vs provean | +0.769 |
| ESM-1v vs esm1b | +0.900 |
| ESM-1v vs am_dbnsfp | -0.838 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.730 |
| FoldX ΔΔG (ProtVar) vs revel | +0.358 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.396 |
| FoldX ΔΔG (ProtVar) vs sift | -0.418 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.369 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.433 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.429 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.235 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.423 |
| FoldX ΔΔG (ProtVar) vs provean | -0.410 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.387 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.468 |
| ThermoMPNN ΔΔG vs revel | +0.432 |
| ThermoMPNN ΔΔG vs cadd | +0.448 |
| ThermoMPNN ΔΔG vs sift | -0.487 |
| ThermoMPNN ΔΔG vs polyphen | +0.435 |
| ThermoMPNN ΔΔG vs metarnn | +0.496 |
| ThermoMPNN ΔΔG vs vest4 | +0.509 |
| ThermoMPNN ΔΔG vs primateai | +0.306 |
| ThermoMPNN ΔΔG vs mutassessor | +0.512 |
| ThermoMPNN ΔΔG vs provean | -0.454 |
| ThermoMPNN ΔΔG vs esm1b | -0.472 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.530 |
| revel vs cadd | +0.717 |
| revel vs sift | -0.710 |
| revel vs polyphen | +0.702 |
| revel vs metarnn | +0.893 |
| revel vs vest4 | +0.755 |
| revel vs primateai | +0.683 |
| revel vs mutassessor | +0.555 |
| revel vs provean | -0.637 |
| revel vs esm1b | -0.686 |
| revel vs am_dbnsfp | +0.744 |
| cadd vs sift | -0.811 |
| cadd vs polyphen | +0.813 |
| cadd vs metarnn | +0.814 |
| cadd vs vest4 | +0.699 |
| cadd vs primateai | +0.506 |
| cadd vs mutassessor | +0.712 |
| cadd vs provean | -0.701 |
| cadd vs esm1b | -0.734 |
| cadd vs am_dbnsfp | +0.748 |
| sift vs polyphen | -0.770 |
| sift vs metarnn | -0.796 |
| sift vs vest4 | -0.710 |
| sift vs primateai | -0.465 |
| sift vs mutassessor | -0.765 |
| sift vs provean | +0.735 |
| sift vs esm1b | +0.756 |
| sift vs am_dbnsfp | -0.763 |
| polyphen vs metarnn | +0.816 |
| polyphen vs vest4 | +0.676 |
| polyphen vs primateai | +0.510 |
| polyphen vs mutassessor | +0.721 |
| polyphen vs provean | -0.712 |
| polyphen vs esm1b | -0.712 |
| polyphen vs am_dbnsfp | +0.743 |
| metarnn vs vest4 | +0.881 |
| metarnn vs primateai | +0.642 |
| metarnn vs mutassessor | +0.704 |
| metarnn vs provean | -0.747 |
| metarnn vs esm1b | -0.765 |
| metarnn vs am_dbnsfp | +0.828 |
| vest4 vs primateai | +0.619 |
| vest4 vs mutassessor | +0.669 |
| vest4 vs provean | -0.691 |
| vest4 vs esm1b | -0.721 |
| vest4 vs am_dbnsfp | +0.774 |
| primateai vs mutassessor | +0.398 |
| primateai vs provean | -0.419 |
| primateai vs esm1b | -0.525 |
| primateai vs am_dbnsfp | +0.593 |
| mutassessor vs provean | -0.691 |
| mutassessor vs esm1b | -0.692 |
| mutassessor vs am_dbnsfp | +0.722 |
| provean vs esm1b | +0.700 |
| provean vs am_dbnsfp | -0.738 |
| esm1b vs am_dbnsfp | -0.774 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 20 |

**gnomAD r4 missense variants mapped:** 630

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,091** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,168 | 1,923 |
| mean AlphaMissense | 0.273 | 0.844 |
| mean ESM-1v | 6.314 | 11.57 |
| mean FoldX ΔΔG | 0.511 | 2.308 |
| mean ThermoMPNN ΔΔG | 0.385 | 1.225 |
| mean REVEL | 0.265 | 0.741 |
| mean CADD phred | 18.207 | 27.481 |
| mean SIFT | -0.251 | -0.013 |
| mean PolyPhen-2 HVAR | 0.139 | 0.826 |
| mean MetaRNN | 0.355 | 0.867 |
| mean VEST4 | 0.492 | 0.837 |
| mean PrimateAI | 0.698 | 0.841 |
| mean PROVEAN | 1.834 | 5.314 |
| **fraction seen in gnomAD** | **24.49%** (286) | **16.85%** (324) |
| fraction at the interface | 4.97% | 3.95% |

**Validation:** the damaging cluster is **depleted** in the population — 16.85% of it appears in gnomAD against 24.49% of the tolerant cluster (a 1.5-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 9,842**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,112 | 5,730 |
| mean AlphaMissense | 0.429 | 0.954 |
| mean ESM-1v | 7.85 | 13.736 |
| mean FoldX ΔΔG | 0.421 | 3.217 |
| mean ThermoMPNN ΔΔG | 0.349 | 1.467 |
| **fraction seen in gnomAD** | **9.63%** (396) | **3.73%** (214) |

Depletion **2.6×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 5.23% | 3.54% |

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
