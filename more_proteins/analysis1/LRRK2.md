# LRRK2 — variant-effect analysis

*Leucine-rich repeat serine/threonine-protein kinase 2* · UniProt `Q5S007` · 2527 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Roc | 1328–1511 | 184 |
| COR | 1546–1740 | 195 |
| Protein kinase | 1879–2138 | 260 |

**Pair analysed:** Roc ↔ Protein kinase

**AlphaFold PAE:** inter-module mean **17.47 Å**, intra-module **6.17 Å**, **ratio 2.83**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 50.7 | 0 | 100% / 100% |
| 9om2.1.A (100.0% id) | 56.1 | 0 | 100% / 100% |
| 8tzh.1.B (100.0% id) | 55.2 | 0 | 100% / 100% |
| 9yqk.1.A (100.0% id) | 50.2 | 0 | 98% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 44,954 |
| ThermoMPNN ΔΔG | 0 |


## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 3,063

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
