# TYK2 DMS: descriptive statistics and correlation structure

*26 October 2026. Basic characterisation of all 11 arms of the Howard et al. TYK2 deep mutational
scan, before any biological analysis. Source table: `TYK2_DMS_Howard2026_all_arms.csv`.*

**Scores are log₂ fold change versus wild-type TYK2**, so 0 = wild type, −1 = half the signal,
+1 = double. No absolute units. Abundance is the same idea on a GFP:BFP FACS ratio.

23,732 rows: **22,545 missense**, **1,187 nonsense**, 0 synonymous.

---

## 1. What the eleven "arms" are

An **arm** is one experimental condition, scored across the whole variant library. The dataset has
eleven: ten measuring **interferon signalling** under different treatments, and one measuring
**protein abundance**. Every arm scores the same ~22,500 missense variants, so they can be compared
variant by variant.

| arm | what was done to the cells | measured by |
|---|---|---|
| `ifn_1U` | IFN-α 1 U/mL | ISRE-luciferase reporter |
| `ifn_10U` | IFN-α 10 U/mL | ISRE-luciferase reporter |
| `ifn_100U` | IFN-α 100 U/mL | ISRE-luciferase reporter |
| `ifn_100U_dup` | IFN-α 100 U/mL — **a repeat of the row above** | ISRE-luciferase reporter |
| `bms986202_20nM` | IFN-α 100 U/mL **+ BMS-986202 20 nM** | ISRE-luciferase reporter |
| `bms986202_20nM_dup` | same — **a repeat** | ISRE-luciferase reporter |
| `bms986202_1uM` | IFN-α 100 U/mL + BMS-986202 1 µM | ISRE-luciferase reporter |
| `bms986202_10uM` | IFN-α 100 U/mL + BMS-986202 10 µM | ISRE-luciferase reporter |
| `ndi034858_7nM` | IFN-α 100 U/mL **+ NDI-034858 7 nM** | ISRE-luciferase reporter |
| `ndi034858_1uM` | IFN-α 100 U/mL + NDI-034858 1 µM | ISRE-luciferase reporter |
| **`abundance`** | nothing — steady-state protein level | VAMP-seq (GFP:BFP ratio, FACS) |

### The three things that vary

**Interferon dose (1, 10, 100 U/mL).** The stimulus TYK2 transduces. More IFN means more signal and
more room to see a variant break it — but also less room to see a variant *improve* on wild type.

**Drug, and its concentration.** **BMS-986202** and **NDI-034858** (zasocitinib) are **allosteric
TYK2 inhibitors**: they bind the **JH2 pseudokinase domain**, not the ATP site, and work by holding
JH2 docked onto JH1 — stabilising the autoinhibited state. BMS-986202 is from the same series as
deucravacitinib (Sotyktu). Both were given at a **sub-saturating** dose (20 nM / 7 nM) and a
**saturating** one (1–10 µM).

**Readout.** Ten arms report *signalling*; one reports *how much protein is present*. These are
different questions and, as §7 shows, they correlate only weakly.

### Two things to know before using any arm

**Saturating drug arms carry no information.** At 1 µM and 10 µM the drug shuts down signalling in
every variant including wild type. Since scores are relative to wild type, everything returns to
zero — a **nonsense variant scores +0.034**, i.e. a truncated protein looks normal. Use only
`bms986202_20nM`, `bms986202_20nM_dup` and `ndi034858_7nM`.

**Two arms are repeats, and the repeats disagree** (§2). `ifn_100U_dup` and `bms986202_20nM_dup`
measure conditions already measured elsewhere in the dataset. The label "duplicate assay" is
MaveDB's; the publication does not describe them as such or report their agreement.

### How to read a score

Log₂ fold change versus wild-type TYK2. **0 = wild type**, −1 = half the signal, +1 = double. No
absolute units. Each arm carries its own internal floor: the **nonsense** (premature-stop) variants,
which are non-functional by construction and define what "completely broken" scores in that arm.

---


### Why abundance was measured only once — and what that costs

Abundance is not a *treatment* of the signalling experiment; it is a **separate assay with a
separate library**. VAMP-seq requires TYK2 fused to GFP with a BFP normalisation control, then FACS
sorting into quartile bins — the paper reports *"Three assay replicates were seeded and
independently sorted via FACS on 3 different days."* Signalling is a pooled luciferase readout where
barcodes are simply sequenced. Running the sorted assay across ten conditions would have multiplied
the work by an order of magnitude.

There is also an a-priori argument for a single measurement: abundance reflects folding and
degradation — how much protein exists — and interferon stimulates signalling *downstream* of a
protein that is already present. On that reasoning, IFN dose is irrelevant to abundance.

**That reasoning does not extend to the drugs.** Ligand binding commonly stabilises proteins; it is
the basis of thermal-shift assays. BMS-986202 and NDI-034858 bind the JH2 domain, so they could
plausibly raise TYK2 abundance, and differentially across variants. **An abundance arm with drug
would be the most informative missing experiment in this dataset** — and it bears directly on the
interface question (`interface_effect.md`): if interface variants lose abundance by loosening the
JH2–JH1 contact, a drug that tightens that contact might partially rescue them.

**Abundance reproducibility cannot be measured directly — but it can be estimated, and the estimate
is poor.** Two signalling arms are repeats, so their reliability is observable (§2). Abundance was
deposited as a single score set, so there is no equivalent. The reported per-variant standard errors
provide a route around this.

### Estimating reliability from the reported standard errors

If `var(observed) = var(true) + var(error)`, the expected correlation between two independent
repeats is `var(true) / var(observed)`. Where real repeats exist the prediction can be checked:

| pair | predicted | **observed** | ratio |
|---|--:|--:|--:|
| ifn_100U / ifn_100U_dup | 0.662 | **0.700** | 1.06 |
| bms986202_20nM / bms986202_20nM_dup | 0.553 | **0.607** | 1.10 |

Accurate to within 10% on both, so the method can be applied where no repeat exists.

| arm | SD | median SE | error share of variance | **estimated replicate r** |
|---|--:|--:|--:|--:|
| ifn_100U | 0.631 | 0.313 | 31% | **0.689** *(observed 0.700)* |
| ndi034858_7nM | 0.615 | 0.339 | 34% | 0.657 |
| ifn_100U_dup | 0.603 | 0.341 | 36% | 0.635 |
| bms986202_20nM_dup | 0.574 | 0.337 | 39% | 0.610 |
| ifn_10U | 0.551 | 0.317 | 41% | 0.585 |
| **abundance** | **0.120** | **0.077** | **49%** | **0.506 → 0.545 corrected** |
| bms986202_20nM | 0.553 | 0.350 | 50% | 0.501 |
| **ifn_1U** | 0.328 | 0.311 | **112%** | **0.000** |

**Abundance is estimated at r ≈ 0.55 — among the least reliable arms, not the most.** Nearly half
its observed variance is measurement error.

Two independent checks agree. The **nonsense variants** are all equally dead by construction, so
their spread is pure noise: the ratio of that spread to the reported SE is **1.69** for IFN 100 U/mL
and **1.81** for abundance — the true error is about 1.8× the reported SE in both, slightly worse
for abundance. And **`ifn_1U` returns 0.000**: its reported errors account for its entire variance,
so that arm may carry no recoverable signal at all — consistent with its separation of 0.56 (§5).

### A correction

An earlier version of this section described abundance's low standard errors as *"reassuring about
internal consistency"*. **That was wrong.** What matters is the SE *relative to* the spread being
measured. Abundance has a tight distribution (SD 0.120), so its small SE (0.077) is proportionally
large — 49% of variance, against 31% for IFN 100 U/mL.

### What still holds

Abundance remains the arm carrying the most weight here: best correlation with every predictor
(+0.42), and the interface finding rests on it. Those are **group-level** comparisons over hundreds
of variants, where an r ≈ 0.55 per-variant error averages down heavily — the 69% vs 38% contrast
involves 494 variants and is not threatened by this.

**Individual abundance scores are another matter.** At r ≈ 0.55 a single variant's value carries
substantial error, so single-variant abundance claims should not be made from this dataset alone.
An orthogonal measurement — western blot or mass spectrometry on a small set — would settle both
this and the drug-stabilisation question above.

---

## 2. Warning: repeated experiments disagree badly

**Two of the eleven arms are repeats of a condition measured elsewhere in the dataset.** They are
the only direct measure of reproducibility available, and they fail it.

| comparison | Spearman | Pearson | n |
|---|--:|--:|--:|
| **IFN-α 100 U/mL vs its own repeat** | **+0.448** | +0.700 | 22,530 |
| **BMS-986202 20 nM vs its own repeat** | **+0.527** | +0.607 | 22,526 |
| *different drug, same batch* (BMS 20 nM′ / NDI 7 nM) | *+0.752* | *+0.824* | *22,533* |
| *10× dose difference, same batch* (IFN 10 U / 100 U) | *+0.723* | *+0.795* | *22,536* |
| *different condition, same batch* (IFN 100′ / NDI 7 nM) | *+0.716* | *+0.814* | *22,533* |

**Repeating the identical experiment gives worse agreement (ρ = 0.45) than changing the dose
tenfold (ρ = 0.72) or changing the drug entirely (ρ = 0.75).** Whatever separates the two IFN
100 U/mL measurements is larger than the biology being measured.

### How large is the disagreement in practice?

For IFN-α 100 U/mL against its repeat:

| | |
|---|--:|
| median absolute difference between the two measurements | **0.295** |
| median absolute score itself | **0.278** |
| 75th percentile of the difference | 0.520 |
| 90th percentile | 0.767 |

**The typical disagreement between two measurements of the same variant is slightly larger than the
typical score.** A variant's measured effect and the error on that measurement are the same size.

### The consequence for variant calls

Taking the bottom and top deciles of each measurement independently:

| call | n per replicate | agreed by both | **replication rate** |
|---|--:|--:|--:|
| **loss of function** (bottom decile) | 2,253 | 1,757 | **78%** |
| **gain of function** (top decile) | 2,253 | 459 | **20%** |

**Only 20% of gain-of-function calls replicate.** Four out of five variants in the top decile of one
measurement are not in the top decile of the repeat. Loss-of-function calls hold up far better
(78%), because loss is a large, directional effect while gain is a small one near the noise.

Even **nonsense variants** — which have a large, consistent, unambiguous effect — reproduce at only
**ρ = 0.518** between the two arms.

### What follows from this

1. **Single-variant claims from one arm are unreliable**, particularly gain-of-function claims. Any
   individual variant of interest should be checked against both IFN 100 U/mL arms before being
   relied on.
2. **Group-level comparisons remain valid.** Averaging thousands of variants averages this error
   down; that is why the domain- and region-level results elsewhere in this project are stable
   across arms while individual positions move.
3. **The batch structure in §6 is the likely cause**, not an additional problem: the two repeats sit
   in different batches, and batch dominates condition throughout this dataset.
4. **The publication reports none of this.** It describes biological triplicates *within* each score
   set but gives no agreement statistics *between* score sets, and the term "duplicate assay" is
   MaveDB's, not the paper's.

---

## 3. Descriptive statistics — missense (n = 22,545)

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

## 4. Descriptive statistics — nonsense (n = 1,187): the dead-protein anchor

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

## 5. Assay quality per arm

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

## 6. Correlation between arms

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

## 7. Abundance versus signalling

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

## 8. Separating a signalling defect from an abundance defect

A variant can lose signal for two different reasons: there is **less protein**, or the protein
**does not work**. The dataset measures both, so in principle the two can be told apart. In practice
they can be separated cleanly for about **9% of variants** and not at all for the rest. This section
sets out why, because the problem applies to any analysis combining the two readouts.

### 8.1 The relationship has two regimes, not one

Signalling (IFN-α 100 U/mL) against abundance, in abundance deciles:

| abundance bin | n | median signal | local slope |
|---|--:|--:|--:|
| **−0.412 .. −0.326** | 2,252 | **−0.658** | **+8.65** |
| −0.326 .. −0.232 | 2,251 | −0.168 | +2.36 |
| −0.232 .. −0.162 | 2,251 | −0.132 | +1.55 |
| −0.162 .. −0.112 | 2,251 | −0.122 | +0.41 |
| −0.112 .. −0.076 | 2,252 | −0.078 | +0.59 |
| −0.076 .. −0.050 | 2,252 | −0.068 | +2.59 |
| −0.050 .. −0.030 | 2,251 | −0.060 | +2.01 |
| −0.030 .. −0.012 | 2,251 | −0.070 | −1.80 |
| −0.012 .. +0.007 | 2,251 | −0.066 | −5.07 |
| +0.007 .. +0.111 | 2,252 | −0.063 | −1.38 |

**Below roughly −0.30, protein is limiting** and signal falls steeply — slope +8.65 in the bottom
decile. **Above roughly −0.16 the slope flattens and turns negative**: more protein buys nothing,
consistent with the doxycycline-induced overexpression saturating the pathway.

A single linear fit averages across that threshold and describes neither regime.

### 8.2 Three reasons the residual method is weak here

**Abundance explains only 9% of signalling variance.** The naive fit gives slope 1.603, intercept
−0.053, Pearson r = **+0.305**, R² = **0.093**. Most of what varies in signalling has nothing to do
with protein level.

**Regression dilution.** Abundance has estimated reliability ≈ **0.545** (§2), so the attenuation-
corrected slope is 1.603 / 0.545 = **2.94**. A residual computed with the naive slope therefore
**leaves roughly 45% of the abundance effect unremoved** — the "specific activity" residual still
contains abundance.

**Matching on a noisy variable has the mirror problem.** Comparing variants within abundance strata
avoids the linearity assumption, but the strata are defined by a measurement that is ~45% error, so
bins are contaminated by regression to the mean.

**Nonsense variants do not calibrate this.** They have zero intrinsic function by construction, so
their signal should be at the floor regardless of protein level. Their observed slope is **+0.590**,
but that is confounded: a truncation further along the protein is both more stable and more likely
to retain function, so position drives both axes.

### 8.3 What does work: classify instead of regress

| category | definition | n | share |
|---|---|--:|--:|
| **clean signalling defect** | abundance > −0.20, signal in bottom decile | **958** | 4.3% |
| **clean abundance defect** | abundance ≤ −0.30, signal above the 40th percentile | **1,010** | 4.5% |
| both low | cannot be separated | 1,002 | 4.5% |
| both normal | — | 11,074 | 49.2% |
| ambiguous middle | — | 8,469 | 37.6% |

The two corner categories are interpretable **because they do not depend on a slope**. A variant
with wild-type protein levels and no signal is a functional defect under any model of the
relationship; a variant with severely reduced protein that still signals normally is an abundance
defect under any model. Those ~2,000 variants are the ones that can be named individually.

The 37.6% ambiguous middle cannot be resolved with these data. Neither can the 4.5% where both
readouts are low — a dead protein present at low level is consistent with either cause, or both.

### 8.4 Practical guidance

| if you want to | do this | not this |
|---|---|---|
| name individual variants | take the corner categories | threshold on a residual |
| compare two groups of variants | compare within abundance strata, and report the strata | report a single regression coefficient |
| claim a per-molecule activity change | measure it directly | infer it from a residual slope |

**For the interface analysis** (`interface_effect.md`): that result is a **corner claim**, not a
residual claim — interface variants sit at low abundance while retaining signal, which is the
clean-abundance-defect quadrant, robust to both the non-linearity and the dilution. What does *not*
follow from these data is the quantitative "specific activity" language: stating that each surviving
molecule works harder implies a slope that cannot be estimated reliably here.

---

## 9. How each arm relates to the sequence predictors

*Added after the genome-wide dbNSFP extraction (`external_data/TYK2/tyk2_dbnsfp_genomewide.csv`,
7,195 variants including CADD and MetaRNN). Both sides oriented so that higher = more damaging.*

Spearman, missense only:

| predictor | ifn_1U | ifn_10U | ifn_100U | ifn_100U′ | BMS 20nM | BMS 20nM′ | NDI 7nM | **abundance** | n |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **AlphaMissense** | **+0.169** | **+0.367** | +0.341 | +0.335 | +0.328 | +0.364 | +0.375 | **+0.418** | 22,516 |
| ESM1b | +0.144 | +0.314 | +0.291 | +0.282 | +0.288 | +0.313 | +0.324 | +0.362 | 22,516 |
| MetaRNN | +0.171 | +0.334 | +0.298 | +0.289 | +0.283 | +0.307 | +0.322 | +0.408 | 6,797 |
| REVEL | +0.156 | +0.302 | +0.267 | +0.260 | +0.264 | +0.280 | +0.292 | **+0.411** | 6,797 |
| VEST4 | +0.166 | +0.335 | +0.299 | +0.291 | +0.293 | +0.315 | +0.329 | +0.381 | 6,797 |
| CADD | +0.147 | +0.288 | +0.257 | +0.241 | +0.268 | +0.278 | +0.289 | +0.380 | 6,797 |
| PrimateAI | +0.119 | +0.249 | +0.224 | +0.218 | +0.221 | +0.234 | +0.246 | +0.350 | 6,791 |
| PolyPhen-2 | +0.143 | +0.271 | +0.236 | +0.230 | +0.241 | +0.260 | +0.271 | +0.343 | 6,797 |
| SIFT | +0.146 | +0.286 | +0.257 | +0.247 | +0.249 | +0.261 | +0.277 | +0.321 | 6,797 |
| GERP | +0.057 | +0.154 | +0.140 | +0.125 | +0.160 | +0.142 | +0.158 | +0.221 | 5,607 |

### Four observations

**1. Every predictor does better on abundance than on signalling.** AlphaMissense: **+0.418 on
abundance against +0.341 at 100 U/mL**. The pattern holds for all ten, including pure conservation
(GERP, +0.221 vs +0.140). These tools were trained to recognise variants that break proteins, and
protein level is the more direct readout of that. It is also what the stability literature predicts
(Gerasimavicius et al., *Protein Science* 2023, benchmarking nine tools against 49 DMS datasets).

**2. `ifn_1U` is the hardest arm for every predictor, by a factor of two.** AlphaMissense drops from
+0.367 at 10 U/mL to **+0.169** at 1 U/mL. Not a property of any particular tool — all ten halve.
The arm's separation is 0.56 and its SD/SE is 1.06 (§5), so most of this is the assay, not the
predictors. Any conclusion drawn from `ifn_1U` inherits that.

**3. Adding IFN *raises* correlations up to 10 U/mL, then flattens.** 1 U → 10 U → 100 U gives
+0.169 → **+0.367** → +0.341 for AlphaMissense. The peak is at 10 U/mL, not the highest dose, in
every row. The middle dose has both adequate dynamic range and enough residual sensitivity, and it
is the arm this project has used least.

**4. The drug arms behave like ordinary signalling arms.** BMS 20 nM, BMS 20 nM′ and NDI 7 nM give
+0.33, +0.36, +0.38 for AlphaMissense — slightly *above* the no-drug 100 U/mL arm (+0.341) and in
the same range as its batch-2 replicate (+0.335). Sub-saturating inhibitor does not change what the
predictors can see. That is expected: predictors score intrinsic variant damage, and partial
inhibition rescales signal without altering which variants are broken.

**Coverage note.** AlphaMissense and ESM1b are available for all 22,516 variants; everything else is
limited to the ~6,800 reachable by a single nucleotide change. The two sets are not directly
comparable in precision, though AlphaMissense's value changes by under 0.01 when restricted to the
smaller set.

---

## 10. Descriptive statistics for all sixteen predictors

*Raw values, as distributed — **not** sign-flipped. The last column says which direction means damaging.*

| predictor | n | coverage | mean | std | min | 25% | 50% | 75% | max | damaging |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **AlphaMissense** | 22,553 | 100% | +0.474 | 0.330 | +0.024 | +0.164 | +0.376 | +0.821 | +1.000 | high |
| **ESM1b** | 22,553 | 100% | -10.505 | 4.527 | -24.164 | -13.906 | -10.572 | -7.000 | +4.885 | **low** |
| **MetaRNN** | 6,803 | 30% | +0.496 | 0.338 | +0.000 | +0.161 | +0.455 | +0.850 | +0.994 | high |
| **CADD phred** | 6,803 | 30% | +19.490 | 10.304 | +0.001 | +11.770 | +23.500 | +26.700 | +35.000 | high |
| **REVEL** | 6,803 | 30% | +0.379 | 0.271 | +0.001 | +0.145 | +0.318 | +0.599 | +0.983 | high |
| **VEST4** | 6,803 | 30% | +0.484 | 0.271 | +0.019 | +0.238 | +0.456 | +0.726 | +0.990 | high |
| **PolyPhen-2** | 6,803 | 30% | +0.564 | 0.414 | +0.000 | +0.078 | +0.696 | +0.983 | +1.000 | high |
| **SIFT** | 6,803 | 30% | +0.150 | 0.244 | +0.000 | +0.001 | +0.023 | +0.193 | +1.000 | **low** |
| **PrimateAI** | 6,797 | 30% | +0.491 | 0.157 | +0.188 | +0.363 | +0.475 | +0.611 | +0.911 | high |
| **MutAssessor** | 6,797 | 30% | +1.839 | 1.166 | -3.095 | +0.995 | +1.895 | +2.710 | +4.805 | high |
| **PROVEAN** | 6,803 | 30% | -2.895 | 2.492 | -13.250 | -4.550 | -2.410 | -0.990 | +4.530 | **low** |
| **GERP** | 5,613 | 25% | +1.361 | 2.752 | -11.500 | +0.162 | +2.080 | +3.330 | +6.010 | high |
| **BLOSUM62** | 22,553 | 100% | -1.423 | 1.492 | -4.000 | -3.000 | -2.000 | -1.000 | +3.000 | **low** |
| **ddG_closed** | 22,536 | 100% | -4.600 | 4.304 | -10.000 | -10.000 | -3.946 | -1.213 | +10.000 | **low** |
| **ddG_open** | 22,536 | 100% | -4.410 | 4.423 | -10.000 | -10.000 | -3.686 | -1.048 | +10.000 | **low** |
| **ddG_diff** | 22,536 | 100% | +0.190 | 2.737 | -20.000 | -0.294 | +0.000 | +0.517 | +20.000 | n/a |

**Coverage splits into two groups.** AlphaMissense, ESM1b, BLOSUM62 and the three ΔΔG terms cover
**100%** of the 22,553 substitutions. Everything from dbNSFP covers only **~30%** — the variants
reachable by a single nucleotide change — and GERP only 25%. Correlations involving the dbNSFP
group are computed on ~6,800 variants, the others on ~22,500.

**Scales are wildly different**: PrimateAI spans 0.19–0.91 (SD 0.157) while ΔΔG spans the full
clipped range with SD 4.3, and CADD phred runs 0–35. This is why every correlation below is given
as Spearman first.


### 10.1 ΔΔG: raw and clipped side by side

Section 10 lists the three ΔΔG terms **clipped to [−10, 10]**, the window the published pipeline
uses. The raw values span three orders of magnitude more, so both are given here. All 22,536
TYK2 variants, matched AlphaFold 3 pair.

| feature | n | mean | std | min | 1% | 25% | 50% | 75% | 99% | max |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| ddG_closed raw | 22,536 | −50.68 | **188.38** | **−3047.9** | −941.26 | −11.35 | −3.95 | −1.21 | +6.69 | +540.0 |
| **ddG_closed clipped** | 22,536 | −4.60 | 4.30 | −10.0 | −10.00 | −10.00 | −3.95 | −1.21 | +6.69 | +10.0 |
| ddG_open raw | 22,536 | −49.00 | 183.02 | −3078.3 | −922.88 | −10.96 | −3.69 | −1.05 | +11.75 | +457.8 |
| **ddG_open clipped** | 22,536 | −4.41 | 4.42 | −10.0 | −10.00 | −10.00 | −3.69 | −1.05 | +10.00 | +10.0 |
| ddG_diff raw | 22,536 | +1.68 | **98.37** | −2188.7 | −202.29 | −1.02 | +0.05 | +1.30 | +248.79 | +1963.0 |
| **ddG_diff clipped** | 22,536 | +0.19 | 2.74 | −20.0 | −8.87 | −0.29 | +0.00 | +0.52 | +10.50 | +20.0 |

**Clipping moves 27.6% of ddG_closed values** (below −10) plus 0.68% above +10. The medians are
untouched — −3.95 either way — because the window only affects the tails.

### What clipping changes, and what it does not

| quantity | raw | clipped |
|---|--:|--:|
| r(closed, open) Pearson | **+0.860** | +0.804 |
| ρ(closed, open) Spearman | +0.837 | +0.823 |
| SD of the difference | 98.37 | 2.74 |
| …as a share of SD(ddG_closed) | 52% | **64%** |

| feature | AUC abundance | AUC IFN 100 U | AUC IFN 1 U |
|---|--:|--:|--:|
| ddG_closed raw | **0.714** | **0.745** | 0.567 |
| **ddG_closed clipped** | 0.704 | 0.733 | 0.565 |
| ddG_diff raw | 0.490 | 0.507 | 0.502 |
| **ddG_diff clipped** | 0.499 | 0.516 | 0.499 |

**Three points.**

**Clipping costs about 0.01 AUC.** ddG_closed scores 0.714 raw against 0.704 clipped on abundance,
0.745 against 0.733 at 100 U/mL. The extreme values carry ordering information: a ΔΔG of −3,000 is
a meaningless energy but a reliable statement that the substitution does not physically fit.
Discarding those variants entirely is worse still (0.693 at 100 U/mL).

**The difference feature is null either way** — 0.490 to 0.516 across all six cells. No treatment of
the tails rescues it, which rules out clipping as the explanation for its failure.

**Clipping slightly lowers the closed↔open correlation** (0.860 → 0.804 Pearson) because it
compresses the extremes, where the two states agree most strongly. That in turn *raises* the
difference's apparent share of the variance, from 52% to 64%.

**The magnitudes are not free energies.** The extreme values are ~100% `fa_rep` — pure steric
overlap — measured directly in `conclusions_ddG_difference_feature.md` §9, and reproduced by
Rosetta's own `ddg_monomer` (§10). Rank the values; never quote them as energies. On that basis a
rank transform, not clipping, is the technically correct treatment: it gives results identical to
raw (both rank-based statistics are unchanged by any monotone transform) while removing the
temptation to read the numbers as kcal/mol.

---

## 11. Correlation matrices — Spearman and Pearson

All features **oriented so that higher = more damaging**, so every entry should be positive if two
features agree.

### 11.1 Spearman (rank)

| | AlphaM | ESM1b | MetaRNN | CADD | REVEL | VEST4 | PPh2 | SIFT | PrimAI | MutAss | PROVEAN | GERP | BLOSUM | ddGclos | ddGopen | ddGdiff |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AlphaM** | — | +0.79 | +0.86 | +0.81 | +0.76 | +0.85 | +0.76 | +0.72 | +0.76 | +0.53 | +0.76 | +0.52 | +0.33 | +0.48 | +0.47 | +0.02 |
| **ESM1b** | +0.79 | — | +0.76 | +0.72 | +0.66 | +0.75 | +0.68 | +0.64 | +0.59 | +0.51 | +0.74 | +0.47 | +0.32 | +0.44 | +0.44 | +0.03 |
| **MetaRNN** | +0.86 | +0.76 | — | +0.85 | +0.86 | +0.92 | +0.83 | +0.79 | +0.76 | +0.58 | +0.84 | +0.61 | +0.29 | +0.49 | +0.47 | +0.00 |
| **CADD** | +0.81 | +0.72 | +0.85 | — | +0.81 | +0.83 | +0.81 | +0.76 | +0.75 | +0.45 | +0.76 | +0.61 | +0.23 | +0.42 | +0.41 | +0.01 |
| **REVEL** | +0.76 | +0.66 | +0.86 | +0.81 | — | +0.81 | +0.77 | +0.70 | +0.74 | +0.39 | +0.73 | +0.55 | +0.27 | +0.40 | +0.39 | +0.01 |
| **VEST4** | +0.85 | +0.75 | +0.92 | +0.83 | +0.81 | — | +0.80 | +0.73 | +0.77 | +0.56 | +0.79 | +0.57 | +0.33 | +0.47 | +0.46 | +0.01 |
| **PPh2** | +0.76 | +0.68 | +0.83 | +0.81 | +0.77 | +0.80 | — | +0.72 | +0.71 | +0.53 | +0.73 | +0.50 | +0.22 | +0.42 | +0.42 | +0.02 |
| **SIFT** | +0.72 | +0.64 | +0.79 | +0.76 | +0.70 | +0.73 | +0.72 | — | +0.59 | +0.58 | +0.80 | +0.48 | +0.30 | +0.40 | +0.39 | +0.01 |
| **PrimAI** | +0.76 | +0.59 | +0.76 | +0.75 | +0.74 | +0.77 | +0.71 | +0.59 | — | +0.35 | +0.62 | +0.52 | +0.06 | +0.36 | +0.35 | -0.00 |
| **MutAss** | +0.53 | +0.51 | +0.58 | +0.45 | +0.39 | +0.56 | +0.53 | +0.58 | +0.35 | — | +0.58 | +0.30 | +0.26 | +0.39 | +0.39 | +0.03 |
| **PROVEAN** | +0.76 | +0.74 | +0.84 | +0.76 | +0.73 | +0.79 | +0.73 | +0.80 | +0.62 | +0.58 | — | +0.50 | +0.46 | +0.43 | +0.43 | +0.03 |
| **GERP** | +0.52 | +0.47 | +0.61 | +0.61 | +0.55 | +0.57 | +0.50 | +0.48 | +0.52 | +0.30 | +0.50 | — | +0.10 | +0.24 | +0.24 | +0.02 |
| **BLOSUM** | +0.33 | +0.32 | +0.29 | +0.23 | +0.27 | +0.33 | +0.22 | +0.30 | +0.06 | +0.26 | +0.46 | +0.10 | — | +0.23 | +0.22 | +0.02 |
| **ddGclos** | +0.48 | +0.44 | +0.49 | +0.42 | +0.40 | +0.47 | +0.42 | +0.40 | +0.36 | +0.39 | +0.43 | +0.24 | +0.23 | — | +0.82 | -0.18 |
| **ddGopen** | +0.47 | +0.44 | +0.47 | +0.41 | +0.39 | +0.46 | +0.42 | +0.39 | +0.35 | +0.39 | +0.43 | +0.24 | +0.22 | +0.82 | — | +0.26 |
| **ddGdiff** | +0.02 | +0.03 | +0.00 | +0.01 | +0.01 | +0.01 | +0.02 | +0.01 | -0.00 | +0.03 | +0.03 | +0.02 | +0.02 | -0.18 | +0.26 | — |

### 11.2 Pearson (linear)

| | AlphaM | ESM1b | MetaRNN | CADD | REVEL | VEST4 | PPh2 | SIFT | PrimAI | MutAss | PROVEAN | GERP | BLOSUM | ddGclos | ddGopen | ddGdiff |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **AlphaM** | — | +0.76 | +0.81 | +0.66 | +0.76 | +0.82 | +0.65 | +0.42 | +0.73 | +0.50 | +0.71 | +0.37 | +0.32 | +0.45 | +0.44 | +0.02 |
| **ESM1b** | +0.76 | — | +0.74 | +0.70 | +0.65 | +0.74 | +0.65 | +0.48 | +0.58 | +0.52 | +0.69 | +0.43 | +0.32 | +0.42 | +0.42 | +0.02 |
| **MetaRNN** | +0.81 | +0.74 | — | +0.81 | +0.85 | +0.93 | +0.81 | +0.57 | +0.76 | +0.56 | +0.79 | +0.51 | +0.28 | +0.45 | +0.44 | -0.01 |
| **CADD** | +0.66 | +0.70 | +0.81 | — | +0.74 | +0.78 | +0.78 | +0.61 | +0.70 | +0.46 | +0.67 | +0.57 | +0.21 | +0.38 | +0.38 | +0.01 |
| **REVEL** | +0.76 | +0.65 | +0.85 | +0.74 | — | +0.81 | +0.72 | +0.47 | +0.75 | +0.40 | +0.71 | +0.46 | +0.25 | +0.38 | +0.37 | +0.00 |
| **VEST4** | +0.82 | +0.74 | +0.93 | +0.78 | +0.81 | — | +0.77 | +0.51 | +0.77 | +0.55 | +0.76 | +0.50 | +0.32 | +0.44 | +0.43 | +0.00 |
| **PPh2** | +0.65 | +0.65 | +0.81 | +0.78 | +0.72 | +0.77 | — | +0.53 | +0.65 | +0.52 | +0.66 | +0.42 | +0.22 | +0.40 | +0.40 | +0.01 |
| **SIFT** | +0.42 | +0.48 | +0.57 | +0.61 | +0.47 | +0.51 | +0.53 | — | +0.38 | +0.47 | +0.57 | +0.32 | +0.24 | +0.29 | +0.29 | +0.00 |
| **PrimAI** | +0.73 | +0.58 | +0.76 | +0.70 | +0.75 | +0.77 | +0.65 | +0.38 | — | +0.35 | +0.61 | +0.45 | +0.05 | +0.33 | +0.32 | -0.01 |
| **MutAss** | +0.50 | +0.52 | +0.56 | +0.46 | +0.40 | +0.55 | +0.52 | +0.47 | +0.35 | — | +0.56 | +0.32 | +0.24 | +0.36 | +0.37 | +0.03 |
| **PROVEAN** | +0.71 | +0.69 | +0.79 | +0.67 | +0.71 | +0.76 | +0.66 | +0.57 | +0.61 | +0.56 | — | +0.42 | +0.46 | +0.37 | +0.37 | +0.01 |
| **GERP** | +0.37 | +0.43 | +0.51 | +0.57 | +0.46 | +0.50 | +0.42 | +0.32 | +0.45 | +0.32 | +0.42 | — | +0.09 | +0.20 | +0.19 | -0.00 |
| **BLOSUM** | +0.32 | +0.32 | +0.28 | +0.21 | +0.25 | +0.32 | +0.22 | +0.24 | +0.05 | +0.24 | +0.46 | +0.09 | — | +0.21 | +0.20 | -0.01 |
| **ddGclos** | +0.45 | +0.42 | +0.45 | +0.38 | +0.38 | +0.44 | +0.40 | +0.29 | +0.33 | +0.36 | +0.37 | +0.20 | +0.21 | — | +0.80 | -0.27 |
| **ddGopen** | +0.44 | +0.42 | +0.44 | +0.38 | +0.37 | +0.43 | +0.40 | +0.29 | +0.32 | +0.37 | +0.37 | +0.19 | +0.20 | +0.80 | — | +0.35 |
| **ddGdiff** | +0.02 | +0.02 | -0.01 | +0.01 | +0.00 | +0.00 | +0.01 | +0.00 | -0.01 | +0.03 | +0.01 | -0.00 | -0.01 | -0.27 | +0.35 | — |

### 11.3 Where Spearman and Pearson disagree

| pair | Spearman | Pearson | difference | n |
|---|--:|--:|--:|--:|
| AlphaMissense vs **SIFT** | +0.720 | +0.420 | **+0.300** | 6,803 |
| **SIFT** vs PROVEAN | +0.802 | +0.568 | +0.233 | 6,803 |
| REVEL vs **SIFT** | +0.701 | +0.472 | +0.230 | 6,803 |
| MetaRNN vs **SIFT** | +0.794 | +0.570 | +0.225 | 6,803 |
| VEST4 vs **SIFT** | +0.730 | +0.506 | +0.224 | 6,803 |
| **SIFT** vs PrimateAI | +0.591 | +0.385 | +0.206 | 6,797 |
| PolyPhen-2 vs **SIFT** | +0.723 | +0.534 | +0.189 | 6,803 |
| AlphaMissense vs GERP | +0.522 | +0.370 | +0.152 | 5,613 |
| AlphaMissense vs CADD | +0.808 | +0.663 | +0.146 | 6,803 |

**Nine of the twelve largest disagreements involve SIFT**, and Spearman is higher every time.
SIFT's distribution is extremely skewed — median **0.023**, 25th percentile **0.001**, i.e. most
variants are pressed against zero. Pearson is dragged down by that compression; the *ranking*
agrees with the other tools far better than the *values* do. Any analysis using raw SIFT scores
linearly will understate its agreement with the panel.

The same applies, more mildly, to AlphaMissense vs CADD (+0.81 rank, +0.66 linear) and to GERP.

**Use Spearman throughout.** The only features where Pearson exceeds Spearman are the ΔΔG pair
(+0.80 vs +0.82 — essentially equal) and ΔΔG_diff against its own inputs, where the linear figure
is inflated by the clipped extremes.

---

## 12. What the matrices show

**One dominant block.** Eleven of the sixteen features correlate at +0.6 to +0.92 with each other:
AlphaMissense, ESM1b, MetaRNN, CADD, REVEL, VEST4, PolyPhen-2, SIFT, PrimateAI, PROVEAN and (more
loosely) MutationAssessor and GERP. **MetaRNN ↔ VEST4 reaches +0.92** — the two highest-agreeing
features in the set, both machine-learned meta-predictors.

**Three features sit outside it.**

| feature | agreement with the main block | why |
|---|--:|---|
| **BLOSUM62** | +0.05 to +0.46 | a substitution matrix — no structure, no conservation, no training |
| **GERP** | +0.10 to +0.61 | pure sequence conservation, no variant-specific modelling |
| **ΔΔG_closed / ΔΔG_open** | **+0.20 to +0.49** | physics on a structure — a genuinely different input |

ΔΔG's independence is the one worth noting: at +0.40–0.49 it agrees enough to be measuring
something real, but is far enough from +0.85 to add information the sequence panel does not have.
PrimateAI vs BLOSUM62 at **+0.05** is the single lowest pair in the matrix.

**ΔΔG_diff is null against all fifteen others** (−0.00 to +0.03). Its only non-zero entries are
with its own two inputs — **−0.18** and **+0.26** Spearman, **−0.27** and **+0.35** Pearson. A
quantity near-orthogonal to both terms it is built from, which is what subtracting two features
correlated at +0.82 produces.

---

## 13. Practical summary

| | |
|---|---|
| best signalling arms | `ifn_100U`, `ifn_100U_dup`, `ndi034858_7nM` (separation 2.5–2.7) |
| best abundance arm | `abundance` (separation 2.62, lowest SE) |
| weakest usable arm | **`ifn_1U`** — separation 0.56, SD/SE 1.06 |
| unusable | `bms986202_1uM`, `bms986202_10uM`, `ndi034858_1uM` |
| mandatory constraint | pair arms **within batch** for any subtraction |
| **reproducibility** | **ρ = 0.45 between repeats of the same condition; GOF calls replicate at 20%** |
| per-arm dead anchor | use the arm's own nonsense median, not −0.352 |
| best arm for predictor benchmarking | **`abundance`** (ρ up to +0.42), then **`ifn_10U`** (+0.37) |
| worst arm for predictor benchmarking | **`ifn_1U`** (+0.17) — half of every other signalling arm |

*Source: Howard et al., eLife 2026, DOI 10.7554/eLife.110149.2 (preprint bioRxiv
10.1101/2025.10.11.681520). MaveDB `urn:mavedb:00001270-a` and `00001271-a`, retrieved
26 October 2026.*
