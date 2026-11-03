# The JAK2 clustering report — `analyse.py` → `plots.py` → `build_html.py`

Human-readable companion to the three scripts that turn `jak2_clustering_v1.csv`
into `jak2_clustering_v1_wo_ddg_oc.html`. Mirrors
`../../JAK1/clustering/build_report_jak1_info.md`.

## The three stages, and why they are three

| script | reads | writes | time |
|---|---|---|---|
| `analyse.py` | `jak2_clustering_v1.csv`, `jak2_gnomad.csv`, `jak2_clinvar.csv` | `stats.json` (4.5 KB) + 5 `.npy` arrays | 1.3 s |
| `plots.py` | the `.npy` arrays + `stats.json` | `figs/*.png` (5 files, 324 KB) | 1.0 s |
| `build_html.py` | `stats.json`, `figs/*.png`, `jak2_clustering_v1_config.json` | `jak2_clustering_v1_wo_ddg_oc.html` (436 KB) | 0.02 s |

Split this way for one reason: **every number in the report comes out of
`stats.json`, and nothing is computed inside the HTML template.** On JAK1 an
earlier monolithic version had statistics inlined in f-strings in the template,
and when a defect was found in the gnomAD handling there was no way to tell which
printed numbers were affected without re-reading the whole template. Now
`stats.json` is the single auditable record, and it is committed alongside the
report.

The `.npy` intermediates (`X`, `cl`, `ing`, `ncov`, `pos`) let `plots.py` be
re-run — restyling a figure, changing a bin width — without redoing the
statistics. They are **not committed** (`.gitignore`): `analyse.py` rewrites them
in 1.3 s, so there is no reason to version 2 MB of float arrays.

## What `analyse.py` computes

- **Per-cluster feature summary** — for each of the 8 features: n, coverage, mean,
  median, SD per cluster, the difference, Cohen's *d* (pooled SD), Mann–Whitney U
  p, and AUC. This is the table the report leads with.
  **These AUCs are circular** and the report says so: they are the features the
  clustering was built from, so they describe the split rather than test it.
- **gnomAD enrichment, pooled and stratified.** Fisher exact on the 2×2, then a
  **Mantel–Haenszel odds ratio** stratified by dbNSFP reachability. The pooled OR
  (1.96) and the MH OR (1.52) differ because 100% of gnomAD-matched variants sit
  inside the 31.1% dbNSFP-reachable subset while the tolerant cluster is
  disproportionately inside it (37.3% vs 27.6%) — Simpson's paradox. The MH figure
  is the one to quote. This is the exact defect found by self-audit on JAK1
  (pooled 2.89 → MH 2.32), so it is computed both ways here from the start.
- **ClinVar spot check** — 19/21 usable labels placed correctly, with the honest
  14/16 figure after removing the 5 variants that were seeds.
- **The 28-variant literature panel** (`S["panel"]`) — the supplied reading list in its three
  groups, each variant's cluster, all 8 feature values, domain, and gnomAD status. Every WT
  residue is asserted against `JAK2_O60674_1132aa.txt` at build time, so a mislabelled variant
  fails the build rather than printing a wrong row.
- **Per-domain and per-coverage breakdowns**, and damaging fraction in 25-residue
  windows along the protein.

## What `plots.py` draws

| figure | what it shows |
|---|---|
| `cluster_means.png` | per-cluster means, **standardised**, so 8 features on 8 different scales are comparable on one axis. The headline figure — it is what "how do the clusters differ" looks like. |
| `distributions.png` | per-feature histograms by cluster, which is where the bimodality of AlphaMissense/PolyPhen-2/ClinPred and the heavy overlap of BLOSUM62/FoldX become visible. |
| `auc.png` | per-feature AUC, ranked. |
| `gnomad.png` | observed-in-gnomAD percentage per cluster, beside the pooled-vs-stratified OR. |
| `along_protein.png` | damaging fraction and gnomAD rate in 25-residue windows, with domains shaded and V617F marked. |

matplotlib only, `Agg` backend, no seaborn — one less pinned dependency, and the
figures are simple enough not to need it.

### The panel's threshold highlighting

`S["panel_thresholds"]` holds the damaging-direction cutoffs, and `build_html.py` turns each cell
into one of three states — plain, light yellow, strong yellow:

| predictor | damaging | stringent |
|---|--:|--:|
| ESM-1b | < −7.5 | — |
| AlphaMissense | > 0.564 | — |
| CADD phred | ≥ 25 | ≥ 30 (top 0.1%) |
| PolyPhen-2 | ≥ 0.447 (possibly damaging) | ≥ 0.909 (probably damaging) |
| SIFT | ≤ 0.05 | — |
| ClinPred | ≥ 0.5 | — |
| FoldX, BLOSUM62 | — | — |

The thresholds live in `analyse.py` and reach the template through `stats.json`, so they are
recorded with the numbers they coloured rather than buried in CSS. The comparison operator is
stored per predictor (`lt`/`gt`/`le`/`ge`) because the damaging direction is not uniform — ESM-1b
and SIFT go down, the rest go up, and hard-coding `>` is the obvious way to silently invert half
the table. FoldX and BLOSUM62 are deliberately uncoloured: neither has a cutoff of this kind,
and inventing one would make the table look more decided than the evidence is.

Two tiers are shown only where the predictor itself defines two. The yellows are set in `rgba`
over the surface token rather than as flat hex, so they stay legible in both themes; the strong
tier also pins dark text, since a 78%-opacity yellow under dark mode would otherwise carry the
light-mode foreground.

## What `build_html.py` does

A single self-contained HTML file: figures are **inlined as base64 `data:` URIs**,
so the report can be emailed or opened from anywhere with no `figs/` directory
beside it. That is why a 324 KB figure set becomes a 436 KB page. `figs/` is still
committed, for reuse in slides and for diffing.

The page is theme-aware (light/dark via `prefers-color-scheme` plus
`[data-theme]`), responsive to phone width, and uses no external JavaScript.
One external stylesheet (Google Fonts) with a real serif/sans fallback stack, so
it degrades correctly offline.

### Errors hit
- **Hard-coded absolute paths.** The first version opened
  `/Users/chervov/ProteinModelling1/JAK2/clustering/jak2_clustering_v1_config.json`
  and `figs/<name>.png` relative to the *current directory*, because it was
  developed in a scratch directory outside the repo. It therefore only ran from
  one place. Now everything resolves from `pathlib.Path(__file__).parent`, so the
  three scripts run from any working directory. This is the same trap as the JAK1
  report.
- **HTML entities rendering literally** (carried over from the JAK1 reports):
  `esc(p.replace("|", " &harr; "))` escapes the ampersand of the entity it just
  inserted, printing `&harr;` as text. The escape must come first —
  `esc(p).replace(...)`.
- **A status string where a float was expected.** On the JAK1/top-10 side, a
  `wt_mismatch` marker in a JSON field reached arithmetic and raised
  `TypeError: unsupported operand type(s) for -: 'float' and 'str'`. Guarded here
  by `num()`/`stat()` helpers that return `None` for anything non-numeric rather
  than letting a sentinel string into a mean.

### Alternatives considered
- **Jupyter/nbconvert** — rejected: the output carries execution counts and
  styling that diff badly, and the point is a file that can be reviewed in git.
- **Quarto / Pandoc from Markdown** — rejected: adds a toolchain dependency for a
  single page, and gives less control over the theme-aware CSS.
- **Plotly or Observable for interactivity** — rejected for now: it would mean an
  external script tag and a much larger page, and the report's questions
  ("which feature separates the clusters") are answered by static figures. Worth
  revisiting if the v2 report has to carry the conformational axis.

## Reproduce

```bash
cd JAK2/clustering
python3 cluster_jak2.py   # if jak2_clustering_v1.csv is not present
python3 analyse.py
python3 plots.py
python3 build_html.py
open jak2_clustering_v1_wo_ddg_oc.html
```

Total, from the committed feature CSVs: **under 4 seconds**.
