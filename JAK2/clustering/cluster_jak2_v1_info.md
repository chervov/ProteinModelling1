# `cluster_jak2.py` — the JAK2 clustering, version `v1_wo_ddg_oc`

Human-readable companion to `cluster_jak2.py`. Documents the method, the choices
that were made (and why), the errors hit on the way, timings, and output sizes.

## What this produces

| file | size | contents |
|---|---|---|
| `jak2_clustering_v1.csv` | 1.27 MB | 21,508 rows — `index, variant, pos, wt, alt, <8 features>, cluster` |
| `jak2_clustering_v1_config.json` | 1.1 KB | features, seeds, seed rule, iterations, sizes, feature ranges, seed-sensitivity |

`cluster` is `1` (tolerant) or `2` (damaging). **C1 = 7,746, C2 = 13,762.**

## Method

Follows Jeanpierre *et al.* as applied to JAK1 in `../../JAK1/clustering/`:

1. **Gower distance.** Each feature is min–max scaled to [0, 1], and the distance
   between two variants is the mean absolute difference **over the features both
   variants have**. Nothing is imputed — a variant with 4 features and one with 8
   are compared on their 4 shared ones. This matters a great deal here: three
   features sit at 31.1% coverage because dbNSFP only indexes single-nucleotide
   changes, so a mean-imputation approach would be inventing two thirds of three
   columns.
2. **Semi-supervised K-means**, k = 2, with 10 variants pinned to their clusters
   and never reassigned. Centroids are means over non-missing values.
   Converged in **13 iterations**.

## The seed choice — and why it barely matters

The paper names 10 JAK1 seeds. **JAK2 has no published equivalent**, so they had
to be derived. The rule chosen, stated before looking at any result:

- **C1 (tolerant)** — the 5 ClinVar benign/likely-benign JAK2 missense variants
  with the **highest gnomAD allele frequency**, all 2-star review status:
  `R1063H, D1096E, C480F, N337D, K244R`.
  This mirrors the paper's description of its tolerant seeds as "common in the
  general population (from gnomAD v4)".
- **C2 (damaging)** — the 5 ClinVar pathogenic/likely-pathogenic variants ranked
  by review stars: `V617F, R867Q, R938Q, P1095L, K539L`.
  Mirrors "clinically reported to cause gain-of-function".

Both lists come from data **no feature saw** (ClinVar classification, gnomAD AF),
not from the predictors being clustered.

**Seed sensitivity.** Fifteen random 5+5 draws from the pool of labelled variants
reproduce **0.9998–1.0000** of the labels. The supervision *orients* the
answer — it decides which pole gets called "Cluster 1" — rather than determining
its structure, exactly as on JAK1. So the hand-made rule above is **not load
bearing**, and that is the main reason it was acceptable to invent one.

## Features: 8, not 11

| included | source | coverage |
|---|---|---|
| ESM-1b LLR | `build_esm1b.py` | 100% |
| AlphaMissense | `build_alphamissense.py` | 100% |
| CADD phred | `build_dbnsfp.py` | 31.1% |
| FoldX ΔΔG (standing in for "MutFunc") | `build_foldx.py` | 94.6% |
| SIFT | `build_dbnsfp.py` | 31.1% |
| PolyPhen-2 HumVar | `build_polyphen.py` | 100% |
| BLOSUM62 | `build_blosum62.py` | 100% |
| ClinPred | `build_dbnsfp.py` | 31.1% |

**Excluded: `ddg_closed`, `ddg_open`, `ddg_delta`** — the three dual-state Rosetta
ΔΔG columns. No dual-state Rosetta run exists for JAK2; producing one needs an
open and a closed JAK2 model plus the ~CPU-weeks of ΔΔG that `data/ddg/` documents
for JAK1. Hence the version name `v1_wo_ddg_oc` ("without ΔΔG open/closed").

On JAK1 those three were the **weakest** features in the set — `ddg_delta` scored
AUC 0.4966, i.e. nothing, and *dropping all three improved* agreement with the
published clustering (ARI 0.484 → 0.492). So the loss is real but likely small.
A v2 with the conformational axis remains the obvious next step.

### Unexamined choices
- **Equal feature weights.** The paper's weights are unpublished.
- **PolyPhen-2 HumVar, not HumDiv.** The paper does not say which model. Both were
  computed (`jak2_polyphen2_humvar.csv`, `..._humdiv.csv`); they disagree on 23.4%
  of JAK2 variants. On JAK1 this single choice moved the result more than any
  other. It is recorded, not resolved.
- **FoldX from the committed extract**, not fresh from EBI — see
  `build_foldx_jak2_info.md` for the blocked source and the MutFunc alternative.

## Validation — against data no feature saw

- **gnomAD** (1,498 of these substitutions observed): C1 9.91% vs C2 5.30%,
  Fisher p = 8.5 × 10⁻³⁶, pooled **OR 1.96**. But the pooled figure is
  **confounded**: 100% of gnomAD-matched variants are inside the 31.1%
  dbNSFP-reachable subset, and C1 is disproportionately inside it (37.3% vs
  27.6%) — Simpson's paradox, the same trap caught on JAK1. Stratifying by
  reachability gives **Mantel–Haenszel OR 1.52**, which is the number to quote.
  Weaker than JAK1's 2.32, plausibly because this clustering has no ΔΔG axis.
  **Not** controlled for CpG mutability (CpG sites mutate ~10× faster).
- **ClinVar**: 347 JAK2 missense records, of which 305 are "Uncertain
  significance", leaving 21 usable labels. **19/21 placed correctly** — 7/7
  pathogenic in C2, 12/14 benign in C1 (the two misplaced are `L383V` and
  `Y1021F`). **10 of the 21 are seeds** — they were chosen from ClinVar, as the 5 highest-AF
  benign and the 5 best-reviewed pathogenic — so the honest score on unseen labels is **9/11**. Critically **V617F lands in the damaging cluster** — the canonical
  JAK2 gain-of-function mutation, and the one result that would have invalidated
  the exercise had it come out the other way.

## Errors hit

- **`numpy.DTypePromotionError`** in the first version of the label assignment:
  `np.where(labels==0, 1, np.where(labels==1, 2, ""))` mixes `int` and `str`, which
  numpy refuses to promote. The nested ternary was pointless anyway — nothing is ever
  unassigned, since every variant has at least one feature (`none: 0` in the coverage
  report) — so it collapsed to `labels + 1`.

No other error survived into the record. The two things worth noting as *avoided*
rather than hit:

- **Seeds are resolved by variant string**, not by row position, and the script
  prints a sequence check of all 10 against `JAK2_O60674_1132aa.txt` before
  clustering (all 10 `sequence OK, in data: True`). Pinning by index against a
  stale universe file is the obvious way to silently pin the wrong variants.
- **Feature ranges use `nanmax − nanmin`**, i.e. observed values only. Taking the
  range before masking would have let the single FoldX outlier (range 74.02, one
  clashing substitution) compress every other FoldX value into the bottom few
  percent of [0, 1]. The outlier is kept rather than winsorised — the Gower mean
  over 8 features dilutes it, and a cutoff would be an undocumented judgement call.

## Timing and sizes

Measured on this machine (re-run 3 November 2026 to record it):

| step | time |
|---|---|
| **whole script**, including the 15-draw seed-sensitivity check | **1.6 s** wall (2.6 s user) |

Peak memory is a few hundred MB. It is this fast because **no pairwise distance
matrix is ever formed**: `gower()` compares all 21,508 variants against the 2
centroids, so each iteration is O(n · k · features) — 21,508 × 2 × 8 — not O(n²).
A naive pairwise Gower on 21,508 variants would be 2.3 × 10⁸ pairs and would not
fit comfortably in memory.

Outputs: `jak2_clustering_v1.csv` 1.27 MB, `jak2_clustering_v1_config.json` 1.1 KB.

## Reproduce

```bash
python3 cluster_jak2.py          # -> jak2_clustering_v1.csv + _config.json
python3 analyse.py               # -> jak2_clustering_v1_stats.json + .npy arrays
python3 plots.py                 # -> figs/*.png
python3 build_html.py            # -> jak2_clustering_v1_wo_ddg_oc.html
```

See `build_report_jak2_info.md` for the report stage.
