# gnomAD for JAK2 — the primary external criterion

Companion to [`build_gnomad.py`](build_gnomad.py), which writes
[`jak2_gnomad.csv`](jak2_gnomad.csv). Written 3 November 2026.

**1,498 of 21,508 observed — 6.96%.** About 9 s.

---

## 1. Why this matters more for JAK2 than it did for JAK1

JAK1 had Dataset EV1: a published clustering to measure against. **JAK2 has none.** So the
clustering cannot be scored by agreement with anyone — it has to be validated against data that
**no feature saw**. gnomAD is that data, and on JAK1 it worked: both the paper's clustering and the
rebuild depleted the damaging cluster of observed variation by a stratified odds ratio of 2.3–2.4,
p ≈ 10⁻³³, from a split that never saw population frequencies.

## 2. Source

The public gnomAD GraphQL endpoint, `https://gnomad.broadinstitute.org/api`, queried by gene symbol
against GRCh38, dataset `gnomad_r4`. No key, no registration, one request.

Returns **6,809 variants for JAK2** across all consequence classes, of which **1,923 are missense**.

## 3. Two deliberate decisions, both learned from JAK1

### 3a. The wild-type residue is verified, not assumed

gnomAD gives no UniProt position — only an HGVSp string, so that string is the only link to our
numbering. Matching on (position, alt) alone is not safe:

> On JAK1, **89 records disagreed** with the canonical sequence, all in positions 665–708, where
> gnomAD evidently annotates a different transcript. No constant offset reconciled them (the best
> fit explained 16 of 89), so they were dropped — leaving a documented blind spot inside the JH2
> pseudokinase domain.

**For JAK2 there were zero mismatches.** The same check, the same code, a clean result — which is
the point of running it rather than assuming either outcome.

### 3b. "Observed" means allele count > 0, tested explicitly

gnomAD lists sites that were sequenced but never seen: `af == 0.0` with `ac == 0` at an allele
number around 1.4 M. **392 JAK2 records are like this** and are excluded.

The obvious idiom looks equivalent and is not:

```python
af = ex.get("af") or ge.get("af")     # WRONG
```

It drops the exome-only zero cases only because `0.0` is falsy, and **keeps** the genome-only and
both-source ones, where the `or` falls through to a second `0.0` and returns it. On JAK1 that
admitted 5 never-observed sites and inflated the count from 934 to 939. The test here is on
`ac == 0`, written out.

## 4. Output

[`jak2_gnomad.csv`](jak2_gnomad.csv), 21,508 rows in the canonical order, columns
`index, variant, wt, pos, alt, gnomad_af, gnomad_ac, gnomad_an, in_gnomad`.

| | |
|---|--:|
| observed | **1,498 (6.96%)** |
| allele frequency | 6.84×10⁻⁷ … 1.29×10⁻² |
| median AF | 1.37×10⁻⁶ |
| above AF 10⁻⁴ | 26 |
| above AF 10⁻³ | 7 |

Blank means **not observed**, left blank rather than 0 — an allele frequency of 0 and "never seen"
are different statements, and the distinction is exactly what §3b is about.

**JAK2 is better covered than JAK1**: 6.96% against 4.3%. More observed variants means more
statistical power for the enrichment test that has to carry the validation.

## 5. The confound to apply when using this

On JAK1, the pooled enrichment was **inflated by a Simpson's paradox** and had to be corrected:
96.7% of gnomAD-matched variants fall in the dbNSFP-reachable subset, which is only ~31% of all
variants, and the tolerant cluster is disproportionately inside it. Pooling across strata gave
OR 2.89 where the Mantel–Haenszel estimate was 2.32.

**The same correction will be needed here.** gnomAD holds observed SNVs and dbNSFP indexes exactly
the single-nucleotide-reachable substitutions, so the two sets nearly coincide for JAK2 too. Report
the stratified odds ratio, not the pooled one.

**Not controlled for mutability.** CpG dinucleotides mutate roughly 10× faster, so part of any
enrichment could be mutational opportunity rather than selection. Settling it needs a
trinucleotide-context expectation per variant. Not done here, and logged as open on JAK1 too.

## 6. Timing and alternatives

| | |
|---|---|
| GraphQL query, 6,809 variants | ~8 s |
| parse, verify, write | < 1 s |

Alternatives not used: the gnomAD VCF releases (hundreds of GB, and would need coordinate→protein
mapping we would then have to verify anyway), and the gnomAD browser's per-variant pages (one HTTP
request per variant — thousands of requests for the same data).
