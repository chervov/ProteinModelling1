# IGF2R — variant-effect analysis

*Cation-independent mannose-6-phosphate receptor* · UniProt `P11717` · 2491 aa · candidate

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| MRH 1 | 47–163 | 117 |
| MRH 2 | 172–320 | 149 |
| MRH 3 | 326–468 | 143 |
| MRH 4 | 473–619 | 147 |
| MRH 5 | 625–762 | 138 |
| MRH 6 | 765–924 | 160 |
| MRH 7 | 932–1079 | 148 |
| MRH 8 | 1082–1219 | 138 |
| MRH 9 | 1225–1363 | 139 |
| MRH 10 | 1367–1508 | 142 |
| MRH 11 | 1514–1648 | 135 |
| MRH 12 | 1650–1797 | 148 |
| Fibronectin type-II | 1802–1989 | 188 |
| MRH 14 | 1992–2127 | 136 |
| MRH 15 | 2135–2280 | 146 |

**Pair analysed:** MRH 6 ↔ MRH 9

**AlphaFold PAE:** inter-module mean **14.03 Å**, intra-module **5.83 Å**, **ratio 2.4**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 24.7 | 34 | 100% / 100% |
| SWISSMODEL_6um1-1-A_42-2282 | 23.0 | 64 | 100% / 100% |
| SWISSMODEL_6um1-1-A_59-1990 | 22.7 | 80 | 100% / 100% |
| SWISSMODEL_6um2-1-A_171-1795 | 44.5 | 2 | 100% / 100% |
| SWISSMODEL_6um2-1-A_472-2125 | 36.9 | 13 | 100% / 100% |

## 2. The inter-domain interface

Most compact structure: `IGF2R_P11717_SWISSMODEL_6um1-1-A_59-1990.pdb`, centroid distance **22.7 Å**, **80 residue pairs** in contact within 5 Å.

**Domain A interface residues (37):** `797, 799, 800, 858, 859, 860, 861, 862, 863, 864, 866, 868, 877, 878, 879, 881, 886, 888, 890, 892, 893, 894, 895, 897, 899, 901, 903, 904, 905, 906, 908, 909, 913, 914, 915, 916, 917`

**Domain B interface residues (30):** `1233, 1305, 1306, 1307, 1308, 1310, 1312, 1314, 1315, 1320, 1322, 1323, 1324, 1326, 1328, 1330, 1332, 1333, 1334, 1339, 1341, 1342, 1343, 1344, 1345, 1348, 1352, 1354, 1356, 1358`

### Are interface variants different? (Mann–Whitney, interface vs the rest)

| feature | n interface | n other | median interface | median other | p |
|---|--:|--:|--:|--:|--:|
| FoldX ΔΔG | 1,273 | 41,724 | 0.969 | 1.324 | 5.6e-20 |
| REVEL | 228 | 8,314 | 0.175 | 0.18 | 0.55 |
| CADD phred | 239 | 8,770 | 24.0 | 23.9 | 0.29 |
| SIFT | 228 | 8,314 | 0.047 | 0.033 | 0.14 |
| PolyPhen-2 HVAR | 228 | 8,314 | 0.712 | 0.699 | 0.55 |
| MetaRNN | 228 | 8,314 | 0.366 | 0.385 | 0.36 |
| VEST4 | 239 | 8,770 | 0.504 | 0.466 | 0.29 |
| PrimateAI | 228 | 8,310 | 0.422 | 0.447 | 0.067 |
| PROVEAN | 228 | 8,314 | -2.325 | -2.19 | 0.33 |
| ESM1b | 228 | 8,314 | -6.88 | -5.374 | 1.9e-05 |
| AlphaMissense (dbNSFP) | 228 | 8,310 | 0.23 | 0.216 | 0.6 |

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 42,997 |
| ThermoMPNN ΔΔG | 0 |
| revel | 8,542 |
| cadd | 9,009 |
| sift | 8,542 |
| polyphen | 8,542 |
| metarnn | 8,542 |
| vest4 | 9,009 |
| primateai | 8,538 |
| mutassessor | 0 |
| provean | 8,542 |
| esm1b | 8,542 |
| am_dbnsfp | 8,538 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.532 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.424 |
| FoldX ΔΔG (ProtVar) vs sift | -0.490 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.493 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.551 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.518 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.395 |
| FoldX ΔΔG (ProtVar) vs provean | -0.520 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.468 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.570 |
| revel vs cadd | +0.825 |
| revel vs sift | -0.763 |
| revel vs polyphen | +0.891 |
| revel vs metarnn | +0.928 |
| revel vs vest4 | +0.872 |
| revel vs primateai | +0.714 |
| revel vs provean | -0.813 |
| revel vs esm1b | -0.647 |
| revel vs am_dbnsfp | +0.813 |
| cadd vs sift | -0.779 |
| cadd vs polyphen | +0.834 |
| cadd vs metarnn | +0.830 |
| cadd vs vest4 | +0.816 |
| cadd vs primateai | +0.676 |
| cadd vs provean | -0.759 |
| cadd vs esm1b | -0.613 |
| cadd vs am_dbnsfp | +0.760 |
| sift vs polyphen | -0.764 |
| sift vs metarnn | -0.797 |
| sift vs vest4 | -0.749 |
| sift vs primateai | -0.585 |
| sift vs provean | +0.793 |
| sift vs esm1b | +0.670 |
| sift vs am_dbnsfp | -0.742 |
| polyphen vs metarnn | +0.903 |
| polyphen vs vest4 | +0.843 |
| polyphen vs primateai | +0.697 |
| polyphen vs provean | -0.783 |
| polyphen vs esm1b | -0.626 |
| polyphen vs am_dbnsfp | +0.803 |
| metarnn vs vest4 | +0.880 |
| metarnn vs primateai | +0.718 |
| metarnn vs provean | -0.845 |
| metarnn vs esm1b | -0.696 |
| metarnn vs am_dbnsfp | +0.827 |
| vest4 vs primateai | +0.719 |
| vest4 vs provean | -0.813 |
| vest4 vs esm1b | -0.634 |
| vest4 vs am_dbnsfp | +0.826 |
| primateai vs provean | -0.587 |
| primateai vs esm1b | -0.453 |
| primateai vs am_dbnsfp | +0.694 |
| provean vs esm1b | +0.715 |
| provean vs am_dbnsfp | -0.764 |
| esm1b vs am_dbnsfp | -0.659 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 3,052

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,751** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,851 | 3,900 |
| mean FoldX ΔΔG | 0.751 | 3.774 |
| mean REVEL | 0.099 | 0.391 |
| mean CADD phred | 13.666 | 27.221 |
| mean SIFT | -0.241 | -0.02 |
| mean PolyPhen-2 HVAR | 0.223 | 0.937 |
| mean MetaRNN | 0.185 | 0.765 |
| mean VEST4 | 0.263 | 0.679 |
| mean PrimateAI | 0.363 | 0.555 |
| mean PROVEAN | 1.318 | 4.505 |
| **fraction seen in gnomAD** | **23.73%** (914) | **17.74%** (692) |
| fraction at the interface | 3.25% | 2.64% |

**Validation:** the damaging cluster is **depleted** in the population — 17.74% of it appears in gnomAD against 23.73% of the tolerant cluster (a 1.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
