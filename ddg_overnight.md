# Overnight dual-state ddG: TYK2 and JAK1 at scale

Auto-generated 2026-10-22 22:28 by `analyse_ddg.py`; regenerated every 30 min
as results arrive. **This supersedes the 469-variant and 500-variant pilots of sections 56-59**,
which were too small and, for TYK2, confined to the 4OLI interface.

Protocol is unchanged from section 56 (verified against the PyRosetta PagP tutorial to four
decimals): FastRelax with coordinate constraints on each model, `mutate_residue` with an 8 A
repack shell, the native repacked identically so neither side is favoured, and the paper's sign
convention ddG = dG_WT - dG_mut, so **negative = destabilizing**. One efficiency change: the WT
repack is computed once per position and reused across that position's substitutions, which is
exact (the shell is identical) and ~19x cheaper.

## TYK2 - the matched AlphaFold 3 pair

**12,000 variants** at 633 positions (53.2% of the 22,536 possible).

| | ddG_closed | ddG_open | ddG_open - ddG_closed |
|---|--:|--:|--:|
| median | -3.93 | -3.65 | +0.00 |
| SD | 4.35 | 4.44 | 2.76 |
| fraction inside [-10,10] | 0.725 | 0.730 | - |

- Pearson r(closed, open) = **+0.803**, Spearman **+0.818**
- the difference's SD is **63%** of ddG_closed's

### Against measured phenotype (the test the paper could not run)

AUC oriented so **higher = more damaging**; targets are the global DMS deciles.

| feature | LOF, IFN-a 1 U/mL | LOF, IFN-a 100 U/mL | GOF, IFN-a 1 U/mL | rho vs IFN 1 U |
|---|--:|--:|--:|--:|
| ddG_closed | 0.576 | 0.742 | 0.450 | -0.116 |
| ddG_open | 0.570 | 0.729 | 0.446 | -0.109 |
| **ddG_open - ddG_closed** | 0.494 | 0.514 | 0.500 | +0.004 |
| AlphaMissense (ref) | 0.611 | 0.884 | 0.440 | -0.173 |
| ESM-1b (ref) | 0.592 | 0.825 | 0.455 | -0.140 |

### Correlation with the sequence predictors

| predictor | vs ddG_closed | vs ddG_open | vs the difference | n |
|---|--:|--:|--:|--:|
| AlphaMissense | +0.473 | +0.472 | +0.042 | 12,000 |
| ESM-1b | +0.429 | +0.432 | +0.050 | 12,000 |
| REVEL | +0.370 | +0.357 | +0.017 | 3,708 |
| SIFT | +0.387 | +0.385 | +0.034 | 3,708 |
| PolyPhen-2 | +0.401 | +0.405 | +0.035 | 3,663 |
| BLOSUM62 | +0.221 | +0.213 | +0.020 | 12,000 |

### Clustering with ddG included, scored against the DMS

| cluster | n | median IFN 1U | median IFN 100U | % LOF 1U | % LOF 100U | % GOF |
|---|--:|--:|--:|--:|--:|--:|
| 1 | 6,705 | -0.005 | -0.033 | 7.6 | 1.5 | 11.5 |
| 2 | 5,295 | -0.105 | -0.279 | 13.4 | 21.1 | 7.9 |

Silhouette **0.274** (the paper's JAK1 clusters: 0.098).
- cluster-2 membership vs LOF, IFN-a 1 U/mL: AUC **0.577** (p=5.6e-25)
- cluster-2 membership vs LOF, IFN-a 100 U/mL: AUC **0.765** (p=6.3e-274)
- cluster-2 membership vs GOF, IFN-a 1 U/mL: AUC **0.451** (p=8.7e-11)

## JAK1 - Jeanpierre's own open and closed models

*0 variants so far - too few to analyse; this section fills in automatically.*

