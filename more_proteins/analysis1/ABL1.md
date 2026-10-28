# ABL1 — variant-effect analysis

*Tyrosine-protein kinase ABL1* · UniProt `P00519` · 1130 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH3 | 61–121 | 61 |
| SH2 | 127–217 | 91 |
| Protein kinase | 242–493 | 252 |

**Pair analysed:** SH3 ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **8.58 Å**, intra-module **3.48 Å**, **ratio 2.46**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 34.6 | 8 | 100% / 100% |
| 1opl.1.A (99.4% id) | 34.8 | 5 | 98% / 100% |
| 1y57.1.A (43.1% id) | 37.4 | 4 | 95% / 100% |

## 2. The inter-domain interface

Most compact structure: `P00519.pdb`, centroid distance **34.6 Å**, **8 residue pairs** in contact within 5 Å.

**Domain A interface residues (6):** `74, 75, 76, 77, 96, 98`

**Domain B interface residues (3):** `263, 264, 294`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 171 | 21,299 | 0.988 | 0.555 | 5.7e-28 |
| ESM-1v | 171 | 21,299 | -9.549 | -5.501 | 1.6e-22 |
| FoldX ΔΔG | 171 | 10,450 | 0.274 | 1.017 | 1.3e-12 |
| ThermoMPNN ΔΔG | 171 | 21,299 | 0.832 | 0.192 | 2.1e-11 |
| REVEL | 54 | 6,269 | 0.524 | 0.263 | 4e-05 |
| CADD phred | 59 | 6,441 | 28.7 | 25.7 | 1.2e-06 |
| SIFT | 54 | 6,269 | 0.011 | 0.01 | 0.9 |
| PolyPhen-2 HVAR | 54 | 6,263 | 0.889 | 0.656 | 0.016 |
| MetaRNN | 54 | 6,269 | 0.765 | 0.532 | 0.0007 |
| VEST4 | 59 | 6,583 | 0.781 | 0.649 | 0.00062 |
| PrimateAI | 54 | 6,128 | 0.884 | 0.739 | 2.5e-16 |
| MutationAssessor | 54 | 6,254 | 1.16 | 1.04 | 0.84 |
| PROVEAN | 54 | 6,269 | -3.725 | -2.06 | 6.4e-07 |
| ESM1b | 54 | 6,269 | -10.305 | -5.878 | 3.7e-06 |
| AlphaMissense (dbNSFP) | 54 | 6,263 | 0.953 | 0.349 | 1.2e-07 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 21,470 |
| ESM-1v | 21,470 |
| FoldX ΔΔG (ProtVar) | 10,621 |
| ThermoMPNN ΔΔG | 21,470 |
| revel | 6,323 |
| cadd | 6,500 |
| sift | 6,323 |
| polyphen | 6,317 |
| metarnn | 6,323 |
| vest4 | 6,642 |
| primateai | 6,182 |
| mutassessor | 6,308 |
| provean | 6,323 |
| esm1b | 6,323 |
| am_dbnsfp | 6,317 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.742 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.486 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.571 |
| AlphaMissense vs revel | +0.836 |
| AlphaMissense vs cadd | +0.777 |
| AlphaMissense vs sift | -0.622 |
| AlphaMissense vs polyphen | +0.721 |
| AlphaMissense vs metarnn | +0.857 |
| AlphaMissense vs vest4 | +0.849 |
| AlphaMissense vs primateai | +0.842 |
| AlphaMissense vs mutassessor | +0.619 |
| AlphaMissense vs provean | -0.789 |
| AlphaMissense vs esm1b | -0.773 |
| AlphaMissense vs am_dbnsfp | +0.981 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.483 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.541 |
| ESM-1v vs revel | -0.695 |
| ESM-1v vs cadd | -0.633 |
| ESM-1v vs sift | +0.487 |
| ESM-1v vs polyphen | -0.566 |
| ESM-1v vs metarnn | -0.689 |
| ESM-1v vs vest4 | -0.644 |
| ESM-1v vs primateai | -0.673 |
| ESM-1v vs mutassessor | -0.515 |
| ESM-1v vs provean | +0.730 |
| ESM-1v vs esm1b | +0.881 |
| ESM-1v vs am_dbnsfp | -0.718 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.683 |
| FoldX ΔΔG (ProtVar) vs revel | +0.442 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.257 |
| FoldX ΔΔG (ProtVar) vs sift | -0.368 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.425 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.485 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.434 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.305 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.431 |
| FoldX ΔΔG (ProtVar) vs provean | -0.413 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.418 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.464 |
| ThermoMPNN ΔΔG vs revel | +0.557 |
| ThermoMPNN ΔΔG vs cadd | +0.472 |
| ThermoMPNN ΔΔG vs sift | -0.327 |
| ThermoMPNN ΔΔG vs polyphen | +0.401 |
| ThermoMPNN ΔΔG vs metarnn | +0.560 |
| ThermoMPNN ΔΔG vs vest4 | +0.536 |
| ThermoMPNN ΔΔG vs primateai | +0.536 |
| ThermoMPNN ΔΔG vs mutassessor | +0.425 |
| ThermoMPNN ΔΔG vs provean | -0.530 |
| ThermoMPNN ΔΔG vs esm1b | -0.543 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.556 |
| revel vs cadd | +0.815 |
| revel vs sift | -0.601 |
| revel vs polyphen | +0.755 |
| revel vs metarnn | +0.922 |
| revel vs vest4 | +0.856 |
| revel vs primateai | +0.841 |
| revel vs mutassessor | +0.611 |
| revel vs provean | -0.785 |
| revel vs esm1b | -0.738 |
| revel vs am_dbnsfp | +0.845 |
| cadd vs sift | -0.653 |
| cadd vs polyphen | +0.740 |
| cadd vs metarnn | +0.836 |
| cadd vs vest4 | +0.816 |
| cadd vs primateai | +0.770 |
| cadd vs mutassessor | +0.641 |
| cadd vs provean | -0.772 |
| cadd vs esm1b | -0.695 |
| cadd vs am_dbnsfp | +0.789 |
| sift vs polyphen | -0.728 |
| sift vs metarnn | -0.679 |
| sift vs vest4 | -0.643 |
| sift vs primateai | -0.485 |
| sift vs mutassessor | -0.608 |
| sift vs provean | +0.619 |
| sift vs esm1b | +0.497 |
| sift vs am_dbnsfp | -0.634 |
| polyphen vs metarnn | +0.824 |
| polyphen vs vest4 | +0.783 |
| polyphen vs primateai | +0.665 |
| polyphen vs mutassessor | +0.634 |
| polyphen vs provean | -0.654 |
| polyphen vs esm1b | -0.582 |
| polyphen vs am_dbnsfp | +0.739 |
| metarnn vs vest4 | +0.946 |
| metarnn vs primateai | +0.851 |
| metarnn vs mutassessor | +0.647 |
| metarnn vs provean | -0.794 |
| metarnn vs esm1b | -0.736 |
| metarnn vs am_dbnsfp | +0.877 |
| vest4 vs primateai | +0.836 |
| vest4 vs mutassessor | +0.621 |
| vest4 vs provean | -0.771 |
| vest4 vs esm1b | -0.701 |
| vest4 vs am_dbnsfp | +0.866 |
| primateai vs mutassessor | +0.547 |
| primateai vs provean | -0.747 |
| primateai vs esm1b | -0.729 |
| primateai vs am_dbnsfp | +0.849 |
| mutassessor vs provean | -0.605 |
| mutassessor vs esm1b | -0.532 |
| mutassessor vs am_dbnsfp | +0.624 |
| provean vs esm1b | +0.781 |
| provean vs am_dbnsfp | -0.788 |
| esm1b vs am_dbnsfp | -0.771 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 113 |
| likely_benign | 103 |
| benign | 39 |
| likely_pathogenic | 35 |
| conflict | 11 |
| pathogenic | 4 |

**gnomAD r4 missense variants mapped:** 1,217

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,164** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,195 | 1,969 |
| mean AlphaMissense | 0.403 | 0.928 |
| mean ESM-1v | 5.112 | 11.111 |
| mean FoldX ΔΔG | 0.359 | 2.226 |
| mean ThermoMPNN ΔΔG | 0.343 | 1.284 |
| mean REVEL | 0.318 | 0.705 |
| mean CADD phred | 24.953 | 29.969 |
| mean SIFT | -0.117 | -0.011 |
| mean PolyPhen-2 HVAR | 0.431 | 0.908 |
| mean MetaRNN | 0.539 | 0.892 |
| mean VEST4 | 0.603 | 0.87 |
| mean PrimateAI | 0.761 | 0.874 |
| mean PROVEAN | 2.286 | 5.662 |
| **fraction seen in gnomAD** | **18.58%** (222) | **8.28%** (163) |
| fraction at the interface | 1.67% | 1.73% |

**Validation:** the damaging cluster is **depleted** in the population — 8.28% of it appears in gnomAD against 18.58% of the tolerant cluster (a 2.2-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 3 pathogenic / 1 benign, cluster 0 has 0 / 4; OR = inf, p = 0.14.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 10,621**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 4,891 | 5,730 |
| mean AlphaMissense | 0.619 | 0.985 |
| mean ESM-1v | 6.307 | 13.799 |
| mean FoldX ΔΔG | 0.307 | 3.117 |
| mean ThermoMPNN ΔΔG | 0.331 | 1.624 |
| **fraction seen in gnomAD** | **6.36%** (311) | **1.59%** (91) |

Depletion **4.0×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 1.82% | 1.43% |

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
