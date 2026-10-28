# SF3B4 — variant-effect analysis

*Splicing factor 3B subunit 4* · UniProt `Q15427` · 424 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| RRM 1 | 13–91 | 79 |
| RRM 2 | 100–179 | 80 |

**Pair analysed:** RRM 1 ↔ RRM 2

**AlphaFold PAE:** inter-module mean **8.77 Å**, intra-module **2.72 Å**, **ratio 3.23**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 25.3 | 17 | 100% / 100% |
| SWISSMODEL_6tr0-1-A_6-182 | 37.2 | 0 | 100% / 100% |
| SWISSMODEL_6xlx-1-A_9-181 | 24.8 | 23 | 100% / 100% |
| SWISSMODEL_8hk1-1-E_11-181 | 23.8 | 43 | 100% / 100% |
| SWISSMODEL_8i0p-1-9_13-180 | 26.9 | 7 | 100% / 100% |
| SWISSMODEL_9f4k-1-A_7-179 | 31.0 | 11 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `SF3B4_Q15427_SWISSMODEL_8hk1-1-E_11-181.pdb`, centroid distance **23.8 Å**, **43 residue pairs** in contact within 5 Å.

**Domain A interface residues (17):** `16, 17, 18, 19, 45, 56, 58, 75, 76, 77, 78, 82, 83, 85, 87, 89, 91`

**Domain B interface residues (18):** `107, 108, 109, 110, 112, 115, 134, 135, 137, 138, 139, 140, 141, 142, 143, 168, 169, 170`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 665 | 7,391 | 0.999 | 0.639 | 1.8e-128 |
| ESM-1v | 665 | 7,391 | -16.291 | -9.752 | 5.8e-153 |
| FoldX ΔΔG | 665 | 7,372 | 1.037 | 0.51 | 4e-09 |
| ThermoMPNN ΔΔG | 665 | 7,391 | 0.853 | 0.263 | 5.7e-57 |
| REVEL | 213 | 2,282 | 0.398 | 0.189 | 1e-41 |
| CADD phred | 221 | 2,360 | 25.7 | 23.2 | 9.4e-22 |
| SIFT | 213 | 2,282 | 0.008 | 0.013 | 0.14 |
| PolyPhen-2 HVAR | 213 | 2,282 | 0.928 | 0.489 | 4.1e-20 |
| MetaRNN | 213 | 2,282 | 0.777 | 0.427 | 9.5e-40 |
| VEST4 | 221 | 2,360 | 0.759 | 0.577 | 3.6e-31 |
| PrimateAI | 213 | 2,276 | 0.878 | 0.822 | 4.7e-38 |
| MutationAssessor | 213 | 2,276 | 1.875 | 1.265 | 2.5e-09 |
| PROVEAN | 213 | 2,282 | -5.9 | -2.72 | 3.2e-51 |
| ESM1b | 213 | 2,282 | -13.91 | -8.059 | 1.3e-47 |
| AlphaMissense (dbNSFP) | 213 | 2,276 | 0.997 | 0.478 | 1.2e-42 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 8,056 |
| ESM-1v | 8,056 |
| FoldX ΔΔG (ProtVar) | 8,037 |
| ThermoMPNN ΔΔG | 8,056 |
| revel | 2,495 |
| cadd | 2,581 |
| sift | 2,495 |
| polyphen | 2,495 |
| metarnn | 2,495 |
| vest4 | 2,581 |
| primateai | 2,489 |
| mutassessor | 2,489 |
| provean | 2,495 |
| esm1b | 2,495 |
| am_dbnsfp | 2,489 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.891 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.345 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.510 |
| AlphaMissense vs revel | +0.812 |
| AlphaMissense vs cadd | +0.707 |
| AlphaMissense vs sift | -0.268 |
| AlphaMissense vs polyphen | +0.625 |
| AlphaMissense vs metarnn | +0.793 |
| AlphaMissense vs vest4 | +0.721 |
| AlphaMissense vs primateai | +0.782 |
| AlphaMissense vs mutassessor | +0.421 |
| AlphaMissense vs provean | -0.786 |
| AlphaMissense vs esm1b | -0.826 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.323 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.511 |
| ESM-1v vs revel | -0.813 |
| ESM-1v vs cadd | -0.672 |
| ESM-1v vs sift | +0.274 |
| ESM-1v vs polyphen | -0.621 |
| ESM-1v vs metarnn | -0.806 |
| ESM-1v vs vest4 | -0.720 |
| ESM-1v vs primateai | -0.696 |
| ESM-1v vs mutassessor | -0.468 |
| ESM-1v vs provean | +0.842 |
| ESM-1v vs esm1b | +0.928 |
| ESM-1v vs am_dbnsfp | -0.881 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.559 |
| FoldX ΔΔG (ProtVar) vs revel | +0.363 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.314 |
| FoldX ΔΔG (ProtVar) vs sift | -0.223 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.312 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.372 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.314 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.293 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.281 |
| FoldX ΔΔG (ProtVar) vs provean | -0.306 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.324 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.333 |
| ThermoMPNN ΔΔG vs revel | +0.543 |
| ThermoMPNN ΔΔG vs cadd | +0.444 |
| ThermoMPNN ΔΔG vs sift | -0.319 |
| ThermoMPNN ΔΔG vs polyphen | +0.482 |
| ThermoMPNN ΔΔG vs metarnn | +0.555 |
| ThermoMPNN ΔΔG vs vest4 | +0.447 |
| ThermoMPNN ΔΔG vs primateai | +0.369 |
| ThermoMPNN ΔΔG vs mutassessor | +0.400 |
| ThermoMPNN ΔΔG vs provean | -0.533 |
| ThermoMPNN ΔΔG vs esm1b | -0.514 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.505 |
| revel vs cadd | +0.658 |
| revel vs sift | -0.310 |
| revel vs polyphen | +0.760 |
| revel vs metarnn | +0.891 |
| revel vs vest4 | +0.783 |
| revel vs primateai | +0.671 |
| revel vs mutassessor | +0.466 |
| revel vs provean | -0.782 |
| revel vs esm1b | -0.773 |
| revel vs am_dbnsfp | +0.813 |
| cadd vs sift | -0.491 |
| cadd vs polyphen | +0.671 |
| cadd vs metarnn | +0.714 |
| cadd vs vest4 | +0.593 |
| cadd vs primateai | +0.502 |
| cadd vs mutassessor | +0.463 |
| cadd vs provean | -0.623 |
| cadd vs esm1b | -0.631 |
| cadd vs am_dbnsfp | +0.707 |
| sift vs polyphen | -0.479 |
| sift vs metarnn | -0.328 |
| sift vs vest4 | -0.202 |
| sift vs primateai | -0.106 |
| sift vs mutassessor | -0.287 |
| sift vs provean | +0.302 |
| sift vs esm1b | +0.267 |
| sift vs am_dbnsfp | -0.268 |
| polyphen vs metarnn | +0.779 |
| polyphen vs vest4 | +0.566 |
| polyphen vs primateai | +0.496 |
| polyphen vs mutassessor | +0.472 |
| polyphen vs provean | -0.597 |
| polyphen vs esm1b | -0.596 |
| polyphen vs am_dbnsfp | +0.625 |
| metarnn vs vest4 | +0.871 |
| metarnn vs primateai | +0.661 |
| metarnn vs mutassessor | +0.566 |
| metarnn vs provean | -0.759 |
| metarnn vs esm1b | -0.765 |
| metarnn vs am_dbnsfp | +0.795 |
| vest4 vs primateai | +0.617 |
| vest4 vs mutassessor | +0.491 |
| vest4 vs provean | -0.641 |
| vest4 vs esm1b | -0.668 |
| vest4 vs am_dbnsfp | +0.723 |
| primateai vs mutassessor | +0.300 |
| primateai vs provean | -0.636 |
| primateai vs esm1b | -0.655 |
| primateai vs am_dbnsfp | +0.782 |
| mutassessor vs provean | -0.457 |
| mutassessor vs esm1b | -0.427 |
| mutassessor vs am_dbnsfp | +0.421 |
| provean vs esm1b | +0.790 |
| provean vs am_dbnsfp | -0.786 |
| esm1b vs am_dbnsfp | -0.826 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 17 |
| likely_benign | 3 |
| conflict | 3 |
| pathogenic | 2 |
| benign | 1 |

**gnomAD r4 missense variants mapped:** 332

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,483** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,469 | 1,014 |
| mean AlphaMissense | 0.31 | 0.973 |
| mean ESM-1v | 6.604 | 13.955 |
| mean FoldX ΔΔG | 0.376 | 1.872 |
| mean ThermoMPNN ΔΔG | 0.2 | 1.045 |
| mean REVEL | 0.14 | 0.444 |
| mean CADD phred | 19.743 | 26.256 |
| mean SIFT | -0.117 | -0.028 |
| mean PolyPhen-2 HVAR | 0.32 | 0.822 |
| mean MetaRNN | 0.322 | 0.739 |
| mean VEST4 | 0.481 | 0.736 |
| mean PrimateAI | 0.778 | 0.873 |
| mean PROVEAN | 1.694 | 5.727 |
| **fraction seen in gnomAD** | **18.65%** (274) | **5.72%** (58) |
| fraction at the interface | 2.04% | 18.05% |

**Validation:** the damaging cluster is **depleted** in the population — 5.72% of it appears in gnomAD against 18.65% of the tolerant cluster (a 3.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 8,037**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,162 | 3,875 |
| mean AlphaMissense | 0.331 | 0.98 |
| mean ESM-1v | 6.784 | 15.376 |
| mean FoldX ΔΔG | 0.359 | 2.13 |
| mean ThermoMPNN ΔΔG | 0.196 | 1.019 |
| **fraction seen in gnomAD** | **6.37%** (265) | **1.73%** (67) |

Depletion **3.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 0.70% | 16.41% |

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
