# ddG across structure pairs: are the new features better, the same, or worse?

*Auto-generated 2026-10-26 10:49 by `analyse_pairs.py`.*

| source | structures | n |
|---|---|--:|
| `T_within96` | within-run 96/384 pair - the one depth where TYK2 is genuinely bi-stable | 5,000 |
| `T_crossmax` | template-pinned closed x deep-MSA open - maximal separation | 5,000 |
| `T_af3xcamp` | AF3 closed x our own deep-MSA open - cross-method | 5,000 |
| `T_nullctrl` | **two IDENTICAL structures** - the noise floor, measured directly | 5,000 |
| `J_afdb` | AlphaFold DB JAK1 x Jeanpierre open - cross-source | 5,000 |
| `T_af3full` | matched AlphaFold 3 pair (the reference, full coverage) | 22,536 |
| `J_jpfull` | Jeanpierre open/closed (the reference, full coverage) | 21,926 |

## 1. Each pair against its own benchmark

AUC oriented so higher = more damaging. TYK2 against the DMS; JAK1 against the paper's clusters.

| source | feature | abundance | IFN 1U | IFN 100U | GOF | rho vs IFN1 | rho vs AlphaMiss |
|---|---|--:|--:|--:|--:|--:|--:|
| `T_within96` | closed | 0.708 | 0.569 | 0.730 | 0.454 | -0.104 | +0.441 |
| `T_within96` | open | 0.714 | 0.565 | 0.737 | 0.443 | -0.109 | +0.465 |
| `T_within96` | **diff** | 0.507 | 0.491 | 0.524 | 0.474 | -0.008 | +0.033 |
| `T_crossmax` | closed | 0.721 | 0.553 | 0.741 | 0.450 | -0.101 | +0.464 |
| `T_crossmax` | open | 0.710 | 0.559 | 0.742 | 0.451 | -0.100 | +0.463 |
| `T_crossmax` | **diff** | 0.468 | 0.514 | 0.503 | 0.505 | +0.005 | -0.017 |
| `T_af3xcamp` | closed | 0.728 | 0.557 | 0.743 | 0.454 | -0.097 | +0.489 |
| `T_af3xcamp` | open | 0.712 | 0.559 | 0.744 | 0.450 | -0.104 | +0.456 |
| `T_af3xcamp` | **diff** | 0.502 | 0.509 | 0.522 | 0.490 | -0.013 | -0.010 |
| `T_nullctrl` | closed | 0.712 | 0.561 | 0.743 | 0.448 | -0.103 | +0.464 |
| `T_nullctrl` | open | 0.711 | 0.562 | 0.743 | 0.450 | -0.102 | +0.460 |
| `T_nullctrl` | **diff** | 0.491 | 0.491 | 0.503 | 0.487 | -0.005 | +0.010 |
| `T_af3full` | closed | 0.704 | 0.565 | 0.733 | 0.453 | -0.108 | +0.475 |
| `T_af3full` | open | 0.697 | 0.563 | 0.728 | 0.448 | -0.109 | +0.466 |
| `T_af3full` | **diff** | 0.499 | 0.499 | 0.516 | 0.498 | -0.002 | +0.018 |

| source | feature | AUC vs the paper's JAK1 clusters |
|---|---|--:|
| `J_afdb` | closed | 0.743 |
| `J_afdb` | open | 0.737 |
| `J_afdb` | **diff** | 0.490 |
| `J_jpfull` | closed | 0.741 |
| `J_jpfull` | open | 0.739 |
| `J_jpfull` | **diff** | 0.495 |

## 2. Do different structure pairs agree with each other?

### TYK2 - Spearman on variants present in both

| | `T_within96` | `T_crossmax` | `T_af3xcamp` | `T_nullctrl` | `T_af3full` |
|---|---|---|---|---|---|
| `T_within96` (closed) | - | +0.798 | +0.769 | +0.880 | +0.769 |
| `T_crossmax` (closed) | +0.798 | - | +0.814 | +0.818 | +0.812 |
| `T_af3xcamp` (closed) | +0.769 | +0.814 | - | +0.786 | +0.976 |
| `T_nullctrl` (closed) | +0.880 | +0.818 | +0.786 | - | +0.783 |
| `T_af3full` (closed) | +0.769 | +0.812 | +0.976 | +0.783 | - |

| | `T_within96` | `T_crossmax` | `T_af3xcamp` | `T_nullctrl` | `T_af3full` |
|---|---|---|---|---|---|
| `T_within96` (**difference**) | - | -0.058 | -0.023 | -0.021 | -0.005 |
| `T_crossmax` (**difference**) | -0.058 | - | +0.359 | +0.036 | +0.083 |
| `T_af3xcamp` (**difference**) | -0.023 | +0.359 | - | +0.018 | +0.352 |
| `T_nullctrl` (**difference**) | -0.021 | +0.036 | +0.018 | - | -0.021 |
| `T_af3full` (**difference**) | -0.005 | +0.083 | +0.352 | -0.021 | - |

### JAK1 - Spearman on variants present in both

| | `J_afdb` | `J_jpfull` |
|---|---|---|
| `J_afdb` (closed) | - | +0.893 |
| `J_jpfull` (closed) | +0.893 | - |

| | `J_afdb` | `J_jpfull` |
|---|---|---|
| `J_afdb` (**difference**) | - | +0.368 |
| `J_jpfull` (**difference**) | +0.368 | - |

## 3. Does averaging across structures help?

### TYK2 - ensemble over 5 pairs, 5,000 shared variants

| feature | abundance | IFN 1U | IFN 100U | GOF |
|---|--:|--:|--:|--:|
| **ensemble mean ddG_closed** | 0.736 | 0.564 | 0.758 | 0.448 |
| **ensemble mean difference** | 0.498 | 0.503 | 0.532 | 0.486 |
| single: `T_within96` closed | 0.708 | 0.569 | 0.730 | 0.454 |
| single: `T_crossmax` closed | 0.721 | 0.553 | 0.741 | 0.450 |
| single: `T_af3xcamp` closed | 0.728 | 0.557 | 0.743 | 0.454 |
| single: `T_nullctrl` closed | 0.712 | 0.561 | 0.743 | 0.448 |
| single: `T_af3full` closed | 0.726 | 0.558 | 0.732 | 0.454 |

**Incremental value over AlphaMissense** (5-fold CV, folds grouped by position):

| model | AUC abundance | AUC IFN 1U |
|---|--:|--:|
| AlphaMissense alone | 0.867 | 0.577 |
| + ensemble ddG_closed | 0.865 | 0.579 |
| + ensemble difference | 0.866 | 0.577 |
| + both | 0.864 | 0.579 |

### JAK1 - ensemble over 2 pairs, 5,000 shared variants

| feature | AUC vs the paper's clusters |
|---|--:|
| **ensemble mean ddG_closed** | 0.748 |
| **ensemble mean difference** | 0.499 |

