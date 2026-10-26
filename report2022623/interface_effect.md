# The TYK2 JH2–JH1 interface effect

**A dissociation between protein abundance and signalling, measured on deep mutational scanning data**

**Data from *Deep mutational scanning reveals pharmacologically relevant insights into TYK2
signaling and disease*** (Howard et al., *eLife* 2026) — full citation in section 2.

*Generated 2026-10-23. Data, methods and every number below are reproducible from
`data/orianne/tyk2_variants.csv`, `data/ddg/ddg_TYK2_all.json` and `data/orianne/iface_*.json`.*

---

## 1. Summary

Mutations at the 26-residue JH2–JH1 interface of TYK2 do something that no other region of the
protein does: they **destroy protein abundance while leaving interferon signalling intact**.

| | interface | rest of JH2+JH1 |
|---|--:|--:|
| variants in the bottom abundance quartile | **68.8%** | 37.7% |
| variants that are loss-of-function at IFN-α 100 U/mL | **4.9%** | 15.3% |
| variants that are loss-of-function at IFN-α 1 U/mL | **8.1%** | 11.4% |

That is a three-fold *enrichment* for low abundance alongside a three-fold *depletion* for loss of
function. Both effects are large, both are highly significant, and they point in opposite
directions. Normally the two track each other closely — a protein that is not there cannot signal.

The interpretation that fits every test below is that **interface mutations produce a
de-repressed enzyme**: each surviving molecule signals harder, which compensates for there being
far fewer of them. The effect appears exactly where that compensation would be visible — at the
lowest abundances — and disappears where protein is plentiful.

**This is not classical gain of function.** Interface variants are *not* enriched among the top
decile of absolute signal (9.6% vs 8.9%, p = 0.81). The gain is in **specific activity**: signal
per unit protein. A screen that ranks variants by raw signalling output cannot see it.

**The specific-activity mechanism failed its decisive test** (section 10, added 26 October).
Interface variants show no change in sensitivity to the allosteric TYK2 inhibitors that act on the
JH2-JH1 equilibrium, on an assay that detects drug-pocket effects at p = 1e-16. The measured
dissociation below is unaffected; the conformational *explanation* for it is not supported.

---

## 2. Source of the data

All phenotype measurements analysed here come from a single published deep mutational scan:

> **Deep mutational scanning reveals pharmacologically relevant insights into TYK2 signaling and
> disease**
>
> Conor J. Howard, Nathan S. Abell, … Sriram Kosuri, **Diane E. Dickel** (24 authors)
>
> *eLife*, published **10 June 2026**. DOI **[10.7554/eLife.110149.2](https://doi.org/10.7554/eLife.110149.2)**
> Corresponding author: Diane E. Dickel (Octant, Inc.)
>
> Preprint: *bioRxiv*, posted **12 October 2025** (v2, **23 December 2025**),
> DOI **[10.1101/2025.10.11.681520](https://doi.org/10.1101/2025.10.11.681520)**
>
> Scores obtained from **MaveDB**: `urn:mavedb:00001270-a-*` (IFN-α signalling) and
> `urn:mavedb:00001271-a-1` (VAMP-seq protein abundance).

**This document contributes no new measurements.** It is a reanalysis of their data, combined with
structural data (PDB **4OLI**; AlphaFold 3 models generated in this project) and PyRosetta ΔΔG
computed here. Every phenotype number below is theirs.

**Relation to their own conclusions.** Howard et al. report that human variants protective against
autoimmune phenotypes act by *reducing TYK2 protein abundance*, and propose TYK2 degradation as a
therapeutic strategy. The interface effect described here is a distinct and partly opposing
observation: a set of variants that reduce abundance just as severely **yet do not reduce
signalling**, because the surviving protein appears to be de-repressed. If that holds, reduced
abundance is not by itself sufficient for the protective phenotype — *where* in the protein the
abundance is lost matters. Their paper also reports novel allosteric sites; the analysis here was
carried out independently, from a crystal-structure interface definition, and the two should be
cross-checked.

---

## 3. What "the interface" means here

The 26 residues with ΔSASA > 25 Å² at the JH2–JH1 interface of the TYK2 crystal structure **4OLI**:

> 579, 580, 582, 610, 637, 663, 664, 666, 672, 674, 728, 743, 744, 756, 900, 901, 921, 922, 923,
> 926, 980, 982, 983, 992, 993, 1033

These give **494 missense variants**, 491 of which carry all three DMS readouts.

The definition was made from a crystal structure, independently of any DMS or model data, so it is
not circular with respect to anything measured here. It is also **confirmed by the AlphaFold 3
models**: the median relative solvent accessibility of these residues rises by **+0.213** going
from the closed model to the open one — they are precisely the residues that become exposed when
JH1 is released.

### The DMS data

| | |
|---|---|
| source | Howard et al., *eLife* 2026 (see section 2) |
| system | HEK293T with endogenous TYK2 knocked out, STAT2 + IRF9 restored |
| signalling | barcoded luciferase on an 8× ISRE promoter, doxycycline-inducible TYK2, IFN-α2a at 1 or 100 U/mL |
| abundance | VAMP-seq — N-terminal GFP with a co-transcriptional BFP control, FACS-sorted on the GFP:BFP ratio |
| scale | 0 = wild type, **−0.352 = the nonsense median** (dead protein) |
| coverage used | 22,536 variants at 1 U/mL and 100 U/mL, 22,516 on abundance |

---

## 4. The primary observation

Thresholds are the global DMS deciles across all 22,536 variants.

| group | n | med IFN 1U | med IFN 100U | med abundance | %LOF 1U | %LOF 100U | %GOF | % bottom-quartile abundance |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **interface (26 res)** | **494** | **−0.026** | **−0.087** | **−0.297** | **8.1** | **5.1** | 9.5 | **68.8** |
| JH2+JH1 non-interface | 10,325 | −0.075 | −0.154 | −0.127 | 11.4 | 15.3 | 9.2 | 37.7 |
| JH2 non-interface | 5,244 | −0.060 | −0.122 | −0.107 | 10.3 | 12.4 | 10.2 | 30.5 |
| JH1 non-interface | 5,081 | −0.091 | −0.190 | −0.164 | 12.5 | 18.4 | 8.2 | 45.1 |
| FERM | 7,709 | −0.027 | −0.100 | −0.040 | 9.8 | 5.9 | 11.5 | 12.4 |
| all variants | 22,536 | −0.048 | −0.118 | −0.076 | 10.0 | 10.0 | 10.0 | 25.0 |

The interface median abundance of **−0.297** sits close to the **−0.352** nonsense anchor: the
typical interface mutant is nearly as depleted as a truncated protein. Yet its median signalling at
100 U/mL (**−0.087**) is *better* than the kinase-domain average (−0.154).

### Statistical tests against the domain-matched control

Interface residues all lie in JH2, JH1 or the linker, so the comparison is made against
non-interface residues **of the same domains** rather than the whole protein.

| comparison | interface | control | test | p |
|---|--:|--:|---|--:|
| median IFN-α 1 U/mL | −0.026 | −0.075 | Mann–Whitney, AUC 0.550 | 1.8e−04 |
| median IFN-α 100 U/mL | −0.087 | −0.154 | Mann–Whitney, AUC 0.550 | 1.6e−04 |
| **median abundance** | **−0.297** | **−0.127** | Mann–Whitney, **AUC 0.319** | **3.8e−42** |
| LOF at 1 U/mL | 8.1% | 11.4% | Fisher, OR 0.69 | 0.023 |
| **LOF at 100 U/mL** | **5.1%** | **15.3%** | Fisher, **OR 0.29** | **2.3e−12** |
| GOF at 1 U/mL | 9.5% | 9.2% | Fisher, OR 1.04 | 0.81 |

The abundance effect (p = 4e−42) is far stronger than either signalling effect, and the GOF row is
flatly null. The headline is the **sign conflict** between rows 3 and 5.

---

## 5. The effect is not explained by burial

Interface residues are buried, and buried residues are destabilizing, so the obvious objection is
that "interface" is just a proxy for "buried". It is not.

Median relative solvent accessibility in the closed model is **0.132** at the interface versus
**0.163** across JH2+JH1 — barely more buried. Repeating the comparison against a control matched
on burial (non-interface JH2/JH1 residues whose RSA falls in the interface's 5th–95th percentile
range, n = 5,253):

| group | n | med abundance | % bottom-quartile abundance | med IFN 100U | %LOF 100U | %GOF |
|---|--:|--:|--:|--:|--:|--:|
| interface | 491 | **−0.297** | **68.8** | −0.088 | **4.9** | 9.6 |
| burial-matched non-interface | 5,253 | −0.126 | 37.7 | −0.148 | 14.0 | 8.9 |
| all JH2/JH1 non-interface | 10,318 | −0.128 | 37.7 | −0.154 | 15.3 | 9.2 |

| test vs burial-matched control | result | p |
|---|--:|--:|
| abundance | AUC **0.312** | 3.1e−43 |
| IFN-α 100 U/mL | AUC 0.547 | 5.7e−04 |
| IFN-α 1 U/mL | AUC 0.546 | 7.2e−04 |
| LOF at 100 U/mL | 4.9% vs 14.0%, **OR 0.32** | 3.5e−10 |

Every effect survives at essentially full strength. Interface residues are destabilizing **far
beyond what their burial predicts**, and protected from signalling loss at the same time.

---

## 6. The mechanism: signalling is preserved only where protein is scarce

If interface mutants compensate for low abundance with higher activity per molecule, the advantage
should appear at low abundance and vanish at normal abundance. Splitting by abundance quintile
(bins defined on the control set):

| abundance quintile | n interface | n control | med IFN 1U (iface) | (control) | p | med IFN 100U (iface) | (control) | p |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **Q1 [−0.407, −0.320]** | **210** | 2,064 | **+0.015** | −0.172 | **5e−17** | **−0.071** | **−0.792** | **1e−44** |
| Q2 [−0.320, −0.183] | 131 | 2,063 | −0.036 | −0.073 | 0.25 | −0.072 | −0.145 | 0.013 |
| Q3 [−0.183, −0.088] | 64 | 2,064 | −0.027 | −0.049 | 0.51 | −0.214 | −0.077 | 0.008 |
| Q4 [−0.088, −0.032] | 45 | 2,063 | −0.043 | −0.029 | 0.15 | −0.086 | −0.046 | 0.14 |
| Q5 [−0.032, +0.079] | 41 | 2,064 | −0.074 | −0.050 | 0.73 | −0.117 | −0.078 | 0.43 |

**This is the clearest result in the analysis.** In Q1 — protein levels at or below the nonsense
anchor — non-interface kinase-domain mutants are essentially dead at 100 U/mL (**−0.792**), while
interface mutants at the *same* abundance signal near wild type (**−0.071**). The gap is **0.72
units**, more than twice the entire distance from wild type to the nonsense anchor, at p = 1e−44.

Above Q1 the effect collapses to nothing. The advantage exists only when protein is limiting,
which is what a specific-activity gain predicts and what a measurement artefact does not.

### Abundance-adjusted signalling

Fitting signalling on abundance in the control set and taking interface residuals:

| comparison | interface residual | control residual | p | AUC |
|---|--:|--:|--:|--:|
| IFN-α 1 U/mL, domain-matched control | +0.073 | −0.003 | 1.6e−08 | 0.575 |
| IFN-α 100 U/mL, domain-matched control | **+0.438** | +0.117 | 2.0e−38 | 0.673 |
| IFN-α 100 U/mL, **burial-matched** control | **+0.364** | +0.130 | 3.9e−25 | 0.641 |

---

### The same analysis at 1 U/mL

The effect is **present at 1 U/mL but about half the size**, and the reason is partly the assay and
partly real.

| test | **1 U/mL** | 100 U/mL |
|---|--:|--:|
| median interface vs control | −0.026 vs −0.075 | −0.088 vs −0.154 |
| Mann–Whitney p | 1.7e−04 | 2.1e−04 |
| **AUC** | **0.550** | **0.549** |
| LOF rate, interface vs control | 8.1% vs 11.4% | 4.9% vs 15.3% |
| odds ratio | **0.69** | **0.28** |
| Fisher p | 0.028 | 1.1e−12 |
| GOF rate, interface vs control | 9.6% vs 9.2% | 8.4% vs 9.9% |
| Fisher p | 0.75 | 0.28 |
| abundance-adjusted residual, domain-matched | **+0.073** vs −0.003 | **+0.438** vs +0.117 |
| p / AUC | 2e−08 / 0.575 | 2e−38 / 0.673 |
| **effect in SD units of that assay** | **0.23** | **0.51** |
| abundance-adjusted residual, burial-matched | +0.061 vs −0.003 | +0.364 vs +0.130 |
| p / AUC | 2e−06 / 0.565 | 4e−25 / 0.641 |
| **effect in SD units** | **0.20** | **0.37** |

Three things to read off this.

**1. The whole-distribution shift is identical at both doses.** AUC 0.550 at 1 U/mL against 0.549
at 100 U/mL. As a rank statistic over all interface variants, the effect does not depend on dose at
all.

**2. The LOF depletion is much weaker at 1 U/mL** — OR 0.69 (p = 0.028) against OR 0.28
(p = 1e−12) — and this part is largely an assay-range artefact. The 1 U/mL readout is **compressed
on the loss side**:

| | 1 U/mL | 100 U/mL |
|---|--:|--:|
| 1st percentile | **−0.857** | **−2.419** |
| 10th percentile | −0.447 | −0.999 |
| SD | 0.328 | 0.631 |
| nonsense median | −0.352 | −0.352 |

At 1 U/mL a dead protein scores −0.86 at worst; at 100 U/mL it falls to −2.42. With less room
between "working" and "dead", there is correspondingly less room for the interface to be *protected
from* falling. Note the nonsense anchor is −0.352 at both doses, so at 1 U/mL the bottom decile
(−0.447) already sits **below** the dead-protein anchor — the low-dose assay spends much of its
range on noise rather than on resolving degrees of failure.

**3. After normalising for that, roughly half the difference is real.** In SD units of each assay
the abundance-adjusted effect is **0.23 at 1 U/mL versus 0.51 at 100 U/mL** (0.20 vs 0.37 against
the burial-matched control). So compression explains part of the gap but not all of it.

The same holds in the lowest-abundance quintile, which is where the mechanism shows:

| dose | n iface | n control | med interface | med control | gap | **gap / SD** | p |
|---|--:|--:|--:|--:|--:|--:|--:|
| **1 U/mL** | 210 | 2,064 | **+0.015** | −0.172 | +0.187 | **0.57** | 5.2e−17 |
| **100 U/mL** | 210 | 2,064 | −0.071 | −0.792 | +0.722 | **1.14** | 1.1e−44 |

At 1 U/mL, interface mutants with near-dead protein levels still signal at **+0.015 — above wild
type** — while matched controls sit at −0.172. The effect is unambiguous (p = 5e−17); it is simply
half as large in normalised terms.

**Why the low dose should show it *less*, biologically.** At limiting ligand, signalling is
receptor- and ligand-limited rather than TYK2-limited, so having more active kinase per molecule
buys less. At saturating ligand the kinase step is closer to rate-limiting, so de-repression
translates more directly into output. That the effect is *larger* at saturating ligand is therefore
consistent with the specific-activity model rather than an embarrassment for it.

**The practical consequence is the opposite of section 52's.** For *predictors*, 1 U/mL is the
informative dose, because that is where activating variants appear and where every sequence tool
collapses to AUC ~0.60. For *this* effect, 100 U/mL is the informative dose, because it has the
dynamic range to show protection from loss. The two doses are not interchangeable and the better
one depends on the question.

---

## 7. Per-residue breakdown

All 26 residues. `RSA` is relative solvent accessibility in the AF3 closed model, `ΔRSA` the gain
on opening, `residual` the abundance-adjusted IFN-α 100 U/mL signal. p-values are Holm-corrected
across the 26 tests; **bold** residues are individually significant.

| residue | domain | n | RSA | ΔRSA | med abundance | % low ab | med IFN 100U | %LOF | residual | p (Holm) |
|---|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| **D921** | JH1 | 19 | 0.216 | +0.276 | -0.344 | 95% | +0.205 | 0% | **+0.760** | 1e-07 |
| **H582** | linker | 19 | 0.389 | +0.130 | -0.309 | 84% | +0.186 | 5% | **+0.695** | 0.0036 |
| **T923** | JH1 | 19 | 0.057 | +0.558 | -0.342 | 90% | +0.013 | 0% | **+0.606** | 2.8e-05 |
| R901 | JH1 | 19 | 0.219 | +0.221 | -0.323 | 95% | -0.033 | 10% | **+0.593** | 0.065 |
| **L637** | JH2 | 19 | 0.180 | +0.048 | -0.312 | 79% | +0.029 | 0% | **+0.577** | 0.001 |
| **K728** | JH2 | 19 | 0.176 | +0.177 | -0.333 | 95% | -0.072 | 0% | **+0.538** | 0.01 |
| **A743** | JH2 | 19 | 0.096 | +0.185 | -0.332 | 74% | +0.004 | 0% | **+0.519** | 0.046 |
| **I900** | JH1 | 19 | 0.102 | +0.355 | -0.307 | 74% | -0.000 | 0% | **+0.484** | 0.0061 |
| **R744** | JH2 | 19 | 0.162 | +0.242 | -0.367 | 100% | -0.123 | 0% | **+0.428** | 0.016 |
| V610 | JH2 | 19 | 0.102 | +0.258 | -0.226 | 68% | -0.049 | 5% | **+0.412** | 0.57 |
| **H674** | JH2 | 19 | 0.096 | +0.092 | -0.343 | 74% | -0.086 | 0% | **+0.394** | 0.033 |
| F672 | JH2 | 19 | 0.121 | +0.302 | -0.291 | 74% | -0.182 | 0% | **+0.378** | 0.36 |
| M926 | JH1 | 18 | 0.166 | +0.171 | -0.297 | 72% | -0.156 | 0% | **+0.372** | 0.065 |
| R992 | JH1 | 19 | 0.681 | +0.004 | -0.220 | 63% | -0.033 | 0% | **+0.366** | 0.27 |
| Q664 | JH2 | 19 | 0.030 | +0.180 | -0.159 | 47% | -0.106 | 0% | **+0.364** | 0.57 |
| Y980 | JH1 | 19 | 0.093 | +0.096 | -0.347 | 95% | -0.241 | 5% | **+0.360** | 0.57 |
| S666 | JH2 | 19 | 0.320 | +0.251 | -0.296 | 58% | -0.031 | 0% | **+0.345** | 0.1 |
| P982 | JH1 | 18 | 0.152 | +0.263 | -0.355 | 89% | -0.306 | 0% | **+0.297** | 0.39 |
| G922 | JH1 | 19 | 0.285 | +0.298 | -0.121 | 47% | -0.012 | 0% | **+0.285** | 0.57 |
| N1033 | JH1 | 19 | 0.091 | +0.237 | -0.269 | 74% | -0.168 | 0% | **+0.282** | 0.26 |
| S663 | JH2 | 19 | 0.138 | +0.130 | -0.149 | 42% | -0.108 | 0% | **+0.221** | 0.62 |
| L983 | JH1 | 19 | 0.121 | +0.205 | -0.211 | 58% | -0.243 | 0% | **+0.218** | 1 |
| H993 | JH1 | 18 | 0.126 | +0.226 | -0.112 | 17% | -0.055 | 0% | **+0.152** | 1 |
| K756 | JH2 | 19 | 0.028 | +0.131 | -0.355 | 95% | -0.574 | 21% | **+0.104** | 1 |
| S580 | linker | 19 | 0.077 | +0.306 | -0.064 | 10% | -0.315 | 16% | **-0.044** | 0.57 |
| **L579** | linker | 19 | 0.281 | +0.146 | -0.116 | 21% | -1.507 | 63% | **-1.281** | 1.3e-05 |
**10 of 26 residues are individually significant after correction**, and 24 of 26 have a positive
residual. The effect is distributed across the interface, not driven by one or two positions.

### Two residues worth singling out

**L579 is the exception that proves the rule.** It runs hard in the opposite direction: **63% of
its variants are loss-of-function** at 100 U/mL, residual **−1.281**, p = 1.3e−05 — and its
abundance is nearly normal (−0.116, only 21% in the bottom quartile). A residue that sits in the
interface footprint but destroys signalling without destabilizing the protein is behaving like a
catalytic or binding requirement rather than an autoinhibitory contact.

**H582 is the strongest activator in the entire DMS** (H582W, IFN-α 1 U/mL = **+1.339**) and
appears here as the second-ranked interface residue (residual +0.695, p = 0.0036). This analysis
independently recovers it from a structural definition, which is the kind of agreement that makes
the interface assignment credible.

---

## 8. What the physics says — and a negative result

If the abundance loss were ordinary thermodynamic destabilization, computed ΔΔG should predict it.
Using the 20,897-variant overnight ΔΔG set on the matched AF3 pair (sign convention
ΔΔG = ΔG_WT − ΔG_mut, so **negative = destabilizing**):

| group | n | median ΔΔG_closed | median ΔΔG_open − ΔΔG_closed | median abundance |
|---|--:|--:|--:|--:|
| interface | 397 | **−5.65** | **+0.65** | −0.296 |
| burial-matched non-interface | 4,962 | −4.88 | +0.00 | −0.127 |
| all JH2/JH1 non-interface | 9,628 | −4.62 | +0.00 | −0.129 |

| | |
|---|--:|
| ΔΔG_closed, interface vs burial-matched | AUC 0.470, p = 0.042 |
| ρ(ΔΔG_closed, abundance) **within the interface** | **+0.057** (n = 397) |
| ρ(ΔΔG_closed, abundance) within burial-matched control | **+0.234** (n = 4,962) |

**Computed stability does not account for the interface abundance deficit.** Interface variants are
only marginally more destabilizing than burial-matched controls (−5.65 vs −4.88, a weak effect at
p = 0.042), yet their abundance deficit is enormous (AUC 0.312, p = 3e−43). Worse, the normal
coupling between predicted stability and measured abundance **breaks down inside the interface**:
ρ falls from +0.234 to +0.057.

So the abundance loss is **not** simple unfolding of the monomer. Something specific to breaking
this interface removes the protein — plausibly exposure of a degron normally buried by JH1
docking, or degradation of the released JH1 lobe — and ΔΔG computed on a static model has no
representation for it.

One consistency check does land: interface mutations shift the ΔΔG difference toward open
(**+0.65** vs +0.00 elsewhere), the direction expected if they loosen JH2–JH1 packing. That is a
sanity check on the interface definition, not evidence for the difference feature, which carries no
predictive signal anywhere (AUC 0.500 at n = 20,897).

---

## 9. Why this matters

**For reading pathogenicity predictors.** Every sequence-based predictor scores these variants as
damaging, because they are destabilizing and sit at conserved buried positions — and on signalling,
which is the phenotype that matters clinically, they are *protective*. The interface is a region
where the predictors are confidently and systematically wrong about direction.

**For assay design.** An abundance screen and a signalling screen disagree maximally here. Reading
either alone gives the opposite answer about this interface. The dissociation is only visible when
both are measured on the same variants.

**For the autoinhibition model.** The pseudokinase domain JH2 holds JH1 inactive; breaking the
interface should release it. The DMS shows the predicted release — but as *specific activity*, not
as raw output, and only once abundance is accounted for. The interface is simultaneously
destabilizing and activating, and those two effects cancel in the raw signalling readout.

**For gain-of-function discovery.** This is the one place in TYK2 where the data show a coherent
activating mechanism, and **it is invisible to every method tried in this project**: six sequence
predictors (AUC < 0.5 for GOF), dual-state ΔΔG (AUC 0.499), MSA-subsampling openness, and the full
clustering pipeline all miss it. It only emerged by conditioning measured signalling on measured
abundance.

---

## 10. The decisive test, run — and the conformational interpretation fails it

*Added 26 October 2026, after extracting all 11 arms of the Howard et al. DMS
(`TYK2/DMS_Howard2026/`). Section 9 named this the single most valuable follow-up. It was run; the
result goes against the mechanism proposed above, and is reported here rather than set aside.*

### The prediction

**BMS-986202** and **NDI-034858** are allosteric TYK2 inhibitors that bind the **JH2 pseudokinase
domain**, not the ATP site. They act by *stabilising* the autoinhibited state — holding JH2 docked
onto JH1 — which is the same axis, in the opposite direction, as the interface mutations studied
here. (BMS-986202 is from the deucravacitinib series; NDI-034858 is zasocitinib.)

If interface mutations work by shifting the closed↔open equilibrium, they should shift sensitivity
to a drug that acts on that equilibrium. Each inhibitor arm is IFN-α 100 U/mL **plus** drug, so

> **drug effect = (signal with inhibitor) − (signal at 100 U/mL, no drug)**

More negative = more suppressed by the drug. Only the sub-saturating arms carry information: at
1 µM and 10 µM the nonsense median is ≈ 0, i.e. the drug flattens every variant.

### The measure works — positive controls

| check | result |
|---|--:|
| BMS 20 nM vs its duplicate assay | Pearson **+0.590** |
| BMS vs NDI — **different drugs** | Pearson **+0.543** |
| mean \|drug effect\|, JH2 (drug-binding domain) | **0.415** |
| mean \|drug effect\|, JH1 | 0.361 |
| JH2 vs JH1 | **p = 1.4e−16**, AUC 0.546 |

The top resistant positions are almost all in JH2 — 596, 671, 741, 640, 758, 759, 595, 796, 687 —
as are the most sensitive (599, 600, 700, 711, 811). The assay localises drug effects to the domain
the drugs bind.

### The interface shows nothing

Against the burial-matched control of section 5:

| comparison | interface | burial-matched control | p | AUC |
|---|--:|--:|--:|--:|
| BMS-986202 20 nM | +0.010 | +0.017 | 0.63 | 0.494 |
| BMS-986202 20 nM (duplicate) | +0.015 | −0.003 | 0.31 | 0.514 |
| NDI-034858 7 nM | −0.021 | −0.031 | 0.70 | 0.495 |
| mean \|drug effect\|, interface vs rest of JH2+JH1 | 0.361 | 0.358 | 0.11 | 0.479 |

Null in both drugs, in both replicates, by both tests.

**This is a clean negative, not an underpowered one.** The same measure, on the same variants,
detects JH2 drug-pocket effects at p = 1e−16 and detects nothing at the JH2–JH1 interface.

### What survives and what does not

**Survives.** The abundance/signalling dissociation itself is unaffected — it rests on the DMS
measurements of sections 3–6 and is independent of this test. Interface variants still lose
abundance severely (69% bottom-quartile vs 38%) while being depleted for loss of function (4.9% vs
15.3%), and still signal at −0.071 against −0.792 for matched controls in the lowest abundance
quintile (p = 1e−44).

**Does not survive.** The *interpretation* that this reflects a shifted closed↔open equilibrium.
That inference predicted a shift in allosteric-drug sensitivity, and the prediction failed.

Readings still compatible with all the data:

1. the interface effect is about **stability and degradation**, not conformational equilibrium —
   consistent with section 7, where computed ΔΔG fails to explain the abundance loss and the
   stability–abundance coupling breaks down inside the interface;
2. the equilibrium shift is real but **too small to change drug sensitivity** at 20 nM / 7 nM;
3. the drugs occupy a JH2 pocket whose binding is **largely independent of the JH2–JH1 docking
   state**, so the assay cannot see the equilibrium at all.

Distinguishing (1) from (2) and (3) needs direct measurement — a kinase assay on purified interface
mutants, or inhibitor dose–response on a handful of them — not more reanalysis of this dataset.

### A correction carried from this extraction

Each arm has its own nonsense anchor. **−0.352 is the abundance value**; the signalling anchors run
from −0.228 (1 U/mL) to −1.66 (100 U/mL). Section 2 and the dose discussion quote −0.352 as a
general "dead protein" line, which is right for abundance and wrong for the signalling arms. The
statement that the 1 U/mL bottom decile (−0.447) sits below the dead-protein line still holds, and
is in fact stronger against the correct anchor of −0.228.

---

## 11. Limitations, stated plainly

1. **VAMP-seq uses an N-terminal GFP tag** while the interface is C-terminal. If breaking the
   interface changes GFP maturation or accessibility rather than true protein level, the abundance
   deficit could be partly reporter artefact. Nothing here distinguishes those; an orthogonal
   abundance measurement (western blot, mass spectrometry) on a handful of interface variants would
   settle it, and is the single most valuable follow-up.
2. **The signalling assay is doxycycline-induced**, i.e. overexpression. Reserve capacity may mask
   abundance loss in a way that physiological expression would not, which would inflate the Q1
   effect.
3. **The specific-activity interpretation is inferred, not measured.** No per-molecule activity was
   determined; it is the hypothesis that fits the abundance-conditioned pattern. A direct kinase
   assay on purified interface mutants would test it.
4. **n = 494** interface variants versus 10,325 controls. Group-level effects are very well
   powered, but only 10 of 26 individual residues reach significance.
5. **Interface membership is from one crystal structure** (4OLI) at a ΔSASA > 25 Å² cut-off. A
   different structure or threshold would shift the set, though the AF3 ΔRSA agreement (+0.213)
   suggests the definition is robust.
6. **Causality is not established.** This is an association across 494 variants, consistent with
   the autoinhibition model but not a proof of it.
7. **The conformational interpretation failed its sharpest test** (section 10). Interface variants
   show no shift in allosteric-inhibitor sensitivity, in either drug, in either replicate, on an
   assay that detects JH2 drug-pocket effects at p = 1e-16. The measured dissociation stands; the
   equilibrium explanation for it does not.

---

## 12. Reproducing this

| file | contents |
|---|---|
| `data/orianne/tyk2_variants.csv` | 22,553 variants, all predictors and three DMS readouts |
| `data/ddg/ddg_TYK2_all.json` | 20,897 variants, dual-state ΔΔG on the matched AF3 pair |
| `data/orianne/iface_groups.json` | the group summaries of §3 |
| `data/orianne/iface_perresidue.json` | the per-residue table of §6 |
| `data/orianne/rsa_af3.json` | per-residue RSA in both AF3 models |
| `TYK2/af3/tyk2_af3_{closed,open}.pdb` | the two structures |

Related: `mutation_analysis.md` §52 (dose dependence), §55 (H582W), §56–60 (ΔΔG),
`mutations_clustering.md` (the clustering pipeline).
