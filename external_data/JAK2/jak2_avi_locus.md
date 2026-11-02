# JAK2 whole locus — AVI for all 440,031 possible SNVs

Every possible single-nucleotide variant across the JAK2 locus, scored with the **AlphaGenome Atlas**
AVI and annotated by region class. Retrieved 2 November 2026. Companion to
[`jak2_avi_coding.md`](jak2_avi_coding.md), which covers the coding sequence and the protein-level
mapping.

**The pull took 77 seconds** — 440,031 variants at ~5,700/s, in fifteen 10 kb `query_interval` calls.
The Atlas is precomputed, so the whole locus costs less than two minutes.

Region: `chr9:4,983,272–5,129,948` — canonical transcript **ENST00000381652** (25 exons, + strand)
plus 2 kb upstream for the promoter.

## Files

| file | size | contents |
|---|--:|---|
| [`jak2_locus_avi.csv.gz`](jak2_locus_avi.csv.gz) | 6.8 MB | all 440,031 SNVs: variant, position, ref, alt, region class, raw AVI |
| [`jak2_locus_noncoding_high_avi.csv`](jak2_locus_noncoding_high_avi.csv) | 20 KB | the 324 non-coding SNVs scoring above 1.5 |
| [`jak2_locus_avi.py`](jak2_locus_avi.py) | | reproduces all of it |

## 1. The model's non-coding signal is almost entirely splicing

| region class | n | mean AVI | median | p99 | max |
|---|--:|--:|--:|--:|--:|
| **splice_donor** (first 2 intronic nt) | 144 | **1.716** | 1.756 | 2.040 | 2.130 |
| **splice_acceptor** (last 2 intronic nt) | 144 | **1.672** | 1.678 | 2.064 | 2.079 |
| CDS_splice_region | 396 | 1.115 | 1.036 | 2.951 | 3.228 |
| CDS | 9,801 | 0.862 | 0.773 | 2.388 | 3.457 |
| 5′UTR_splice_region | 45 | 0.508 | 0.420 | 1.533 | 1.545 |
| splice_region (3–8 intronic nt) | 864 | 0.481 | 0.303 | 1.912 | 2.047 |
| 5′UTR | 1,356 | 0.248 | 0.212 | 0.882 | 1.487 |
| 3′UTR_splice_region | 9 | 0.149 | 0.156 | 0.202 | 0.203 |
| 3′UTR | 9,462 | 0.113 | 0.089 | 0.465 | 1.256 |
| upstream (2 kb promoter) | 6,000 | 0.098 | 0.057 | 0.731 | 1.335 |
| **intron** | **411,810** | **0.040** | 0.017 | 0.431 | 1.641 |

The two canonical splice dinucleotide classes score **~43× the intronic background** and **twice the
CDS mean**. Everything about the ordering is what it should be if the model is detecting splicing
rather than generic conservation: the donor/acceptor GT–AG at the top, the 3–8 nt splice region well
below them but still 12× background, and the deep intron at the floor.

This is a useful internal validation, because nothing in the pipeline told the model where the exons
are. The 288 splice-dinucleotide variants were identified purely by Ensembl exon coordinates after
the fact, and they are exactly the positions the Atlas scores highest.

**The promoter and 3′UTR are quiet.** 2 kb upstream averages 0.098 and the 3′UTR 0.113, barely above
intronic. For JAK2 the regulatory signal is not where variant-interpretation guidelines usually look;
it is at the splice junctions.

## 2. 430,000 non-coding possibilities reduce to 324 candidates

Of the 429,834 non-coding SNVs, only **324 (0.08%)** score above 1.5, and they are overwhelmingly the
splice sites:

| region | count above 1.5 |
|---|--:|
| splice_donor | 125 |
| splice_acceptor | 122 |
| splice_region | 71 |
| **intron** | **4** |
| 5′UTR_splice_region | 2 |

That is the practical value of the Atlas here: a locus-wide screen that leaves a shortlist short
enough to look at individually, without having to decide in advance where to look.

Top of the list:

| variant | region | AVI |
|---|---|--:|
| chr9:5073787:T>G | splice_donor | 2.130 |
| chr9:5123003:G>C | splice_acceptor | 2.079 |
| chr9:5123003:G>A | splice_acceptor | 2.065 |
| chr9:5029782:G>C | splice_acceptor | 2.062 |
| chr9:5073790:G>A | splice_region | 2.047 |
| chr9:5123122:G>C | splice_donor | 2.043 |

`chr9:5073787` is the donor of **exon 14** — the V617F exon. Its skipping would remove the stretch of
JH2 that carries V617.

## 3. The four deep-intronic hits are a polypyrimidine-tract signature

Three of the four intronic variants above 1.5 are the **same change at the same offset**:

| variant | AVI | position |
|---|--:|---|
| chr9:5077442:**T>G** | 1.641 | **11 nt** upstream of exon start 5,077,453 |
| chr9:5080218:**T>G** | 1.623 | **11 nt** upstream of exon start 5,080,229 |
| chr9:5122993:**T>G** | 1.532 | **11 nt** upstream of exon start 5,123,004 |
| chr9:5083127:T>G | 1.517 | 1,266 nt into an intron |

T→G eleven bases before an exon destroys a pyrimidine in the **polypyrimidine tract**, weakening the
3′ splice site without touching the AG dinucleotide — a known pathogenic mechanism that a
dinucleotide-only filter misses entirely.

The profile across the tract confirms it is a real gradient, not three coincidences:

| nt upstream of exon start | n | mean AVI | max |
|---|--:|--:|--:|
| 9 | 72 | 0.382 | 1.479 |
| 10 | 72 | 0.326 | 1.472 |
| **11** | 72 | **0.386** | **1.641** |
| 12 | 72 | 0.194 | 0.675 |
| 15 | 72 | 0.210 | 1.443 |
| 20 | 72 | 0.176 | 1.161 |
| 25 | 72 | 0.144 | 0.965 |
| **beyond 25** | 411,000+ | **0.039** | 1.641 |

A decay from ~0.39 at the tract down to the 0.039 background — **a 10× elevation** over the region
where U2AF binds, falling away smoothly with distance.

**`chr9:5083127:T>G` is the one genuine oddity**: 1,266 nt deep in an intron, no splice site nearby,
and the only variant of its kind in the whole locus. A cryptic splice site or branch point is the
obvious hypothesis; nothing here tests it.

## Caveats

1. **Raw AVI only.** The API returns raw scores, not the Phred/percentile scale used in
   `variant_panel_24`. The 1.5 threshold in §2 is chosen for convenience, not calibrated — it is
   roughly where the CDS p99 sits.
2. **Region classes are from one transcript.** ENST00000381652 only. A variant intronic here may be
   exonic in another isoform, and JAK2 has several.
3. **The two 5′UTR hits** (`chr9:4986022:G>C/T`, AVI 1.55 and 1.52) are classified as
   5′UTR_splice_region because they fall within 3 nt of a 5′UTR exon edge. The distance figure
   printed by `needles.py` for them is misleading — that script measures to non-containing exons
   only, so it reports the previous exon 392 nt away rather than the edge they actually sit on.
4. **Non-commercial use only** per the AlphaGenome terms, and not validated for clinical use.
5. **Nothing here is experimentally verified.** These are predictions that identify which ~324 of
   430,000 possibilities would be worth an RT-PCR or minigene assay.
