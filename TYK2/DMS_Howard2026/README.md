# TYK2 deep mutational scan — Howard et al. 2026, all 11 arms

Complete extraction from MaveDB of every score set from:

> **Deep mutational scanning reveals pharmacologically relevant insights into TYK2 signaling and
> disease**
> Conor J. Howard, Nathan S. Abell, … Sriram Kosuri, **Diane E. Dickel** (24 authors)
> *eLife*, published 10 June 2026. DOI [10.7554/eLife.110149.2](https://doi.org/10.7554/eLife.110149.2)
> Preprint: bioRxiv 10.1101/2025.10.11.681520

Downloaded from the MaveDB API on 26 October 2026, experiments `urn:mavedb:00001270-a`
(signalling, 10 score sets) and `urn:mavedb:00001271-a` (abundance, 1 score set).

## Files

| file | contents |
|---|---|
| `TYK2_DMS_Howard2026_all_arms.csv` | **all 11 arms merged**, one row per variant, scores + standard errors |
| `raw/raw_<arm>.csv` | the unmodified MaveDB download for each arm |

Columns: `variant, pos, wt, alt, class`, then one column per arm, then `<arm>_se`.
`class` is `missense`, `nonsense` (alt `*`) or `synonymous`. 23,732 rows; **22,545 missense**.

## The 11 arms

| column | MaveDB | condition | missense n | median (missense) | median (nonsense) |
|---|---|---|--:|--:|--:|
| `ifn_1U` | 00001270-a-1 | IFN-α 1 U/mL | 22,536 | −0.048 | −0.228 |
| `ifn_10U` | 00001270-a-4 | IFN-α 10 U/mL | 22,536 | −0.150 | −1.246 |
| `ifn_100U` | 00001270-a-6 | IFN-α 100 U/mL | 22,536 | −0.118 | −1.645 |
| `ifn_100U_dup` | 00001270-a-9 | IFN-α 100 U/mL (duplicate assay) | 22,533 | −0.115 | −1.660 |
| `bms986202_20nM` | 00001270-a-5 | + BMS-986202, 20 nM | 22,533 | −0.149 | −1.140 |
| `bms986202_20nM_dup` | 00001270-a-7 | + BMS-986202, 20 nM (duplicate) | 22,533 | −0.158 | −1.364 |
| `bms986202_1uM` | 00001270-a-8 | + BMS-986202, 1 µM | 22,533 | +0.014 | +0.034 |
| `bms986202_10uM` | 00001270-a-2 | + BMS-986202, 10 µM | 22,536 | +0.011 | +0.068 |
| `ndi034858_7nM` | 00001270-a-3 | + NDI-034858, 7 nM | 22,533 | −0.159 | −1.574 |
| `ndi034858_1uM` | 00001270-a-10 | + NDI-034858, 1 µM | 22,533 | +0.009 | +0.006 |
| `abundance` | 00001271-a-1 | VAMP-seq protein abundance | 22,516 | −0.076 | −0.352 |

All inhibitor arms are at IFN-α 100 U/mL. BMS-986202 and NDI-034858 are **allosteric TYK2
inhibitors that bind the JH2 pseudokinase domain**, not the ATP site.

**Coverage is complete and uniform.** 22,507 of 22,545 missense variants (99.8%) are measured in
**all 11 arms**; no arm is a subset of another.

## Two things to know before using these

**1. The saturating-inhibitor arms have no dynamic range.** At BMS 1 µM / 10 µM and NDI 1 µM the
nonsense median is ≈ 0 — identical to the missense median. The drug suppresses signalling in every
variant, so the assay cannot distinguish a dead protein from a working one. For variant-effect work
use the **sub-saturating** arms, `bms986202_20nM` and `ndi034858_7nM`, where the nonsense anchor is
−1.14 to −1.57 and dynamic range is preserved.

**2. Each arm has its own nonsense anchor; −0.352 is the *abundance* value.** The signalling anchor
ranges from −0.228 (1 U/mL) to −1.66 (100 U/mL). Quoting −0.352 as a general "dead protein" line is
wrong for the signalling arms — at 1 U/mL a dead protein only reaches −0.228, which is why that dose
has so little room to resolve loss of function.

## Why the inhibitor arms matter here

They measure, per variant, sensitivity to drugs acting **through the JH2–JH1 interface** — the same
axis as the open/closed arrangement this project models. The interface effect
(`interface_effect.md`) predicts that interface variants should shift allosteric-inhibitor
sensitivity specifically, while leaving ATP-competitive inhibition unchanged. These arms are the
direct test of that, and were unused until now.
