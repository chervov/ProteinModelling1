# CSK — variant-effect analysis

*Tyrosine-protein kinase CSK* · UniProt `P41240` · 450 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH3 | 9–70 | 62 |
| SH2 | 82–171 | 90 |
| Protein kinase | 195–449 | 255 |

**Pair analysed:** SH3 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **11.09 Å**, intra-module **3.39 Å**, **ratio 3.27**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.4 | 11 | 100% / 100% |
| 1k9a.5.A (98.4% id) | 35.8 | 8 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P41240.pdb`, centroid distance **34.4 Å**, **11 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `13, 32, 33, 34, 53, 68, 69, 70`

**Domain B interface residues (8):** `215, 217, 241, 242, 244, 251, 252, 253`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 304 | 8,246 | 0.762 | 0.893 | 2e-05 |
| ESM-1v | 304 | 8,246 | -9.769 | -10.736 | 0.0017 |
| FoldX ΔΔG | 304 | 8,151 | 1.292 | 1.231 | 0.3 |
| ThermoMPNN ΔΔG | 304 | 8,246 | 1.083 | 0.971 | 0.03 |
| REVEL | 91 | 2,557 | 0.358 | 0.494 | 0.033 |
| CADD phred | 98 | 2,687 | 26.35 | 25.4 | 0.014 |
| SIFT | 91 | 2,557 | 0.03 | 0.014 | 0.089 |
| PolyPhen-2 HVAR | 91 | 2,557 | 0.373 | 0.803 | 0.0028 |
| MetaRNN | 91 | 2,557 | 0.624 | 0.775 | 0.051 |
| VEST4 | 98 | 2,687 | 0.659 | 0.647 | 0.64 |
| PrimateAI | 91 | 2,551 | 0.823 | 0.802 | 0.001 |
| MutationAssessor | 91 | 2,551 | 1.73 | 1.75 | 0.58 |
| PROVEAN | 91 | 2,557 | -2.58 | -2.89 | 0.1 |
| ESM1b | 91 | 2,557 | -10.551 | -10.415 | 0.79 |
| AlphaMissense (dbNSFP) | 91 | 2,551 | 0.633 | 0.701 | 0.096 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 8,550 |
| ESM-1v | 8,550 |
| FoldX ΔΔG (ProtVar) | 8,455 |
| ThermoMPNN ΔΔG | 8,550 |
| revel | 2,648 |
| cadd | 2,785 |
| sift | 2,648 |
| polyphen | 2,648 |
| metarnn | 2,648 |
| vest4 | 2,785 |
| primateai | 2,642 |
| mutassessor | 2,642 |
| provean | 2,648 |
| esm1b | 2,648 |
| am_dbnsfp | 2,642 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.903 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.532 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.597 |
| AlphaMissense vs revel | +0.740 |
| AlphaMissense vs cadd | +0.720 |
| AlphaMissense vs sift | -0.768 |
| AlphaMissense vs polyphen | +0.815 |
| AlphaMissense vs metarnn | +0.858 |
| AlphaMissense vs vest4 | +0.809 |
| AlphaMissense vs primateai | +0.649 |
| AlphaMissense vs mutassessor | +0.728 |
| AlphaMissense vs provean | -0.809 |
| AlphaMissense vs esm1b | -0.794 |
| AlphaMissense vs am_dbnsfp | +0.999 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.497 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.576 |
| ESM-1v vs revel | -0.728 |
| ESM-1v vs cadd | -0.712 |
| ESM-1v vs sift | +0.766 |
| ESM-1v vs polyphen | -0.773 |
| ESM-1v vs metarnn | -0.850 |
| ESM-1v vs vest4 | -0.800 |
| ESM-1v vs primateai | -0.572 |
| ESM-1v vs mutassessor | -0.761 |
| ESM-1v vs provean | +0.810 |
| ESM-1v vs esm1b | +0.874 |
| ESM-1v vs am_dbnsfp | -0.888 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.736 |
| FoldX ΔΔG (ProtVar) vs revel | +0.405 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.396 |
| FoldX ΔΔG (ProtVar) vs sift | -0.446 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.461 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.511 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.501 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.301 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.512 |
| FoldX ΔΔG (ProtVar) vs provean | -0.472 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.457 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.537 |
| ThermoMPNN ΔΔG vs revel | +0.478 |
| ThermoMPNN ΔΔG vs cadd | +0.482 |
| ThermoMPNN ΔΔG vs sift | -0.490 |
| ThermoMPNN ΔΔG vs polyphen | +0.531 |
| ThermoMPNN ΔΔG vs metarnn | +0.573 |
| ThermoMPNN ΔΔG vs vest4 | +0.564 |
| ThermoMPNN ΔΔG vs primateai | +0.348 |
| ThermoMPNN ΔΔG vs mutassessor | +0.595 |
| ThermoMPNN ΔΔG vs provean | -0.517 |
| ThermoMPNN ΔΔG vs esm1b | -0.533 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.609 |
| revel vs cadd | +0.639 |
| revel vs sift | -0.691 |
| revel vs polyphen | +0.751 |
| revel vs metarnn | +0.827 |
| revel vs vest4 | +0.702 |
| revel vs primateai | +0.521 |
| revel vs mutassessor | +0.610 |
| revel vs provean | -0.723 |
| revel vs esm1b | -0.648 |
| revel vs am_dbnsfp | +0.741 |
| cadd vs sift | -0.717 |
| cadd vs polyphen | +0.716 |
| cadd vs metarnn | +0.731 |
| cadd vs vest4 | +0.725 |
| cadd vs primateai | +0.506 |
| cadd vs mutassessor | +0.617 |
| cadd vs provean | -0.704 |
| cadd vs esm1b | -0.631 |
| cadd vs am_dbnsfp | +0.721 |
| sift vs polyphen | -0.783 |
| sift vs metarnn | -0.796 |
| sift vs vest4 | -0.709 |
| sift vs primateai | -0.470 |
| sift vs mutassessor | -0.705 |
| sift vs provean | +0.807 |
| sift vs esm1b | +0.681 |
| sift vs am_dbnsfp | -0.769 |
| polyphen vs metarnn | +0.847 |
| polyphen vs vest4 | +0.726 |
| polyphen vs primateai | +0.566 |
| polyphen vs mutassessor | +0.702 |
| polyphen vs provean | -0.793 |
| polyphen vs esm1b | -0.688 |
| polyphen vs am_dbnsfp | +0.816 |
| metarnn vs vest4 | +0.891 |
| metarnn vs primateai | +0.615 |
| metarnn vs mutassessor | +0.757 |
| metarnn vs provean | -0.820 |
| metarnn vs esm1b | -0.748 |
| metarnn vs am_dbnsfp | +0.866 |
| vest4 vs primateai | +0.614 |
| vest4 vs mutassessor | +0.683 |
| vest4 vs provean | -0.737 |
| vest4 vs esm1b | -0.705 |
| vest4 vs am_dbnsfp | +0.817 |
| primateai vs mutassessor | +0.426 |
| primateai vs provean | -0.529 |
| primateai vs esm1b | -0.510 |
| primateai vs am_dbnsfp | +0.651 |
| mutassessor vs provean | -0.696 |
| mutassessor vs esm1b | -0.661 |
| mutassessor vs am_dbnsfp | +0.731 |
| provean vs esm1b | +0.734 |
| provean vs am_dbnsfp | -0.807 |
| esm1b vs am_dbnsfp | -0.794 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 4 |
| benign | 2 |

**gnomAD r4 missense variants mapped:** 323

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,620** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,121 | 1,499 |
| mean AlphaMissense | 0.267 | 0.881 |
| mean ESM-1v | 6.006 | 11.994 |
| mean FoldX ΔΔG | 0.609 | 2.9 |
| mean ThermoMPNN ΔΔG | 0.493 | 1.484 |
| mean REVEL | 0.27 | 0.673 |
| mean CADD phred | 19.977 | 27.593 |
| mean SIFT | -0.288 | -0.022 |
| mean PolyPhen-2 HVAR | 0.173 | 0.887 |
| mean MetaRNN | 0.4 | 0.891 |
| mean VEST4 | 0.405 | 0.767 |
| mean PrimateAI | 0.701 | 0.827 |
| mean PROVEAN | 0.994 | 5.081 |
| **fraction seen in gnomAD** | **17.84%** (200) | **7.94%** (119) |
| fraction at the interface | 3.84% | 3.20% |

**Validation:** the damaging cluster is **depleted** in the population — 7.94% of it appears in gnomAD against 17.84% of the tolerant cluster (a 2.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 8,455**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,899 | 4,556 |
| mean AlphaMissense | 0.433 | 0.96 |
| mean ESM-1v | 7.262 | 14.142 |
| mean FoldX ΔΔG | 0.541 | 3.931 |
| mean ThermoMPNN ΔΔG | 0.471 | 1.754 |
| **fraction seen in gnomAD** | **6.46%** (252) | **1.47%** (67) |

Depletion **4.4×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 4.08% | 3.18% |

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
