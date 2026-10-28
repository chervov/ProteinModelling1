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

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 10,488 |
| ThermoMPNN ΔΔG | 0 |


## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 500

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
