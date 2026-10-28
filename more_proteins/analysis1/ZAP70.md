# ZAP70 — variant-effect analysis

*Tyrosine-protein kinase ZAP-70* · UniProt `P43403` · 619 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 10–102 | 93 |
| SH2 2 | 163–254 | 92 |
| Protein kinase | 338–600 | 263 |

**Pair analysed:** SH2 1 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **13.22 Å**, intra-module **3.5 Å**, **ratio 3.77**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 42.9 | 0 | 100% / 100% |
| 4k2r.1.A (99.8% id) | 43.0 | 0 | 100% / 100% |
| 4fl2.1.A (56.9% id) | 35.0 | 17 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P43403_4fl2-1-A.pdb`, centroid distance **35.0 Å**, **17 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `17, 37, 40, 41, 43, 60, 62, 72`

**Domain B interface residues (9):** `567, 591, 592, 594, 595, 596, 598, 599, 600`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 323 | 11,438 | 0.619 | 0.856 | 3.6e-11 |
| ESM-1v | 323 | 11,438 | -9.245 | -10.357 | 0.00055 |
| FoldX ΔΔG | 323 | 10,412 | 0.543 | 1.376 | 5.4e-16 |
| ThermoMPNN ΔΔG | 323 | 11,438 | 0.546 | 0.788 | 0.00055 |
| REVEL | 97 | 3,578 | 0.331 | 0.472 | 0.0035 |
| CADD phred | 103 | 3,757 | 25.0 | 24.4 | 0.31 |
| SIFT | 97 | 3,578 | 0.053 | 0.021 | 0.23 |
| PolyPhen-2 HVAR | 97 | 3,578 | 0.861 | 0.726 | 0.48 |
| MetaRNN | 97 | 3,578 | 0.494 | 0.691 | 0.025 |
| VEST4 | 103 | 3,757 | 0.482 | 0.639 | 0.0023 |
| PrimateAI | 97 | 3,572 | 0.574 | 0.684 | 0.012 |
| MutationAssessor | 97 | 3,568 | 1.2 | 1.812 | 0.00038 |
| PROVEAN | 97 | 3,578 | -1.66 | -2.35 | 0.0009 |
| ESM1b | 97 | 3,578 | -5.522 | -7.768 | 1.2e-06 |
| AlphaMissense (dbNSFP) | 97 | 3,572 | 0.374 | 0.651 | 0.0017 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 11,761 |
| ESM-1v | 11,761 |
| FoldX ΔΔG (ProtVar) | 10,735 |
| ThermoMPNN ΔΔG | 11,761 |
| revel | 3,675 |
| cadd | 3,860 |
| sift | 3,675 |
| polyphen | 3,675 |
| metarnn | 3,675 |
| vest4 | 3,860 |
| primateai | 3,669 |
| mutassessor | 3,665 |
| provean | 3,675 |
| esm1b | 3,675 |
| am_dbnsfp | 3,669 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.875 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.521 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.568 |
| AlphaMissense vs revel | +0.726 |
| AlphaMissense vs cadd | +0.763 |
| AlphaMissense vs sift | -0.723 |
| AlphaMissense vs polyphen | +0.746 |
| AlphaMissense vs metarnn | +0.851 |
| AlphaMissense vs vest4 | +0.854 |
| AlphaMissense vs primateai | +0.716 |
| AlphaMissense vs mutassessor | +0.633 |
| AlphaMissense vs provean | -0.757 |
| AlphaMissense vs esm1b | -0.799 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.446 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.517 |
| ESM-1v vs revel | -0.718 |
| ESM-1v vs cadd | -0.751 |
| ESM-1v vs sift | +0.746 |
| ESM-1v vs polyphen | -0.716 |
| ESM-1v vs metarnn | -0.831 |
| ESM-1v vs vest4 | -0.807 |
| ESM-1v vs primateai | -0.644 |
| ESM-1v vs mutassessor | -0.660 |
| ESM-1v vs provean | +0.795 |
| ESM-1v vs esm1b | +0.882 |
| ESM-1v vs am_dbnsfp | -0.858 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.687 |
| FoldX ΔΔG (ProtVar) vs revel | +0.360 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.373 |
| FoldX ΔΔG (ProtVar) vs sift | -0.389 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.352 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.454 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.438 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.265 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.397 |
| FoldX ΔΔG (ProtVar) vs provean | -0.457 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.426 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.502 |
| ThermoMPNN ΔΔG vs revel | +0.416 |
| ThermoMPNN ΔΔG vs cadd | +0.438 |
| ThermoMPNN ΔΔG vs sift | -0.472 |
| ThermoMPNN ΔΔG vs polyphen | +0.412 |
| ThermoMPNN ΔΔG vs metarnn | +0.522 |
| ThermoMPNN ΔΔG vs vest4 | +0.486 |
| ThermoMPNN ΔΔG vs primateai | +0.317 |
| ThermoMPNN ΔΔG vs mutassessor | +0.471 |
| ThermoMPNN ΔΔG vs provean | -0.497 |
| ThermoMPNN ΔΔG vs esm1b | -0.513 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.562 |
| revel vs cadd | +0.718 |
| revel vs sift | -0.655 |
| revel vs polyphen | +0.747 |
| revel vs metarnn | +0.845 |
| revel vs vest4 | +0.778 |
| revel vs primateai | +0.574 |
| revel vs mutassessor | +0.575 |
| revel vs provean | -0.712 |
| revel vs esm1b | -0.664 |
| revel vs am_dbnsfp | +0.726 |
| cadd vs sift | -0.749 |
| cadd vs polyphen | +0.793 |
| cadd vs metarnn | +0.800 |
| cadd vs vest4 | +0.764 |
| cadd vs primateai | +0.595 |
| cadd vs mutassessor | +0.557 |
| cadd vs provean | -0.735 |
| cadd vs esm1b | -0.698 |
| cadd vs am_dbnsfp | +0.763 |
| sift vs polyphen | -0.668 |
| sift vs metarnn | -0.777 |
| sift vs vest4 | -0.728 |
| sift vs primateai | -0.509 |
| sift vs mutassessor | -0.646 |
| sift vs provean | +0.800 |
| sift vs esm1b | +0.729 |
| sift vs am_dbnsfp | -0.724 |
| polyphen vs metarnn | +0.832 |
| polyphen vs vest4 | +0.788 |
| polyphen vs primateai | +0.665 |
| polyphen vs mutassessor | +0.543 |
| polyphen vs provean | -0.685 |
| polyphen vs esm1b | -0.636 |
| polyphen vs am_dbnsfp | +0.746 |
| metarnn vs vest4 | +0.933 |
| metarnn vs primateai | +0.693 |
| metarnn vs mutassessor | +0.675 |
| metarnn vs provean | -0.820 |
| metarnn vs esm1b | -0.774 |
| metarnn vs am_dbnsfp | +0.854 |
| vest4 vs primateai | +0.722 |
| vest4 vs mutassessor | +0.643 |
| vest4 vs provean | -0.787 |
| vest4 vs esm1b | -0.748 |
| vest4 vs am_dbnsfp | +0.855 |
| primateai vs mutassessor | +0.409 |
| primateai vs provean | -0.563 |
| primateai vs esm1b | -0.555 |
| primateai vs am_dbnsfp | +0.716 |
| mutassessor vs provean | -0.645 |
| mutassessor vs esm1b | -0.625 |
| mutassessor vs am_dbnsfp | +0.633 |
| provean vs esm1b | +0.775 |
| provean vs am_dbnsfp | -0.758 |
| esm1b vs am_dbnsfp | -0.799 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 148 |
| conflict | 7 |
| pathogenic | 3 |
| likely_benign | 3 |
| benign | 1 |
| likely_pathogenic | 1 |

**gnomAD r4 missense variants mapped:** 739

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,354** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,384 | 1,970 |
| mean AlphaMissense | 0.272 | 0.85 |
| mean ESM-1v | 6.179 | 11.503 |
| mean FoldX ΔΔG | 0.687 | 2.842 |
| mean ThermoMPNN ΔΔG | 0.478 | 1.345 |
| mean REVEL | 0.282 | 0.673 |
| mean CADD phred | 15.803 | 26.746 |
| mean SIFT | -0.264 | -0.025 |
| mean PolyPhen-2 HVAR | 0.24 | 0.873 |
| mean MetaRNN | 0.325 | 0.859 |
| mean VEST4 | 0.358 | 0.788 |
| mean PrimateAI | 0.551 | 0.747 |
| mean PROVEAN | 1.159 | 3.999 |
| **fraction seen in gnomAD** | **24.35%** (337) | **17.46%** (344) |
| fraction at the interface | 4.05% | 2.08% |

**Validation:** the damaging cluster is **depleted** in the population — 17.46% of it appears in gnomAD against 24.35% of the tolerant cluster (a 1.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 10,735**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,666 | 6,069 |
| mean AlphaMissense | 0.416 | 0.949 |
| mean ESM-1v | 7.405 | 13.448 |
| mean FoldX ΔΔG | 0.616 | 3.664 |
| mean ThermoMPNN ΔΔG | 0.422 | 1.572 |
| **fraction seen in gnomAD** | **9.77%** (456) | **3.71%** (225) |

Depletion **2.6×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 4.16% | 2.13% |

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
