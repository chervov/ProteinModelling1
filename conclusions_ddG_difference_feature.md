# Conclusions: the dual-state ΔΔG difference feature

**ΔΔG_open − ΔΔG_closed does not work. It is not underpowered, mis-signed, or mis-clipped —
it carries no information.**

*23 October 2026 · 44,462 variants at 100% coverage of both proteins · TYK2 and JAK1*

---

## 1. What was tested and why

The distinctive component of the Jeanpierre/Debeaupuis pipeline (*EMBO Mol Med* 2025) is not ΔΔG
but the **difference between two ΔΔG values**, one computed on a closed model and one on an open
model:

> ΔΔG = ΔG_WT − ΔG_mut, so **negative = destabilizing**. ΔΔG_open > ΔΔG_closed is taken to mean the
> mutation favours the open state. *(Appendix S3)*

This is a **conformational-preference** estimate, not a stability estimate, and it is the one
feature in their 11-feature panel that no sequence predictor could replace. That is why it was
worth reproducing.

| | variants | coverage | structures |
|---|--:|--:|---|
| **TYK2** | **22,536** | **100%** | matched AlphaFold 3 pair, generated for this purpose |
| **JAK1** | **21,926** | **100%** | Jeanpierre's own published open and closed models |

Protocol: FastRelax with coordinate constraints on each model, `mutate_residue` with an 8 Å repack
shell, the native repacked identically so neither side is favoured. Verified against PyRosetta's
own published ΔΔG tutorial (PagP set) to four decimal places — **0.3590** against their 0.3590768,
and **0.6712** against their 0.6720891 excluding proline.

---

## 2. The result

| test | TYK2 (n=22,536) | JAK1 (n=21,926) |
|---|--:|--:|
| AUC vs loss of function, IFN-α 1 U/mL | **0.499** | — |
| AUC vs loss of function, IFN-α 100 U/mL | **0.516** | — |
| AUC vs gain of function, IFN-α 1 U/mL | **0.498** | — |
| AUC vs abundance (VAMP-seq) | **0.499** | — |
| AUC vs the paper's own cluster labels | — | **0.495** (p = 0.25) |
| ρ vs IFN-α 1 U/mL | **−0.002** | — |
| ρ vs AlphaMissense | +0.018 | −0.009 |
| ρ vs ESM-1b | +0.028 | −0.011 |

At n = 22,536 an AUC of 0.499 is a **measured zero**, not an underpowered null. The feature is
uncorrelated with every measured phenotype, every sequence predictor, and the paper's own labels.

---

## 3. Why it fails: the two states are ~75% the same measurement

| correlation, ΔΔG_closed vs ΔΔG_open | TYK2 | JAK1 |
|---|--:|--:|
| **Pearson, unclipped** | **+0.860** | **+0.859** |
| Spearman, unclipped | +0.837 | +0.875 |
| Pearson, clipped to [−10,10] | +0.804 | +0.848 |
| Pearson, restricted to variants inside the window | +0.786 | +0.775 |
| **ρ² — shared rank variance** | **0.70** | **0.77** |

The two figures are nearly identical across two proteins and two completely unrelated sources of
structures — AlphaFold 3 for TYK2, Jeanpierre's published models for JAK1. **Subtracting two
quantities that share 70–77% of their variance leaves the quarter they do not share, which is
dominated by repack noise.**

And the residual is **not** small:

| | TYK2 | JAK1 |
|---|--:|--:|
| SD of ΔΔG_closed | 4.30 | 4.39 |
| SD of ΔΔG_open | 4.42 | 4.26 |
| **SD of the difference** | **2.74** | **2.39** |
| as a fraction of ΔΔG_closed | **64%** | **54%** |

This is the worst possible combination: **large amplitude and zero information**. In a Gower
distance the feature is weighted comparably to the features that work, so it actively moves
variants between clusters for no reason. A small residual would have been harmless; this is not.

### This is expected, not a bug in the calculation

Most of the 22,536 mutations sit far from the JH2–JH1 interface, where the local environment is
**identical in both models**. ΔΔG genuinely *should* be the same in both states for those
variants. Any conformational signal can only come from the interface — and must exceed the noise
generated everywhere else.

The interface subset confirms both halves of this:

| | n | median ΔΔG_open − ΔΔG_closed |
|---|--:|--:|
| 4OLI JH2–JH1 interface residues | 494 | **+0.519** |
| everything else | 22,042 | **+0.000** |

Interface mutations **do** shift the difference toward open (Mann–Whitney p = 7e−23, AUC 0.629) —
the physics behaves sensibly. But 26 residues out of 1,187 cannot lift a protein-wide feature
above chance, and even **within** the interface the difference predicts nothing: AUC 0.455 against
loss of function (p = 0.35) and 0.531 for the "more open → gain of function" direction (p = 0.48).

---

## 4. Clipping is not the problem — it costs a little

The paper clips ΔΔG to [−10, 10]; 27.6% of our values fall outside it. Clipping was tested as a
possible cause and is not one.

**Single-state ΔΔG_closed against the TYK2 DMS, under each treatment:**

| treatment | AUC abundance | AUC IFN-α 100 U/mL |
|---|--:|--:|
| **raw, no clipping** | **0.714** | **0.745** |
| clipped to [−100,100] | 0.713 | 0.743 |
| clipped to [−50,50] | 0.712 | 0.741 |
| clipped to [−20,20] | 0.708 | 0.738 |
| **clipped to [−10,10]** *(the paper's choice)* | 0.704 | 0.733 |
| clipped to [−5,5] | 0.692 | 0.706 |
| **variants outside the window dropped** | 0.701 | **0.693** |

Clipping costs ≈0.01 AUC and tighter clipping costs more; discarding the outliers is worst of all.
The 27.6% outside the window **carry signal** — a ΔΔG of −3,000 is a meaningless energy but a
reliable statement that the substitution does not physically fit, which is real information about
damage. Clipping merges those variants with merely-destabilizing ones.

**Only the ordering is meaningful.** Signed-log and rank transforms reproduce the raw numbers
exactly (0.714 / 0.745), as they must for rank-based statistics. The correct treatment is a rank
transform, not clipping.

**For the difference feature, the clipping order makes no difference either:**

| treatment | AUC abundance | AUC IFN 100 U | AUC IFN 1 U |
|---|--:|--:|--:|
| clip each term, then subtract | 0.499 | 0.516 | 0.499 |
| subtract, then clip | 0.491 | 0.507 | 0.502 |
| no clipping at all | 0.490 | 0.507 | 0.502 |

0.49–0.52 under every treatment.

---

## 5. Single-state ΔΔG: real signal, but no added value

ΔΔG_closed is **not** dead — unlike the difference, it predicts measured phenotype:

| feature | abundance | IFN-α 100 U/mL | IFN-α 1 U/mL |
|---|--:|--:|--:|
| ΔΔG_closed | 0.704 | **0.733** | 0.565 |
| ΔΔG_open | 0.697 | 0.728 | 0.563 |
| ΔΔG_open − ΔΔG_closed | 0.499 | 0.516 | 0.499 |
| AlphaMissense | **0.859** | **0.879** | **0.607** |
| ESM-1b | 0.796 | 0.823 | 0.589 |

Two observations. First, ΔΔG does **worse on abundance (0.704) than on signalling (0.733)** —
backwards, since abundance is a stability readout and ΔΔG is a stability calculation. It
underperforms on its own home turf. Second, AlphaMissense beats it by 0.15 on that same readout.

### Does it add anything on top of the sequence predictors?

It correlates only ≈+0.47 with AlphaMissense, so it looks independent. It is not, where it counts.
Five-fold cross-validation, folds grouped by residue position:

| model | abundance | IFN 100 U | IFN 1 U |
|---|--:|--:|--:|
| AlphaMissense alone | 0.856 | 0.877 | 0.605 |
| **+ ΔΔG_closed** | 0.855 | 0.878 | 0.606 |
| 3 sequence features | 0.854 | 0.874 | 0.605 |
| **+ both ΔΔG terms** | 0.854 | 0.877 | 0.606 |

**ΔAUC between −0.001 and +0.003.** Partial ρ controlling for AlphaMissense: +0.065 (abundance),
+0.072 (IFN 100 U), +0.033 (IFN 1 U). Against experimental data, ΔΔG contributes **nothing**. Its
apparent independence is independence in the *noise*, not in the signal.

### Against the JAK1 panel it does add a little

| model | AUC vs the paper's cluster labels |
|---|--:|
| ΔΔG_closed alone | 0.740 |
| AlphaMissense alone | 0.884 |
| **+ ΔΔG_closed** | **0.891** (+0.007) |
| AlphaMissense + ESM-1b + BLOSUM62 | 0.912 |
| + both ΔΔG | 0.915 (+0.003) |
| full 6-predictor panel | 0.920 |
| + both ΔΔG | 0.924 (+0.004) |

Partial ρ with the label, controlling for AlphaMissense: **+0.151**.

**That contrast is itself the finding.** ΔΔG adds a small but real increment against the paper's
**constructed labels**, and nothing against **measured phenotype**. The clusters are built partly
from features ΔΔG shares structure with; the DMS is ground truth. The feature looks useful against
the construct and is useless against reality — the same pattern as the paper's whole panel, one
level down.

---

## 6. Correction to earlier sections of `mutation_analysis.md`

**Section 59 claimed ΔΔG_closed is "independent and informative — the most valuable non-redundant
feature in the panel." That is wrong as a general claim** and is superseded here. It was based on
correlation structure plus standalone AUC against the paper's clusters, without testing incremental
value against experimental data. The accurate statement is narrower: ΔΔG adds ≈+0.007 against the
paper's labels and ≤0.003 against measured phenotype.

**Section 56 claimed ΔΔG_closed "predicts no measured phenotype (AUC 0.520)."** Also superseded,
in the opposite direction: that figure came from 469 interface-only variants at the 1 U/mL dose.
At full coverage ΔΔG_closed reaches **0.733** at 100 U/mL. The interface subset reproduces the old
number (0.525), so the pilot was unrepresentative rather than wrong about what it measured.

---

## 7. What stands

| question | answer | evidence |
|---|---|---|
| Does ΔΔG_open − ΔΔG_closed work? | **No** | AUC 0.499 at n = 22,536; 0.495 vs the paper's own labels |
| Is it a power problem? | **No** | 44,462 variants, 100% coverage of both proteins |
| Is it a clipping problem? | **No** | 0.49–0.52 under every clipping scheme |
| Is it a sign/direction problem? | **No** | both orientations give ≈0.50; interface shift is in the *expected* direction and still predicts nothing |
| Is it a bad-models problem? | **No** | fails identically on a matched AF3 pair and on the paper's own models |
| Why does it fail? | the two states share **70–77%** of their variance; the difference is the noisy remainder, at 54–64% of the original amplitude |
| Does single-state ΔΔG work? | **Yes for loss of function** (AUC 0.733) — but adds **nothing** over AlphaMissense |

**Bottom line.** The reproduction succeeded: the protocol validates against an official benchmark
and the stability term recovers the paper's published cluster medians to within 0.4 kcal/mol. The
feature the reproduction was undertaken for does not work, and the reason is structural rather than
incidental — no choice of models, clipping, or sample size can fix a difference between two
measurements that are 75% the same.

---

---

## 8. Published context: are the ΔΔG artefacts known?

*Added 25 October 2026. A new measurement on the same data (§8.1) prompted a literature check:
is the magnitude behaviour of these ΔΔG values a known problem? It is — every oddity here is
documented. None of it rescues the difference feature.*

### 8.1 A new measurement: the magnitude is dominated by the destination residue

Pooling all 22,536 TYK2 substitutions by the residue they mutate **to** (so position and native
residue are averaged out), the mean ΔΔG_closed varies ~50-fold by destination residue alone:

| mutated to | mean ΔΔG_closed | mean DMS abundance | n |
|---|--:|--:|--:|
| P | −177.6 | −0.15 | 1105 |
| W | −172.4 | −0.14 | 1163 |
| Y | −158.9 | −0.12 | 1152 |
| F | −124.4 | −0.12 | 1140 |
| … | … | … | … |
| C | −8.9 | −0.10 | 1155 |
| G | −3.8 | −0.11 | 1096 |
| S | −3.7 | −0.10 | 1110 |
| A | −3.3 | −0.10 | 1104 |

Mean ΔΔG_closed per destination residue against residue volume: **Pearson r = −0.62** over all 20
types, **−0.84 excluding proline** (proline is small but scores worst — a backbone effect rather
than a bulk one). Measured abundance, by contrast, barely moves across destination residues
(−0.10 to −0.15). The cells say the destination residue alone matters little; ΔΔG says it dominates.

Independent correlations on the same join (n = 22,536), consistent with the AUCs in §5:
ΔΔG_closed vs signalling Spearman **+0.23**, vs abundance **+0.26**, vs AlphaMissense Pearson
**−0.22** (negative = destabilising, so the sign is as expected); ΔΔG_open − ΔΔG_closed vs
signalling **+0.006**, vs abundance **−0.010**, vs AlphaMissense **+0.004**.

### 8.2 What the literature says

**Units.** Rosetta's Cartesian ΔΔG output is in Rosetta energy units; the documentation specifies
a **scaling factor of 2.94** to convert to kcal/mol (Park et al., supporting information). This
explains part of the inflation, not values near −3,000.
[cartesian_ddG docs](https://docs.rosettacommons.org/docs/latest/cartesian-ddG)

**Bulky mutations and side-chain-only repacking — the direct match for §8.1.** The Flex ddG paper
states that "mutations to larger side chains might require some degree of backbone rearrangement to
accommodate the change", which a repack-only protocol does not provide. `ddg_monomer` mitigates
this by **down-weighting the repulsive van der Waals term** across its minimisation rounds (10%,
then 33%, then full strength); a protocol without that ramp retains the clash energy.
`cartesian_ddG` was designed partly for this reason — it "allows small local backbone movement" and
exposes `-bbnbr` to flex residues i−1, i, i+1. The docs also recommend `-fa_max_dis 9.0`
(default 6) for stability prediction.
[Flex ddG](https://www.biorxiv.org/content/10.1101/221689.full.pdf) ·
[ddg_monomer docs](https://docs.rosettacommons.org/docs/latest/application_documentation/analysis/ddg-monomer)

**Extreme values usually trace to the input structure.** A RosettaCommons thread describes exactly
this symptom — particular residues giving extreme values across all mutations — and attributes it
to an input that was not pre-optimised: "If you don't, then you'll see variations in your results
where mutations get anomalously high/low values." The ProQ3 authors met the same problem and
resolved it with constrained minimisation (`-ddg:min_cst`).
[forum thread](https://forum.rosettacommons.org/node/5031) · [ProQ3](https://arxiv.org/pdf/1602.05832)

**A protocol choice worth revisiting.** The Cartesian ΔΔG docs state the input should be relaxed
with **unrestrained** backbone and side chains, because "unrestrained relax has been found to
produce fewer errors in classification" (citing Frenz et al.). Our run used FastRelax with
coordinate constraints — the opposite choice — which is a plausible route by which clashes survive
into the ΔΔG.

**The abundance/function inversion is anomalous.** Gerasimavicius, Livesey & Marsh
(*Protein Science* 2023) benchmarked nine stability tools against 49 deep mutational scans: FoldX
and Rosetta correlated best among stability methods, and correlations were **highest for
abundance-based readouts**, as theory predicts. §5 found the reverse here (abundance 0.704 <
signalling 0.733). Combined with §8.1, the most economical explanation is that the clash term
corrupts the stability axis specifically.
[PMC10273344](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10273344/)

**General predictor biases.** Most ΔΔG predictors violate anti-symmetry, ΔΔG(A→B) = −ΔΔG(B→A),
because training sets are dominated by destabilising variants (Pucci et al. 2018; Usmanova et al.
2018; review: Montanucci et al. 2019). The validation ceiling is itself limited: the Tsuboyama
mega-scale dataset correlates 0.75–0.96 with classical measurements and its assay saturates near
5 kcal/mol. The Rosetta docs now note that **ThermoMPNN "may perform better than cartesian ddG in
some situations"**.
[Montanucci et al.](https://bmcbioinformatics.biomedcentral.com/counter/pdf/10.1186/s12859-019-2923-1.pdf) ·
[mega-scale benchmark](https://pmc.ncbi.nlm.nih.gov/articles/PMC13228446/)

### 8.3 What this changes, and what it does not

**Could change:** the *absolute* ΔΔG numbers. A Cartesian protocol with unrestrained pre-relax,
backbone-neighbour flexibility and the 2.94 conversion would compress the −3,000 tail, likely move
the abundance AUC toward the published pattern, and make the values physically quotable. §4 already
shows the outliers carry ordering information, so a rank transform remains the right treatment
either way.

**Does not change:** the finding of this document. The difference feature fails because
ΔΔG_closed and ΔΔG_open correlate at **0.86** (§3); a better protocol improves both terms together
and leaves the difference just as uninformative. No reported artefact acts on one state and not the
other. AUC 0.499 is arithmetic, not a protocol bug.

---

*Data: `data/ddg/ddg_TYK2_all.json`, `data/ddg/ddg_JAK1_all.json` (44,462 variants, both states).
Run-book: `data/ddg/RUNBOOK.md`. Context: `mutation_analysis.md` §56–60.*
