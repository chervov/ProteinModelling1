# TAP1 — variant-effect analysis

*Antigen peptide transporter 1* · UniProt `Q03518` · 748 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| ABC transmembrane type-1 | 187–470 | 284 |
| ABC transporter | 503–742 | 240 |

**Pair analysed:** ABC transmembrane type-1 ↔ ABC transporter

**AlphaFold PAE:** inter-module mean **13.88 Å**, intra-module **6.25 Å**, **ratio 2.22**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 58.7 | 10 | 100% / 100% |
| 9h8o.1.A (29.2% id) | 54.2 | 20 | 100% / 100% |
| 9n62.1.A (100.0% id) | 62.6 | 8 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q03518_9h8o-1-A.pdb`, centroid distance **54.2 Å**, **20 residue pairs** in contact within 5 Å.

**Domain A interface residues (11):** `258, 261, 265, 269, 270, 277, 281, 282, 284, 289, 290`

**Domain B interface residues (13):** `555, 575, 589, 590, 591, 592, 593, 597, 601, 635, 637, 638, 639`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| AlphaMissense | 456 | 13,756 | 0.289 | 0.298 | 0.86 |
| ESM-1v | 456 | 13,756 | -8.571 | -7.001 | 8.8e-17 |
| FoldX ΔΔG | 456 | 12,996 | 1.013 | 0.623 | 7.6e-09 |
| ThermoMPNN ΔΔG | 456 | 13,756 | 0.522 | 0.579 | 0.24 |
| REVEL | 29 | 328 | 0.312 | 0.442 | 0.02 |
| CADD phred | 30 | 344 | 19.335 | 23.8 | 0.03 |
| SIFT | 29 | 328 | 0.105 | 0.004 | 2.1e-05 |
| PolyPhen-2 HVAR | 29 | 328 | 0.324 | 0.742 | 0.14 |
| MetaRNN | 29 | 328 | 0.398 | 0.445 | 0.9 |
| VEST4 | 30 | 344 | 0.242 | 0.356 | 0.1 |
| PrimateAI | 29 | 322 | 0.334 | 0.514 | 1e-10 |
| MutationAssessor | 29 | 322 | 2.25 | 1.823 | 0.052 |
| PROVEAN | 29 | 328 | -2.98 | -1.985 | 0.16 |
| ESM1b | 29 | 328 | -6.847 | -6.541 | 0.73 |
| AlphaMissense (dbNSFP) | 29 | 322 | 0.136 | 0.144 | 0.46 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 14,212 |
| ESM-1v | 14,212 |
| FoldX ΔΔG (ProtVar) | 13,452 |
| ThermoMPNN ΔΔG | 14,212 |
| revel | 357 |
| cadd | 374 |
| sift | 357 |
| polyphen | 357 |
| metarnn | 357 |
| vest4 | 374 |
| primateai | 351 |
| mutassessor | 351 |
| provean | 357 |
| esm1b | 357 |
| am_dbnsfp | 351 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.734 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.363 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.429 |
| AlphaMissense vs revel | +0.648 |
| AlphaMissense vs cadd | +0.588 |
| AlphaMissense vs sift | -0.445 |
| AlphaMissense vs polyphen | +0.520 |
| AlphaMissense vs metarnn | +0.640 |
| AlphaMissense vs vest4 | +0.670 |
| AlphaMissense vs primateai | +0.186 |
| AlphaMissense vs mutassessor | +0.454 |
| AlphaMissense vs provean | -0.596 |
| AlphaMissense vs esm1b | -0.584 |
| AlphaMissense vs am_dbnsfp | +0.876 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.387 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.491 |
| ESM-1v vs revel | -0.608 |
| ESM-1v vs cadd | -0.520 |
| ESM-1v vs sift | +0.469 |
| ESM-1v vs polyphen | -0.509 |
| ESM-1v vs metarnn | -0.645 |
| ESM-1v vs vest4 | -0.579 |
| ESM-1v vs primateai | -0.005 |
| ESM-1v vs mutassessor | -0.524 |
| ESM-1v vs provean | +0.616 |
| ESM-1v vs esm1b | +0.817 |
| ESM-1v vs am_dbnsfp | -0.586 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.661 |
| FoldX ΔΔG (ProtVar) vs revel | +0.409 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.253 |
| FoldX ΔΔG (ProtVar) vs sift | -0.332 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.294 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.397 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.371 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.219 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.240 |
| FoldX ΔΔG (ProtVar) vs provean | -0.437 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.356 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.397 |
| ThermoMPNN ΔΔG vs revel | +0.508 |
| ThermoMPNN ΔΔG vs cadd | +0.376 |
| ThermoMPNN ΔΔG vs sift | -0.402 |
| ThermoMPNN ΔΔG vs polyphen | +0.398 |
| ThermoMPNN ΔΔG vs metarnn | +0.483 |
| ThermoMPNN ΔΔG vs vest4 | +0.498 |
| ThermoMPNN ΔΔG vs primateai | +0.246 |
| ThermoMPNN ΔΔG vs mutassessor | +0.351 |
| ThermoMPNN ΔΔG vs provean | -0.505 |
| ThermoMPNN ΔΔG vs esm1b | -0.399 |
| ThermoMPNN ΔΔG vs am_dbnsfp | +0.404 |
| revel vs cadd | +0.849 |
| revel vs sift | -0.447 |
| revel vs polyphen | +0.841 |
| revel vs metarnn | +0.926 |
| revel vs vest4 | +0.905 |
| revel vs primateai | +0.115 |
| revel vs mutassessor | +0.718 |
| revel vs provean | -0.803 |
| revel vs esm1b | -0.709 |
| revel vs am_dbnsfp | +0.737 |
| cadd vs sift | -0.398 |
| cadd vs polyphen | +0.789 |
| cadd vs metarnn | +0.818 |
| cadd vs vest4 | +0.817 |
| cadd vs primateai | +0.115 |
| cadd vs mutassessor | +0.628 |
| cadd vs provean | -0.734 |
| cadd vs esm1b | -0.635 |
| cadd vs am_dbnsfp | +0.704 |
| sift vs polyphen | -0.435 |
| sift vs metarnn | -0.407 |
| sift vs vest4 | -0.421 |
| sift vs primateai | -0.425 |
| sift vs mutassessor | -0.260 |
| sift vs provean | +0.392 |
| sift vs esm1b | +0.375 |
| sift vs am_dbnsfp | -0.373 |
| polyphen vs metarnn | +0.825 |
| polyphen vs vest4 | +0.809 |
| polyphen vs primateai | +0.160 |
| polyphen vs mutassessor | +0.683 |
| polyphen vs provean | -0.700 |
| polyphen vs esm1b | -0.639 |
| polyphen vs am_dbnsfp | +0.675 |
| metarnn vs vest4 | +0.900 |
| metarnn vs primateai | +0.034 |
| metarnn vs mutassessor | +0.766 |
| metarnn vs provean | -0.843 |
| metarnn vs esm1b | -0.760 |
| metarnn vs am_dbnsfp | +0.733 |
| vest4 vs primateai | +0.149 |
| vest4 vs mutassessor | +0.709 |
| vest4 vs provean | -0.797 |
| vest4 vs esm1b | -0.685 |
| vest4 vs am_dbnsfp | +0.769 |
| primateai vs mutassessor | -0.048 |
| primateai vs provean | +0.061 |
| primateai vs esm1b | +0.114 |
| primateai vs am_dbnsfp | +0.163 |
| mutassessor vs provean | -0.704 |
| mutassessor vs esm1b | -0.663 |
| mutassessor vs am_dbnsfp | +0.608 |
| provean vs esm1b | +0.723 |
| provean vs am_dbnsfp | -0.671 |
| esm1b vs am_dbnsfp | -0.687 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

| ClinVar significance | n |
|---|--:|
| VUS | 150 |
| benign | 9 |
| likely_benign | 6 |
| conflict | 5 |

**gnomAD r4 missense variants mapped:** 802

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 283** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 139 | 144 |
| mean AlphaMissense | 0.154 | 0.377 |
| mean ESM-1v | 5.222 | 8.571 |
| mean FoldX ΔΔG | 0.465 | 2.662 |
| mean ThermoMPNN ΔΔG | 0.539 | 1.348 |
| mean REVEL | 0.311 | 0.749 |
| mean CADD phred | 15.932 | 26.681 |
| mean SIFT | -0.198 | -0.018 |
| mean PolyPhen-2 HVAR | 0.308 | 0.931 |
| mean MetaRNN | 0.3 | 0.868 |
| mean VEST4 | 0.241 | 0.648 |
| mean PrimateAI | 0.415 | 0.493 |
| mean PROVEAN | 1.531 | 4.683 |
| **fraction seen in gnomAD** | **20.14%** (28) | **11.81%** (17) |
| fraction at the interface | 14.39% | 6.25% |

**Validation:** the damaging cluster is **depleted** in the population — 11.81% of it appears in gnomAD against 20.14% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


### The same split on all variants, using only the four full-coverage features

The table above uses 12 features and is therefore restricted to variants dbNSFP scores — i.e. those reachable by a single nucleotide change. Repeating the split with only **AlphaMissense, ESM-1v, FoldX ΔΔG and ThermoMPNN ΔΔG**, which score every substitution, gives **n = 13,452**:

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,895 | 4,557 |
| mean AlphaMissense | 0.249 | 0.671 |
| mean ESM-1v | 5.98 | 11.545 |
| mean FoldX ΔΔG | 0.366 | 3.424 |
| mean ThermoMPNN ΔΔG | 0.406 | 1.618 |
| **fraction seen in gnomAD** | **5.03%** (447) | **5.09%** (232) |

Depletion **1.0×**. The two splits should be read together: the 12-feature one uses richer evidence on a third of the variants, the 4-feature one uses weaker evidence on all of them.
| fraction at the interface | 3.11% | 3.93% |

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
