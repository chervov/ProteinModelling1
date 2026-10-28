# DDX3Y — variant-effect analysis

*ATP-dependent RNA helicase DDX3Y* · UniProt `O15523` · 660 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 209–401 | 193 |
| Helicase C-terminal | 412–573 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **12.36 Å**, intra-module **3.96 Å**, **ratio 3.12**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 31.6 | 35 | 100% / 100% |
| SWISSMODEL_8ark-2-A_125-573 | 42.2 | 18 | 100% / 100% |
| SWISSMODEL_8arp-1-A_118-573 | 31.4 | 44 | 100% / 100% |
| SWISSMODEL_8ssw-1-A_132-578 | 50.7 | 0 | 100% / 100% |
| SWISSMODEL_9e2c-1-A_132-572 | 31.9 | 38 | 100% / 99% |

## 2. The inter-domain interface

Most compact structure: `DDX3Y_O15523_SWISSMODEL_8arp-1-A_118-573.pdb`, centroid distance **31.4 Å**, **44 residue pairs** in contact within 5 Å.

**Domain A interface residues (22):** `223, 224, 225, 229, 273, 274, 275, 276, 278, 279, 282, 285, 299, 300, 301, 302, 346, 349, 352, 353, 381, 382`

**Domain B interface residues (19):** `447, 448, 449, 450, 470, 471, 472, 475, 478, 496, 498, 499, 501, 518, 519, 521, 522, 525, 549`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 779 | 11,761 | 0.998 | 0.728 | 7.3e-169 |
| ESM-1v | 779 | 11,761 | -16.623 | -11.83 | 7.9e-171 |
| FoldX ΔΔG | 779 | 8,265 | 0.336 | 1.357 | 2.2e-52 |
| ThermoMPNN ΔΔG | 779 | 11,761 | 0.452 | 0.363 | 0.6 |
| CADD phred | 255 | 3,812 | 26.9 | 23.8 | 5.1e-30 |
| SIFT | 236 | 3,602 | 0.0 | 0.017 | 7.7e-42 |
| PolyPhen-2 HVAR | 236 | 3,602 | 0.986 | 0.548 | 5.9e-30 |
| MetaRNN | 236 | 3,602 | 0.846 | 0.349 | 1.3e-58 |
| VEST4 | 255 | 3,812 | 0.778 | 0.544 | 1.3e-52 |
| MutationAssessor | 236 | 3,596 | 2.975 | 1.965 | 2e-17 |
| PROVEAN | 236 | 3,602 | -5.595 | -2.95 | 1.6e-30 |
| ESM1b | 236 | 3,602 | -13.405 | -10.427 | 2.3e-31 |
| AlphaMissense (dbNSFP) | 236 | 3,596 | 0.996 | 0.477 | 4.8e-59 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,540 |
| ESM-1v | 12,540 |
| FoldX ΔΔG (ProtVar) | 9,044 |
| ThermoMPNN ΔΔG | 12,540 |
| revel | 0 |
| cadd | 4,067 |
| sift | 3,838 |
| polyphen | 3,838 |
| metarnn | 3,838 |
| vest4 | 4,067 |
| primateai | 14 |
| mutassessor | 3,832 |
| provean | 3,838 |
| esm1b | 3,838 |
| am_dbnsfp | 3,832 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.886 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.499 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.558 |
| AlphaMissense vs cadd | +0.800 |
| AlphaMissense vs sift | -0.788 |
| AlphaMissense vs polyphen | +0.784 |
| AlphaMissense vs metarnn | +0.834 |
| AlphaMissense vs vest4 | +0.821 |
| AlphaMissense vs mutassessor | +0.543 |
| AlphaMissense vs provean | -0.777 |
| AlphaMissense vs esm1b | -0.756 |
| AlphaMissense vs am_dbnsfp | +0.997 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.405 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.533 |
| ESM-1v vs cadd | -0.804 |
| ESM-1v vs sift | +0.803 |
| ESM-1v vs polyphen | -0.765 |
| ESM-1v vs metarnn | -0.850 |
| ESM-1v vs vest4 | -0.825 |
| ESM-1v vs mutassessor | -0.508 |
| ESM-1v vs provean | +0.801 |
| ESM-1v vs esm1b | +0.852 |
| ESM-1v vs am_dbnsfp | -0.873 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.692 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.418 |
| FoldX ΔΔG (ProtVar) vs sift | -0.394 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.463 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.441 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.430 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.359 |
| FoldX ΔΔG (ProtVar) vs provean | -0.417 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.391 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.472 |
| ThermoMPNN ΔΔG vs cadd | +0.489 |
| ThermoMPNN ΔΔG vs sift | -0.483 |
| ThermoMPNN ΔΔG vs polyphen | +0.493 |
| ThermoMPNN ΔΔG vs metarnn | +0.508 |
| ThermoMPNN ΔΔG vs vest4 | +0.508 |
| ThermoMPNN ΔΔG vs mutassessor | +0.321 |
| ThermoMPNN ΔΔG vs provean | -0.481 |
| ThermoMPNN ΔΔG vs esm1b | -0.520 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.534 |
| cadd vs sift | -0.846 |
| cadd vs polyphen | +0.825 |
| cadd vs metarnn | +0.845 |
| cadd vs vest4 | +0.774 |
| cadd vs mutassessor | +0.533 |
| cadd vs provean | -0.769 |
| cadd vs esm1b | -0.702 |
| cadd vs am_dbnsfp | +0.799 |
| sift vs polyphen | -0.797 |
| sift vs metarnn | -0.807 |
| sift vs vest4 | -0.734 |
| sift vs mutassessor | -0.580 |
| sift vs provean | +0.772 |
| sift vs esm1b | +0.719 |
| sift vs am_dbnsfp | -0.789 |
| polyphen vs metarnn | +0.829 |
| polyphen vs vest4 | +0.740 |
| polyphen vs mutassessor | +0.560 |
| polyphen vs provean | -0.727 |
| polyphen vs esm1b | -0.653 |
| polyphen vs am_dbnsfp | +0.784 |
| metarnn vs vest4 | +0.899 |
| metarnn vs mutassessor | +0.539 |
| metarnn vs provean | -0.845 |
| metarnn vs esm1b | -0.743 |
| metarnn vs am_dbnsfp | +0.833 |
| vest4 vs mutassessor | +0.491 |
| vest4 vs provean | -0.782 |
| vest4 vs esm1b | -0.731 |
| vest4 vs am_dbnsfp | +0.820 |
| mutassessor vs provean | -0.496 |
| mutassessor vs esm1b | -0.385 |
| mutassessor vs am_dbnsfp | +0.545 |
| provean vs esm1b | +0.745 |
| provean vs am_dbnsfp | -0.778 |
| esm1b vs am_dbnsfp | -0.754 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 165

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,769** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,053 | 1,716 |
| mean AlphaMissense | 0.293 | 0.901 |
| mean ESM-1v | 8.513 | 13.606 |
| mean FoldX ΔΔG | 0.53 | 2.714 |
| mean ThermoMPNN ΔΔG | 0.361 | 1.156 |
| mean CADD phred | 17.533 | 26.922 |
| mean SIFT | -0.23 | -0.006 |
| mean PolyPhen-2 HVAR | 0.192 | 0.892 |
| mean MetaRNN | 0.248 | 0.72 |
| mean VEST4 | 0.399 | 0.726 |
| mean PROVEAN | 2.03 | 5.593 |
| **fraction seen in gnomAD** | **6.84%** (72) | **1.17%** (20) |
| fraction at the interface | 1.99% | 12.53% |

**Validation:** the damaging cluster is **depleted** in the population — 1.17% of it appears in gnomAD against 6.84% of the tolerant cluster (a 5.8-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 10 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 9,044**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,171 | 5,873 |
| mean AlphaMissense | 0.389 | 0.962 |
| mean ESM-1v | 9.714 | 15.662 |
| mean FoldX ΔΔG | 0.47 | 3.36 |
| mean ThermoMPNN ΔΔG | 0.338 | 1.3 |
| **fraction seen in gnomAD** | **2.59%** (82) | **0.17%** (10) |

Depletion **15.2×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 2.49% | 11.92% |

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
