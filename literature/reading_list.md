# Reading list

Newest first. One block per paper: title, authors, venue, year, link, and what it establishes.

---

## A curated benchmark for cofolding models on kinase conformational states

Sun & Head-Gordon · *npj Drug Discovery* · **2026** ·
[10.1038/s44386-026-00068-z](https://doi.org/10.1038/s44386-026-00068-z)

Benchmarks whether cofolding models of the AlphaFold3 type reproduce the correct **kinase
conformational state**, not merely a plausible fold.

**Why it matters here.** This is the failure mode the project hit directly: AlphaFold gives
*open* for JAK1 and JAK2 and *closed* for JAK3 and TYK2, and our own runs reached the right
arrangement only at shallow MSA depth. A benchmark for exactly that question is worth reading
before any further conformational modelling.
*(Summarised from CrossRef metadata — the full text was behind a login.)*

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
