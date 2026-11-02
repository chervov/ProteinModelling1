# JAK1 clustering — rebuilt step by step

Rebuilding the Jeanpierre/Debeaupuis JAK1 variant clustering from the ground up, one feature
at a time, with every step checked before the next is added. Started 2 November 2026.

Each feature file holds **all 23,080 Dataset EV1 rows in EV1 order**, so any two can be joined
by row position as well as by `variant_id`.

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
| ddG closed / open / open−closed | only 500 variants (2.3%) exist, in `data/orianne/jak1_cluster_ddg.json` |

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

## Clustering

Once the matrix is assembled the clustering itself is **semi-supervised K-means on Gower
distance, seeded with 10 labelled variants**, per the paper's Appendix S3. The comparison that is
currently missing from this project is a **per-variant** agreement measure — Adjusted Rand Index
and a confusion matrix against the EV1 labels — rather than only cluster sizes and marginal
statistics.
