# Overnight dual-state ddG: TYK2 and JAK1 at scale

Auto-generated 2026-10-23 13:27 by `analyse_ddg.py`; regenerated every 30 min
as results arrive. **This supersedes the 469-variant and 500-variant pilots of sections 56-59**,
which were too small and, for TYK2, confined to the 4OLI interface.

Protocol is unchanged from section 56 (verified against the PyRosetta PagP tutorial to four
decimals): FastRelax with coordinate constraints on each model, `mutate_residue` with an 8 A
repack shell, the native repacked identically so neither side is favoured, and the paper's sign
convention ddG = dG_WT - dG_mut, so **negative = destabilizing**. One efficiency change: the WT
repack is computed once per position and reused across that position's substitutions, which is
exact (the shell is identical) and ~19x cheaper.

## TYK2 - the matched AlphaFold 3 pair

**20,897 variants** at 1,101 positions (92.7% of the 22,536 possible).

| | ddG_closed | ddG_open | ddG_open - ddG_closed |
|---|--:|--:|--:|
| median | -3.96 | -3.71 | +0.00 |
| SD | 4.31 | 4.42 | 2.70 |
| fraction inside [-10,10] | 0.723 | 0.727 | - |

- Pearson r(closed, open) = **+0.809**, Spearman **+0.824**
- the difference's SD is **63%** of ddG_closed's

### Against measured phenotype (the test the paper could not run)

AUC oriented so **higher = more damaging**; targets are the global DMS deciles.

| feature | LOF, IFN-a 1 U/mL | LOF, IFN-a 100 U/mL | GOF, IFN-a 1 U/mL | rho vs IFN 1 U |
|---|--:|--:|--:|--:|
| ddG_closed | 0.568 | 0.729 | 0.453 | -0.110 |
| ddG_open | 0.565 | 0.723 | 0.450 | -0.110 |
| **ddG_open - ddG_closed** | 0.500 | 0.514 | 0.499 | -0.001 |
| AlphaMissense (ref) | 0.611 | 0.878 | 0.436 | -0.173 |
| ESM-1b (ref) | 0.592 | 0.825 | 0.445 | -0.147 |

### Correlation with the sequence predictors

| predictor | vs ddG_closed | vs ddG_open | vs the difference | n |
|---|--:|--:|--:|--:|
| AlphaMissense | +0.470 | +0.460 | +0.016 | 20,897 |
| ESM-1b | +0.440 | +0.435 | +0.029 | 20,897 |
| REVEL | +0.380 | +0.373 | +0.015 | 6,458 |
| SIFT | +0.378 | +0.380 | +0.025 | 6,458 |
| PolyPhen-2 | +0.402 | +0.404 | +0.021 | 6,378 |
| BLOSUM62 | +0.227 | +0.222 | +0.018 | 20,897 |

### Clustering with ddG included, scored against the DMS

| cluster | n | median IFN 1U | median IFN 100U | % LOF 1U | % LOF 100U | % GOF |
|---|--:|--:|--:|--:|--:|--:|
| 1 | 11,928 | -0.005 | -0.033 | 7.4 | 1.6 | 11.5 |
| 2 | 8,969 | -0.106 | -0.285 | 13.5 | 21.5 | 7.7 |

Silhouette **0.258** (the paper's JAK1 clusters: 0.098).
- cluster-2 membership vs LOF, IFN-a 1 U/mL: AUC **0.584** (p=3.4e-49)
- cluster-2 membership vs LOF, IFN-a 100 U/mL: AUC **0.766** (p=0)
- cluster-2 membership vs GOF, IFN-a 1 U/mL: AUC **0.448** (p=7.9e-20)

## JAK1 - Jeanpierre's own open and closed models

**21,926 variants** at 1,154 positions (100.0% of the 21,926 possible).

| | ddG_closed | ddG_open | ddG_open - ddG_closed |
|---|--:|--:|--:|
| median | -3.79 | -3.98 | +0.00 |
| SD | 4.39 | 4.26 | 2.39 |
| fraction inside [-10,10] | 0.722 | 0.724 | - |

- Pearson r(closed, open) = **+0.848**, Spearman **+0.863**
- the difference's SD is **54%** of ddG_closed's

### Against the paper's own cluster labels

| feature | AUC vs their labels | p | median C1 | median C2 |
|---|--:|--:|--:|--:|
| ddG_closed | 0.741 | 0 | -1.61 | -6.04 |
| ddG_open | 0.739 | 0 | -1.73 | -6.06 |
| **ddG_open - ddG_closed** | 0.495 | 0.25 | +0.00 | +0.00 |
| *paper's reported medians (ddG_closed)* | - | - | *-2.05* | *-6.36* |

### Correlation with the sequence predictors

| predictor | vs ddG_closed | vs ddG_open | vs the difference | n |
|---|--:|--:|--:|--:|
| AlphaMissense | +0.462 | +0.463 | -0.009 | 21,926 |
| ESM-1b | +0.455 | +0.449 | -0.011 | 21,926 |
| ClinPred | +0.442 | +0.437 | -0.003 | 6,873 |
| REVEL | +0.369 | +0.380 | +0.025 | 6,873 |
| SIFT | +0.414 | +0.412 | -0.006 | 6,873 |
| PolyPhen-2 | +0.372 | +0.376 | +0.016 | 6,873 |
| BLOSUM62 | +0.240 | +0.245 | +0.003 | 21,926 |

