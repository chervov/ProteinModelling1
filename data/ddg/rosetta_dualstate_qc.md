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

**(c) Unrelaxed steric clashes contaminate the single-state columns.**

| protein | n | median ddg_closed | abs>10 | abs>100 | survive abs<15 | median delta (kept) | SD delta (kept) |
|---|--:|--:|--:|--:|--:|--:|--:|
| JAK1 | 21,926 | -3.79 | 27.8% | 11.0% | 74.3% | -0.011 | 2.42 |
| TYK2 | 22,536 | -3.95 | 27.6% | 10.6% | 74.3% | +0.058 | 2.44 |

A median of -3.8 kcal/mol is wrong on its face: most random substitutions destabilise, so the
median should be near +1. Minima reach -2,935 kcal/mol. `clash_diagnosis.json` gives the cause -
`frac_rep` approximately 1.0, i.e. essentially the whole energy difference is `fa_rep`, repulsive
van der Waals from a side chain inserted without relaxation. `kellogg_ddg_monomer.json`
confirms it on 5 calibration variants: G746W scores 963 kcal/mol. Gly->bulky substitutions
are the worst affected (40% of JAK1 Gly->WFYRK exceed 100 kcal/mol), while R775A (0.62) and
H667F (2.08) are sane - the pipeline works wherever no clash is created.

**The dual-state design partly rescues itself.** `delta` is far better behaved (median -0.011,
IQR -1.24..+1.04) because an identical unrelaxed clash appears in both states and subtracts out.
But 4.5% of deltas still exceed 100 kcal/mol, so a filter is still required.

### Recommended use
Filter on `abs(ddg_closed) < 15 and abs(ddg_open) < 15` - this keeps 74.3% of both datasets and
~61% of positions retain at least 15 of 19 substitutions. Analyse `delta` only, never the raw
single-state columns. Treat the result as a conformational-shift score, and rank within it
rather than quoting absolute kcal/mol.

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
