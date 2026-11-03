# JAK1 clustering — rebuilt step by step

Rebuilding the Jeanpierre/Debeaupuis JAK1 variant clustering from the ground up, one feature
at a time, with every step checked before the next is added. Started 2 November 2026.

Each feature file holds **all 23,080 Dataset EV1 rows in EV1 order**, so any two can be joined
by row position as well as by `variant_id`.

## → The analysis report (plots)

**[`jak1_clustering_analysis.html`](jak1_clustering_analysis.html)** — exploratory analysis with
figures: feature histograms by cluster, the correlation matrix, per-feature AUC against both
clusterings, **gnomAD r4 enrichment**, the disagreement analysis and the stratified ARI. Open it in a
browser (GitHub will not render it; use `htmlpreview.github.io` or download). Figures also in
[`figs/`](figs); built by `fetch_gnomad.py` → `analyse.py` → `plots.py` / `plots2.py` →
`build_html.py`, with numbers in `stats.json`.

> **Two headlines from it.** (1) Both clusterings deplete the damaging cluster of gnomAD-observed
> variants — **stratified OR 2.34** (paper) and **2.42** (rebuilt), p ≈ 1e-33 within the informative
> stratum. They are *indistinguishable* on this external criterion despite disagreeing on one variant
> in seven, so ARI 0.484 does not mean one is right and the other wrong. The pooled odds ratios
> (2.89 / 2.84) are inflated by a dbNSFP confound and should not be quoted — see the report.
> (2) **Scored on matched subsets, AlphaMissense is the best single feature** (AUC 0.9470), not
> ClinPred (0.9463); ClinPred's and CADD's apparent lead is an artefact of being scored only on the
> easier 31.3% that dbNSFP reaches. On the harder complement, **ESM-1b is best** (0.8884).

## → The final results file

**[`jak1_clustering_rebuilt.csv`](jak1_clustering_rebuilt.csv)** — one row per substitution
(21,926), every feature, and **both cluster labels side by side**. This is the file to open first.

| column | contents |
|---|---|
| 1–4 | `variant_id`, `wt`, `pos`, `alt` |
| **5** | **`cluster`** — the **paper's** label, from Dataset EV1 |
| 6–16 | the 11 features: `esm1b`, `alphamissense`, `ddg_closed`, `ddg_open`, `ddg_delta`, `cadd`, `foldx`, `sift`, `polyphen2`, `blosum62`, `clinpred` |
| **17** | **`my_cluster`** — the **rebuilt** label |

`cluster` **1 = tolerant** (AlphaMissense median 0.166), **2 = damaging** (median 0.953).
Agreement 84.87%, ARI 0.4836. Supporting files:
[`jak1_clustering_config.json`](jak1_clustering_config.json) (seeds, features, clipping, ranges),
[`jak1_clustering_comparison.json`](jak1_clustering_comparison.json) (confusion matrix,
leave-one-out, sensitivity), and the write-up
[`clustering_jak1_results.md`](clustering_jak1_results.md).

> **Read the headline ARI with care.** The 0.4836 averages over two regimes that behave very
> differently. Restricted to variants where both clusterings actually have the data to decide —
> ≥10 of 11 features present *and* an unambiguous AlphaMissense score — agreement is **94.3%,
> ARI 0.786** (n=4,931). On the opposite subset — ≤8 features *and* an intermediate score — it is
> **68.0%, ARI 0.130** (n=4,976), barely above chance. Disagreement is concentrated in the
> intermediate band (3.0×) *and*, independently, where features are missing (2.1×). See
> [§ Where the two clusterings disagree](#where-the-two-clusterings-disagree).

## Files so far

| file | contents |
|---|---|
| [`JAK1_P23458.fasta`](JAK1_P23458.fasta) | UniProt P23458 canonical sequence, 1,154 aa |
| [`jak1_sequence_info.json`](jak1_sequence_info.json) | which sequence this is: accession, entry name, length, UniProt version, md5/sha256 |
| [`44321_2025_317_MOESM3_ESM.xlsx`](44321_2025_317_MOESM3_ESM.xlsx) | Dataset EV1 from the paper supplementary, unmodified |
| [`jak1_ev1_clusters.csv`](jak1_ev1_clusters.csv) | the same two columns (`variant_id`, `cluster`), same order, as CSV |
| [`jak1_esm1b.csv`](jak1_esm1b.csv) | ESM-1b, 21,926 of 23,080 rows |
| [`jak1_alphamissense.csv`](jak1_alphamissense.csv) | AlphaMissense, 21,926 of 23,080 rows |
| [`jak1_blosum62.csv`](jak1_blosum62.csv) | BLOSUM62, all 23,080 rows |
| [`jak1_polyphen2_humvar.csv`](jak1_polyphen2_humvar.csv) | PolyPhen-2 **HumVar**, 21,926 of 21,926 — **100%** |
| [`jak1_polyphen2_humdiv.csv`](jak1_polyphen2_humdiv.csv) | PolyPhen-2 **HumDiv**, 21,926 of 21,926 — **100%** |
| `jak1_pph2_hum{var,div}_raw.txt.gz`, [`pph2_input_jak1.txt`](pph2_input_jak1.txt), [`pph2_sessions.txt`](pph2_sessions.txt) | raw server output, the batch input, and the session ids |
| [`build_features.py`](build_features.py), [`build_blosum.py`](build_blosum.py), [`seq_info.py`](seq_info.py) | reproduce the above, including the checks |

## File conventions — the same for every feature file here

**Index column: `variant_id`**, first column, the EV1 identifier (`A1005E` = wild type, position,
mutant). `wt`, `pos` and `alt` are the same thing parsed out, and `cluster` carries the paper's EV1
label. Then one or more feature columns.

**Row set: all 23,080 EV1 rows, in EV1 order** — not the 21,926 real substitutions. EV1 includes
1,154 self-substitutions (`A1005A`), and keeping them means every file here has identical row count
and order, so any two can be joined **either** on `variant_id` **or** by row position. First row
`A1005A`, last `Y999Y`.

**Missing values are empty fields** — `A1005A,A,1005,A,1,,` — never `NA`, `NaN`, `null`, `.`, `-1`
or `0`. This matters because **0 is a real value for several of these features**: a SIFT score of
`0.0` means maximally intolerant, and BLOSUM62 is routinely 0. Any numeric sentinel would collide
with genuine data; an empty field cannot. `pandas.read_csv` gives `NaN` and R's `read.csv` gives
`NA` with no extra arguments.

**Blankness is informative, not random.** It marks either a self-substitution or a substitution
needing two or three nucleotide changes, which genomic-indexed sources cannot reach. Those
unreachable substitutions are systematically **more severe** (BLOSUM62 mean −1.76 against −0.54 for
the reachable ones), so imputing them would bias the result.

| feature file | populated | blank |
|---|--:|--:|
| `jak1_blosum62.csv` | 23,080 (**all**) | 0 |
| `jak1_esm1b.csv`, `jak1_alphamissense.csv` | 21,926 | 1,154 |
| `jak1_polyphen2_humvar.csv`, `..._humdiv.csv` | 21,926 | 1,154 |
| `jak1_sift.csv`, `jak1_clinpred.csv`, `jak1_revel.csv` | 6,873 | 16,207 |


## The sequence

**UniProt P23458 / JAK1_HUMAN, 1,154 aa**, Swiss-Prot entry version 248 (modified 2026-11-02),
sequence md5 `933420e3eac5be8b1760cde731133e4a`. In the FASTA the first line is the **header**,
not sequence — `>sp|P23458|JAK1_HUMAN Tyrosine-protein kinase JAK1 OS=Homo sapiens`, where `sp`
means Swiss-Prot (reviewed). Parsers skip it and concatenate the rest.
`jak1_sequence_info.json` carries the same facts in a form a script can check, so the variant
numbering is pinned to one specific sequence version.

## Dataset EV1

23,080 rows = **21,926 real substitutions (19 × 1,154) + 1,154 self-substitutions** (`A1005A`
and friends, where wild type equals "mutant"). Cluster split over all rows is 8,713 / 14,367;
excluding the self-substitutions it is **7,559 / 14,367**, which is the figure the paper reports.

## Checks passed

**1. Every variant matches the sequence.** All **23,080 of 23,080** wild-type residues in
`variant_id` match UniProt P23458 at the stated position. Zero mismatches, and all 1,154
positions are covered. So EV1 is keyed on the canonical isoform with no numbering offset.

**2. `data/orianne/jak1_features.json` is in EV1 order.** Its 21,926 rows reproduce the EV1
`variant_id` sequence exactly once the self-substitutions are removed, and all 21,926 of its
`cluster` labels agree with EV1. Features taken from that file therefore need no reordering.

**3. BLOSUM62 is independently reproduced.** Computed here from the matrix (Biopython
`substitution_matrices`), not copied: **0 disagreements** against the 21,926 values in
`jak1_features.json`.

## Notes on the features

**BLOSUM62 depends only on the substitution, not the position.** It is a 20×20 lookup, so every
V→F in JAK1 carries the same value (−1) wherever it sits. It is the only position-blind feature
in the paper's set, and the weakest predictor of their clusters (AUC 0.632), while also being the
least correlated with the others (0.28–0.39, against 0.64–0.83 among the rest).

Self-substitutions take the matrix **diagonal** (4 to 11), which is a real BLOSUM62 value, so
`jak1_blosum62.csv` has no blanks. The other feature files leave those 1,154 rows empty, because
a self-substitution has no pathogenicity score.

**The paper reports BLOSUM62 as 43.74% missing** — identical to its SIFT and PolyPhen-2
missingness. A BLOSUM62 lookup can never be missing, so that figure shows the value was taken
from the same annotation source as SIFT and PolyPhen (dbNSFP or VEP) and inherited its coverage
gaps. Computing it locally gives 100%, as here.

## Still to add

| feature | status |
|---|---|
| PolyPhen-2 | **done, 100%** — see below |
| SIFT | no live service: `sift.bii.a-star.edu.sg` returns 502, PROVEAN redirects to `sitedown.jcvi.org`. Only route is local `sift4g` (Linux + a protein database) |
| ClinPred | 31.3%, dbNSFP only |
| REVEL | 31.3%, dbNSFP only |
| CADD | not obtained; the earlier attempt is recorded in `mutations_clustering.md` |
| MutFunc | not obtained (92.07% missing in the paper itself) |
| ddG closed / open / open−closed | **done, 100%** — `jak1_ddg_rosetta_dualstate.csv`, from `data/ddg/ddg_JAK1_all.json` (complete 21,926 saturation on Jeanpierre's own models). The 500-variant `data/orianne/jak1_cluster_ddg.json` is a test subset, not the dataset |

## PolyPhen-2 at 100% coverage — how, and what it shows

dbNSFP caps PolyPhen-2 at 31.3% because it is indexed on *genomic* variants, so substitutions
needing two or three nucleotide changes have no row. PolyPhen-2 itself is protein-level: its batch
query takes `P23458 617 V F` directly. Both models were run on all 21,926 EV1 substitutions and
both returned **21,926 of 21,926 — 100%**, in about four minutes each.

Demonstrated rather than assumed: `A1005D` needs two nucleotide changes, and PolyPhen-2 scored it
(the log's `find_gene: Not a single-nucleotide AA substitution` message is about genomic annotation
and is non-fatal).

| | HumDiv | HumVar |
|---|--:|--:|
| probably damaging | 14,343 (65.4%) | 11,212 (51.1%) |
| possibly damaging | 3,304 (15.1%) | 3,754 (17.1%) |
| benign | 4,279 (19.5%) | 6,960 (31.7%) |
| mean probability | 0.790 | 0.663 |
| AUC vs EV1 clusters | 0.8798 | **0.8848** |

**The two models disagree on 5,633 variants (25.7%)**, Pearson 0.871 / Spearman 0.940. The paper
says only "PolyPhen2 pathogenicity score" without naming a model, so this is a real ambiguity in
reproducing its feature matrix — hence both are provided. HumVar is the more conservative model and
the one PolyPhen-2 recommends for Mendelian-disease diagnostics; it also scores marginally better
against the EV1 clusters.

### Validation against the dbNSFP values

On the 423 variants where the repo already had a score: **Pearson 0.958, Spearman 0.973** (HumVar).
Not identical, and the reason is specific — PolyPhen-2 mixes sequence and structural features, and
this run's PDB/DSSP snapshot (25-May-2021, 178,229 structures) is newer than dbNSFP's:

| | n | median abs. difference | differing > 0.1 |
|---|--:|--:|--:|
| scored from alignment only | 109 | **0.0000** | **0.0%** |
| a structure contributed | 314 | 0.0065 | 17.8% |

Where the inputs are identical the reproduction is exact; divergence is confined entirely to
structure-scored variants. That argues the new column is preferable for clustering — it is
internally consistent (one tool version, one sequence database, one structure snapshot across all
21,926), whereas the dbNSFP column mixes whatever was current when each value was computed.

**Caveat inherent to the tool:** PolyPhen-2 v2.2.3r408's sequence database is UniRef100 release
**2011_12**. Fifteen years old, not a choice we made, and worth weighing when comparing this feature
against ESM-1b or AlphaMissense.

## The paper's SIFT/PolyPhen coverage did not come from dbNSFP

`mutations_clustering.md` §3 documents SIFT, PolyPhen-2, REVEL, AlphaMissense and ClinPred as all
coming from one MyVariant/dbNSFP query (`q=dbnsfp.genename:JAK1`), at ~33%. It does not address why
the paper reports SIFT and PolyPhen-2 at **43.74% missing = 56.3% present**, nearly double.

Tested directly ([`test_sift_coverage.py`](test_sift_coverage.py)) — querying by **genomic region**
instead of gene name:

| query | dbNSFP records | SIFT | SIFT4G | PolyPhen-2 | ClinPred |
|---|--:|--:|--:|--:|--:|
| `dbnsfp.genename:JAK1` | 8,501 | **6,873** | 6,873 | 6,873 | 6,873 |
| `chr1:65,298,912-65,432,187` (GRCh37) | 8,501 | **6,873** | 6,873 | 6,873 | 6,873 |

**Identical — 0 variants unique to either query.** Query strategy is not the explanation. All four
predictors share exactly the same 6,873, so 31.3% is a uniform property of the data, not of how it
is fetched.

The reason is structural: dbNSFP is built from all possible **single**-nucleotide changes. Nine SNVs
per codon (3 positions × 3 alternates) yield at most ~6 distinct amino-acid changes out of 19, so
~31% is dbNSFP's ceiling by construction and **no query can exceed it**.

Therefore the paper's 56.3% **cannot have come from dbNSFP**. Combined with its ClinPred at only
14.25% — *below* what dbNSFP offers — its SIFT, PolyPhen-2 and BLOSUM62 (all three at exactly
43.74% missing) must have been produced by a separate route, most likely running the tools
themselves. Our PolyPhen-2 run reaching 100% shows a full native run gives complete coverage, so
their 56.3% was a partial one. The mechanism remains unknown, but it is a question about their
pipeline, not a shortfall in this one.

## Clustering — done

**Semi-supervised K-means on Gower distance, seeded with the 10 labelled variants** named in
Appendix §2.2, run on all 21,926 substitutions and compared with EV1 variant by variant. Full
write-up: **[`clustering_jak1_results.md`](clustering_jak1_results.md)**. Scripts
[`cluster_jak1.py`](cluster_jak1.py) and [`compare_clustering.py`](compare_clustering.py); output
[`jak1_clustering_rebuilt.csv`](jak1_clustering_rebuilt.csv) (both labels on every row) and
[`jak1_clustering_comparison.json`](jak1_clustering_comparison.json).

| | |
|---|--:|
| same label as EV1 | **18,608 / 21,926 — 84.87%** |
| **Adjusted Rand Index** | **0.4836** |
| Cohen's κ | 0.6737 |
| cluster sizes, paper → rebuilt | 7,559 / 14,367 → **8,401 / 13,525** |
| label-permutation null | 53.6% |

So the two-cluster structure reproduces in outline, well beyond chance, but **ARI 0.48 is moderate**
— one variant in seven is assigned differently, concentrated in the intermediate band where no
feature is decisive. Four headline findings:

1. **`T138H`, one of the ten published seeds, is not a JAK1 variant** — position 138 is Tyr. The
   clustering necessarily ran on 4 + 5 anchors. `Y138H` is the likely intent and changes nothing.
2. **The seeds do not matter.** 25 random 5 + 5 draws from the EV1 clusters give ARI 0.4833–0.4839,
   indistinguishable from the named seeds. The supervision only *orients* the result (which pole is
   "Cluster 1"); the structure is unsupervised.
3. **PolyPhen-2 dominates** (leave-one-out ΔARI −0.090, twice the next five combined), which makes
   the paper's silence on HumDiv vs HumVar the most consequential ambiguity in reproducing it.
4. **The ΔΔG features subtract, though they are not uninformative.** `ddg_delta` is inert to four
   decimals; dropping all three ΔΔG features gives the *closest* agreement with the paper of anything
   tried (ARI 0.4917, sizes 7,868 / 14,058). Consistent with the clash contamination in
   `build_rosetta_ddg_jak1_info.md` §3. Note that oriented correctly — these columns are
   ΔΔG = ΔG_WT − ΔG_mut, so **negative = destabilising**, the opposite of FoldX in the same table —
   `ddg_closed` and `ddg_open` reach AUC 0.74 against the EV1 clusters, on a par with FoldX at 0.72.
   They are redundant with FoldX rather than blank.

## Where the two clusterings disagree

*Added 3 November 2026, computed from `jak1_clustering_rebuilt.csv`.*

The 3,318 disagreements (15.13%) are not spread evenly. Two independent effects concentrate them.

**1. They sit in the intermediate band.** C1 is the tolerant cluster, C2 the damaging one, and the
variants that move are exactly those between the poles:

| group | n | AlphaMissense median |
|---|--:|--:|
| paper C1, agreed | 6,321 | **0.166** |
| paper C2 → rebuilt C1 | 2,080 | 0.323 |
| paper C1 → rebuilt C2 | 1,238 | 0.745 |
| paper C2, agreed | 12,287 | **0.953** |

**2. They concentrate where features are missing.** Disagreement rises monotonically as coverage
falls, and the three 31.3%-coverage features are present in 33.7% of agreements but only 18.2% of
disagreements:

| features present | n | disagreement |
|--:|--:|--:|
| 7 | 765 | **25.5%** |
| 8 | 14,288 | 17.6% |
| 10 | 356 | 11.2% |
| 11 | 6,517 | **8.7%** |

**The two effects are independent and multiply.** Within every AlphaMissense band, coverage still
costs 6.8 to 16.1 percentage points:

| AlphaMissense band | n | overall | ≤8 features | ≥10 features |
|---|--:|--:|--:|--:|
| confident tolerant (<0.25) | 5,416 | 14.5% | 19.8% | 9.3% |
| intermediate-low (0.25–0.55) | 4,068 | **31.8%** | **36.5%** | 20.4% |
| intermediate-high (0.55–0.80) | 2,850 | 21.8% | 25.7% | 10.8% |
| confident damaging (≥0.80) | 9,592 | **6.4%** | 8.0% | **1.2%** |

### What this does to the headline number

| subset | n | agreement | **ARI** |
|---|--:|--:|--:|
| ALL — the published headline | 21,926 | 84.9% | **0.484** |
| high coverage (≥10 of 11 features) | 6,873 | 91.2% | 0.679 |
| confident AlphaMissense | 15,008 | 90.6% | 0.657 |
| **both: high coverage AND confident AM** | 4,931 | **94.3%** | **0.786** |
| **neither: ≤8 features AND intermediate AM** | 4,976 | **68.0%** | **0.130** |

**The reproduction is substantially better than ARI 0.484 suggests.** Where both clusterings have
the data to decide they agree 94.3% at ARI 0.786, and the best cell — confident-damaging at high
coverage — disagrees on 1.2% of variants. The headline is dragged down by 4,976 variants with
sparse features *and* intermediate scores, which disagree 68% of the time at ARI 0.130: barely
above chance. Those are substitutions needing 2–3 nucleotide changes, so CADD, SIFT and ClinPred
are all absent, leaving Gower distance over 7–8 dimensions on a variant that is ambiguous anyway.
**Neither label is trustworthy there**, so scoring the disagreement against the rebuild overstates
the gap.

### Consequence for the open question

The gap was previously attributed to one of: ΔΔG contamination, the HumDiv/HumVar ambiguity, or
something unknown in the paper's pipeline. Those explain little by comparison — dropping all three
ΔΔG features moves ARI 0.484 → 0.492. Stratifying by data quality moves it 0.484 → 0.786, an order
of magnitude more. **The dominant cause is missingness interacting with the Gower distance**, not a
methodological difference.

This also means the published EV1 assignment carries very different confidence per variant, and
nothing in EV1 marks which. A per-variant confidence field — feature count plus distance to the
decision boundary — would be more useful than further tuning of the clustering.
