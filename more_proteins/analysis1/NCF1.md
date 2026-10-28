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

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 7,106 |
| ThermoMPNN ΔΔG | 0 |


## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 470

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
