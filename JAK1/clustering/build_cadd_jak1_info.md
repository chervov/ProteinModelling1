# CADD for JAK1 — where to get it, and a correction to the project's notes

Covers [`jak1_cadd.csv`](jak1_cadd.csv). Written 2 November 2026.

**Headline: CADD was obtainable all along, free, in a single HTTP query.**
`mutations_clustering.md` §4 records it as *"attempted and unavailable … This is one of only two
sequence-based pathogenicity scores the paper names, so its absence is a real gap in the
reproduction, not a convenience omission."* That note is **stale**, and the reason is a field path.

---

## 1. What CADD is

**C**ombined **A**nnotation **D**ependent **D**epletion (Rentzsch et al. 2019). A model trained to
separate simulated *de novo* variants from variants that survived natural selection, over ~60
annotations — conservation, regulatory context, protein consequence, other predictors' scores.

| | |
|---|---|
| raw score | unbounded, model output |
| **PHRED** | **−10·log₁₀(rank / all ~8.6 billion SNVs)** — the usual column |
| **10** | top 10% of all possible SNVs |
| **20** | top 1% |
| **30** | top 0.1% |
| direction | **high = more deleterious** |
| scope | **every** SNV, coding or not — unlike missense-only predictors |

It is a **per-nucleotide** score by design, which matters below.

## 2. Where to get it — options compared

| route | coverage | cost | verdict |
|---|--:|---|---|
| **MyVariant `cadd.phred`** | **31.3%** (6,873) | one HTTP query, free | **use this** |
| dbNSFP `dbnsfp.cadd.phred` | **0%** | — | empty: CADD is licence-restricted inside the academic dbNSFP build |
| pre-scored file + tabix | 31.3% | **81.47 GB** file, or ~4 MB by remote range query | works, unnecessary |
| CADD web API | — | — | the endpoint format I tried 404s on both mirrors |
| run CADD locally | 31.3% | the full annotation stack | pointless |

### The correction: CADD is not inside dbNSFP, it is beside it

MyVariant serves CADD as **its own source document**, not as part of `dbnsfp`:

```
_exists_:dbnsfp.cadd.phred   ->  0 records      <- what was tried, hence "unavailable"
_exists_:cadd.phred          ->  8,229 records  <- CADD lives here
```

So the query is simply:

```
GET https://myvariant.info/v1/query
    q      = dbnsfp.genename:JAK1
    fields = dbnsfp.aa,cadd.phred,cadd.rawscore
```

The same class of mistake as requesting `dbnsfp.aaref` instead of `dbnsfp.aa.ref`
(`build_dbnsfp_jak1_info.md` §2): a wrong field path returns an empty result rather than an error,
which reads as "the data isn't there" instead of "I asked the wrong question". Worth checking
`_exists_:` on a field before concluding a source lacks it.

### The 81 GB route, for the record

If a genome-wide slice is ever needed beyond one gene, this was measured and works:

| | |
|---|--:|
| `whole_genome_SNVs.tsv.gz` (v1.7, GRCh38) | **81.47 GB** |
| `whole_genome_SNVs.tsv.gz.tbi` | 2.76 MB |
| HTTP byte-range support | **confirmed** (206 Partial Content) |
| measured density | **9.77 compressed bytes/row** |
| one JAK gene locus (~135 kb) | **≈ 4 MB** to fetch |
| all four JAK loci | ≈ 10 MB |

Mirrors: `krishna.gs.washington.edu` (US) and `kircherlab.bihealth.org` (DE). Free for
non-commercial use. Format is `chrom pos ref alt raw phred`. Note `pysam` does not build on
Windows, so a remote tabix query needs either a Linux box or a pure-Python bgzf reader.

## 3. Coverage: the same 31.3% ceiling

6,873 of 21,926 substitutions — identical to SIFT, ClinPred and REVEL, for the same structural
reason: CADD is scored per genomic SNV, so substitutions needing two or three nucleotide changes
have no entry. The 81 GB file would not help; it is the same single-nucleotide enumeration.

One detail: 7,274 distinct substitutions came back with a CADD score, but only **6,873** mapped
into EV1. The ~401 dropped refer to a **different wild-type residue** at that position — they come
from non-canonical transcripts whose amino acid differs from P23458. Dropping them is correct; the
same phenomenon produced the `R896I` anomaly found in the TYK2 table (position 896 is Tyr in the
canonical sequence).

## 4. CADD is the *least* protein-level feature in the set

Over the 834 substitutions reachable by more than one nucleotide change, the spread of CADD PHRED
*within a single amino-acid substitution*:

| feature | max within-substitution spread |
|---|--:|
| SIFT, SIFT4G | 0.000000 |
| PolyPhen-2 HVAR | 0.141 |
| REVEL | 0.243 |
| ClinPred | 0.434 |
| **CADD PHRED** | **16.45** |

**16.45 PHRED is enormous** — the difference between "top 10%" and "top 0.0003%" of all human SNVs,
for the same protein change. Expected, since CADD deliberately scores the nucleotide event with its
genomic context (CpG status, transversion, splice proximity), not the amino-acid swap.

Consequence: for a protein-level feature matrix CADD must be aggregated, and the choice is
consequential rather than cosmetic. **This file uses `max`**, stated explicitly.

## 5. Validation

Against the `CADD phred` column already in `external_data/JAK1/jak1_variants_inf_predict.csv`:

| | |
|---|--:|
| shared variants | 423 |
| **identical (within 0.05)** | **423 (100.0%)** |
| median absolute difference | **0.000** |
| maximum difference | **0.00** |

Perfect agreement — so the later work in this project already used this route, and only
`mutations_clustering.md` §4 was never updated.

## 6. The file

[`jak1_cadd.csv`](jak1_cadd.csv) — 23,080 rows, EV1 order, conventions as in the README
(`variant_id` index, empty field for missing).

```csv
variant_id,wt,pos,alt,cluster,cadd_phred,cadd_raw
```

| | |
|---|--:|
| rows | 23,080 |
| populated | **6,873 (31.3% of real substitutions)** |
| blank | 16,207 |
| PHRED range | 0.0 – 35.0 |
| median | **24.8** |

A median of 24.8 means the typical possible JAK1 missense substitution sits in roughly the **top
0.33%** of all human SNVs by CADD — unsurprising for a set dominated by changes never seen in a
living person, and a reminder that CADD's percentile is genome-wide, so almost any coding variant
scores high. For ranking *within* a gene the absolute value says little; the ordering is what counts.

## 7. What this means for the paper's feature list

CADD was one of two sequence-based scores the paper names and the only one this project had not
obtained. With this file, the gap is closed at the paper's own coverage level:

| feature | paper | here |
|---|--:|--:|
| **CADD** | not stated | **31.3%** |
| SIFT | 56.3% | 31.3% |
| PolyPhen-2 | 56.3% | **100%** |
| ClinPred | 14.25% | 31.3% |
| AlphaMissense | 29.7% | **100%** |
| ESM-1b | 100% | 100% |
| BLOSUM62 | 56.3% | **100%** |

Still missing: MutFunc (92.07% missing in the paper itself) and the three ddG features, which exist
for only 500 variants.
