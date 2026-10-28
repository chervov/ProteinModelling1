# ITGB2 — variant-effect analysis

*Integrin beta-2* · UniProt `P05107` · 769 aa · measured

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| PSI | 24–74 | 51 |
| VWFA | 124–363 | 240 |
| I-EGF 1 | 449–482 | 34 |
| I-EGF 2 | 483–535 | 53 |
| I-EGF 3 | 536–574 | 39 |
| I-EGF 4 | 575–613 | 39 |

**Pair analysed:** PSI ↔ I-EGF 4

**AlphaFold PAE:** inter-module mean **14.65 Å**, intra-module **2.75 Å**, **ratio 5.33**. A ratio above ~2 means AlphaFold is confident about each domain and unsure where they sit relative to each other.

### Inter-domain geometry per structure

| structure | centroid Å | contacts | coverage |
|---|--:|--:|---|
| AlphaFold v6 | 43.9 | 0 | 100% / 100% |
| 3k6s.1.B (99.9% id) | 44.5 | 0 | 100% / 100% |
| 7nxd.1.B (47.3% id) | 43.8 | 0 | 100% / 100% |
| 7usl.1.B (100.0% id) | 42.1 | 0 | 100% / 100% |
| 8xez.1.B (40.1% id) | 50.5 | 0 | 100% / 100% |

## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 14,136 |
| ThermoMPNN ΔΔG | 0 |
| revel | 4,567 |
| cadd | 4,796 |
| sift | 4,567 |
| polyphen | 0 |
| metarnn | 4,573 |
| vest4 | 4,798 |
| primateai | 4,559 |
| mutassessor | 0 |
| provean | 4,567 |
| esm1b | 0 |
| am_dbnsfp | 4,567 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.422 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.362 |
| FoldX ΔΔG (ProtVar) vs sift | -0.446 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.473 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.442 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.350 |
| FoldX ΔΔG (ProtVar) vs provean | -0.510 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.499 |
| revel vs cadd | +0.742 |
| revel vs sift | -0.736 |
| revel vs metarnn | +0.894 |
| revel vs vest4 | +0.844 |
| revel vs primateai | +0.736 |
| revel vs provean | -0.737 |
| revel vs am_dbnsfp | +0.806 |
| cadd vs sift | -0.778 |
| cadd vs metarnn | +0.780 |
| cadd vs vest4 | +0.760 |
| cadd vs primateai | +0.646 |
| cadd vs provean | -0.739 |
| cadd vs am_dbnsfp | +0.765 |
| sift vs metarnn | -0.810 |
| sift vs vest4 | -0.770 |
| sift vs primateai | -0.619 |
| sift vs provean | +0.814 |
| sift vs am_dbnsfp | -0.758 |
| metarnn vs vest4 | +0.909 |
| metarnn vs primateai | +0.756 |
| metarnn vs provean | -0.833 |
| metarnn vs am_dbnsfp | +0.859 |
| vest4 vs primateai | +0.778 |
| vest4 vs provean | -0.801 |
| vest4 vs am_dbnsfp | +0.853 |
| primateai vs provean | -0.624 |
| primateai vs am_dbnsfp | +0.758 |
| provean vs am_dbnsfp | -0.788 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 1,096

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 4,423** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 1,975 | 2,448 |
| mean FoldX ΔΔG | 0.657 | 3.653 |
| mean REVEL | 0.283 | 0.763 |
| mean CADD phred | 10.519 | 25.368 |
| mean SIFT | -0.293 | -0.017 |
| mean MetaRNN | 0.258 | 0.882 |
| mean VEST4 | 0.25 | 0.735 |
| mean PrimateAI | 0.396 | 0.615 |
| mean PROVEAN | 1.452 | 5.335 |
| **fraction seen in gnomAD** | **26.58%** (525) | **18.83%** (461) |

**Validation:** the damaging cluster is **depleted** in the population — 18.83% of it appears in gnomAD against 26.58% of the tolerant cluster (a 1.4-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
