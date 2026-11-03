# How the JAK1 clustering report is built

Companion to [`build_report.py`](build_report.py), which produces
[`jak1_clustering_analysis.html`](jak1_clustering_analysis.html). Written 3 November 2026.

The report is a **single self-contained HTML file**: all ten figures are inlined as base64 PNGs, so
it opens from disk with no server, no network and no image directory. 1.0 MB. GitHub will not render
it — download it, or use `htmlpreview.github.io`.

---

## 1. Running it

```bash
cd JAK1/clustering
python3 build_report.py              # everything, ~40 s including the gnomAD fetch
python3 build_report.py --no-fetch   # skip the network step, ~6 s
```

`--no-fetch` reuses the committed `jak1_gnomad.csv`. Use it unless you want fresh gnomAD data;
gnomAD releases change allele counts, so a refetch will move the numbers slightly.

Requires `numpy`, `scipy`, `pandas`, `matplotlib`, and `openpyxl` only if you also rebuild from the
EV1 spreadsheet.

## 2. The eight steps, and why the order is load-bearing

| # | script | writes | notes |
|--:|---|---|---|
| 1 | [`build_gnomad.py`](build_gnomad.py) | `jak1_gnomad.csv`, `jak1_gnomad.json` | **network.** Documented separately in [`build_gnomad_jak1_info.md`](build_gnomad_jak1_info.md) |
| 2 | [`analyse.py`](analyse.py) | `stats.json`, `X/pap/reb/ing/gaf/ncov.npy` | per-feature AUC, raw enrichment, and the cached arrays everything downstream reads |
| 3 | [`derive_stats.py`](derive_stats.py) | **extends** `stats.json` | stratified odds ratios, ARI by subset, disagreement tables, the windowed anticorrelation |
| 4 | [`plots.py`](plots.py) | 5 figures | histograms, correlation matrix, AUC, gnomAD enrichment, AF gradient |
| 5 | [`plots2.py`](plots2.py) | 3 figures | disagreement, stratified ARI, along the protein |
| 6 | [`plots3.py`](plots3.py) | 1 figure | AUC on matched subsets |
| 7 | [`plots4.py`](plots4.py) | 1 figure | pooled vs stratified OR, external ARI |
| 8 | [`build_html.py`](build_html.py) | the HTML | reads `stats.json` and `figs/*.png`, inlines everything |

**Step 3 must follow step 2, and this is the pipeline's one real trap.** `analyse.py` rewrites
`stats.json` *from scratch* on every run. Anything added to it afterwards is destroyed the next time
step 2 runs. During development that happened twice: `build_html.py` died with
`KeyError('auc_subsets')` because a re-run of `analyse.py` had wiped the keys a later step had
added. `derive_stats.py` exists as a separate file, rather than as code pasted into a session, so
that the extension step is reproducible rather than something a person has to remember.
`build_report.py` exists so nobody has to know any of this.

The four `plots*.py` files are split by when they were written, not by any principle. They are
independent of each other and can run in any order, provided steps 2 and 3 are done.

## 3. What goes into the figures

All eleven features are oriented so that **larger means more damaging** before any AUC or
correlation is computed:

```python
SIGN = {"esm1b": -1, "alphamissense": 1, "ddg_closed": -1, "ddg_open": -1, "ddg_delta": -1,
        "cadd": 1, "foldx": 1, "sift": -1, "polyphen2": 1, "blosum62": -1, "clinpred": 1}
```

The three Rosetta ΔΔG columns are negative because this project computes ΔΔG = ΔG_WT − ΔG_mut, so
**negative = destabilising** — the opposite of FoldX in the same table
(`build_rosetta_ddg_jak1_info.md` §2). Getting that wrong is not a cosmetic error: scored with the
wrong sign, `ddg_closed` appears to have AUC 0.26; oriented correctly it is
0.7409. An early version of this pipeline had it backwards
and reported the ΔΔG features as anti-predictive.

## 4. Two analysis decisions worth knowing before reading the output

**AUC is computed on each feature's own non-missing rows.** So a column headed "all variants" is
6,873 rows for ClinPred, CADD and SIFT and 21,926 for the rest — the rows are *not* comparable. The
report prints the effective `n` under every value and provides matched-subset columns where every
feature is scored on identical variants. That is where the ranking changes: AlphaMissense
0.947 overtakes ClinPred
0.9463.

**Two of the ARI stratifications are circular and are labelled as such.** `strat` splits on
AlphaMissense, which is itself one of the eleven clustering features, so selecting variants where it
is decisive selects variants both clusterings agree on. `strat_external` splits only on variables
outside the feature set — gnomAD observation, and feature count, which is fixed by codon
reachability rather than by any score. The report leads with the external figures
(0.637 observed in gnomAD, 0.679 at high coverage)
and presents the circular 0.786 as an upper bound.

## 5. The figures

| file | shows |
|---|---|
| `hist_by_cluster.png` | all 11 feature distributions, split by EV1 cluster |
| `corr.png` | Spearman correlation, oriented |
| `auc.png` | per-feature AUC against both clusterings |
| `auc_subsets.png` | the same on matched subsets — the fair comparison |
| `gnomad_enrich.png` | % of each cluster observed in gnomAD |
| `gnomad_af.png` | % called damaging, by allele-frequency band |
| `gnomad_strat.png` | pooled vs Mantel–Haenszel OR; ARI on external strata |
| `along_protein.png` | damaging fraction and gnomAD rate in 25-residue windows |
| `disagreement.png` | disagreement by coverage, and band × coverage |
| `ari_strat.png` | ARI by subset |

They are committed to [`figs/`](figs) as well as inlined, so they can be reused without extracting
base64.

## 6. Regenerating after a data change

Any change to `jak1_clustering_rebuilt.csv` or `jak1_gnomad.csv` needs the **full** sequence from
step 2, not just `build_html.py` — the `.npy` caches and `stats.json` both go stale. `build_report.py`
is the safe way to do it. The HTML is deterministic given the inputs, so a clean re-run should
reproduce the committed file byte for byte apart from the generation date.

## 7. Related material

- [`build_gnomad_jak1_info.md`](build_gnomad_jak1_info.md) — the gnomAD feature, its two exclusions,
  and the Simpson's paradox in the pooled enrichment
- [`clustering_jak1_results.md`](clustering_jak1_results.md) — the clustering itself, and the
  per-variant comparison with the paper
- [`README.md`](README.md) — directory conventions, file inventory, open items
