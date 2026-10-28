# DICER1 — variant-effect analysis

*Endoribonuclease Dicer* · UniProt `Q9UPY3` · 1922 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 51–227 | 177 |
| Helicase C-terminal | 433–602 | 170 |
| Dicer dsRNA-binding fold | 630–722 | 93 |
| PAZ | 895–1042 | 148 |
| RNase III 1 | 1276–1403 | 128 |
| RNase III 2 | 1666–1824 | 159 |
| DRBM | 1849–1914 | 66 |

**Pair analysed:** Helicase ATP-binding ↔ RNase III 2

**AlphaFold PAE:** inter-module mean **17.12 Å**, intra-module **6.04 Å**, **ratio 2.83**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 44.7 | 0 | 100% / 100% |
| SWISSMODEL_7v6c-1-A_44-1915 | 96.2 | 0 | 100% / 100% |
| SWISSMODEL_7w0e-1-C_40-1914 | 58.0 | 0 | 100% / 100% |
| SWISSMODEL_7xw3-1-A_39-1917 | 34.4 | 33 | 100% / 100% |
| SWISSMODEL_7zpj-1-A_46-1916 | 32.7 | 39 | 100% / 100% |
| SWISSMODEL_8hf0-1-A_40-1915 | 55.9 | 0 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `DICER1_Q9UPY3_SWISSMODEL_7zpj-1-A_46-1916.pdb`, centroid distance **32.7 Å**, **39 residue pairs** in contact within 5 Å.

**Domain A interface residues (14):** `52, 53, 56, 68, 72, 75, 76, 79, 80, 114, 115, 116, 117, 118`

**Domain B interface residues (19):** `1668, 1692, 1693, 1694, 1755, 1756, 1757, 1758, 1759, 1760, 1761, 1762, 1763, 1766, 1767, 1769, 1770, 1774, 1777`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 627 | 35,891 | 0.962 | 0.822 | 6e-19 |
| ESM-1v | 627 | 35,891 | -4.996 | -4.012 | 2.2e-24 |
| FoldX ΔΔG | 627 | 25,916 | 1.025 | 1.118 | 0.044 |
| ThermoMPNN ΔΔG | 627 | 35,891 | 0.695 | 0.418 | 2.7e-11 |
| REVEL | 156 | 8,218 | 0.498 | 0.325 | 1.7e-08 |
| CADD phred | 166 | 8,723 | 24.7 | 24.4 | 0.38 |
| SIFT | 156 | 8,218 | 0.037 | 0.037 | 0.71 |
| PolyPhen-2 HVAR | 156 | 8,139 | 0.912 | 0.721 | 6.3e-05 |
| MetaRNN | 156 | 8,218 | 0.769 | 0.55 | 8e-11 |
| VEST4 | 166 | 8,722 | 0.782 | 0.677 | 3.3e-07 |
| PrimateAI | 156 | 8,137 | 0.859 | 0.786 | 4.9e-14 |
| MutationAssessor | 156 | 8,013 | 1.698 | 1.7 | 0.19 |
| PROVEAN | 156 | 8,218 | -2.71 | -1.58 | 1.4e-06 |
| ESM1b | 156 | 8,218 | -8.331 | -6.162 | 2.1e-07 |
| AlphaMissense (dbNSFP) | 156 | 8,216 | 0.911 | 0.539 | 2.7e-07 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 36,518 |
| ESM-1v | 36,518 |
| FoldX ΔΔG (ProtVar) | 26,543 |
| ThermoMPNN ΔΔG | 36,518 |
| revel | 8,374 |
| cadd | 8,889 |
| sift | 8,374 |
| polyphen | 8,295 |
| metarnn | 8,374 |
| vest4 | 8,888 |
| primateai | 8,293 |
| mutassessor | 8,169 |
| provean | 8,374 |
| esm1b | 8,374 |
| am_dbnsfp | 8,372 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.299 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.415 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.529 |
| AlphaMissense vs revel | +0.783 |
| AlphaMissense vs cadd | +0.760 |
| AlphaMissense vs sift | -0.633 |
| AlphaMissense vs polyphen | +0.702 |
| AlphaMissense vs metarnn | +0.793 |
| AlphaMissense vs vest4 | +0.743 |
| AlphaMissense vs primateai | +0.761 |
| AlphaMissense vs mutassessor | +0.568 |
| AlphaMissense vs provean | -0.729 |
| AlphaMissense vs esm1b | -0.725 |
| AlphaMissense vs am_dbnsfp | +0.982 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.210 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.219 |
| ESM-1v vs revel | -0.342 |
| ESM-1v vs cadd | -0.266 |
| ESM-1v vs sift | +0.349 |
| ESM-1v vs polyphen | -0.271 |
| ESM-1v vs metarnn | -0.343 |
| ESM-1v vs vest4 | -0.277 |
| ESM-1v vs primateai | -0.155 |
| ESM-1v vs mutassessor | -0.395 |
| ESM-1v vs provean | +0.345 |
| ESM-1v vs esm1b | +0.464 |
| ESM-1v vs am_dbnsfp | -0.248 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.691 |
| FoldX ΔΔG (ProtVar) vs revel | +0.373 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.282 |
| FoldX ΔΔG (ProtVar) vs sift | -0.345 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.258 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.402 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.362 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.181 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.356 |
| FoldX ΔΔG (ProtVar) vs provean | -0.396 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.372 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.381 |
| ThermoMPNN ΔΔG vs revel | +0.528 |
| ThermoMPNN ΔΔG vs cadd | +0.436 |
| ThermoMPNN ΔΔG vs sift | -0.386 |
| ThermoMPNN ΔΔG vs polyphen | +0.387 |
| ThermoMPNN ΔΔG vs metarnn | +0.547 |
| ThermoMPNN ΔΔG vs vest4 | +0.487 |
| ThermoMPNN ΔΔG vs primateai | +0.372 |
| ThermoMPNN ΔΔG vs mutassessor | +0.443 |
| ThermoMPNN ΔΔG vs provean | -0.545 |
| ThermoMPNN ΔΔG vs esm1b | -0.555 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.524 |
| revel vs cadd | +0.707 |
| revel vs sift | -0.627 |
| revel vs polyphen | +0.731 |
| revel vs metarnn | +0.878 |
| revel vs vest4 | +0.805 |
| revel vs primateai | +0.661 |
| revel vs mutassessor | +0.618 |
| revel vs provean | -0.728 |
| revel vs esm1b | -0.726 |
| revel vs am_dbnsfp | +0.793 |
| cadd vs sift | -0.721 |
| cadd vs polyphen | +0.693 |
| cadd vs metarnn | +0.729 |
| cadd vs vest4 | +0.690 |
| cadd vs primateai | +0.607 |
| cadd vs mutassessor | +0.550 |
| cadd vs provean | -0.696 |
| cadd vs esm1b | -0.633 |
| cadd vs am_dbnsfp | +0.741 |
| sift vs polyphen | -0.531 |
| sift vs metarnn | -0.633 |
| sift vs vest4 | -0.547 |
| sift vs primateai | -0.388 |
| sift vs mutassessor | -0.618 |
| sift vs provean | +0.716 |
| sift vs esm1b | +0.599 |
| sift vs am_dbnsfp | -0.612 |
| polyphen vs metarnn | +0.716 |
| polyphen vs vest4 | +0.642 |
| polyphen vs primateai | +0.666 |
| polyphen vs mutassessor | +0.469 |
| polyphen vs provean | -0.558 |
| polyphen vs esm1b | -0.573 |
| polyphen vs am_dbnsfp | +0.699 |
| metarnn vs vest4 | +0.932 |
| metarnn vs primateai | +0.649 |
| metarnn vs mutassessor | +0.667 |
| metarnn vs provean | -0.740 |
| metarnn vs esm1b | -0.720 |
| metarnn vs am_dbnsfp | +0.795 |
| vest4 vs primateai | +0.628 |
| vest4 vs mutassessor | +0.578 |
| vest4 vs provean | -0.654 |
| vest4 vs esm1b | -0.641 |
| vest4 vs am_dbnsfp | +0.755 |
| primateai vs mutassessor | +0.326 |
| primateai vs provean | -0.529 |
| primateai vs esm1b | -0.550 |
| primateai vs am_dbnsfp | +0.760 |
| mutassessor vs provean | -0.645 |
| mutassessor vs esm1b | -0.608 |
| mutassessor vs am_dbnsfp | +0.564 |
| provean vs esm1b | +0.776 |
| provean vs am_dbnsfp | -0.742 |
| esm1b vs am_dbnsfp | -0.739 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 2736 |
| conflict | 119 |
| pathogenic | 23 |
| likely_benign | 19 |
| likely_pathogenic | 14 |
| benign | 8 |

**gnomAD r4 missense variants mapped:** 1,777

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 5,952** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 2,399 | 3,553 |
| mean AlphaMissense | 0.321 | 0.882 |
| mean ESM-1v | 3.617 | 5.249 |
| mean FoldX ΔΔG | 0.603 | 2.422 |
| mean ThermoMPNN ΔΔG | 0.412 | 1.201 |
| mean REVEL | 0.233 | 0.604 |
| mean CADD phred | 19.813 | 27.204 |
| mean SIFT | -0.31 | -0.033 |
| mean PolyPhen-2 HVAR | 0.38 | 0.849 |
| mean MetaRNN | 0.377 | 0.791 |
| mean VEST4 | 0.509 | 0.811 |
| mean PrimateAI | 0.694 | 0.837 |
| mean PROVEAN | 0.917 | 4.364 |
| **fraction seen in gnomAD** | **19.42%** (466) | **10.22%** (363) |
| fraction at the interface | 2.21% | 2.90% |

**Validation:** the damaging cluster is **depleted** in the population — 10.22% of it appears in gnomAD against 19.42% of the tolerant cluster (a 1.9-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 20 pathogenic / 1 benign, cluster 0 has 0 / 2; OR = inf, p = 0.012.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 26,543**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 16,895 | 9,648 |
| mean AlphaMissense | 0.627 | 0.966 |
| mean ESM-1v | 4.062 | 6.776 |
| mean FoldX ΔΔG | 0.637 | 4.77 |
| mean ThermoMPNN ΔΔG | 0.467 | 1.919 |
| **fraction seen in gnomAD** | **5.63%** (952) | **2.12%** (205) |

Depletion **2.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.35% | 2.38% |

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
