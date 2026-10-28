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

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 42,997 |
| ThermoMPNN ΔΔG | 0 |


## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 3,052

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

Not enough jointly-scored variants to cluster.

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
