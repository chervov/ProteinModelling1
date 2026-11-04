# TYK2 variant clustering

All **11** features over all **22,553** TYK2 missense substitutions (UniProt P29597, 1,187 aa),
by the same method applied to JAK2. 4 November 2026.

- **[`tyk2_clustering_report.html`](tyk2_clustering_report.html)** — the full report with figures
- **[`protein_models/tyk2_models_3d.html`](protein_models/tyk2_models_3d.html)** — interactive 3D structures
- Labels: [`tyk2_clustering_v1.csv`](tyk2_clustering_v1.csv) · every number: `stats_tyk2.json`

| | |
|---|---|
| C1 tolerant / C2 damaging | **9,144 / 13,409** |
| converged | 8 iterations |
| gnomAD Mantel–Haenszel OR | **1.52** |
| **DMS AUC** (abundance / IFN 100 U) | **0.683 / 0.636** |

---

## 1. What is different about TYK2

**TYK2 has a deep mutational scan.** Howard *et al.* 2026 measured interferon signalling and
protein abundance for essentially every TYK2 missense variant. **22,536** of them overlap this
clustering and no feature saw any of them. JAK2's entire external validation rested on **21**
usable ClinVar labels; this is three orders of magnitude more evidence, and it changes what can
honestly be claimed.

**TYK2 has an experimental closed structure.** 4OLI, the autoinhibited JH2–JH1 crystal. The AF3
closed model reproduces it to **2.02 Å** JH1 RMSD after superposing JH2. JAK2's only closed
reference was a homology model, matched at 6.0–6.9 Å.

**TYK2's ClinVar is far thinner.** Two Pathogenic missense records, both 0-star, against JAK2's
five 2-star ones. That shapes the seeding (§3).

**The AlphaFold DB model is closed, not open.** For JAK2 the AFDB model is open (FERM–JH1 93.8 Å);
for TYK2 it is **closed** (39.7 Å, 1.66 Å from the crystal). The default AlphaFold answer is not
the same conformational state across the JAK family — worth knowing before reusing either as a
reference.

## 2. The DMS validation — the headline result

| DMS arm | n | C1 tolerant | C2 damaging | **AUC** |
|---|--:|--:|--:|--:|
| protein abundance | 22,516 | −0.068 | −0.149 | **0.683** |
| IFN 10 U | 22,536 | −0.051 | −0.359 | **0.647** |
| IFN 100 U | 22,536 | −0.035 | −0.379 | **0.636** |
| IFN 1 U | 22,536 | −0.003 | −0.080 | 0.572 |

Every arm separates in the right direction at overwhelming significance — but with n = 22,536 the
p-values say almost nothing. **The AUC of 0.64–0.68 is the number that matters.**

The clustering carries genuine signal about measured function and is **not a sharp predictor of
it**. AUC 0.68 means that given one damaging-cluster and one tolerant-cluster variant at random,
the damaging one is the more impaired about two times in three. Useful for describing a population
of variants; weak for calling any individual one.

**Abundance (0.683) beats interferon signalling (0.636).** The features are predominantly
stability and conservation predictors, so they track whether the protein folds better than whether
it signals. That is the honest description of what this clustering measures — and it is a caution
for the JAK2 work, where no comparable measurement exists to check it against.

## 3. Seeds

- **C1 tolerant** — the 5 highest-AF ClinVar benign/likely-benign variants, all 2-star:
  `V362F`, `I684S`, `G363S`, `A53T`, `R197H`. **`P1104A` is excluded** although it ranks 4th by
  allele frequency: it is ClinVar-benign because it is common, but it is the established TYK2
  loss-of-function allele behind the TB-susceptibility literature, so pinning it to the tolerant
  pole would pin a known functional variant to the wrong cluster.
- **C2 damaging — only two.** `L757V`, `L1014P`, the only Pathogenic missense records, both
  0-star. Rather than invent three more, the damaging pole is pinned with two seeds and the DMS is
  kept **entirely for validation**.

Seed sensitivity: 15 random draws reproduce **0.9999** of the labels, so the thin seeding costs
nothing. As on JAK1 and JAK2, the supervision orients the result rather than determining it.

## 4. Per-feature summary

ΔΔG sign: `ΔΔG = ΔG_WT − ΔG_mut`, **negative = destabilising** (opposite to FoldX).

| feature | coverage | C1 mean | C2 mean | AUC |
|---|--:|--:|--:|--:|
| ClinPred | 31.0% | 0.276 | 0.935 | 0.980 |
| PolyPhen-2 HumVar | 100.0% | 0.210 | 0.925 | 0.979 |
| CADD | 30.9% | 10.872 | 27.004 | 0.973 |
| AlphaMissense | 100.0% | 0.185 | 0.671 | 0.935 |
| SIFT | 31.0% | 0.289 | 0.029 | 0.908 |
| ESM-1b | 100.0% | −6.891 | −12.970 | 0.895 |
| FoldX ΔΔG | 89.5% | 0.687 | 3.090 | 0.752 |
| **ΔΔG closed** | 99.9% | −15.860 | −74.461 | 0.747 |
| **ΔΔG open** | 99.9% | −14.527 | −72.541 | 0.742 |
| BLOSUM62 | 100.0% | −0.981 | −1.724 | 0.643 |
| **ΔΔG delta** | 99.9% | 1.333 | 1.919 | **0.502** |

These AUCs are circular — these are the features the clustering was built from. The DMS AUCs in §2
are not.

**`ddg_delta` scores 0.502**, chance, exactly as on JAK2 (0.499) and JAK1 (0.4966). Three
proteins, three independent model sets, the same answer.

## 5. The ΔΔG — reused, not recomputed

Taken from the overnight PyRosetta run of **22 October 2026** across four molab CPU boxes
(`data/ddg/RUNBOOK.md`), joined onto the canonical order by
[`build_ddg.py`](build_ddg.py), which also re-verifies every wild-type residue against P29597
(0 mismatches). 22,536 of 22,553 substitutions, 99.9%.

| state | model | AF3 job | seed | template | FERM–JH1 | JH1 vs 4OLI |
|---|---|---|--:|:-:|--:|--:|
| closed | `tyk2_af3_closed.pdb` | fold_18_48 | 1087670550 | **ON** | 39.3 Å | **2.02 Å** |
| open | `tyk2_af3_open.pdb` | fold_19_34 | 1754329433 | **OFF** | 82.9 Å | 75.79 Å |

Both states were re-measured rather than trusted from their filenames, after 41 of 71 JAK2
structure files turned out to be mislabelled. These two are correctly named.

**The pair is confounded.** The two models come from different AF3 jobs, with different seeds
*and* opposite template settings — they differ in provenance as well as conformation. The
structural analysis makes it concrete: **the FERM domain alone differs by 5.47 Å between them**,
against 0.10–0.66 Å for every domain across JAK2's five models. JAK2's two states were related by
a rigid-body motion of JH1 and nothing else; TYK2's are not.

On JAK2 the reproducibility test across two independent model pairs showed `ddg_delta` does not
survive a change of structures (r = 0.074). TYK2 has one pair, so that test cannot be run here —
and the difference additionally absorbs a template and a seed change. **Treat ΔΔG delta as
uninterpretable for TYK2.**

## 6. Other validation

- **gnomAD**: C1 8.90% observed vs C2 5.05%, pooled OR 1.84 → **Mantel–Haenszel OR 1.52** after
  stratifying by dbNSFP reachability. Essentially identical to JAK2's 1.54.
- **ClinVar**: 20 of 23 usable labels correct — but with only two Pathogenic records, both 0-star,
  this is a far weaker check than §2 and should not be quoted on its own.

## 7. What this is, and what it is not

- **Not a reproduction** — there is no published TYK2 clustering.
- **AUC 0.64–0.68 against measured function.** This is the most honest calibration any clustering
  in this project has, and it is moderate. Nothing here supports using a cluster label to call an
  individual variant.
- **ΔΔG delta is uninterpretable** for TYK2 (§5), and inert on every protein tested.
- **PolyPhen-2 HumVar, not HumDiv**; equal feature weights; FoldX at 89.5%; the gnomAD test is not
  CpG-mutability controlled. As for JAK2.

## Files

| file | what |
|---|---|
| `build_universe.py` … `build_clinvar.py` | one script per feature, each with the JAK2 provenance |
| `build_ddg.py` | joins the reused October ΔΔG, documents the structures |
| `cluster_tyk2.py` | the 11-feature clustering |
| `analyse_tyk2.py` → `stats_tyk2.json` | every number, including the DMS arms |
| `plots_tyk2.py` → `figs_tyk2/` | the figures |
| `build_html_tyk2.py` → `tyk2_clustering_report.html` | the report |
| `protein_models/` | structures, geometry, PAE, the 3D viewer |

```bash
python3 cluster_tyk2.py && python3 analyse_tyk2.py && \
python3 plots_tyk2.py && python3 build_html_tyk2.py
```
