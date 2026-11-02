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

Common columns: `variant_id, wt, pos, alt, cluster, <feature>`.

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

## Clustering

Once the matrix is assembled the clustering itself is **semi-supervised K-means on Gower
distance, seeded with 10 labelled variants**, per the paper's Appendix S3. The comparison that is
currently missing from this project is a **per-variant** agreement measure — Adjusted Rand Index
and a confusion matrix against the EV1 labels — rather than only cluster sizes and marginal
statistics.
