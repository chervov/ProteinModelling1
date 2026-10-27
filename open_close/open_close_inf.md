# "Open" and "closed" mean at least three different things in the JAK literature

*Written 27 October 2026. A terminology note, not a result. Its purpose is to stop a reader of our
work from assuming we mean something we do not.*

---

## 1. The problem in one table

Three conformational transitions in JAK kinases are all routinely called "open → closed". They
differ by more than an order of magnitude in scale and are measured on completely different parts
of the protein.

| axis | what moves | scale | who uses this sense |
|---|---|--:|---|
| **G-loop** | the glycine-rich loop folds over the ATP pocket on ligand binding | **a few Å** | Sanachai et al. 2020 |
| **DFG-in/out** | Asp and Phe of the DFG motif swap places at the start of the activation loop | **~10 Å** | Kincore, KinConfBench, Gizzio et al. |
| **JH2–JH1** | the whole pseudokinase domain docks onto or releases the kinase domain | **~80 Å** | **this project**, Jeanpierre/Debeaupuis, Shan et al., Lupardus et al. |

**This project always means the third.** When our documents say a structure is open or closed, we
mean the inter-domain arrangement: where JH1 sits relative to JH2 and FERM. We never mean the
G-loop, and we never mean DFG.

A reader who knows the ATP-site literature will default to one of the first two. The three senses
need to be distinguished explicitly every time, because the words alone do not do it.

---

## 2. Why the three cannot substitute for one another

**They are orthogonal, not nested.** A JAK can be DFG-in while JH1 is either docked or released;
it can have a closed G-loop in either arrangement. Knowing one tells you nothing about the others.

Two consequences matter for us:

1. **Kincore and KinConfBench cannot validate our open/closed calls.** They classify the
   *intra-domain* active-site state. We measure the *inter-domain* arrangement. KinConfBench's
   60–80 % accuracy figures are not about the property we measure.
2. **Equally, our results are not duplicative of theirs.** The four-JAK arrangement matrix measures
   multi-domain autoinhibitory docking, which their benchmark does not cover at all.

### Scale, measured in our own data

From `reference_states.md`, the JH2–JH1 axis in our reference panel:

| state | FERM–JH1 centroid distance |
|---|---|
| closed / autoinhibited | **40–45 Å** |
| active dimer (7T6F-like) | **~84 Å** |
| open | **92–94 Å** |

A ~50 Å range on the FERM–JH1 measure, against a few Å for the G-loop. The G-loop transition would
be invisible at the resolution at which we classify states, and our transition is far too large to
be described by any active-site metric.

**One internal caveat, also from `reference_states.md`.** Even within our own axis, two measures
disagree: FERM–JH1 separates the three states cleanly, but JH2–JH1 centroid distance puts closed at
38–40 Å and open at 45–46 Å — a ~7 Å separation, too small to classify a single structure. This is
why the project uses the **arrangement metric** (JH1 Cα RMSD after superposing JH2, 15 Å threshold)
rather than a centroid distance. "Compact" and "closed" are also not the same thing: at shallow MSA
every seed can be compact by FERM–JH1 while sitting 28 Å or more from the closed reference by
arrangement. See `open_close.md` and `mutation_analysis.md` §9.

---

## 3. The G-loop sense — Sanachai et al. 2020

**Kamonpan Sanachai, Panupong Mahalapbutr, Kiattawee Choowongkomon, Rungtiva P. Poo-arporn, Peter
Wolschann, Thanyada Rungrotmongkol**, "Insights into the Binding Recognition and Susceptibility of
Tofacitinib toward Janus Kinases", *ACS Omega* 2020 Jan 2; **5**(1):369–377.
DOI [10.1021/acsomega.9b02800](https://doi.org/10.1021/acsomega.9b02800) — title, journal, volume,
pages and author list verified against Crossref, 27 October 2026.

**What it is.** MD plus end-point free-energy study of tofacitinib bound to the **ATP sites** of the
three JAK kinase domains. 3 × 500 ns per complex in AMBER16; binding energies by MM-PBSA, MM-GBSA,
QM/MM-GBSA (PM3 and SCC-DFTB) and SIE; plus their own ADP-Glo IC₅₀ measurements. Structures: JAK1
**3EYG**, JAK3 **3LXK**, JAK2 **4D0X** with the ligand placed by superposition.

**Their open→closed is the G-loop** folding over the ATP pocket on ligand binding. Kinase domains
only — no JH2, no full-length construct — so the paper says nothing about autoinhibition.

**What is useful to us.** The hinge contacts are mapped precisely, with H-bond occupancies of
80–100 %: E957/L959 (JAK1), E930/L932 (JAK2), E903/L905 (JAK3). Mapped onto TYK2 by global
alignment these become **E979** (conserved in all three) and **V981** (leucine in the other three,
valine in TYK2) — immediately adjacent to **P982**, the one variant in our campaign with a
significant conformational result. The paper also supplies experimental IC₅₀ anchors for two of our
four proteins.

**What we found when we checked the hinge against the DMS.** Their occupancies are **backbone**
contacts. A missense substitution swaps the side chain and leaves the backbone intact, so binding
should survive — and the DMS confirms it. What the hinge positions *do* show is abundance damage:
**84 % and 68 % of their variants fall in the bottom abundance quartile** against a 25 % baseline,
median abundance −0.297. Destabilising, not binding-disrupting.

**A caveat on their central claim, visible in their own numbers.** They report affinity
JAK3 > JAK2 ≈ JAK1 and call it agreement with experiment. Their own IC₅₀s are JAK3 20.6 nM and
JAK2 26.9 nM — a 1.3-fold difference, i.e. **0.16 kcal/mol**. Against that:

| method | predicted JAK3–JAK2 gap (kcal/mol) | overshoot vs their own experiment |
|---|--:|--:|
| MM-PBSA | 3.70 | **23×** |
| MM-GBSA | 5.13 | **32×** |
| PM3/MM-GBSA | 8.64 | **55×** |
| SCC-DFTB/MM-GBSA | 11.60 | **73×** |
| **SIE** | **0.13** | **1×** |

The method they feature least — SIE — is the only one that reproduces the measured selectivity; the
QM-corrected methods they present as most sophisticated are the furthest off. Four methods get the
sign right and the magnitude wrong by up to 73×.

This is the same pattern we hit with PyRosetta ΔΔG, and a useful external precedent for it:
**end-point free-energy methods rank acceptably and quantify badly**, which is why this project
clips to ranks rather than trusting magnitudes. See `conclusions_ddG_difference_feature.md`.

Also note JAK2 had **no tofacitinib co-crystal** — the pose was superimposed from another complex,
and that modelled pose carries the whole selectivity comparison.

---

## 4. The DFG sense — Kincore, KinConfBench, Gizzio

### 4.1 What DFG-in/out is

DFG is a conserved Asp-Phe-Gly motif at the start of the activation loop, in the ATP pocket.

| | Asp (D) | Phe (F) | catalysis |
|---|---|---|---|
| **DFG-in** | points **into** the ATP site, coordinates Mg²⁺ | sits in the adjacent hydrophobic back pocket | **active-capable** |
| **DFG-out** | flipped **out**, no Mg²⁺ coordination | swings **into** the ATP site | **inactive** |

Asp and Phe essentially swap places — a ~180° backbone flip. A third bin, **DFG-inter**
("DFG-up"), is intermediate. A second axis, **αC-in/out**, describes whether the αC-helix Glu forms
its salt bridge with the β3 Lys.

Dunbrack's nomenclature combines a **spatial** label (DFGin / DFGout / DFGinter) with a **dihedral**
label from the backbone dihedrals (BLAminus, BLBplus, ABAminus, BBAminus, …). **DFGin-BLAminus is
the genuinely active configuration.**

**Why this axis is the basis of kinase drug classification.** Type I inhibitors bind the DFG-**in**
(active-like) ATP site — most kinase drugs. Type II inhibitors require DFG-**out**: the Phe vacating
the back pocket opens an allosteric cavity the drug extends into, with **imatinib on ABL1** the
classic case. You cannot design a type II inhibitor against a kinase you cannot model in DFG-out.

**The PDB is lopsided.** In the Kincore table we pulled — 26,322 structures, 466 human kinases —
**DFGin-BLAminus is 57.5 % of all structures**. That bias is what KinConfBench's "apo-drift"
finding points at: models trained on the PDB inherit the prior and default to the common state. The
balanced kinases are therefore the interesting benchmark targets: **ABL1** (44 in / 88 out / 58
inter), **RIPK1** (4 / 124), **KIT** (52 / 82), **BRAF** (252 / 160). See
`kinase_targets_for_modelling.md` and `data/kincore/`.

### 4.2 References

- **Kincore** — Modi & Dunbrack, "Kincore: a web resource for structural classification of protein
  kinases and their inhibitors", *Nucleic Acids Research* 2022, **50**:D654–D664, DOI
  [10.1093/nar/gkab920](https://doi.org/10.1093/nar/gkab920). Web resource
  classifying every protein-kinase structure in the PDB by DFG-motif and αC-helix geometry, so you
  can look up which kinases have been *observed* in more than one state and in which PDB entries.
- **The nomenclature behind it** — Modi & Dunbrack, "Defining a new nomenclature for the structures
  of active and inactive kinases", *PNAS* 2019, **116**:6818–6827, DOI
  [10.1073/pnas.1814279116](https://doi.org/10.1073/pnas.1814279116).
- **KinConfBench** — code and curation at
  [github.com/THGLab/KinConfBench](https://github.com/THGLab/KinConfBench); all inference results
  and analysis files on Figshare, DOI
  [10.6084/m9.figshare.31986663](https://doi.org/10.6084/m9.figshare.31986663). **1,420 unique
  systems — 43 apo targets and 1,377 holo complexes** from 437 human catalytic kinase domains, PDB
  snapshot 2025-08-01, annotated through the Dunbrack KinCoRe pipeline. Explicitly curates holo/apo
  pairs, i.e. the same kinase in two states. Its central finding: across three diffusion-based
  cofolding models (Boltz-2, Chai-1, Protenix) predictions default to the apo state for a large
  fraction of holo complexes **even when those complexes are in the training set**, and the drift
  worsens for complexes deposited after the training cutoff.
- **Gizzio et al.**, *Biochemical Journal* 2026, **483**:1281–1317 — defines active conformations
  for all 437 human catalytic kinase domains; the UniProt list KinConfBench starts from.

---

## 5. The JH2–JH1 sense — ours

- **Lupardus, Ultsch, Wallweber, Bir Kohli, Johnson & Eigenbrot**, "Structure of the
  pseudokinase–kinase domains from protein kinase TYK2 reveals a mechanism for Janus kinase (JAK)
  autoinhibition", *PNAS* 2014, **111**:8025–8030 — **4OLI**, deposited title "The
  pseudokinase/kinase protein from JAK-family member TYK2", 2.8 Å. The **only experimental closed
  structure in the JAK family**, and the reference for every interface measurement in this project.
- **Shan, Gnanasambandan, Ungureanu, Kim, Hammarén, Yamashita, Silvennoinen, Shaw & Hubbard**,
  "Molecular basis for pseudokinase-dependent autoinhibition of JAK2 tyrosine kinase",
  *Nature Structural & Molecular Biology* 2014 — the D. E. Shaw / Hubbard model placing the disease
  mutations at the pseudokinase–kinase interface and proposing that **JAK2 V617F relieves
  autoinhibition** by stabilising an α-helix in the SH2–JH2 linker.
- **Jeanpierre / Debeaupuis** JAK1 open and closed models — the pipeline this project reproduces and
  critiques. Files `ma-a1sai` (open) and `ma-l9b1f` (closed); see `conclusions_ddG_difference_feature.md`
  for the negative result on their key ΔΔG difference feature.
- **Howard et al.**, *eLife* 2026, DOI
  [10.7554/eLife.110149.2](https://doi.org/10.7554/eLife.110149.2) — the TYK2 deep mutational scan
  (11 arms, 23,732 variants) used throughout. MaveDB `urn:mavedb:00001270-a` and `00001271-a`.
  See `TYK2/DMS_Howard2026/`.
- **Gakovic, Ragimbeau, Francois-Newton, Krolewski & Pellegrini**, *J Biol Chem* 2008,
  PMID [18456658](https://pubmed.ncbi.nlm.nih.gov/18456658/) — TYK2 **V678F**, the V617F-equivalent
  construct: increased catalytic activity, constitutive STAT3 phosphorylation, **no notable effect
  on IFN-α signalling**. The π-stacking requirement behind the JAK2 mechanism is *Biochemistry* 2010,
  PMID [20958061](https://pubmed.ncbi.nlm.nih.gov/20958061/) (F595–F617). See
  `mutation_analysis.md` §3.5.

---

## 6. Practical rule for our write-ups

When a document in this repository says **open** or **closed** without qualification, it means the
**JH2–JH1 inter-domain arrangement**, measured as JH1 Cα RMSD against the reference panel after
superposing JH2, with a 15 Å match threshold.

Where a document discusses the ATP site or cites Sanachai, Kincore, KinConfBench or Gizzio, the
sense must be named explicitly — "G-loop closed", "DFG-in", "DFGin-BLAminus" — and never left as
bare "closed".

## Related documents

| file | what it covers |
|---|---|
| `reference_states.md` | the reference panel and the measured open/closed criteria on our axis |
| `open_close.md` | the arrangement metric itself, and compact ≠ closed |
| `mutation_analysis.md` | §9 burial at the JH2–JH1 interface; §3.5 the TYK2 678 position |
| `kinase_targets_for_modelling.md` | the Kincore-derived candidate list and DFG state counts |
| `conclusions_ddG_difference_feature.md` | why we clip ΔΔG to ranks rather than trusting magnitudes |
| `TYK2/DMS_Howard2026/` | the DMS data, its 11 arms and their quality |
