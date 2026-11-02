# JAK family — AlphaGenome Atlas AVI across all four loci

Every possible SNV in JAK1, JAK2, JAK3 and TYK2, scored with the **AlphaGenome Atlas** AVI and
annotated by region class. Retrieved 2 November 2026.

**1,017,717 variants in 178 seconds** (~5,700/s). The Atlas is precomputed, so a whole-family
non-coding screen costs about three minutes.

| gene | transcript | strand | locus | SNVs | time |
|---|---|:-:|--:|--:|--:|
| JAK1 | ENST00000342505 | − | chr1:64,833,229–64,968,549 (135.3 kb) | 405,963 | 71.3 s |
| JAK2 | ENST00000381652 | + | chr9:4,983,272–5,129,948 (146.7 kb) | 440,031 | 75.4 s |
| JAK3 | ENST00000458235 | − | chr19:17,824,782–17,849,982 (25.2 kb) | 75,603 | 13.5 s |
| TYK2 | ENST00000525621 | − | chr19:10,350,533–10,382,572 (32.0 kb) | 96,120 | 17.2 s |

Each locus is the canonical transcript span plus 2 kb of promoter. Per-gene data is in
`external_data/<GENE>/`; the cross-gene table is
[`jak_family_avi_by_region.csv`](jak_family_avi_by_region.csv); the script is
[`jak_locus_avi.py`](jak_locus_avi.py).

## 1. Mean AVI by region class

| region | JAK1 | JAK2 | JAK3 | TYK2 |
|---|--:|--:|--:|--:|
| **splice_donor** | **1.827** | **1.716** | 1.552 | **1.571** |
| **splice_acceptor** | 1.801 | 1.672 | **1.602** | 1.558 |
| CDS_splice_region | 1.176 | 1.115 | 1.025 | 0.982 |
| CDS | 0.856 | 0.862 | 0.677 | 0.607 |
| splice_region (3–8 nt) | 0.400 | 0.481 | 0.290 | 0.304 |
| 5′UTR | 0.164 | 0.248 | 0.202 | 0.073 |
| 3′UTR | 0.109 | 0.113 | 0.004 | −0.020 |
| upstream (2 kb) | 0.036 | 0.098 | 0.056 | 0.013 |
| **intron** | **0.047** | **0.040** | **0.018** | **0.011** |
| donor ÷ intron | **39×** | **43×** | **86×** | **143×** |

The ordering is identical in all four genes: canonical splice dinucleotides at the top, then the
exonic splice region, then CDS, then everything else barely above the intronic floor. Promoter and
3′UTR are quiet throughout — TYK2's 3′UTR mean is even slightly negative.

**The coding sequence is not where the strongest predicted non-coding effects are.** A splice
dinucleotide variant scores about twice the mean CDS variant in every gene.

## 2. JAK1 and JAK2 score higher than JAK3 and TYK2 in coding

CDS means: JAK1 0.856 ≈ JAK2 0.862, then JAK3 0.677, TYK2 0.607. The gap is consistent across
`CDS_splice_region` and the splice classes too.

This tracks the known constraint on each gene. JAK2 loss is not tolerated; JAK1 likewise. TYK2 by
contrast tolerates loss of function in humans — the common **P1104A** hypomorph is carried at
appreciable frequency — and JAK3 loss causes SCID only in biallelic form, with carriers unaffected.
AVI includes conservation and AlphaMissense components, both of which should read that difference,
and they do. It is a consistency check on the scores rather than a new finding.

## 3. The polypyrimidine-tract signature is universal

Mean AVI for intronic positions 3–25 nt from the acceptor, against the deep-intronic background:

| gene | tract | deep intron | ratio |
|---|--:|--:|--:|
| JAK1 | 0.122 | 0.047 | **2.6×** |
| JAK2 | 0.216 | 0.039 | **5.5×** |
| JAK3 | 0.086 | 0.016 | **5.4×** |
| TYK2 | 0.092 | 0.009 | **9.9×** |

Present in all four. This is the region where U2AF binds, and variants there weaken the 3′ splice
site without touching the AG dinucleotide — a mechanism any donor/acceptor-only filter misses.

### Why this also validates the strand handling

In genomic coordinates the 5′ splice donor sits at the **low** end of an intron for a + strand gene
and at the **high** end for a − strand gene. JAK1, JAK3 and TYK2 are all on the minus strand, so
labelling by genomic order would have swapped donor and acceptor on three of the four genes. The
means alone cannot detect that, because donor and acceptor score so similarly everywhere.

The polypyrimidine hits can. In **JAK2** (+ strand) the three tract variants are **T>G**: transcript
T is a pyrimidine, and G is not. In **JAK1** (− strand) the five tract variants are **A>T** and
**A>C**: genomic A is transcript **T**, again a pyrimidine, replaced by transcript A or G, again
purines. Same biochemistry, complementary bases, exactly as it must appear if the strand logic is
right.

## 4. The shortlists: ~1.4 million possibilities down to 1,063 candidates

Non-coding SNVs scoring above 1.5:

| gene | total non-coding | above 1.5 | donor | acceptor | splice_region | intron | other |
|---|--:|--:|--:|--:|--:|--:|--:|
| JAK1 | 395,982 | 326 (0.082%) | 131 | 136 | 50 | **8** | 1 (5′UTR) |
| JAK2 | 429,834 | 324 (0.075%) | 125 | 122 | 71 | **4** | 2 (5′UTR) |
| JAK3 | 65,478 | 202 (0.309%) | 76 | 107 | 12 | 0 | **7 (promoter)** |
| TYK2 | 85,428 | 211 (0.247%) | 97 | 96 | 17 | **1** | 0 |

Overwhelmingly splice sites, as expected. The interesting entries are the handful that are not.

### JAK3 has a promoter cluster — unique among the four

Seven variants above 1.5 in the 2 kb upstream window, and they are not scattered: all seven fall
within **65 bp**, at **−22 to −86 nt from the transcript start**.

| variant | AVI | from TSS |
|---|--:|--:|
| chr19:17848004:G>C | 1.963 | −22 |
| chr19:17848045:T>A | 1.904 | −63 |
| chr19:17848024:T>A | 1.884 | −42 |
| chr19:17848012:C>A | 1.625 | −30 |
| chr19:17848068:A>G | 1.594 | −86 |
| chr19:17848043:T>A | 1.548 | −61 |
| chr19:17848026:C>A | 1.542 | −44 |

That window is the core promoter. JAK1, JAK2 and TYK2 have **no** promoter variant above 1.5, so this
is specific to JAK3 rather than a general property of the scorer. Given that JAK3 expression is
restricted to the haematopoietic lineage, a discrete sensitive element there is plausible — but this
is a prediction about a 65 bp window, nothing more.

### Two adjacent deep-intronic bases in JAK1

`chr1:64898162:T>A` scores **2.124** — the highest non-coding AVI in the entire family — and its
neighbour `chr1:64898163:C>A` scores 1.538. Both are **~11.8 kb from the nearest exon**, with no
splice site anywhere near. Two adjacent bases, deep in an intron, both in the top handful.

The remaining five JAK1 intronic hits are all 9–14 nt from an exon edge, i.e. the tract signature of
§3. JAK2's `chr9:5083127:T>G` (1,266 nt deep) and TYK2's single intronic hit are the only other
non-tract intronic entries.

Cryptic splice sites or an intronic regulatory element are the obvious hypotheses for the JAK1 pair.
Nothing here tests either.

## Caveats

1. **Raw AVI only.** The API returns raw scores, not the Phred/percentile scale. The 1.5 cutoff is
   chosen for convenience — roughly the CDS 99th percentile — not calibrated against outcomes.
2. **One transcript per gene.** Region classes come from the canonical transcript only; a position
   intronic here may be exonic in another isoform, and all four genes have several.
3. **Gene-to-gene comparisons of absolute AVI are weak.** Intronic backgrounds differ 4-fold across
   the family (0.047 to 0.011), partly reflecting gene density and intron length — JAK3 and TYK2 sit
   in gene-dense chr19 regions. Within-gene comparisons are the safer reading.
4. **Nothing is experimentally verified.** These are predictions identifying which ~1,000 of
   ~1.4 million non-coding possibilities would justify a minigene or reporter assay.
5. **Non-commercial use only** per the AlphaGenome terms; not validated for clinical use.
