# TYK2 clustering

Variant clustering for TYK2 (UniProt P29597, 1,187 aa), built by the same pipeline as
[`../../JAK2/clustering/`](../../JAK2/clustering/). 4 November 2026.

**Start here:** [`tyk2_clustering_report.md`](tyk2_clustering_report.md) ·
[`tyk2_clustering_report.html`](tyk2_clustering_report.html) ·
[`protein_models/tyk2_models_3d.html`](protein_models/tyk2_models_3d.html)

**C1 tolerant 9,144 / C2 damaging 13,409.** Validated against a **deep mutational scan** —
22,536 experimental measurements, AUC 0.64–0.68 — which is the first time in this project a
clustering could be checked against real functional data rather than a handful of ClinVar labels.

## Features

| feature | coverage | source |
|---|--:|---|
| ESM-1b | 100% | HuggingFace zip, one member by HTTP range request |
| AlphaMissense | 100% | DeepMind Zenodo, streamed with early stop |
| PolyPhen-2 HumVar / HumDiv | 100% | PolyPhen-2 batch server |
| BLOSUM62 | 100% | computed |
| ΔΔG closed / open / delta | 99.9% | **reused** from the 2026-10-22 run, see `build_ddg.py` |
| FoldX | 89.5% | ProtVar committed extract |
| CADD / SIFT / ClinPred | ~31% | dbNSFP via myvariant.info |

The ~31% is dbNSFP's structural ceiling — it indexes single-nucleotide changes only — not a
fetching failure.

## Differences from JAK2

| | JAK2 | TYK2 |
|---|---|---|
| external validation | 21 ClinVar labels | **22,536 DMS measurements** |
| closed reference | homology model, 6.0 Å | **4OLI crystal, 2.02 Å** |
| ClinVar Pathogenic | 5, all 2-star | **2, both 0-star** |
| AlphaFold DB model | **open** (93.8 Å) | **closed** (39.7 Å) |
| ΔΔG model pair | two pairs, one clean | one pair, **confounded** |
| damaging seeds | 5 | **2** |

## Reproduce

```bash
python3 build_universe.py
for f in esm1b alphamissense blosum62 dbnsfp polyphen foldx gnomad clinvar; do python3 build_$f.py; done
python3 build_ddg.py          # joins the reused October ddG, recomputes nothing
python3 cluster_tyk2.py
python3 analyse_tyk2.py && python3 plots_tyk2.py && python3 build_html_tyk2.py
cd protein_models && python3 analyse_models.py && python3 plot_models.py && python3 build_3d.py
```
