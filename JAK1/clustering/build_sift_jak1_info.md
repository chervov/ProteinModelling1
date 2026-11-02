# SIFT for JAK1 — what it is, where it came from, and what the file contains

Covers [`jak1_sift.csv`](jak1_sift.csv). Written 2 November 2026. The route comparison is in
[`build_dbnsfp_jak1_info.md`](build_dbnsfp_jak1_info.md) §8; this file is the feature's own record.

---

## 1. What SIFT measures

**S**orting **I**ntolerant **F**rom **T**olerant. For each position it builds a multiple alignment
of homologous sequences, derives a position-specific scoring matrix with sequence weighting and
pseudocounts, and reports a **scaled probability** for each amino acid: how acceptable that residue
is at that position given what evolution has tolerated.

| | |
|---|---|
| range | **0 to 1** |
| direction | **low = damaging** (inverted relative to most predictors) |
| damaging threshold | **≤ 0.05** |
| what it uses | sequence conservation only — **no structure**, no allele frequencies, no training on disease labels |

Being alignment-based has one consequence that matters here: SIFT is a function of the **amino-acid
change alone**. Measured over the 759 JAK1 substitutions reachable by more than one nucleotide
change, the within-substitution spread is **exactly 0.000000** — every genomic route to the same
protein change gives the same score. Contrast ClinPred (0.434) and REVEL (0.243), which are not
protein-level. So SIFT *could* be computed for all 21,926 substitutions; only the lack of a working
service prevents it.

## 2. Two different SIFTs, disagreeing on one call in ten

dbNSFP carries `sift` and `sift4g` as separate columns — the original SIFT and **SIFT4G**
(Vaser et al. 2016), a reimplementation built for genome-scale speed. They are **not**
interchangeable:

| | |
|---|--:|
| Pearson / Spearman | 0.8975 / 0.9394 |
| identical values | 884 of 6,873 (**12.9%**) |
| median absolute difference | 0.017 (worst 0.955) |
| median score | SIFT 0.0250, SIFT4G 0.0560 |
| called damaging (≤ 0.05) | SIFT **57.5%**, SIFT4G **48.8%** |
| **disagree on the damaging call** | **730 (10.6%)** |

The paper cites **Sim et al. 2012**, which is the original SIFT web server, so **`sift` is the
column to use**. `sift4g` is carried alongside for comparison, deliberately not merged. SIFT4G is
the more conservative of the two here, calling 8.7 points fewer variants damaging.

## 3. Where this came from

**dbNSFP 4.8a, served by MyVariant.info** — not dbSNP, which carries no predictor scores at all
(see `build_dbnsfp_jak1_info.md` §6).

```
GET https://myvariant.info/v1/query
    q      = dbnsfp.genename:JAK1
    fields = dbnsfp.aa,dbnsfp.sift,dbnsfp.sift4g
```

Script: [`build_dbnsfp_features.py`](build_dbnsfp_features.py).

**Coverage is 31.3% (6,873 of 21,926)** and that is dbNSFP's structural ceiling: it is built from
single-nucleotide changes only, so ~69% of amino-acid substitutions have no row. Querying by genomic
region instead of gene name returns identical results ([`test_sift_coverage.py`](test_sift_coverage.py)),
so no query strategy helps.

Other routes, all tested — none better:

| route | coverage | why not |
|---|--:|---|
| Ensembl VEP REST | ~31% | works, but takes nucleotide input, so the same ceiling |
| EBI Proteins API | 8.8% | protein-keyed and adds 113 new substitutions (+0.6 pt), but only **15.9%** of shared values match — a different alignment |
| SIFT web server | 100% | **HTTP 502**, origin down |
| PROVEAN | — | **retired**, redirects to `sitedown.jcvi.org` |
| `sift4g` locally | **100%** | the only full-coverage route: Linux plus a protein database |

**Validation:** against the `sift` column in `data/orianne/jak1_features.json`, **6,873 of 6,873
identical, max difference 0.000000.** That exactness validates the query, the field paths and the
position mapping — the values are certainly right; only the quantity is limited.

## 4. The file

[`jak1_sift.csv`](jak1_sift.csv) — **23,080 rows**, one per Dataset EV1 row, in EV1 order.

```csv
variant_id,wt,pos,alt,cluster,sift,sift4g
A1005A,A,1005,A,1,,
A1005C,A,1005,C,2,,
A1005E,A,1005,E,2,0.001,0.0
```

| column | meaning |
|---|---|
| `variant_id` | **the index** — the EV1 `variant_id`, e.g. `A1005E` (wild type, position, mutant) |
| `wt`, `pos`, `alt` | the same parsed out, so no string handling is needed |
| `cluster` | the paper's EV1 cluster label, carried along for convenience |
| `sift` | **original SIFT** scaled probability — the feature to use |
| `sift4g` | SIFT4G, for comparison only |

### Row set and ordering

All **23,080** EV1 rows are kept, not the 21,926 real substitutions. EV1 includes 1,154
**self-substitutions** (`A1005A`, where wild type equals "mutant"), and keeping them means every
feature file in this directory has identical row count and order. So any two can be joined **either**
on `variant_id` **or** by row position. First row `A1005A`, last `Y999Y`.

### Missing values are empty fields

A missing score is written as **nothing at all** — `A1005A,A,1005,A,1,,` — not `NA`, `NaN`, `null`,
`.`, `-1` or `0`.

This is deliberate. **A SIFT score of `0.0` is a real, meaningful value** meaning maximally
intolerant: in the example above `A1005E` has `sift4g = 0.0`. Any numeric sentinel would collide
with genuine data. An empty field cannot.

Read back as missing by default in the usual tools:

```python
pd.read_csv("jak1_sift.csv")                 # -> NaN
```
```r
read.csv("jak1_sift.csv")                    # -> NA
```

**16,207 of 23,080 rows are blank**, which decomposes as:

| | n |
|---|--:|
| self-substitutions (no score exists) | 1,154 |
| substitutions needing 2–3 nucleotide changes (absent from dbNSFP) | 15,053 |
| **total blank** | **16,207** |
| populated | **6,873** |

So blankness carries information here, and it is not random: it marks the substitutions a
genomic-indexed source cannot reach. Anything that imputes these values is imputing a
**systematically more severe** set — the unreachable substitutions average BLOSUM62 −1.76 against
−0.54 for the reachable ones.

## 5. How to read the numbers

| `sift` | reading |
|---|---|
| ≤ 0.05 | **damaging** / intolerant |
| > 0.05 | tolerated |
| 0.0 | maximally intolerant — a real value, not missing |

Low is bad, which is the opposite of AlphaMissense, PolyPhen-2, REVEL, ClinPred and CADD. When
combining features, SIFT must be inverted or the distance will be computed with one axis reversed.

For scale, the medians in this file are **SIFT 0.025** and **SIFT4G 0.056** — so over all possible
JAK1 substitutions the typical one sits at or just past the damaging threshold, which is what you
would expect for a set dominated by substitutions never observed in a living person.
