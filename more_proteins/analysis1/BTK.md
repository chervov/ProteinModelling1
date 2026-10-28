# BTK — variant-effect analysis

*Tyrosine-protein kinase BTK* · UniProt `Q06187` · 659 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PH | 3–133 | 131 |
| SH3 | 214–274 | 61 |
| SH2 | 281–377 | 97 |
| Protein kinase | 402–655 | 254 |

**Pair analysed:** PH ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **26.38 Å**, intra-module **5.1 Å**, **ratio 5.17**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 43.0 | 3 | 100% / 100% |
| 8s93.1.A (92.3% id) | 44.4 | 14 | 100% / 100% |
| 4y93.1.A (96.0% id) | 39.5 | 13 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q06187_8s93-1-A.pdb`, centroid distance **44.4 Å**, **14 residue pairs** in contact within 5 Å.

**Domain A interface residues (9):** `3, 5, 34, 35, 58, 59, 130, 131, 133`

**Domain B interface residues (5):** `421, 422, 424, 425, 461`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 266 | 12,255 | 0.485 | 0.902 | 1.1e-24 |
| ESM-1v | 266 | 12,255 | -8.356 | -9.833 | 8.4e-10 |
| FoldX ΔΔG | 266 | 11,514 | 0.618 | 1.205 | 7.1e-09 |
| ThermoMPNN ΔΔG | 266 | 12,255 | 0.696 | 0.836 | 0.024 |
| REVEL | 82 | 3,772 | 0.465 | 0.635 | 0.00026 |
| CADD phred | 88 | 4,018 | 22.75 | 24.5 | 9.8e-05 |
| SIFT | 82 | 3,772 | 0.091 | 0.018 | 0.00013 |
| PolyPhen-2 HVAR | 82 | 3,772 | 0.208 | 0.841 | 1.9e-07 |
| MetaRNN | 82 | 3,778 | 0.526 | 0.737 | 1.8e-05 |
| VEST4 | 88 | 4,011 | 0.412 | 0.584 | 5.5e-05 |
| PrimateAI | 82 | 3,766 | 0.721 | 0.744 | 0.27 |
| MutationAssessor | 82 | 3,766 | 1.212 | 1.87 | 0.00063 |
| PROVEAN | 82 | 3,772 | -1.94 | -2.76 | 0.012 |
| ESM1b | 82 | 3,778 | -9.835 | -10.164 | 0.2 |
| AlphaMissense (dbNSFP) | 82 | 3,778 | 0.276 | 0.66 | 6e-06 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 12,521 |
| ESM-1v | 12,521 |
| FoldX ΔΔG (ProtVar) | 11,780 |
| ThermoMPNN ΔΔG | 12,521 |
| revel | 3,854 |
| cadd | 4,106 |
| sift | 3,854 |
| polyphen | 3,854 |
| metarnn | 3,860 |
| vest4 | 4,099 |
| primateai | 3,848 |
| mutassessor | 3,848 |
| provean | 3,854 |
| esm1b | 3,860 |
| am_dbnsfp | 3,860 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.867 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.537 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.563 |
| AlphaMissense vs revel | +0.826 |
| AlphaMissense vs cadd | +0.769 |
| AlphaMissense vs sift | -0.701 |
| AlphaMissense vs polyphen | +0.778 |
| AlphaMissense vs metarnn | +0.840 |
| AlphaMissense vs vest4 | +0.819 |
| AlphaMissense vs primateai | +0.640 |
| AlphaMissense vs mutassessor | +0.746 |
| AlphaMissense vs provean | -0.782 |
| AlphaMissense vs esm1b | -0.774 |
| AlphaMissense vs am_dbnsfp | +0.982 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.502 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.547 |
| ESM-1v vs revel | -0.815 |
| ESM-1v vs cadd | -0.754 |
| ESM-1v vs sift | +0.747 |
| ESM-1v vs polyphen | -0.741 |
| ESM-1v vs metarnn | -0.842 |
| ESM-1v vs vest4 | -0.799 |
| ESM-1v vs primateai | -0.587 |
| ESM-1v vs mutassessor | -0.778 |
| ESM-1v vs provean | +0.826 |
| ESM-1v vs esm1b | +0.878 |
| ESM-1v vs am_dbnsfp | -0.837 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.703 |
| FoldX ΔΔG (ProtVar) vs revel | +0.468 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.410 |
| FoldX ΔΔG (ProtVar) vs sift | -0.417 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.455 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.493 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.493 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.328 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.459 |
| FoldX ΔΔG (ProtVar) vs provean | -0.466 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.450 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.523 |
| ThermoMPNN ΔΔG vs revel | +0.498 |
| ThermoMPNN ΔΔG vs cadd | +0.424 |
| ThermoMPNN ΔΔG vs sift | -0.460 |
| ThermoMPNN ΔΔG vs polyphen | +0.469 |
| ThermoMPNN ΔΔG vs metarnn | +0.539 |
| ThermoMPNN ΔΔG vs vest4 | +0.529 |
| ThermoMPNN ΔΔG vs primateai | +0.354 |
| ThermoMPNN ΔΔG vs mutassessor | +0.547 |
| ThermoMPNN ΔΔG vs provean | -0.492 |
| ThermoMPNN ΔΔG vs esm1b | -0.519 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.559 |
| revel vs cadd | +0.801 |
| revel vs sift | -0.752 |
| revel vs polyphen | +0.828 |
| revel vs metarnn | +0.911 |
| revel vs vest4 | +0.832 |
| revel vs primateai | +0.663 |
| revel vs mutassessor | +0.778 |
| revel vs provean | -0.818 |
| revel vs esm1b | -0.742 |
| revel vs am_dbnsfp | +0.819 |
| cadd vs sift | -0.724 |
| cadd vs polyphen | +0.774 |
| cadd vs metarnn | +0.798 |
| cadd vs vest4 | +0.756 |
| cadd vs primateai | +0.538 |
| cadd vs mutassessor | +0.694 |
| cadd vs provean | -0.770 |
| cadd vs esm1b | -0.678 |
| cadd vs am_dbnsfp | +0.755 |
| sift vs polyphen | -0.693 |
| sift vs metarnn | -0.755 |
| sift vs vest4 | -0.668 |
| sift vs primateai | -0.470 |
| sift vs mutassessor | -0.700 |
| sift vs provean | +0.764 |
| sift vs esm1b | +0.673 |
| sift vs am_dbnsfp | -0.685 |
| polyphen vs metarnn | +0.824 |
| polyphen vs vest4 | +0.769 |
| polyphen vs primateai | +0.624 |
| polyphen vs mutassessor | +0.706 |
| polyphen vs provean | -0.745 |
| polyphen vs esm1b | -0.653 |
| polyphen vs am_dbnsfp | +0.776 |
| metarnn vs vest4 | +0.923 |
| metarnn vs primateai | +0.667 |
| metarnn vs mutassessor | +0.776 |
| metarnn vs provean | -0.822 |
| metarnn vs esm1b | -0.762 |
| metarnn vs am_dbnsfp | +0.836 |
| vest4 vs primateai | +0.647 |
| vest4 vs mutassessor | +0.705 |
| vest4 vs provean | -0.758 |
| vest4 vs esm1b | -0.716 |
| vest4 vs am_dbnsfp | +0.815 |
| primateai vs mutassessor | +0.507 |
| primateai vs provean | -0.548 |
| primateai vs esm1b | -0.529 |
| primateai vs am_dbnsfp | +0.637 |
| mutassessor vs provean | -0.721 |
| mutassessor vs esm1b | -0.692 |
| mutassessor vs am_dbnsfp | +0.742 |
| provean vs esm1b | +0.751 |
| provean vs am_dbnsfp | -0.769 |
| esm1b vs am_dbnsfp | -0.772 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 266

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,615** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,551 | 2,064 |
| mean AlphaMissense | 0.282 | 0.89 |
| mean ESM-1v | 5.575 | 11.164 |
| mean FoldX ΔΔG | 0.538 | 2.875 |
| mean ThermoMPNN ΔΔG | 0.471 | 1.426 |
| mean REVEL | 0.362 | 0.809 |
| mean CADD phred | 17.596 | 26.482 |
| mean SIFT | -0.275 | -0.024 |
| mean PolyPhen-2 HVAR | 0.284 | 0.912 |
| mean MetaRNN | 0.413 | 0.888 |
| mean VEST4 | 0.362 | 0.744 |
| mean PrimateAI | 0.65 | 0.791 |
| mean PROVEAN | 1.3 | 4.96 |
| **fraction seen in gnomAD** | **9.41%** (146) | **4.17%** (86) |
| fraction at the interface | 3.48% | 1.36% |

**Validation:** the damaging cluster is **depleted** in the population — 4.17% of it appears in gnomAD against 9.41% of the tolerant cluster (a 2.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 11,780**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 5,108 | 6,672 |
| mean AlphaMissense | 0.437 | 0.96 |
| mean ESM-1v | 6.62 | 12.993 |
| mean FoldX ΔΔG | 0.491 | 3.534 |
| mean ThermoMPNN ΔΔG | 0.446 | 1.652 |
| **fraction seen in gnomAD** | **3.45%** (176) | **0.94%** (63) |

Depletion **3.7×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.43% | 1.36% |

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
