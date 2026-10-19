# Selected conclusions (20261019_131543)

Consolidated results for JAK1, JAK2, JAK3 and TYK2. Method: OpenFold model_1 with guided recycling,
15 recycles, MSA depth as the control variable, mutants paired with wild type on identical seeds.

---

## 0. What is measured

Two numbers describe every predicted structure.

**FERM–JH1 centroid distance** — how far the kinase domain sits from the FERM domain. Simple, but it
reports only one aspect of the geometry.

**The arrangement metric** — the one most results below rest on. For each seed:

1. superpose the predicted structure onto a reference using **only JH2** (pseudokinase) Cα atoms;
2. without moving anything further, measure the **RMSD of the JH1** (kinase) Cα atoms.

The result is a distance in Å describing *where the kinase domain sits relative to the pseudokinase
domain*. It is insensitive to fold quality: each domain can be perfect and still give a large number if
JH1 is parked elsewhere. Every per-seed list in this document — for example R657Q's
`2 2 3 4 · 83 89 91 91` — is one such number per seed.

**Both metrics are required.** FERM–JH1 detects JAK3 M592F (p = 0.012) but misses A572V (p = 0.13); the
arrangement metric does the reverse. Reporting either alone misrepresents at least one variant.

---

## 1. Reference states and the open/closed criteria

Every reference structure, measured identically. Cross-paralogue mappings by sequence alignment
(identity 44–59 %); full table in [reference_states.md](reference_states.md).

| structure | protein | FERM–JH1 | JH2–JH1 | state |
|---|---|--:|--:|---|
| **4OLI crystal** | TYK2 | – | 39.0 | **experimental closed (autoinhibited)** |
| **7T6F cryo-EM** | JAK1 | 84.1 | 45.0 | **experimental active dimer** |
| ma-l9b1f | JAK1 | 40.0 | 39.5 | closed model (Jeanpierre) |
| ma-a1sai | JAK1 | 92.6 | 46.1 | open model (Jeanpierre) |
| AF2 | JAK1 / JAK2 | 92.3 / 93.8 | 46.3 / 46.1 | **open** |
| AF2 | JAK3 / TYK2 | 41.5 / 39.7 | 38.3 / 37.2 | **closed** |

**Criteria — FERM–JH1 separates the states; JH2–JH1 does not:**

| state | FERM–JH1 |
|---|---|
| closed / autoinhibited | **40–45 Å** |
| active dimer (7T6F-like) | **~84 Å** |
| open | **92–94 Å** |

JH2–JH1 spans only 38–40 Å (closed) versus 45–46 Å (open) — a 7 Å gap, too small to classify anything.
Hence the arrangement metric.

**Scale for the arrangement metric:** the two independent closed references — a model (ma-l9b1f) and a
crystal structure of a *different* paralogue (4OLI) — agree to **4.1 Å**. Open versus closed is **~81 Å**.
Working thresholds: **< 25 Å = that state, > 60 Å = not that state.**

**A trap:** the AlphaFold models of **JAK1 and JAK2 are open** while those of **JAK3 and TYK2 are closed**.
"Distance vs AF2" therefore means distance-from-open for JAK1/JAK2 and distance-from-closed for
JAK3/TYK2. The two must never be pooled without checking. AF2 TYK2 is only **1.6 Å** from the
experimental 4OLI arrangement.

---

## 2. MSA depth, not sequence, decides the conformation

Each JAK switches between arrangements as the alignment is thinned, and each does so at a different
depth. A mutation is only detectable where wild type visits both states.

| | both states appear at | at 128/512 |
|---|---|---|
| JAK2 | 512/8192 (7 closed / 7 open) | mostly detached JH1 |
| JAK1 | 128/512 | bistable |
| JAK3 | 128/512 (7 of 16 seeds closed-like) | bistable |
| **TYK2** | **none found** | uniformly open |

JAK3's switch is unusually sharp: 16/16 compact at 128/512, 15/16 open one step deeper at 256/1024.

---

## 3. The third JAK1 arrangement — an experimentally supported state

Detail: [JAK1/JAK1_third.md](JAK1/JAK1_third.md).

At shallow MSA (all 5 seeds at 64/256, 2 of 5 at 96/384; never at 128/512 or deeper) JAK1 adopts a
**third arrangement, neither open nor closed**. It is one well-defined state: six of seven structures
cluster within 0.7–9.5 Å of one another.

| | FERM–JH1 | SH2–JH1 | JH2–JH1 |
|---|--:|--:|--:|
| **third arrangement** | **83.7–84.6** | **53.7–55.7** | **43.9–45.8** |
| open (ma-a1sai) | 92.5 | 77.7 | 46.0 |
| closed (ma-l9b1f) | 40.1 | 55.3 | 39.5 |

JH1 is **rotated 130–150°** relative to the open state and touches **only JH2** — zero contacts with FERM
or SH2 — through an interface of its own: JH2 residues ~750 and 798–807 against JH1 residues ~930–941
and 997. That interface shares almost nothing with the open or closed one and **does not involve the
V658 region** central to closed.

**It matches an experimental structure.** The cryo-EM active JAK1 dimer **7T6F** (mouse JAK1 V657F bound
to IFNλR1; Glassman et al., Science 2022) agrees to **4.9 Å** by the arrangement metric, with matching
domain distances and the same interface residues. The discrimination is clean: the other cryo-EM JAK1
dimer, **8EWY**, matches our **open** state instead (3.7–4.5 Å).

Not an artefact: every domain is within 1.3 Å of the AF2 fold, and JH1 pLDDT is 88.9–91.2.

**This is what JAK1 V658F drives the protein into** — from 2 of 5 seeds to **16/16** at 96/384
(p = 0.0075), and at 128/512 it removes the closed state while gaining 4–5 seeds here (p = 0.035). The
mutation the cryo-EM structure carries pushes the model toward the state that structure shows: the
cleanest internal validation in the project.

---

## 4. JAK3 — five mutations, two classes

MSA 128/512, 16 seeds each, arrangement metric. Wild type retains the closed arrangement in **7/16**.

| variant | n | closed-like (< 25 Å) | median | Fisher |
|---|--:|--:|--:|--:|
| wild type | 16 | 7/16 | 61.5 | – |
| **M592F** (= JAK2 V617F position) | 16 | **1/16** | 64.0 | **0.037** |
| **A572V** *(reported activating)* | 16 | **1/16** | 84.3 | **0.037** |
| M511I *(reported activating)* | 16 | 7/16 | 84.8 | 1.00 |
| A573V | 16 | 12/16 | 2.7 | – |
| R657Q *(reported activating)* | 8* | 4/8 | 43.1 | 1.00 |

\* second half running.

**Class 1 — the closed state is abolished.** M592F and A572V, 7/16 → 1/16. M592F's escapees reach the
genuinely open state (**3.3 Å** from the JAK1 open model), which is the same arrangement wild type adopts
spontaneously at full MSA depth. A572V's are splayed, matching no reference.

**Class 2 — the closed state is retained but becomes far more canonical.** M511I, A573V and R657Q keep
similar or larger numbers of closed seeds, but at **1–4 Å** from the reference where wild type's best
reach only **16–23 Å**. They also sharpen the bimodality (R657Q: nothing between 4 and 83 Å).

**Of three reported activating alleles, one abolishes the closed state and two tighten it.** Not one
phenotype. Three unseparated explanations for class 2: the model misses their mechanism (JAK3 oncogenic
hyperactivity is reported to depend on **ATP binding to JH2**, and we model no nucleotide); tighter is
not more populated; or the metric reports packing rather than catalytic competence.

**A numbering error, found and corrected:** JAK3 has adjacent alanines at 572 and 573. The reported
allele is **A572V**; an earlier run used A573V. Both were then run — and they fall into different classes.

---

## 5. TYK2 — the ground-truth test

TYK2 is the only JAK with an experimental closed structure (4OLI, 2.8 Å).

**1. Free prediction never reaches the closed state, at any depth.** Across 32/64, 64/256, 96/384,
128/512 and the default, the closest approach is **25.4 Å**, with 3 of ~100 seeds below 30 Å. JAK1,
JAK2 and JAK3 all reach theirs. Yet once 4OLI is imposed as a template the closed state is **perfectly
stable** through twelve template-free recycles (16/16 seeds within 2 Å). **A real but inaccessible basin.**

**2. V678F, the reported activating substitution, has a strong effect.** At 64/256 wild type ranges
41.2–92.0 Å while V678F is confined to **90.7–94.8 Å** — it abolishes wild type's partial approaches to
closed, **p = 0.0008**. *Replication to n = 16 is running; the figure is not final.*

**3. P982A shows no significant effect at any depth** (p = 0.59 / 0.34 / 0.14), so the structural
prediction below is unsupported — though with wild type never occupying the closed state, the assay may
have no floor to measure against.

**4. The 4OLI template-release assay does not work.** All 16 seeds stayed 1.4–1.9 Å from the template
through every template-free recycle: no dynamic range, so no mutant could be distinguished.

---

## 6. Structural analysis of seven variants of interest

Interface burial in each protein's own closed structure (ΔSASA on closing; > 25 Å² = interface).
Detail: [mutation_analysis.md](mutation_analysis.md).

- **TYK2 P982 is the only one of the seven at a domain interface** — 47 % exposed alone, **59.8 Å² buried
  on closing**, 28 cross-domain contacts of which **12 are deleted by proline→alanine**. Proline is
  conserved at this position in all four JAKs (JAK1 P960, JAK2 P933, JAK3 P906).
- TYK2 V678, JAK3 Y581, JAK2 V578 / L805 / V1110 and JAK2 G571 all bury **0.0 Å²**. V678F's effect must
  therefore be **allosteric**, which makes it the more striking result.
- **Sequence predictors are unreliable here.** AlphaMissense scores JAK2 V617F (ClinVar Pathogenic) at
  0.33–0.39 "benign" and TYK2 P1104A (ClinVar Benign) at 0.82 "pathogenic" — wrong in both directions,
  being trained on loss of function rather than conformational gain of function.
- None of the seven has a dedicated functional study in the literature.

---

## 7. Methodological conclusions

**Two metrics are mandatory** — see section 0.

**Mode collapse is real, and MSA subsampling is the cure.** TYK2 wild-type seed spread against the
closed reference, by depth:

| MSA | 128/512 | 96/384 | 64/256 | 32/64 |
|---|--:|--:|--:|--:|
| spread | **0.6 Å** | 8.8 Å | 50.8 Å | 57.4 Å |

At 128/512 a rank test returned p = 0.011 for a 0.5 Å median difference — **significance manufactured
from collapsed variance**. Always check seed spread before trusting a p-value.

**Small samples mislead.** JAK3 A572V read p = 0.00094 from 8 seeds and **p = 0.035** from 16. No
8-seed result is quoted as settled.

**Stop quoting pLDDT as support.** The GPCR benchmark below finds R² = 0.046 between pLDDT and
correctness (ipTM reaches 0.49). pLDDT appears in every run and says almost nothing about whether the
conformational state is right.

### Two 2026 benchmarks that bear on this work

**KinConfBench** (Sun & Head-Gordon, *npj Drug Discovery* **3**, 33): 2225 kinase chains, Boltz-2 /
Chai-1 / Protenix / RFAA. *"Geometric success metrics of a ligand pose do not correlate strongly with the
correct kinase conformational state"* — our two-metric finding, independently. They document the same
mode collapse (~0.1 Å ensemble diversity) and recommend **MSA sub-sampling and templates** as the fix —
our method. Critically, they **exclude pseudokinase domains** — *"such as members of the Janus Kinase
family"* — so the JH2–JH1 question is outside the best current kinase benchmark, and they call for
exactly this project's next step: predicting how *"drug-resistant mutations alter the conformational
ensemble."*

**GPCR cofolding** (Schrödinger, *npj Drug Discovery* **3**, 30): pLDDT is a poor correctness signal;
co-folding methods carry a conformational prior (*"tend to predict inactive receptor structures"*), the
same kind of bias as the AF2 polarity in section 1.

---

## 8. The catalytic domain conformation is constant — the signal is entirely interdomain

Labels from **Kincore-standalone2** (Dunbrack lab, the same tool KinConfBench uses), run on every
structure available. Kincore locates the catalytic (JH1) domain by HMM and assigns the DFG motif,
X-DFG dihedral, αC-helix, salt bridge, activation loop termini and spine.

| structure | Kincore label |
|---|---|
| AF2 JAK1 / JAK2 / JAK3 / TYK2 | `Inactive_DFGin_BLAminus_SBin_NTout_CTout` |
| **4OLI** (experimental closed, TYK2) | `Inactive_DFGin_BLAminus_SBin_NTout_CTout` |
| ma-l9b1f (closed) · ma-a1sai (open) | `Inactive_DFGin_BLAminus_SBin_NTout_CTout` |
| JAK3 wild type · M592F · A572V · A573V | `Inactive_DFGin_BLAminus_SBin_NTout_CTout` |
| TYK2 wild type · P982A · V678F | `Inactive_DFGin_BLAminus_SBin_NTout_CTout` |
| **7T6F** (cryo-EM active dimer) | `Inactive_DFGin_None_SBout_NTout_CTout` |

**All 23 structures give the identical label**, the single exception being the cryo-EM active dimer,
which differs only by a broken salt bridge and an unassignable X-DFG dihedral — plausibly local
resolution in that loop — and is *not* labelled Active either.

### Three consequences

1. **The measurement choice is validated.** Mutations change nothing in the catalytic domain's own
   conformation — not the DFG motif, not the αC-helix, not the activation loop. Everything this project
   detects lives in **where JH1 sits relative to JH2**, which is what the arrangement metric reports.
   There was nothing to find in the kinase-domain state, and now that is measured rather than assumed.

2. **One explanation for JAK3 class 2 is eliminated.** Section 4 listed three candidate reasons why
   M511I, A573V and R657Q tighten the closed arrangement instead of opening it; one was *"the metric
   reports packing rather than catalytic competence"*. Their kinase domains are in exactly the same
   state as wild type's, so that is not the explanation. The remaining candidates are the **missing
   nucleotide mechanism** (JAK3 oncogenic hyperactivity is reported to depend on ATP binding to JH2,
   which we do not model) and **tighter is not more populated**.

3. **It bounds what this pipeline can say.** Unphosphorylated, ligand-free JAK models sit in one
   catalytic conformation regardless of sequence or MSA depth. Any question about active-site competence
   requires phosphorylation or a bound nucleotide, neither of which is modelled here.

Note that all four AF2 models carry this same inactive label while **AF2 JAK1/JAK2 are open and AF2
JAK3/TYK2 are closed** (section 1) — independent confirmation that the catalytic-domain state and the
interdomain arrangement are orthogonal descriptions.

Tooling: `github.com/DunbrackLab/Kincore-standalone2`, requires HMMER. Runs on our existing PDB files in
seconds, no GPU.

---

## 9. Next experiments



1. ~~KinCoRe labelling of our JH1 domains~~ — **done, see section 8.** Result: the catalytic
   conformation is identical across every structure, so all signal is interdomain.
2. **Co-fold TYK2 + deucravacitinib.** The drug binds JH2 and is thought to stabilise the closed state,
   which TYK2 never reaches unaided. If the ligand pulls the model closed, it is doing genuine
   ligand-induced reasoning; if not, that is apo-drift — tested on the one JAK with an experimental
   closed structure to check against.
