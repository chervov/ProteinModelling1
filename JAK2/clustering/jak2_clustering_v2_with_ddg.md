# JAK2 variant clustering — v2, with the dual-state ΔΔG

All **11** of the paper's features over all **21,508** JAK2 missense substitutions
(UniProt O60674, 1,132 aa). 4 November 2026.

Interactive version with figures: **[`jak2_clustering_v2_with_ddg.html`](jak2_clustering_v2_with_ddg.html)**.
Previous eight-feature version, left unchanged:
[`jak2_clustering_v1_wo_ddg_oc.html`](jak2_clustering_v1_wo_ddg_oc.html).

| | v1 (8 features) | **v2 (11 features)** |
|---|---|---|
| C1 tolerant / C2 damaging | 7,746 / 13,762 | **7,910 / 13,598** |
| iterations to converge | 13 | 10 |
| gnomAD pooled OR | 1.96 | **1.97** |
| gnomAD Mantel–Haenszel OR | 1.52 | **1.54** |
| ClinVar correct | 19/21 | **20/21** |

---

## 1. The headline: the ΔΔG features change almost nothing

**v1 and v2 agree on 99.11% of variants, ARI 0.9644** — 192 of 21,508 move. The external gnomAD
validation is unchanged to two decimal places. ClinVar improves by one variant, which is within
noise at n = 21.

This repeats the JAK1 result, where dropping the same three features *improved* agreement with the
published clustering (ARI 0.484 → 0.492). **`jak2_clustering_v1_wo_ddg_oc` was not missing
anything that matters**, and that is worth saying plainly given the effort spent filling the gap —
a model inventory, pair selection, PAE analysis and two PyRosetta runs.

## 2. `ddg_delta` is unusable, and the second model pair is how we know

ΔΔG was computed on **two independent model pairs**: pair 1 (untemplated, both states from one
run) and pair 2 (templated), 43,016 ΔΔG pairs in total, 100% coverage. Pair 2 exists solely to
test whether these numbers describe the protein or the structures.

| feature | AUC | pair 1 ↔ pair 2 (Pearson r) | Spearman ρ | verdict |
|---|--:|--:|--:|---|
| ΔΔG closed | 0.713 | 0.893 | 0.928 | reproducible |
| ΔΔG open | 0.717 | 0.870 | 0.906 | reproducible |
| **ΔΔG delta** | **0.499** | **0.074** | **0.155** | **do not use** |

Two independent facts:

- **AUC 0.499 is exact chance.** On JAK1 the same feature scored 0.4966 — two proteins, two
  independent model sets, same answer.
- **r = 0.074 is the stronger evidence.** `ddg_closed` and `ddg_open` survive a change of
  structures; their difference does not.

The cause is in the data: **median `delta` = −0.003**. ΔΔG is local, and the two states differ
only in where JH1 sits, so for almost every position nothing about the residue's environment
changes. `delta` is a difference of two large, strongly correlated numbers — dominated by
numerical noise, and noise is what fails to reproduce when the structures change.

So `ddg_delta` is not a weak feature. **It is not measuring a property of the protein.**

**Which pair is used barely matters either.** Clustering on pair 2's ΔΔG instead of pair 1's moves
**21** variants of 21,508 (ARI 0.9961). Pair 1 remains the right default on design grounds — both
states from one untemplated run, so only the conformation differs, and pair 2's open model sits
0.33 Å from the AlphaFold DB model it was templated on.

## 3. The 28 listed variants — does adding ΔΔG move any of them?

**No. Not one.** All 27 missense variants in the supplied list keep the cluster they had in v1.
`R426X` is nonsense and has no row in either version — the universe is missense only, and no
predictor in this set scores a stop-gain.

Listed in the order given, with the two groups and the four variants that appear in both Group-2
blocks (`G571R`, `V578I`, `L805I`, `V1110E`) repeated as supplied.

| group | variant | v1, no ΔΔG | **v2, with ΔΔG** | changed | ΔΔG closed | ΔΔG open | ΔΔG delta |
|---|---|:-:|:-:|:-:|--:|--:|--:|
| **GROUP 1 — GOF variants previously reported** | | | | | | | |
| GROUP 1 | **T108A** | C1 | **C1** | no | -2.1 | -2.2 | -0.10 |
| GROUP 1 | **Y317H** | C2 | **C2** | no | 2.4 | 1.7 | -0.78 |
| GROUP 1 | **H345L** | C1 | **C1** | no | -4.6 | -4.3 | +0.31 |
| GROUP 1 | **H608N** | C2 | **C2** | no | -0.3 | 0.8 | +1.18 |
| GROUP 1 | **L611S** | C2 | **C2** | no | -4.6 | -1.8 | +2.85 |
| GROUP 1 | **V617I** | C2 | **C2** | no | 0.9 | -0.2 | -1.15 |
| GROUP 1 | **V617F** | C2 | **C2** | no | -6.6 | -7.4 | -0.75 |
| GROUP 1 | **V625F** | C2 | **C2** | no | -180.3 | -186.6 | -6.29 |
| GROUP 1 | **E846D** | C1 | **C1** | no | -1.0 | -0.1 | +0.89 |
| GROUP 1 | **R867Q** | C2 | **C2** | no | 0.9 | 1.7 | +0.88 |
| GROUP 1 | **T875N** | C2 | **C2** | no | -6.2 | -0.2 | +6.04 |
| GROUP 1 | **S755R** | C1 | **C1** | no | -1.6 | -1.5 | +0.03 |
| GROUP 1 | **R938Q** | C2 | **C2** | no | -0.8 | -1.0 | -0.26 |
| GROUP 1 | **R1063H** | C1 | **C1** | no | 0.6 | 0.1 | -0.50 |
| **GROUP 2 — variants identified in this study** | | | | | | | |
| GROUP 2 | **V1110E** | C2 | **C2** | no | 2.4 | 2.6 | +0.23 |
| GROUP 2 | **G571R** | C2 | **C2** | no | -16.5 | -14.7 | +1.82 |
| GROUP 2 | **V578I** | C2 | **C2** | no | -38.2 | -33.9 | +4.35 |
| GROUP 2 | **L805I** | C1 | **C1** | no | -3.5 | -2.6 | +0.86 |
| **GROUP 2 — variants identified in this study** | | | | | | | |
| GROUP 2 | **P37A** | C1 | **C1** | no | -2.2 | 1.0 | +3.22 |
| GROUP 2 | **F240V** | C2 | **C2** | no | -0.9 | -2.4 | -1.56 |
| GROUP 2 | **H380Y** | C2 | **C2** | no | -10.1 | -16.8 | -6.79 |
| GROUP 2 | **R426X** | — | — | — | — | — | — |
| GROUP 2 | **C427R** | C1 | **C1** | no | 0.6 | -0.0 | -0.64 |
| GROUP 2 | **G571R** | C2 | **C2** | no | -16.5 | -14.7 | +1.82 |
| GROUP 2 | **V578I** | C2 | **C2** | no | -38.2 | -33.9 | +4.35 |
| GROUP 2 | **L805I** | C1 | **C1** | no | -3.5 | -2.6 | +0.86 |
| GROUP 2 | **I1065T** | C2 | **C2** | no | -6.5 | -6.5 | -0.05 |
| GROUP 2 | **V1110E** | C2 | **C2** | no | 2.4 | 2.6 | +0.23 |

ΔΔG sign: `ΔΔG = ΔG_WT − ΔG_mut`, **negative = destabilising** (opposite to FoldX).
`delta = open − closed`.

**Reading it.** The ΔΔG columns vary a good deal across these variants — `V625F` is far more
destabilising than `T108A` — yet none of that variation is enough to move a single one across the
cluster boundary. That is the panel-level version of the global result: 192 of 21,508 variants
move, and none of them are these.

Note also how small the `delta` column is: `V617F` is −0.75, `V617I` −1.15, most of the rest under
1 kcal/mol in absolute value. These are the variants with the strongest claim to acting *through*
the autoinhibitory interface, and the open/closed difference still barely separates them from the
rest — consistent with `ddg_delta` carrying no usable signal (section 2).

## 4. Per-feature summary

ΔΔG sign convention: `ΔΔG = ΔG_WT − ΔG_mut`, **negative = destabilising** (opposite to FoldX).
AUC is computed on the damaging direction.

| feature | coverage | C1 mean | C2 mean | Cohen's d | AUC |
|---|--:|--:|--:|--:|--:|
| PolyPhen-2 HumVar | 100.0% | 0.225 | 0.915 | +3.26 | 0.964 |
| CADD | 31.1% | 16.954 | 27.269 | +2.06 | 0.955 |
| ClinPred | 31.1% | 0.601 | 0.969 | +1.84 | 0.951 |
| AlphaMissense | 100.0% | 0.233 | 0.776 | +2.42 | 0.942 |
| ESM-1b | 100.0% | −6.171 | −12.473 | −1.95 | 0.921 |
| SIFT | 31.1% | 0.326 | 0.037 | −1.35 | 0.898 |
| FoldX ΔΔG | 94.6% | 0.636 | 2.953 | +0.66 | 0.742 |
| **ΔΔG open** | 100.0% | −17.966 | −76.095 | −0.30 | 0.717 |
| **ΔΔG closed** | 100.0% | −19.266 | −75.739 | −0.29 | 0.713 |
| BLOSUM62 | 100.0% | −0.822 | −1.713 | −0.61 | 0.665 |
| **ΔΔG delta** | 100.0% | 1.301 | −0.356 | −0.02 | **0.499** |

**These AUCs are circular** — these are the features the clustering was built from, so they rank
the features against each other and do not validate the result.

`ddg_closed` and `ddg_open` correlate at **0.896**, the highest pair in the whole matrix. They are
effectively one feature, a general destabilisation term, which FoldX already supplies at AUC
0.742. Giving both weight 1 double-counts that signal — the same objection that applies to the
CADD / ClinPred / PolyPhen-2 / SIFT block.

## 5. External validation (unchanged from v1)

- **gnomAD**: C1 9.87% observed vs C2 5.27%, pooled OR 1.97, p = 4.3 × 10⁻³⁶. The pooled figure is
  confounded — 100% of gnomAD-matched variants sit in the 31.1% dbNSFP-reachable subset and C1 is
  over-represented there — so the figure to quote is the **Mantel–Haenszel OR of 1.54**.
- **ClinVar**: **20 of 21** usable labels placed correctly, 7/7 pathogenic in the damaging cluster
  and 13/14 benign in the tolerant one. **10 of the 21 are seeds** — they were chosen from ClinVar — so the
  honest score on unseen labels is **10/11**. **V617F is in the damaging cluster.**

## 6. Seeds

Unchanged from v1, and still barely consequential: 15 random 5+5 draws reproduce
**0.9996–1.0000** of the labels. The supervision orients the result rather than determining it.

## 7. What this is, and what it is not

- **Not a reproduction.** There is no published JAK2 clustering to measure against.
- **The conformational axis is present but inert.** `ddg_delta` carries no signal and does not
  reproduce; `ddg_closed` and `ddg_open` are a destabilisation term, not a conformational one.
- **ΔΔG from a single conformer per state**, not an ensemble.
- **The interface caveat.** The residues where a conformational difference could plausibly be real
  — the JH1–JH2 and JH1–FERM interfaces — are where AlphaFold is least confident (FERM–JH1 PAE
  21.0 Å against a 31 Å ceiling). A difference feature restricted to those residues has not been
  tested and is the one remaining way the conformational idea could still work.
- **PolyPhen-2 HumVar, not HumDiv**; equal feature weights; FoldX standing in for "MutFunc" at
  94.6%; the gnomAD test is not CpG-mutability controlled. All as in v1.

## Files

| file | what |
|---|---|
| `cluster_jak2_v2.py` | the 11-feature clustering |
| `jak2_clustering_v2.csv`, `..._config.json` | labels and configuration |
| `jak2_ddg_closed.csv`, `_open.csv`, `_delta.csv` | the three features (from pair 1) |
| `analyse_with_ddg.py` → `stats_with_ddg.json` | every number in this report |
| `plots_with_ddg.py` → `figs_with_ddg/` | the figures |
| `build_html_with_ddg.py` → `jak2_clustering_v2_with_ddg.html` | the HTML report |
| `ddg/FINDINGS_dualstate_ddg.md` | the ΔΔG run and its findings |
| `ddg/RUNBOOK_jak2_dualstate_ddg.md` | how the run was operated |
| `data/ddg/ddg_JAK2P{1,2}_all.json` | raw ΔΔG, both pairs |

```bash
python3 cluster_jak2_v2.py && python3 analyse_with_ddg.py && \
python3 plots_with_ddg.py && python3 build_html_with_ddg.py
```
