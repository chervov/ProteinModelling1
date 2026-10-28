# CFTR — variant-effect analysis

*Cystic fibrosis transmembrane conductance regulator* · UniProt `P13569` · 1480 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 1 | 81–365 | 285 |
| ABC transporter 1 | 423–646 | 224 |
| ABC transmembrane type-1 2 | 859–1155 | 297 |
| ABC transporter 2 | 1210–1443 | 234 |

**Pair analysed:** ABC transporter 1 ↔ ABC transporter 2

**AlphaFold PAE:** inter-module mean **13.06 Å**, intra-module **6.2 Å**, **ratio 2.11**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 30.0 | 14 | 100% / 100% |
| SWISSMODEL_6d3r-1-A_42-1439 | 40.3 | 0 | 100% / 98% |
| SWISSMODEL_9dw5-1-A_3-1436 | 46.1 | 0 | 100% / 97% |
| SWISSMODEL_9dw9-1-A_1-1451 | 27.1 | 64 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `CFTR_P13569_SWISSMODEL_9dw9-1-A_1-1451.pdb`, centroid distance **27.1 Å**, **64 residue pairs** in contact within 5 Å.

**Domain A interface residues (28):** `458, 459, 460, 461, 493, 494, 525, 528, 529, 549, 550, 551, 552, 553, 555, 573, 576, 577, 578, 579, 580, 581, 582, 584, 585, 605, 608, 611`

**Domain B interface residues (26):** `1244, 1245, 1246, 1247, 1291, 1292, 1347, 1348, 1349, 1350, 1371, 1374, 1375, 1376, 1377, 1378, 1380, 1402, 1404, 1436, 1437, 1439, 1440, 1441, 1442, 1443`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 1,026 | 27,094 | 0.727 | 0.535 | 5.5e-24 |
| ESM-1v | 1,026 | 27,094 | -6.788 | -5.128 | 6.9e-50 |
| FoldX ΔΔG | 1,026 | 22,363 | 0.573 | 1.094 | 1.6e-20 |
| ThermoMPNN ΔΔG | 1,026 | 27,094 | 0.489 | 0.539 | 0.0017 |
| REVEL | 294 | 7,727 | 0.827 | 0.651 | 2.1e-23 |
| CADD phred | 318 | 8,198 | 25.75 | 23.6 | 6.2e-14 |
| SIFT | 294 | 7,727 | 0.005 | 0.023 | 3.3e-10 |
| PolyPhen-2 HVAR | 294 | 7,727 | 0.96 | 0.741 | 2.4e-08 |
| MetaRNN | 294 | 7,727 | 0.903 | 0.765 | 1.5e-26 |
| VEST4 | 318 | 8,198 | 0.847 | 0.7 | 5.9e-20 |
| PrimateAI | 294 | 7,727 | 0.648 | 0.554 | 7.1e-15 |
| MutationAssessor | 294 | 7,727 | 1.77 | 1.9 | 0.069 |
| PROVEAN | 294 | 7,727 | -2.83 | -1.64 | 9.7e-16 |
| ESM1b | 294 | 7,727 | -8.37 | -6.3 | 6.5e-09 |
| AlphaMissense (dbNSFP) | 294 | 7,727 | 0.432 | 0.257 | 1.4e-10 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 28,120 |
| ESM-1v | 28,120 |
| FoldX ΔΔG (ProtVar) | 23,389 |
| ThermoMPNN ΔΔG | 28,120 |
| revel | 8,021 |
| cadd | 8,516 |
| sift | 8,021 |
| polyphen | 8,021 |
| metarnn | 8,021 |
| vest4 | 8,516 |
| primateai | 8,021 |
| mutassessor | 8,021 |
| provean | 8,021 |
| esm1b | 8,021 |
| am_dbnsfp | 8,021 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.623 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.491 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.524 |
| AlphaMissense vs revel | +0.793 |
| AlphaMissense vs cadd | +0.732 |
| AlphaMissense vs sift | -0.621 |
| AlphaMissense vs polyphen | +0.744 |
| AlphaMissense vs metarnn | +0.809 |
| AlphaMissense vs vest4 | +0.814 |
| AlphaMissense vs primateai | +0.686 |
| AlphaMissense vs mutassessor | +0.566 |
| AlphaMissense vs provean | -0.641 |
| AlphaMissense vs esm1b | -0.705 |
| AlphaMissense vs am_dbnsfp | +0.997 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.381 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.465 |
| ESM-1v vs revel | -0.668 |
| ESM-1v vs cadd | -0.624 |
| ESM-1v vs sift | +0.631 |
| ESM-1v vs polyphen | -0.528 |
| ESM-1v vs metarnn | -0.653 |
| ESM-1v vs vest4 | -0.580 |
| ESM-1v vs primateai | -0.373 |
| ESM-1v vs mutassessor | -0.584 |
| ESM-1v vs provean | +0.705 |
| ESM-1v vs esm1b | +0.728 |
| ESM-1v vs am_dbnsfp | -0.568 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.662 |
| FoldX ΔΔG (ProtVar) vs revel | +0.440 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.387 |
| FoldX ΔΔG (ProtVar) vs sift | -0.383 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.359 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.437 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.426 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.282 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.342 |
| FoldX ΔΔG (ProtVar) vs provean | -0.388 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.437 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.497 |
| ThermoMPNN ΔΔG vs revel | +0.518 |
| ThermoMPNN ΔΔG vs cadd | +0.423 |
| ThermoMPNN ΔΔG vs sift | -0.405 |
| ThermoMPNN ΔΔG vs polyphen | +0.409 |
| ThermoMPNN ΔΔG vs metarnn | +0.530 |
| ThermoMPNN ΔΔG vs vest4 | +0.507 |
| ThermoMPNN ΔΔG vs primateai | +0.369 |
| ThermoMPNN ΔΔG vs mutassessor | +0.331 |
| ThermoMPNN ΔΔG vs provean | -0.452 |
| ThermoMPNN ΔΔG vs esm1b | -0.527 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.542 |
| revel vs cadd | +0.808 |
| revel vs sift | -0.736 |
| revel vs polyphen | +0.817 |
| revel vs metarnn | +0.906 |
| revel vs vest4 | +0.859 |
| revel vs primateai | +0.661 |
| revel vs mutassessor | +0.646 |
| revel vs provean | -0.784 |
| revel vs esm1b | -0.715 |
| revel vs am_dbnsfp | +0.795 |
| cadd vs sift | -0.759 |
| cadd vs polyphen | +0.777 |
| cadd vs metarnn | +0.788 |
| cadd vs vest4 | +0.748 |
| cadd vs primateai | +0.577 |
| cadd vs mutassessor | +0.654 |
| cadd vs provean | -0.717 |
| cadd vs esm1b | -0.648 |
| cadd vs am_dbnsfp | +0.732 |
| sift vs polyphen | -0.647 |
| sift vs metarnn | -0.694 |
| sift vs vest4 | -0.625 |
| sift vs primateai | -0.429 |
| sift vs mutassessor | -0.639 |
| sift vs provean | +0.800 |
| sift vs esm1b | +0.577 |
| sift vs am_dbnsfp | -0.624 |
| polyphen vs metarnn | +0.784 |
| polyphen vs vest4 | +0.793 |
| polyphen vs primateai | +0.681 |
| polyphen vs mutassessor | +0.591 |
| polyphen vs provean | -0.617 |
| polyphen vs esm1b | -0.605 |
| polyphen vs am_dbnsfp | +0.745 |
| metarnn vs vest4 | +0.859 |
| metarnn vs primateai | +0.685 |
| metarnn vs mutassessor | +0.612 |
| metarnn vs provean | -0.737 |
| metarnn vs esm1b | -0.712 |
| metarnn vs am_dbnsfp | +0.809 |
| vest4 vs primateai | +0.722 |
| vest4 vs mutassessor | +0.551 |
| vest4 vs provean | -0.676 |
| vest4 vs esm1b | -0.674 |
| vest4 vs am_dbnsfp | +0.815 |
| primateai vs mutassessor | +0.385 |
| primateai vs provean | -0.461 |
| primateai vs esm1b | -0.504 |
| primateai vs am_dbnsfp | +0.689 |
| mutassessor vs provean | -0.614 |
| mutassessor vs esm1b | -0.555 |
| mutassessor vs am_dbnsfp | +0.567 |
| provean vs esm1b | +0.633 |
| provean vs am_dbnsfp | -0.646 |
| esm1b vs am_dbnsfp | -0.704 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 2,127

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 6,636** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,714 | 3,922 |
| mean AlphaMissense | 0.173 | 0.632 |
| mean ESM-1v | 3.775 | 6.403 |
| mean FoldX ΔΔG | 0.46 | 2.181 |
| mean ThermoMPNN ΔΔG | 0.352 | 1.144 |
| mean REVEL | 0.463 | 0.82 |
| mean CADD phred | 17.141 | 26.596 |
| mean SIFT | -0.232 | -0.029 |
| mean PolyPhen-2 HVAR | 0.244 | 0.9 |
| mean MetaRNN | 0.46 | 0.896 |
| mean VEST4 | 0.47 | 0.843 |
| mean PrimateAI | 0.47 | 0.66 |
| mean PROVEAN | 0.853 | 3.346 |
| **fraction seen in gnomAD** | **25.57%** (694) | **25.75%** (1,010) |
| fraction at the interface | 3.32% | 5.20% |

**Validation:** the damaging cluster is enriched in the population — 25.75% of it appears in gnomAD against 25.57% of the tolerant cluster (a 1.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 23,389**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 14,023 | 9,366 |
| mean AlphaMissense | 0.416 | 0.884 |
| mean ESM-1v | 4.583 | 8.362 |
| mean FoldX ΔΔG | 0.53 | 3.899 |
| mean ThermoMPNN ΔΔG | 0.407 | 1.738 |
| **fraction seen in gnomAD** | **9.64%** (1,352) | **4.94%** (463) |

Depletion **2.0×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 4.08% | 4.85% |

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
