# ΔΔG prediction: surveys, benchmarks and methodological pitfalls

*Compiled 28 October 2026 for the ddG-at-scale groundwork. Companion to the datasets memo
(`ddg_precomputed.md`), which covers training/benchmark data and is not repeated here.*

**How to read the numbers.** Every metric below is tagged **[IND]** (measured by an independent
group that did not author the ranked methods) or **[SELF]** (reported by the authors of the
method that wins). All DOIs in this document were resolved against the CrossRef API on
28 Oct 2026: **33 distinct DOIs are cited below and all 33 resolved** (38 were checked in total
during the survey; the 5 that are not cited were dropped after reading). Numbers were taken from
full text retrieved via PMC or Unpaywall,
not from recollection; where a value exists only inside a figure panel or supplementary table
that was not retrievable, this is stated rather than guessed.

---

## 0. The one-paragraph answer

On genuinely unseen single-point mutations, the best ΔΔG predictors reach **Pearson r ≈ 0.5–0.6**,
not the 0.7–0.8 that method papers advertise, and the gap is almost entirely explained by three
artefacts: evaluation on mutations that were in the training set, evaluation on direct-plus-reverse
pairs (which rewards antisymmetry rather than accuracy), and random rather than homology-aware
splits. An independent theoretical analysis puts the ceiling imposed by experimental noise at
**r ≈ 0.7–0.8**, so reported correlations above that range should be read as evidence of
overtraining, not of progress ([10.1093/bioinformatics/bty880](https://doi.org/10.1093/bioinformatics/bty880) [IND]).
For the specific job of interpreting human missense variants, ΔΔG is a **weak** classifier
(best AUC ≈ 0.66–0.68) because a large minority of pathogenic variants do not act by
destabilisation at all. AlphaFold models **are** acceptable inputs; AlphaFold's own pLDDT is not a
ΔΔG proxy. There is **no benchmark at all** on large multi-domain proteins.

---

## 1. Independent benchmarks and assessments

### 1.1 Comparison table

Pearson *r* unless stated. "Direct" = wild-type→mutant as measured; "reverse/inverse" =
mutant→wild-type; "total" = both pooled.

| # | Assessment | Year | DOI | Ind.? | Data | What was compared | Headline result |
|--|---|--|---|--|---|---|---|
| 1 | Pancotti et al., *Brief. Bioinform.* — the S669 blind set | 2022 | [10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555) | **[IND]** | S669: 669 variants from proteins <25 % identity to S2648 + VariBench; plus Ssym+ (704) | 21 tools, structure- and sequence-based | **Direct-only r = 0.22–0.50** (best MAESTRO 0.50, then ACDC-NN 0.46). **Reverse r = −0.01–0.45.** **Total r = 0.26–0.62** (PremPS 0.62, ACDC-NN 0.61, INPS-Seq 0.61). Best RMSE 1.49 kcal/mol (PremPS); Rosetta RMSE 2.69. All methods compress predictions toward zero; stabilising variants hardest |
| 2 | Zheng et al., *Protein Sci.* | 2023/24 | [10.1002/pro.4861](https://doi.org/10.1002/pro.4861) | **[IND]** | New 4,038-mutation set from ThermoMutDB + FireProtDB + ProThermDB, non-overlapping with S2648, **>1,000 stabilising** | **27 methods**, incl. mega-scale/transfer-learning era | **r = 0.20–0.53 on unseen data.** *None* of the 27 predicted stabilising mutations accurately — including methods that score well on antisymmetry. Authors conclude fixing training-set imbalance alone will not fix this |
| 3 | Pucci et al., *Bioinformatics* — the Ssym balanced set | 2018 | [10.1093/bioinformatics/bty348](https://doi.org/10.1093/bioinformatics/bty348) | **[IND]** | **Ssym**, built here: equal stabilising/destabilising, WT *and* mutant crystal structures ≤2.5 Å | 15 predictors, direct vs inverse | Collapse on the independent (inverse) half: MUPRO r 0.79→0.07, STRUM 0.75→−0.15, AUTOMUTE 0.73→−0.01, iSTABLE 0.72→−0.08, I-Mutant3.0 0.62→−0.04. Least-biased: PoPMuSiC<sup>sym</sup> 0.48/0.48, ⟨δ⟩ 0.03. Best inverse among pre-existing tools: Rosetta 0.43, FoldX 0.39 |
| 4 | Usmanova et al., *Bioinformatics* — self-consistency | 2018 | [10.1093/bioinformatics/bty340](https://doi.org/10.1093/bioinformatics/bty340) | **[IND]** | Crystal structures only — **no experimental ΔΔG needed** | FoldX, Eris, Rosetta, I-Mutant; bias as a function of number of mutations introduced | All four carry an inherent bias that accumulates with mutation count. FoldX's bias was substantially reduced by an extra Modeller relaxation step |
| 5 | Fang, *Brief. Bioinform.* — critical review | 2019 | [10.1093/bib/bbz071](https://doi.org/10.1093/bib/bbz071) | **[IND]** | Hypothetical reverse mutations | 5 representative ML algorithms | **All five overfit.** Diagnosed causes: too few training cases, insufficiently informative features. (Rebuttal/response: [10.1093/bib/bbz168](https://doi.org/10.1093/bib/bbz168) — see §4 of this report for the disagreement) |
| 6 | Marabotti et al., *BMC Bioinformatics* | 2021 | [10.1186/s12859-021-04238-w](https://doi.org/10.1186/s12859-021-04238-w) | **[IND]** | — | 5 recent web servers | Still "far from ideal"; destabilising bias; **predictions unreliable inside ΔΔG ±0.5 kcal/mol**; a consensus of several tools is a crude but effective improvement |
| 7 | Thiltgen & Goldstein, *PLoS ONE* — the original self-consistency idea | 2012 | [10.1371/journal.pone.0046084](https://doi.org/10.1371/journal.pone.0046084) | **[IND]** | — | — | Origin of the δ = ΔΔG<sub>dir</sub> + ΔΔG<sub>inv</sub> bias statistic later used by Pucci and Pancotti (full text retrieved; specific per-tool values not re-extracted here) |
| 8 | Akdel et al., *Nat. Struct. Mol. Biol.* — AF2 community assessment | 2022 | [10.1038/s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w) | **[IND]** | 2,648 single-point mutations from ThermoMutDB (legend says 121 proteins, Methods says 132 — an internal inconsistency in the paper) | **11 methods × {AF2 model, experimental structure, homology models at 20–90 % identity}** | ΔΔG from **AF2 models ≈ experimental structures**. Homology models degrade substantially **below 40 % template identity**. See §3 |
| 9 | Nielsen/Stein/Lindorff-Larsen, *CSBJ* | 2022 | [10.1016/j.csbj.2022.11.048](https://doi.org/10.1016/j.csbj.2022.11.048) | **[IND]** | 4 proteins with many measured ΔΔGs, templates across an identity range | 3 ΔΔG methods on crystal vs homology models | Homology models substitute for crystal structures **if template identity ≥40 %**; Rosetta `cartesian_ddg` is the most robust to modelling perturbation. Independently reproduces #8's 40 % threshold |
| 10 | Tsishyn/Pucci/Rooman, *Bioinformatics* — RSALOR | 2025 | [10.1093/bioinformatics/btaf322](https://doi.org/10.1093/bioinformatics/btaf322) | **[IND]** for the baseline comparison | ProteinGym, ~700,000 single-site mutations, 218 DMS datasets; **AlphaFold structures** | A 2-feature baseline (log-odds ratio × relative solvent accessibility) vs 27 predictors incl. 19 pLMs | On the **Stability** slice: ProSST-2048 0.638, SaProt 0.565, **RSALOR 0.551**, ESM2-650M 0.496, **−RSA alone 0.480**, conservation alone 0.447, TranceptEVE 0.424. Spearman. A two-feature model beats most deep models |
| 11 | ProteinGym (Notin et al.) | 2023 | [10.1101/2023.12.07.570727](https://doi.org/10.1101/2023.12.07.570727) | **[IND]** (benchmark authors ≠ most ranked methods) | 217 substitution DMS assays / 2.4 M mutants; 66 indel assays; 2,525-gene clinical set | 70+ models, zero-shot and supervised | Zero-shot DMS-wide Spearman: GEMME 0.457, TranceptEVE-L 0.457, EVE 0.441, ESM-IF1 0.422, ProteinMPNN 0.258. **Supervised split effect: a one-hot baseline scores 0.579 on random splits but 0.064 on contiguous splits**; ProteinNPT 0.730 random vs 0.547 contiguous |
| 12 | Dieckhaus et al., *PNAS* — ThermoMPNN | 2024 | [10.1073/pnas.2314853121](https://doi.org/10.1073/pnas.2314853121) | **[SELF]** | Mega-scale + FireProt splits (>25 % identity filtered), Ssym, S669 | ThermoMPNN vs Rosetta, RaSP, PROSTATA | Ssym direct **PCC 0.72**, inverse **0.60**; **S669 PCC 0.43**. Mega-scale Spearman 0.725 vs 0.487 for pretrained ProteinMPNN alone. Authors note Stability Oracle reported 0.72/0.72 on Ssym but code was unavailable to check |
| 13 | Li & Luo, *Nat. Commun.* — SPURS | 2025 | [10.1038/s41467-025-67609-4](https://doi.org/10.1038/s41467-025-67609-4) | **[SELF]** | 10 independent test sets (Ssym-dir/inv, S669, S2648, S783, S4611, S8754, FireProt-HF, …), >25 % identity excluded | SPURS vs FoldX, Rosetta, PROSTATA, RaSP, Stability Oracle, ThermoNet, ThermoMPNN | Significantly higher or comparable Spearman/Pearson on **7/8** test sets; better precision *and* recall than ThermoMPNN at prioritising the 1,178 stabilising vs 27,139 destabilising mega-scale test mutations. **Per-dataset values are in Fig. 2e and Supplementary Tables 1–3, which were not in the retrieved text — the specific correlations are therefore not quoted here** |
| 14 | Dieckhaus & Kuhlman, *Protein Sci.* — double mutants | 2024 | [10.1002/pro.70003](https://doi.org/10.1002/pro.70003) | mixed (same group as ThermoMPNN, but the finding is negative about their own field) | Largest available double-point-mutation stability set | Additive vs epistasis-aware models | **Simple additive models match epistasis-aware predictors on most metrics.** Neither AI- nor physics-based models consistently capture epistasis; epistasis-aware models help only marginally, and only on stabilising doubles |

### 1.2 What actually came out on top

Across the independent assessments the recurring winners are not the newest models:

1. On **S669** (the hardest single-point blind set): PremPS, ACDC-NN, INPS-Seq, DDGun3D — a
   mixture of a statistical-potential method, two antisymmetric neural networks and an
   *untrained* baseline.
2. On **Ssym inverse** (the only truly held-out half of that set): PoPMuSiC<sup>sym</sup>,
   Rosetta, FoldX — i.e. the physics-based tools, because they are not fitted to the
   destabilising-dominated databases.
3. On **pathogenicity discrimination**: FoldX, then Rosetta
   ([10.1038/s41598-020-72404-w](https://doi.org/10.1038/s41598-020-72404-w),
   [10.1002/pro.4688](https://doi.org/10.1002/pro.4688)) [IND].
4. On **mega-scale-era ΔΔG regression**: ThermoMPNN and SPURS, but only on mega-scale-derived
   test data; ThermoMPNN's own S669 number (0.43) sits inside the 0.22–0.50 direct-only band that
   Pancotti measured for the previous generation.

**The practical reading:** DDGun/DDGun3D ([10.1186/s12859-019-2923-1](https://doi.org/10.1186/s12859-019-2923-1),
[10.1093/nar/gkac325](https://doi.org/10.1093/nar/gkac325)) is untrained and antisymmetric by
construction, and lands within ~0.04 Pearson of the best trained methods on S669. It is the right
sanity-check baseline: if a sophisticated pipeline cannot beat it on your data, the extra
complexity is buying nothing.

---

## 2. Failure modes, each with the paper that established it

### 2.1 Antisymmetry violation — ΔΔG(A→B) ≠ −ΔΔG(B→A)

**Established by:** Thiltgen & Goldstein 2012 ([10.1371/journal.pone.0046084](https://doi.org/10.1371/journal.pone.0046084)),
then quantified in the paired 2018 papers Pucci et al.
([10.1093/bioinformatics/bty348](https://doi.org/10.1093/bioinformatics/bty348)) and Usmanova et al.
([10.1093/bioinformatics/bty340](https://doi.org/10.1093/bioinformatics/bty340)) — published
alongside each other, each explicitly cross-referencing the other.

Thermodynamics requires ΔΔG<sub>A→B</sub> = −ΔΔG<sub>B→A</sub>. Pucci measured
r<sub>dir,inv</sub> (should be −1) and ⟨δ⟩ = ΔΔG<sub>dir</sub> + ΔΔG<sub>inv</sub> (should be 0)
for 15 tools. Black-box ML methods were worst: AUTOMUTE ⟨δ⟩ = −0.99, MUPRO −0.97, mCSM −0.91,
STRUM −0.87, DUET −0.84 kcal/mol — i.e. they predict *destabilising* in both directions, by about
1 kcal/mol on average. Usmanova's protocol is the more useful operationally because it needs
**only structures, no experimental ΔΔG**, so it can be run on your own targets.

**Practical consequence:** you can audit any predictor on your own proteins for free, by scoring
A→B and B→A and checking that the sum is near zero. Do this before trusting a tool on a new
protein family. Note also the trap in reading benchmark tables: the "total" column in S669 is
computed over direct **and** reverse variants, so an antisymmetric method automatically scores
higher there (PremPS 0.62 total vs 0.41 direct). **Quote direct-only numbers when comparing to
your own single-direction predictions.**

### 2.2 Homology leakage and dataset overlap

**Established by:** Sanavia et al. 2020 review ([10.1016/j.csbj.2020.07.011](https://doi.org/10.1016/j.csbj.2020.07.011)),
which lists "over-optimistic prediction performance, due to sequence similarity between proteins
used in training and test datasets" as one of four core issues; demonstrated concretely by
Pucci ([10.1093/bioinformatics/bty348](https://doi.org/10.1093/bioinformatics/bty348)), who notes
the Ssym direct mutations "belong to the training dataset of the methods tested, so that the
predictions are likely to be overfitted" — and then shows r dropping from 0.79 to 0.07 on the
held-out inverse half. Fang 2019 ([10.1093/bib/bbz071](https://doi.org/10.1093/bib/bbz071)) reaches
the same conclusion for five ML algorithms. Dataset-dependency specifically:
[10.1021/acs.jcim.0c00591](https://doi.org/10.1021/acs.jcim.0c00591) (title/abstract verified via
CrossRef; full text not retrieved).

The cleanest modern quantification of **split choice** is ProteinGym's supervised table: a
one-hot-encoding model with no biology in it at all scores Spearman **0.579** under random splits
and **0.064** under contiguous splits — a ~9× inflation produced purely by how the split was drawn
([10.1101/2023.12.07.570727](https://doi.org/10.1101/2023.12.07.570727)).

**Practical consequence:** S2648, S669 and Ssym are *not* independent of each other in the way
their names suggest. S669 was explicitly constructed from proteins with **<25 % sequence identity
to S2648 ∪ VariBench**, which is why it is the valid blind set — but Ssym's *direct* half overlaps
the training data of nearly every pre-2020 tool. Use the published homology-filtered splits
(ThermoMPNN's `dataset_splits/`, FireProt-HF) rather than redrawing your own.

### 2.3 Destabilising-mutation class imbalance

**Established by:** Pucci et al. 2018 ([10.1093/bioinformatics/bty348](https://doi.org/10.1093/bioinformatics/bty348))
— curated databases are "dominated by destabilizing mutations", causing predictions to be better
for destabilising than stabilising mutations. Confirmed independently on a purpose-built set with
>1,000 stabilising mutations by Zheng et al. ([10.1002/pro.4861](https://doi.org/10.1002/pro.4861)):
**none** of 27 methods predicted stabilising mutations accurately.

**Where the literature disagrees:** Pucci's prescription is to rebalance (or impose antisymmetry
structurally, as in PoPMuSiC<sup>sym</sup>). Two later independent papers argue imbalance is *not*
the primary cause. Yang et al. 2023 ([10.1371/journal.pone.0283727](https://doi.org/10.1371/journal.pone.0283727))
build a balanced set and show, with leave-one-protein-out validation, that good cross-validation
numbers on a balanced set still do not demonstrate robustness — pointing instead at data quality
and uninformative features. Zheng et al. ([10.1002/pro.4861](https://doi.org/10.1002/pro.4861))
state directly that "solely addressing training dataset bias may not significantly enhance
accuracy of predicting stabilizing mutations". Pancotti
([10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555)) adds that even methods that are
antisymmetric *by construction* still fail on stabilising variants — so the architectural fix does
not fix the accuracy problem either. **Treat "we rebalanced our training set" as insufficient
evidence of fitness for stabilising-mutation work.**

### 2.4 Sign and convention confusion

**Established by:** Sanavia et al. 2020 ([10.1016/j.csbj.2020.07.011](https://doi.org/10.1016/j.csbj.2020.07.011)),
which spells out that ΔΔG<sub>u</sub> = ΔG<sub>u</sub><sup>mut</sup> − ΔG<sub>u</sub><sup>wt</sup>
(negative = destabilising) and the opposite convention ΔΔG<sub>f</sub> are both in use, and that
"it is crucial to specify which definition is adopted".

This is not hypothetical. In building S669, Pancotti et al. started from 900 ThermoMutDB variants,
**excluded ~24 %** for annotation inconsistencies (free energies that were actually transition-state
kinetics or binding affinities, multiple variants recorded as single, etc.), and then **changed the
value or the sign for ~20 % of the remaining 669** because "the sign of the ΔΔGs was not coherent
or because the values were imprecise" ([10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555)).
That is a ~44 % touch rate on a curated database by careful manual re-reading of the primary
literature.

Conventions also differ between modern papers: SPURS defines stabilising as ΔΔG < −0.5 kcal/mol
([10.1038/s41467-025-67609-4](https://doi.org/10.1038/s41467-025-67609-4)) while the S669/ThermoMutDB
lineage treats negative ΔΔG<sub>u</sub> as destabilising.

**Practical consequence:** fix the sign convention **per file**, empirically, before merging
anything. The cheap check: proline substitutions in helices and buried hydrophobic→charged
substitutions must come out destabilising. Run it on every input table.

### 2.5 Compression toward zero / no resolving power near ΔΔG = 0

**Established by:** Pancotti et al. ([10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555)) —
"a common issue with all the tested methods is the compression of the ΔΔG predictions toward zero".
Marabotti et al. ([10.1186/s12859-021-04238-w](https://doi.org/10.1186/s12859-021-04238-w)) put a
number on it: predictions are **unreliable within ΔΔG ±0.5 kcal/mol**.

**Practical consequence:** do not rank variants by small ΔΔG differences, and do not use a
threshold inside ±0.5 kcal/mol to call anything. Published practice for a "substantial" effect is
ΔΔG > 1.5 kcal/mol ([10.1038/s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w)).

### 2.6 The accuracy ceiling

**Established by:** Montanucci et al. 2019 ([10.1093/bioinformatics/bty880](https://doi.org/10.1093/bioinformatics/bty880)) [IND].
Using pairs of independent experimental measurements of the *same* mutation, they derive
analytically that the Pearson upper bound is a function of measurement noise and of the spread of
ΔΔG in the dataset, and that **with current data the best attainable performance is r ≈ 0.7–0.8**.
Two corollaries from that paper, both load-bearing for this project: **higher Pearson values are
indicative of overtraining**, and **comparisons of predictors evaluated on different datasets are
inherently misleading**.

### 2.7 Epistasis is not captured

**Established by:** [10.1002/pro.70003](https://doi.org/10.1002/pro.70003). On the largest
double-mutant stability set, additive models match epistasis-aware predictors on most metrics.

**Practical consequence:** for multi-point variants, sum the single-mutant ΔΔGs; a dedicated
multi-mutant model is unlikely to beat that, and DDGun/FoldX do additivity transparently.

### 2.8 Complex models may be learning only conservation and burial

**Established by:** [10.1093/bioinformatics/btaf322](https://doi.org/10.1093/bioinformatics/btaf322) [IND].
Relative solvent accessibility *alone* reaches Spearman 0.480 on the ProteinGym Stability slice;
conservation log-odds alone 0.447; their product 0.551 — above ESM2-650M (0.496) and TranceptEVE-L
(0.424), and within 0.09 of the best model tested (ProSST-2048, 0.638).

**Practical consequence:** include RSA and a conservation score as baseline features in any
downstream model, and as a sanity floor for any predictor you adopt.

---

## 3. Are AlphaFold models acceptable inputs?

**Verdict: yes for ΔΔG, with caveats — but do not confuse two different questions.**

**Question A — AF models as *input structures* to a ΔΔG predictor. Answer: acceptable.**
The strongest evidence is Akdel et al. 2022
([10.1038/s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w)) [IND], which ran
**11 well-established ΔΔG methods** over 2,648 measured single-point mutations using AF2 models,
experimental structures, and Modeller homology models binned by template identity from 20 % to
90 %. Result, in the paper's own words: predictions from AF2 models were *comparable to those of
experimental structures*, while homology-model predictions "tended to show substantial decreases
in performance for templates below 40 % sequence identity". The 40 % threshold is independently
reproduced by Nielsen et al. ([10.1016/j.csbj.2022.11.048](https://doi.org/10.1016/j.csbj.2022.11.048)) [IND],
who additionally identify Rosetta `cartesian_ddg` as the protocol most robust to modelling
perturbation. The numeric values behind Akdel's Fig. 3d are in a box-plot panel; the per-method
correlations were not recoverable from the retrieved text, so **the "comparable" claim is reported
qualitatively, as the authors state it, not as a numeric penalty.** A measured penalty in
kcal/mol or Δr is, as far as this survey found, **not published**.

Supporting practice: ProteinGym itself distributes **AlphaFold models** as its reference structures
because most DMS targets lack experimental coverage
([10.1093/bioinformatics/btaf322](https://doi.org/10.1093/bioinformatics/btaf322)), and RaSP
([10.7554/eLife.82593](https://doi.org/10.7554/eLife.82593)) computed ~230 million human-proteome
ΔΔG values on predicted structures.

**Caveat — confidence gating.** Akdel show concordance degrades in regions with pLDDT < 50, and
that low-confidence regions are enriched for intrinsically disordered segments which are genuinely
more mutation-tolerant. For this project: **gate on per-residue pLDDT**, and treat
inter-domain linkers and low-pLDDT regions as out of scope for ΔΔG rather than as
confidently-neutral.

**Question B — AlphaFold's own output as a ΔΔG *proxy*. Answer: no.**
Pak et al. 2023 ([10.1371/journal.pone.0282689](https://doi.org/10.1371/journal.pone.0282689)) [IND]
fed wild-type and mutant sequences to AlphaFold and correlated the change in pLDDT (and mean
pLDDT) with measured ΔΔG, and separately with GFP fluorescence from a large single-mutant set.
They found **very weak or no correlation** in both cases. Running AlphaFold on the mutant sequence
is not a stability calculation.

**A third, awkward data point.** Ersoy et al. 2023
([10.3389/fgene.2023.1052383](https://doi.org/10.3389/fgene.2023.1052383)) [IND] used AF2
structures of 26 hereditary-cancer genes as input to five stability predictors over >1,000 ClinVar
missense variants. The stability predictors gave AUROC **0.614–0.719** for pathogenicity
(MUpro 0.534), and 0.596–0.682 when restricted to high-confidence AF2 regions — but **the AF2
confidence score at the variant position alone achieved AUROC 0.852**, beating every stability
predictor built on top of it. That is a warning that an apparent ΔΔG signal for pathogenicity can
be largely a proxy for burial/order that pLDDT captures more directly.

---

## 4. Does ΔΔG predict pathogenicity? Is it even the right quantity?

**Verdict: ΔΔG is a real but weak and highly protein-dependent signal, and it is the right quantity
for only part of the problem.**

### 4.1 The discrimination numbers

Gerasimavicius, Liu & Marsh 2020 ([10.1038/s41598-020-72404-w](https://doi.org/10.1038/s41598-020-72404-w)) [IND]
tested **13 stability predictors** on ClinVar-pathogenic vs gnomAD-benign missense variants.
Best was **FoldX, AUC 0.661**, then INPS3D 0.640, Rosetta 0.617, PoPMuSiC 0.614. Three findings
matter more than the ranking:

1. Using **|ΔΔG|** (absolute energy change) rather than signed ΔΔG improved nearly every predictor —
   i.e. strongly *stabilising* mutations are also enriched in disease.
2. Utility is **highly heterogeneous across proteins** — a global AUC hides proteins where ΔΔG
   works well and proteins where it is noise.
3. All 13 were **inferior to the best dedicated variant-effect predictors**.

The same group's follow-up ([10.1038/s41467-022-31686-6](https://doi.org/10.1038/s41467-022-31686-6)) [IND],
on 13,050 ClinVar and 211,266 gnomAD variants with FoldX v5, found that computing ΔΔG on **full
biological assemblies instead of isolated monomers** raised the mean |ΔΔG| of pathogenic variants
from **3.39 to 3.89 kcal/mol** and the AUC from **0.652 to 0.677**.

Against DMS rather than ClinVar labels: Gerasimavicius et al. 2023
([10.1002/pro.4688](https://doi.org/10.1002/pro.4688)) [IND] compared **9 stability tools** to
**49 DMS datasets / 170,940 variants**. FoldX and Rosetta again led; a "Foldetta" consensus of the
two matched dedicated variant-effect predictors. Critically, **predicted ΔΔG correlates best with
DMS phenotypes based on protein abundance** — which is exactly the mechanism ΔΔG describes — and
much less well with activity-type assays.

### 4.2 Why the ceiling exists: mechanism

The limiting factor is not predictor quality but that destabilisation is only one mechanism.
[10.1038/s41467-022-31686-6](https://doi.org/10.1038/s41467-022-31686-6) shows pathogenic
mutations in autosomal-recessive genes (overwhelmingly loss-of-function) are far more structurally
perturbing than autosomal-dominant ones; that dominant-negative and gain-of-function mutations are
**milder than LOF and closer in magnitude to benign variants**; and that DN mutations are strongly
enriched at **protein interfaces** — mean |ΔΔG| rising from 2.66 (monomer) to 3.32 kcal/mol (full
complex) for DN, versus 2.42→2.65 for GOF. Nearly all variant-effect predictors, *including purely
conservation-based ones*, underperform on non-LOF mutations.

How much of the problem is this? Badonyi & Marsh 2025
([10.1038/s41467-025-63234-3](https://doi.org/10.1038/s41467-025-63234-3)) [IND] estimate across
**2,837 phenotypes in 1,979 Mendelian disease genes** that **dominant-negative and gain-of-function
mechanisms account for 48 % of phenotypes in dominant genes**, and find widespread intragenic
heterogeneity — **43 % of dominant and 49 % of mixed-inheritance genes harbour both LOF and
non-LOF mechanisms**. Broader context: [10.1146/annurev-genom-111221-103208](https://doi.org/10.1146/annurev-genom-111221-103208).

**Practical consequence for this project.** ΔΔG is the right quantity for
**recessive / haploinsufficient / abundance-driven loss of function**, and it is close to the wrong
quantity for dominant-negative and gain-of-function variants — which are roughly half of dominant
phenotypes, are concentrated at interfaces, and will be systematically *under*-scored. Since the
intragenic heterogeneity figures show the same gene can host both, mechanism cannot be assigned
gene-by-gene up front. A ΔΔG-only variant interpretation pipeline will have a mechanism-shaped
blind spot, and it should be reported as a stability score, not as a pathogenicity score.
Mitigations the literature supports: use **|ΔΔG|** not signed ΔΔG; compute on **complexes** where
assemblies exist; combine FoldX+Rosetta rather than trusting one; and keep a sequence-based VEP
alongside.

*(This report concerns research methodology and variant interpretation at population scale, not
clinical decisions about any individual. ΔΔG-derived scores are not diagnostic evidence; variant
classification for a patient belongs with a qualified clinical geneticist working to ACMG/AMP
criteria with the full case context.)*

---

## 5. Current accuracy on held-out data, and the multi-domain question

### 5.1 Held-out accuracy, honestly stated

| Evaluation condition | Best reported *r* | Source |
|---|---|---|
| Direct single-point mutations, proteins <25 % identity to training (S669) | **0.50** (MAESTRO); 0.43 for ThermoMPNN | [IND] [10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555); [SELF] [10.1073/pnas.2314853121](https://doi.org/10.1073/pnas.2314853121) |
| New non-overlapping curated set, 27 methods (incl. mega-scale era) | **0.53** | [IND] [10.1002/pro.4861](https://doi.org/10.1002/pro.4861) |
| Direct + reverse pooled (S669 "total") | **0.62** (PremPS) | [IND] [10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555) |
| Ssym inverse (held out from pre-2020 tools) | **0.43** (Rosetta) → **0.60** (ThermoMPNN) → 0.72 (Stability Oracle, code unavailable for verification) | [IND] [10.1093/bioinformatics/bty348](https://doi.org/10.1093/bioinformatics/bty348); [SELF] [10.1073/pnas.2314853121](https://doi.org/10.1073/pnas.2314853121) |
| Mega-scale test split (same experimental platform as training) | **0.725** Spearman | [SELF] [10.1073/pnas.2314853121](https://doi.org/10.1073/pnas.2314853121) |
| Theoretical ceiling from experimental noise | **0.70–0.80** | [IND] [10.1093/bioinformatics/bty880](https://doi.org/10.1093/bioinformatics/bty880) |

Read down that table: the mega-scale-platform number (0.725) is at the theoretical ceiling, and the
cross-dataset numbers (0.43–0.53) are far below it. **Performance is a function of how similar the
test data is to the training platform, more than of which method is used.** Budget *r* ≈ 0.4–0.5
and RMSE ≈ 1.5 kcal/mol for new human proteins, not the headline figures.

### 5.2 Large multi-domain proteins: the evidence does not exist

This is the clearest gap found in this survey, and it is directly load-bearing for a project
targeting many human genes.

**Every major benchmark is built from small, single-domain, globular proteins:**

- **Mega-scale / Tsuboyama** ([10.1038/s41586-023-06328-6](https://doi.org/10.1038/s41586-023-06328-6)):
  domains of **40–72 residues** only. This is the training data for ThermoMPNN, SPURS, PROSTATA
  and most of the current generation.
- **S2648** (as used in the AF2 assessment): 2,648 mutations over 121–132 "globular proteins"
  ([10.1038/s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w)).
- **Ssym**: 342 direct mutations with only **19 experimental wild-type structures** — small,
  heavily crystallised model proteins ([10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555)).
- **S669**: 669 variants from thermodynamic denaturation studies — a technique that works on small
  reversibly-folding proteins.
- **Site-saturation mutagenesis of 500 human protein domains**
  ([10.1038/s41586-024-08370-4](https://doi.org/10.1038/s41586-024-08370-4)): "domains", by design.
- Pancotti et al. explicitly **excluded membrane proteins** from S669 as a different chemical
  environment ([10.1093/bib/bbab555](https://doi.org/10.1093/bib/bbab555)).

**No independent assessment of ΔΔG accuracy as a function of protein length, domain count, or
inter-domain-interface location was found in this survey.** Targeted searches for protein-size and
multi-domain effects on ΔΔG accuracy returned no such benchmark. This is an **absence of evidence**,
stated as such — not a measured negative result.

**The indirect evidence that domain context matters is real, however.** The single clearest
quantitative signal is that moving from isolated monomers to full assemblies changes predicted
|ΔΔG| by ~15 % on average and shifts pathogenicity AUC from 0.652 to 0.677, with
dominant-negative variants — those concentrated at interfaces — gaining most (2.66 → 3.32 kcal/mol)
([10.1038/s41467-022-31686-6](https://doi.org/10.1038/s41467-022-31686-6)) [IND]. An
inter-**domain** interface within one chain is structurally the same kind of environment as an
inter-**molecular** one, so the direction of the effect should be expected to carry over; the
magnitude for intra-chain domain interfaces has not been measured.

**Practical consequences:**

1. Treat any ΔΔG for a residue at an inter-domain interface of a large protein as **extrapolation
   beyond the validated domain of every current method**, and label it as such in outputs.
2. A predictor's S669/Ssym/mega-scale score carries **no** demonstrated transfer to a 1,000-residue
   multi-domain kinase. Prefer methods whose inputs are the full structure over methods that crop a
   local neighbourhood, but recognise that this preference is reasoned, not benchmarked.
3. The FireProtDB subset is the only widely used benchmark component drawn from real multi-domain
   proteins with UniProt anchoring ([10.1093/nar/gkaa981](https://doi.org/10.1093/nar/gkaa981)) and
   is therefore the most relevant held-out set available — a point already made in the datasets
   memo.
4. If the project needs a defensible accuracy figure for large proteins, it will have to be
   **generated**, not cited: assembling a held-out set of measured ΔΔGs in proteins >300 residues,
   stratified by interface vs core vs surface, would be a genuinely novel and publishable control.

---

## 6. Where the literature disagrees

1. **Is class imbalance the cause of poor stabilising-mutation prediction?**
   Pucci ([bty348](https://doi.org/10.1093/bioinformatics/bty348)) says largely yes and fixes it
   architecturally. Yang ([pone.0283727](https://doi.org/10.1371/journal.pone.0283727)) and Zheng
   ([pro.4861](https://doi.org/10.1002/pro.4861)) say no — data quality and feature
   informativeness dominate, and balancing does not deliver. Unresolved; the empirical fact that
   antisymmetric-by-construction methods *still* fail on stabilising variants favours the latter.
2. **Do the ML methods overfit?** Fang ([bbz071](https://doi.org/10.1093/bib/bbz071)) says all five
   examined do. A formal response was published in the same journal
   ([bbz168](https://doi.org/10.1093/bib/bbz168), title/DOI verified; full text not retrieved for
   this report, so its specific counter-arguments are **not** characterised here). Readers should
   consult both.
3. **Are predicted structures as good as experimental ones?** Akdel
   ([s41594-022-00849-w](https://doi.org/10.1038/s41594-022-00849-w)) and Nielsen
   ([csbj.2022.11.048](https://doi.org/10.1016/j.csbj.2022.11.048)) say yes within stated
   confidence/identity limits. Pak ([pone.0282689](https://doi.org/10.1371/journal.pone.0282689))
   is widely cited as saying no — but it tested a *different* claim (pLDDT as a ΔΔG proxy). These
   two findings are frequently conflated in secondary literature; they are compatible.
4. **Has the mega-scale era actually improved generalisation?** ThermoMPNN
   ([pnas.2314853121](https://doi.org/10.1073/pnas.2314853121)) and SPURS
   ([s41467-025-67609-4](https://doi.org/10.1038/s41467-025-67609-4)) report state-of-the-art
   [SELF]. But ThermoMPNN's own S669 figure (0.43) sits mid-range in Pancotti's 2022
   direct-only band, Zheng's 27-method independent assessment caps the whole field at 0.53
   including mega-scale methods, and RSALOR shows a two-feature baseline at 0.551 Spearman on
   ProteinGym Stability. **No independent assessment yet confirms that the mega-scale generation
   generalises better than PremPS/ACDC-NN/DDGun on genuinely unseen non-domain-sized proteins.**

---

## 7. Access notes

All 33 DOIs cited in this report resolved via CrossRef on 28 Oct 2026 (33/33; 38 DOIs were checked
in total during the survey, 5 of which are not cited here). Full text was retrieved and read for the
primary sources. Items where a specific number could not be verified, and which are therefore
described qualitatively or omitted above:

- **Akdel 2022 Fig. 3d** — per-method AF2-vs-experimental ΔΔG correlations exist only as a box
  plot; no numeric table in the retrieved text.
- **SPURS Fig. 2e / Supplementary Tables 1–3** — per-dataset Spearman/Pearson not present in the
  retrieved main text.
- **Gerasimavicius 2022 Figs 2c/3c** — AUCs by inheritance mode and by mechanism are in figure
  panels; only the Fig. 1 AUCs (0.652 / 0.677) and the mean |ΔΔG| values appear in text.
- **Zheng 2023 ([10.1002/pro.4861](https://doi.org/10.1002/pro.4861))** — PMC returned metadata and
  abstract only (≈3.9 kB); the per-method table was not retrievable. The r = 0.20–0.53 range and
  the 4,038 / 27-method / >1,000-stabilising counts are from the abstract, which is authoritative
  for those figures, but **individual method rankings from this paper are not quoted**.
- **[10.1021/acs.jcim.0c00591](https://doi.org/10.1021/acs.jcim.0c00591)** (dataset dependency),
  **[10.1093/bib/bbz168](https://doi.org/10.1093/bib/bbz168)** (response to Fang),
  **[10.1093/bioinformatics/bty979](https://doi.org/10.1093/bioinformatics/bty979)** (INPS test
  case) — DOI, title and venue verified via CrossRef; full text not retrieved. Cited only for the
  existence and topic of the work.

Nothing required registration or was paywalled beyond retrieval; Oxford University Press hybrid
articles were obtained via PMC, and Wiley/Elsevier articles via Unpaywall or PMC.
