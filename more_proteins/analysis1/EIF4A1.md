# EIF4A1 — variant-effect analysis

*Eukaryotic initiation factor 4A-I* · UniProt `P60842` · 406 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Helicase ATP-binding | 63–234 | 172 |
| Helicase C-terminal | 245–406 | 162 |

**Pair analysed:** Helicase ATP-binding ↔ Helicase C-terminal

**AlphaFold PAE:** inter-module mean **9.66 Å**, intra-module **3.95 Å**, **ratio 2.44**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 30.1 | 49 | 100% / 100% |
| SWISSMODEL_2hxy-1-A_32-406 | 36.7 | 27 | 100% / 100% |
| SWISSMODEL_3eiq-1-A_22-400 | 36.4 | 5 | 100% / 96% |
| SWISSMODEL_4c9b-1-A_15-406 | 47.6 | 3 | 100% / 100% |
| SWISSMODEL_9avr-1-A_30-402 | 29.2 | 54 | 100% / 98% |

## 2. The inter-domain interface

Most compact structure: `EIF4A1_P60842_SWISSMODEL_9avr-1-A_30-402.pdb`, centroid distance **29.2 Å**, **54 residue pairs** in contact within 5 Å.

**Domain A interface residues (21):** `78, 79, 80, 81, 108, 109, 110, 111, 112, 114, 115, 135, 136, 137, 183, 185, 186, 213, 214, 215, 217`

**Domain B interface residues (21):** `302, 308, 311, 312, 315, 319, 331, 332, 334, 335, 336, 337, 354, 355, 357, 358, 361, 362, 365, 366, 391`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 798 | 6,916 | 0.999 | 0.968 | 5.8e-142 |
| ESM-1v | 798 | 6,916 | -15.515 | -11.219 | 7.5e-143 |
| FoldX ΔΔG | 798 | 6,479 | 1.986 | 1.244 | 1.9e-07 |
| ThermoMPNN ΔΔG | 798 | 6,916 | 0.577 | 0.751 | 3e-09 |
| REVEL | 233 | 2,044 | 0.705 | 0.392 | 6.8e-55 |
| CADD phred | 254 | 2,173 | 26.9 | 25.1 | 1.5e-11 |
| SIFT | 233 | 2,044 | 0.0 | 0.001 | 2.8e-19 |
| PolyPhen-2 HVAR | 233 | 2,044 | 0.943 | 0.31 | 6.5e-27 |
| MetaRNN | 240 | 2,060 | 0.948 | 0.734 | 2.2e-55 |
| VEST4 | 254 | 2,155 | 0.892 | 0.733 | 1e-34 |
| MutationAssessor | 233 | 2,039 | 3.61 | 1.805 | 1.1e-33 |
| PROVEAN | 233 | 2,044 | -5.42 | -3.58 | 3.8e-23 |
| ESM1b | 240 | 2,057 | -13.316 | -11.978 | 4e-10 |
| AlphaMissense (dbNSFP) | 240 | 2,060 | 0.995 | 0.814 | 5.8e-49 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 7,714 |
| ESM-1v | 7,714 |
| FoldX ΔΔG (ProtVar) | 7,277 |
| ThermoMPNN ΔΔG | 7,714 |
| revel | 2,277 |
| cadd | 2,427 |
| sift | 2,277 |
| polyphen | 2,277 |
| metarnn | 2,300 |
| vest4 | 2,409 |
| primateai | 6 |
| mutassessor | 2,272 |
| provean | 2,277 |
| esm1b | 2,297 |
| am_dbnsfp | 2,300 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.870 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.496 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.491 |
| AlphaMissense vs revel | +0.762 |
| AlphaMissense vs cadd | +0.669 |
| AlphaMissense vs sift | -0.740 |
| AlphaMissense vs polyphen | +0.779 |
| AlphaMissense vs metarnn | +0.821 |
| AlphaMissense vs vest4 | +0.780 |
| AlphaMissense vs mutassessor | +0.656 |
| AlphaMissense vs provean | -0.758 |
| AlphaMissense vs esm1b | -0.694 |
| AlphaMissense vs am_dbnsfp | +0.940 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.468 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.472 |
| ESM-1v vs revel | -0.749 |
| ESM-1v vs cadd | -0.658 |
| ESM-1v vs sift | +0.742 |
| ESM-1v vs polyphen | -0.772 |
| ESM-1v vs metarnn | -0.826 |
| ESM-1v vs vest4 | -0.747 |
| ESM-1v vs mutassessor | -0.698 |
| ESM-1v vs provean | +0.743 |
| ESM-1v vs esm1b | +0.771 |
| ESM-1v vs am_dbnsfp | -0.800 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.694 |
| FoldX ΔΔG (ProtVar) vs revel | +0.405 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.354 |
| FoldX ΔΔG (ProtVar) vs sift | -0.365 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.490 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.455 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.463 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.395 |
| FoldX ΔΔG (ProtVar) vs provean | -0.389 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.372 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.440 |
| ThermoMPNN ΔΔG vs revel | +0.420 |
| ThermoMPNN ΔΔG vs cadd | +0.388 |
| ThermoMPNN ΔΔG vs sift | -0.402 |
| ThermoMPNN ΔΔG vs polyphen | +0.525 |
| ThermoMPNN ΔΔG vs metarnn | +0.468 |
| ThermoMPNN ΔΔG vs vest4 | +0.474 |
| ThermoMPNN ΔΔG vs mutassessor | +0.415 |
| ThermoMPNN ΔΔG vs provean | -0.389 |
| ThermoMPNN ΔΔG vs esm1b | -0.444 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.460 |
| revel vs cadd | +0.645 |
| revel vs sift | -0.682 |
| revel vs polyphen | +0.749 |
| revel vs metarnn | +0.867 |
| revel vs vest4 | +0.790 |
| revel vs mutassessor | +0.597 |
| revel vs provean | -0.732 |
| revel vs esm1b | -0.652 |
| revel vs am_dbnsfp | +0.780 |
| cadd vs sift | -0.656 |
| cadd vs polyphen | +0.745 |
| cadd vs metarnn | +0.691 |
| cadd vs vest4 | +0.646 |
| cadd vs mutassessor | +0.597 |
| cadd vs provean | -0.641 |
| cadd vs esm1b | -0.558 |
| cadd vs am_dbnsfp | +0.660 |
| sift vs polyphen | -0.738 |
| sift vs metarnn | -0.754 |
| sift vs vest4 | -0.667 |
| sift vs mutassessor | -0.605 |
| sift vs provean | +0.737 |
| sift vs esm1b | +0.668 |
| sift vs am_dbnsfp | -0.744 |
| polyphen vs metarnn | +0.849 |
| polyphen vs vest4 | +0.768 |
| polyphen vs mutassessor | +0.725 |
| polyphen vs provean | -0.682 |
| polyphen vs esm1b | -0.634 |
| polyphen vs am_dbnsfp | +0.784 |
| metarnn vs vest4 | +0.863 |
| metarnn vs mutassessor | +0.712 |
| metarnn vs provean | -0.775 |
| metarnn vs esm1b | -0.673 |
| metarnn vs am_dbnsfp | +0.825 |
| vest4 vs mutassessor | +0.638 |
| vest4 vs provean | -0.710 |
| vest4 vs esm1b | -0.628 |
| vest4 vs am_dbnsfp | +0.786 |
| mutassessor vs provean | -0.567 |
| mutassessor vs esm1b | -0.501 |
| mutassessor vs am_dbnsfp | +0.679 |
| provean vs esm1b | +0.667 |
| provean vs am_dbnsfp | -0.756 |
| esm1b vs am_dbnsfp | -0.707 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 1 |

**gnomAD r4 missense variants mapped:** 275

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,138** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 865 | 1,273 |
| mean AlphaMissense | 0.53 | 0.956 |
| mean ESM-1v | 7.003 | 12.457 |
| mean FoldX ΔΔG | 0.551 | 2.63 |
| mean ThermoMPNN ΔΔG | 0.395 | 1.183 |
| mean REVEL | 0.257 | 0.59 |
| mean CADD phred | 21.557 | 27.092 |
| mean SIFT | -0.129 | -0.003 |
| mean PolyPhen-2 HVAR | 0.112 | 0.762 |
| mean MetaRNN | 0.449 | 0.872 |
| mean VEST4 | 0.545 | 0.841 |
| mean PROVEAN | 2.164 | 5.282 |
| **fraction seen in gnomAD** | **15.26%** (132) | **4.79%** (61) |
| fraction at the interface | 2.77% | 16.42% |

**Validation:** the damaging cluster is **depleted** in the population — 4.79% of it appears in gnomAD against 15.26% of the tolerant cluster (a 3.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 11 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 7,277**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,662 | 3,615 |
| mean AlphaMissense | 0.736 | 0.988 |
| mean ESM-1v | 9.079 | 14.9 |
| mean FoldX ΔΔG | 0.457 | 4.282 |
| mean ThermoMPNN ΔΔG | 0.365 | 1.58 |
| **fraction seen in gnomAD** | **4.59%** (168) | **1.24%** (45) |

Depletion **3.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 5.46% | 16.54% |

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
