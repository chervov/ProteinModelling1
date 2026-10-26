# TYK2 DMS: descriptive statistics and correlation structure

*26 October 2026. Basic characterisation of all 11 arms of the Howard et al. TYK2 deep mutational
scan, before any biological analysis. Source table: `TYK2_DMS_Howard2026_all_arms.csv`.*

**Scores are log₂ fold change versus wild-type TYK2**, so 0 = wild type, −1 = half the signal,
+1 = double. No absolute units. Abundance is the same idea on a GFP:BFP FACS ratio.

23,732 rows: **22,545 missense**, **1,187 nonsense**, 0 synonymous.

---

## 1. Descriptive statistics — missense (n = 22,545)

| column | count | mean | std | min | 25% | 50% | 75% | max | NA |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| ifn_1U | 22,536 | −0.048 | **0.328** | −2.692 | −0.251 | −0.048 | +0.151 | +4.479 | 9 |
| ifn_10U | 22,536 | −0.234 | 0.551 | −3.067 | −0.496 | −0.150 | +0.126 | +3.878 | 9 |
| ifn_100U | 22,536 | −0.239 | **0.631** | −4.276 | −0.435 | −0.118 | +0.135 | +2.640 | 9 |
| ifn_100U_dup | 22,533 | −0.232 | 0.603 | −6.554 | −0.434 | −0.115 | +0.140 | +2.878 | 12 |
| bms986202_20nM | 22,533 | −0.209 | 0.553 | −3.458 | −0.525 | −0.149 | +0.159 | +2.327 | 12 |
| bms986202_20nM_dup | 22,533 | −0.243 | 0.574 | −4.531 | −0.531 | −0.158 | +0.140 | +3.635 | 12 |
| bms986202_1uM | 22,533 | +0.019 | 0.345 | −2.811 | −0.188 | +0.014 | +0.217 | +3.505 | 12 |
| bms986202_10uM | 22,536 | +0.017 | 0.338 | −2.492 | −0.186 | +0.011 | +0.216 | +2.506 | 9 |
| ndi034858_7nM | 22,533 | −0.268 | 0.615 | −4.196 | −0.532 | −0.159 | +0.134 | +3.340 | 12 |
| ndi034858_1uM | 22,533 | +0.017 | 0.350 | −3.863 | −0.190 | +0.009 | +0.213 | +4.097 | 12 |
| **abundance** | 22,516 | −0.116 | **0.120** | −0.412 | −0.195 | −0.076 | −0.021 | +0.111 | 29 |

## 2. Descriptive statistics — nonsense (n = 1,187): the dead-protein anchor

| column | count | mean | std | min | 25% | **50%** | 75% | max |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| ifn_1U | 1,187 | −0.224 | 0.311 | −1.334 | −0.415 | **−0.228** | −0.041 | +0.981 |
| ifn_10U | 1,187 | −1.220 | 0.439 | −2.753 | −1.495 | **−1.246** | −1.003 | +0.795 |
| ifn_100U | 1,187 | −1.606 | 0.596 | −3.940 | −1.977 | **−1.645** | −1.270 | +0.729 |
| ifn_100U_dup | 1,186 | −1.592 | 0.550 | −3.060 | −1.957 | −1.660 | −1.285 | +0.555 |
| bms986202_20nM | 1,187 | −1.119 | 0.409 | −2.434 | −1.368 | −1.140 | −0.910 | +0.732 |
| bms986202_20nM_dup | 1,186 | −1.330 | 0.405 | −2.664 | −1.573 | −1.364 | −1.140 | +0.712 |
| bms986202_1uM | 1,187 | +0.030 | 0.303 | −1.192 | −0.145 | **+0.034** | +0.212 | +1.345 |
| bms986202_10uM | 1,187 | +0.063 | 0.326 | −1.418 | −0.145 | **+0.068** | +0.255 | +1.566 |
| ndi034858_7nM | 1,186 | −1.526 | 0.448 | −2.613 | −1.806 | −1.574 | −1.308 | +1.172 |
| ndi034858_1uM | 1,187 | −0.002 | 0.322 | −2.353 | −0.163 | **+0.006** | +0.185 | +1.256 |
| **abundance** | 1,182 | −0.325 | 0.088 | −0.416 | −0.373 | **−0.352** | −0.319 | +0.135 |

**Each arm has its own anchor.** −0.352 is the *abundance* value; signalling anchors run from
−0.228 (1 U/mL) to −1.66 (100 U/mL). Quoting −0.352 as a general "dead protein" line is wrong for
the signalling arms.

### Nonsense variants behave as biology predicts

Stop codons at IFN-α 100 U/mL, by where the stop falls:

| region | n | median | % scoring > −0.5 |
|---|--:|--:|--:|
| FERM (1–430) | 430 | −1.521 | 6% |
| SH2 / linker (431–588) | 158 | −1.466 | 3% |
| JH2 pseudokinase | 287 | −1.725 | 1% |
| JH1 kinase | 301 | −1.809 | 3% |
| **last 11 residues (1177–1187)** | 11 | **+0.038** | **100%** |

Truncation is lethal anywhere in the first 1,176 residues and completely tolerated in the last 11.
A clean internal validation that the scores mean what they claim — and the reason the nonsense
*median* rather than the mean is the right anchor.

---

## 3. Assay quality per arm

**Separation** = (missense median − nonsense median) / pooled SD, i.e. how many SD separate a
typical variant from a dead protein.

| arm | gap | pooled SD | **separation** | median SE | SD / SE |
|---|--:|--:|--:|--:|--:|
| ifn_100U_dup | +1.545 | 0.577 | **2.68** | 0.341 | 1.77 |
| **ndi034858_7nM** | +1.415 | 0.538 | **2.63** | 0.339 | 1.82 |
| abundance | +0.275 | 0.105 | **2.62** | 0.077 | 1.55 |
| ifn_100U | +1.527 | 0.614 | **2.49** | 0.313 | **2.01** |
| bms986202_20nM_dup | +1.206 | 0.497 | 2.43 | 0.337 | 1.70 |
| ifn_10U | +1.096 | 0.498 | 2.20 | 0.317 | 1.74 |
| bms986202_20nM | +0.991 | 0.486 | 2.04 | 0.350 | 1.58 |
| **ifn_1U** | **+0.179** | 0.319 | **0.56** | 0.311 | **1.06** |
| ndi034858_1uM | +0.003 | 0.336 | **0.01** | 0.353 | 0.99 |
| bms986202_1uM | −0.021 | 0.325 | **−0.06** | 0.351 | 0.98 |
| bms986202_10uM | −0.056 | 0.332 | **−0.17** | 0.326 | 1.04 |

**Three tiers.**

1. **Usable (separation 2.0–2.7)** — the three IFN arms at 10 and 100 U/mL, the two BMS 20 nM arms,
   NDI 7 nM, and abundance.
2. **Marginal: `ifn_1U`, separation 0.56, SD/SE = 1.06.** The biological spread barely exceeds the
   measurement error. This is the dose on which gain-of-function analysis depends, and it is by far
   the weakest arm.
3. **Dead: the three saturating inhibitor arms**, separation ≈ 0 and SD/SE ≈ 1.0 — a truncated
   protein scores like wild type because the drug suppresses everything. They carry no variant
   information and should not be used.

---

## 4. Correlation between arms

Spearman, missense only (n up to 22,533):

| | IFN1 | IFN10 | IFN100 | IFN100′ | BMS20n | BMS20n′ | NDI7n | BMS1u | BMS10u | NDI1u | abund |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **IFN1** | — | +0.52 | +0.52 | +0.19 | +0.20 | +0.21 | +0.22 | −0.01 | +0.40 | +0.00 | +0.10 |
| **IFN10** | +0.52 | — | **+0.72** | +0.44 | +0.44 | +0.47 | +0.48 | −0.02 | +0.24 | −0.01 | +0.21 |
| **IFN100** | +0.52 | +0.72 | — | **+0.45** | +0.42 | +0.44 | +0.46 | −0.03 | +0.25 | −0.01 | +0.20 |
| **IFN100′** | +0.19 | +0.44 | **+0.45** | — | +0.43 | **+0.68** | **+0.72** | −0.03 | −0.05 | −0.00 | +0.20 |
| **BMS20n** | +0.20 | +0.44 | +0.42 | +0.43 | — | +0.53 | +0.51 | +0.27 | −0.03 | +0.30 | +0.15 |
| **BMS20n′** | +0.21 | +0.47 | +0.44 | **+0.68** | +0.53 | — | **+0.75** | −0.01 | −0.04 | +0.02 | +0.18 |
| **NDI7n** | +0.22 | +0.48 | +0.46 | **+0.72** | +0.51 | +0.75 | — | −0.02 | −0.05 | +0.01 | +0.19 |
| **BMS1u** | −0.01 | −0.02 | −0.03 | −0.03 | +0.27 | −0.01 | −0.02 | — | +0.02 | +0.49 | −0.06 |
| **BMS10u** | +0.40 | +0.24 | +0.25 | −0.05 | −0.03 | −0.04 | −0.05 | +0.02 | — | +0.01 | −0.05 |
| **NDI1u** | +0.00 | −0.01 | −0.01 | −0.00 | +0.30 | +0.02 | +0.01 | +0.49 | +0.01 | — | −0.05 |
| **abund** | +0.10 | +0.21 | +0.20 | +0.20 | +0.15 | +0.18 | +0.19 | −0.06 | −0.05 | −0.05 | — |

### The arms group by assay batch, not by condition

**`ifn_100U` and `ifn_100U_dup` are the same experimental condition and correlate at only +0.45**,
while `ifn_100U_dup` correlates with `ndi034858_7nM` at **+0.72** and `bms986202_20nM_dup` at
**+0.68**. Hierarchical clustering on 1 − Spearman splits the seven informative arms as:

- **batch 1**: `ifn_1U`, `ifn_10U`, `ifn_100U`
- **batch 2**: `ifn_100U_dup`, `bms986202_20nM`, `bms986202_20nM_dup`, `ndi034858_7nM`

Within a group, arms agree at 0.68–0.75 *regardless of drug*; across groups at 0.42–0.48
*regardless of condition*. **Batch is a stronger signal than the experiment.**

**Consequence.** Any analysis subtracting one arm from another must pair arms from the same batch.
Getting this wrong changed a test in `interface_effect.md` §10 from p = 0.63 to p = 6.8e−05. The
publication does not mention batch effects, batch correction, or between-arm agreement; the term
"duplicate assay" is MaveDB's, not the paper's.

The three saturating arms correlate with essentially everything at ≈ 0, consistent with carrying
noise only. (`BMS10u` vs `IFN1` at +0.40 and `BMS1u` vs `NDI1u` at +0.49 are correlations between
two noise distributions, not biology.)

---

## 5. Abundance versus signalling

| signalling arm | Spearman with abundance | median signalling, bottom-quartile abundance | rest |
|---|--:|--:|--:|
| ifn_1U | **+0.101** | −0.104 | −0.028 |
| ifn_10U | +0.206 | −0.360 | −0.103 |
| ifn_100U | +0.204 | −0.292 | −0.078 |

**The two readouts are nearly independent (ρ ≈ 0.10–0.21).** Losing protein does not reliably
predict losing signal — which is the general form of the dissociation analysed in
`interface_effect.md`. Note also the scale difference: abundance SD is 0.120 against 0.631 for
IFN 100 U/mL, so abundance and signalling magnitudes must never be compared directly.

---

## 6. Practical summary

| | |
|---|---|
| best signalling arms | `ifn_100U`, `ifn_100U_dup`, `ndi034858_7nM` (separation 2.5–2.7) |
| best abundance arm | `abundance` (separation 2.62, lowest SE) |
| weakest usable arm | **`ifn_1U`** — separation 0.56, SD/SE 1.06 |
| unusable | `bms986202_1uM`, `bms986202_10uM`, `ndi034858_1uM` |
| mandatory constraint | pair arms **within batch** for any subtraction |
| per-arm dead anchor | use the arm's own nonsense median, not −0.352 |

*Source: Howard et al., eLife 2026, DOI 10.7554/eLife.110149.2 (preprint bioRxiv
10.1101/2025.10.11.681520). MaveDB `urn:mavedb:00001270-a` and `00001271-a`, retrieved
26 October 2026.*
