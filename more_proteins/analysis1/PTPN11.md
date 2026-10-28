# PTPN11 — variant-effect analysis

*Tyrosine-protein phosphatase non-receptor type 11* · UniProt `Q06124` · 593 aa · **reference**

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| SH2 1 | 6–102 | 97 |
| SH2 2 | 112–216 | 105 |
| Tyrosine-protein phosphatase | 247–517 | 271 |

**Pair analysed:** SH2 1 ↔ Tyrosine-protein phosphatase

**AlphaFold PAE:** inter-module mean **6.54 Å**, intra-module **3.26 Å**, **ratio 2.01**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 30.6 | 70 | 100% / 100% |
| 4DGX (X-ray, autoinhibited) | 30.3 | 64 | 100% / 94% |

## 2. The inter-domain interface

Most compact structure: `Q06124.pdb`, centroid distance **30.6 Å**, **70 residue pairs** in contact within 5 Å.

**Domain A interface residues (23):** `6, 7, 9, 10, 33, 41, 57, 58, 59, 60, 61, 62, 63, 69, 70, 71, 72, 73, 74, 75, 76, 79, 80`

**Domain B interface residues (28):** `248, 252, 255, 256, 258, 259, 262, 265, 279, 280, 281, 282, 285, 366, 425, 426, 427, 459, 460, 461, 463, 464, 465, 502, 503, 506, 507, 510`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| FoldX ΔΔG | 969 | 9,519 | 2.287 | 1.021 | 1.6e-34 |
| REVEL | 303 | 3,211 | 0.897 | 0.66 | 3.6e-41 |
| CADD phred | 327 | 3,401 | 27.9 | 25.0 | 2.9e-22 |
| SIFT | 303 | 3,211 | 0.002 | 0.024 | 1.2e-21 |
| PolyPhen-2 HVAR | 303 | 3,211 | 0.94 | 0.373 | 2.7e-26 |
| MetaRNN | 303 | 3,219 | 0.937 | 0.752 | 1.1e-47 |
| VEST4 | 327 | 3,405 | 0.892 | 0.769 | 1.1e-37 |
| PrimateAI | 298 | 3,205 | 0.883 | 0.854 | 5.9e-25 |
| MutationAssessor | 298 | 3,199 | 2.532 | 1.815 | 3.9e-13 |
| PROVEAN | 303 | 3,211 | -5.12 | -2.88 | 1.5e-36 |
| ESM1b | 257 | 2,529 | -12.169 | -10.504 | 8.8e-17 |
| AlphaMissense (dbNSFP) | 303 | 3,210 | 0.995 | 0.842 | 1.6e-51 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 10,488 |
| ThermoMPNN ΔΔG | 0 |
| revel | 3,514 |
| cadd | 3,728 |
| sift | 3,514 |
| polyphen | 3,514 |
| metarnn | 3,522 |
| vest4 | 3,732 |
| primateai | 3,503 |
| mutassessor | 3,497 |
| provean | 3,514 |
| esm1b | 2,786 |
| am_dbnsfp | 3,513 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.559 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.379 |
| FoldX ΔΔG (ProtVar) vs sift | -0.511 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.528 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.554 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.463 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.277 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.551 |
| FoldX ΔΔG (ProtVar) vs provean | -0.513 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.439 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.533 |
| revel vs cadd | +0.583 |
| revel vs sift | -0.731 |
| revel vs polyphen | +0.774 |
| revel vs metarnn | +0.904 |
| revel vs vest4 | +0.722 |
| revel vs primateai | +0.492 |
| revel vs mutassessor | +0.757 |
| revel vs provean | -0.794 |
| revel vs esm1b | -0.679 |
| revel vs am_dbnsfp | +0.749 |
| cadd vs sift | -0.666 |
| cadd vs polyphen | +0.705 |
| cadd vs metarnn | +0.644 |
| cadd vs vest4 | +0.591 |
| cadd vs primateai | +0.340 |
| cadd vs mutassessor | +0.591 |
| cadd vs provean | -0.636 |
| cadd vs esm1b | -0.584 |
| cadd vs am_dbnsfp | +0.630 |
| sift vs polyphen | -0.828 |
| sift vs metarnn | -0.763 |
| sift vs vest4 | -0.649 |
| sift vs primateai | -0.319 |
| sift vs mutassessor | -0.796 |
| sift vs provean | +0.733 |
| sift vs esm1b | +0.667 |
| sift vs am_dbnsfp | -0.730 |
| polyphen vs metarnn | +0.820 |
| polyphen vs vest4 | +0.692 |
| polyphen vs primateai | +0.389 |
| polyphen vs mutassessor | +0.797 |
| polyphen vs provean | -0.738 |
| polyphen vs esm1b | -0.660 |
| polyphen vs am_dbnsfp | +0.772 |
| metarnn vs vest4 | +0.811 |
| metarnn vs primateai | +0.460 |
| metarnn vs mutassessor | +0.803 |
| metarnn vs provean | -0.814 |
| metarnn vs esm1b | -0.664 |
| metarnn vs am_dbnsfp | +0.779 |
| vest4 vs primateai | +0.468 |
| vest4 vs mutassessor | +0.668 |
| vest4 vs provean | -0.737 |
| vest4 vs esm1b | -0.627 |
| vest4 vs am_dbnsfp | +0.747 |
| primateai vs mutassessor | +0.325 |
| primateai vs provean | -0.457 |
| primateai vs esm1b | -0.308 |
| primateai vs am_dbnsfp | +0.522 |
| mutassessor vs provean | -0.737 |
| mutassessor vs esm1b | -0.667 |
| mutassessor vs am_dbnsfp | +0.723 |
| provean vs esm1b | +0.698 |
| provean vs am_dbnsfp | -0.768 |
| esm1b vs am_dbnsfp | -0.750 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 500

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 3,262** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,290 | 1,972 |
| mean FoldX ΔΔG | 0.454 | 2.866 |
| mean REVEL | 0.437 | 0.838 |
| mean CADD phred | 20.996 | 27.741 |
| mean SIFT | -0.312 | -0.019 |
| mean PolyPhen-2 HVAR | 0.088 | 0.777 |
| mean MetaRNN | 0.451 | 0.889 |
| mean VEST4 | 0.552 | 0.85 |
| mean PrimateAI | 0.805 | 0.866 |
| mean PROVEAN | 1.448 | 5.044 |
| **fraction seen in gnomAD** | **16.67%** (215) | **10.19%** (201) |
| fraction at the interface | 2.56% | 13.44% |

**Validation:** the damaging cluster is **depleted** in the population — 10.19% of it appears in gnomAD against 16.67% of the tolerant cluster (a 1.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
