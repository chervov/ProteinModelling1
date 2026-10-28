# ACTN4 — variant-effect analysis

*Alpha-actinin-4* · UniProt `O43707` · 911 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Calponin-homology (CH) 1 | 50–154 | 105 |
| Calponin-homology (CH) 2 | 163–269 | 107 |
| EF-hand 1 | 765–800 | 36 |
| EF-hand 2 | 806–841 | 36 |

**Pair analysed:** Calponin-homology (CH) 1 ↔ Calponin-homology (CH) 2

**AlphaFold PAE:** inter-module mean **6.44 Å**, intra-module **3.03 Å**, **ratio 2.13**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 27.0 | 38 | 100% / 100% |
| SWISSMODEL_1sjj-1-A_44-911 | 46.0 | 0 | 100% / 100% |
| SWISSMODEL_6sl3-1-B_48-483 | 27.3 | 33 | 100% / 100% |
| SWISSMODEL_6sl7-1-B_48-483 | 26.7 | 38 | 100% / 100% |
| SWISSMODEL_7ank-1-A_47-519 | 26.5 | 46 | 100% / 100% |
| SWISSMODEL_9sis-1-B_46-909 | 26.9 | 45 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `ACTN4_O43707_SWISSMODEL_7ank-1-A_47-519.pdb`, centroid distance **26.5 Å**, **46 residue pairs** in contact within 5 Å.

**Domain A interface residues (16):** `50, 51, 52, 54, 55, 56, 58, 59, 62, 65, 144, 147, 150, 151, 153, 154`

**Domain B interface residues (21):** `165, 236, 238, 239, 240, 241, 242, 245, 246, 249, 251, 252, 253, 255, 256, 258, 259, 260, 262, 263, 266`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 703 | 16,606 | 0.998 | 0.905 | 3e-146 |
| ESM-1v | 703 | 16,606 | -16.638 | -14.806 | 8.3e-54 |
| FoldX ΔΔG | 703 | 15,751 | 1.844 | 0.907 | 3.6e-17 |
| ThermoMPNN ΔΔG | 703 | 16,606 | 1.103 | 0.572 | 1.6e-29 |
| REVEL | 220 | 5,259 | 0.906 | 0.441 | 8e-72 |
| CADD phred | 230 | 5,524 | 29.0 | 25.7 | 1.3e-17 |
| SIFT | 220 | 5,259 | 0.001 | 0.008 | 4e-21 |
| PolyPhen-2 HVAR | 220 | 5,259 | 0.98 | 0.618 | 8.3e-26 |
| MetaRNN | 220 | 5,261 | 0.945 | 0.762 | 3.9e-43 |
| VEST4 | 230 | 5,521 | 0.861 | 0.74 | 5.6e-22 |
| PrimateAI | 220 | 5,253 | 0.891 | 0.799 | 3e-65 |
| MutationAssessor | 220 | 5,253 | 2.868 | 2.455 | 3e-10 |
| PROVEAN | 220 | 5,259 | -4.47 | -3.47 | 2.5e-13 |
| ESM1b | 220 | 5,259 | -14.291 | -12.327 | 4e-16 |
| AlphaMissense (dbNSFP) | 220 | 5,255 | 0.992 | 0.731 | 7.3e-49 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 17,309 |
| ESM-1v | 17,309 |
| FoldX ΔΔG (ProtVar) | 16,454 |
| ThermoMPNN ΔΔG | 17,309 |
| revel | 5,479 |
| cadd | 5,754 |
| sift | 5,479 |
| polyphen | 5,479 |
| metarnn | 5,481 |
| vest4 | 5,751 |
| primateai | 5,473 |
| mutassessor | 5,473 |
| provean | 5,479 |
| esm1b | 5,479 |
| am_dbnsfp | 5,475 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.762 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.445 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.487 |
| AlphaMissense vs revel | +0.784 |
| AlphaMissense vs cadd | +0.690 |
| AlphaMissense vs sift | -0.697 |
| AlphaMissense vs polyphen | +0.761 |
| AlphaMissense vs metarnn | +0.792 |
| AlphaMissense vs vest4 | +0.738 |
| AlphaMissense vs primateai | +0.641 |
| AlphaMissense vs mutassessor | +0.664 |
| AlphaMissense vs provean | -0.688 |
| AlphaMissense vs esm1b | -0.714 |
| AlphaMissense vs am_dbnsfp | +1.000 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.353 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.421 |
| ESM-1v vs revel | -0.675 |
| ESM-1v vs cadd | -0.638 |
| ESM-1v vs sift | +0.650 |
| ESM-1v vs polyphen | -0.679 |
| ESM-1v vs metarnn | -0.723 |
| ESM-1v vs vest4 | -0.706 |
| ESM-1v vs primateai | -0.409 |
| ESM-1v vs mutassessor | -0.641 |
| ESM-1v vs provean | +0.709 |
| ESM-1v vs esm1b | +0.816 |
| ESM-1v vs am_dbnsfp | -0.756 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.713 |
| FoldX ΔΔG (ProtVar) vs revel | +0.393 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.326 |
| FoldX ΔΔG (ProtVar) vs sift | -0.411 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.457 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.463 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.418 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.222 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.427 |
| FoldX ΔΔG (ProtVar) vs provean | -0.397 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.403 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.457 |
| ThermoMPNN ΔΔG vs revel | +0.442 |
| ThermoMPNN ΔΔG vs cadd | +0.373 |
| ThermoMPNN ΔΔG vs sift | -0.463 |
| ThermoMPNN ΔΔG vs polyphen | +0.498 |
| ThermoMPNN ΔΔG vs metarnn | +0.513 |
| ThermoMPNN ΔΔG vs vest4 | +0.478 |
| ThermoMPNN ΔΔG vs primateai | +0.187 |
| ThermoMPNN ΔΔG vs mutassessor | +0.506 |
| ThermoMPNN ΔΔG vs provean | -0.430 |
| ThermoMPNN ΔΔG vs esm1b | -0.508 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.504 |
| revel vs cadd | +0.725 |
| revel vs sift | -0.727 |
| revel vs polyphen | +0.753 |
| revel vs metarnn | +0.888 |
| revel vs vest4 | +0.732 |
| revel vs primateai | +0.638 |
| revel vs mutassessor | +0.657 |
| revel vs provean | -0.683 |
| revel vs esm1b | -0.626 |
| revel vs am_dbnsfp | +0.784 |
| cadd vs sift | -0.736 |
| cadd vs polyphen | +0.761 |
| cadd vs metarnn | +0.765 |
| cadd vs vest4 | +0.694 |
| cadd vs primateai | +0.484 |
| cadd vs mutassessor | +0.655 |
| cadd vs provean | -0.655 |
| cadd vs esm1b | -0.596 |
| cadd vs am_dbnsfp | +0.690 |
| sift vs polyphen | -0.809 |
| sift vs metarnn | -0.775 |
| sift vs vest4 | -0.627 |
| sift vs primateai | -0.419 |
| sift vs mutassessor | -0.725 |
| sift vs provean | +0.690 |
| sift vs esm1b | +0.628 |
| sift vs am_dbnsfp | -0.698 |
| polyphen vs metarnn | +0.839 |
| polyphen vs vest4 | +0.725 |
| polyphen vs primateai | +0.465 |
| polyphen vs mutassessor | +0.784 |
| polyphen vs provean | -0.711 |
| polyphen vs esm1b | -0.645 |
| polyphen vs am_dbnsfp | +0.762 |
| metarnn vs vest4 | +0.828 |
| metarnn vs primateai | +0.565 |
| metarnn vs mutassessor | +0.786 |
| metarnn vs provean | -0.748 |
| metarnn vs esm1b | -0.667 |
| metarnn vs am_dbnsfp | +0.794 |
| vest4 vs primateai | +0.501 |
| vest4 vs mutassessor | +0.700 |
| vest4 vs provean | -0.679 |
| vest4 vs esm1b | -0.641 |
| vest4 vs am_dbnsfp | +0.738 |
| primateai vs mutassessor | +0.330 |
| primateai vs provean | -0.382 |
| primateai vs esm1b | -0.355 |
| primateai vs am_dbnsfp | +0.641 |
| mutassessor vs provean | -0.676 |
| mutassessor vs esm1b | -0.624 |
| mutassessor vs am_dbnsfp | +0.664 |
| provean vs esm1b | +0.665 |
| provean vs am_dbnsfp | -0.688 |
| esm1b vs am_dbnsfp | -0.715 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 76 |
| likely_benign | 12 |
| likely_pathogenic | 6 |
| other | 5 |
| pathogenic | 5 |
| conflict | 5 |
| benign | 2 |

**gnomAD r4 missense variants mapped:** 859

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 5,207** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,934 | 3,273 |
| mean AlphaMissense | 0.291 | 0.86 |
| mean ESM-1v | 10.445 | 14.081 |
| mean FoldX ΔΔG | 0.453 | 2.205 |
| mean ThermoMPNN ΔΔG | 0.342 | 1.108 |
| mean REVEL | 0.238 | 0.664 |
| mean CADD phred | 20.925 | 28.326 |
| mean SIFT | -0.224 | -0.015 |
| mean PolyPhen-2 HVAR | 0.137 | 0.814 |
| mean MetaRNN | 0.409 | 0.861 |
| mean VEST4 | 0.494 | 0.811 |
| mean PrimateAI | 0.673 | 0.825 |
| mean PROVEAN | 1.841 | 4.968 |
| **fraction seen in gnomAD** | **19.96%** (386) | **11.89%** (389) |
| fraction at the interface | 1.03% | 6.11% |

**Validation:** the damaging cluster is **depleted** in the population — 11.89% of it appears in gnomAD against 19.96% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 16,454**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 5,866 | 10,588 |
| mean AlphaMissense | 0.398 | 0.945 |
| mean ESM-1v | 11.889 | 16.416 |
| mean FoldX ΔΔG | 0.401 | 2.613 |
| mean ThermoMPNN ΔΔG | 0.309 | 1.212 |
| **fraction seen in gnomAD** | **9.41%** (552) | **2.27%** (240) |

Depletion **4.1×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 0.99% | 6.09% |

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
