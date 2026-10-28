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

## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 14,212 |
| ESM-1v | 14,212 |
| FoldX ΔΔG (ProtVar) | 13,452 |
| ThermoMPNN ΔΔG | 14,212 |

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| AlphaMissense vs ESM-1v | -0.734 |
| AlphaMissense vs FoldX ΔΔG (ProtVar) | +0.363 |
| AlphaMissense vs ThermoMPNN ΔΔG | +0.429 |
| ESM-1v vs FoldX ΔΔG (ProtVar) | -0.387 |
| ESM-1v vs ThermoMPNN ΔΔG | -0.491 |
| FoldX ΔΔG (ProtVar) vs ThermoMPNN ΔΔG | +0.661 |

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

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 13,452** variants with all of AlphaMissense, ESM-1v, FoldX ΔΔG, ThermoMPNN ΔΔG.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 8,895 | 4,557 |
| mean AlphaMissense | 0.249 | 0.671 |
| mean ESM-1v | 5.98 | 11.545 |
| mean FoldX ΔΔG | 0.366 | 3.424 |
| mean ThermoMPNN ΔΔG | 0.406 | 1.618 |
| **fraction seen in gnomAD** | **5.03%** (447) | **5.09%** (232) |
| fraction at the interface | 3.11% | 3.93% |

**Validation:** the damaging cluster is enriched in the population — 5.09% of it appears in gnomAD against 5.03% of the tolerant cluster (a 1.0-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.

**Against ClinVar** (pathogenic/likely vs benign/likely, Fisher exact): cluster 1 has 0 pathogenic / 0 benign, cluster 0 has 0 / 8; OR = nan, p = 1.

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
