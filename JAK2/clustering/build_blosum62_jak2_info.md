# BLOSUM62 for JAK2 — computed, not fetched

Companion to [`build_blosum62.py`](build_blosum62.py), which writes
[`jak2_blosum62.csv`](jak2_blosum62.csv). Written 3 November 2026.

**21,508 of 21,508 — 100%, in 0.2 s, no network.** A 20×20 lookup cannot be missing.

---

## 1. Source

Henikoff S & Henikoff JG, *Amino acid substitution matrices from protein blocks*, **PNAS**
1992;89:10915–10919. The matrix is taken from Biopython's `substitution_matrices`, which ships the
NCBI table.

## 2. The matrix is cross-checked, not trusted

A silent version difference in a dependency would be invisible and would change every value. So the
published matrix is written out in the script as `REFERENCE` and compared cell by cell:

```
matrix: Biopython agrees with the published BLOSUM62 at all 400 cells
```

If Biopython is absent, the embedded copy is used instead, so the script has **no hard dependency**.
That matters for a pipeline meant to run elsewhere.

## 3. It is the only position-blind feature

BLOSUM62 depends on the substitution alone. **Every V→F in JAK2 scores −1**, all 56 of them,
wherever they sit. On JAK1 it was both the weakest predictor of the paper's clusters (AUC 0.632)
and the least correlated with the others (0.28–0.39 against 0.64–0.83 among the rest) — which is
what a feature carrying no positional information should look like.

## 4. Output

[`jak2_blosum62.csv`](jak2_blosum62.csv), 516 KB, columns
`index, variant, wt, pos, alt, blosum62`.

| score | −4 | −3 | −2 | −1 | 0 | 1 | 2 | 3 |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| n | 909 | 4,892 | 5,202 | 4,981 | 2,978 | 1,429 | 882 | 235 |

Range −4 … 3; lower = less conservative substitution.

**No diagonal entries.** Self-substitutions would take the matrix diagonal (A→A = 4), a real value,
but this directory's universe excludes them — unlike JAK1, which kept 1,154 of them to match
Dataset EV1 row-for-row. So this file has no blanks and no diagonal.

## 5. The paper reports BLOSUM62 as 43.74% missing

A BLOSUM62 lookup can never be missing. That figure is identical to the paper's SIFT and
PolyPhen-2 missingness, which shows the value was taken from the same annotation source as those
two — dbNSFP or VEP — and inherited its coverage gaps rather than being computed. Computing it
locally gives 100%, as here and as in JAK1.

## 6. Timing and alternatives

0.2 s, entirely local. No alternatives were needed or considered: there is one published BLOSUM62,
and nothing to download.
