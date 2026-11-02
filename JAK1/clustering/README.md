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
| SIFT | available at 31.3% from dbNSFP; **can reach 100%** by running SIFT directly, since it scores any substitution from an alignment |
| PolyPhen-2 | same — 31.3% via dbNSFP, protein-level in principle |
| ClinPred | 31.3%, dbNSFP only |
| REVEL | 31.3%, dbNSFP only |
| CADD | not obtained; the earlier attempt is recorded in `mutations_clustering.md` |
| MutFunc | not obtained (92.07% missing in the paper itself) |
| ddG closed / open / open−closed | only 500 variants (2.3%) exist, in `data/orianne/jak1_cluster_ddg.json` |

Once the matrix is assembled the clustering itself is **semi-supervised K-means on Gower
distance, seeded with 10 labelled variants**, per the paper's Appendix S3. The comparison that is
currently missing from this project is a **per-variant** agreement measure — Adjusted Rand Index
and a confusion matrix against the EV1 labels — rather than only cluster sizes and marginal
statistics.
