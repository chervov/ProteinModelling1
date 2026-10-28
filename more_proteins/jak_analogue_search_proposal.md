# Finding JAK-like proteins: what to search for, and why the current criterion is inverted

*Written 28 October 2026. A proposal, consolidating what was measured across
`more_proteins_review.md`, `twostate_vs_floppy.md` and the PTPN2 case study. The central argument is
that screening for inter-domain **variation** selects against the proteins we want.*

---

## 1. The problem with "look for a range of domain arrangements"

JAK is interesting **because its closed state is almost unobserved**. There is exactly one
experimental structure of the autoinhibited pseudokinase–kinase pair (4OLI, TYK2), no full-length
experimental closed structure in the family, and every SWISS-MODEL lineage descends from the
extended cryo-EM structures 7T6F/8EWY. That is why the project exists: the drug-relevant state is
the one the standard method cannot reach.

A screen that requires **two templates spanning the domain pair in different arrangements**
therefore selects for proteins whose question is **already answered**. Both states are in the PDB;
there is nothing left to model. Demonstrated concretely:

| | |
|---|---|
| JAK1 FERM–JH1 in the production screen | **9.0 Å spread** over 3 observations, *all extended* |
| JAK1 FERM–JH1 with ModelArchive + orthologs (Stage 1) | **54.5 Å** |
| JAK's own JH2–JH1, the drug-relevant motion | **10.3 Å — ranks 87th of 270 pairs** |

**The screen, applied to JAK, would discard JAK.** That is the acceptance test any replacement has
to pass.

Three further measured problems, all in the review documents:

- **71% of mobile pairs are floppy** — 147 of 207 have zero inter-domain contacts in any structure, so no closed state exists to model (`twostate_vs_floppy.md` §2)
- **76% of >20 Å hits rest on one same-protein template** — the range is target-vs-homolog (`more_proteins_review.md` §3)
- **Ranking by `n_parents` ranks by fame**, which is why the results are integrins, CFTR and P-glycoprotein — textbook cycles, already solved

---

## 2. Invert the criterion

What distinguishes JAK is not variation. It is this:

> **A compact state with a real inter-domain interface exists — and the models do not reproduce it.**

That is a *gap* signature, not a variation signature. Operationally, three streams:

### Stream A — architecture (cheap, proteome-wide)

- **≥2 folded domains** with an intervening linker
- **Use InterPro, not UniProt `Domain` features.** The current screen's own limitation note says UniProt omits RTK ectodomain subdomains, so EGFR, ERBB2, ERBB4 and LTK are absent despite being strong candidates. PTPN2 showed the converse: 1 domain in UniProt, correctly excluded.
- Exclude pairs where either domain is predominantly disordered (SPOT-disorder or pLDDT < 70), since ΔΔG and arrangement are both undefined there

### Stream B — does a closed state with an interface exist? *(the discriminator)*

For each pair, find the **most compact** available conformation from *any* source and count
inter-domain heavy-atom contacts within 5 Å. Pass if ≥ ~20 residue-pair contacts.

Reference scale, from this project: TYK2 JH2–JH1 in 4OLI is **21 interface residues / 1147 Å²**;
P982 alone makes 28 cross-domain atom contacts and V678 makes 0. SHP2 in 4DGX gives **64** for
N-SH2↔PTP and **0** for the other two pairs — one specific interface, the JAK pattern.

**Sources must go beyond SWISS-MODEL.** This is the single biggest fix:

| source | why it matters |
|---|---|
| **PDB directly** (not SWISS-MODEL relays) | relays are in author numbering and are rejected by the gate |
| **ModelArchive** | carries the closed JAK1 model `ma-l9b1f`; Stage 1 found it only after missing it on the first pass |
| **Vertebrate orthologs** | Stage 1 took FERM–JH1 from 10 to 41 observations by pooling 11 |
| **AlphaFold-Multimer / AF3 intra-chain** | can produce compact states no template provides |
| **Literature** | for cases with a described but un-deposited interface |

### Stream C — do the models miss it? *(what makes it a target)*

A pair qualifies as a modelling target when Stream B finds an interface **and**:

- **AlphaFold places the domains apart** — i.e. the AF arrangement is outside or at the extended end of whatever range exists
- **high inter-module PAE with low intra-module PAE** — the modules are individually confident, their relative placement is not
- **few or no template lineages reach the compact state** — the JAK situation exactly

**Critical caution on PAE** (`twostate_vs_floppy.md` §5): high inter-module PAE **cannot
distinguish a two-state switch from a floppy linker** — both mean "AlphaFold doesn't know". PAE is
necessary, never sufficient. **Stream B is what makes it sufficient**, and nothing in
`more_proteins/` currently tests Stream B.

### Scoring

Rank on **Stream C given Stream B**, not on variation. A useful single number:

```
JAK-likeness  =  (contacts in the most compact state)          # is there a closed state at all
              ×  (1 - fraction of template lineages reaching it)   # do models miss it
              ×  (inter-module PAE / intra-module PAE)          # is the placement uncertain
```

JAK scores high on all three. An integrin scores low on the second (both states abundantly solved).
A floppy linker scores zero on the first.

---

## 3. The acceptance test — run this before trusting any output

A labelled control set, with the required verdict. **If the screen does not reproduce these, it is
not measuring the right thing.**

### Must rank at the top

| protein | pair | closed-state evidence | why models miss it |
|---|---|---|---|
| **JAK1/2/3, TYK2** | FERM/SH2 ↔ JH1 | **4OLI** (21 res, 1147 Å²); ModelArchive `ma-l9b1f` | all SWISS-MODEL lineages extended; AF flips between >90%-identity orthologs |
| **FAK (PTK2)** | FERM ↔ kinase | [Lietha et al., *Cell* 2007](https://www.cell.com/fulltext/S0092-8674(07)00680-0): FERM bridges both kinase lobes across the active-site cleft; F596D at the interface activates; same conformation in 3 crystal forms | the **best positive control** — JAK's architecture with one fewer domain, and the intact autoinhibited crystal exists |
| **SHP2 (PTPN11)** | N-SH2 ↔ PTP | measured here on 4DGX: **64 contacts**, other pairs 0; E76K activates | **currently absent from the 3,247-protein screen** despite 119 SWISS-MODEL structures incl. full-module templates at 99.8% identity |
| **SHP1 (PTPN6)** | N-SH2 ↔ PTP | same architecture, 14 PDB entries | **screened and recorded `n_parents = 0`** despite `3ps5.1.A` (99.8%) and `2b3o.1.A` (100%) spanning 1–529 |
| **SRC, ABL1, BTK/Tec** | SH3+SH2 ↔ kinase | 2SRC is `DFGin-BLBplus`/Inactive; established in `open_close/open_close_inf.md` §2c | partially present already (large SH3↔kinase ranges) |

### Must rank low — the negative controls

| protein | pair | why it must fail |
|---|---|---|
| **ACTN2/ACTN4** | CH2 ↔ EF-hand | **zero contacts in every structure**; a rigid 280 Å rod. Currently the screen's "sharpest AlphaFold failure" |
| **AKT1** | PH ↔ kinase | **invariant across 11 parents**; only AlphaFold places it elsewhere |
| IGF2R | MRH1 ↔ MRH12 etc. | zero contacts, 180 Å apparent displacement — tandem repeats on a string |
| TMPRSS15 | MAM ↔ CUB2 | 0.2 Å centroid spread, 73 Å superposition RMSD, **zero contacts** |

**SHP1 is the best debug case in the whole set**: a single protein, reproducible, with known-good
full-length templates at 99.8–100% identity, that the pipeline scores as zero. Whatever rejects it
is probably rejecting others silently — the zero-parent rows in the 3,247-protein screen deserve an
audit, not a filter.

---

## 4. Candidates already identified, with the evidence

From the contact analysis over the 161 committed structures (`interface_contacts.csv`). These pass
Stream B cleanly; Stream C still needs checking for each.

### ABC transporters — the strongest two-state result in the data

| gene | pair | n | compact d / contacts | extended d / contacts |
|---|---|--:|---|---|
| **ABCB1** (P-gp) | ABC transporter 1 ↔ 2 | 3 | 28.0 Å / **78** | 62.2 Å / **0** |
| **CFTR** | ABC transporter 1 ↔ 2 | 3 | 27.1 Å / **64** | 46.1 Å / **0** |
| **ABCC2** | ABC transporter 1 ↔ 2 | 4 | 27.6 Å / **63** | 49.5 Å / **0** |
| **ABCC4** | ABC transporter 1 ↔ 2 | 4 | 27.5 Å / **60** | 70.2 Å / **0** |

Four paralogues, independent template sets, ~60–78 contacts closed and **exactly zero** open. Better
sampled than JAK (CFTR 21 entries, ABCB1 23). **Likely to fail Stream C** precisely because both
states are well solved — which makes them the ideal *method validation* set rather than modelling
targets.

### DEAD-box helicases — the closest mechanistic parallel

Two RecA-like lobes closing on RNA and ATP. Pair: Helicase ATP-binding ↔ Helicase C-terminal.

| gene | n | compact / contacts | extended / contacts |
|---|--:|---|---|
| **EIF4A3** | 3 | 29.3 Å / **56** | 47.5 Å / 3 |
| **EIF4A1** | 4 | 29.2 Å / **54** | 47.6 Å / 3 |
| **DDX3Y** | 4 | 31.4 Å / **44** | 50.7 Å / **0** |
| **DDX3X** | 3 | 32.0 Å / **38** | 50.7 Å / **0** |
| **DDX23** | **8** | 34.0 Å / **33** | 56.3 Å / **0** |
| **SMARCAD1** | 5 | 28.4 Å / **53** | 133.4 Å / **0** |

DDX23 at 8 structures is the best-sampled single protein in the set; DDX3X/DDX3Y are a paralogue
replicate.

### Worth checking next, by architecture

Not yet measured — all two-state inter-domain autoinhibition with a described interface, and all
the right shape:

**EGFR ectodomain** (tethered ↔ extended, domain II–IV tether — and one of the four the UniProt
domain gap currently excludes) · **Vinculin** (head–tail, large buried interface) · **Talin**
(R9–F3) · **CaMKII** · **SOS1** (DH-PH autoinhibition) · **p47phox** · receptor PTPs with tandem
catalytic domains.

---

## 5. Concrete plan

**Phase 0 — fix the known failures (1–2 days).** These are bugs, not design questions.

1. **Debug SHP1 (P29350).** Single protein, reproducible, known-good templates. Find out whether the 80% numbering gate or the ≥50% domain-coverage rule rejects it.
2. **Audit the zero-parent rows** in `nonkinase_screen_full.csv` — SHP1 shows that `n_parents = 0` can mean "gate failed", not "no data".
3. **Add PTPN11** and explain its absence from the candidate gene set.
4. **Add ModelArchive and ortholog pooling to the production path**, then re-run the 86 multi-domain-covered kinases. Stage 1's lift was 10 → 41 observations for one pair.
5. **Switch to InterPro domains** to recover EGFR, ERBB2, ERBB4, LTK.

**Phase 1 — add the discriminator (2–3 days).** Compute the Stream B contact count for every pair,
in the most compact available conformation from *all* sources. Gate on it. This removes ~71% of the
current candidates and is the step that separates switches from tethers. Code already exists:
`interface.py`.

**Phase 2 — the acceptance test (1 day).** Run the labelled set in §3. **Required outcome: JAK, FAK
and SHP2 in the top tier; ACTN2 CH2↔EF-hand and AKT1 not.** Do not proceed if this fails.

**Phase 3 — score on the gap, not the range.** Stream C: AF placement, inter/intra-module PAE ratio,
fraction of template lineages reaching the compact state. **This is where the PAE work already done
elsewhere plugs in** — and it needs joining to this analysis, which is currently impossible because
no PAE data is committed under `more_proteins/`.

**Phase 4 — report per pair, with all three metrics.** Centroid spread (translation only),
superposition RMSD (translation + rotation, with the flip check sup/sep < 1.8), and contacts
(interface). Never collapse to one number: each has a documented failure mode and they disagree
one-directionally.

---

## 6. The two measurement lessons, stated once

**Centroid distance is a conservative lower bound on mobility.** Over 296 pairs it never over-calls,
but **66 of the 94 pairs it calls rigid are mobile by superposition** (28 strongly). ρ = 0.776
between the metrics.

**Superposition RMSD has its own artefact.** 24 of 296 rows (8%) have sup/sep > 1.8, indicating a
180° Kabsch flip rather than motion — ACTN2 CH2↔EF-hand reports 515 Å in a 280 Å protein at
sup/sep = 1.95.

**Only the contact count has no geometric failure mode**, needs no superposition and no distance,
and is the one that answers the question actually being asked: *is there a closed state to model?*

---

## 7. One-line answer

**Stop searching for proteins whose domains are seen in many arrangements. Search for proteins that
have a real inter-domain interface which AlphaFold and the available templates fail to produce — and
require the search to rank JAK, FAK and SHP2 at the top before believing anything else it says.**
