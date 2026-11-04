# JAK3 variant clustering

All **11** features over all **21,356** JAK3 missense substitutions (UniProt P52333, 1,124 aa),
by the method applied to JAK2 and TYK2. 4 November 2026.

- **[`jak3_clustering_report.html`](jak3_clustering_report.html)** — the full report with figures
- **[`protein_models/jak3_models_3d.html`](protein_models/jak3_models_3d.html)** — interactive 3D structures

| | |
|---|---|
| C1 tolerant / C2 damaging | **9,436 / 11,920** |
| converged | 10 iterations |
| gnomAD Mantel–Haenszel OR | **1.53** |
| **ClinVar** | **40 of 41** correct (**30 of 31** excluding seeds) |

---

## 1. The headline: this is the best-validated clustering of the three

**40 of 41 usable ClinVar labels are placed correctly** — 22 of 23 Pathogenic/Likely-pathogenic
in the damaging cluster, 18 of 18 Benign/Likely-benign in the tolerant one. Excluding the 10
labels used as seeds, the honest out-of-sample score is **30 of 31**.

The single miss is **`R403H`**. Its neighbour `R403C` at the same position *is* placed correctly
and is a seed, so the clustering separates two substitutions at one residue — which is the kind
of discrimination it generally cannot make.

Compare: JAK2 scored 19/21 overall and 9/11 unseen; TYK2 had only two Pathogenic records to test
against. JAK3's ClinVar is far richer — 23 Pathogenic/Likely-pathogenic records, most 3-star
("reviewed by expert panel").

**But the comparison is not like-for-like, and the reason matters.**

## 2. Why JAK3 is an easier problem

**JAK3's pathogenic variants are loss of function.** They cause SCID. JAK2's are *gain* of
function — myeloproliferative neoplasms. Every feature in this set is trained or calibrated on
protein damage: ClinPred, PolyPhen-2, CADD, SIFT, AlphaMissense, ESM-1b, FoldX and ΔΔG all ask
"does this break the protein". For JAK3 that is exactly the right question. For JAK2 it is the
wrong one, which is why AlphaMissense puts V617F at the 37th percentile and misses half the known
activating alleles.

So **40/41 should not be read as the method working better on JAK3**. It is the method being
asked an easier question. The honest summary across the family:

| | JAK2 | TYK2 | JAK3 |
|---|---|---|---|
| pathogenic mechanism | **gain** of function | mixed | **loss** of function |
| best external validation | 19/21 ClinVar | **AUC 0.64–0.68** vs DMS | **40/41 ClinVar** |
| gnomAD MH OR | 1.54 | 1.52 | **1.53** |

The gnomAD depletion is **remarkably consistent** at 1.52–1.54 across all three — that is the
same measurement on the same scale, and it says the clusterings have comparable, modest power to
separate variants that survive in the population from ones that do not.

## 3. Per-feature summary

ΔΔG sign: `ΔΔG = ΔG_WT − ΔG_mut`, **negative = destabilising** (opposite to FoldX).

| feature | coverage | C1 mean | C2 mean | AUC |
|---|--:|--:|--:|--:|
| ClinPred | 31.0% | 0.371 | 0.956 | 0.972 |
| PolyPhen-2 HumVar | 100.0% | 0.170 | 0.842 | 0.959 |
| CADD | 30.9% | 14.035 | 27.098 | 0.957 |
| AlphaMissense | 100.0% | 0.222 | 0.719 | 0.925 |
| SIFT | 31.0% | 0.288 | 0.025 | 0.904 |
| ESM-1b | 100.0% | −7.850 | −13.129 | 0.860 |
| FoldX ΔΔG | 93.9% | 0.796 | 3.237 | 0.749 |
| **ΔΔG open** | 100.0% | −21.627 | −83.663 | 0.714 |
| **ΔΔG closed** | 100.0% | −21.171 | −78.771 | 0.712 |
| BLOSUM62 | 100.0% | −0.999 | −1.748 | 0.646 |
| **ΔΔG delta** | 100.0% | −0.457 | −4.892 | **0.527** |

Circular — these are the features the clustering was built from.

### ΔΔG delta, now on a fourth protein

| protein | `ddg_delta` AUC |
|---|--:|
| JAK1 | 0.4966 |
| JAK2 | 0.499 |
| TYK2 | 0.502 |
| **JAK3** | **0.527** |

Four proteins, four independent model sets, four results at or within noise of chance. JAK3's
0.527 is the highest of them and still carries essentially nothing. On JAK2 the second model pair
additionally showed the values do not reproduce when the structures change (r = 0.074).
**The conformational difference feature does not work.**

`ddg_closed` and `ddg_open` correlate at **0.849** — effectively one general destabilisation term,
which FoldX already supplies at AUC 0.749.

## 4. The ΔΔG run

Computed fresh, locally, with PyRosetta on 4 November 2026: **21,356 variants, 100%**, 39.4 min at
32,500 variants/h after ~75 min of FastRelax on the two states.

| state | model | predictor | template | FERM–JH1 | JH1 vs AFDB closed |
|---|---|---|:-:|--:|--:|
| closed | `jak3_af3_notemplate_closed_model0.pdb` | AF3 | none | 40.7 Å | **0.82 Å** |
| open | `JAK3_20261016_172413/selected_open.pdb` | OpenFold | none | 94.1 Å | 82.12 Å |

**Both states were measured, not trusted.** 14 of JAK3's 30 `selected_*.pdb` files are
mislabelled, and three OpenFold runs produced *compact* models sitting **15–16 Å from the
autoinhibited arrangement** — collapsed into some other state. FERM–JH1 distance alone would have
accepted all three.

**The pair is confounded across predictors** (AF3 closed, OpenFold open), but mildly: every
per-domain RMSD between the two states is **0.31–0.93 Å**, against 5.47 Å for TYK2's FERM domain.
These two structures really are related by a motion of JH1 and little else.

**JAK3 has no experimental closed structure**, so the reference is the AlphaFold DB model — which
is itself closed. That is notable in its own right: the AFDB model is closed for JAK3 and TYK2 and
**open** for JAK2, so the default AlphaFold state is not constant across this family.

## 5. What this is, and what it is not

- **Not a reproduction** — there is no published JAK3 clustering.
- **40/41 reflects an easier question**, not a better method (§2).
- **`ddg_delta` is inert**, on a fourth protein.
- **No DMS**, unlike TYK2, so there is no calibration here against measured function. TYK2's
  AUC of 0.64–0.68 is the best estimate of what a clustering like this is actually worth, and
  nothing about JAK3 supersedes it.
- **PolyPhen-2 HumVar, not HumDiv**; equal feature weights; FoldX at 93.9%; the gnomAD test is not
  CpG-mutability controlled.

## Files

| file | what |
|---|---|
| `build_*.py` | one per feature |
| `collect_jak3.py`, `build_ddg.py` | the ΔΔG run's results → features |
| `cluster_jak3.py` | the 11-feature clustering |
| `analyse_jak3.py` → `stats_jak3.json` | every number |
| `plots_jak3.py` → `figs_jak3/` | the figures |
| `build_html_jak3.py` → `jak3_clustering_report.html` | the report |
| `protein_models/` | structures, geometry, PAE, 3D viewer |
