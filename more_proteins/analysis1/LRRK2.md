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
| revel | 8,379 |
| cadd | 8,920 |
| sift | 8,379 |
| polyphen | 8,350 |
| metarnn | 8,379 |
| vest4 | 8,889 |
| primateai | 8,349 |
| mutassessor | 8,339 |
| provean | 8,379 |
| esm1b | 8,350 |
| am_dbnsfp | 8,378 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.404 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.377 |
| FoldX ΔΔG (ProtVar) vs sift | -0.417 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.387 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.435 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.439 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.273 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.347 |
| FoldX ΔΔG (ProtVar) vs provean | -0.408 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.399 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.499 |
| revel vs cadd | +0.769 |
| revel vs sift | -0.629 |
| revel vs polyphen | +0.741 |
| revel vs metarnn | +0.871 |
| revel vs vest4 | +0.799 |
| revel vs primateai | +0.680 |
| revel vs mutassessor | +0.514 |
| revel vs provean | -0.679 |
| revel vs esm1b | -0.568 |
| revel vs am_dbnsfp | +0.693 |
| cadd vs sift | -0.700 |
| cadd vs polyphen | +0.793 |
| cadd vs metarnn | +0.843 |
| cadd vs vest4 | +0.799 |
| cadd vs primateai | +0.675 |
| cadd vs mutassessor | +0.512 |
| cadd vs provean | -0.668 |
| cadd vs esm1b | -0.542 |
| cadd vs am_dbnsfp | +0.712 |
| sift vs polyphen | -0.667 |
| sift vs metarnn | -0.704 |
| sift vs vest4 | -0.647 |
| sift vs primateai | -0.444 |
| sift vs mutassessor | -0.552 |
| sift vs provean | +0.724 |
| sift vs esm1b | +0.568 |
| sift vs am_dbnsfp | -0.629 |
| polyphen vs metarnn | +0.832 |
| polyphen vs vest4 | +0.771 |
| polyphen vs primateai | +0.623 |
| polyphen vs mutassessor | +0.603 |
| polyphen vs provean | -0.655 |
| polyphen vs esm1b | -0.572 |
| polyphen vs am_dbnsfp | +0.707 |
| metarnn vs vest4 | +0.906 |
| metarnn vs primateai | +0.715 |
| metarnn vs mutassessor | +0.580 |
| metarnn vs provean | -0.736 |
| metarnn vs esm1b | -0.604 |
| metarnn vs am_dbnsfp | +0.773 |
| vest4 vs primateai | +0.687 |
| vest4 vs mutassessor | +0.567 |
| vest4 vs provean | -0.704 |
| vest4 vs esm1b | -0.560 |
| vest4 vs am_dbnsfp | +0.776 |
| primateai vs mutassessor | +0.360 |
| primateai vs provean | -0.461 |
| primateai vs esm1b | -0.368 |
| primateai vs am_dbnsfp | +0.659 |
| mutassessor vs provean | -0.529 |
| mutassessor vs esm1b | -0.410 |
| mutassessor vs am_dbnsfp | +0.504 |
| provean vs esm1b | +0.606 |
| provean vs am_dbnsfp | -0.684 |
| esm1b vs am_dbnsfp | -0.562 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 3,063

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 7,787** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 3,855 | 3,932 |
| mean FoldX ΔΔG | 0.802 | 2.866 |
| mean REVEL | 0.132 | 0.483 |
| mean CADD phred | 15.542 | 27.245 |
| mean SIFT | -0.274 | -0.041 |
| mean PolyPhen-2 HVAR | 0.153 | 0.821 |
| mean MetaRNN | 0.228 | 0.748 |
| mean VEST4 | 0.334 | 0.756 |
| mean PrimateAI | 0.429 | 0.623 |
| mean PROVEAN | 1.189 | 3.307 |
| **fraction seen in gnomAD** | **23.87%** (920) | **18.08%** (711) |

**Validation:** the damaging cluster is **depleted** in the population — 18.08% of it appears in gnomAD against 23.87% of the tolerant cluster (a 1.3-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
