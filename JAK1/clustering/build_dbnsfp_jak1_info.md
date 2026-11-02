# ClinPred, SIFT and REVEL for JAK1 — source, method, and what the data turned out to be

How `jak1_clinpred.csv`, `jak1_sift.csv` and `jak1_revel.csv` were produced, why they stop at
31.3%, and an empirical finding that matters for using them: **ClinPred and REVEL are not
protein-level scores.** Written 2 November 2026.

---

## 1. The source — dbNSFP, not dbSNP

Easy to confuse, so to be explicit:

| | |
|---|---|
| **dbSNP** | a registry of observed variants and their rsIDs. Carries no pathogenicity predictions. **Not used here.** |
| **dbNSFP** | a precomputed database of functional predictions for non-synonymous SNVs — it aggregates ~40 published predictors onto every possible single-nucleotide coding change. **This is the source.** |
| **MyVariant.info** | a BioThings API that serves dbNSFP (among other sources) over HTTP, so no bulk download is needed. **This is the access route.** |

Version actually served, from `myvariant.info/v1/metadata`:

```
dbNSFP version   4.8a
downloaded       2025-01-17   (by MyVariant)
indexed          2025-02-19
MyVariant build  20250624
records          82,755,468   (hg19 index)
upstream         https://sites.google.com/site/jpopgen/dbNSFP
```

So the scores are dbNSFP **4.8a**. That matters for reproducibility: a later dbNSFP will shift
values, and the version is not visible from the CSVs themselves.

## 2. The query

```
GET https://myvariant.info/v1/query
    q        = dbnsfp.genename:JAK1
    fields   = dbnsfp.aa,dbnsfp.clinpred,dbnsfp.sift,dbnsfp.sift4g,dbnsfp.revel,dbnsfp.polyphen2
    fetch_all= true
```

Then page with the returned `_scroll_id`. **One trap:** the continuation request must repeat
`fields`, or later pages come back without the subdocuments you asked for — which silently yields
zeros rather than an error.

### The field paths are not what dbNSFP's own documentation implies

dbNSFP's flat files use columns `aaref`, `aaalt`, `aapos`. MyVariant nests them:

```json
"aa": {"ref": "Y", "alt": "F", "pos": 1048, "refcodon": "TAT",
       "codonpos": 2, "codon_degeneracy": 0}
```

There are no top-level `dbnsfp.aaref` fields. My first attempt requested those, got nothing, and
reported **0 substitutions** — a wrong answer that looked like a coverage result. The predictor
paths are:

| predictor | path |
|---|---|
| ClinPred | `dbnsfp.clinpred.{score, pred, rankscore}` |
| SIFT | `dbnsfp.sift.{score, pred, converted_rankscore}` |
| SIFT4G | `dbnsfp.sift4g.{score, pred, converted_rankscore}` |
| REVEL | `dbnsfp.revel.score` |
| PolyPhen-2 | `dbnsfp.polyphen2.{hdiv, hvar}.{score, pred, rankscore}` |

ClinPred is an object, not a bare float — `mutations_clustering.md` §3 flags the same thing.

### What came back

| | |
|---|--:|
| records for JAK1 | **8,501** |
| mapping to a protein substitution in 1–1154 | 8,218 |
| distinct substitutions | 7,274 |
| **distinct substitutions with predictor scores** | **6,873 (31.3% of 21,926)** |

All four predictors return **exactly the same 6,873** — the coverage is a property of the data, not
of any one tool.

## 3. The 31.3% ceiling is structural

dbNSFP is built from all possible **single**-nucleotide changes: 9 SNVs per codon (3 positions × 3
alternates) yield at most ~6 distinct amino-acid changes out of 19. So ~31% is dbNSFP's maximum by
construction.

Confirmed by experiment ([`test_sift_coverage.py`](test_sift_coverage.py)): querying by **genomic
region** (`chr1:65,298,912-65,432,187`, GRCh37) instead of gene name returns **identical** results —
6,873 both ways, **zero** variants unique to either. No query strategy can exceed it.

**For ClinPred and REVEL the ceiling cannot be lifted at all.** Both are *ensembles* whose input
features are other predictors' scores plus gnomAD per-population allele frequencies. A substitution
needing two nucleotide changes has no genomic SNV, therefore no allele frequency and no component
scores — there is nothing to feed the model. Running them ourselves would not help.

**SIFT is different**: it is a protein-level method (see §4), so it *could* reach 100%. The obstacle
is only that no service is up — `sift.bii.a-star.edu.sg` returns 502 and PROVEAN redirects to
`sitedown.jcvi.org`, leaving local `sift4g` (Linux plus a protein database) as the sole route. For
comparison, PolyPhen-2 **was** lifted to 100% this way; see
[`build_polyphen_jak1_info.md`](build_polyphen_jak1_info.md).

## 4. Finding: ClinPred and REVEL are not protein-level scores

759 substitutions are reachable by more than one nucleotide change. A genuinely protein-level score
must give one value per amino-acid change regardless of which SNV produced it. Measured:

| predictor | max spread within one substitution | protein-level? |
|---|--:|---|
| **SIFT** | **0.000000** | **yes** |
| **SIFT4G** | **0.000000** | **yes** |
| PolyPhen-2 HVAR | 0.141 | no (transcript-dependent) |
| REVEL | 0.243 | **no** |
| **ClinPred** | **0.434** | **no** |

**601 of the 759** multi-SNV substitutions have genuinely different ClinPred values across their
SNVs — 8.7% of the column. So for ClinPred and REVEL a "protein-level value" is **ill-defined** and
requires a documented aggregation rule. This is the empirical fingerprint of the ensemble argument
in §3: these scores partly describe the *nucleotide* event, not just the amino-acid change.

**The files here use `max`.** Stated rather than implied, because the choice is visible in the data.

## 5. Validation against the existing reproduction

Against the ClinPred/SIFT/REVEL columns in `data/orianne/jak1_features.json` (6,873 shared rows):

| predictor | identical | max difference |
|---|--:|--:|
| **SIFT** | **6,873 / 6,873** | **0.000000** |
| ClinPred | 6,541 | 0.414845 |
| REVEL | 6,647 | 0.204000 |

SIFT reproduces **exactly**, which validates the query, the field paths and the mapping.

The ClinPred and REVEL differences are entirely the aggregation question
([`check_clinpred.py`](check_clinpred.py)). Trying every simple rule:

| aggregation | disagreements | inside the 759 multi-SNV set | outside |
|---|--:|--:|--:|
| max | 332 | **332** | **0** |
| min | 293 | 293 | **0** |
| mean | 601 | 601 | **0** |
| first | 593 | 593 | **0** |

**Every disagreement under every rule falls inside the multi-SNV set; none outside.** The underlying
data is therefore identical to the existing reproduction — only the collapse differs. Note that *no*
simple rule reproduces it exactly (min comes closest, 293 still differing), so
`jak1_features.json` used some other selection, most plausibly the **canonical-transcript** record
rather than an aggregate over SNVs.

## 6. Can any of this come from dbSNP? No — on two independent counts

Worth settling explicitly, because dbSNP and dbNSFP are easy to conflate.

### It carries no prediction scores

Queried NCBI's RefSNP record directly for a JAK1 missense variant:

```
GET https://api.ncbi.nlm.nih.gov/variation/v0/refsnp/2100943997      (rs2100943997, JAK1 D1039N)
```

48,203 characters of JSON. Occurrences of each predictor name in the whole payload:

| searched for | mentions |
|---|--:|
| clinpred | **0** |
| sift | **0** |
| polyphen | **0** |
| revel | **0** |
| cadd | **0** |

What it *does* carry: `allele_annotation` (functional consequence — missense, synonymous and so
on), `frequency` (ALFA, gnomAD, TOPMed, 1000 Genomes), `clinical` (ClinVar links), plus HGVS,
placements and MANE Select ids. **No pathogenicity predictor is in dbSNP**, so ClinPred, SIFT,
REVEL, PolyPhen-2 and CADD cannot be obtained from it at all. dbSNP is a *registry of variants*;
dbNSFP is a *database of predictions about variants*.

### And its coverage is far worse, because it holds only observed variants

dbNSFP enumerates every possible single-nucleotide coding change. dbSNP contains only variants that
have actually been seen in a sample. Measured over the 8,501 JAK1 dbNSFP records:

| | n | share |
|---|--:|--:|
| JAK1 dbNSFP records | 8,501 | |
| with a ClinPred score | 7,742 | 91.1% |
| **with a dbSNP rsID at all** | **2,042** | **24.0%** |
| with both | 1,898 | |

So of the 7,742 scored variants, only **1,898 (24.5%)** exist in dbSNP — and as a share of all
21,926 possible substitutions, anything dbSNP-registered caps out at **9.3%**, against dbNSFP's
31.3%.

**Conclusion: dbSNP is the wrong instrument twice over** — it has no scores to give, and it covers
a third as many variants. Its genuine uses in this project are different ones: rsIDs for
cross-referencing, allele frequencies, and ClinVar links. Those are already obtained from gnomAD
and ClinVar directly.

## 7. An alternative source for ClinPred: UCSC

ClinPred is also hosted by UCSC as a composite of **four bigWigs, one per alternate allele**:

```
api.genome.ucsc.edu/getData/track?genome=hg38;track=clinPred{A|C|G|T};chrom=chr1;start=…;end=…
bulk: hgdownload.soe.ucsc.edu/gbdb/hg38/clinPred/{a,c,g,t}.bw
```

UCSC's track metadata says *"Downloaded from sites.google.com/site/clinpred on May 5, 2026"*, so it
is more recent than dbNSFP 4.8a's snapshot. Cross-checked eight JAK1 variants against dbNSFP —
**8 of 8 identical to four decimal places** (e.g. Y1048F 0.9394, Y1048S 0.9988, N931D 0.5358).

Worth knowing because it needs no dbNSFP dependency, is native hg38, and returns a value per
alternate allele directly. It does **not** improve coverage — it is the same genomic-SNV data.

## 8. Comparison with the paper

| feature | paper | here |
|---|--:|--:|
| ClinPred | 14.25% present | **31.3%** |
| SIFT | 56.3% present | 31.3% |
| REVEL | not in the paper's 11 | 31.3% |

ClinPred is a feature where this project is **2.2× ahead** of the paper. SIFT is the one where it is
behind, and `build_polyphen_jak1_info.md` §1 explains why the paper's number cannot have come from
dbNSFP either.

## 9. Files

| file | contents |
|---|---|
| [`jak1_clinpred.csv`](jak1_clinpred.csv) | ClinPred, 23,080 rows in EV1 order, 6,873 scored |
| [`jak1_sift.csv`](jak1_sift.csv) | SIFT and SIFT4G, same shape |
| [`jak1_revel.csv`](jak1_revel.csv) | REVEL, same shape |
| [`build_dbnsfp_features.py`](build_dbnsfp_features.py) | produces all three, and measures the within-substitution spread |
| [`check_clinpred.py`](check_clinpred.py) | the aggregation test in §5 |
| [`test_sift_coverage.py`](test_sift_coverage.py) | the region-vs-gene-name test in §3 |

Columns: `variant_id, wt, pos, alt, cluster, <predictor>`. All keep the full 23,080 EV1 rows so
they align by position with every other feature file here; the 1,154 self-substitutions and the
~15,000 multi-nucleotide substitutions are blank.
