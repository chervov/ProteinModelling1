# The JAK1 clustering, rebuilt and compared variant by variant

Covers [`cluster_jak1.py`](cluster_jak1.py), [`compare_clustering.py`](compare_clustering.py),
[`jak1_clustering_rebuilt.csv`](jak1_clustering_rebuilt.csv) and
[`jak1_clustering_comparison.json`](jak1_clustering_comparison.json). Written 2 November 2026.

This closes the gap named at the end of the [README](README.md): the project had compared the
clustering with the paper's only through cluster sizes and marginal statistics. What was missing
was a **per-variant** agreement measure. Here it is, on all **21,926** substitutions, plus the
sensitivity checks that decide whether the agreement means anything.

---

## 1. The method, as the appendix actually specifies it

Appendix §2.1–2.2 pins down more than earlier notes assumed:

**Gower distance**, which is what lets the paper use features at 7.9% coverage without imputing:

```
d_ij  =  Σ_k w_k · δ_ijk · d_ijk  /  Σ_k w_k · δ_ijk
```

`δ_ijk = 1` only when **both** variants have feature *k*; `d_ijk` is the range-normalised absolute
difference. So a missing value removes that feature from both numerator and denominator rather than
being filled in — a variant with 3 features is compared on those 3. Weights are not stated, so all
are 1 here.

**Ten named seed variants**, quoted verbatim:

| Cluster 1 — "common in the general population (from gnomAD v4)" | Cluster 2 — "clinically reported to cause gain-of-function" |
|---|---|
| S383G, I62V, I878V, **T138H**, S512L | S703I, A634D, C787F, H596D, V985I |

and "the algorithm then used these seed clusters to classify the remaining **21,916**" — which is
21,926 − 10, confirming the seeds sit inside the same row set and that Cluster 1 is the
common/benign pole.

Gower has no natural centroid, so each cluster is represented by its per-feature mean over assigned
members (missing values skipped) and points go to the nearer representative — K-means with Gower as
the metric, the reading that matches "initial anchors". Seeds stay pinned to their own cluster;
that is the whole of the supervision. The three ΔΔG features are clipped to [−10, 10] as the paper
does. Converged in **10 iterations**.

## 2. First finding: one of the ten seeds is not a JAK1 variant

**`T138H` does not exist.** Position 138 of UniProt P23458 is **tyrosine**, not threonine, so there
is no such row in Dataset EV1 and the clustering necessarily ran on **4 + 5** anchors. The check is
in `cluster_jak1.py`; the other nine all match the canonical sequence.

The likeliest reading is a one-letter slip for **`Y138H`**, which does exist, is reachable by a
single nucleotide (TAT→CAT), carries AlphaMissense **0.136** and ESM-1b **−2.154**, and is labelled
**Cluster 1** in EV1 — all consistent with "common in gnomAD v4". Adding it as a fifth Cluster-1
seed changes **nothing**: ARI 0.4836, 8,401 / 13,525, identical to four decimal places. Which leads
straight to the next point.

## 3. Second finding: the seeds do not matter

| seeding | ARI | same label | sizes |
|---|--:|--:|---|
| the paper's named seeds (4 + 5 usable) | **0.4836** | 84.87% | 8,401 / 13,525 |
| + `Y138H` as the missing fifth | 0.4836 | 84.87% | 8,401 / 13,525 |
| **25 random draws of 5 + 5 from the EV1 clusters** | **median 0.4836, range 0.4833–0.4839** | | |

Twenty-five random seed sets, drawn blind from the two EV1 clusters, reproduce the named-seed result
to within ±0.0003 ARI. **The "semi-supervised" step contributes essentially nothing.** Ten anchors
among 21,926 points are swamped the moment the first full assignment pass runs; after that the
representatives are the means of ~8,400 and ~13,500 variants, and where the ten seeds started is
irrelevant.

The seeds do one real job: they **orient** the solution, fixing which pole gets labelled "Cluster 1".
That is not nothing — it is what makes the output interpretable as benign-vs-GOF rather than an
arbitrary 1/2 — but it is not classification from labelled examples. The structure comes from the
unsupervised geometry of the feature matrix. Any description of this as learning from the ten
clinical labels overstates what they do.

## 4. Per-variant agreement with Dataset EV1

| | rebuilt → 1 | rebuilt → 2 | total |
|---|--:|--:|--:|
| **paper Cluster 1** | **6,321** | 1,238 | 7,559 |
| **paper Cluster 2** | 2,080 | **12,287** | 14,367 |
| total | 8,401 | 13,525 | **21,926** |

| | |
|---|--:|
| same label | **18,608 (84.87%)** |
| **Adjusted Rand Index** | **0.4836** |
| Cohen's κ | 0.6737 |
| label-permutation null | mean 53.6%, 97.5th pct 54.2% |

Against a null of 53.6%, 84.87% is far outside the permutation distribution — the agreement is
real, not a product of matching marginals. But **ARI 0.48 is moderate, not a reproduction.** One
variant in seven is classified differently, and the disagreement is asymmetric: **2,080 of the
paper's Cluster 2 move to Cluster 1** (14.5% of it) against 1,238 the other way, which is why the
rebuilt benign cluster is larger (8,401 vs 7,559).

This is the honest answer to "does the clustering reproduce?" — **the broad split does, the
per-variant assignment only partly.** Expected, given that four of the eleven features had to be
obtained by a different route than the paper used (PolyPhen-2 at 100% rather than 56.3%, CADD and
SIFT at 31.3%, FoldX standing in for MutFunc) and that the paper does not name its PolyPhen-2 model
or its feature weights.

### Where the disagreement sits

Variants the two methods disagree on are **systematically milder** on every feature with signal:

| feature | median, agree | median, disagree | p |
|---|--:|--:|--:|
| ESM-1b | −8.97 | **−6.82** | 1e−131 |
| AlphaMissense | 0.769 | **0.427** | 4e−115 |
| FoldX ΔΔG | 1.300 | **0.590** | 1e−118 |
| ddG closed | −4.31 | −2.43 | 2e−88 |
| PolyPhen-2 HumVar | 0.955 | **0.688** | 8e−55 |
| ClinPred | 0.912 | 0.816 | 3e−12 |
| CADD | 25.0 | 23.9 | 1e−06 |
| BLOSUM62 | −2.0 | −1.0 | 0.005 |
| **ddG delta** | −0.009 | −0.033 | **0.25** |

So the two clusterings agree on the clear cases at both poles and part company in the middle — the
intermediate band where no feature is decisive. That is a property of a two-means split of a
continuum, not a defect in either run, and it is where a clinical reading of either clustering
should be most cautious.

And `ddg_delta` is the one feature showing **no** difference (p = 0.25), consistent with its AUC of
0.5035 (`build_rosetta_ddg_jak1_info.md` §4).

### And, independently, where features are missing

*Added 3 November 2026.* The band effect above is only half of it. Disagreement also rises
monotonically as **coverage** falls, and the two effects are independent.

| features present | n | disagreement |
|--:|--:|--:|
| 7 | 765 | **25.5%** |
| 8 | 14,288 | 17.6% |
| 10 | 356 | 11.2% |
| 11 | 6,517 | **8.7%** |

The three 31.3%-coverage features (CADD, SIFT, ClinPred) are present in 33.7% of agreements but
only **18.2%** of disagreements. Crossing the two effects shows neither is a proxy for the other —
within *every* AlphaMissense band, coverage still costs 6.8 to 16.1 percentage points:

| AlphaMissense band | n | overall | ≤8 features | ≥10 features | gap |
|---|--:|--:|--:|--:|--:|
| confident tolerant (<0.25) | 5,416 | 14.5% | 19.8% | 9.3% | 10.5 |
| intermediate-low (0.25–0.55) | 4,068 | **31.8%** | **36.5%** | 20.4% | 16.1 |
| intermediate-high (0.55–0.80) | 2,850 | 21.8% | 25.7% | 10.8% | 14.9 |
| confident damaging (≥0.80) | 9,592 | **6.4%** | 8.0% | **1.2%** | 6.8 |

Band effect 3.0×, coverage effect 2.1×, and they multiply: the spread from best cell to worst is
1.2% → 36.5%, a factor of 30.

### What this does to the headline ARI

| subset | n | agreement | **ARI** |
|---|--:|--:|--:|
| ALL — the figure reported in §4 | 21,926 | 84.9% | **0.484** |
| high coverage (≥10 of 11 features) | 6,873 | 91.2% | 0.679 |
| confident AlphaMissense | 15,008 | 90.6% | 0.657 |
| **both: high coverage AND confident AM** | 4,931 | **94.3%** | **0.786** |
| **neither: ≤8 features AND intermediate AM** | 4,976 | **68.0%** | **0.130** |

**The reproduction is substantially better than ARI 0.484 suggests.** Where both clusterings have
the data to decide they agree 94.3% at ARI 0.786. The headline is dragged down by 4,976 variants
carrying sparse features *and* an intermediate score, which disagree 68% of the time at ARI 0.130 —
barely above the 53.6% permutation null. Those are substitutions needing two or three nucleotide
changes, so CADD, SIFT and ClinPred are all absent by construction (README § *The paper's
SIFT/PolyPhen coverage did not come from dbNSFP*), leaving Gower distance over 7–8 dimensions on a
variant that is ambiguous anyway. **Neither label is trustworthy there**, so counting that
disagreement against the rebuild overstates the gap.

This also changes what §6 and §8 attribute the gap to. Dropping all three ΔΔG features moves ARI
0.484 → 0.492; the HumDiv/HumVar choice is worth about ΔARI 0.090. Stratifying by data quality
moves it 0.484 → 0.786 — an order of magnitude more explanatory power than either. **The dominant
cause is missingness interacting with the Gower distance**, not a methodological difference between
the two pipelines.

One consequence for downstream use: the published EV1 assignment carries very different confidence
per variant and nothing in EV1 marks which. A per-variant confidence field — feature count plus
distance to the decision boundary — would be more useful than further tuning of the clustering.

## 5. Which features actually carry the clustering

Leave one feature out, recluster, re-measure against EV1:

| removed | ARI | Δ |
|---|--:|--:|
| **polyphen2** | 0.3934 | **−0.0901** |
| clinpred | 0.4600 | −0.0236 |
| alphamissense | 0.4718 | −0.0118 |
| sift | 0.4722 | −0.0113 |
| esm1b | 0.4782 | −0.0053 |
| cadd | 0.4803 | −0.0033 |
| blosum62 | 0.4821 | −0.0014 |
| **ddg_delta** | 0.4836 | **0.0000** |
| ddg_closed | 0.4886 | **+0.0051** |
| foldx | 0.4886 | **+0.0050** |
| ddg_open | 0.4911 | **+0.0075** |

Three results worth stating plainly:

1. **PolyPhen-2 dominates** — removing it costs nearly twice as much as the next five combined.
   Which makes the paper's silence about HumDiv vs HumVar the single most consequential ambiguity in
   reproducing it, since the two models disagree on 25.7% of variants (README). This run uses
   HumVar.
2. **`ddg_delta` is exactly neutral — 0.0000 to four decimals.** It is not merely weak; it is inert.
   Removing the paper's distinctive feature changes not one of the 21,926 assignments.
3. **Removing a ΔΔG or FoldX feature *improves* agreement with the paper.** Every structural feature
   has a non-positive or negative contribution. Given the clash contamination documented in
   `build_rosetta_ddg_jak1_info.md` §3 — 27.8% of values beyond |10|, minimum −2,935 kcal/mol — the
   clipping to [−10, 10] saturates a quarter of them at the boundary, so they add a near-binary
   "clashes / does not clash" signal rather than an energy. That is the most likely reason they
   dilute rather than sharpen.

## 6. Sensitivity to what the paper leaves open

| feature set | k | ARI | same | sizes |
|---|--:|--:|--:|---|
| baseline (HumVar, FoldX in, ΔΔG clipped) | 11 | 0.4836 | 84.87% | 8,401 / 13,525 |
| without `ddg_delta` | 10 | 0.4836 | 84.87% | 8,401 / 13,525 |
| **without all three ΔΔG** | 8 | **0.4917** | **85.20%** | 7,868 / 14,058 |
| only the 100%-coverage features | 7 | 0.4335 | 82.97% | 9,214 / 12,712 |
| only the 31.3% genomic features | 3 | 0.3989 | 81.75% | 1,791 / 5,082 (15,053 unassignable) |
| ESM-1b + AlphaMissense alone | 2 | 0.3487 | 79.54% | 10,127 / 11,799 |
| ESM-1b alone | 1 | 0.2105 | 73.04% | 12,640 / 9,286 |

**Dropping all three ΔΔG features gives the closest agreement with the paper of anything tried** —
ARI 0.4917, and cluster sizes 7,868 / 14,058 against the paper's 7,559 / 14,367, much nearer than
the baseline's. A feature set without the paper's own structural features reproduces the paper's
clusters better than one with them. Read together with §5 that is consistent, and it points at the
clash contamination rather than at the dual-state idea itself: the *concept* of an open-versus-closed
preference is sound, but these particular numbers are too damaged to carry it.

The monotone decline from 11 to 1 feature confirms the ensemble is doing real work — no single
predictor, not even ESM-1b, substitutes for it.

## 7. What this supports, and what it does not

**Supported.** The paper's two-cluster structure is reproducible in broad outline: a 34%/66% split
on independently assembled features, 84.87% per-variant agreement, far beyond chance. The
pipeline — Gower distance over a mixed, partly missing feature set, oriented by clinical anchors —
works and is a sensible design for this problem.

**Not supported.**

- **ARI 0.4836 is moderate.** Per-variant assignments should not be treated as reproduced, and
  neither clustering should be used to make a call about an individual variant in the intermediate
  band, which is exactly where the two disagree.
- **The semi-supervised framing is not doing the work** (§3). Random seeds give the same answer to
  ±0.0003.
- **The dual-state ΔΔG features contribute nothing or less than nothing** (§§5–6), and `ddg_delta`
  contributes *exactly* nothing.
- **One of the ten published seeds does not exist** (§2).

Numbers are reproducible from the two scripts in this directory; raw per-variant output is in
`jak1_clustering_rebuilt.csv` (both labels on every row) and the summary in
`jak1_clustering_comparison.json`.

## 8. Caveats on this rebuild

- **Four of eleven features are not the paper's values.** PolyPhen-2 is a fresh native run at 100%
  rather than the paper's 56.3%; SIFT, CADD and ClinPred come from dbNSFP at 31.3% where the paper
  reports 56.3% and 14.25%; FoldX stands in for "MutFunc score", which today's mutfunc cannot
  reproduce (`build_mutfunc_jak1_info.md` §2). Divergence from the paper is therefore expected and
  the 15% disagreement cannot be attributed to method alone.
- **Equal feature weights** — the paper's `w_k` are not published.
- **HumVar, not HumDiv**, and §5 shows that choice matters more than any other.
- **Gower with a mean representative is one reading** of "K-means ... anchors"; K-medoids on the full
  21,926 × 21,926 distance matrix is the alternative and was not run.
- **The EV1 labels are not ground truth.** They are the paper's clustering output, not validated
  clinical calls, so ARI measures agreement between two unsupervised partitions — not accuracy. A
  low ARI does not establish which is better, and neither does a high one.
