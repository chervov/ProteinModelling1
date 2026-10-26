# TYK2: predictors, ΔΔG and measured phenotype — all-vs-all

*26 October 2026. Twelve features on the same variants: seven sequence-based pathogenicity
predictors, three PyRosetta ΔΔG terms, and the two experimental DMS readouts.*

Source: `external_data/TYK2/tyk2_variants_inf_predict_ext.csv`.
**n = 2,247 variants with a parseable identifier; 2,188 complete across all twelve.**

> **Why this sample, and what it costs.** CADD and MetaRNN exist **only** in this curated file —
> nobody extracted them genome-wide. That is an artefact of how the data was assembled, not a real
> limit: both are available in dbNSFP for the ~31% of substitutions reachable by a single
> nucleotide change, the same coverage as REVEL, SIFT and PolyPhen-2. Pulling them for all of those
> would roughly triple the sample and remove the bias described next.
>
> **The curated set is not representative.** It is dominated by gnomAD observations — variants seen
> in healthy people — and is therefore **enriched for benign variants**: median AlphaMissense
> **0.170 here against 0.376 genome-wide**. The consequence is restriction of range, and it is
> directional:
>
> | pair | curated (n≈2,200) | genome-wide | difference |
> |---|--:|--:|--:|
> | AlphaMissense vs ESM1b | +0.751 | +0.786 | −0.035 |
> | AlphaMissense vs REVEL | +0.761 | +0.724 | +0.037 |
> | AlphaMissense vs ΔΔG_closed | +0.484 | +0.481 | +0.003 |
> | **AlphaMissense vs DMS abundance** | **+0.360** | **+0.418** | **−0.059** |
> | **AlphaMissense vs DMS signalling** | **+0.264** | **+0.341** | **−0.077** |
> | **DMS signalling vs abundance** | **+0.137** | **+0.204** | **−0.067** |
>
> **Predictor-to-predictor and predictor-to-ΔΔG correlations are unaffected** (±0.04), so sections
> 3.1, 3.2 and 3.4 stand as written. **Predictor-to-phenotype correlations in this table are
> understated by 0.06–0.08** — selecting benign variants compresses the damaging end where the
> signal lives. Genome-wide values should be preferred wherever both exist.

---

## 1. Descriptive statistics

| column | n | mean | std | min | 25% | 50% | 75% | max | orientation |
|---|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **AlphaMissense** | 2,246 | +0.328 | 0.306 | +0.024 | +0.096 | +0.170 | +0.514 | +0.999 | higher = damaging |
| **REVEL** | 2,191 | +0.369 | 0.274 | +0.001 | +0.129 | +0.300 | +0.595 | +0.983 | higher = damaging |
| **CADD phred** | 2,191 | +19.867 | 10.397 | +0.001 | +12.005 | +23.500 | +27.200 | +35.000 | higher = damaging |
| **SIFT** | 2,191 | +0.166 | 0.255 | +0.000 | +0.002 | +0.033 | +0.232 | +1.000 | **lower** = damaging |
| **PolyPhen-2 HVAR** | 2,191 | +0.565 | 0.413 | +0.000 | +0.079 | +0.705 | +0.986 | +1.000 | higher = damaging |
| **MetaRNN** | 2,191 | +0.471 | 0.340 | +0.000 | +0.137 | +0.389 | +0.826 | +0.994 | higher = damaging |
| **ESM1b** | 2,191 | −8.369 | 3.576 | −19.217 | −10.972 | −8.383 | −5.677 | +4.885 | **lower** = damaging |
| **ddG closed** | 2,244 | −38.996 | **159.854** | **−2988.610** | −10.240 | −3.195 | −0.867 | +137.060 | negative = destabilising |
| **ddG open** | 2,244 | −37.494 | **150.610** | −2771.880 | −9.488 | −3.130 | −0.680 | +104.030 | negative = destabilising |
| **ddG open−closed** | 2,244 | +1.502 | 68.772 | −1662.070 | −0.972 | +0.020 | +1.080 | +1083.010 | positive = favours open |
| **DMS signalling (IFN-α 100 U/mL)** | 2,244 | −0.178 | 0.561 | −3.355 | −0.343 | −0.089 | +0.139 | +1.644 | lower = loss of function |
| **DMS abundance (VAMP-seq)** | 2,243 | −0.105 | 0.117 | −0.405 | −0.173 | −0.063 | −0.016 | +0.087 | lower = less protein |

**Scales differ by three orders of magnitude.** The seven predictors are bounded (0–1, or CADD
0–35); ΔΔG runs to −2,989 with SD 160. Those extremes are steric-clash penalties, not energies
(`conclusions_ddG_difference_feature.md` §9 measures them as ~100% `fa_rep`), which is why every
correlation below is **Spearman**.

---

## 2. All-vs-all correlation (Spearman)

All features oriented so that **higher = more damaging**, so every entry should be positive if the
features agree.

| | AlphaMiss | REVEL | CADD | SIFT | PPh2 | MetaRNN | ESM1b | ddGclos | ddGopen | ddGdiff | DMSsig | DMSab |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **AlphaMiss** | — | +0.76 | +0.79 | +0.70 | +0.76 | **+0.85** | +0.75 | +0.48 | +0.49 | +0.02 | +0.26 | +0.36 |
| **REVEL** | +0.76 | — | +0.81 | +0.69 | +0.76 | **+0.85** | +0.67 | +0.41 | +0.42 | +0.03 | +0.26 | +0.40 |
| **CADD** | +0.79 | +0.81 | — | +0.76 | +0.81 | **+0.85** | +0.72 | +0.44 | +0.44 | +0.04 | +0.24 | +0.37 |
| **SIFT** | +0.70 | +0.69 | +0.76 | — | +0.74 | +0.78 | +0.63 | +0.41 | +0.41 | +0.03 | +0.23 | +0.32 |
| **PPh2** | +0.76 | +0.76 | +0.81 | +0.74 | — | +0.83 | +0.67 | +0.44 | +0.45 | +0.02 | +0.21 | +0.32 |
| **MetaRNN** | +0.85 | +0.85 | +0.85 | +0.78 | +0.83 | — | +0.75 | +0.48 | +0.48 | +0.02 | +0.27 | +0.40 |
| **ESM1b** | +0.75 | +0.67 | +0.72 | +0.63 | +0.67 | +0.75 | — | +0.43 | +0.45 | +0.04 | +0.25 | +0.32 |
| **ddGclos** | +0.48 | +0.41 | +0.44 | +0.41 | +0.44 | +0.48 | +0.43 | — | **+0.84** | −0.16 | +0.18 | +0.24 |
| **ddGopen** | +0.49 | +0.42 | +0.44 | +0.41 | +0.45 | +0.48 | +0.45 | +0.84 | — | +0.21 | +0.16 | +0.23 |
| **ddGdiff** | +0.02 | +0.03 | +0.04 | +0.03 | +0.02 | +0.02 | +0.04 | −0.16 | +0.21 | — | −0.01 | −0.03 |
| **DMSsig** | +0.26 | +0.26 | +0.24 | +0.23 | +0.21 | +0.27 | +0.25 | +0.18 | +0.16 | −0.01 | — | **+0.14** |
| **DMSab** | +0.36 | +0.40 | +0.37 | +0.32 | +0.32 | +0.40 | +0.32 | +0.24 | +0.23 | −0.03 | +0.14 | — |

---

## 3. Four blocks

### 3.1 The seven sequence predictors are effectively one feature

Every pairwise correlation is **+0.63 to +0.85**. PCA on the rank-transformed scores
(n = 2,188): eigenvalues **5.55, 0.40, 0.33, 0.22, 0.22, 0.17, 0.11** →
**PC1 = 79.3%**, PC1+PC2 = 85.1%.

The two features added in this round sit squarely inside the block. **MetaRNN correlates ≥ +0.78
with all six others** — the highest average of any feature — which is expected, since it is a
meta-predictor trained on them. It is the centroid of the panel, not an independent view. **CADD**
likewise ranges +0.72 to +0.85.

This reproduces the JAK1 finding (PC1 = 79.3% on six predictors, `mutation_analysis.md` §59) on a
different protein with two additional predictors, and lands on the identical number.

### 3.2 ΔΔG is the only partly independent computational feature

ΔΔG_closed correlates **+0.41 to +0.49** with the panel — substantial agreement, but far enough
from +0.85 that it is not an eighth copy. Adding it to the PCA drops PC1 from **79.3% to 73.0%**,
the largest dent any feature makes.

Matches the genome-wide value (+0.475 against AlphaMissense on all 22,536 variants), so this is not
an artefact of the curated sample.

### 3.3 The measured phenotypes agree with nothing — including each other

| | curated (this table) | genome-wide |
|---|--:|--:|
| DMS abundance, best predictor | +0.40 (REVEL, MetaRNN) | **+0.42** (AlphaMissense) |
| DMS signalling, best predictor | +0.27 (MetaRNN) | **+0.34** (AlphaMissense) |
| **DMS signalling ↔ DMS abundance** | **+0.14** | **+0.20** |

**The two experimental readouts correlate with each other less than any predictor correlates with
either of them** — +0.14 in this sample, **+0.20 genome-wide**, against +0.34 and +0.42 for
AlphaMissense. The qualitative claim survives the bias correction; the exact figure is the
genome-wide one. Losing protein does not reliably predict losing signal. The
predictors cluster tightly around a single axis that is not what the cells measure — and the cells'
own two measurements are not one axis either.

This is the quantitative form of the dissociation analysed in `interface_effect.md`: that document
examines one region where abundance and signalling come apart sharply, but mild decoupling is the
protein-wide background.

### 3.4 ΔΔG_open − ΔΔG_closed is null against all eleven other features

+0.02 to +0.04 against every sequence predictor; **−0.01** against signalling and **−0.03** against
abundance. Its only non-zero entries are with its own two inputs, **−0.16** and **+0.21** — the
difference is near-orthogonal to both terms it is built from, which is what subtracting two
quantities correlated at **+0.84** produces.

Adding CADD and MetaRNN does not change this. The feature was already shown null against measured
phenotype at n = 22,536 (`conclusions_ddG_difference_feature.md` §2); it is now also null against
the two most widely used predictors not previously tested against it.

---

## 4. Summary

| block | internal agreement | agreement with the DMS |
|---|--:|--:|
| 7 sequence predictors (PC1 = 79.3%) | +0.63 to +0.85 | +0.21 to +0.40 |
| ΔΔG_closed / ΔΔG_open | +0.84 with each other, +0.41–0.49 with predictors | +0.16 to +0.24 |
| **ΔΔG_open − ΔΔG_closed** | **−0.16 / +0.21 with its own inputs** | **−0.01 / −0.03** |
| DMS signalling ↔ DMS abundance | — | **+0.14** (curated) / **+0.20** (genome-wide) |

*Data: `external_data/TYK2/tyk2_variants_inf_predict_ext.csv`. Related:
`ddg_by_target_aa.md`, `conclusions_ddG_difference_feature.md`,
`TYK2/DMS_Howard2026/dms_basic_statistics.md`.*

---

## 5. What would improve this

**Extract CADD and MetaRNN genome-wide.** Both are in dbNSFP for the ~6,900 single-nucleotide-
reachable TYK2 substitutions — three times this sample, with no benign enrichment. That would let
the full twelve-feature matrix be computed on an unbiased set, and is the single change that would
most strengthen this analysis. The only features that would remain restricted are those already
limited to that 31% (REVEL, SIFT, PolyPhen-2).
