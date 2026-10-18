# Cross-run analysis of the whole campaign (2026-10-18)

Every run folder in this repository was re-read and re-analysed together, rather than run by run. The
per-seed "selected structure" tables of **54 runs** were parsed into one table of **478 seed values**
(10 early JAK1/JAK2 runs from 13–14 October use a layout the parser does not read and are excluded; so are
the template-bearing runs wherever a comparison is made, which is noted per section).

All p-values below were recomputed from the per-seed values: Mann-Whitney U (two-sided, tie-corrected) for
distances, Fisher's exact test for state counts. "Open" means FERM–JH1 > 80 Å, "compact" < 60 Å.

---

## 1. The assay does detect the canonical activating mutations

Measured as state counts rather than medians, four comparisons are significant and all point the same way —
the activating mutation increases the fraction of open seeds:

| comparison | wild type open | mutant open | Fisher p |
|---|---|---|---|
| **JAK2 V617F at 512/8192** | 7/16 | **16/16** | **0.0008** |
| JAK1 V658F at 96/384 | 2/5 | 16/16 | 0.0075 |
| JAK3 M592F at 128/512 | 0/16 | 5/16 | 0.043 |
| JAK1 V658F at 128/512 | 12/20 | 14/15 | 0.048 |

V617F abolishing JAK2's compact state entirely (7/16 → 16/16 open) is the strongest single result in the
campaign. This matters for interpreting every negative result: the method is **not** globally insensitive.

## 2. Detection only works inside a narrow window of MSA depth

Every significant result above occurs at a depth where wild type is **partially** open. Where wild type is
at a floor (0/n open) or a ceiling (n/n open), every test returns p = 1.00:

| situation | examples | outcome |
|---|---|---|
| wild type at ceiling | JAK1 V658F at 64/256 (WT 5/5) | p = 1.00 |
| wild type at floor | JAK2 V617F at 64/256 and 96/384 (WT 0/16, 0/5); TYK2 P982A at 32/64 (WT 0/15) | p = 1.00 |
| wild type mixed | the four hits in §1 | detectable |

The one exception is JAK3 M592F, which escapes a floor (WT 0/16 → 5/16).

**Consequence: the depth must be tuned per protein before screening mutations.** A null obtained at a
saturated depth carries no information. Several nulls in this campaign were obtained at saturated depths.

## 3. The V617F "depth reversal" — resolved: the anomaly is in wild type

V617F first appeared to give opposite significant answers one depth apart: *closing* JAK2 at 256/1024
(wild type 16/16 open → mutant 4/8, p = 0.0066) and *opening* it at 512/8192 (7/16 → 16/16, p = 0.0008).
Seeds 8–15 of the 256/1024 arm were run to test whether the weaker (n = 8) side was batch variance
([JAK2_V617F_20261018_201552](JAK2/runs/JAK2_V617F_20261018_201552/conclusions.md)).

It was not: pooled V617F is **9/16 open** and the halves agree exactly (4/8 vs 5/8, Fisher p = 1.00).
But the full depth scan shows where the problem actually lies:

| open seeds (FERM–JH1 > 80 Å) | 64/256 | 128/512 | 256/1024 | 512/8192 |
|---|---|---|---|---|
| JAK2 wild type | 0/16 | 1/15 | **16/16** | 7/16 |
| JAK2 V617F | 0/16 | 6/16 | 9/16 | 16/16 |

**V617F is monotonic (0 → 6 → 9 → 16 open with increasing depth). Wild type is not (0 → 1 → 16 → 7).**

Wild type spikes to fully open at 256/1024 and drops back to 7/16 at 512/8192, while being nearly all
compact at the two shallower depths. That one point is the sole depth at which V617F looks like it
"closes" JAK2. Everywhere else the mutation is as open as, or more open than, wild type (128/512 p = 0.083;
512/8192 p = 0.0008; 64/256 both at the floor).

So the mutation behaves consistently and in the expected direction. **What needs explaining is JAK2 wild
type at 256/1024** — reproducible across its own two runs (n5 + n11, p = 0.72) yet far off the trend of its
neighbours. Until that is understood, 256/1024 should not be used as a comparison depth for JAK2, and the
"V617F closes JAK2" reading should be retired.

## 4. The distributions are bimodal, so medians are the wrong summary

JAK2 wild type at 512/8192 is 9 seeds near 47 Å and 7 seeds near 95 Å. Its median, 49.6 Å, describes no
structure that was actually produced. Conditions with both basins populated (≥2 seeds each):

JAK1 WT 128/512 · JAK1 WT 96/384 · JAK2 V617F 128/512 · JAK2 V617F 256/1024 · JAK2 WT 512/8192 ·
JAK3 M592F 128/512 · TYK2 P982A 64/256 · TYK2 WT 64/256

The two test families disagree on real cases, in both directions:

- **JAK3 A573V**: Mann-Whitney on medians p = 0.001, but state counts 0/16 vs 0/16 (p = 1.00). The mutation
  shifts position *within* the compact basin; it does not change state.
- **JAK3 M592F**: medians p = 0.012 and counts p = 0.043 — agreeing, because seeds genuinely cross over.

Report both, and say which one the claim rests on.

## 5. Wild-type depth profiles are not monotonic for JAK1 and JAK2

Fraction of open seeds by depth (no template):

| | 32/64 | 64/256 | 96/384 | 128/512 | 160/640 | 256/1024 | 512/8192 |
|---|---|---|---|---|---|---|---|
| JAK1 | – | 5/5 | 2/5 | 12/20 | 5/5 | 5/5 | – |
| JAK2 | – | 0/16 | 0/5 | 1/15 | – | **16/16** | 7/16 |
| JAK3 | – | – | – | 0/16 | – | 15/16 | 8/8 |
| TYK2 | 0/15 | 8/16 | – | 8/8 | – | – | – |

JAK3 and TYK2 switch cleanly from compact to open as the MSA deepens. **JAK1 and JAK2 do not**: JAK2 is fully
open at 256/1024 but falls back to 7/16 at 512/8192, and JAK1 dips at 96/384. Some points rest on n = 5.
The simple "deeper MSA → more open" model holds for two of the four kinases.

## 6. Batch-to-batch variance affects 6 of 10 repeated conditions

Two runs of the *same* condition, hours or days apart on different sandboxes:

| condition | run A | run B | MW p |
|---|---|---|---|
| JAK3 A572V 128/512 | n8 med 55.1 | n8 med 49.5 | **0.010** |
| TYK2 WT 64/256 | n8 med 56.3 | n8 med 92.1 | **0.010** |
| JAK2 WT 64/256 | n5 med 62.6 | n11 med 57.2 | **0.023** |
| JAK2 WT full+template | n5 med 44.8 | n5 med 44.1 | **0.027** |
| JAK3 M511I 128/512 | n8 med 53.2 | n8 med 43.7 | 0.083 |
| TYK2 P982A 64/256 | n8 med 85.6 | n8 med 91.8 | 0.083 |
| JAK2 WT 256/1024 | n5 med 94.8 | n11 med 94.8 | 0.721 |
| JAK2 WT 512/8192 | n5 med 49.6 | n11 med 49.6 | 0.776 |
| TYK2 WT 32/64 | n7 med 45.2 | n8 med 45.5 | 0.685 |
| TYK2 P982A 32/64 | n7 med 45.0 | n8 med 41.0 | 0.325 |

Batches disagree in the mixed regime and agree at saturation — the same regime where effects are detectable
is the regime where the baseline is unstable. **Never quote a single 8-seed half**, and check halves against
each other before quoting a pooled result.

**This touches a headline result.** JAK3 A572V's two halves differ at p = 0.010, and on pooled FERM–JH1 this
analysis gets p = 0.13 with 0/16 vs 0/16 open, where `mutation_analysis.md` reports p = 0.035. The
discrepancy needs reconciling before A572V is cited; it may come from a different wild-type set or a
one-sided test.

## 7. TYK2 is a low-confidence outlier

Mean pLDDT of selected structures:

| | 32/64 | 64/256 | 128/512 | 256/1024 | 512/8192 |
|---|---|---|---|---|---|
| JAK1 | 82.0 | 84.5 | 85.2 | 85.7 | 85.9 |
| JAK2 | 86.2 | 84.1 | 85.1 | 85.8 | 85.6 |
| JAK3 | – | – | 84.1 | 85.3 | 85.8 |
| **TYK2** | **76.8** | **80.6** | **81.3** | – | – |

TYK2 sits 4–8 points below all three JAKs at every depth, and its spread at 32/64 is 3× larger (sd 1.8 vs
≤ 0.6). Whatever makes TYK2 behave differently in this campaign may be prediction quality rather than
biology.

## 8. One published number is a statistical artifact

TYK2 P982A at 128/512 is reported as significant (Mann-Whitney p = 0.011). Both arms are 8/8 open and the
difference in medians is 0.5 Å — 0.5 % of the ~50 Å open/closed separation. Significant on ranks because
both distributions are tight; meaningless as structure. Pair every p-value with an effect size in Å and a
state count.

---

## What follows from this

1. **Before screening a mutation, locate the protein's sensitive depth** — the one where wild type is mixed
   *and* reproducible across two independent batches. For TYK2 no such depth has been found yet: 32/64 is a
   floor, 128/512 a ceiling, 64/256 mixed but unstable. Depths between 32/64 and 64/256 are untested.
2. **Use 16 seeds minimum, split into two batches that are checked against each other** before pooling.
3. **Report state counts and medians together**, with effect sizes in Å.
4. ~~For TYK2, add JH2–JH1 as a readout.~~ **Retracted — see §9.**
5. **Explain the JAK2 wild-type 256/1024 anomaly (§3)** and reconcile the A572V discrepancy (§6) before
   building further on either. The V617F reversal itself is resolved.

---

## 9. Added after a power test: a coordinate is either saturated or irreproducible

JH2–JH1 was proposed above as TYK2's usable readout, on the strength of V678F reaching p = 0.028 and P982A
trending at p = 0.097 with 15 seeds. Sixteen further P982A seeds
([TYK2_P982A_20261018_201530](TYK2/runs/TYK2_P982A_20261018_201530/conclusions.md)) destroy that:

| JH2–JH1 at 32/64 | n | median | vs wild type |
|---|--:|--:|---|
| wild type | 15 | 49.3 | – |
| P982A seeds 0–15 | 15 | 53.5 | p = 0.097 (looser) |
| P982A seeds 16–31 | 16 | 45.0 | p = 0.093 (tighter) |
| **P982A pooled** | **31** | **46.5** | **p = 0.96** |

The two batches of the *same condition* differ at **p = 0.0005**, straddle wild type, and each trends to
near-significance in the opposite direction. V678F's own halves differ by 4.3 Å on this coordinate
(p = 0.066), so its p = 0.028 is inside the same noise and should be treated as unconfirmed.

At 32/64 the two coordinates therefore fail in complementary ways:

| coordinate | P982A batch 1 vs 2 | informative? |
|---|---|---|
| FERM–JH1 | 42.4 vs 42.9 Å, p = 0.57 — stable | no: 0/31 open, saturated at the floor |
| JH2–JH1 | 53.5 vs 45.0 Å, p = 0.0005 — unstable | no: noise exceeds the effect |

**A coordinate here is either saturated and reproducible, or responsive and irreproducible.** No depth
tested so far escapes this, and it is the main obstacle to measuring TYK2 mutation effects.

**Revised priority: measure the batch effect before running more comparisons.** Three or four wild-type
batches of 8 seeds at one depth would give the between-batch variance directly, and every claimed effect in
this repository could then be judged against it. The MSA is rebuilt per run, making MSA sampling the prime
suspect; caching one MSA across batches would separate that from everything else.

---

Reproduction: the parser and analysis scripts used here are straightforward to regenerate — read each
`conclusions.md`, pull the per-seed table and the matching `run_config.json`, and group by
(target, mutation, MSA, template).
