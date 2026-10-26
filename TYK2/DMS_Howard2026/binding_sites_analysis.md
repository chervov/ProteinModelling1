# Drug-response positions in TYK2, read out from the DMS inhibitor arms

*26 October 2026. Analysis of the BMS-986202 and NDI-034858 arms of the Howard et al. DMS
(`TYK2/DMS_Howard2026/`), compared against the positions the paper itself reports.*

---

## 1. What is measured

Each inhibitor arm is **IFN-α 100 U/mL plus drug**, so the informative quantity is the difference
from the no-drug arm of the **same batch**:

> **drug effect (per variant) = (score with drug) − (score without drug)**

Both inputs are log₂ fold change versus wild type, so this asks: *does the drug hit this variant
harder or less hard than it hits wild type?* Negative = more sensitive, positive = more resistant,
zero = the drug treats it like wild type.

Per **position**, the drug effect is averaged over its ~19 substitutions.

### Which columns, and the batch constraint

| with drug | paired no-drug column | batch |
|---|---|---|
| `bms986202_20nM` | `ifn_100U` | 1 − 1 |
| `bms986202_20nM_dup` | `ifn_100U_dup` | 2 − 2 |
| `ndi034858_7nM` | `ifn_100U_dup` | 2 − 2 |

The arms carry an **undocumented batch structure**: `ifn_100U` and `ifn_100U_dup` are the same
condition yet correlate at only **ρ = 0.45**, while `ifn_100U_dup` correlates with `ndi034858_7nM`
at **0.72** and with `bms986202_20nM_dup` at **0.68**. Batch is a stronger signal than condition, so
a drug arm must be paired with the no-drug arm from its own batch. The paper does not mention batch
effects or report between-arm agreement.

The three saturating arms (`bms986202_1uM`, `bms986202_10uM`, `ndi034858_1uM`) are unusable: their
nonsense median is ≈ 0, i.e. a truncated protein scores like wild type, so no variant information
survives.

---

## 2. The drug effect is confined to the allosteric pocket

Position-level drug effect by region, using the two batch-2 arms:

| region | n variants | mean effect | SD | mean \|effect\| |
|---|--:|--:|--:|--:|
| **allosteric pocket (paper's residues)** | 342 | **+0.155** | **0.644** | **0.545** |
| JH2, outside the pocket | 5,111 | +0.005 | 0.388 | 0.301 |
| linker / SH2 | 4,062 | −0.041 | 0.285 | 0.219 |
| JH1 kinase | 5,309 | −0.031 | 0.336 | 0.259 |
| FERM | 7,709 | −0.035 | 0.328 | 0.255 |

Everything outside the pocket centres on **zero** — those variants respond to the drug exactly as
wild type does. Only the pocket departs, with about **double the mean absolute effect** and double
the spread.

The same conclusion from the other direction — correlation between with-drug and without-drug
scores, where high means "the drug does not change the variant ranking here":

| region | BMS vs no-drug | NDI vs no-drug |
|---|--:|--:|
| **allosteric pocket** | **0.650** | **0.760** |
| JH1 kinase | **0.846** | 0.878 |
| linker / SH2 | 0.744 | 0.792 |
| JH2, outside pocket | 0.713 | 0.776 |
| FERM | 0.727 | 0.767 |

Adding drug barely changes the ranking in JH1 (r = 0.85); the pocket is where it rearranges most.

**Two caveats.** The residual 0.22–0.30 mean |effect| outside the pocket is **not** biology — it is
the noise floor of subtracting two noisy arms, and it sets the detection limit for anything subtle.
JH2-outside-pocket sits slightly above the other non-pocket regions (0.301), which is consistent
with the paper's remark about positions implicated through *"allosteric transmission"*, but the
effect is too small to claim.

---

## 3. Comparison with the positions the paper reports

The paper names:

- **allosteric pocket**: 594, 596, 598, 603, 606, 694, 695, 696, 737, 739, 740, 757
- **BMS-986202 resistance (FDR < 0.01)**: **690** (V690P), **671** (A671E/K/L/Q/Y), **687** (T687R),
  **758** (S758D/H)
- **drug-interaction residues**: 601, 603, 640, 694, 739

Ranking positions by mean drug effect (≥10 variants, no significance test) gives:

| my top resistant | status in the paper |
|---|---|
| **671** | **resistance position** ✓ |
| **687** | **resistance position** ✓ |
| **640** | **drug-interaction residue** ✓ |
| 741 | adjacent to 739, 740 |
| 759 | adjacent to 757, 758 |
| 689 | adjacent to 687, 690 |
| 595 | adjacent to 594, 596 |
| 642, 796, 799 | not in the paper |

| my top sensitive | status in the paper |
|---|---|
| **739** | **pocket + potentiating** ✓ |
| **601** | **drug-interaction residue** ✓ |
| 599, 600 | adjacent to 598 |
| 811, 700, 711, 894, 898, 682 | not in the paper |

**5 of 20 are named in the paper; another 6 lie within two residues of a named position; 9 are not
reported.** In the other direction, **13 of the paper's 16 named positions are missing from the
top-10 lists**, including V690 — their single strongest resistance position.

### Why the method misses things theirs finds

**V690P is the clearest case.** The paper tests one substitution — valine to proline. Averaging all
19 substitutions at position 690 dilutes a single strong variant into the noise. The approaches see
different things: position averaging finds sites where *most* substitutions matter; their
per-variant FDR testing finds individual variants.

**A correction to an earlier claim.** The statement that these positions "are the drug binding site"
was an inference from *"they are in JH2 and the drugs bind JH2"* — but JH2 is 287 residues and the
pocket is ~12, so membership of JH2 is weak evidence. What the ranking actually recovers is the
broader drug-response region: the pocket, its immediate neighbours, and some positions outside it.
No significance test or multiple-testing correction was applied across 1,187 positions; the support
for these being real is that they reproduce across two different drugs and concentrate in JH2, which
is a sanity check rather than statistics.

---

## 4. Do the two drugs act on the same sites?

Both from batch 2 against the same baseline, so directly comparable:

| level | Pearson | Spearman |
|---|--:|--:|
| per variant (n = 22,533) | +0.584 | +0.549 |
| **per position** (n = 1,187) | **+0.785** | +0.696 |

Largely the same pocket, as expected for two JH2 allosteric inhibitors. Position-level agreement
exceeds variant-level, so most disagreement is per-substitution noise rather than different sites.

**Where they genuinely differ:**

| position | BMS | NDI | difference | the paper |
|---|--:|--:|--:|---|
| **758** | **+0.729** | +0.185 | **+0.544** | BMS resistance, partial NDI overlap |
| **671** | **+0.938** | +0.537 | +0.401 | BMS resistance — *"only about half also disrupt NDI"* |
| 673 | +0.379 | −0.388 | +0.768 | not reported |
| **601** | **−0.883** | −0.433 | −0.450 | drug-interaction residue |
| **690** | +0.025 | **+0.305** | −0.279 | BMS resistance (V690P) |

**Two of these independently reproduce the paper's own observations.** At **671** they report that
of 11 BMS-resistance variants only about half also disrupt NDI; the position means give BMS +0.94
against NDI +0.54 — the same partial overlap. At **758** they note BMS resistance with partial NDI
overlap; the means give +0.73 against +0.19.

**One disagrees, for the reason above**: 690 looks slightly more NDI-affected here because the
position average dilutes the single V690P effect.

---

## 5. What this supports

1. **The measure is real.** Drug effects localise to the allosteric pocket, vanish everywhere else,
   agree between two different drugs at ρ = 0.79 position-wise, and independently recover three of
   the paper's named resistance/interaction residues plus its partial-overlap finding at two of them.
2. **It is cruder than the paper's.** Position averaging cannot see variant-specific effects, and no
   multiple-testing correction was applied. Their per-variant FDR analysis is the better instrument
   for identifying individual resistance variants.
3. **The detection limit is ~0.3 in mean |effect|.** That is the noise floor outside the pocket, and
   it is why the JH2–JH1 interface test (`interface_effect.md` §10, effect ≈ 0.08) is inconclusive
   rather than negative.

*Data: `TYK2/DMS_Howard2026/TYK2_DMS_Howard2026_all_arms.csv`. Source publication: Howard et al.,
eLife 2026, DOI 10.7554/eLife.110149.2.*
