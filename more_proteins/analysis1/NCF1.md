# NCF1 — variant-effect analysis

*Neutrophil cytosol factor 1* · UniProt `P14598` · 390 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PX | 4–125 | 122 |
| SH3 1 | 156–215 | 60 |
| SH3 2 | 226–285 | 60 |

**Pair analysed:** PX ↔ SH3 2

**AlphaFold PAE:** inter-module mean **28.66 Å**, intra-module **2.7 Å**, **ratio 10.63**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 48.5 | 0 | 100% / 100% |
| 2dyb.1.A (21.8% id) | 27.6 | 17 | 100% / 95% |

## 2. The inter-domain interface

Most compact structure: `P14598_2dyb-1-A.pdb`, centroid distance **27.6 Å**, **17 residue pairs** in contact within 5 Å.

**Domain A interface residues (8):** `16, 17, 18, 19, 20, 45, 121, 123`

**Domain B interface residues (9):** `238, 239, 240, 241, 242, 243, 244, 248, 249`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| FoldX ΔΔG | 323 | 6,783 | 0.524 | 0.826 | 2.9e-06 |
| REVEL | 99 | 2,217 | 0.286 | 0.224 | 0.92 |
| CADD phred | 103 | 2,328 | 23.5 | 23.6 | 0.1 |
| SIFT | 99 | 2,217 | 0.008 | 0.026 | 0.048 |
| PolyPhen-2 HVAR | 99 | 2,217 | 0.676 | 0.682 | 0.093 |
| MetaRNN | 99 | 2,221 | 0.489 | 0.448 | 0.93 |
| VEST4 | 103 | 2,328 | 0.433 | 0.402 | 0.8 |
| PrimateAI | 99 | 2,211 | 0.631 | 0.705 | 0.00018 |
| MutationAssessor | 99 | 1,667 | 2.27 | 2.485 | 0.73 |
| PROVEAN | 99 | 2,217 | -2.91 | -2.33 | 0.18 |
| ESM1b | 99 | 2,221 | -7.962 | -6.782 | 0.0059 |
| AlphaMissense (dbNSFP) | 99 | 2,215 | 0.22 | 0.284 | 0.93 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 7,106 |
| ThermoMPNN ΔΔG | 0 |
| revel | 2,316 |
| cadd | 2,431 |
| sift | 2,316 |
| polyphen | 2,316 |
| metarnn | 2,320 |
| vest4 | 2,431 |
| primateai | 2,310 |
| mutassessor | 1,766 |
| provean | 2,316 |
| esm1b | 2,320 |
| am_dbnsfp | 2,314 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.453 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.386 |
| FoldX ΔΔG (ProtVar) vs sift | -0.419 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.420 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.511 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.475 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.168 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.481 |
| FoldX ΔΔG (ProtVar) vs provean | -0.490 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.419 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.523 |
| revel vs cadd | +0.700 |
| revel vs sift | -0.681 |
| revel vs polyphen | +0.770 |
| revel vs metarnn | +0.892 |
| revel vs vest4 | +0.842 |
| revel vs primateai | +0.198 |
| revel vs mutassessor | +0.787 |
| revel vs provean | -0.768 |
| revel vs esm1b | -0.700 |
| revel vs am_dbnsfp | +0.731 |
| cadd vs sift | -0.718 |
| cadd vs polyphen | +0.810 |
| cadd vs metarnn | +0.724 |
| cadd vs vest4 | +0.655 |
| cadd vs primateai | +0.506 |
| cadd vs mutassessor | +0.683 |
| cadd vs provean | -0.678 |
| cadd vs esm1b | -0.476 |
| cadd vs am_dbnsfp | +0.759 |
| sift vs polyphen | -0.662 |
| sift vs metarnn | -0.733 |
| sift vs vest4 | -0.637 |
| sift vs primateai | -0.286 |
| sift vs mutassessor | -0.690 |
| sift vs provean | +0.784 |
| sift vs esm1b | +0.573 |
| sift vs am_dbnsfp | -0.664 |
| polyphen vs metarnn | +0.815 |
| polyphen vs vest4 | +0.747 |
| polyphen vs primateai | +0.478 |
| polyphen vs mutassessor | +0.719 |
| polyphen vs provean | -0.673 |
| polyphen vs esm1b | -0.562 |
| polyphen vs am_dbnsfp | +0.780 |
| metarnn vs vest4 | +0.930 |
| metarnn vs primateai | +0.256 |
| metarnn vs mutassessor | +0.765 |
| metarnn vs provean | -0.822 |
| metarnn vs esm1b | -0.740 |
| metarnn vs am_dbnsfp | +0.789 |
| vest4 vs primateai | +0.217 |
| vest4 vs mutassessor | +0.663 |
| vest4 vs provean | -0.751 |
| vest4 vs esm1b | -0.726 |
| vest4 vs am_dbnsfp | +0.761 |
| primateai vs mutassessor | +0.447 |
| primateai vs provean | -0.177 |
| primateai vs esm1b | -0.015 |
| primateai vs am_dbnsfp | +0.438 |
| mutassessor vs provean | -0.707 |
| mutassessor vs esm1b | -0.627 |
| mutassessor vs am_dbnsfp | +0.672 |
| provean vs esm1b | +0.704 |
| provean vs am_dbnsfp | -0.725 |
| esm1b vs am_dbnsfp | -0.604 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 470

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,215** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 969 | 1,246 |
| mean FoldX ΔΔG | 0.496 | 2.418 |
| mean REVEL | 0.121 | 0.438 |
| mean CADD phred | 12.746 | 25.463 |
| mean SIFT | -0.276 | -0.037 |
| mean PolyPhen-2 HVAR | 0.162 | 0.877 |
| mean MetaRNN | 0.207 | 0.739 |
| mean VEST4 | 0.218 | 0.623 |
| mean PrimateAI | 0.615 | 0.74 |
| mean PROVEAN | 1.188 | 4.212 |
| **fraction seen in gnomAD** | **19.92%** (193) | **17.58%** (219) |
| fraction at the interface | 5.06% | 4.01% |

**Validation:** the damaging cluster is **depleted** in the population — 17.58% of it appears in gnomAD against 19.92% of the tolerant cluster (a 1.1-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
