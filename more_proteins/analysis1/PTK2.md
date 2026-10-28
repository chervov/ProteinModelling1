# PTK2 — variant-effect analysis

*Focal adhesion kinase 1* · UniProt `Q05397` · 1052 aa · **reference**

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| FERM | 35–355 | 321 |
| Protein kinase | 422–680 | 259 |
| Focal AT | 914–1045 | 132 |

**Pair analysed:** FERM ↔ Protein kinase

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 44.4 | 43 | 100% / 100% |
| 2J0J (X-ray, autoinhibited FERM-kinase) | 45.0 | 42 | 100% / 96% |

## 2. The inter-domain interface

Most compact structure: `Q05397.pdb`, centroid distance **44.4 Å**, **43 residue pairs** in contact within 5 Å.

**Domain A interface residues (19):** `44, 45, 46, 180, 182, 183, 184, 186, 187, 188, 190, 192, 193, 196, 197, 200, 201, 205, 236`

**Domain B interface residues (21):** `575, 576, 578, 579, 580, 581, 592, 594, 595, 596, 597, 598, 629, 630, 632, 633, 636, 637, 661, 662, 663`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 760 | 19,228 | 0.964 | 0.777 | 1.2e-41 |
| ESM-1v | 760 | 19,228 | -14.082 | -12.338 | 3.3e-42 |
| FoldX ΔΔG | 665 | 14,326 | 1.256 | 1.001 | 0.0092 |
| ThermoMPNN ΔΔG | 760 | 19,228 | 0.633 | 0.378 | 1.3e-12 |
| REVEL | 240 | 5,881 | 0.603 | 0.407 | 2.1e-15 |
| CADD phred | 254 | 6,291 | 26.65 | 25.0 | 0.00012 |
| SIFT | 240 | 5,949 | 0.002 | 0.021 | 2.3e-13 |
| PolyPhen-2 HVAR | 240 | 5,874 | 0.954 | 0.806 | 3e-06 |
| MetaRNN | 240 | 5,949 | 0.762 | 0.601 | 3e-08 |
| VEST4 | 254 | 6,292 | 0.727 | 0.669 | 0.00021 |
| PrimateAI | 240 | 5,870 | 0.801 | 0.754 | 3.6e-12 |
| MutationAssessor | 240 | 5,859 | 1.39 | 1.845 | 0.00017 |
| PROVEAN | 240 | 5,949 | -3.725 | -2.43 | 1.6e-14 |
| ESM1b | 240 | 5,870 | -11.685 | -10.157 | 1e-07 |
| AlphaMissense (dbNSFP) | 240 | 5,949 | 0.893 | 0.468 | 4.7e-19 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 19,988 |
| ESM-1v | 19,988 |
| FoldX ΔΔG (ProtVar) | 14,991 |
| ThermoMPNN ΔΔG | 19,988 |
| revel | 6,121 |
| cadd | 6,545 |
| sift | 6,189 |
| polyphen | 6,114 |
| metarnn | 6,189 |
| vest4 | 6,546 |
| primateai | 6,110 |
| mutassessor | 6,099 |
| provean | 6,189 |
| esm1b | 6,110 |
| am_dbnsfp | 6,189 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.750 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.447 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.521 |
| AlphaMissense vs revel | +0.719 |
| AlphaMissense vs cadd | +0.687 |
| AlphaMissense vs sift | -0.673 |
| AlphaMissense vs polyphen | +0.645 |
| AlphaMissense vs metarnn | +0.798 |
| AlphaMissense vs vest4 | +0.662 |
| AlphaMissense vs primateai | +0.690 |
| AlphaMissense vs mutassessor | +0.557 |
| AlphaMissense vs provean | -0.730 |
| AlphaMissense vs esm1b | -0.755 |
| AlphaMissense vs am_dbnsfp | +0.986 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.342 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.441 |
| ESM-1v vs revel | -0.674 |
| ESM-1v vs cadd | -0.576 |
| ESM-1v vs sift | +0.533 |
| ESM-1v vs polyphen | -0.551 |
| ESM-1v vs metarnn | -0.661 |
| ESM-1v vs vest4 | -0.627 |
| ESM-1v vs primateai | -0.611 |
| ESM-1v vs mutassessor | -0.432 |
| ESM-1v vs provean | +0.614 |
| ESM-1v vs esm1b | +0.681 |
| ESM-1v vs am_dbnsfp | -0.723 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.715 |
| FoldX ΔΔG (ProtVar) vs revel | +0.396 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.276 |
| FoldX ΔΔG (ProtVar) vs sift | -0.367 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.297 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.412 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.331 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.249 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.347 |
| FoldX ΔΔG (ProtVar) vs provean | -0.407 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.335 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.424 |
| ThermoMPNN ΔΔG vs revel | +0.455 |
| ThermoMPNN ΔΔG vs cadd | +0.350 |
| ThermoMPNN ΔΔG vs sift | -0.430 |
| ThermoMPNN ΔΔG vs polyphen | +0.368 |
| ThermoMPNN ΔΔG vs metarnn | +0.510 |
| ThermoMPNN ΔΔG vs vest4 | +0.405 |
| ThermoMPNN ΔΔG vs primateai | +0.359 |
| ThermoMPNN ΔΔG vs mutassessor | +0.363 |
| ThermoMPNN ΔΔG vs provean | -0.475 |
| ThermoMPNN ΔΔG vs esm1b | -0.484 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.514 |
| revel vs cadd | +0.644 |
| revel vs sift | -0.672 |
| revel vs polyphen | +0.595 |
| revel vs metarnn | +0.856 |
| revel vs vest4 | +0.694 |
| revel vs primateai | +0.560 |
| revel vs mutassessor | +0.524 |
| revel vs provean | -0.714 |
| revel vs esm1b | -0.595 |
| revel vs am_dbnsfp | +0.723 |
| cadd vs sift | -0.646 |
| cadd vs polyphen | +0.673 |
| cadd vs metarnn | +0.717 |
| cadd vs vest4 | +0.661 |
| cadd vs primateai | +0.515 |
| cadd vs mutassessor | +0.580 |
| cadd vs provean | -0.666 |
| cadd vs esm1b | -0.596 |
| cadd vs am_dbnsfp | +0.675 |
| sift vs polyphen | -0.560 |
| sift vs metarnn | -0.714 |
| sift vs vest4 | -0.503 |
| sift vs primateai | -0.436 |
| sift vs mutassessor | -0.580 |
| sift vs provean | +0.735 |
| sift vs esm1b | +0.593 |
| sift vs am_dbnsfp | -0.668 |
| polyphen vs metarnn | +0.690 |
| polyphen vs vest4 | +0.600 |
| polyphen vs primateai | +0.572 |
| polyphen vs mutassessor | +0.538 |
| polyphen vs provean | -0.554 |
| polyphen vs esm1b | -0.534 |
| polyphen vs am_dbnsfp | +0.640 |
| metarnn vs vest4 | +0.732 |
| metarnn vs primateai | +0.666 |
| metarnn vs mutassessor | +0.581 |
| metarnn vs provean | -0.796 |
| metarnn vs esm1b | -0.720 |
| metarnn vs am_dbnsfp | +0.810 |
| vest4 vs primateai | +0.544 |
| vest4 vs mutassessor | +0.476 |
| vest4 vs provean | -0.587 |
| vest4 vs esm1b | -0.540 |
| vest4 vs am_dbnsfp | +0.674 |
| primateai vs mutassessor | +0.350 |
| primateai vs provean | -0.535 |
| primateai vs esm1b | -0.569 |
| primateai vs am_dbnsfp | +0.688 |
| mutassessor vs provean | -0.578 |
| mutassessor vs esm1b | -0.449 |
| mutassessor vs am_dbnsfp | +0.553 |
| provean vs esm1b | +0.721 |
| provean vs am_dbnsfp | -0.745 |
| esm1b vs am_dbnsfp | -0.753 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 22 |
| likely_benign | 2 |

**gnomAD r4 missense variants mapped:** 1,215

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,556** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,896 | 2,660 |
| mean AlphaMissense | 0.303 | 0.846 |
| mean ESM-1v | 8.43 | 12.726 |
| mean FoldX ΔΔG | 0.53 | 2.422 |
| mean ThermoMPNN ΔΔG | 0.361 | 1.171 |
| mean REVEL | 0.274 | 0.639 |
| mean CADD phred | 20.826 | 27.84 |
| mean SIFT | -0.251 | -0.026 |
| mean PolyPhen-2 HVAR | 0.404 | 0.876 |
| mean MetaRNN | 0.422 | 0.826 |
| mean VEST4 | 0.494 | 0.779 |
| mean PrimateAI | 0.691 | 0.806 |
| mean PROVEAN | 1.614 | 4.8 |
| **fraction seen in gnomAD** | **20.20%** (383) | **12.67%** (337) |
| fraction at the interface | 3.38% | 5.49% |

**Validation:** the damaging cluster is **depleted** in the population — 12.67% of it appears in gnomAD against 20.20% of the tolerant cluster (a 1.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 14,991**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,095 | 6,896 |
| mean AlphaMissense | 0.544 | 0.959 |
| mean ESM-1v | 10.416 | 15.516 |
| mean FoldX ΔΔG | 0.47 | 3.701 |
| mean ThermoMPNN ΔΔG | 0.331 | 1.625 |
| **fraction seen in gnomAD** | **7.67%** (621) | **2.65%** (183) |

Depletion **2.9×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.68% | 5.32% |

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
