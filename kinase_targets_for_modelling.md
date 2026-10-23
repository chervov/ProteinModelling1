# Kinases where our multi-domain conformational modelling applies

*23 October 2026. Companion to `new_methods_summary20261023.md`.*

---

## 1. What makes a kinase a candidate

Our method varies **MSA depth** and **template presence/source** to recover **inter-domain
arrangements** — where a regulatory module docks onto, or releases from, the kinase domain. The JAK
case is JH2 (pseudokinase) docking onto JH1.

This is **not** the axis that Kincore and KinConfBench describe. Those classify the **intra-domain**
active-site state (DFG-in/out, αC-in/out) *within* the kinase domain. A kinase can be DFG-in while
its regulatory domain is either docked or released — the two axes are orthogonal.

A kinase is a candidate when **all three** hold:

1. **A regulatory module that docks onto the kinase domain** — SH3-SH2, PH, pseudokinase, CaM-binding
   segment, juxtamembrane, GS domain, autoinhibitory domain.
2. **Two arrangements are experimentally known**, or at least one is known and the other credibly
   modelled — otherwise there is no reference to score against.
3. **Multi-domain structures exist**, not just the isolated kinase domain. *Kincore counts below are
   kinase-domain structures and do not establish this* — it must be checked per target in the PDB.

---

## 2. Tier 1 — the strongest candidates

Classic, well-characterised autoinhibition with both states solved, and good structural coverage.

| gene | mechanism | Kincore N | active | inactive | states | why |
|---|---|--:|--:|--:|--:|---|
| **ABL1** | myristoyl + SH3-SH2 clamp | 192 | 20 | 172 | 6 | the textbook assembled/disassembled pair; **DFG 44 in / 88 out / 58 inter** — balanced on both axes |
| **SRC** | SH3-SH2 clamp | 96 | 10 | 78 | 6 | the canonical closed↔open kinase |
| **LCK** | SH3-SH2 clamp | 78 | 48 | 30 | 5 | best active/inactive balance in the SRC family |
| **HCK** | SH3-SH2 clamp | 92 | 6 | 86 | 4 | full-length autoinhibited structures exist |
| **BTK** | PH-TH-SH3-SH2 | 294 | 4 | 290 | 6 | large multi-domain literature; drug-relevant |
| **SYK** | tandem SH2 | 206 | 36 | 140 | 4 | autoinhibited ↔ ITAM-released |
| **AKT1** | PH-domain clamp | 80 | 14 | 66 | 3 | PH-in / PH-out is a clean two-state problem |
| **BRAF** | CRD / 14-3-3 autoinhibition | 436 | 8 | 426 | 8 | **DFG 252 in / 160 out**; monomer↔dimer |
| **LRRK2** | ROC-COR-kinase-WD40 | 84 | 14 | 70 | 6 | genuinely multi-domain; cryo-EM in two states |
| **EIF2AK2 (PKR)** | pseudokinase/kinase-like tandem | 24 | 4 | 20 | 3 | nearest architectural analogue to the JAKs |
| **ERN1 (IRE1)** | kinase-RNase tandem | 100 | 16 | 78 | 5 | oligomerisation-coupled conformational change |
| **MAP2K1 (MEK1)** | helix-A autoinhibition | 244 | 12 | 232 | 6 | well-populated both states |
| **PAK1** | autoinhibitory domain (AID) | 138 | 18 | 116 | **9** | most conformational states of any candidate |
| **CHEK2** | SCD-FHA docking | 92 | 4 | 88 | 3 | dimerisation-coupled activation |
| **MELK** | UBA domain | 106 | 4 | 64 | 7 | UBA-docked vs released |

---

## 3. Tier 2 — by mechanism class

Good coverage; the two-state question is less sharply defined or multi-domain structures are sparser.

**Juxtamembrane autoinhibition (receptor tyrosine kinases)** — the JM segment folds back onto the
kinase domain; activation releases it. The largest single class.

| gene | N | act | inact | states | | gene | N | act | inact | states |
|---|--:|--:|--:|--:|---|---|--:|--:|--:|--:|
| MET | 270 | 4 | 266 | 8 | | IGF1R | 148 | 4 | 142 | 7 |
| FGFR1 | 298 | 6 | 292 | 7 | | KDR (VEGFR2) | 108 | 4 | 104 | 7 |
| FGFR2 | 210 | 10 | 200 | 4 | | MERTK | 134 | 4 | 130 | 7 |
| EPHA2 | 162 | 4 | 146 | 6 | | NTRK1 | 128 | 4 | 124 | 5 |
| KIT | 136 | 36 | 94 | 3 | | ALK | 136 | 4 | 132 | 5 |
| FGFR4 | 112 | 4 | 108 | 6 | | DDR1 | 86 | 4 | 82 | 4 |
| INSR | 52 | 14 | 38 | 4 | | CSF1R | 48 | 6 | 42 | 3 |

**CaM / regulatory-segment autoinhibition** — CAMK2A (54), DAPK1 (164), PHKG1 (40), CAMK1 (16),
DAPK3 (32), CASK (64). CAMK2 is attractive: the regulatory segment occludes the substrate site and
the holoenzyme assembles into a hub.

**GS-domain receptors** — ACVR1 (326), TGFBR1 (118), ACVR2A (16). The GS domain is an explicit
autoinhibitory element released by type-II receptor phosphorylation; ACVR1 is disease-relevant (FOP).

**PAK family** — PAK1 (138), PAK4 (108), PAK2 (20). The AID is a *trans*-autoinhibitory element.

**UBA / KA1** — MARK3 (50), SIK3 (46), MARK2 (28), MARK1 (24).

**Regulatory-subunit systems** — PRKACA (164), PRKG1 (38), PRKCB (24), PRKCQ (22). These need the
partner chain modelled, so they are a different experiment from single-chain multi-domain folding.

**Other docking/adaptor** — AURKA (474, and 134 DFG-inter), MAP4K1 (208), RIPK2 (144), RIPK1 (128 —
**124 of them DFG-out**, the most out-shifted kinase in the set), MAP3K5 (120), PDPK1 (164),
STK10 (54), ULK1 (60).

---

## 4. Priority order, and why

| rank | target | the specific reason |
|---|---|---|
| 1 | **ABL1** | both arrangements solved, both DFG states abundant, enormous literature — the best validation target |
| 2 | **SRC / LCK / HCK** | the canonical SH3-SH2 clamp; three paralogues give a family replicate the way the JAKs did |
| 3 | **EIF2AK2 (PKR)** | closest architecture to the JAKs outside the family — tests whether our pseudokinase/kinase result generalises |
| 4 | **BTK** | 294 structures, drug-relevant, multi-domain autoinhibition well described |
| 5 | **AKT1** | PH-in/PH-out is the cleanest binary inter-domain question available |
| 6 | **LRRK2** | hardest and most interesting — four domains, cryo-EM states, disease variants |
| 7 | **BRAF** | autoinhibition plus dimerisation; 14-3-3 makes it a two-chain problem |
| 8 | **MET / EPHA2 / KIT** | juxtamembrane class, where a *family* sweep is cheap once one works |

---

## 5. Caveats

1. **Kincore counts are kinase-domain structures.** They establish that a kinase is well studied;
   they do **not** establish that multi-domain or full-length structures exist. Each target needs a
   PDB check for constructs spanning the regulatory module before modelling.
2. **The mechanism assignments are from the structural-biology literature, not a database query.**
   They should be verified per target.
3. **Two reference structures are required** for our arrangement metric — one per state. Where only
   the autoinhibited form is solved, the released form has to come from a related kinase or a model,
   which weakens the comparison exactly as it did for JAK1.
4. **Our own JAK results are not yet externally validated** (see `new_methods_summary20261023.md`
   §4: AF2-DB and AF3 disagree with our pipeline on JAK2 and JAK3). Extending to a kinase with
   *both* arrangements experimentally solved — ABL1 or SRC — would test the method where the answer
   is already known, which is the right next step before trusting it on new targets.

*Data: `data/kincore/top50_kinases_conformations.csv`, `data/kincore/autoinhibition_candidates.json`
(129 genes across 15 mechanism classes, with Kincore counts). Source: Kincore, Modi & Dunbrack,
NAR 2022, snapshot fetched 2026-10-23.*
