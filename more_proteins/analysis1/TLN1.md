# TLN1 — variant-effect analysis

*Talin-1* · UniProt `Q9Y490` · 2541 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| FERM | 86–403 | 318 |
| I/LWEQ | 2293–2533 | 241 |

**Pair analysed:** FERM ↔ I/LWEQ

**AlphaFold PAE:** inter-module mean **27.93 Å**, intra-module **12.9 Å**, **ratio 2.16**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 48.2 | 4 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `Q9Y490.pdb`, centroid distance **48.2 Å**, **4 residue pairs** in contact within 5 Å.

**Domain A interface residues (3):** `357, 372, 373`

**Domain B interface residues (3):** `2505, 2508, 2512`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| FoldX ΔΔG | 57 | 45,182 | 0.337 | 0.843 | 0.00014 |
| REVEL | 25 | 8,614 | 0.668 | 0.346 | 3.8e-05 |
| CADD phred | 26 | 9,040 | 27.8 | 25.3 | 0.0018 |
| SIFT | 25 | 8,614 | 0.002 | 0.016 | 0.0043 |
| PolyPhen-2 HVAR | 25 | 8,614 | 0.907 | 0.481 | 0.003 |
| MetaRNN | 25 | 8,614 | 0.81 | 0.691 | 0.011 |
| VEST4 | 26 | 9,040 | 0.748 | 0.721 | 0.53 |
| PrimateAI | 25 | 8,612 | 0.878 | 0.775 | 1.7e-09 |
| MutationAssessor | 25 | 8,612 | 2.655 | 2.2 | 0.044 |
| PROVEAN | 25 | 8,614 | -3.56 | -3.0 | 0.17 |
| ESM1b | 25 | 8,614 | -10.909 | -9.747 | 0.11 |
| AlphaMissense (dbNSFP) | 25 | 8,612 | 0.975 | 0.556 | 9.8e-07 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 45,239 |
| ThermoMPNN ΔΔG | 0 |
| revel | 8,639 |
| cadd | 9,066 |
| sift | 8,639 |
| polyphen | 8,639 |
| metarnn | 8,639 |
| vest4 | 9,066 |
| primateai | 8,637 |
| mutassessor | 8,637 |
| provean | 8,639 |
| esm1b | 8,639 |
| am_dbnsfp | 8,637 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.390 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.293 |
| FoldX ΔΔG (ProtVar) vs sift | -0.372 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.392 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.402 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.366 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.152 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.348 |
| FoldX ΔΔG (ProtVar) vs provean | -0.370 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.396 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.442 |
| revel vs cadd | +0.667 |
| revel vs sift | -0.730 |
| revel vs polyphen | +0.763 |
| revel vs metarnn | +0.876 |
| revel vs vest4 | +0.761 |
| revel vs primateai | +0.550 |
| revel vs mutassessor | +0.732 |
| revel vs provean | -0.748 |
| revel vs esm1b | -0.636 |
| revel vs am_dbnsfp | +0.732 |
| cadd vs sift | -0.717 |
| cadd vs polyphen | +0.757 |
| cadd vs metarnn | +0.728 |
| cadd vs vest4 | +0.648 |
| cadd vs primateai | +0.467 |
| cadd vs mutassessor | +0.663 |
| cadd vs provean | -0.665 |
| cadd vs esm1b | -0.643 |
| cadd vs am_dbnsfp | +0.661 |
| sift vs polyphen | -0.816 |
| sift vs metarnn | -0.755 |
| sift vs vest4 | -0.594 |
| sift vs primateai | -0.426 |
| sift vs mutassessor | -0.727 |
| sift vs provean | +0.769 |
| sift vs esm1b | +0.654 |
| sift vs am_dbnsfp | -0.702 |
| polyphen vs metarnn | +0.843 |
| polyphen vs vest4 | +0.666 |
| polyphen vs primateai | +0.528 |
| polyphen vs mutassessor | +0.789 |
| polyphen vs provean | -0.717 |
| polyphen vs esm1b | -0.674 |
| polyphen vs am_dbnsfp | +0.753 |
| metarnn vs vest4 | +0.891 |
| metarnn vs primateai | +0.582 |
| metarnn vs mutassessor | +0.771 |
| metarnn vs provean | -0.775 |
| metarnn vs esm1b | -0.702 |
| metarnn vs am_dbnsfp | +0.776 |
| vest4 vs primateai | +0.573 |
| vest4 vs mutassessor | +0.647 |
| vest4 vs provean | -0.678 |
| vest4 vs esm1b | -0.633 |
| vest4 vs am_dbnsfp | +0.705 |
| primateai vs mutassessor | +0.440 |
| primateai vs provean | -0.443 |
| primateai vs esm1b | -0.446 |
| primateai vs am_dbnsfp | +0.630 |
| mutassessor vs provean | -0.698 |
| mutassessor vs esm1b | -0.626 |
| mutassessor vs am_dbnsfp | +0.670 |
| provean vs esm1b | +0.689 |
| provean vs am_dbnsfp | -0.674 |
| esm1b vs am_dbnsfp | -0.732 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 2,603

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 8,095** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,363 | 4,732 |
| mean FoldX ΔΔG | 0.55 | 2.198 |
| mean REVEL | 0.179 | 0.548 |
| mean CADD phred | 20.606 | 27.93 |
| mean SIFT | -0.294 | -0.021 |
| mean PolyPhen-2 HVAR | 0.105 | 0.783 |
| mean MetaRNN | 0.34 | 0.813 |
| mean VEST4 | 0.461 | 0.801 |
| mean PrimateAI | 0.676 | 0.805 |
| mean PROVEAN | 1.538 | 4.441 |
| **fraction seen in gnomAD** | **22.81%** (767) | **13.82%** (654) |
| fraction at the interface | 0.03% | 0.23% |

**Validation:** the damaging cluster is **depleted** in the population — 13.82% of it appears in gnomAD against 22.81% of the tolerant cluster (a 1.7-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
