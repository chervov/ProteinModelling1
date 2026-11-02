# JAK2 coding region — AlphaGenome Atlas AVI for every possible SNV

Every single-nucleotide variant in the JAK2 coding sequence, scored with the **AlphaGenome Atlas**
AVI (AlphaGenome Variant Impact) and mapped to protein level. Retrieved 2 November 2026.

**The whole pull took 8.2 seconds.** The Atlas is a lookup of precomputed scores, not a model run —
all ~9 billion human SNVs were precomputed and released on 8 September 2026 — so cost was never the
constraint it looked like.

## Files

| file | rows | contents |
|---|--:|---|
| [`jak2_cds_avi_snv.csv`](jak2_cds_avi_snv.csv) | 10,197 | one row per CDS SNV: genomic variant, codon change, consequence, raw AVI |
| [`jak2_cds_avi_protein.csv`](jak2_cds_avi_protein.csv) | 6,697 | one row per amino-acid substitution, AVI aggregated over the codon changes that produce it (`avi_max`, `avi_mean`, `n_snv`) |
| [`jak2_synonymous_high_avi.csv`](jak2_synonymous_high_avi.csv) | 17 | the synonymous variants scoring above the mean missense — see §4 |
| [`jak2_cds_avi.py`](jak2_cds_avi.py) | | reproduces all of it |

## Method

Canonical transcript **ENST00000381652** (chr9, + strand, 1,132 aa, CDS 5,021,988–5,126,791,
23 coding exons, 3,399 nt including the stop codon). One `query_interval` call per coding exon
returns the dense precomputed scores for all three alternates at every position; consequences come
from local codon translation against the Ensembl CDS sequence, not from an annotation service.

**Every reference base matched** the Ensembl CDS (0 mismatches in 10,197), and all 1,132 codons are
covered.

```python
from alphagenome.atlas import atlas          # NOT dna_client - a separate endpoint
client = atlas.create(api_key)
client.query_interval(interval=iv, requested_scorers=["AVI_SCORE"])
```

Measured throughput: **~1,195 variants/s**. `query_interval` needs no reference bases, which is why
it is preferred over `query_variants` here.

| consequence | n | mean AVI | max |
|---|--:|--:|--:|
| missense | 7,581 | 0.950 | 2.995 |
| synonymous | 2,100 | 0.272 | 1.767 |
| nonsense | 508 | **2.181** | 3.457 |
| stop_lost | 8 | | |

AVI ranks stop-gains far above missense, which is the expected ordering and a reassuring internal
check.

## 1. Coverage: 31% of the protein, and that is a hard ceiling

6,697 distinct substitutions out of the **19 × 1,132 = 21,508** possible, i.e. **31.1%**. The other
~14,800 need two or three nucleotide changes in one codon and therefore have no SNV to look up. No
SNV-indexed resource — Atlas, dbNSFP, gnomAD — can go past this; only predictors that work directly
in protein space (AlphaMissense, ESM1b) cover all 21,508.

## 2. For missense, AVI largely restates AlphaMissense

Joined against [`jak2_variants_inf_predict.csv`](jak2_variants_inf_predict.csv), 2,541 shared
variants:

| AVI vs | Spearman |
|---|--:|
| **AlphaMissense** | **+0.879** |
| MetaRNN | +0.796 |
| CADD phred | +0.745 |
| REVEL | +0.731 |
| ESM1b | −0.683 *(ESM1b is inverted by convention)* |

ρ = 0.88 against AlphaMissense is expected: AVI is a composite that **includes** AlphaMissense as one
of its input features. On the ClinVar variants in this gene it is not an improvement either —
**AUC 0.881 for AVI against 0.893 for AlphaMissense alone** (6 pathogenic, 14 benign, so treat both
as indicative only).

**Consequence for the tables: do not count AVI and AlphaMissense as two independent votes.** They are
correlated by construction, and a "N of 21 predictors agree" tally that includes both is inflated.
This confirms, on 2,541 variants rather than 24, what
[`../../JAK2/variant_panel_24/README.md`](../../JAK2/variant_panel_24/README.md) found: *"AVI adds
little beyond AlphaMissense plus conservation."*

## 3. The known drivers sit in the middle of JAK2's own distribution

Percentile within all 6,697 JAK2 substitutions (100 = most impactful):

| variant | AVI | percentile |
|---|--:|--:|
| V625F | 2.515 | **99.9** |
| T875N | 1.491 | 88.5 |
| L611S | 1.192 | 68.0 |
| I1065T | 1.010 | 58.0 |
| **V617F** | **0.981** | **56.4** |
| R867Q | 0.947 | 54.0 |
| H608N | 0.908 | 50.9 |
| G571R | 0.888 | 49.5 |
| V578I | 0.863 | 47.6 |
| L805I | 0.810 | 42.7 |
| V617I | 0.809 | 42.7 |
| V1110E | 0.770 | 38.5 |
| Y317H | 0.761 | 37.3 |
| T108A | 0.296 | 3.2 |

**V617F — the canonical MPN driver — is at the 56th percentile.** Median. This is the same result the
ΔΔG work produced independently: V617F sits at the **37th percentile** of JAK2's ThermoMPNN
distribution, below the gene's median.

Two damage predictors built on unrelated principles both place the best-characterised activating
mutation in human haematology in the middle of the pack. That is not a failure of either tool — it is
the signature of **gain of function through release of JH2 autoinhibition**, a mechanism that neither
destabilises the fold nor looks like loss of a conserved function. **Neither AVI nor ΔΔG should be
used to rank JAK2 variants for activation.** Only V625F stands out, at the 99.9th percentile.

## 4. What AVI adds that nothing else here can: splice-disrupting synonymous variants

The existing panel of ~21 predictors scores **missense only**. AVI scores every SNV, and the
synonymous results are not flat:

| distance to nearest exon boundary | n | mean AVI | max |
|---|--:|--:|--:|
| **0–2 nt** | 78 | **0.491** | 1.767 |
| 3–5 nt | 85 | 0.237 | 1.167 |
| 6–10 nt | 127 | 0.257 | 0.751 |
| 11–25 nt | 422 | 0.254 | 0.804 |
| 26–50 nt | 724 | 0.265 | 1.160 |
| > 50 nt | 664 | 0.272 | 1.695 |

Synonymous variants **at the exon edge score roughly double** the flat background, which is constant
from 3 nt inward. Nine of the top fifteen are at **distance 0** — the last base of an exon, part of
the 5′ splice donor consensus. The mechanism is splicing, and the pattern is exactly what it should
be if AVI is detecting it rather than noise.

**17 synonymous variants score above the mean missense (0.95); 10 are within 5 nt of a boundary.**
The leaders:

| variant | codon | AVI | distance to edge |
|---|---|--:|--:|
| chr9:5054884:G>A | Q312 CAG>CAA | 1.767 | **0** |
| chr9:5090570:G>A | K962 AAG>AAA | 1.716 | **0** |
| chr9:5078383:A>T | G690 GGA>GGT | 1.695 | 61 |
| chr9:5066789:G>A | E442 GAG>GAA | 1.653 | **0** |
| chr9:5126446:G>A | E1097 GAG>GAA | 1.487 | **0** |
| chr9:5123121:G>T | A1059 GCG>GCT | 1.437 | **0** |

The seven that are *not* near a boundary (G690 at 61 nt, R426 at 50 nt) would be exonic splicing
enhancer or branch-point candidates — a weaker claim, and untested here.

**This is the case for using the Atlas on the JAK family.** Not the missense column, which is
AlphaMissense in different units, but the variants the project excluded by construction: synonymous,
intronic, UTR and splice-region. The same pull over the full 145.6 kb locus is 436,683 SNVs and
about **six minutes**.

## 5. Genome-wide Phred, added by calibration

The API returns the raw AVI only — `scorer_metadata()` offers `AVI_SCORE`,
`AVI_SCORE_FEATURE_IMPORTANCE` and `AVI_SCORE_MODEL_FEATURES`, and no phred, quantile or
percentile scorer exists. The Phred scale (−10·log₁₀ of the genome-wide tail quantile) used in
`variant_panel_24` therefore has to be reconstructed.

Two sets of paired (raw, Phred) observations exist in this repository, giving **35 knots** spanning
raw **0.296–2.632** and Phred **14.34–46.82**:

| source | n |
|---|--:|
| [`../../JAK2/variant_panel_24/alphagenome_avi_raw_output.md`](../../JAK2/variant_panel_24/alphagenome_avi_raw_output.md) (both columns present) | 24 |
| [`../../JAK2/variant_panel_24/JAK2_benign_AVI_background.csv`](../../JAK2/variant_panel_24/JAK2_benign_AVI_background.csv) (Phred given; raw fetched from the Atlas) | 12 |

The mapping is **monotone cubic (PCHIP) interpolation** over those knots, published as
[`../jak_avi_phred_calibration.json`](../jak_avi_phred_calibration.json) with every knot listed.
Zero non-monotone knots, as Phred must be monotone in raw by construction.

**Accuracy, by leave-one-out** (each knot predicted from the other 34 — agreement *at* the knots is
guaranteed and proves nothing):

| | Phred |
|---|--:|
| median absolute error | **0.004** |
| mean | 0.038 |
| 90th percentile | 0.061 |
| worst case | 0.623 |

**Why fit shapes were rejected.** A linear fit gives max residual 2.41 Phred, a quadratic 2.07, and
linear-in-log(raw) 8.80. An earlier quadratic fitted on the 12 benign points alone appeared
excellent (residual 0.07) but only because those points span a narrow range where the curve is
locally straight; extended, it curves, and a quadratic on that subset turns over and would
*decrease* Phred for high scores.

**Applied only where it covers the data.** The calibration starts at raw 0.296, while intronic AVI
averages ~0.04:

| dataset | rows in calibrated range |
|---|--:|
| `jak2_cds_avi_protein.csv` | **96.7%** |
| `jak2_cds_avi_snv.csv` | **83.6%** |
| whole-locus files (all four genes) | 5–12% |

So `avi_phred` and `avi_top_pct` columns are added to the two coding files and **not** to the
locus files, where a 90%-blank column would be worse than none. Anyone needing Phred there can
apply the published calibration. Values outside the knot range are left blank rather than
extrapolated.

## Caveats

1. **Phred is reconstructed, not served.** See §5 — median leave-one-out error 0.004 Phred, but it
   is an interpolation of 35 observations, not the server's own number. Percentiles in §3 remain
   **within JAK2**; `avi_top_pct` in the CSVs is genome-wide. Validation of the raw score itself:
   `chr9:5073770:G>T` is 0.98103 here and 0.981 in
   [`../../JAK2/variant_panel_24/alphagenome_avi_raw_output.md`](../../JAK2/variant_panel_24/alphagenome_avi_raw_output.md).
2. **AVI is a damage detector.** It does not model gain of function — see §3.
3. **Aggregation choice.** `avi_max` is used for the protein-level scores where several codon changes
   give the same substitution; `avi_mean` and the count are in the file so either can be used.
4. **Non-commercial use only**, per the AlphaGenome terms, and not validated for clinical use.
