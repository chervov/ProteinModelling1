# gnomAD population frequencies for JAK1 — provenance, the two exclusions, and the confound

Companion to [`build_gnomad.py`](build_gnomad.py), which writes
[`jak1_gnomad.csv`](jak1_gnomad.csv). Written 3 November 2026. Every number below was produced by
running that script, not quoted from a paper.

gnomAD is the only feature in this directory that **neither clustering used**. That makes it an
external test rather than an input: if an unsupervised split of predictor scores is biologically
meaningful, variants the population tolerates should fall preferentially in one cluster. They do.

---

## 1. Where the data comes from

gnomAD v4 through the public GraphQL endpoint, queried by gene symbol against GRCh38. No key, no
registration, one request:

```python
QUERY = ("query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){"
         "variants(dataset:gnomad_r4){consequence hgvsp exome{af ac an} genome{af ac an}}}}")
```

The response carries **5,104 variants** for JAK1 across all consequence classes — 2,954 intronic,
1,132 missense, 586 synonymous, 165 splice-region, and the rest UTR and upstream. Only the
**1,132 missense** records are used.

The protein change arrives as an HGVSp string, `p.Val658Phe`, which is parsed into (wild type,
position, alternate). gnomAD gives no UniProt position directly, so this string is the only link to
the EV1 numbering — which is why it is checked rather than trusted.

## 2. Two exclusions, both deliberate

### 2a. 89 records whose wild-type residue disagrees with P23458

```python
if not (1 <= pos <= len(seq)) or seq[pos - 1] != wt:
    mismatched.append(...)
    continue
```

89 of the 1,132 missense records name a wild-type residue that is **not** what UniProt P23458 has at
that position. They are not scattered: **every one falls between positions 665 and 708**, a
44-residue window. No constant offset reconciles them — the best-fitting shift explains only 16 of
the 89 — so this is not a simple numbering difference but a different transcript with an alternative
exon in that region.

They are **dropped, not remapped**. Guessing an alignment would put population data on the wrong
residues, which is worse than a gap.

**The gap is not in neutral territory.** Positions 665–708 sit inside the JH2 pseudokinase domain
(583–855), the region this project cares about most and the one containing the V658F-equivalent
position. Any use of the gnomAD column near there should know it is sparse for an annotation reason,
not a biological one. This is logged as an open item in the [README](README.md).

### 2b. 100 records with allele count zero

gnomAD lists ~100 JAK1 missense sites with `af == 0.0` and `ac == 0`: the position was sequenced —
`an` is around 1.46 million alleles — but **no copy of the alternate allele was ever seen**. They are
in the table as sites, not as observations, and are excluded:

```python
if af is None or ac == 0:
    n_zero_ac += 1
    continue
```

**This test is written on allele count, deliberately.** The obvious idiom

```python
af = ex.get("af") or ge.get("af")     # DON'T
```

appears to do the same job, because `0.0` is falsy in Python. It does not. It drops the 95
exome-only cases but **keeps** the 4 genome-only and 1 both-sources cases, where the `or` falls
through to a second `0.0` and returns it. An earlier version of this script used that idiom and
counted 939 observed variants instead of 934 — five unobserved sites admitted by accident. The same
falsy-zero trap is why this directory's convention is **empty fields, never `0`**, for missing
values.

## 3. The funnel

| step | records |
|---|--:|
| gnomAD r4 variants for JAK1, all classes | 5,104 |
| missense | 1,132 |
| with a parseable `p.` HGVSp | 1,132 |
| &minus; wild type disagrees with P23458 (positions 665–708) | &minus;89 |
| &minus; allele count 0 (sequenced, never observed) | &minus;100 |
| accepted, deduplicated to distinct (position, alternate) | **934** |

934 of 21,926 possible substitutions, **4.26%**. Where a
substitution is reachable by more than one nucleotide change, the record with the highest allele
frequency is kept.

## 4. The file

[`jak1_gnomad.csv`](jak1_gnomad.csv) — all **23,080 EV1 rows in EV1 order**, so it joins to every
other feature file here by row position as well as by `variant_id`.

| column | meaning |
|---|---|
| `variant_id`, `wt`, `pos`, `alt`, `cluster` | the standard index for this directory |
| `gnomad_af` | allele frequency, highest across exome and genome; **empty** if never observed |
| `gnomad_ac` | allele count; empty if never observed |
| `gnomad_an` | allele number at that site |
| `in_gnomad` | 1 or 0 — the convenience flag used for enrichment |

Blank means **not observed**, and is left blank rather than set to 0 for the reason in §2b.

## 5. What it shows, and the confound that nearly broke it

Raw rates by the paper's EV1 clusters:

| | observed in gnomAD | n |
|---|--:|--:|
| cluster 1 (tolerant) | **7.29%** | 7,559 |
| cluster 2 (damaging) | **2.67%** | 14,367 |

Pooled odds ratio **2.87**, Fisher p = 5.6e-55. **That figure is
confounded and should not be quoted.**

**100.0% of gnomAD-matched variants fall in the dbNSFP-defined subset**, which
is only 31.3% of all variants. That is structural rather than coincidental: gnomAD
holds observed SNVs and dbNSFP indexes exactly the single-nucleotide-reachable substitutions, so the
two sets nearly coincide. And the tolerant cluster is disproportionately inside it —
37.3% of C1 against 28.2% of C2. Pooling across strata therefore
inflates the association: a textbook Simpson's paradox.

Stratifying by dbNSFP reachability and combining with Mantel–Haenszel:

| clustering | pooled OR | **stratified OR** | within-dbNSFP p |
|---|--:|--:|--:|
| paper (EV1) | 2.87 | **2.32** | 2.1e-32 |
| rebuilt | 2.83 | **2.4** | 1.1e-34 |

**The finding survives the correction**, and the two clusterings remain indistinguishable
(2.32 against 2.4) despite disagreeing on one variant in
seven. The second stratum carries only
0 gnomAD observations among
15,053 variants, so its apparent
reversal is noise, not a counter-signal.

## 6. What this does NOT control for

**Mutability.** CpG dinucleotides mutate roughly an order of magnitude faster than other sites. If
the tolerant cluster is enriched for CpG positions, part of the stratified odds ratio is mutational
*opportunity* rather than purifying selection. Settling it needs a trinucleotide-context expectation
per variant, testing observed against expected rather than observed against the other cluster. Not
computed here; logged as an open item.

**Ancestry structure and filtering.** The allele frequency used is the global one, highest across
exome and genome. Population-specific frequencies and the per-variant FILTER status are available in
the API response and are not used.

## 7. Related material

- [`jak1_clustering_analysis.html`](jak1_clustering_analysis.html) — the full exploratory report,
  with the enrichment figures, the allele-frequency gradient and the along-the-protein anticorrelation
  (Spearman ρ = -0.546 over 47 windows).
- [`jak1_clustering_rebuilt.csv`](jak1_clustering_rebuilt.csv) — the clustering this is tested against.
- [`README.md`](README.md) — directory conventions, and the open items this file contributes.
