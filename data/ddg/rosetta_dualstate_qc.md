# What is already in `data/ddg/`, and what it can answer

Audit of the files in this directory that were **not** produced by the JAK2 variant run
(`compute_jak2_ddg.py`, `jak2_variants_ddg*.csv`, `jak2_ddg.png`, `README.md`).

## 1. There IS a second method here: dual-state PyRosetta

Per `RUNBOOK.md`, an overnight run on 2026-10-22 across 4 CPU boxes produced:

| file | content |
|---|---|
| `ddg_JAK1_all.json` | 21,926 variants, 1,154 positions - complete JAK1 saturation |
| `ddg_TYK2_all.json` | 22,536 variants, 1,187 positions - complete TYK2 saturation |
| `pairs/ddg_T_{crossmax,nullctrl,within96,af3xcamp}.json`, `pairs/ddg_J_afdb.json` | 5,000 variants each - structure-pair controls |

The records are `{pos, wt, alt, ddg_closed, ddg_open, delta}`.

## 2. It does not answer the JAK2 variant question, for three reasons

**(a) No JAK2.** JAK1 and TYK2 only. `RosettaNewV1.html` contains zero occurrences of
`JAK2`, `O60674` or `V617F`.

**(b) Different quantity.** `delta = ddg_open - ddg_closed` is a *conformational preference
shift*, not a folding stability change. It asks "does this mutation favour the open state?",
which is arguably the better question for a gain-of-function hypothesis - but it is not
comparable with ThermoMPNN or FoldX single-state ddG and must not be merged into that table.

**(c) CORRECTED 4 Nov 2026 - the negative median is NOT an error; the extreme tail still is.**

> My original version of this section argued the data were contaminated partly because the median
> `ddg_closed` was negative, claiming it "should be near +1". **That was my mistake**, from assuming
> the FoldX sign convention. `DDG_COMPUTATION_REPORT.md` states the convention explicitly:
> **ddG = dG_WT - dG_mut, so NEGATIVE = destabilising** - the opposite of FoldX. A median of -3.8
> is therefore exactly what a correct calculation should give. The report also records that the
> protocol reproduces PyRosetta's published ddG tutorial to four decimals, and notes the sign has
> been got wrong twice in this project. I have now made it a third time, in the opposite direction.

| protein | n | median ddg_closed | abs>10 | abs>100 | survive abs<15 | median delta (kept) |
|---|--:|--:|--:|--:|--:|--:|
| JAK1 | 21,926 | -3.79 | 27.8% | 11.0% | 74.3% | -0.011 |
| TYK2 | 22,536 | -3.95 | 27.6% | 10.6% | 74.3% | +0.058 |
| JAK2 P1 | 21,508 | -4.16 | 27.8% | 10.8% | - | -0.000 |
| JAK2 P2 | 21,508 | -4.21 | 28.3% | 11.1% | - | -0.040 |

What does survive is the **extreme tail**: minima reach -3,498 kcal/mol, and ~11% of values exceed
|100|, which is unphysical under any sign convention. `clash_diagnosis.json` gives the cause -
`frac_rep` approximately 1.0, essentially the whole energy difference being repulsive van der Waals
from a side chain placed without relaxation. `kellogg_ddg_monomer.json` confirms it on 5 calibration
variants: G746W scores 963 kcal/mol. Gly->bulky is worst (40% of JAK1 Gly->WFYRK exceed 100).

**(d) The dual-state `delta` does not reproduce between the two JAK2 runs.**

`ddg_JAK2P1_all.json` and `ddg_JAK2P2_all.json` are both complete JAK2 saturation scans
(21,508 = 19 x 1,132) and so can be compared directly, variant by variant:

| set | n | Pearson r | Spearman rho | median abs diff | sign agreement |
|---|--:|--:|--:|--:|--:|
| all paired rows | 21,508 | **+0.074** | +0.155 | 1.39 | **55.4%** |
| after abs(single-state)<15 filter | 15,396 | **+0.295** | +0.172 | 0.78 | **55.2%** |

Sign agreement of 55% is barely above the 50% a coin would give. Filtering improves the correlation
but not the sign agreement at all. **This supersedes the "analyse `delta` only" recommendation in the
original version of this memo**: on the evidence of these two runs, `delta` is dominated by whatever
differs between P1 and P2 rather than by the mutation.

One caveat on that conclusion: this directory does not document what P1 and P2 denote.
`DDG_COMPUTATION_REPORT.md` (3 Nov) covers only TYK2 and JAK1 and predates these files. If P1 and P2
are two *different* open/closed structure pairs, then the finding is that `delta` is highly sensitive
to the choice of structure pair; if they are repeats of the same pair, it is that `delta` is not
reproducible. Either reading argues against using per-variant `delta` values. Distinguishing them
needs only the provenance of the two files.

### Recommended use
Do not use per-variant `delta`. Aggregate statistics over thousands of variants may still carry
signal, since the noise is centred near zero (mean difference -0.005 after filtering), but any
single variant's value is not supported by the agreement between the two runs. If single-variant
dual-state numbers are needed, run the same pair twice and keep only variants where the two agree.

## 3. The six-column multi-method table is still not in this repository

`RosettaNewV1.html` contains zero occurrences of FoldX, PoPMuSiC, mCSM, DUET, Consensus,
Cross-Tool, ThermoMPNN or RaSP. This matches the earlier finding that `mutation_analysis.md`
contains zero occurrences of FoldX, PoPMuSiC or Cross-Tool. Whatever produced that table was
not run in this repository.

## 4. Current state of the JAK2 variant table

| method | status |
|---|---|
| ThermoMPNN | done, all 23 computable variants |
| FoldX 5.0 | done via ProtVar precomputed (94.6% of JAK2 positions) |
| RaSP | obtainable locally |
| Rosetta cartesian_ddg | not run; the Rosetta here is dual-state on JAK1/TYK2 |
| PoPMuSiC 3.1 | registration-gated web server |
| mCSM-Stability, DUET, SDM | `biosig.lab.uq.edu.au` is not on the network allowlist |
