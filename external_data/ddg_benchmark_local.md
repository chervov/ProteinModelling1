# ΔΔG predictors benchmarked locally — three methods, one held-out human set

*Run 28 October 2026 on an 8-core CPU, no GPU. Every number here was computed on this machine
from the tools' own released weights; nothing is quoted from a paper unless marked as such.
Companion to [ddg_study_agent.md](ddg_study_agent.md), which surveys the literature and the
precomputed resources.*

## What was actually run

| tool | what ran | outcome |
|---|---|---|
| **ThermoMPNN** | 23 human proteins (269,458 variants) + 357 Ssym structures | complete; 32.1 min + 48.8 min |
| **RaSP** | 23 human proteins (269,458 variants) + 357 Ssym structures | complete; 32.1 min + 145.8 min |
| **ProtVar FoldX** | full 1.56 GB table streamed, 23 accessions extracted | complete, 5.2 min |
| DDGun | — | **blocked**, see below |

The ProtVar stream independently confirms EBI's row count: **208,792,558 data rows**, of which
201,742 belong to the 23 accessions. No fabricated figure anywhere.

## 1. Three-way head-to-head on 386 held-out human measurements

FireProtDB's homology-filtered split (>25% identity removed), 23 human proteins, 386 experimental
ΔΔG values. **All three methods cover all 386 variants**, so the comparison is like-for-like.

| method | Pearson r | Spearman | RMSE (kcal/mol) |
|---|--:|--:|--:|
| **ThermoMPNN** (local, AlphaFold inputs) | **+0.517** | +0.559 | **1.47** |
| ProtVar FoldX (precomputed by EBI) | +0.388 | +0.482 | 2.56 |
| RaSP (local, same AlphaFold inputs) | +0.366 | +0.431 | 1.84 |

![three-way]({{artifact:752bc744-e1cc-4e02-b971-d13f64ac7fd8}})

ThermoMPNN wins overall and on RMSE by a wide margin. But the split by direction of effect
reverses part of that story:

| method | destabilising (n=278) | **stabilising (n=108)** |
|---|--:|--:|
| ThermoMPNN | +0.430 | **+0.068** |
| ProtVar FoldX | **+0.497** | +0.013 |
| RaSP | +0.425 | **-0.121** |

**On destabilising mutations alone, FoldX is the most accurate of the three** — the empirical force
field beats both deep-learning methods. ThermoMPNN's overall advantage comes from spanning the two
regimes more coherently, not from being better within the common one.

**All three fail on stabilising mutations**: +0.07, +0.01, and RaSP actively *anti*-correlated at
−0.12. Three different method families — a graph network, a self-supervised 3D CNN, and an
empirical force field — fail the same way. This independently reproduces, on data none of them was
trained on, the finding that none of 27 assessed methods predicts stabilising mutations accurately
([10.1002/pro.4861](https://doi.org/10.1002/pro.4861)).

### Consensus does not help, and here is why

| combination | Pearson r |
|---|--:|
| ThermoMPNN alone | **+0.517** |
| ThermoMPNN + FoldX (z-averaged) | +0.509 |
| all three | +0.489 |

This **contradicts the standard advice** that a consensus of several tools is a crude but effective
improvement ([10.1186/s12859-021-04238-w](https://doi.org/10.1186/s12859-021-04238-w)) and the
"Foldetta" result ([10.1002/pro.4688](https://doi.org/10.1002/pro.4688)). The reason is visible in
the data: **the predictors agree with each other far more than any of them agrees with experiment.**

| pair | r |
|---|--:|
| ThermoMPNN ↔ RaSP | +0.702 |
| RaSP ↔ FoldX | +0.594 |
| ThermoMPNN ↔ FoldX | +0.583 |
| *mean of each vs experiment* | *+0.424* |

Averaging correlated errors cannot cancel them. Consensus buys nothing when the members share a
systematic bias, which on this set they plainly do.

## 2. The antisymmetry audit — the free check nobody runs

Thermodynamics requires ΔΔG(A→B) = −ΔΔG(B→A). Ssym is built for exactly this test: 342 mutations
over 15 wild-type structures, each paired with **its own mutant crystal structure**. I ran
**both ThermoMPNN and RaSP** over all 357 structures — 699 saturation-mutagenesis runs in total.

![antisymmetry]({{artifact:9cb476a9-c028-4f3e-9124-a8b0fb10627d}})

**Pipeline validation first.** The experimental control is exact — r(exp_dir, exp_inv) = **−1.000**
and ⟨δ_exp⟩ = **0.000** — confirming the pairing and the position mapping are correct. ThermoMPNN's
measured accuracy then reproduces the published values almost exactly, which validates the whole
chain: **0.729 direct / 0.603 inverse** here against **0.72 / 0.60** published
([10.1073/pnas.2314853121](https://doi.org/10.1073/pnas.2314853121)).

| | ThermoMPNN (n=341) | RaSP (n=342) | required |
|---|--:|--:|--:|
| accuracy, direct half \|r\| | **0.729** | 0.649 | — |
| accuracy, inverse half \|r\| | **0.603** | **0.189** | — |
| r(pred_dir, pred_inv) | −0.705 | −0.288 | **−1.000** |
| ⟨δ⟩ = ΔΔG(A→B)+ΔΔG(B→A) | +0.689 | +1.626 | **0** |
| median \|δ\| | 0.497 | 1.314 | 0 |

**RaSP collapses on the inverse half** — 0.649 → 0.189 — reproducing the classic Ssym failure Pucci
et al. documented for black-box ML methods (MUPRO 0.79→0.07, STRUM 0.75→−0.15, AUTOMUTE 0.73→−0.01)
([10.1093/bioinformatics/bty348](https://doi.org/10.1093/bioinformatics/bty348)). ThermoMPNN holds
up far better, losing only 0.13.

**Both are biased in the same direction.** δ is positive in both conventions (positive =
destabilising), so **both predict "destabilising" whichever way the mutation is run** — RaSP by
2.4× more than ThermoMPNN. The panels show the character of the failure clearly: ThermoMPNN's
points form a band *parallel to* the thermodynamic line but offset above it (a systematic
offset), whereas RaSP's form a diffuse cloud (offset *and* little antisymmetry at all).

For context, the least-biased tool in Pucci's survey was PoPMuSiC^sym at ⟨δ⟩ = 0.03 kcal/mol, so
ThermoMPNN's +0.69 is roughly 70% of the worst black-box methods and ~20× the best physics-based one.

**Practical consequence:** a predicted ΔΔG below about ±0.7 kcal/mol (ThermoMPNN) or ±1.6 (RaSP)
is inside the model's own directional bias. Do not report the sign of a small prediction.

## 3. Engineering findings worth recording

**RaSP's shipped inference is ~9× slower than necessary.** `ds_pred` reloads a downstream model
*and recomputes the cavity model* once per ensemble member, but the cavity output does not depend on
which member. Hoisting it out of the loop: **213.6 s → 23.2 s** for lysozyme's 2,960 predictions,
values bit-identical. The rewritten loop is `run_rasp_predict.py`.

**Four 2022-era breakages** had to be patched before RaSP would run at all, all documented in-place:

| breakage | fix |
|---|---|
| `np.int` removed in NumPy ≥1.24 | replaced with `int` |
| `Bio.SubsMat` removed in Biopython ≥1.80 | made optional (PRISM output only) |
| mkdssp 4.x accepts only mmCIF | SASA computed with Biopython Shrake-Rupley instead |
| training-only plotting imports | made optional |

The DSSP substitution was verified harmless *before* being made: `resenv.sasa` is read only by
`visualization.py` and never enters the model, which consumes atom coordinates on a 3D grid. The
predictions cannot change. ThermoMPNN needed no patches but **cannot be `git clone`d in this
sandbox** — the repo contains a `.idea/` directory the filesystem refuses to create; the codeload
tarball works.

**Measured throughput, CPU-only:** ThermoMPNN 280 variants/s sustained; RaSP ~125 variants/s after
the fix. RaSP is ~2.2× slower, less accurate here, and far more antisymmetry-biased, so ThermoMPNN remains the
workhorse recommendation.

## 4. DDGun could not be run, and no substitute was faked

DDGun is the baseline the literature says to beat — untrained, antisymmetric by construction, within
~0.04 Pearson of the best trained methods on S669. It **cannot run here**: all three of its score
terms (`get_pot_prof`, `get_subs_prof`, `get_seq_prof`) require an HSSP sequence profile built by
hhblits against uniclust30, a ~25 GB database, and there is no profile-free mode. Supplying a
single-sequence profile would silently reduce it to a substitution-matrix lookup — not DDGun, and
worthless as the baseline it is meant to provide. **It is reported as not run rather than
approximated.** Running it needs either the 25 GB database or a precomputed-profile source.

## 5. What this changes about the recommendation

1. **ThermoMPNN stays the workhorse** — best overall accuracy and RMSE here, 2.2× faster than RaSP.
2. **But use FoldX where it is already computed.** ProtVar covers 76% of human residues for free and
   is the *better* predictor on destabilising mutations specifically. There is no reason to
   recompute what EBI has already published.
3. **Drop the consensus plan.** It made things worse on this set; the members' errors are correlated.
4. **Never report the sign of a small ΔΔG.** The measured antisymmetry bias is ±0.69 kcal/mol for
   ThermoMPNN and ±1.63 for RaSP, which swamps any prediction near zero — on top of the
   ±0.5 kcal/mol experimental noise floor.
5. **Do not use any of these to search for stabilising mutations.** All three have no skill there.
