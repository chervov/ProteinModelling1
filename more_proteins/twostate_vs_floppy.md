# Mobile is not the same as two-state: separating JAK-like switches from floppy linkers

*Written 28 October 2026, prompted by the question: "what I am afraid is that there are proteins
where domains are linked by a thin linker — that would mean they are too mobile, and I am not sure
a closed form for them would make sense at all." It would not. This quantifies the problem on the
committed structures and names the candidates that survive.*

---

## 0. The answer

**The fear is correct and the effect is large. Of 207 domain pairs that are mobile by a
superposition metric, 147 (71%) have essentially no inter-domain contacts in *any* structure.**
They are flexible tethers, not conformational switches. For those, a "closed form" is not a state —
it is wherever the crystallographer caught them.

Only **60 pairs (29%)** show the JAK signature: a substantial interface in the compact structure
that is absent in the extended one.

The discriminator is cheap and robust: **count inter-domain heavy-atom contacts within 5 Å in the
most compact and the most extended structure.** It needs no superposition, so it is immune to the
failure modes of both metrics discussed in `more_proteins_review.md`.

Reference scale from this project: TYK2 **P982 alone** makes 28 cross-domain contacts in 4OLI,
**V678** makes 0, and the whole JH2–JH1 interface buries 1147 Å² over 21 residues
(`mutation_analysis.md` §3, §9).

---

## 1. Why mobility alone is the wrong criterion

Three distinguishable situations all produce large inter-domain variation:

| | interface in compact state | defined states? | closed form meaningful? |
|---|---|---|---|
| **Two-state switch** (JAK, FAK, SRC) | **large, specific** | **two** | **yes** |
| Flexible tether (beads on a string) | none | continuum | **no** |
| Rigid rod sampled badly | none | one | no — the variation is artefact |

The `more_proteins/` screen ranks on variation, so it ranks all three together. Worse, the two
failure classes produce the *biggest* numbers, because an unconstrained domain can go anywhere while
a real hinge is limited by its interface.

The screen's own top results illustrate this. ACTN2 α-actinin was reported as "the sharpest
AlphaFold failure in the project" — and it is a **rigid rod**, not a switch. Its CH2↔EF-hand pairs
have **zero** inter-domain contacts in every structure. The 280 Å separation is architecture, not
mobility.

---

## 2. The measurement

`interface.py` → `interface_contacts.csv`, 297 (protein, pair) rows over the 161 committed
structures. For each pair, inter-domain contacts are counted as **distinct residue pairs with heavy
atoms within 5 Å**, in the most compact and most extended structure.

Classification, using the project's own 15 Å arrangement threshold for "mobile" and a 12-residue-pair
floor for "has an interface":

| class | pairs | |
|---|--:|---|
| **FLOPPY** — mobile, no interface in any state | **147** | **71% of mobile pairs** |
| **TWO-STATE** — interface in compact, lost in extended | **60** | 29% |
| mobile but interface retained throughout | 21 | hinge within a persistent interface |
| rigid or not measurable | 68 | |

The floppy set is led by exactly the cases the reports highlighted:

| gene | pair | contacts (max over all structures) | superposition RMSD |
|---|---|--:|--:|
| ACTN4 | CH 2 ↔ EF-hand 1 | **0** | 516 Å |
| ACTN2 | CH 2 ↔ EF-hand 1 | **0** | 515 Å |
| IGF2R | MRH 1 ↔ Fibronectin type-II | **0** | 191 Å |
| IGF2R | MRH 7 ↔ MRH 12 | **0** | 182 Å |
| DICER1 | Helicase ATP-binding ↔ RNase III 1 | **0** | 147 Å |

Zero contacts with a 500 Å apparent displacement is the clearest possible statement that the
metric is measuring something other than a conformational switch.

---

## 3. What survives: the real JAK analogues in your own data

Two families come out cleanly, both well-sampled and both textbook two-state systems:

### 3.1 ABC transporters — the strongest result

The nucleotide-binding domains dimerise on ATP and separate on hydrolysis. A genuine, functional,
two-state cycle with a large defined interface.

| gene | pair | n | compact d / contacts | extended d / contacts |
|---|---|--:|---|---|
| **ABCB1** (P-glycoprotein) | ABC transporter 1 ↔ 2 | 3 | 28.0 Å / **78** | 62.2 Å / **0** |
| **CFTR** | ABC transporter 1 ↔ 2 | 3 | 27.1 Å / **64** | 46.1 Å / **0** |
| **ABCC2** | ABC transporter 1 ↔ 2 | 4 | 27.6 Å / **63** | 49.5 Å / **0** |
| **ABCC4** | ABC transporter 1 ↔ 2 | 4 | 27.5 Å / **60** | 70.2 Å / **0** |

Four paralogues, independent template sets, converging on the same pattern: ~60–78 contacts closed,
**exactly zero** open. That is a cleaner two-state signature than JAK's own, because both states are
experimentally sampled many times — `nonkinase100b_report.md` notes CFTR has 21 entries and ABCB1 has
23. Where JAK has one crystal of the closed pseudokinase–kinase pair and models for the rest, the
ABC transporters have both ends of the cycle in the PDB repeatedly.

### 3.2 DEAD-box helicases — the closest mechanistic parallel

Two RecA-like domains close around RNA and ATP, and separate when empty. The domain pair is
**Helicase ATP-binding ↔ Helicase C-terminal**:

| gene | n | compact d / contacts | extended d / contacts |
|---|--:|---|---|
| **EIF4A3** | 3 | 29.3 Å / **56** | 47.5 Å / 3 |
| **EIF4A1** | 4 | 29.2 Å / **54** | 47.6 Å / 3 |
| **DDX3Y** | 4 | 31.4 Å / **44** | 50.7 Å / **0** |
| **DDX3X** | 3 | 32.0 Å / **38** | 50.7 Å / **0** |
| **DDX23** | **8** | 34.0 Å / **33** | 56.3 Å / **0** |
| **SMARCAD1** | 5 | 28.4 Å / **53** | 133.4 Å / **0** |
| DICER1 | 5 | 27.3 Å / **56** | 39.4 Å / 24 |

DDX23 at 8 distinct structures is the best-sampled single protein in the set. Note DDX3X and DDX3Y
are paralogues giving near-identical numbers — a family replicate.

### 3.3 Others worth a look

**ACTN2/ACTN4 CH1↔CH2** (46 contacts compact, 0 extended, 5 structures for ACTN4) — the actin-binding
head. Note this is a *different* pair from the floppy CH2↔EF-hand rod; the same protein contributes
to both lists, which is itself a useful warning against scoring proteins rather than pairs.

**Tandem RRMs** — SF3B4 (43/0, n=5), U2AF2 (16/0), SNRPB2 (22/1). Known to close on RNA. Small
interfaces, so treat as provisional.

**EHD2/EHD3 G-domain↔EH** (21/0 each) and **IGF2R MRH pairs** — IGF2R dominates the two-state list
by count, but it has 15 tandem MRH domains, so most pairs are neighbours in a chain and many of its
*other* pairs are in the floppy list. Its contribution needs per-pair, not per-protein, reading.

---

## 4. Literature: JAK open/closed in your sense, and the analogous systems

### 4.1 JAK, inter-domain

Checked this session:

- **Lupardus, Ultsch, Wallweber, Bir Kohli, Johnson & Eigenbrot**, *PNAS* 2014, 111:8025–8030 — **4OLI**, the TYK2 JH2–JH1 autoinhibited crystal, 2.8 Å. The only experimental closed structure in the family.
- **Shan, Gnanasambandan, Ungureanu, Kim, Hammarén, Yamashita, Silvennoinen, Shaw & Hubbard**, *Nat Struct Mol Biol* 2014 — the JAK2 autoinhibition model; V617F acts through the SH2–JH2 linker.
- [**Glassman et al., *Science* 2022**](https://www.science.org/doi/10.1126/science.abn8933) — cryo-EM of a full-length JAK1–receptor complex; the autoinhibited model was built by **docking 4OLI into the FERM–SH2–PK of the mJAK1 cryo-EM structure**. This is the provenance of the "block is rigid, JH1 moves" picture and explains why `stage1_jak_report.md` found the block identical to 0.1 Å across 7T6F and 8EWY — it was rigid-body placed, as that report correctly suspects.
- [**Structural models of full-length JAK2**, bioRxiv 2019](https://www.biorxiv.org/content/10.1101/727727v1.full) — integrative models; states plainly that **no full-length JAK2 structure exists**. Proposes JH2 trapping the JH1 activation loop and blocking αC.
- [**Crystal structure of the FERM–SH2 module of human JAK2**, *PLOS ONE* 2016](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0156218) — the FERM and SH2 domains and their linkers "interact intimately to form an integrated structural module". **Direct experimental support for the rigid-block result**, independent of the cryo-EM rigid-body placement.
- Earlier **electron microscopy of JAK1** reported distinct **compact and elongated** states, i.e. monomeric JAKs sampling an equilibrium. This is the closest literature statement of your open/closed in the inter-domain sense.
- [**Structural Regulation and Therapeutic Perspectives of JAK2**, MDPI 2025](https://www.mdpi.com/2813-3757/4/2/17) — notes that full-length cryo-EM in both states remains a **future goal**.

**So the gap is real**: there is no experimental full-length JAK in the closed state. The project is not duplicating existing work.

### 4.2 FAK is the closest architectural analogue

[**Lietha, Cai, Ceccarelli, Li, Schaller & Eck**, "Structural basis for the autoinhibition of focal
adhesion kinase", *Cell* 2007, 129:1177–1187](https://www.cell.com/fulltext/S0092-8674(07)00680-0) —
verified this session:

- crystal structure spanning **FERM–linker–kinase**; the FERM domain **bridges the N- and C-lobes of the kinase and extends across the active-site cleft**
- the principal contact is **FERM F2 lobe ↔ kinase C-lobe**
- **interface mutations activate the kinase** (F596D)
- the linker carrying Tyr397 binds a groove on F1, sequestering the autophosphorylation site
- the same conformation appeared in **two further crystal forms**, arguing against a packing artefact

A FERM domain clamping a kinase domain through a specific interface, released by interface
mutations — that is JAK's architecture with one fewer domain, and it has what JAK lacks: a
crystal structure of the intact autoinhibited arrangement. **If you want a positive control for the
whole approach, FAK is it.** I could not find a paper comparing FAK and JAK autoinhibition directly,
and the search returned nothing on buried surface area at the FAK interface, so treat the analogy as
a structural observation rather than a citable claim.

### 4.3 Other two-state inter-domain autoinhibition systems

From domain knowledge, not verified this session — each would need checking before use:

| system | mechanism | why relevant |
|---|---|---|
| **SRC family** | SH3+SH2 clamp on the kinase back face, latched by pTyr527 | established in `open_close/open_close_inf.md` §2c; 2SRC is `DFGin-BLBplus` |
| **ABL1** | SH3–SH2 clamp plus myristoyl pocket | two-state, drug-relevant |
| **BTK / Tec family** | PH-TH and SH3–SH2 modules; [PHTH conformational heterogeneity drives multiple regulatory states](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10945472/) | already in the kinome table with large SH3↔kinase ranges |
| **SHP2 / PTPN11** | N-SH2 occludes the PTP active site; E76K activates | **PTPN11 is in your structure set**; textbook two-state |
| **Vinculin** | head–tail autoinhibition, large buried interface | non-kinase positive control |
| **Talin** | R9–F3 autoinhibition | |
| **EGFR ectodomain** | tethered ↔ extended, domain II–IV tether | the RTK ectodomain case your UniProt domain features currently miss |
| **Integrins** | bent ↔ extended | already found; §2 shows PSI↔I-EGF2 has an interface, CH2↔EF-hand does not |

---

## 4.4 Worked case: PTPN2 — no, and the reason is instructive (28 October 2026)

Asked whether PTPN2 has an open/closed arrangement in this project's sense. **It cannot: it has one
domain.**

UniProt P17706, 415 residues:

| | |
|---|---|
| **Domain** | Tyrosine-protein phosphatase, **5–275 — the only one** |
| Active site | C216, phosphocysteine intermediate |
| Region | 346–415 ER location; 376–415 mediates STX17 interaction |

Residues 276–415 are regulatory **regions**, not domains, so no domain pair exists and PTPN2 is
correctly absent from every table in `more_proteins/` (verified: 0 rows in `kinome480_*`,
`nonkinase_screen_full.csv`, and both tables computed here).

The SWISS-MODEL repository agrees — 16 structures, widest genuine span **1–302** (7f5o, 7f5n):
catalytic domain plus a little. There is nothing to measure.

**PTPN2 is regulated, but by a different mechanism.** Its disordered C-terminal tail is an
*intramolecular* brake —
[Nature Communications 2021](https://www.nature.com/articles/s41467-021-27633-6) shows by NMR, SAXS
and XL-MS that the tail autoinhibits by generating steric bulk near the active site rather than
occupying it, and that the Integrin-α1 cytosolic tail displaces it and fully activates the enzyme.
That is **tail-on-domain**, not domain-on-domain: there is no second folded module to dock, so there
is no closed state in our sense and no arrangement to model.

Worth noting for the project's biology regardless: **TCPTP dephosphorylates JAK1 and JAK3 but not
JAK2**, while PTP1B does the reverse ([FEBS J review](https://febs.onlinelibrary.wiley.com/doi/10.1111/j.1742-4658.2012.08563.x)).
So PTPN2 is a direct JAK regulator — biologically central, structurally not analogous.

A caution on terminology: the PTP literature does use "open/closed" for the **WPD loop** over the
active site, which would be a fourth sense to add to the three in `open_close/open_close_inf.md`
(G-loop, DFG, JH2–JH1). But the WPD-dynamics work I found is on **PTP1B**, not TCPTP, and for TCPTP
the search returned no WPD open/closed result — so do not attribute it to PTPN2 without checking.

### The real finding: SHP2 and SHP1 are what you wanted, and both are missing from the screen

**PTPN11 (SHP2)**, Q06124, 593 residues — three domains, exactly the architecture:

```
SH2-1    6-102
SH2-2  112-216
PTP    247-517      (active site C459)
```

One structure file sits in `more_proteins/structures/` — `PTPN11_SHP2_template-4DGX.pdb` — named
unlike every other file (no accession, no provider), so it was added by hand as a control rather
than produced by the pipeline. I measured it:

| pair | centroid distance | **inter-domain contacts** |
|---|--:|--:|
| **SH2-1 ↔ PTP** | 30.3 Å | **64** |
| SH2-2 ↔ PTP | 41.6 Å | **0** |
| SH2-1 ↔ SH2-2 | 33.8 Å | **0** |

Domain coverage 100 / 100 / 94%. **This is the JAK pattern precisely**: one specific pairwise
interface carrying the autoinhibition, the other pairs merely co-located. For scale, TYK2's JH2–JH1
interface is 21 residues and 1147 Å². The N-SH2 blocking the PTP active site, released by E76K and
the other activating mutations, is textbook two-state inter-domain autoinhibition — and it is a
**phosphatase**, i.e. a functional counterpart to JAK rather than another kinase.

**And the templates exist in quantity.** SWISS-MODEL returns **119 structures** for Q06124,
including full-module spans:

```
  4-537  len 534  PDB         4h34
  2-535  len 534  PDB         4gwf
  1-534  len 534  PDB         5xzr
  2-534  len 533  SWISSMODEL  4nwg.1.A   identity 99.814
  3-533  len 531  PDB         4nwf
```

**Yet PTPN11 appears nowhere in the 3,247-protein non-kinase screen.** Not scored zero — absent.

**PTPN6 (SHP1)**, P29350, same three-domain architecture (SH2-1 4–100, SH2-2 110–213, PTP 244–515),
*was* screened:

```
nonkinase_screen_full.csv:
  P29350, n_parents=0, n_entries=0, PTPN6, n_dom=3, n_pdb=14
```

**n_parents = 0** — no multi-domain template survived the gate. But SWISS-MODEL offers
`3ps5.1.A` at **99.8%** identity and `2b3o.1.A` at **100%**, both spanning **1–529**, the entire
module. Three domains, 14 PDB entries, full-length same-protein templates — and the pipeline
recorded nothing.

### Why this matters

This is the **same failure as §2 of `more_proteins_review.md`**, in a new place. There, JAK's own
closed state was missing because the SWISS-MODEL lineage only carries the extended cryo-EM
structures. Here, two proteins with abundant, high-identity, full-module templates produce zero
usable observations.

The two cases differ in cause — JAK's is source coverage, SHP1's looks like the gate or the ≥50%
domain-coverage rule — but the consequence is identical: **the screen is silent on exactly the
proteins that best match the target phenotype.** SHP1 and SHP2 should be the easiest possible hits.

**Recommended actions:**

1. **Debug SHP1 (P29350) specifically.** It is a single-protein, reproducible failure with known-good templates at 99.8–100% identity. Whatever rejects it is likely rejecting others silently — the 3,247-protein screen's zero-parent rows deserve an audit, not a filter.
2. **Add PTPN11 to the screen.** Its omission from the candidate list needs explaining; if the list was built from a gene set that excluded it, that set needs checking too.
3. **Use SHP2 as the second positive control alongside FAK** (§4.2). Both have a crystallised autoinhibited state with one specific interface; FAK is the kinase analogue, SHP2 the phosphatase one. A pipeline that misses both is not yet measuring the right thing.
4. **Do not look for open/closed in PTPN2, PTPN1 or other single-domain PTPs.** Their regulation is tail- or loop-based. The multi-domain PTPs — PTPN11, PTPN6, and the receptor PTPs with tandem catalytic domains — are where the question applies.

---

## 5. The PAE warning — important

You asked about PAE as a selection signal. **High inter-module PAE cannot distinguish a two-state
switch from a floppy linker.** Both produce the same thing: AlphaFold does not know where the module
goes, so predicted error between modules is high.

That means **selecting on PAE will enrich for flexible tethers**, which are precisely the cases
where a closed form is meaningless. PAE is a good *necessary* filter — a protein with low
inter-module PAE has one arrangement and can be dropped — but it is not sufficient, and on its own
it points in the wrong direction.

The sufficient condition is an interface. Concretely, a candidate should pass all three:

1. **low intra-module PAE** — the modules are individually confident
2. **high inter-module PAE** — their relative placement is uncertain
3. **a compact structure with a real inter-domain interface** (≳20 residue-pair contacts, or ≳500 Å² buried) **that the extended structure lacks**

Criteria 1–2 are what the PAE work gives. **Criterion 3 is the one nothing in `more_proteins/`
currently tests**, and it is the one that removes 71% of the candidates.

---

## 6. Both distance metrics have failure modes; the contact count does not

For completeness, and against my own §5.1b: the superposition metric has its own pathology.

ACTN2/ACTN4 CH2↔EF-hand report **515 Å RMSD** — impossible in a 280 Å protein. Diagnosis:

| pair | mean separation | sup RMSD | ratio |
|---|--:|--:|--:|
| ACTN2 CH2↔EF-hand 1 | 264.2 Å | 515.3 Å | **1.95** |
| ACTN4 CH2↔EF-hand 1 | 264.6 Å | 516.1 Å | **1.95** |
| ACTN2 CH2↔EF-hand 2 | 264.1 Å | 513.4 Å | **1.94** |

A ratio of ~2.0 is a **180° superposition flip**: where the aligned domain is small or pseudo-symmetric
and the measured domain is far away, Kabsch can settle on a near-inverted solution that swings the
distant domain to the opposite side, giving RMSD ≈ 2× the lever arm. Domain coverage was checked and
is 100% in all three ACTN2 files, so this is not a coverage artefact.

**24 of 296 rows (8%) have sup/sep > 1.8 and should be treated as flip-suspect.**

| metric | blind to | inflated by |
|---|---|---|
| centroid distance | hinge rotation (66/94 "rigid" pairs are mobile) | — |
| superposition RMSD | — | lever arm; 180° flips at long range (8% of rows) |
| **inter-domain contacts** | **neither — no superposition, no distance** | partial domain coverage |

So report all three. The contact count is the one that answers "is there a closed state", and it is
the only one with no geometric failure mode.

---

## 7. What I would change in the screen

1. **Add the contact criterion and make it a gate, not a column.** A pair with no interface in its most compact structure is not a JAK candidate however mobile it is. This removes 147 of 207.
2. **Score pairs, not proteins.** ACTN2 is simultaneously the best (CH1↔CH2, 46/0) and the worst (CH2↔EF-hand, 0/0) case in the set. A per-protein verdict is meaningless here.
3. **Treat PAE as necessary, not sufficient** (§5), and say so wherever the PAE candidate list is used.
4. **Add FAK and SHP2 as positive controls.** Both have a crystallised autoinhibited state with a defined interface. If the pipeline does not rank them highly, it is not detecting the right thing — and FAK's FERM–kinase clamp is the same architecture as JAK's.
5. **Promote the ABC transporters and DEAD-box helicases** out of the general results and into the candidate list. They are better sampled than JAK itself and genuinely two-state.

## 8. Files

| file | contents |
|---|---|
`interface.py` | the contact computation |
`interface_contacts.csv` | 297 rows: compact/extended distance and contact counts per pair |
`superpose.py`, `superposition_vs_centroid.csv` | the superposition metric, from `more_proteins_review.md` §5.1b |

Reproduce:

```bash
python3 -I superpose.py     # needs the 161 structures from more_proteins/structures/
python3 -I interface.py
```
