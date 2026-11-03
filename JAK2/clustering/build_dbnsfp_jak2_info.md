# CADD, SIFT and ClinPred for JAK2 — dbNSFP, and its hard 31% ceiling

Companion to [`build_dbnsfp.py`](build_dbnsfp.py), which writes
[`jak2_cadd.csv`](jak2_cadd.csv), [`jak2_sift.csv`](jak2_sift.csv) and
[`jak2_clinpred.csv`](jak2_clinpred.csv). Written 3 November 2026.

**6,697 of 21,508 each — 31.1%, in 48 s.** That is dbNSFP's structural ceiling, not a shortfall in
the fetching.

---

## 1. Source

dbNSFP (Liu et al.), accessed through **myvariant.info**, its standard programmatic interface:

```
https://myvariant.info/v1/query?q=dbnsfp.genename:JAK2&fields=...&size=1000&from=N
```

The full dbNSFP release is tens of gigabytes; the API serves the same records by gene, which is
what makes this usable for an arbitrary protein. **8,361 records** for JAK2, fetched in 9 pages of
1,000.

Alternatives considered: downloading dbNSFP itself (tens of GB, and per-chromosome files needing
coordinate mapping — all cost, no benefit at one gene), and Ensembl VEP (runs the tools rather than
serving dbNSFP's cached values, so it would not match what the paper used).

## 2. Why 31%, and why no query can beat it

**dbNSFP is built from all possible *single*-nucleotide changes.** Nine SNVs per codon (3 positions
× 3 alternates) reach at most about 6 of the 19 possible amino-acid substitutions. So ~31% is the
ceiling by construction.

The JAK1 directory tested this directly rather than assuming it
([`JAK1/clustering/test_sift_coverage.py`](../../JAK1/clustering/test_sift_coverage.py)): a
gene-name query and a genomic-region query returned **identical record sets, 0 variants unique to
either**. Query strategy is not the lever.

This is also why **PolyPhen-2 is fetched from its own server instead**
([`build_polyphen_jak2_info.md`](build_polyphen_jak2_info.md)): it is protein-level and reaches
100%.

## 3. Two problems in the data, both measured

### 3a. dbNSFP is keyed on nucleotides, so the mapping is many-to-one

The same amino-acid substitution can arise from several nucleotide changes and appears several
times. Values are aggregated with **`max`**, as JAK1 did — but the spread across routes is printed
first, so the choice is visible rather than silent:

| feature | substitutions | reachable by >1 SNV | **max spread** |
|---|--:|--:|--:|
| SIFT | 6,697 | 766 | **0.0000** |
| **ClinPred** | 6,697 | 766 | **0.7841** |
| CADD | 7,108 | 863 | 10.1190 |

**SIFT behaves as a protein-level score should** — identical by whichever nucleotide route, spread
exactly zero.

**CADD is expected to vary**: it scores the nucleotide change, not the amino-acid change, so
different routes to the same substitution genuinely differ. A spread of 10 Phred is large but not
anomalous.

**ClinPred is the surprise.** It is presented as a missense pathogenicity score, yet the same
substitution scores up to **0.78 apart on a 0–1 scale** depending on the nucleotide route. It must
be folding in genomic or allele-frequency features. So `max` is a real choice affecting 766
variants here, not a formality — and the same caveat applies to the JAK1 column, which was
aggregated the same way without this having been measured.

### 3b. 411 stop-gains had to be excluded

CADD initially reported 7,108 substitutions against 6,697 written. The difference is **411
variants whose alternate residue is `X`** — stop-gains, which dbNSFP includes and a missense
universe does not. Examples: `C1094X`, `C1105X`, `C125X`. Correctly dropped; the discrepancy was
chased down rather than rounded over.

### 3c. 272 records skipped on transcript ambiguity

`dbnsfp.aa.pos` can carry several transcript positions. Each record keeps only the position whose
wild-type residue matches the pinned sequence; **272 of 8,361 records had none** and were dropped.
This is the same check that caught a bad join earlier in the project.

## 4. Output

Three files, 516 KB each, 21,508 rows in the canonical order.

| file | populated | range | direction |
|---|--:|---|---|
| [`jak2_cadd.csv`](jak2_cadd.csv) | 6,697 (31.1%) | 0.001 … 35 | higher = more damaging |
| [`jak2_sift.csv`](jak2_sift.csv) | 6,697 (31.1%) | 0 … 1 | **lower** = more damaging |
| [`jak2_clinpred.csv`](jak2_clinpred.csv) | 6,697 (31.1%) | 0.0053 … 0.99999 | higher = more damaging |

SIFT runs the other way from the other two. Thresholds, from the dbNSFP README where the authors
define one: SIFT ≤ 0.05, CADD ≥ 20 by convention, ClinPred ≥ 0.5 by the authors.

## 5. The coverage gap is not random

The 68.9% without these three are the substitutions needing two or three nucleotide changes. They
are systematically **more severe** — on JAK1, BLOSUM62 mean −1.76 against −0.54 for the reachable
ones. So this is not a random sample, and imputing would bias the result. Gower distance handles
it by comparing each pair on the features both have.

On JAK1 this mattered: disagreement between the two clusterings ran at 8.7% where all 11 features
were present and 25.5% where only 7 were, independently of how damaging the variant was.

## 6. Timing

| step | time |
|---|---|
| 9 paginated API calls, 8,361 records | ~45 s |
| parse, dedup, write three files | ~3 s |
| **total** | **48 s** |
