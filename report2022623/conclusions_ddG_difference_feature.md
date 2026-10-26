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

---

## 9. Measured: the extreme values are 100% steric repulsion

*Added 25 October 2026. §8 inferred the clash explanation from residue-volume statistics and the
literature. This section measures it directly: PyRosetta 2026.39 installed on a fresh molab box,
same structure (`TYK2/af3/tyk2_af3_closed.pdb`), same protocol as `pipeline/ddg/worker.py`.
Script: [`pipeline/ddg/diagnose_clash.py`](pipeline/ddg/diagnose_clash.py); raw output:
[`data/ddg/clash_diagnosis.json`](data/ddg/clash_diagnosis.json).*

Three protocols on the same relaxed pose:

- **A** — the pipeline exactly: `mutate_residue(pack_radius=8.0)`, ΔΔG = E(WT repacked) − E(mut).
- **fa_rep** — the change in the weighted Lennard-Jones repulsive term alone, as a fraction of ΔΔG.
- **B** — A plus `MinMover` over backbone *and* side chains of the 8 Å shell, i.e. the backbone
  movement a repack-only protocol cannot provide.

Test set: the three most extreme positions in the merged results (746, 964, 801) and two ordinary
ones (667, 775).

| variant | pipeline | A (reproduction) | B (flexible bb) | ΔΔG that is `fa_rep` |
|---|--:|--:|--:|--:|
| G746W | −2988.6 | −3030.7 | **−106.2** | **100%** |
| G746F | −2901.6 | −2922.4 | −313.1 | 100% |
| G746A | −228.8 | −231.4 | −13.8 | 96% |
| G964W | −2724.0 | −2742.0 | **−47.6** | 100% |
| G964F | −2486.0 | −2487.8 | −107.0 | 100% |
| G964A | −148.9 | −149.7 | −7.7 | 98% |
| G801W | −3047.9 | −3059.6 | **−152.7** | 101% |
| G801F | −2204.1 | −2209.5 | −112.9 | 101% |
| G801A | −60.7 | −59.5 | −0.5 | 111% |
| H667F | −17.8 | −12.5 | −7.8 | 104% |
| H667A | −3.9 | −4.5 | −4.1 | — |
| R775W | +2.70 | +1.5 | +1.9 | — |
| R775A | +1.54 | +1.3 | −0.3 | — |

### What it shows

**1. The pipeline reproduces.** Pearson 0.947, Spearman **0.998** against the stored values; the
large magnitudes match to **0.1–2%**. The calculation does what the code says, on an independently
relaxed pose.

**2. The extreme values are entirely clash.** `fa_rep` accounts for ~100% of every large ΔΔG. They
are not energies with a large error — they are the repulsive term and nothing else. §4's reading
("a meaningless energy but a reliable statement that the substitution does not physically fit") is
confirmed as literally true.

**3. All three extreme positions are glycine**, and the damage scales with what replaces it:
G→W/F ≈ −2,200 to −3,060, G→A ≈ −60 to −230, a 10–50× difference at the same position. This is
the mechanism behind the r = −0.84 volume correlation in §8.1: mutating away from glycine in a
fixed backbone is the textbook case Flex ddG says requires backbone movement.

**4. Backbone flexibility removes 20–60× of it.** −3031 → −106, −2742 → −48, −3060 → −153.
With the documented ×2.94 REU→kcal/mol factor those land near −36 kcal/mol: severe, but physical.

**5. The ordering survives — which is why nothing in §1–§7 changes.** A vs B Spearman **0.904**.
The pipeline's design decision ("only the ordering is meaningful", README) is vindicated: the
amplitude is wrong, the rank is approximately right, and every result in this document is
rank-based.

**6. The extreme tail is also *noisy*, not merely inflated.** H667W scored −2246 here against
−435 in the stored run — a 5× spread from identical code, because repacking is stochastic and a
clashed rotamer is an unstable optimum. Ordinary positions reproduce within 1–2%. Error bars on
the tail are therefore large and position-dependent, another reason to rank rather than clip.

**7. The relaxed input still carries strain.** After the coordinate-constrained FastRelax,
residues 344–351 sit at 11–25 REU each. That is the "pre-optimise the input" failure mode from the
RosettaCommons thread in §8.2, localised to one loop.

### The gap, in one line

G746W scores **−2,989**. In the TYK2 DMS, position 746 has mean abundance **−0.31** and mean
signalling **−0.05** — the cells barely register it. A three-thousand-unit "energy" for a
substitution with no measured phenotype is the quantitative reason ΔΔG reaches AUC 0.704 on
abundance where AlphaMissense reaches 0.859 (§5).

### Reproducing

PyRosetta installs on molab with the project's own recipe (`pip install pyrosetta-installer`, then
`install_pyrosetta()`); the 2026.39 cp313 Ubuntu wheel works on the standard image. FastRelax of
the 1,187-residue pose takes ~35 min on one core, which is why `worker.py` caches it per box.
Commercial use of PyRosetta requires a licence; academic use is free.

---

## 10. Cross-check against Rosetta's own ddG application — the protocol is not at fault

*Added 25 October 2026. §9 showed the extreme values are pure `fa_rep` and that a mobile backbone
shrinks them 10-150x, which suggested the repack-only protocol was the cause. That suggestion was
**wrong**. Script: [`pipeline/ddg/compare_ddg_monomer.py`](pipeline/ddg/compare_ddg_monomer.py);
output: [`data/ddg/kellogg_ddg_monomer.json`](data/ddg/kellogg_ddg_monomer.json).*

`pyrosetta.rosetta.protocols.ddg.ddGMover` **is** `ddg_monomer` (Kellogg et al. 2011): it ramps the
repulsive term, minimises under coordinate constraints (`set_min_cst(True)`), restricts to the
neighbourhood, and takes the best of several decoys. It is the protocol §8.2 identified as the
remedy. Run on the same relaxed pose, 3 decoys per variant, ~6 min each:

| variant | pipeline ddG | ddGMover (REU) | ddGMover (kcal/mol, /2.94) |
|---|--:|--:|--:|
| **G746W** | -2988.6 | **+2832.2** | **963** |
| **G801W** | -3047.9 | **+1879.1** | **639** |
| G746A | -228.8 | +216.6 | 74 |
| **H667F** | -17.8 | **+6.1** | **2.08** |
| **R775A** | +1.5 | **+1.8** | **0.62** |

Rosetta's sign convention is the opposite of the paper's: **positive = destabilising** here.

### What this settles

**1. The pipeline is not buggy, and neither is PyRosetta.** Two independently written protocols -
`worker.py`'s repack-only approach and Rosetta's own ddG application - return the same magnitudes
on the same mutations. Combined with §9's independent reproduction of the stored values to 0.1-2%,
there is no implementation defect to find.

**2. For ordinary mutations the numbers are textbook.** H667F gives **2.08 kcal/mol** and R775A
**0.62 kcal/mol** - exactly where real ddG lives. The protocol works correctly; it does not fail
across the board.

**3. The split is between mutations, not between protocols.** Every extreme case is a **buried
glycine replaced by a bulky residue**. No standard ddG method rearranges the backbone enough to
accommodate a tryptophan in a glycine-sized pocket, so they all report the same thing: the
substitution does not fit, scaled by how deep the overlap goes. §9's 10-150x shrinkage under
shell minimisation reflects how far that particular minimiser could distort the structure, not a
convergence toward a true value.

**4. The values are still not energies.** 963 kcal/mol cannot destabilise a domain whose entire
folding free energy is 5-15 kcal/mol. These are **saturated "does not fit" flags** wearing the
units of an energy.

**5. One genuine protocol difference remains, and it is small.** On ordinary mutations the
repack-only protocol over-estimates by roughly 3x (H667F: 17.8 vs 6.1; R775A: 1.5 vs 1.8). That is
a modest, largely rank-preserving inflation - consistent with §5's AUC 0.733 and §9's Spearman
0.904.

### Correction to §8 and §9

§8.2 implied that a Cartesian/ramped protocol "would compress the -3,000 tail" and move the
abundance AUC toward the published pattern; §9 described protocol B's -100 to -300 as "severe, but
physical". Both are **superseded**: Rosetta's own ramped protocol does not compress the tail, and
no value in the hundreds is physical. What stands from those sections is the mechanism (the
magnitude is `fa_rep` at glycine positions, correlating with residue volume at r = -0.84) and the
conclusion that only the ordering may be used.

**The project's treatment was correct from the start.** `pipeline/ddg/README.md` already said "only
the ordering is meaningful, since the extreme values are clash artefacts rather than energies", and
§4 chose rank transforms over clipping. Three independent lines of evidence now support that: the
`fa_rep` decomposition (§9), the rank preservation across protocols (§9), and Rosetta's own
application agreeing with the pipeline (§10).

*Data: `data/ddg/ddg_TYK2_all.json`, `data/ddg/ddg_JAK1_all.json` (44,462 variants, both states).
Run-book: `data/ddg/RUNBOOK.md`. Context: `mutation_analysis.md` §56–60.*
