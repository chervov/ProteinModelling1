# CAMK2A — variant-effect analysis

*Calcium/calmodulin-dependent protein kinase type II subunit alpha* · UniProt `Q9UQM7` · 478 aa · proposed

*Generated 28 October 2026 by `more_proteins/analysis1/pipe.py`. Every number is computed from the sources in §7, not quoted from a paper.*

## 1. Architecture and the domain pair

| domain | range | length |
|---|---|--:|
| Protein kinase | 13–271 | 259 |


## 2. The inter-domain interface

**No interface found** in any available structure for this pair — so there is no closed state to model. By the Stream B criterion of `jak_analogue_search_proposal.md` this is a flexible arrangement, not a two-state switch, however mobile it looks.
## 3. Feature coverage and independence

| feature | variants scored |
|---|--:|
| AlphaMissense | 0 |
| ESM-1v | 0 |
| FoldX ΔΔG (ProtVar) | 8,512 |
| ThermoMPNN ΔΔG | 0 |
| revel | 2,818 |
| cadd | 2,962 |
| sift | 2,818 |
| polyphen | 2,818 |
| metarnn | 2,818 |
| vest4 | 2,962 |
| primateai | 2,812 |
| mutassessor | 2,812 |
| provean | 2,818 |
| esm1b | 2,818 |
| am_dbnsfp | 2,812 |
| gerp | 0 |

*Four features score every substitution (AlphaMissense, ESM-1v and the two ΔΔG methods). The dbNSFP predictors cover only variants reachable by a **single nucleotide change** — typically ~30% of all substitutions — which is the same boundary documented for the JAKs in `TYK2/predictor_correlation_matrix.md`. GERP++ could not be retrieved: the `++` in its field name breaks the myvariant.info field path.*

All-vs-all Spearman (signs as reported, not oriented):

| pair | ρ |
|---|--:|
| FoldX ΔΔG (ProtVar) vs revel | +0.439 |
| FoldX ΔΔG (ProtVar) vs cadd | +0.331 |
| FoldX ΔΔG (ProtVar) vs sift | -0.352 |
| FoldX ΔΔG (ProtVar) vs polyphen | +0.279 |
| FoldX ΔΔG (ProtVar) vs metarnn | +0.465 |
| FoldX ΔΔG (ProtVar) vs vest4 | +0.429 |
| FoldX ΔΔG (ProtVar) vs primateai | +0.273 |
| FoldX ΔΔG (ProtVar) vs mutassessor | +0.341 |
| FoldX ΔΔG (ProtVar) vs provean | -0.395 |
| FoldX ΔΔG (ProtVar) vs esm1b | -0.298 |
| FoldX ΔΔG (ProtVar) vs am_dbnsfp | +0.476 |
| revel vs cadd | +0.651 |
| revel vs sift | -0.699 |
| revel vs polyphen | +0.599 |
| revel vs metarnn | +0.865 |
| revel vs vest4 | +0.765 |
| revel vs primateai | +0.426 |
| revel vs mutassessor | +0.568 |
| revel vs provean | -0.734 |
| revel vs esm1b | -0.569 |
| revel vs am_dbnsfp | +0.742 |
| cadd vs sift | -0.609 |
| cadd vs polyphen | +0.570 |
| cadd vs metarnn | +0.648 |
| cadd vs vest4 | +0.575 |
| cadd vs primateai | +0.337 |
| cadd vs mutassessor | +0.406 |
| cadd vs provean | -0.567 |
| cadd vs esm1b | -0.502 |
| cadd vs am_dbnsfp | +0.583 |
| sift vs polyphen | -0.483 |
| sift vs metarnn | -0.685 |
| sift vs vest4 | -0.558 |
| sift vs primateai | -0.376 |
| sift vs mutassessor | -0.371 |
| sift vs provean | +0.570 |
| sift vs esm1b | +0.528 |
| sift vs am_dbnsfp | -0.673 |
| polyphen vs metarnn | +0.641 |
| polyphen vs vest4 | +0.507 |
| polyphen vs primateai | +0.274 |
| polyphen vs mutassessor | +0.300 |
| polyphen vs provean | -0.507 |
| polyphen vs esm1b | -0.378 |
| polyphen vs am_dbnsfp | +0.527 |
| metarnn vs vest4 | +0.864 |
| metarnn vs primateai | +0.396 |
| metarnn vs mutassessor | +0.563 |
| metarnn vs provean | -0.681 |
| metarnn vs esm1b | -0.529 |
| metarnn vs am_dbnsfp | +0.743 |
| vest4 vs primateai | +0.392 |
| vest4 vs mutassessor | +0.498 |
| vest4 vs provean | -0.629 |
| vest4 vs esm1b | -0.516 |
| vest4 vs am_dbnsfp | +0.719 |
| primateai vs mutassessor | +0.305 |
| primateai vs provean | -0.419 |
| primateai vs esm1b | -0.330 |
| primateai vs am_dbnsfp | +0.591 |
| mutassessor vs provean | -0.448 |
| mutassessor vs esm1b | -0.288 |
| mutassessor vs am_dbnsfp | +0.447 |
| provean vs esm1b | +0.536 |
| provean vs am_dbnsfp | -0.634 |
| esm1b vs am_dbnsfp | -0.647 |

*Two ΔΔG methods correlating well below 1.0 is the expected result — see `external_data/ddg_study.md` §7 and §7b, where FoldX and our PyRosetta agree at ρ = 0.555 and FoldX and ThermoMPNN at ρ = 0.688 on TYK2.*

## 4. ClinVar and gnomAD

No ClinVar-linked variants in the Liao & Lehner table for this protein.

**gnomAD r4 missense variants mapped:** 409

## 5. Two-cluster split (the Jeanpierre/Debeaupuis step)

k-means, k = 2, on z-scored features oriented so that higher = more damaging. **n = 2,638** variants with all of FoldX ΔΔG, REVEL, CADD phred, SIFT, PolyPhen-2 HVAR, MetaRNN, VEST4, PrimateAI, PROVEAN.

| | cluster 0 (tolerant) | cluster 1 (damaging) |
|---|--:|--:|
| size | 819 | 1,819 |
| mean FoldX ΔΔG | 0.613 | 2.379 |
| mean REVEL | 0.231 | 0.58 |
| mean CADD phred | 22.323 | 28.913 |
| mean SIFT | -0.147 | -0.009 |
| mean PolyPhen-2 HVAR | 0.391 | 0.896 |
| mean MetaRNN | 0.428 | 0.847 |
| mean VEST4 | 0.521 | 0.799 |
| mean PrimateAI | 0.799 | 0.863 |
| mean PROVEAN | 2.11 | 5.254 |
| **fraction seen in gnomAD** | **9.40%** (77) | **5.72%** (104) |

**Validation:** the damaging cluster is **depleted** in the population — 5.72% of it appears in gnomAD against 9.40% of the tolerant cluster (a 1.6-fold difference). Purifying selection acting on the damaging cluster is the expected pattern and is an independent check on the split.


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
