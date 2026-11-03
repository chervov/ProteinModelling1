# How to build the HTML reports — and the ways that went wrong

A working guide for `JAK2/clustering/`, written 3 November 2026 after building
`jak2_clustering_v1_wo_ddg_oc.html` and `protein_models/jak2_models_3d.html`. The wrong ways
listed here are **not hypothetical** — every one of them shipped at least once in this directory
and had to be fixed. They are recorded so the next report does not repeat them.

Applies equally to `JAK1/clustering/` and `more_proteins/top10/`.

---

## The pipeline

Three stages, always, never two:

```
analyse.py   data  ->  stats.json      every number, computed once
plots.py     stats ->  figs/*.png      every figure
build_html.py stats + figs -> report.html   layout only, no arithmetic
```

```bash
cd JAK2/clustering
python3 analyse.py && python3 plots.py && python3 build_html.py     # ~4 s total
```

For the structural report the same shape, in `protein_models/`:
`analyse_models.py` → `model_analysis.json` → `plot_models.py` → `build_3d.py`.

### Why three and not one

**No arithmetic inside the template.** The template reads `stats.json` and formats; it never
computes. An earlier JAK1 version had statistics inlined in f-strings throughout the template,
and when a defect was found in the gnomAD handling there was no way to tell which printed numbers
were affected without re-reading the whole file. `stats.json` is committed alongside the report so
every figure in the prose is auditable against one machine-readable record.

---

## The seven wrong ways

### 1. Pinning a CDN version that does not exist

```html
<!-- WRONG: cdnjs has no plotly.js 2.35.2; its mirror stops earlier -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.35.2/plotly.min.js"></script>
```

The page rendered **blank**, with nothing but `ReferenceError: Plotly is not defined` in a console
nobody was looking at. A version existing on one CDN says nothing about another.

**Right:** check the URL returns 200 before committing, and prefer the library the repository
already uses — `more_proteins/top10/*.html` was on 3Dmol.js the whole time.

```bash
curl -sS -o /dev/null -w "%{http_code} %{size_download}B\n" "<the exact URL>"
```

### 2. A relative dependency on a sibling file

```html
<!-- WRONG: breaks the moment the html is copied anywhere on its own -->
<script src="vendor/plotly-2.27.0.min.js"></script>
```

This is worse than the CDN bug because it works on the machine that built it. It broke as soon as
the file was copied to `~/Downloads` — which is the normal way to share a report.

**Right: a report is one file.** Inline the library and base64 every image. These pages exist to
be emailed, archived and opened years later; a page whose purpose is to be passed around must have
no sibling dependency, no network call and no CDN. `vendor/` is a build-time cache only, fetched
on demand and gitignored.

Cost check before inlining: 3Dmol is 0.5 MB, Plotly 3.6 MB. That alone is a reason to prefer
3Dmol for structures.

### 3. Assuming it rendered

Both bugs above survived because the page *looked* finished in the terminal: the build script
printed a size and exited 0. **A report is not done until something has drawn it.**

```bash
# render from an UNRELATED directory, so a sibling dependency fails the way a user would hit it
cp report.html /tmp/check/ && cd /tmp/check
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless=new --enable-unsafe-swiftshader --use-gl=angle --use-angle=swiftshader \
  --virtual-time-budget=30000 --window-size=1250,1500 \
  --screenshot=/tmp/check/shot.png "file:///tmp/check/report.html"
```

`--enable-unsafe-swiftshader` matters: plain headless Chrome has **no WebGL**, and every 3D panel
comes out blank with "WebGL is not supported by your browser" — which looks exactly like a broken
page and is not one. Without software rendering you cannot tell the two apart.

Check the console too, not just the pixels. A page can look fine and still be throwing.

### 4. Doing mathematics in the browser

```js
// WRONG: a hand-rolled Kabsch via power-iteration polar decomposition
function svdRot(C){ let R=C.map(r=>r.slice()); for(let it=0;it<60;it++){ ... } return R }
```

This is the most dangerous category, because it does not fail — it returns a plausible-looking
*wrong* rotation and the picture still looks like a protein.

**Right:** compute in Python where numpy's SVD is already correct and the result is checkable, and
inline the fitted coordinates. `build_3d.py` prints `JH2 fit RMSD 0.37 A over 265 residues` on every
build, which is a number that would move if the fit broke.

### 5. Paths relative to the current directory

```python
b = open(f"figs/{name}.png", "rb")                      # WRONG: depends on cwd
C = json.load(open("/Users/chervov/.../config.json"))   # WRONG: depends on the machine
```

Developed in a scratch directory, these ran from exactly one place.

```python
HERE = pathlib.Path(__file__).parent        # RIGHT
S = json.load(open(HERE / "stats.json"))
b = (HERE / "figs" / f"{name}.png").read_bytes()
```

### 6. Escaping in the wrong order

```python
esc(p.replace("|", " &harr; "))   # WRONG: escapes the & of the entity just inserted
esc(p).replace("|", " &harr; ")   # RIGHT
```

Printed `&harr;` as literal text across several reports before anyone noticed.

### 7. Letting the layout lie

Three real cases, all of which produced a page that was technically correct and visually
misleading:

- **Per-panel autoscaling.** Each 3D panel scaled to its own extent made the compact closed state
  and the extended open state look the same size — the one thing the figure existed to show. Fixed
  with a single `GLOBAL_R` shared by every panel.
- **Missing image CSS.** Without `figure img{width:100%;height:auto}` the embedded PNGs rendered at
  natural size and ran off the right edge of the page.
- **A mislabelled column.** An AUC table headed "all variants" was computed on each feature's own
  non-missing rows — 6,873 for ClinPred, not 21,926. Renamed to "own coverage" with the effective
  *n* printed beside it. **If a column header could be read two ways, the figures underneath are
  wrong for one of those readings.**

---

## Rules for the page itself

**Self-contained.** One file. Library inlined, images base64. The only external reference allowed
is a Google Fonts stylesheet, and only with a real fallback stack so it degrades offline.

**Static first.** Put the matplotlib figures *above* the interactive panels. WebGL is unavailable
in headless browsers, some remote desktops and locked-down machines; the figures and the numbers
must survive that. Give the interactive section a fallback that says so rather than a blank box.

**Theme-aware.** Define every colour as a token on `:root`, redefine under
`@media (prefers-color-scheme: dark)` guarded by `:root:not([data-theme="light"])`, and again under
`:root[data-theme="dark"]`. Set an explicit `background` on `body` — a transparent body shows the
host's theme behind your text.

**Responsive.** 16 px side gutter at every width, no horizontal page scroll, wide tables in their
own `overflow-x:auto` container.

**Say what the numbers cannot do.** Every report here carries its own caveats in the prose:
that per-feature AUCs computed on the clustering's own features are circular; that a pooled odds
ratio is confounded and the Mantel–Haenszel one is the figure to quote; that a model 0.33 Å from
its own template is not independent evidence. A report that only states results is less useful
than one that states what would invalidate them.

---

## Checklist before committing a report

```
[ ] analyse.py -> plots.py -> build_html.py run clean from an empty shell
[ ] every number in the prose traceable to stats.json, none computed in the template
[ ] no cwd-relative or absolute paths; everything via pathlib.Path(__file__).parent
[ ] single file: no sibling dependency, no CDN, no network
[ ] every external URL used at build time checked for 200
[ ] rendered from an unrelated directory with headless Chrome + swiftshader
[ ] browser console clean
[ ] readable at 400 px wide; no horizontal page scroll
[ ] both light and dark themes checked
[ ] shared scale on any set of panels meant to be compared
[ ] every column header says exactly what was counted
[ ] regenerable intermediates (.npy, merged.csv) gitignored, stats.json committed
```

## Related

- [`build_report_jak2_info.md`](build_report_jak2_info.md) — the clustering report specifically
- [`cluster_jak2_v1_info.md`](cluster_jak2_v1_info.md) — the clustering behind it
- [`protein_models/README.md`](protein_models/README.md) — the structural report and its three rebuilds
- [`../../JAK1/clustering/build_report_jak1_info.md`](../../JAK1/clustering/build_report_jak1_info.md) — the JAK1 equivalent
