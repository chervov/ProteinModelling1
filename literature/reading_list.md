# Reading list

Newest first. One block per paper: title, authors, venue, year, link, and what it establishes.

---

## A curated benchmark for cofolding models on kinase conformational states

Sun & Head-Gordon · *npj Drug Discovery* · **2026** ·
[10.1038/s44386-026-00068-z](https://doi.org/10.1038/s44386-026-00068-z) · PDF read 5 Nov 2026

**KinConfBench**: 2,225 high-quality human kinase chains from the PDB, testing whether cofolding
models recover the *experimentally observed conformational state* rather than merely a plausible
fold. Four open-source models — **Boltz-2, Chai-1, Protenix, RoseTTAFold-All-Atom (RFAA)** —
with states labelled by the Modi & Dunbrack nomenclature (DFGin / DFGout / DFGinter × Ramachandran
dihedral labels).

### Which method is best

**The three diffusion-based models beat RFAA; the paper does not crown a winner among them.**

- All four fall in a **~60–80%** band for conformational classification, the diffusion models at
  the top.
- **RFAA's absolute accuracy falls short** — the paper's own words, taken as evidence for "the
  performance advantages of diffusion-based cofolding models". Its best-of-20 sampling rises
  **34.6% → 60.5%**, so its single highest-confidence pose is often wrong.
- On conformational **diversity the order inverts**: Chai-1 and RFAA explore more within the
  correct basin than Boltz-2 and Protenix — though all are "quite limited" in absolute terms.

So: a diffusion model for accuracy, none of them for diversity.

### The three failure modes, which matter more than the ranking

1. **Ligand-pose metrics do not predict conformational correctness.** Good active-site RMSD does
   not mean the right kinase state. This is the paper's central claim and the reason the benchmark
   exists.
2. **Severe mode collapse.** Across 20 inferences roughly two-thirds of systems come out
   *entirely* right or *entirely* wrong — a binary outcome rather than graded uncertainty.
   Sampling more does not yield an ensemble.
3. **"Apo-drift."** All three diffusion models default to the **ligand-free** state for a large
   fraction of holo complexes — *even when those complexes are in the training set* — and it
   worsens for structures deposited after the training cutoff. The models are anchored to the
   training distribution's dominant prior rather than responding to the specific ligand.

Table S4 lists **152 kinase–ligand systems where all four models fail**, offered as a target set.

### Why it matters here

This is the paper behind the KinConfBench reference already in
[`../open_close/open_close_inf.md`](../open_close/open_close_inf.md), and it independently
describes two things we hit:

- **Apo-drift is our AlphaFold result in their language.** AFDB gives *open* for JAK1 and JAK2 and
  *closed* for JAK3 and TYK2 — the dominant prior, not a context-specific answer. Our AFDB
  FERM–JH1 PAE of 18.5–25.8 Å against a ~31 Å ceiling says the same thing numerically.
- **Mode collapse matches our MSA-depth finding.** The JAK1 third arrangement appeared only at
  shallow MSA (64/256 and 96/384) and vanished at 128/512 and deeper: deepening the alignment
  collapses the prediction onto the default state. See
  [`../JAK1/third_structure/`](../JAK1/third_structure/).

**Caveat on scope — do not transfer their numbers to our question.** KinConfBench measures the
**intra-domain DFG / active-site** state; we measure the **inter-domain JH2–JH1** arrangement.
These are two of the three senses in the terminology note and they are *orthogonal*: 4OLI is
autoinhibited (closed, our sense) yet classified `DFGin-BLAminus`, the active configuration. Their
60–80% accuracies are therefore **not** a bound on our problem, and neither is their model ranking.

---

## Energy-Based Models for Predicting Mutational Effects on Proteins

Soga, Lei, He, Bilodeau & Li · arXiv:2508.10629 · **2025** ·
[arxiv.org/abs/2508.10629](https://arxiv.org/abs/2508.10629)

Predicts binding ΔΔG with an energy-based model of the complex's conformation, avoiding explicit
modelling of the full conformational distribution. Splits the prediction into a sequence term
from an inverse-folding model and a structure term from the energy model, assuming equilibrium
between bound and unbound states; reports gains over existing structure- and sequence-based deep
methods, including SARS-CoV-2 antibody optimisation.

**Note the scope:** ΔΔG of **binding**, not of folding. Our ΔΔG work is folding stability, so this
is adjacent rather than directly comparable.

---

## A fast and accurate predictor based on relative solvent accessibility and log-odds ratio (RSALOR)

Tsishyn, Pucci & Rooman · *Bioinformatics* · **2025** ·
[10.1093/bioinformatics/btaf322](https://doi.org/10.1093/bioinformatics/btaf322)

A two-feature model — **log-odds ratio from an MSA × relative solvent accessibility** —
benchmarked on ProteinGym (~700,000 mutations, 218 DMS sets) against 27 predictors including 19
protein language models. On the Stability slice: ProSST-2048 0.638, SaProt 0.565, **RSALOR 0.551**,
ESM2-650M 0.496, **−RSA alone 0.480**, conservation alone 0.447 (Spearman).

**Why it matters here.** RSA alone beats ESM2-650M on stability, and we reproduce the shape of
that result independently on the JAKs: RSA outperforms all three ΔΔG methods at separating the
clusters (AUC 0.765–0.816). See [`../data/ddg/survey/DDG_METHODS_SURVEY.md`](../data/ddg/survey/DDG_METHODS_SURVEY.md) §6.

---

## Identification of pathogenic missense mutations using protein stability predictors

Gerasimavicius, Liu & Marsh · *Scientific Reports* 10:15387 · **2020** ·
[pubmed.ncbi.nlm.nih.gov/32958805](https://pubmed.ncbi.nlm.nih.gov/32958805/)

Tests ΔΔG predictors as **classifiers of pathogenic missense variants** rather than as stability
estimators, and finds them weak discriminators — a large fraction of pathogenic variants do not
act by destabilisation at all.

**Why it matters here.** It is the published version of what we measure independently: Rosetta
ΔΔG reaches AUC 0.71–0.75 against our clustering, and on the TYK2 DMS the sequence predictors
beat every stability method even on the abundance arm.

---

## Insights into the Binding Recognition and Susceptibility of Tofacitinib toward Janus Kinases

Sanachai, Mahalapbutr, Choowongkomon *et al.* · *ACS Omega* 5(1):369–377 · **2020** ·
[PMC6964278](https://pmc.ncbi.nlm.nih.gov/articles/PMC6964278/)

500-ns molecular dynamics plus binding free-energy calculations: tofacitinib binds the ATP site of
JAK1/2/3 chiefly through van der Waals contacts and hinge-region hydrogen bonds, with predicted
affinity highest for JAK3, matching the experimental IC50 ranking. Binding shifts the
glycine-rich loop to a **closed** conformation and reduces its flexibility.

**Read the word "closed" carefully.** This is the **G-loop** sense — a few Å at the ATP pocket —
not the ~80 Å JH2–JH1 domain motion this project means. See
[`../open_close/open_close_inf.md`](../open_close/open_close_inf.md) for the three senses and why
they cannot substitute for one another.
