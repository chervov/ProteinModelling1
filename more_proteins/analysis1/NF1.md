# NF1 — variant-effect analysis

*Neurofibromin* · UniProt `P21359` · 2839 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Ras-GAP | 1251–1482 | 232 |
| CRAL-TRIO | 1580–1738 | 159 |

**Pair analysed:** Ras-GAP ↔ CRAL-TRIO

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| 7r03.1.A (100.0% id) | 42.0 | 1 | 100% / 100% |
| 7r04.1.A (100.0% id) | 74.1 | 0 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `P21359_7r03-1-A.pdb`, centroid distance **42.0 Å**, **1 residue pairs** in contact within 5 Å.

**Domain A interface residues (1):** `1428`

**Domain B interface residues (1):** `1669`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| FoldX ΔΔG | 40 | 84,203 | 0.679 | 1.041 | 0.83 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 84,243 |
| ThermoMPNN ΔΔG | 0 |
| revel | 8,211 |
| cadd | 8,753 |
| sift | 8,211 |
| polyphen | 8,203 |
| metarnn | 8,273 |
| vest4 | 8,689 |
| primateai | 8,202 |
| mutassessor | 8,200 |
| provean | 8,211 |
| esm1b | 8,209 |
| am_dbnsfp | 8,271 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.097 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.085 |
| FoldX ΔΔG (ProtVar) vs sift | -0.075 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.080 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.125 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.131 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.054 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.085 |
| FoldX ΔΔG (ProtVar) vs provean | -0.106 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.079 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.108 |
| revel vs cadd | +0.564 |
| revel vs sift | -0.505 |
| revel vs polyphen | +0.547 |
| revel vs metarnn | +0.892 |
| revel vs vest4 | +0.679 |
| revel vs primateai | +0.465 |
| revel vs mutassessor | +0.578 |
| revel vs provean | -0.648 |
| revel vs esm1b | -0.533 |
| revel vs am_dbnsfp | +0.638 |
| cadd vs sift | -0.655 |
| cadd vs polyphen | +0.629 |
| cadd vs metarnn | +0.702 |
| cadd vs vest4 | +0.646 |
| cadd vs primateai | +0.447 |
| cadd vs mutassessor | +0.595 |
| cadd vs provean | -0.620 |
| cadd vs esm1b | -0.468 |
| cadd vs am_dbnsfp | +0.634 |
| sift vs polyphen | -0.608 |
| sift vs metarnn | -0.628 |
| sift vs vest4 | -0.489 |
| sift vs primateai | -0.294 |
| sift vs mutassessor | -0.646 |
| sift vs provean | +0.624 |
| sift vs esm1b | +0.443 |
| sift vs am_dbnsfp | -0.624 |
| polyphen vs metarnn | +0.646 |
| polyphen vs vest4 | +0.522 |
| polyphen vs primateai | +0.377 |
| polyphen vs mutassessor | +0.651 |
| polyphen vs provean | -0.516 |
| polyphen vs esm1b | -0.310 |
| polyphen vs am_dbnsfp | +0.595 |
| metarnn vs vest4 | +0.770 |
| metarnn vs primateai | +0.534 |
| metarnn vs mutassessor | +0.695 |
| metarnn vs provean | -0.774 |
| metarnn vs esm1b | -0.600 |
| metarnn vs am_dbnsfp | +0.733 |
| vest4 vs primateai | +0.524 |
| vest4 vs mutassessor | +0.534 |
| vest4 vs provean | -0.634 |
| vest4 vs esm1b | -0.497 |
| vest4 vs am_dbnsfp | +0.695 |
| primateai vs mutassessor | +0.385 |
| primateai vs provean | -0.414 |
| primateai vs esm1b | -0.342 |
| primateai vs am_dbnsfp | +0.573 |
| mutassessor vs provean | -0.625 |
| mutassessor vs esm1b | -0.454 |
| mutassessor vs am_dbnsfp | +0.640 |
| provean vs esm1b | +0.545 |
| provean vs am_dbnsfp | -0.695 |
| esm1b vs am_dbnsfp | -0.542 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 2,601

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 8,062** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,274 | 4,788 |
| mean FoldX ΔΔG | 1.403 | 2.051 |
| mean REVEL | 0.236 | 0.591 |
| mean CADD phred | 19.921 | 26.652 |
| mean SIFT | -0.268 | -0.042 |
| mean PolyPhen-2 HVAR | 0.208 | 0.721 |
| mean MetaRNN | 0.354 | 0.784 |
| mean VEST4 | 0.581 | 0.851 |
| mean PrimateAI | 0.743 | 0.845 |
| mean PROVEAN | 1.717 | 4.335 |
| **fraction seen in gnomAD** | **18.81%** (616) | **12.34%** (591) |

**Validation:** the damaging cluster is **depleted** in the population — 12.34% of it appears in gnomAD against 18.81% of the tolerant cluster (a 1.5-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
