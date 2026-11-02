# FoldX ΔΔG for JAK1 — provenance and the caveats that come with it

Covers [`jak1_ddg_foldx_precomputed.csv`](jak1_ddg_foldx_precomputed.csv). Written 2 November 2026.

---

## 1. Where the data comes from

**Not computed in this project.** It is an extract from **EBI ProtVar**, which publishes FoldX ΔΔG
computed on **AlphaFold2** models across the human proteome.

| | |
|---|---|
| upstream | EBI **ProtVar** human-proteome FoldX set, release **2025.02.10** |
| method | **FoldX v5.0** on AlphaFold2 models |
| extract in this repo | [`../../external_data/protvar_foldx_jak_src.csv`](../../external_data/protvar_foldx_jak_src.csv) — 89,927 variants for JAK1/JAK2/JAK3/TYK2 and SRC |
| added | commit `0817a83`, 28 October 2026 |
| JAK1 (P23458) | **20,805** substitutions |
| this file | that extract reshaped into EV1 order by [`build_foldx.py`](build_foldx.py) |

So the chain is: AlphaFold2 model → FoldX v5 → ProtVar proteome release → repo extract → EV1-ordered
feature file. Nothing here ran FoldX.

ProtVar is live and the source is re-fetchable: `www.ebi.ac.uk/ProtVar/` responds, the download page
responds, and there is a Swagger UI at `/ProtVar/api/swagger-ui/index.html` for the API. (Note the
guessed endpoints `/api/mapping/{acc}/accession` and `/api/download/stream` both 404 — use the
Swagger listing rather than inventing paths.)

## 1b. mutfunc's ddG is this same number — verified across the range

mutfunc returns a `pred_ddg` column. It is the same FoldX computation, checked on a spread of
variants chosen from low, middling and extreme ddG plus some low-pLDDT positions
([`verify_mutfunc_ddg.py`](verify_mutfunc_ddg.py)):

| variant | pLDDT | ProtVar FoldX | mutfunc `pred_ddg` |
|---|--:|--:|--:|
| G1068W | 97.8 | **72.5022** | **72.5022** |
| E667M | 96.4 | −6.1182 | −6.1182 |
| A1005G | 96.2 | 1.1230 | 1.1230 |
| A1005S | 96.2 | 0.9601 | 0.9601 |
| A146E | 67.3 | 0.8096 | 0.8096 |

**Maximum absolute difference 0.000050** over the five comparable — identical to four decimals, and
agreeing even on the +72.50 clash artefact. So mutfunc and ProtVar are serving the same FoldX output
(whether one sources the other, or both ran FoldX on the same AlphaFold2 model, is not visible from
outside and does not matter in use).

**But mutfunc mapped only 6 of the 12 requested**, and the misses are not explained by model
confidence: `G1068Y` and `G1068F` are absent at pLDDT 97.8 while `G1068W` at the same position is
present. Coverage is patchy per *substitution*, not merely per position, for reasons not visible
externally. Which is the practical argument for taking FoldX from ProtVar: **94.9% against roughly
8%, for numbers that are bit-for-bit the same where both exist.**

## 2. Coverage, and what the gaps are

| | |
|---|--:|
| populated | **20,805 of 21,926 (94.9%)** |
| positions covered | **1,095 of 1,154** |
| positions with nothing | **59** |

The 59 uncovered positions are the **disordered N-terminus** (1–20 and similar stretches) where the
AlphaFold model has no usable structure. Blank means *"no structural model"*, not *"no effect"* — the
gap is systematic, so imputing zero there would assert tolerance that was never computed.

## 3. The pLDDT warning, quantified

The commit that added the extract records a detail that is easy to miss:

> *Includes per-position pLDDT — filter >= 70, the 2025 file no longer does.*

Older ProtVar releases excluded low-confidence positions; **the 2025.02.10 release does not**. So
this file contains values computed on parts of the model that are barely modelled, and the `plddt`
column is there so they can be filtered.

| | n | share | median ΔΔG | mean | max |
|---|--:|--:|--:|--:|--:|
| **pLDDT ≥ 70** | 19,133 | 92.0% | **1.278** | 2.285 | 72.50 |
| **pLDDT < 70** | 1,672 | 8.0% | **0.208** | 0.465 | 15.47 |
| pLDDT < 50 | 532 | 2.6% | | | |

Low-confidence rows span **88 positions**, and they are not noisy outliers — they are
**systematically near zero** (median 0.21 against 1.28). That is the more dangerous failure mode: a
residue in a disordered region has nothing to pack against, so FoldX reports almost no
destabilisation, which reads as *"tolerated"* when the truth is *"the model cannot say"*.

**Recommendation: filter on `plddt >= 70` before use**, restoring the behaviour of the older ProtVar
releases. That costs 8% of rows and removes a bias toward false tolerance.

## 4. Sign convention — opposite to this project's other ΔΔG

**FoldX: positive = destabilising.** The PyRosetta ΔΔG in `data/ddg/` uses
ΔΔG = ΔG_WT − ΔG_mut, so **negative = destabilising** there. The two are on opposite axes.

Combining them without flipping one would place two stability features in opposition, and in a Gower
distance that is not a visible error — it simply degrades the result. Same trap as SIFT, where low
means damaging while every other predictor here has high meaning damaging.

## 5. FoldX produces clash artefacts too

ΔΔG range is **−6.31 to +72.50 kcal/mol**, median **+1.135**.

No folding free energy approaches 72 kcal/mol. These are **steric-clash artefacts**, exactly as
diagnosed for PyRosetta in `conclusions_ddG_difference_feature.md` §§8–10: a rigid backbone cannot
accommodate a larger residue, so the repulsive term saturates and the result wears the units of an
energy without being one.

**170 substitutions exceed 20 kcal/mol — and all 170 are in pLDDT ≥ 70 regions.** So the extremes
are not a model-quality problem; they come from confidently modelled, well-packed cores, which is the
same signature found for Rosetta (buried positions that cannot host a bulky residue). Filtering on
pLDDT does not remove them and should not be expected to.

**Rank these values; do not read the tail as kcal/mol.** The median of 1.135 is the honest scale.

## 6. The file

```csv
variant_id,wt,pos,alt,cluster,foldx_ddg,plddt,high_confidence
```

23,080 rows, EV1 order, conventions as in the [README](README.md): `variant_id` index, empty field
for missing. One value per substitution — **zero duplicates**, so unlike ClinPred, REVEL and CADD
there is no aggregation choice to document.

| column | meaning |
|---|---|
| `foldx_ddg` | FoldX v5 ddG, kcal/mol, **positive = destabilising** |
| `plddt` | AlphaFold per-position confidence at that residue |
| `high_confidence` | **1** where `plddt >= 70`, **0** below, blank where there is no ddG — the filter the 2025 ProtVar release stopped applying (§3) |

| | n |
|---|--:|
| populated | 20,805 (94.9% of real substitutions) |
| `high_confidence = 1` | **19,133** (92.0% of populated) |
| `high_confidence = 0` | 1,672 |
| blank | 2,275 (1,154 self-substitutions + 1,121 positions with no model) |

Median ddG is **1.278** among high-confidence rows against **0.208** among low — the bias toward
false tolerance, in one line. Filtering on `high_confidence == 1` is the recommended default.

## 7. Related data already in the repository

| file | contents |
|---|---|
| `external_data/protvar_foldx_jak_src.csv` | the source extract, all four JAKs plus SRC |
| `external_data/thermompnn_jak_src.csv` | **ThermoMPNN** ΔΔG — complete 21,508 for JAK2, an independent and better-benchmarked stability predictor |
| `data/ddg/jak2_variants_multimethod.csv` | FoldX next to ThermoMPNN, mCSM and DDMut for 24 JAK2 variants |
| `data/ddg/ddg_JAK1_all.json` | the project's own PyRosetta dual-state ΔΔG (opposite sign convention) |

Worth knowing for feature selection: on 386 held-out human measurements recorded in
`data/ddg/README.md`, **ThermoMPNN reached r = +0.517 and FoldX +0.388**. ThermoMPNN is both more
accurate and complete for JAK2, so if only one stability feature is wanted it is the stronger choice
— FoldX is used here because it is what mutfunc's Stability column is, which is what the paper's
"MutFunc score" most plausibly referred to.
