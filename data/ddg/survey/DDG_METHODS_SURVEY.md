# ΔΔG for the JAK family — what exists, what we computed, and what it is worth

A single answer to: which methods exist, which we have, where the data is, what our own runs cost,
how the methods agree, whether RSA really substitutes for them, and whether the four-residue
outlier tail is a PyRosetta problem or a general one.

Written 5 November 2026. Numbers from [`analyse_ddg_methods.py`](analyse_ddg_methods.py) →
`ddg_survey.json`, over **87,343 substitutions** (all four proteins, complete).
Interactive version with figures: **[`ddg_methods_survey.html`](ddg_methods_survey.html)**.

---

## 1. The six findings

1. **The ΔΔG methods agree with each other only moderately** — Spearman 0.52–0.56 between
   PyRosetta and the others, 0.69–0.70 between FoldX and ThermoMPNN. Identical in all four
   proteins.
2. **RSA alone — one geometric number, no energy function — tracks ΔΔG nearly as well as the
   methods track each other** (ρ 0.49–0.61), and **beats all three of them** at separating the
   clustering's two clusters (AUC 0.77–0.82 against 0.71–0.79).
3. **The four-residue outlier tail is a PyRosetta artefact.** Proline is the extreme case:
   **92.5%** of X→P substitutions give ΔΔG < −10 in Rosetta, against **2.5%** in FoldX and
   **0.0%** in ThermoMPNN.
4. **The aromatic part of the tail is partly shared.** W/Y/F are the top three in FoldX too
   (14.1 / 11.0 / 7.0%), so the steric mechanism is real; the proline mechanism is not.
5. **Against the only experimental data we have** — the TYK2 DMS — **the sequence predictors beat
   the ΔΔG methods even on the stability arm**: AlphaMissense |ρ| 0.42, ThermoMPNN 0.30, RSA 0.29,
   FoldX 0.28, Rosetta 0.26.
6. **`ddg_delta` is noise on all four proteins** (AUC 0.497 / 0.499 / 0.502 / 0.527, |ρ| ≤ 0.02
   with everything).

---

## 2. What methods exist

Physics- and knowledge-based, then learned. Full assessment with DOIs in
[`../../external_data/ddg_literature.md`](../../external_data/ddg_literature.md) (33 resolved
DOIs, independent benchmarks tagged).

| family | methods | note |
|---|---|---|
| force field | **FoldX**, **Rosetta** `ddg_monomer` (Kellogg), Rosetta `cartesian_ddg` | cartesian_ddg is the most robust to modelling error |
| statistical potential | PoPMuSiC, mCSM, DUET, SDM, DDMut | fast, graph/environment features |
| learned, structure-aware | **ThermoMPNN**, RaSP, Stability Oracle, SPURS, ThermoNet | trained on mega-scale data |
| sequence / evolution | GEMME, EVE, TranceptEVE, ESM-2, ProSST, SaProt | not ΔΔG, but competitive on stability DMS |
| **two-feature baseline** | **RSALOR** = log-odds ratio × RSA | the point of §5 |

**The field's real ceiling.** On genuinely unseen single mutations the best methods reach
**r ≈ 0.5–0.6**, not the 0.7–0.8 advertised; the gap is training-set leakage, direct+reverse
evaluation, and random rather than homology-aware splits. Experimental noise caps the achievable
value at r ≈ 0.7–0.8. For interpreting human missense variants ΔΔG is a **weak classifier**
(AUC ≈ 0.66–0.68), because many pathogenic variants do not act by destabilisation at all. And
there is **no benchmark on large multi-domain proteins** — which is exactly what the JAKs are.

## 3. What we have, and where

### Computed by us — dual-state PyRosetta

| protein | file | n | coverage |
|---|---|--:|--:|
| JAK1 | `../ddg_JAK1_all.json` | 21,926 | 100% |
| JAK2 pair 1 | `../ddg_JAK2P1_all.json` | 21,508 | 100% |
| JAK2 pair 2 | `../ddg_JAK2P2_all.json` | 21,508 | 100% |
| JAK3 | `../ddg_JAK3_all.json` | 21,356 | 100% |
| TYK2 | `../ddg_TYK2_all.json` | 22,536 | 99.9% |

Each record: `pos, wt, alt, ddg_closed, ddg_open, delta`.
**Sign convention: ΔΔG = ΔG_WT − ΔG_mut, so negative = destabilising** — the opposite of FoldX,
ThermoMPNN and every published method. Getting this backwards once cost an inverted AUC (0.26
instead of 0.74).

### Precomputed, downloaded

| method | file | coverage |
|---|---|--:|
| **ThermoMPNN** | `../../external_data/thermompnn_jak_src.csv` | **100%** all four |
| **FoldX** (ProtVar, on AlphaFold2) | `../../external_data/protvar_foldx_jak_src.csv` | 89.5–94.6% |
| **RSA** | same ThermoMPNN file, `exposure_rasa` | 100% |
| **RSALOR** (JAK2) | `../rsalor_jak2_family.csv` | per-position |
| mCSM, DDMut, Rosetta cartesian | `../jak2_variants_multimethod.csv` | the 24-variant panel only |

Also: `../ddg_by_target_aa_{JAK1,TYK2}.csv` (the outlier tables), `../jak2_rsa.csv`,
`../kellogg_ddg_monomer.json`, `../clash_diagnosis.json`, and the family MSA
`../jak_family_msa.fasta`.

### What we tried and rejected

**A hand-built biophysical approximation** (`../ddg_approximation.md`) — reviewed in
`../ddg_approximation_review.md` and **rejected**: it cannot predict a stabilising mutation, and
carries no stability information against four established methods. Nothing depends on it.

## 4. Cost and scripts for our own runs

The worker is [`../../pipeline/ddg/worker.py`](../../pipeline/ddg/worker.py), unchanged except
`W` and `NPROC`. Design notes in
[`../../JAK2/clustering/ddg/RUNBOOK_jak2_dualstate_ddg.md`](../../JAK2/clustering/ddg/RUNBOOK_jak2_dualstate_ddg.md).

| stage | cost | note |
|---|---|---|
| **FastRelax**, per state | **~25 min** | single-threaded; cached, so paid once per structure |
| **ΔΔG**, whole protein | **~40 min** | 6 workers, ~30,000–32,500 variants/h |
| **total per protein** | **~1.5–2 h** | 2 states to relax + one ΔΔG pass |
| JAK1 + TYK2 (October) | one night | 4 molab CPU boxes, 20 cores each |
| JAK2, JAK3 (November) | local | 8-core Mac, PyRosetta in the system anaconda |

Two design points that make the cost what it is: the **WT repack is computed once per position
per state** and reused across that position's 19 substitutions (exact, ~19× cheaper), and
**positions are processed in shuffled order**, so a partial run is an unbiased sample.

**Run it:**
```bash
cp pipeline/ddg/worker.py ~/ddg_X/ && cd ~/ddg_X
# place X_closed.pdb and X_open.pdb, write jobs.json, then:
nohup python3 -u worker.py > run.log 2>&1 &
```

## 5. How the methods agree — and the RSA result

JAK2, Spearman, every feature oriented so **+ = more damaging** (Rosetta, ESM-1b and RSA negated):

| | Ros closed | Ros open | Ros delta | ThermoMPNN | RSA | FoldX | AlphaMiss | PolyPhen | ESM-1b | CADD |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **Rosetta closed** | 1.00 | 0.90 | −0.14 | 0.54 | 0.49 | 0.54 | 0.45 | 0.33 | 0.42 | 0.38 |
| **Rosetta open** | 0.90 | 1.00 | 0.13 | 0.55 | 0.52 | 0.56 | 0.46 | 0.34 | 0.42 | 0.39 |
| **Rosetta delta** | −0.14 | 0.13 | 1.00 | −0.01 | 0.01 | 0.02 | −0.01 | 0.01 | −0.03 | 0.01 |
| **ThermoMPNN** | 0.54 | 0.55 | −0.01 | 1.00 | **0.59** | **0.70** | 0.55 | 0.43 | 0.51 | 0.45 |
| **RSA** | 0.49 | 0.52 | 0.01 | **0.59** | 1.00 | **0.56** | 0.54 | 0.45 | 0.49 | 0.43 |
| **FoldX** | 0.54 | 0.56 | 0.02 | **0.70** | 0.56 | 1.00 | 0.50 | 0.41 | 0.45 | 0.39 |
| **AlphaMissense** | 0.45 | 0.46 | −0.01 | 0.55 | 0.54 | 0.50 | 1.00 | 0.72 | 0.80 | 0.73 |

The same numbers in all four proteins, to ±0.03:

| | JAK1 | JAK2 | JAK3 | TYK2 |
|---|--:|--:|--:|--:|
| Rosetta ↔ ThermoMPNN | 0.517 | 0.539 | 0.533 | 0.539 |
| Rosetta ↔ FoldX | 0.527 | 0.544 | 0.558 | 0.555 |
| FoldX ↔ ThermoMPNN | 0.690 | 0.697 | 0.702 | 0.689 |
| **RSA ↔ ThermoMPNN** | **0.589** | **0.595** | **0.582** | **0.608** |
| **RSA ↔ FoldX** | 0.558 | 0.563 | 0.554 | 0.546 |
| **RSA ↔ Rosetta** | 0.488 | 0.495 | 0.486 | 0.514 |

**Read the RSA row against the Rosetta row.** RSA — burial, a number from geometry alone —
correlates with ThermoMPNN at **0.59**, while PyRosetta, a full force-field calculation costing
~1.5 h per protein, correlates with the same ThermoMPNN at **0.54**. The free number does better.

### Separating the clusters, all four proteins (AUC)

| method | JAK1 | JAK2 | JAK3 | TYK2 |
|---|--:|--:|--:|--:|
| **RSA** | **0.782** | **0.765** | **0.767** | **0.816** |
| ThermoMPNN | 0.745 | 0.764 | 0.762 | 0.791 |
| Rosetta closed | 0.744 | 0.713 | 0.711 | 0.746 |
| FoldX | 0.719 | 0.742 | 0.749 | 0.752 |
| Rosetta delta | 0.497 | 0.499 | 0.527 | 0.502 |
| *AlphaMissense (for scale)* | *0.886* | *0.942* | *0.925* | *0.935* |

**RSA beats every ΔΔG method on every protein.** It is also the cheapest thing in the table.

### The paper behind this

**Tsishyn, Pucci & Rooman, *Bioinformatics* 2025 — RSALOR**,
[10.1093/bioinformatics/btaf322](https://doi.org/10.1093/bioinformatics/btaf322). A two-feature
model, **log-odds ratio from an MSA × relative solvent accessibility**, benchmarked on ProteinGym
(~700,000 mutations, 218 DMS sets) against 27 predictors including 19 protein language models.
On the **Stability** slice:

| model | Spearman |
|---|--:|
| ProSST-2048 | 0.638 |
| SaProt | 0.565 |
| **RSALOR** (RSA × LOR) | **0.551** |
| ESM2-650M | 0.496 |
| **−RSA alone** | **0.480** |
| conservation alone | 0.447 |

RSA alone beats ESM2-650M on stability, and the two-feature combination beats most deep models.
Our numbers reproduce the shape of that result on the JAKs independently. We have RSALOR output
for JAK2 (`../rsalor_jak2_family.csv`) but have not yet used it as a clustering feature — the
clearest cheap improvement available.

## 6. The four-residue outlier tail — is it Rosetta-specific?

**Yes, and the proline part is entirely Rosetta's.** Percentage of substitutions beyond an
extreme threshold, by substituted-in residue, JAK2:

| substituted-in | Rosetta (ΔΔG < −10) | FoldX (> +10) | ThermoMPNN (> +10) |
|---|--:|--:|--:|
| **P** | **92.5%** | 2.5% | 0.0% |
| **W** | **46.2%** | **14.1%** | 0.0% |
| I | 45.4% | 1.5% | 0.0% |
| **Y** | **44.6%** | **11.0%** | 0.0% |
| **F** | **43.9%** | **7.0%** | 0.0% |
| V | 38.6% | 0.9% | 0.0% |
| … | … | … | … |
| S | 3.0% | 0.1% | 0.0% |

Three separate conclusions:

- **ThermoMPNN has no tail at all** — 0.0% for all 20 residues. A bounded neural-net output
  cannot produce a −2,900 kcal/mol value, so the comparison is partly unfair, but it does mean
  the tail is not a property of the substitutions.
- **FoldX reproduces the aromatic ranking** — W, Y, F are its top three — so the **steric
  mechanism is real**: inserting a large aromatic into a packed core genuinely clashes.
- **FoldX does not reproduce proline** (2.5% against Rosetta's 92.5%). The proline tail is a
  **backbone-geometry failure specific to Rosetta's protocol**: `mutate_residue` with an 8 Å
  repack does not re-sample the backbone, and proline's ring constrains φ, so a proline forced
  into a non-proline backbone registers an enormous clash that relaxation would relieve.

**Practical consequence.** Our Rosetta ΔΔG should be **winsorised or rank-transformed before
use**, and the raw values at X→P positions should not be interpreted at all. In the clustering
this is partly handled already — Gower min-max scaling over the observed range plus the mean over
8–11 features dilutes it — but a per-method clipped version would be better. The
`../ddg_by_target_aa_*.csv` tables carry a `clip_mean` column computed for exactly this reason.

## 7. Against experimental data — TYK2 DMS

The only experimental anchor in the project: Howard *et al.* 2026, 22,516 missense variants with
interferon signalling and protein abundance. |Spearman ρ|:

| method | abundance (stability) | IFN 100 U (function) |
|---|--:|--:|
| **AlphaMissense** | **0.418** | **0.341** |
| CADD | 0.375 | 0.253 |
| ESM-1b | 0.362 | 0.291 |
| PolyPhen-2 | 0.339 | 0.256 |
| **ThermoMPNN** | 0.295 | 0.268 |
| **RSA** | 0.288 | 0.262 |
| **FoldX** | 0.275 | 0.275 |
| **Rosetta closed** | 0.261 | 0.230 |
| **Rosetta delta** | 0.010 | 0.006 |

**The conservation-based predictors beat the stability methods at predicting measured protein
abundance.** That is the surprising one: abundance is close to a direct readout of folding
stability, which is what ΔΔG is supposed to compute, and AlphaMissense — which never sees a
force field — is 60% better at it than PyRosetta.

**RSA alone (0.288) beats both FoldX and Rosetta.** Again.

A caveat in the methods' favour: these are *single-point* correlations over a whole multi-domain
protein, the hardest possible setting, and the literature's independent ceiling is r ≈ 0.5–0.6
on curated single-domain sets. 0.26–0.30 is poor but not anomalous.

## 8. Recommendations

1. **Do not use `ddg_delta`.** Inert on four proteins; on JAK2 it also fails to reproduce between
   two model pairs (r = 0.074).
2. **Winsorise Rosetta ΔΔG, and drop X→P values.**
3. **Add RSA as a feature.** It is free, already present in the ThermoMPNN file at 100% coverage,
   and outperforms all three ΔΔG methods at separating the clusters.
4. **Consider replacing Rosetta with ThermoMPNN** in the feature set: better AUC (0.76–0.79 vs
   0.71–0.75), better agreement with FoldX, no outlier tail, no 1.5 h per protein, 100% coverage.
   Keep Rosetta only for the dual-state question it was computed for.
5. **Try RSALOR properly** — we have the JAK2 output already.

## Files

| file | what |
|---|---|
| `analyse_ddg_methods.py` → `ddg_survey.json` | every number here |
| `plot_ddg_survey.py` → `figs/` | the six figures |
| `{jak1,jak2,jak3,tyk2}_methods.csv` | the joined per-variant table, all methods |
| `ddg_methods_survey.html` | the interactive version |

Related: [`../DDG_COMPUTATION_REPORT.md`](../DDG_COMPUTATION_REPORT.md) (our protocol in detail) ·
[`../../external_data/ddg_literature.md`](../../external_data/ddg_literature.md) (33 DOIs) ·
[`../../external_data/ddg_precomputed.md`](../../external_data/ddg_precomputed.md) (datasets) ·
[`../rosetta_dualstate_qc.md`](../rosetta_dualstate_qc.md) · [`../RUNBOOK.md`](../RUNBOOK.md)
