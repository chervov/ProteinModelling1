# Mutation analysis — predicting conformational effects without GPU

Living document. Appended to as each analysis completes; newest sections at the bottom of each part.
Started 2026-10-16. Companion to the GPU runs in `JAK3/`, `TYK2/` and the top-level `conclusions_*.md`.

## 1. The variants under analysis

| # | Protein | Variant | UniProt | Domain | Verified in sequence |
|--:|---|---|---|---|---|
| 1 | TYK2 | **V678M** | P29597 | JH2 (pseudokinase) | ✅ V at 678 |
| 2 | TYK2 | **P982A** | P29597 | JH1 (kinase) | ✅ P at 982 |
| 3 | JAK2 | **V1110E** | O60674 | JH1 | ✅ V at 1110 |
| 4 | JAK2 | **G571R** | O60674 | JH2 | ✅ G at 571 |
| 5 | JAK2 | **V578I** | O60674 | JH2 | ✅ V at 578 |
| 6 | JAK2 | **L805I** | O60674 | JH2 | ✅ L at 805 |
| 7 | JAK3 | **Y581C** | P52333 | JH2 | ✅ Y at 581 |

All seven were checked against the UniProt reference sequences; the wild-type residue matches in every case.

## 2. Cross-JAK equivalent positions

Obtained by global pairwise alignment (BLOSUM62, free end gaps) of the full-length sequences.

| Variant | TYK2 | JAK2 | JAK3 | JAK1 |
|---|---|---|---|---|
| TYK2 V678M | **V678** | V617 | M592 | V658 |
| TYK2 P982A | **P982** | P933 | P906 | P960 |
| JAK2 V1110E | A1156 | **V1110** | P1082 | P1136 |
| JAK2 G571R | G634 | **G571** | G546 | G610 |
| JAK2 V578I | V639 | **V578** | V553 | V619 |
| JAK2 L805I | L866 | **L805** | L777 | I845 |
| JAK3 Y581C | H667 | H606 | **Y581** | H647 |

Two observations fall straight out of this table:

- **TYK2 V678 is the classic activating position** — the same site as JAK2 V617F and JAK1 V658F.
  But **JAK3 carries methionine there natively (M592)**, so TYK2 V678M installs a residue that a
  functioning wild-type JAK already has. The activating substitution at this site is phenylalanine,
  not methionine, and the accepted V617F mechanism depends on the aromatic ring.
- **JAK2 L805I installs the residue JAK1 already has (I845)**, so it is close to a built-in negative control.
- **Proline is conserved at the P982/P933/P906/P960 position in all four JAKs** — a conserved proline
  at a domain interface is rarely incidental.

## 3. Structural analysis against the experimental closed structure (4OLI)

4OLI is the TYK2 JH2–JH1 crystal in the autoinhibited state (Lupardus et al., PNAS 2014, 2.8 Å) — the
**only experimental closed structure in the JAK family**. Every variant position was mapped onto 4OLI
(chain A, residues 579–1177) and analysed there.

### 3.1 Method

**Buried** means not reachable by a water-sized probe (1.4 Å radius). Solvent-accessible surface area
(SASA) was computed with Shake–Rupley, and normalised by residue-type maxima (Tien 2013) for relative
accessibility. Two distinct senses matter:

- **buried in the fold** — hidden inside the domain's own core, with or without a partner;
- **buried by the interaction** — exposed when the domain is alone, covered when the partner docks.
  Measured as **ΔSASA = SASA(domain alone) − SASA(in the closed complex)**.

Only the second kind changes the open/closed balance: those atoms cost energy *only* in the closed
state. The conventional threshold for an interface residue is ΔSASA > ~25 Å².

### 3.2 Results

The JH2–JH1 interface buries **2261 Å²** across **36 residues** with ΔSASA > 25 Å².

| Position (TYK2 numbering) | Variant it represents | Domain | Exposed alone | **ΔSASA on closing** | Cross-domain contacts < 5 Å |
|---|---|---|--:|--:|--:|
| **P982** | TYK2 P982A | JH1 | 47 % | **59.8 Å²** | **28** |
| V678 | TYK2 V678M | JH2 | 53 % | 17.2 Å² | **0** |
| A659 | (JAK3 A573) | JH2 | 7 % | 7.2 Å² | – |
| H667 | JAK3 Y581C | JH2 | 18 % | **0.0 Å²** | – |
| V639 | JAK2 V578I | JH2 | 0 % | **0.0 Å²** | – |
| L866 | JAK2 L805I | JH2 | 0 % | **0.0 Å²** | – |
| A1156 | JAK2 V1110E | JH1 | 8 % | **0.0 Å²** | – |

**Only P982 is at the interface.** Every other variant position buries 0.0 Å² on closing.

### 3.3 P982 in detail

Top interface residues by burial on closing:

| rank | residue | domain | ΔSASA |
|--:|---|---|--:|
| 1 | F672 | JH2 | 86.9 Å² |
| 2 | R901 | JH1 | 85.2 Å² |
| 3 | Y916 | JH1 | 83.0 Å² |
| 4 | **Q664** | JH2 | 75.8 Å² |
| 5 | T923 | JH1 | 75.8 Å² |
| … | | | |
| **9** | **P982** | **JH1** | **59.8 Å²** |

P982 ranks **9th of 520 residues**, contributing 2.6 % of the whole interface. Its JH2 partners are
**S663, Q664, V665, S666** — a contiguous stretch.

Contacts broken down per atom:

| atom | cross-domain contacts | survives P→A? |
|---|--:|---|
| backbone (N, CA, C, O) | 3 | yes |
| CB | 13 | yes |
| **CG** | **11** | **no** |
| **CD** | **1** | **no** |

Proline→alanine keeps CB and deletes CG and CD: **12 of 28 cross-domain contacts (43 %) are removed**,
at a residue that is solvent-facing on isolated JH1 and only buried on closing.

Sequence context: `...L-Q-L-V-M978-E-Y-V-P982-L-G-S-L...`. P982 sits immediately after the M978–E979–Y980–V981
stretch, which a 2023 modelling study of deucravacitinib identified as the JH1 β-stretch contacting JH2
in the autoinhibited state. (Their motif naming differs slightly from the sequence as read here; verify
against the primary text before citing.)

### 3.4 V678 in detail

V678 makes **zero** heavy-atom contacts with JH1 within 5 Å, and is 53 % exposed on isolated JH2. Its
17.2 Å² ΔSASA comes from sitting at the interface periphery where the probe is blocked at longer range,
not from contact. Any effect must be allosteric.

One route is worth noting: **F672 is the single largest interface residue (86.9 Å²) and lies six residues
from V678**, plausibly packed against the same segment. A substitution at 678 could reposition F672
without touching JH1 itself.

## 4. Predictions, and the reasoning behind each

| Variant | Predicted effect on the open/closed balance | Confidence | Basis |
|---|---|---|---|
| **TYK2 P982A** | **Destabilises closed specifically** | high (physics), moderate (detectability) | interface core; deletes 43 % of its cross-domain contacts; conserved proline; backbone-entropy term |
| **JAK3 Y581C** | local JH2 destabilisation, little arrangement change | low–moderate | ΔSASA 0.0 Å²; large side-chain deletion but not at the interface |
| **JAK2 G571R** | uncertain; exposed flexible loop | low | absent from 4OLI, only 52 neighbours in the JAK1 closed model — poorly ordered |
| **JAK2 V1110E** | fold destabilisation, not arrangement | moderate | buried in the JH1 core (8 % exposed), 36 Å from the interface; burying a charge |
| **TYK2 V678M** | little or none | moderate | no contacts; methionine lacks the aromatic ring the V617F mechanism needs; JAK3 has M natively |
| **JAK2 V578I** | near-neutral | high | fully buried in the JH2 core, conservative +CH₂ |
| **JAK2 L805I** | near-neutral | high | fully buried; installs the residue JAK1 already carries |

**Magnitude estimate for P982A.** Two contributions, both in the same direction: ~30–35 Å² of buried
interface surface lost (~1 kcal/mol), plus the backbone-entropy term from removing the only residue that
locks the backbone (~0.5–1 kcal/mol, favouring the unbound/open state). Total plausibly 1–2 kcal/mol
destabilisation of closed relative to open — roughly a tenfold equilibrium shift at body temperature.

**The honest caveat.** That is the physics. Whether the *modelling pipeline* detects it is separate:
OpenFold is driven heavily by the MSA, and a single substitution in a 1187-residue query barely changes
the MSA. The JAK1 and JAK2 mutation effects we have seen appeared as population shifts across seeds, not
as changed individual structures. With 16 seeds a ~6-seed swing is needed for p < 0.05.

## 5. Experimental designs proposed (GPU)

1. **Template release from 4OLI** — wild type and mutant started from the experimental closed structure,
   template active for recycles 1–3 then switched off, paired seeds. Measures which one *stays* closed.
   One-sided: detects destabilisation of closed, not stabilisation.
2. **Reciprocal test** — P982 grips S663/Q664/V665/S666 on JH2, and **Q664 is itself the 4th-largest
   interface residue**. Breaking the same contact from the JH2 side (Q664A) and reproducing the phenotype
   would be internal replication of the mechanism rather than a second guess.
3. **Mechanism split at position 982** — P982A (loses contacts + backbone constraint), P982G (upper bound),
   **P982L** (keeps side-chain bulk, loses only the backbone constraint). P982L isolates the entropy term.
4. **Negative control** — H667 or V639, both at 0.0 Å² interface burial.
5. **V678F rather than V678M** as the hotspot test: V678F is the substitution shown experimentally to
   raise TYK2 kinase activity, while methionine is what JAK3 carries as wild type.

## 6. Still to do

- [ ] Literature search for each of the seven variants (section 7)
- [ ] Sequence-based pathogenicity scores: PolyPhen-2, SIFT, CADD, REVEL, AlphaMissense (section 8)
- [ ] ΔΔG on open and closed conformations, the approach used by Jeanpierre et al. (section 9)
- [ ] In-silico alanine scan of all 36 TYK2 interface residues
- [ ] Burial analysis in each protein's **own** closed structure, not only via the TYK2 mapping

---

## 7. Literature search (2026-10-16)

Searched per variant. **None of the seven has a dedicated functional study.** What exists is context.

### TYK2 V678
- **V678F** (not our variant) is reported to **increase TYK2 kinase activity** — consistent with the
  equivalent JAK2 V617F and JAK1 V658F. No data found on **V678M**.
- This matters: the activating substitution at this position is the **aromatic** phenylalanine. Methionine
  is what JAK3 carries natively at the equivalent position (M592), so V678M is not expected to act like V678F.

### TYK2 P982
- **No literature found for P982 in any substitution.** The residue appears in no variant report located.
- Nearby context: a 2023 modelling study of deucravacitinib describes the JH1 β-stretch around M978 as
  contacting JH2 in the autoinhibited state. P982 is immediately C-terminal to it.
- **TYK2 P1104A** (rs34536443), the well-studied kinase-domain proline variant, is a **hypomorph**: catalytically
  impaired but still signalling through IFN-α/β, IL-6 and IL-10 (Li et al., J Immunol 2013); reduced type I IFN
  and IL-12/IL-23 responses; protective against several autoimmune diseases; associated with increased
  tuberculosis risk. Molecular dynamics work attributes the reduced activity to **stabilisation of inactive
  conformations**. A recent deep mutational scan reports reduced protein abundance and signalling.
  *Relevance:* a different proline in the same domain, also implicated in conformational equilibrium — but
  P1104A **stabilises** the inactive state, the opposite of what we predict for P982A.

### JAK2 G571
- **G571R not found.** The neighbouring **G571S** is reported in a patient with isolated erythrocytosis lacking
  V617F and exon 12 mutations (Leukemia Research Reports, 2016), treated with phlebotomy over three years.
  Its functional effect was **not established** — the authors propose only a putative role.
- G571 lies in exon 13, within the pseudokinase domain. Germline JAK2 pseudokinase variants are a recognised
  cause of hereditary erythrocytosis, distinct from polycythaemia vera in lacking clonal evolution.

### JAK2 V1110, L805, V578
- **No reports found for any of the three.** They appear in no clinical variant table located, and the
  curated JAK2 pathogenic list (V617F, R683G, R683S) does not include them.

### JAK3 Y581
- **Y581C not found.** Context: roughly half of clinical JAK3 mutations cluster in the pseudokinase (JH2)
  domain. Established activating JH2 alleles are **M511I, A572V, R657Q, V722I**, found in acute
  megakaryoblastic leukaemia, T-ALL, NK/T-cell lymphoma and related malignancies; A572V, V722I and P132T
  transform Ba/F3 cells to factor-independent growth (Walters et al., Cancer Cell 2006).
- Mechanism: hyperactivity of oncogenic JAK3 mutants **depends on ATP binding to the pseudokinase domain**,
  and the isolated JH2 is unstable and strongly stabilised by ATP (Frontiers in Oncology, 2018).

**Summary:** all seven are effectively uncharacterised. That makes the modelling genuinely predictive rather
than confirmatory, and it also means there is no functional ground truth to check against.

---

## 8. Sequence-based pathogenicity predictors

Retrieved from dbNSFP via the MyVariant.info API, 2026-10-16. Two known variants are included as controls.

| Variant | AlphaMissense | PolyPhen-2 | SIFT | CADD | REVEL | ESM1b | ClinVar |
|---|---|---|---|--:|--:|--:|---|
| **TYK2 V678M** | 0.30–0.42 amb. | 1.00 D | 0.001 D | 31.0 | 0.564 | −6.29 | Uncertain significance |
| **TYK2 P982A** | 0.37–0.53 amb. | 1.00 D | 0.002 D | 27.9 | 0.702 | **−11.22** | – |
| **JAK2 V1110E** | 0.29 B | **0.18 B** | 0.023 D | 23.0 | 0.477 | **−1.22** | – |
| **JAK2 G571R** | 0.27–0.36 amb. | 1.00 D | 0.002 D | **33.0** | 0.874 | −9.50 | – |
| **JAK2 V578I** | 0.24–0.34 B | 1.00 D | 0.000 D | 29.3 | 0.618 | −7.82 | – |
| **JAK2 L805I** | **0.15 B** | 0.91 P | **0.317 T** | 25.6 | **0.439** | −7.67 | – |
| **JAK3 Y581C** | **0.10–0.14 B** | 0.97 D | 0.001 D | **22.2** | **0.369** | −5.17 | – |
| *control:* JAK2 V617F | 0.33–0.39 amb. | 1.00 D | 0.002 D | 33.0 | 0.881 | −10.29 | **Pathogenic** |
| *control:* TYK2 P1104A | **0.82 P** | 1.00 D | 0.002 D | 26.1 | 0.586 | −9.86 | **Benign** |

D = damaging, P = possibly damaging / pathogenic, B = benign, T = tolerated, amb. = ambiguous.

### 8.1 The controls invalidate naive use of these scores here

- **AlphaMissense scores JAK2 V617F at 0.33–0.39 — benign to ambiguous.** This is the most famous pathogenic
  mutation in the family, ClinVar Pathogenic, the driver of polycythaemia vera.
- **AlphaMissense scores TYK2 P1104A at 0.82 — pathogenic.** ClinVar calls it **Benign**; it is a common
  protective variant.

Both controls are wrong, and in opposite directions. The reason is structural: these predictors are trained
largely on loss-of-function disease variants and on evolutionary conservation. A **gain-of-function** mutation
that shifts a conformational equilibrium need not look unusual to them, and a tolerated hypomorph at a
conserved site can look alarming. **For the question we are asking — which conformation does the protein
prefer — these scores should not be treated as evidence.** They are reported for completeness.

### 8.2 What the scores do suggest, read cautiously

- **P982A has the most extreme ESM1b score of all seven (−11.22)** — more extreme than V617F (−10.29).
  ESM1b is a protein language model, so this says the substitution is highly unexpected given evolutionary
  context, consistent with the proline being conserved across all four JAKs. This is the one predictor
  result that agrees with the structural analysis.
- **L805I is the mildest by consensus** — AlphaMissense 0.15, SIFT *tolerated*, REVEL 0.44. This matches the
  structural prediction (fully buried in the JH2 core, and it installs the residue JAK1 already has).
- **Y581C is the mildest by AlphaMissense (0.10–0.14), CADD (22.2) and REVEL (0.37)**, agreeing with the
  structural finding that it buries 0.0 Å² at the interface. Note PolyPhen-2 disagrees (0.97 D).
- **V1110E is the one case where structure and sequence predictors conflict.** PolyPhen-2 calls it **benign**
  (0.18) and ESM1b is nearly neutral (−1.22), while the structural reading was "buried charge, fold
  destabilising". The TYK2 mapping put the equivalent residue at only 8 % exposure, but **this needs checking
  in JAK2's own structure** rather than by homology — see section 6.
- **G571R has the joint-highest CADD (33.0, equal to V617F)** and high REVEL (0.874), but sits in a poorly
  ordered, exposed loop by the structural analysis. High conservation signal, low structural confidence.

### 8.3 Disagreement as a signal

Where PolyPhen-2 says "damaging" for six of seven variants while AlphaMissense says "benign" for four of them,
the predictors are not adding independent information — PolyPhen-2 is close to saturated on this gene family.
The useful discriminators here are **ESM1b** (continuous, and it ranks P982A first) and **the structural
ΔSASA analysis**, which is the only method that distinguishes interface from core.

---

## 9. Burial analysis in each protein's own closed structure

Section 3 mapped every variant onto TYK2/4OLI. That is sound for TYK2 but is homology for JAK2 and JAK3.
Repeated here in each protein's own structure, keeping **only the JH2+JH1 pair** so the comparison matches
4OLI (which contains no FERM-SH2):

- **TYK2** — 4OLI, experimental
- **JAK2** — our own closed prediction, `JAK2/runs/JAK2_20261015_082903/selected_closed.pdb`
  (ma-l9b1f template, default MSA; this closed state persists after the template is switched off)
- **JAK3** — our own closed prediction from today, `JAK3/runs/JAK3_20261016_125830/selected_closed.pdb`
  (13.4 Å from the JAK1 closed model, 16.8 Å from 4OLI — see `JAK3/JAK3_M592F.md`)

| Protein | JH2–JH1 interface | Variant | Exposed alone | **ΔSASA** | Contacts < 5 Å |
|---|--:|---|--:|--:|--:|
| **TYK2** | 1147 Å², 21 residues | **P982A** | 47 % | **59.8 Å²** | **28** |
| | | V678M | 53 % | **0.0 Å²** | 0 |
| **JAK2** | 1825 Å², 28 residues | V1110E | **30 %** | 0.0 Å² | 0 |
| | | G571R | **51 %** | 0.0 Å² | 0 |
| | | V578I | **0 %** | 0.0 Å² | 0 |
| | | L805I | **1 %** | 0.0 Å² | 0 |
| **JAK3** | 983 Å², 14 residues | Y581C | 20 % | 2.3 Å² | 0 |

### 9.1 Correction to section 3

Two numbers in section 3 need amending.

1. **The TYK2 interface is 1147 Å² across 21 residues, not 2261 Å² across 36.** The earlier figure compared
   each isolated domain against the *whole chain*, so burial caused by the inter-domain linker and flanking
   residues was wrongly attributed to the JH2–JH1 interface. Restricting the comparison to the JH2+JH1 pair
   gives the clean number. **P982's own ΔSASA is unchanged at 59.8 Å²**, and its rank and contact breakdown
   stand; only the denominator changes — P982 contributes ~5 % of the interface, not 2.6 %.
2. **V678's interface burial is 0.0 Å², not 17.2 Å².** By the clean measure it touches the interface not at all.
   The conclusion is unchanged and in fact strengthened.

### 9.2 Correction to a prediction: JAK2 V1110E

In section 4 I predicted V1110E would destabilise the JH1 fold by burying a charge, based on the TYK2
mapping putting the equivalent residue at 8 % exposure. **In JAK2's own structure V1110 is 30 % exposed** —
partially solvent-facing, neither at the interface nor in the core.

That removes the basis for the "buried charge" argument and resolves the conflict with the sequence
predictors, which called it the mildest structural case (PolyPhen-2 **benign** at 0.18, ESM1b only −1.22).
**Revised prediction: V1110E is unlikely to shift the conformational equilibrium, and unlikely to be strongly
destabilising.** Homology mapping across 44–51 % identity was not reliable for solvent accessibility, even
though it was reliable for identifying the interface.

### 9.3 The consistent picture

Across both analyses, **P982A is the only variant of the seven that touches a domain interface in any JAK.**
The others separate into three classes:

| Class | Variants | Expected effect |
|---|---|---|
| **Interface** | TYK2 P982A | shifts the open/closed equilibrium |
| **Buried in the JH2 core** | JAK2 V578I (0 % exposed), L805I (1 %) | fold stability only; both substitutions are conservative, so minimal |
| **Partially exposed, no interface** | JAK2 V1110E (30 %), G571R (51 %), JAK3 Y581C (20 %), TYK2 V678M (53 %) | local effects; any conformational effect must be allosteric |

Note the JAK2 and JAK3 structures are **our own predictions**, not experimental, so their interfaces carry
the model's uncertainty. The TYK2 numbers rest on a crystal structure. That the three give a consistent
answer — only P982 at an interface — is reassuring but not independent confirmation.

### 9.4 Revised prediction table

| Variant | Predicted effect on the open/closed balance | Confidence | Changed from section 4? |
|---|---|---|---|
| **TYK2 P982A** | destabilises closed specifically | high (physics), moderate (detectability) | no |
| JAK3 Y581C | local JH2 packing; little arrangement change | moderate | strengthened — 20 % exposed, 2.3 Å², no contacts |
| JAK2 G571R | little; exposed surface loop | moderate | strengthened — 51 % exposed |
| **JAK2 V1110E** | **little; partially exposed, not buried** | moderate | **reversed** — was "fold destabilising" |
| TYK2 V678M | little or none; allosteric at best | moderate | strengthened — 0.0 Å², 0 contacts |
| JAK2 V578I | near-neutral | high | no |
| JAK2 L805I | near-neutral | high | no |

---

## 10. JAK3 GPU results so far, and a numbering error worth recording (2026-10-16 18:15)

Paired runs at MSA 128/512, 16 seeds, no template, 15 recycles. Wild type reference run
`JAK3_20261016_125830`. Statistics by **Mann-Whitney** on the 16 final FERM–JH1 values — threshold-free,
and therefore preferable to the Fisher test on an arbitrary cutoff reported earlier.

| | median | mean | min | max | vs wild type |
|---|--:|--:|--:|--:|---|
| **wild type** | 50.5 | 48.9 | 42 | 56 | – |
| **M592F** | 55.0 | 64.9 | 44 | **97** | **p = 0.011, more extended** |
| **A573V** | **42.0** | 43.6 | 41 | 52 | **p = 0.0020, more compact** |

Two mutations in the pseudokinase domain move JAK3 in **opposite directions**, both significantly.
The Mann-Whitney p for M592F (0.011) is stronger than the Fisher value reported earlier (0.043) because
the rank test uses the whole distribution rather than a cutoff.

### 10.1 Error: A573V is not the reported allele

JAK3 has **two adjacent alanines, A572 and A573** (sequence `...L570-E571-A572-A573-S574-L575...`).
The activating mutation in the literature is **A572V** (Walters et al., Cancer Cell 2006 — identified in
an acute megakaryoblastic leukaemia line, transforms Ba/F3 cells to factor-independent growth).
**The run completed here used A573V, the neighbouring residue.**

This came from a variant list compiled earlier in the project where A573V was recorded as a "known
activating mutation". The residue identity was verified against the sequence — A is indeed at 573 — but
the *position* was never checked against the primary literature, and the adjacent alanine made the error
invisible to that check.

**Consequences:**
- The A573V result stands as an observation: a valine substitution at 573 makes JAK3 measurably **more
  compact** (p = 0.0020). But it must **not** be described as "a known activating mutation failed to open
  JAK3", because A573V is not that mutation.
- **A572V has been added to the queue and is running** (started 18:10), paired with the same wild type.
- M511I and R657Q were re-checked against the literature and **both are correct** as reported activating
  JH2 alleles.

### 10.2 What A573V may mean regardless

A573V sits immediately next to the canonical site, and tightening rather than loosening the arrangement is
a real, reproducible signal across 16 seeds. One reading is that the 572/573 region controls the
compactness of the pseudokinase–kinase packing, and that substitutions there can push it either way.
A572V will test that directly: if A572V opens JAK3 while A573V closes it, two neighbouring residues have
opposite roles — which would be a specific, checkable claim.

### 10.3 Caution carried forward

A relevant literature note: the hyperactivity of oncogenic JAK3 mutants is reported to **depend on ATP
binding to the pseudokinase domain** (Frontiers in Oncology, 2018). Our pipeline models no nucleotide at
all. If a clinically activating JAK3 mutation turns out not to open the arrangement in these runs, that
mechanism is the first explanation to consider — before concluding the mutation has no conformational
effect.

---

## 11. First TYK2 run: the 4OLI template assay does not work (2026-10-16 18:36)

`TYK2_20261016_130845` — TYK2 wild type, 4OLI as template in recycles 1–3 then switched off,
MSA 128/512, 15 recycles, 16 seeds, 219 min on a Colab A100.
Template identity to the query: **539 aligned residues, 99.6 % identical** (the two mismatches are the
crystal's kinase-dead D1023N), confirming the template was fetched and mapped correctly.

### Per-seed distance from the template arrangement (JH1 RMSD after superposing JH2, Å)

Every seed, every recycle:

| | recycle 1 | recycles 2–3 (template on) | recycles 4–15 (template OFF) | final |
|---|--:|--:|--:|--:|
| all 16 seeds | 1.5–3.4 | 1.0–1.5 | **1.1–2.2** | **1.4–1.9** |

**No seed moves.** Releasing the template changes nothing: the structures stay 1.4–1.9 Å from 4OLI for
all twelve template-free recycles. Overall JH2–JH1 distance spans 36.9–38.1 Å against the template's
39.0 Å, and FERM–JH1 only 38.5–47.2 Å.

### Why this kills the assay

The design assumed wild type would mostly stay closed while a destabilising mutation escaped more often.
With wild type at **16/16 seeds locked within 2 Å**, there is no dynamic range: the measurement cannot
distinguish any mutant from wild type, whatever the mutation does. This was listed as the main risk of
the design; it has happened.

Two explanations are consistent with the data, and they are not separated yet:
1. **The release worked, but the basin is deep.** 4OLI is a real crystal structure, and the MSA at this
   depth may independently favour the compact state, so the model has no reason to leave.
2. **The release did not take effect** — the `--template_recycles` patch may not be doing what it should.
   The trajectories show no discontinuity at recycle 3→4, which is what a working release would most
   likely produce.

Distinguishing them needs the "4OLI in all recycles" control. That is now lower priority than the
redesign below, because either way the assay is unusable as configured.

### Redesign

AF2 TYK2 sits at FERM–JH1 39.7 Å and JH2–JH1 37.2 Å; 4OLI sits at JH2–JH1 39.0 Å. **Both references are
compact, and only ~2 Å apart.** So TYK2's default predicted state is already the closed one, and no
template is needed to reach it — which makes the template a liability rather than a tool.

The TYK2 queue has been rebuilt around free prediction, the same design that produced a significant
result for JAK3 M592F (Mann-Whitney p = 0.011):

| # | run | seeds |
|--:|---|--:|
| 1 | TYK2 wild type, no template, MSA 128/512 | 8 |
| 2 | **TYK2 P982A**, no template, MSA 128/512, same seeds | 8 |
| 3 | TYK2 wild type, no template, MSA 512/8192 | 8 |
| 4 | TYK2 P982A, no template, MSA 512/8192 | 8 |

The question becomes "does P982A open TYK2 relative to wild type", measured the same way as every other
mutation in the project, rather than "does P982A escape a template we cannot escape from".

### Also learned
- **TYK2 exceeds a 40 GB A100 with a template.** The paired P982A run died of CUDA out-of-memory after
  11 of 16 seeds and 2.5 h; memory accumulates across seeds. TYK2 work moves to molab.
- Of 240 conformations, 211 were nearest the AF2 model and 29 nearest the mapped 4OLI template — the two
  being so close together means "nearest reference" carries little information for TYK2.

---

## 12. The metric was wrong: FERM–JH1 hides the autoinhibitory interface (2026-10-16 20:20)

A572V finished its first 8 seeds and looked unremarkable on FERM–JH1 (median 54.5 vs wild type 50.5,
p = 0.069). Classifying the structures against mapped references showed something FERM–JH1 could not see,
so every JAK3 run was re-analysed **per seed** on the domain-arrangement metric — JH1 RMSD against the
closed reference after superposing JH2, the measure used for JAK1 and JAK2 all along.

### Per-seed JH1-vs-closed distance (Å), MSA 128/512

| | n | values | median | vs wild type |
|---|--:|---|--:|---|
| **wild type** | 16 | 16 16 17 20 20 21 23 · 58 65 67 68 71 78 89 91 91 | 61.5 | – |
| **A573V** | 16 | **2 2 2 2 2 2 2 2 3 7 9 12** · 64 78 79 80 | **2.7** | **p = 0.0024, closer to closed** |
| **A572V** | 8 | **88 89 90 91 91 92 92 93** | **91.0** | **p = 0.00094, closed state abolished** |
| M592F | 16 | 23 43 48 55 57 58 61 61 67 67 69 83 84 84 91 92 | 64.0 | p = 0.29, no change |

### Three conclusions, two of which reverse what was written earlier

**1. Wild-type JAK3 at 128/512 is bistable, not uniformly compact.** Seven of sixteen seeds sit 16–23 Å
from the closed arrangement and nine sit 58–91 Å away. The earlier statement that wild type is
"uniformly compact" came from FERM–JH1, where every seed fell in a narrow 42–56 Å band. **FERM–JH1 was
masking a two-state distribution.** The project's top-level summaries need this correction.

**2. A572V, the canonical activating allele, does show the activating phenotype.** All 8 seeds land
88–93 Å from the closed arrangement: the autoinhibitory JH2–JH1 packing is **completely abolished**,
p = 0.00094. On FERM–JH1 the same run looked like a non-result (p = 0.069), because JH1 swings away from
JH2 without moving far from FERM. This is the clearest mutation effect measured in the project so far,
and it was nearly missed.

**3. A573V does the opposite, and does it hard.** Twelve of sixteen seeds sit within 12 Å of the closed
arrangement, eight of them at **2 Å** — essentially identical to both the AlphaFold JAK3 model and the
experimental TYK2 autoinhibited crystal 4OLI mapped onto JAK3 (2.3 and 2.4 Å for the representative
structure). Wild type's own closed-like seeds only reach 16 Å. **A573V locks JAK3 into a more canonical
autoinhibited geometry than wild type ever adopts.**

So the two adjacent alanines have **opposite roles**: 572 maintains the autoinhibitory packing, 573
loosens it. That was the specific prediction made when the A572V/A573V mix-up was found, and it holds.

### 4. M592F changes a different thing

M592F is significant on FERM–JH1 (p = 0.011, 5/16 seeds reaching the open state at 94 Å) but **not** on
JH2–JH1 arrangement (p = 0.29). It moves the kinase domain away from FERM while leaving the pseudokinase
packing much as wild type has it. A572V does the reverse. **These are two distinct structural effects,
and a single metric cannot report both.**

### Methodological consequence

Both measures are needed, and they answer different questions:

| metric | question | catches |
|---|---|---|
| FERM–JH1 centroid distance | how far is the kinase from FERM? | M592F |
| JH1 RMSD vs closed ref after superposing JH2 | is the autoinhibitory packing intact? | A572V, A573V |

JAK1 and JAK2 were classified on the arrangement metric throughout. JAK3 defaulted to FERM–JH1 because
the runs carried only the AlphaFold model as a reference, and "nearest reference" was therefore
uninformative. **All JAK3 conclusions in this project should be read on the arrangement metric**, and the
earlier JAK3 sections above are superseded on that point.

---

## 13. TYK2 free prediction: 128/512 is a ceiling (2026-10-16 21:10)

`TYK2_20261016_175018` — TYK2 wild type, **no template**, MSA 128/512, 15 recycles, 8 seeds, 84 min on
molab (RTX PRO 6000).

| seed | pLDDT | JH2–JH1 | FERM–JH1 | JH1 vs AF2 (closed-like) |
|--:|--:|--:|--:|--:|
| 0–7 | 81.9–82.2 | 46.5–46.7 | **93.2–93.8** | **81.9–82.5** |

**All 8 seeds are open, and essentially identical** — FERM–JH1 varies by 0.6 Å across the whole set.
The AlphaFold TYK2 model sits at FERM–JH1 39.7 Å, so free prediction at this depth lands ~54 Å away
from it and never visits the compact state.

### Why this matters, and what it costs

The TYK2 mutation pair was queued at 128/512 by analogy with JAK3, where that depth is bistable. For
TYK2 it is **saturated open**. P982A is predicted to *destabilise* the closed state, i.e. to push
further open — and there is nowhere further to go. A wild type/mutant comparison at this depth could
only ever return "no difference", for a reason that has nothing to do with the mutation.

The P982A run had been running 5 minutes when this was spotted; it was stopped.

### The family now has an ordered depth requirement

| protein | behaviour at 128/512 | depth where both states appear |
|---|---|---|
| JAK2 | mostly detached JH1 | 512/8192 (7 closed / 7 open) |
| JAK1 | bistable | 128/512 |
| JAK3 | **bistable** (7 of 16 seeds closed-like, 9 not) | 128/512 |
| **TYK2** | **uniformly open** | **shallower than 128/512 — unknown** |

TYK2 needs a **shallower** MSA than any other family member to access its closed state. That is a result
in itself: by this measure TYK2's evolutionary signal favours the open arrangement more strongly than
JAK1, JAK2 or JAK3.

It also sits oddly beside two other facts — the AlphaFold TYK2 model is compact, and the 4OLI-templated
run stayed locked in the closed state through twelve template-free recycles. The closed basin clearly
exists and is stable once entered; free prediction at 128/512 simply never enters it.

### Queue

Depth scan, wild type only, 8 seeds each: **96/384 → 64/256 → 32/64**. The P982A pairing waits for a
depth that shows both states. JAK1 reached the 7T6F-like arrangement at 64/256, and both JAK1 and JAK2
went compact at 32/64, so the transition is likely in that range.

### A caution about the uniformity

Eight seeds spanning 0.6 Å is far tighter than anything seen for JAK1, JAK2 or JAK3, where seeds at the
same depth differ by tens of Ångström. Either TYK2's landscape at this depth is genuinely a single deep
funnel, or the seeds are not diversifying as intended for this target. The depth scan will distinguish
these: a real funnel should break up as the MSA thins, whereas a seeding problem would persist.

---

## 14. A572V complete (16 seeds) — and a correction to section 12 (2026-10-16 21:20)

Section 12 reported A572V at **p = 0.00094** from its first 8 seeds. With all 16 seeds that becomes
**p = 0.035**. The first half was unusually uniform; the second half is not. **The earlier figure was
over-confident and should not be quoted.**

### All four JAK3 runs, 16 seeds each, MSA 128/512

Per-seed JH1 RMSD vs the closed reference after superposing JH2 (Å):

| | values | median |
|---|---|--:|
| **wild type** | 16 16 17 20 20 21 23 · 58 65 67 68 71 78 89 91 91 | 61.5 |
| **M592F** | 23 · 43 48 55 57 58 61 61 67 67 69 83 84 84 91 92 | 64.0 |
| **A573V** | 2 2 2 2 2 2 2 2 3 7 9 12 · 64 78 79 80 | 2.7 |
| **A572V** | 18 · 34 48 50 58 61 79 80 88 89 90 91 91 92 92 93 | 84.3 |

The distributions are **bimodal**, so the median is a poor summary and a rank test is not ideal either.
Counting seeds that retain the closed arrangement (wild type's closed cluster is 16–23 Å, so < 25 Å):

| | closed-like seeds | Fisher vs wild type | Mann-Whitney |
|---|--:|--:|--:|
| wild type | **7/16** | – | – |
| **M592F** | **1/16** | **p = 0.037** | p = 0.29 |
| **A572V** | **1/16** | **p = 0.037** | p = 0.035 |
| **A573V** | **12/16** | p = 0.149 (ns) | **p = 0.0024** |

### What each mutation actually does

**M592F and A572V both abolish the closed arrangement** — 7/16 seeds down to 1/16, p = 0.037 each.
They differ in what replaces it: M592F sends 5 seeds to the fully open state (FERM–JH1 94 Å, 3.3 Å from
the JAK1 open model), while A572V produces splayed arrangements matching no reference.

**A573V acts on the *quality* of the closed state, not its frequency.** The count barely moves (12/16
versus 7/16, not significant), but its closed seeds sit at **2 Å** from both the AlphaFold model and the
experimental TYK2 crystal, where wild type's only reach 16–23 Å. That is what the rank test detects
(p = 0.0024) and the count test cannot. A573V does not make the closed state more common — it makes it
much more canonical.

So the two neighbouring alanines still differ, but less starkly than section 12 implied: **572 is
required for the closed arrangement to form at all; 573 loosens its geometry without preventing it.**

### A caveat that needs watching

A572V's two 8-seed halves differ markedly despite identical settings, the same sandbox and the same MSA:

- seeds 0–7: **88 89 90 91 91 92 92 93** — tightly clustered, all far from closed
- seeds 8–15: **18 34 48 50 58 61 79 80** — spread across the whole range

Wild type shows within-run bimodality too, so this may simply be seed variance at n = 8. But if outcomes
cluster by *run* rather than by seed, the paired design is weaker than assumed and every 8-seed result
in this campaign needs re-reading. **Two things to check:** whether the same split appears in M511I and
R657Q, whose halves are running now, and whether the unusual 0.6 Å uniformity of the TYK2 128/512 run is
the same phenomenon.

### Methodological summary for the JAK3 set

| metric | M592F | A572V | A573V |
|---|---|---|---|
| FERM–JH1 | **p = 0.012** | p = 0.13 | **p = 0.0010** |
| arrangement, rank | p = 0.29 | **p = 0.035** | **p = 0.0024** |
| arrangement, closed-count | **p = 0.037** | **p = 0.037** | p = 0.15 |

No single row captures all three mutations. Reporting any one of them alone would misrepresent at least
one variant — which is the central methodological lesson of today's JAK3 work.

---

## 15. TYK2 depth scan and mutants — runs performed independently over the weekend (2026-10-19)

Thirteen TYK2 runs, one JAK3 and one JAK2 run were carried out separately while this session was down.
They complete the TYK2 depth scan and add **V678F**, the substitution the literature reports as
activating. Analysed here on both metrics; `n` combines the 8-seed halves.

### TYK2 free prediction, JH1 RMSD vs the AF2 closed-like reference (Å)

| MSA | variant | n | median | min–max | seeds < 30 Å | p vs WT |
|---|---|--:|--:|---|--:|--:|
| 128/512 | WT | 8 | 82.1 | 81.9–82.5 | 0 | – |
| 128/512 | P982A | 8 | 82.2 | 81.8–82.6 | 0 | 0.59 |
| **64/256** | WT | 16 | 84.5 | 41.2–92.0 | 0 | – |
| **64/256** | P982A | 16 | 88.8 | 36.7–95.8 | 0 | 0.34 |
| **64/256** | **V678F** | 8 | **93.7** | 90.7–94.8 | 0 | **0.0008** |
| 32/64 | WT | 15 | 46.4 | 28.2–85.6 | 1 | – |
| 32/64 | P982A | 31 | 44.7 | 25.4–54.5 | 1 | 0.14 |
| 32/64 | V678F | 16 | 51.6 | 27.5–68.0 | 1 | 0.33 |

### Three results

**1. TYK2 never reaches its closed state by free prediction, at any depth.** Across 32/64, 64/256,
128/512 and the earlier default depth, the closest any seed comes is **25.4 Å**, and only three seeds in
94 fall below 30 Å. At 32/64 the protein becomes compact (median FERM–JH1 45 Å) but the JH2–JH1
arrangement still does not match the autoinhibited geometry. Combined with the 4OLI-templated run — where
the closed state, once imposed, was perfectly stable through twelve template-free recycles — the picture
is a **real but inaccessible basin**: the model will hold TYK2 closed but will not find it.

This differs from JAK1, JAK2 and JAK3, all of which reach their closed state unaided at some depth, and
it is the sharpest cross-family difference the project has produced.

**2. V678F, the reported activating substitution, has a strong and specific effect (p = 0.0008).**
At 64/256 wild type ranges widely (41.2–92.0 Å, sometimes approaching the closed arrangement) while
V678F is confined to **90.7–94.8 Å** — it abolishes the partial approaches that wild type still makes.
This mirrors JAK3 A572V and M592F, which likewise removed the closed state. **A known activating
mutation produces the expected phenotype in TYK2**, which is meaningful validation on the one family
member with an experimental closed structure.

**3. P982A shows no significant effect at any depth** (p = 0.59, 0.34, 0.14). The structural prediction
in sections 3–4 — that deleting 12 of 28 cross-domain contacts at the only interface residue among the
seven variants would destabilise the closed state — **is not supported by these runs.**

Two readings, and they are not yet separable:
- The prediction is wrong, or the effect is too small for ~16–31 seeds.
- **The assay has a floor.** If wild-type TYK2 essentially never occupies the closed state, a mutation
  that destabilises it has nothing to remove. V678F could still register because it suppressed wild
  type's *partial* approaches; P982A may simply act on a state that is already unpopulated.

The second is more likely given result 1, and it means P982A is better tested another way — for example
starting from 4OLI with the template released at recycle 1 rather than 3, provided the grip can be
loosened enough to give the assay dynamic range.

### A false positive worth recording

At 128/512 the Mann-Whitney test returns **p = 0.011 on FERM–JH1** for P982A versus wild type — with
medians of 93.1 and 93.6 Å. A 0.5 Å difference reaches significance only because both distributions are
pathologically tight (spreads of 0.6 Å across 8 seeds). This is **not** a biological result, and it shows
that at a depth where seeds fail to diversify, rank tests will manufacture significance from noise.
Seed diversity is healthy at 64/256 (41–92 Å) and 32/64 (28–86 Å); the problem is specific to 128/512.

### JAK3 M511I — no change in how often, a large change in how tightly

| | n | closed-like seeds (< 25 Å) | arrangement median | p |
|---|--:|--:|--:|--:|
| wild type | 16 | 7/16 | 61.5 | – |
| **M511I** | 16 | **7/16** | 84.8 | 0.82 |

M511I is strongly bimodal: **1, 2, 2, 2, 15, 21, 22** then **84, 86, 88, 88, 89, 90, 90, 90, 92**. The
count of closed seeds is identical to wild type, so by that measure it does nothing — but four of its
closed seeds sit at **1–2 Å** from the reference where wild type's best reach 16 Å. That is the same
signature as A573V: **unchanged frequency, far more canonical geometry.**

Of the three reported activating JAK3 alleles tested so far, **A572V removes the closed state
(p = 0.037) while M511I does not (p = 0.82)**. They are not interchangeable.

### JAK2 V617F at 256/1024, seeds 8–15
Completes an earlier 8-seed run at the depth where JAK2's behaviour was least resolved. Median 2.2 Å
from the AF2 (open) reference — consistent with the established result that V617F drives JAK2 open at
this depth. Full pairing with its wild-type counterpart is left for the JAK2 write-up.

---

## 16. The JAK3 allele set completed, and two classes of effect (2026-10-19)

R657Q, the last of the three reported activating JAK3 alleles, has its first 8 seeds. All five mutations
at MSA 128/512, measured as JH1 RMSD against the closed reference after superposing JH2:

| variant | n | closed-like (< 25 Å) | median | Fisher | rank test |
|---|--:|--:|--:|--:|--:|
| wild type | 16 | 7/16 | 61.5 | – | – |
| **M592F** | 16 | **1/16** | 64.0 | **0.037** | 0.29 |
| **A572V** *(reported)* | 16 | **1/16** | 84.3 | **0.037** | **0.035** |
| M511I *(reported)* | 16 | 7/16 | 84.8 | 1.00 | 0.82 |
| A573V | 16 | 12/16 | 2.7 | 0.15 | **0.0024** |
| **R657Q** *(reported)* | 8 | 4/8 | 43.1 | 1.00 | 0.60 |

R657Q per seed: **2 2 3 4** · **83 89 91 91** — perfectly bimodal, with no intermediate.

### Two classes, not one

**Class 1 — the closed state is abolished.** M592F and A572V drop from 7/16 to 1/16 closed-like seeds
(p = 0.037 each). What remains is open (M592F, reaching 3.3 Å from the JAK1 open model) or splayed
(A572V).

**Class 2 — the closed state is retained but becomes far more canonical.** M511I, A573V and R657Q keep
a similar or larger number of closed seeds, but those seeds sit at **1–4 Å** from the reference where
wild type's best reach only **16–23 Å**. They also sharpen the bimodality: R657Q has nothing between
4 Å and 83 Å, whereas wild type is graded across the range.

Of the **three reported activating alleles, one (A572V) abolishes the closed state and two (M511I,
R657Q) tighten it.** They are not one phenotype.

### How to read class 2

Three possibilities, not yet separable:

1. **The model misses their mechanism.** JAK3 oncogenic mutants' hyperactivity is reported to depend on
   **ATP binding to the pseudokinase domain** (Frontiers in Oncology 2018). We model no nucleotide, so a
   mutation acting through JH2 nucleotide binding would be invisible — and could even look stabilising.
2. **Tighter is not the same as more populated.** These mutations do not make the closed state more
   frequent; they make it more canonical when adopted, and polarise the ensemble toward extremes. A
   deeper, more rigid autoinhibited well with a sharper barrier is not obviously a loss-of-function
   signature.
3. **The measurement captures packing, not activity.** The arrangement metric reports where JH1 sits
   relative to JH2, not whether the kinase active site is competent. See the KinCoRe proposal below.

### What would discriminate

Labelling the **JH1 domain itself** with KinCoRe (DFG-in/out, αC-in/out, activation loop, spine) would
say whether the kinase domain is in an active or inactive conformation — a question orthogonal to the
interdomain arrangement, and one these runs already contain the coordinates to answer at no GPU cost.

## 17. Two 2026 benchmarks that bear directly on this work

**KinConfBench** — Sun & Head-Gordon, *npj Drug Discovery* **3**, 33 (2026).
2225 human kinase chains; Boltz-2, Chai-1, Protenix and RFAA scored on recovering ligand-induced
conformational states using KinCoRe labels. Four points apply here:

1. *"Geometric success metrics of a ligand pose in the active site do not correlate strongly with the
   correct kinase conformational state."* The same lesson as our FERM–JH1 versus arrangement finding.
2. **Mode collapse is general.** Roughly two-thirds of systems give all-correct or all-wrong across 20
   inferences, and diversity within correct ensembles is ~0.1 Å and < 5°, *"below even the fluctuation
   range of a single stable conformational state."*
3. **Their proposed remedy is our method** — *"MSA sub-sampling, supplying different structural
   templates, or incorporation of dynamics data."*
4. **They deliberately exclude pseudokinase domains**: *"for genes encoding both catalytically active and
   pseudokinase domains, such as members of the Janus Kinase family... excluding pseudokinase domains."*
   The JH2–JH1 interdomain question is therefore outside the best current kinase benchmark. They also
   call for exactly this project's next step — testing whether models predict how *"drug-resistant
   mutations alter the conformational ensemble."*
   Data: figshare 10.6084/m9.figshare.31986663 · code: github.com/THGLab/KinConfBench

**Our TYK2 data confirm point 2 directly.** Wild-type seed spread against the closed reference scales
monotonically with MSA depth:

| MSA | n | median | **spread** |
|---|--:|--:|--:|
| 128/512 | 8 | 82.1 | **0.6 Å** |
| 96/384 | 8 | 82.5 | **8.8 Å** |
| 64/256 | 16 | 84.5 | **50.8 Å** |
| 32/64 | 15 | 46.4 | **57.4 Å** |

So the 0.6 Å uniformity flagged in section 13 is **mode collapse that MSA subsampling breaks up**, not a
seeding defect in this pipeline — and it confirms that the p = 0.011 "result" at 128/512 was significance
manufactured from collapsed variance.

**GPCR cofolding** — Zhang, Friesner, Miller & Rodrigues (Schrödinger), *npj Drug Discovery* **3**, 30 (2026).
253 GPCRs from families unseen in training. Two points apply here:

- **pLDDT barely predicts correctness** (R² = 0.046 against Cα RMSD), while ipTM does (R² = 0.49).
  **This project should stop quoting pLDDT ranges as support for a result**; they are reported in every
  run but carry almost no information about whether the conformational state is right.
- *"Co-folding methods tend to predict inactive receptor structures"* — a conformational prior of the
  same kind as the AF2 polarity documented in `reference_states.md` (AF2 is open for JAK1/JAK2, closed
  for JAK3/TYK2).

### A concrete experiment both papers point to

TYK2 has an approved drug, **deucravacitinib**, that binds JH2 and is thought to *stabilise* the closed
state. Our runs show TYK2 never reaches the closed arrangement unaided at any MSA depth. A co-folding
run (Boltz-2 or Chai-1) of **TYK2 + deucravacitinib** therefore asks a sharp question on the one JAK with
an experimental closed structure to check against: if the ligand pulls the model closed, it is doing
genuine ligand-induced conformational reasoning; if it stays open, that is apo-drift in exactly the form
KinConfBench describes.

---

## 18. Y581C abolishes the closed state — and the interface-burial logic fails (2026-10-19)

JAK3 Y581C, MSA 128/512, 16 seeds, paired with wild type `JAK3_20261016_125830`.

| | n | closed-like (< 25 Å) | median | spread |
|---|--:|--:|--:|--:|
| wild type | 16 | **7/16** | 61.5 | 75.3 Å |
| **Y581C** | 16 | **0/16** | 88.4 | **8.6 Å** |

Per seed: `88 88 88 88 88 89 89 89` · `84 87 88 88 92 92 92 92`

**Fisher p = 0.0068 · Mann-Whitney p = 0.00049.** Both halves agree, so unlike A572V and R657Q this one
strengthened on replication. **It is the strongest JAK3 mutation effect measured in the project** —
A572V and M592F reached only p = 0.037 by the count test.

### This contradicts the structural prediction

Section 9 measured Y581C at **0.0 Å² of interface burial** in JAK3's own closed structure, with **no
cross-domain contacts**, and section 4 predicted "local JH2 packing; little arrangement change" with
moderate confidence. That prediction is wrong: Y581C removes the closed arrangement completely.

### The pattern across the whole campaign

| variant | interface burial | effect on the closed state |
|---|--:|---|
| **TYK2 V678F** | **0.0 Å²** | abolishes partial approaches, **p = 0.00012** |
| **JAK3 Y581C** | **0.0 Å²** | abolishes it entirely, **p = 0.0068** |
| JAK3 A572V | not at interface | abolishes it, p = 0.037 |
| JAK3 M592F | 0.0 Å² (= V617 position) | abolishes it, p = 0.037 |
| **TYK2 P982A** | **59.8 Å², 28 contacts** | **no effect at any depth** |

**Every mutation with a measurable effect sits at a position that buries nothing at the interface, and
the one genuine interface residue does nothing.** The two strongest results in the entire project —
V678F and Y581C — both come from residues with zero cross-domain contact.

### What this means

1. **Interface burial does not predict which mutations shift the conformational equilibrium.** The
   ranking of the seven variants in sections 4 and 9 was built on it and should not be used that way.
   Burial identifies where the two domains touch; it does not identify what controls whether they touch.
2. **The effective mechanism is allosteric.** These residues are buried inside their own domain
   (Y581C 20 % exposed in JH2; V678 53 % exposed, 14 Å from JH1) and change the arrangement without
   touching the partner — presumably by altering the packing or rigidity of the domain that presents the
   interface, rather than the interface itself.
3. **P982A's null result is less surprising.** It was predicted to matter *because* it is the only
   interface residue; on the evidence here, that was the wrong criterion.
4. **A better predictor is needed.** Candidates worth testing against the data we now have: burial
   within the residue's own domain, proximity to the segment that positions the largest interface
   residue (for TYK2, F672 is the top interface residue and sits six residues from V678), or ESM1b,
   which ranked P982A most extreme and was the one sequence predictor that agreed with the old logic —
   and therefore also needs re-checking against these outcomes.

### One caveat

Y581C's seed spread is **8.6 Å** against wild type's **75.3 Å**. A tightly clustered mutant compared with
a diverse wild type risks measuring collapse rather than state. The **count test is the robust one here**
(0/16 versus 7/16, p = 0.0068) because it asks only how many seeds reach the closed basin, and that is
the figure to quote.

---

## 19. TYK2 P982A — null at a fourth depth (2026-10-19)

`TYK2_P982A_20261019_132520`, MSA 96/384, 8 seeds, paired with wild type `TYK2_20261019_101530`.

| | n | median | range | seeds < 30 Å |
|---|--:|--:|---|--:|
| wild type | 8 | 82.5 | 81.8–90.6 | 0 |
| P982A | 8 | 82.7 | 78.3–91.5 | 0 |

**Mann-Whitney p = 0.79.** Neither reaches the closed arrangement.

P982A has now been tested at **four MSA depths — 128/512, 96/384, 64/256 and 32/64 — with no significant
effect at any of them** (p = 0.59, 0.79, 0.34, 0.14). Combined with section 18, the verdict on the
structural prediction is clear:

**The variant chosen because it was the only one of the seven at a genuine domain interface is the only
one of the tested set that does nothing.** Meanwhile JAK3 Y581C (0.0 Å² burial) abolishes the closed
state at p = 0.0068 and TYK2 V678F (0.0 Å² burial) at p = 0.00012.

Two honest readings remain, and the data cannot yet separate them:

1. **P982A genuinely has little effect on the conformational equilibrium** — the interface contact it
   removes is not what holds the arrangement together.
2. **The assay has a floor for this protein.** TYK2 never occupies the closed state by free prediction
   at any depth, so a mutation that destabilises that state has nothing to remove. V678F can still
   register because it suppresses wild type's *partial approaches*, which are visible; P982A would only
   show if the closed state were populated.

Reading 2 would be testable with a working template-release assay, but the 4OLI release has no dynamic
range (section 11). Releasing at recycle 1 rather than 3 is the remaining idea, and it is unproven.

---

## 20. V678M: at the V617F hotspot the aromatic ring does the work, not the position (2026-10-20)

TYK2 V678M, MSA 64/256, 16 seeds, paired with wild type and with V678F at the same depth and seeds.

| | n | compact (FERM–JH1 < 60 Å) | p(count) | median arrangement | **p(arrangement)** |
|---|--:|--:|--:|--:|--:|
| wild type | 16 | 7/16 | – | 84.5 | – |
| **V678F** | 16 | **0/16** | **0.0068** | 93.0 | **0.0001** |
| **V678M** | 16 | 4/16 | 0.46 | 85.3 | **1.0000** |

**Phenylalanine abolishes the closed state; methionine is indistinguishable from wild type.** p = 1.0000
on the arrangement metric is not a weak effect — the two distributions are as close to identical as the
test reports.

### The claim

At the position equivalent to JAK2 V617 and JAK1 V658, **the aromatic ring is the active ingredient, not
the location.** Two independent lines agree:

- **TYK2** — valine→phenylalanine abolishes the closed state (p = 0.0001); valine→methionine does nothing.
- **JAK3** — the native residue at the equivalent position is **already methionine (M592)**, and *adding*
  the ring, M592F, abolishes the closed state (p = 0.037).

Methionine at this site is therefore compatible with a functioning wild-type JAK, and introducing an
aromatic ring is what shifts the equilibrium. The literature generally describes this site as "the V617F
position"; on this evidence the position alone is inert.

### Why this is a useful control

V678M rules out the alternative that V678F's effect is simply "any substitution at a sensitive site".
Same residue, same depth, same seeds, same n — one substitution moves everything, the other moves nothing.

### Status of the seven user-supplied variants

| variant | result |
|---|---|
| TYK2 **V678M** | **null** (p = 1.0000), this section |
| TYK2 **P982A** | **null at four depths** (0.59 / 0.79 / 0.34 / 0.14), section 19 |
| JAK3 **Y581C** | **abolishes the closed state**, p = 0.0068 — section 18 |
| JAK2 **G571R** | trending less compact, arrangement p = 0.042, n = 16 — not established |
| JAK2 **V1110E** | trending, p(count) = 0.079 at n = 8; second half running |
| JAK2 V578I | not yet run |
| JAK2 L805I | not yet run |

Worth stating plainly: of the seven, **only Y581C has produced a clear effect so far.** The strongest
result in the project, TYK2 V678F, is a substitution added during this work rather than one from the
original list — and its value comes largely from being paired with V678M as a control.

---

## 21. The depth ladder has only one informative rung for TYK2 (2026-10-20)

V678F was rerun at **96/384 to n = 16** to replicate the 64/256 result at a second depth. It did not
replicate — and the reason is a property of the assay, not of the mutation.

| depth | WT compact | V678F compact | WT median FERM–JH1 | p(arr) | p(rank FERM) |
|---|--:|--:|--:|--:|--:|
| 128/512 free | 0/8 | — | 93.6 | — | — |
| **96/384** | 0/8 | **0/16** | 93.5 | 0.0511 | 0.1460 |
| **64/256** | **7/16** | **0/16** | 80.0 | **0.0001** | 0.0135 |
| 32/64 | 0/15 | 0/16 | 45.2 | 0.3326 | 0.0631 |

**At 96/384 and above, wild-type TYK2 is already 100 % open.** Median FERM–JH1 93.5 Å, seed spread
4.0 Å at 96/384 and 0.6 Å at 128/512. There is no closed population left for a mutation to remove, so
no variant can separate there in either direction. At the other end, 32/64 collapses *every* model
compact (38–52 Å) regardless of genotype. **64/256 is the only TYK2 depth with dynamic range**
(WT 7/16 compact, FERM spread 60.5 Å), and it is the only depth where V678F separates.

The p(arr) = 0.051 at 96/384 should be ignored. It is computed on a distribution with almost no
variance — the same artefact that produced a "significant" p = 0.011 for a 0.5 Å median difference at
128/512. A rank test on a collapsed ensemble manufactures significance from nothing.

**Consequence for experiment design.** The depth ladder is not a free axis to replicate across. A
mutant run at 96/384 or 128/512 cannot produce a result either way, so those runs are not weak
evidence — they are no evidence, at ~77 min of GPU time each. New TYK2 variants should go straight to
64/256. This roughly doubles the information per GPU-hour and is why the queued V678M 96/384 pair was
dropped in favour of deepening WT and V678F at 64/256 to n = 24.

The same test should be applied to the other three JAKs before spending more depth-ladder time: for
each, find the depth where wild type is most evenly split, and run mutants only there. For JAK2 that
is 512/8192 (7 closed / 7 open / 2 FERM-bound of 16), which is where the current queue already sits.

---

## 22. What is actually known about TYK2 structure — a complete census (2026-10-20)

Every PDB entity referencing UniProt **P29597** was retrieved: **52 entities, all X-ray, no cryo-EM,
no full-length structure.**

| Span (UniProt) | Module | n | Best res. | Notable |
|---|---|--:|--:|---|
| 23–583 | FERM-SH2 + IFNAR1 peptide | 1 | 1.99 Å | 4PO6 — the only N-terminal structure |
| 541–873 | JH2 (pseudokinase) | ~19 | 1.71 Å | ligand series; **5C03 has ATP-γS**; 8S9A = TAK-279 |
| **566–1187** | **JH2 + JH1** | **1** | **2.8 Å** | **4OLI** — the autoinhibited module, our template |
| 884–1182 | JH1 (kinase) | ~28 | 1.65 Å | inhibitor series incl. peficitinib (6AAM) |
| 1048–1062 | activation-loop peptide on PTP1B | 2 | 2.15 Å | 8EXN / 8EYC |

### The gap that matters for this project

4PO6 ends at residue 583; 4OLI begins at 566. They overlap by 17 residues, and **no structure has ever
contained both the FERM domain and JH1.** For TYK2 the FERM–JH1 distance therefore has **no
experimental value in any conformational state** — open or closed.

This has a direct consequence we had not stated: **the 40–45 Å "closed" band for TYK2 comes from the
AlphaFold model, not from 4OLI**, because 4OLI contains no FERM domain. 4OLI anchors only the
*arrangement* metric (JH2→JH1 docking), which it does well — 2.8 Å, 99.6 % sequence identity to the
query. So of our two metrics, for TYK2 exactly one is experimentally anchored, and it is not the
distance one. This is a second reason to lead with the arrangement metric, which is also the metric
carrying the V678F result.

### Is there a described open form of TYK2?

**No.** Not at any resolution. What exists:

- The full-length "autoinhibited TYK2" models in the literature are **docked composites of 4PO6 +
  4OLI** — the same two pieces, assembled by modelling. Same information content as our template run,
  not independent evidence.
- Everything about an extended TYK2 is **transferred from JAK1**: Lupardus et al., *Structure* 2011
  (three-lobed full-length JAK1 by EM, "extensive inter-segmental flexibility") and Glassman et al.,
  *Science* 2022 (JAK1 dimer, 7T6F, FERM–JH1 ≈ 84 Å).

**Our 93 Å open state has no experimental counterpart in TYK2 or in the family.** Every experimental
extended JAK structure is a **dimer** at ≈ 84 Å; our 93 Å state is a monomer, 9 Å longer. It is the
AlphaFold-style fully-extended monomer, and its reproducibility across depths (0.6 Å spread at
128/512) is better read as a signature of coevolutionary bias — strong intra-domain signal, almost no
inter-domain signal, linkers extend — than as a sampled conformer.

**This reframes how results should be stated.** The closed end of the axis is anchored by a 2.8 Å
crystal structure; the open end is a default. So the correct claim is **"V678F abolishes any approach
to the closed state"**, not "V678F drives the ensemble open". The former is what the arrangement
metric measures and what survives scrutiny.

### Biochemical facts worth having on record

- **JH2 binds ATP but cannot phosphotransfer** (Min et al., *JBC* 2015; 5C03 with ATP-γS). Mutating
  the JH2 ATP pocket *raises* basal TYK2 phosphorylation — JH2 nucleotide occupancy is itself
  autoinhibitory. Our runs give JH2 no ligand at all, so this degree of freedom is absent from every
  model we have made.
- **V678F** is the designed JAK2-V617F mimic; the JAK1 analogue is **L653F**. A family-wide analogue
  set is therefore available and cheap to run.
- **P1104A** (rs34536443), the autoimmune-protective allele, sits in the **JAK-specific insertion of
  JH1**, not in JH2 — catalytically impaired but signalling-competent.

---

## 23. An external benchmark exists for exactly our prediction task (2026-10-20)

**Howard, Abell, … Dickel, "Deep mutational scanning reveals pharmacologically relevant insights into
TYK2 signaling and disease."** bioRxiv 10.1101/2025.10.11.681520; eLife reviewed preprint 110149,
version 1 dated **2026-03-04**.

**> 23,000 amino-acid substitutions in TYK2**, with two readouts: **IFN-α signalling** and **protein
abundance**. TYK2 is 1187 residues, so 1187 × 19 ≈ 22,550 — this is **saturation across essentially
the whole protein**, and therefore contains measured values for **V678M, V678F, P982A and P1104A**.

Why this matters more than anything else found today:

1. It can **validate or falsify the headline claim** — V678F strongly disruptive, V678M null at the
   same position. If the DMS reproduces that split, it is external confirmation of the method on a
   result we derived blind. If it does not, we need to know now.
2. It gives a **per-residue functional score across the whole JH2–JH1 interface**, which can be
   correlated against our ΔSASA burial values — a direct test of the negative result that interface
   burial fails as a predictor (TYK2 V678F and JAK3 Y581C both bury 0.0 Å² yet give the two strongest
   effects; P982A buries 59.8 Å² and is null at four depths).
3. The finding that **protective variants act by reducing protein abundance** is a caution: some
   variant effects are stability or degradation phenomena, invisible to conformational prediction.
   Worth knowing which of our seven fall in that class before claiming a conformational mechanism.

**Status: abstract only.** The eLife page failed to render and the supplementary tables have not been
retrieved. Pulling that data and cross-tabulating it against our variant list is the highest-value
analysis currently available, and it needs no GPU.

---

## 24. RETRACTION: "the aromatic ring, not the position" is wrong (2026-10-20)

Section 20 of this document claims, on the basis of our V678M null result, that at the position
equivalent to JAK2 V617 **"the aromatic ring is the active ingredient, not the location"**, and that
"methionine at this site is compatible with a functioning wild-type JAK". **Both statements are
contradicted by experiment and are withdrawn.**

The TYK2 deep mutational scan (section 23; MaveDB `urn:mavedb:00001270-a-*`) measures every
substitution at position 678. At 1 U/mL IFN-alpha, relative to wild type:

| aa | signalling | se | abundance |
|---|--:|--:|--:|
| **M** | **+0.561** | 0.252 | **+0.002** |
| I | +0.520 | 0.193 | -0.088 |
| **F** | **+0.390** | 0.080 | **-0.323** |
| W | +0.227 | 0.240 | -0.361 |
| L | +0.145 | 0.230 | -0.183 |
| A | -0.228 | 0.232 | -0.139 |
| G | -0.474 | 0.287 | -0.098 |
| D | -0.479 | 0.280 | -0.201 |

**V678M is activating, not null** - 97th percentile of 23,723 variants. Our control fails, and with
it the inference it supported.

### What the data say instead

**Hydrophobic bulk at 678 activates.** Spearman correlation of side-chain volume with signalling at
this position is **rho = +0.548, p = 0.015**, which ranks in the **99.1st percentile** of all 1186
positions tested. But it is specifically *hydrophobic* bulk: lysine (-0.10), arginine (-0.04),
glutamine (-0.21) and histidine (-0.21) are all larger than methionine and none of them activate.

A caution on that trend: 29 of 1186 positions reach p < 0.05 for a positive volume correlation, and
~30 is exactly the chance expectation. The trend is only admissible because **678 was chosen a
priori** - from V617F homology and our own modelling - rather than found by scanning. On 19 points,
p = 0.015 is modest support.

### The abundance column, which we had not looked at

**V678F destroys the protein**: abundance -0.323, the 10th percentile, against a nonsense-variant
anchor of -0.352. It is 92 % of the way from wild type to no protein. **V678M leaves abundance
untouched** (+0.002, 88th percentile).

Two *separable* consequences of the same position:
- **activation** tracks general hydrophobic bulk (M, I, F, W, L all positive)
- **destabilisation** tracks the aromatic ring specifically (only F -0.323 and W -0.361; the bulky
  aliphatics M +0.002 and I -0.088 are fine)

Volume correlates with signalling (rho +0.548) but **not** with abundance (rho -0.158, p = 0.52),
confirming the two effects are independent.

**So the ring *is* doing something specific - it is the thing that wrecks the fold. It is not the
thing that activates.** Our original sentence had the right noun and the wrong verb.

### Consequence for the project's headline result

**V678F is the confounded variant and V678M is the clean one - the reverse of how we used them.**
Our models show V678F abolishing the closed state (p = 0.0014 at n = 24 vs 16, section 25). Part of
that may be a protein that does not fold properly rather than a specific conformational switch.
V678M activates at least as strongly with the fold intact, and our method called it null.

This is a **false negative of our method**, and the first one we can demonstrate against experiment.

### The experiment this calls for

The full V678 substitution series at 64/256, now queued: **I, W, L** (measured activating) and
**A, G, D** (measured loss-of-function). If our metrics reproduce the measured ordering - and in
particular if A, G and D *tighten* the closed state, a direction no variant in this project has yet
produced - that is a real validation on data nobody has analysed. If they do not, we have located
the method's limit precisely.

---

## 25. Results, 2026-10-20

### TYK2 wild type at 64/256 deepened to n = 24

| variant | n | compact | median FERM-JH1 | p(cnt) | arr<25 | p(arr) |
|---|--:|--:|--:|--:|--:|--:|
| WT | **24** | 8/24 | 85.9 | - | 0/24 | - |
| V678F | 16 | 0/16 | 92.6 | 0.0133 | 0/16 | **0.0014** |
| V678M | 16 | 4/16 | 84.9 | 0.729 | 0/16 | 0.288 |

**V678F survives at n = 24 vs 16, p = 0.0014.** It weakened from p = 0.00012, which is the honest
direction of drift as the wild-type arm deepened, and is consistent with the pattern recorded in
section 17: A572V 0.0009 -> 0.035, R657Q lost significance entirely.

### JAK2 V1110E is null at n = 16

| | n | compact | p(cnt) | p(rank) | p(arr) |
|---|--:|--:|--:|--:|--:|
| WT @ 512/8192 | 16 | 9/16 | - | - | - |
| V1110E | **16** | 7/16 | **0.724** | 0.316 | 0.508 |

At n = 8 it was trending (p = 0.079); the second half erased it. **This is the third variant in the
campaign to lose an apparently promising n = 8 result** (A572V, R657Q, now V1110E), against one that
strengthened (V678F). The rule should be explicit: **no n = 8 result is reportable.**

### JAK2 V578I, first half only (n = 8 - pilot, not a finding)

7/8 compact against wild type's 9/16, median FERM-JH1 47.0 vs 49.6, arrangement 10.7 vs 19.1,
p(rank) = 0.061. The direction is **tighter to closed**, which would be notable - V578I was included
as a near-neutral control. Given the paragraph above, this is recorded as a pilot and nothing more
until seeds 8-15 land.

### Seven-variant scoreboard

| variant | n | verdict |
|---|--:|---|
| JAK3 **Y581C** | 16 | **abolishes the closed state**, p = 0.0068 - the only clear positive |
| JAK2 **G571R** | 16 | arrangement p = 0.042, count p = 0.149 - weak, not established |
| JAK2 **V1110E** | 16 | **null** |
| TYK2 **V678M** | 16 | null in our assay - **false negative**, DMS says activating |
| TYK2 **P982A** | 4 depths | null - DMS agrees (mildly loss-of-function) |
| JAK2 **V578I** | 8 | pilot only, trending tighter |
| JAK2 **L805I** | - | queued |

---

## 26. The 4OLI interface is validated - as a stability element, not a switch (2026-10-20)

The JH2-JH1 interface was defined structurally from **4OLI** by Shrake-Rupley dSASA > 25 A^2, giving
**26 residues**: 579, 580, 582, 610, 637, 663, 664, 666, 672, 674, 728, 743, 744, 756, 900, 901,
921, 922, 923, 926, 980, 982, 983, 992, 993, 1033. Each residue was scored by the median of its ~19
measured substitutions and compared against the other 505 residues in the structure.

| assay | interface | non-interface | p |
|---|--:|--:|--:|
| **abundance** | **-0.302** | -0.121 | **5.5e-05** |
| signalling 1 U | -0.033 | -0.082 | 0.011 |
| signalling 100 U | -0.079 | -0.139 | 0.15 |

On a scale where 0 = wild type and -0.352 = dead protein, the interface median is **86 % of the way
to dead**, against 34 % for the rest of the structure.

**It is not merely burial.** Interface residues are buried by construction, so the comparison was
repeated within relative-solvent-accessibility strata:

| burial (RSA) | interface | other | p |
|---|--:|--:|--:|
| 5-20 % | -0.315 (n=12) | -0.183 (n=131) | 0.036 |
| **20-50 %** | **-0.296 (n=11)** | **-0.082 (n=165)** | **1.6e-05** |

The effect survives and is **strongest among partially-exposed residues** - exactly where a real
interface should show, since those are exposed in the isolated domain and covered when the domains
dock. This is the first independent experimental confirmation that the contact surface our template
encodes is real.

### What this analysis cannot say

The per-residue **median is direction-blind**. At position 678 the activating and inactivating
substitutions cancel to a median of +0.030 - the site carrying our entire headline result is
invisible to the statistic used here. The signalling column is also confounded by abundance, since
interface residues destabilise heavily.

**Therefore the signalling rows above do not support "the interface is not an allosteric switch".**
That question is open; this test cannot answer it. To answer it properly: use the paper's
signalling-only variant class (Table S1), or a direction-sensitive statistic such as the maximum
positive score per residue.

What does hold: **mutating the interface destabilises TYK2**, strongly and independently of burial.

### V678 is not in the interface

672 and 674 are; 678 is not - it buries **0.0 A^2** across the JH2-JH1 contact. The strongest
functional site at this position makes no interface contact at all, so whatever it does works
*through* JH2 rather than by direct contact. P982, which *is* in the interface, is null in our
models and mildly loss-of-function in theirs.

This independently corroborates the negative result recorded earlier: **interface burial predicts
stability, not activation.** It was predicting the wrong quantity.

---

## 27. Standard variant-effect predictors are blind to this axis (2026-10-20)

PolyPhen-2 (HDIV), SIFT, REVEL and AlphaMissense were retrieved for all TYK2 variants in dbNSFP via
MyVariant.info - 9,205 variant rows over 1,188 positions.

### They do not see the interface

| predictor | interface | other | p |
|---|--:|--:|--:|
| PolyPhen-2 | 0.989 | 0.982 | 0.84 |
| AlphaMissense | 0.267 | 0.335 | 0.84 |
| REVEL | 0.488 | 0.518 | 0.58 |
| SIFT | 0.009 | 0.004 | 0.33 |

The interface that the DMS validates at p = 5.5e-05 is invisible to all four.

### They cannot resolve position 678

| sub | PolyPhen | AlphaMissense | REVEL | SIFT | measured signalling |
|---|--:|--:|--:|--:|--:|
| M | 1.000 | 0.302 | 0.564 | 0.001 | **+0.561** |
| L | 0.999 | 0.357 | 0.563 | 0.002 | +0.145 |
| A | 0.998 | 0.491 | 0.546 | 0.001 | -0.228 |
| G | 1.000 | 0.453 | 0.702 | 0.001 | **-0.474** |

PolyPhen calls every substitution damaging (0.998-1.000) while the measured effects span +0.561 to
-0.474. It ranks the strongest activator and the strongest loss identically. Note also that **I, F,
W and D have no entry at all** - they are not reachable by a single nucleotide change from GTG, so
**V678F, our headline variant, is absent from every standard predictor.**

### Across the whole protein they track abundance, not function

| predictor | vs signalling 1 U | vs abundance |
|---|--:|--:|
| PolyPhen-2 | -0.126 | **-0.286** |
| AlphaMissense | -0.148 | **-0.350** |
| REVEL | -0.137 | **-0.370** |
| SIFT | +0.130 | +0.266 |

Every predictor correlates 2-3x more strongly with **protein abundance** than with signalling - the
same split found for the structural interface. These tools predict whether a protein survives
folding, not what it does.

**Consequence:** the PolyPhen and ESM annotations carried in the original seven-variant table were
answering a different question from the one we are asking, which is why they had no predictive value
for our results. It also means our conformational method is not competing with them - it targets the
axis they are blind to. The honest caveat is that rho ~ -0.35 is weak even on the axis they do best.

---

## 28. Corrections to sections 26 and 27, from better statistics (2026-10-20, night)

Three claims made earlier today were tested properly and two of them were wrong. Recorded here
rather than edited in place, so the reasoning stays auditable.

### 28.1 "The signalling column is confounded by abundance" - overstated

Across all 22,513 variants measured on both assays, signalling regressed on abundance gives
**slope +0.287, r = +0.105** (p = 2e-56). Abundance explains roughly **1 % of the variance** in
signalling. The two readouts are very nearly independent, and the signalling scores were never
badly contaminated. The caution in section 26 was more than the data warranted.

### 28.2 "This test cannot say whether the interface is an allosteric switch" - too pessimistic

Repeating the interface comparison with direction-sensitive statistics, and with the (small)
abundance component regressed out:

| statistic | interface | non-interface | p |
|---|--:|--:|--:|
| median, raw | -0.033 | -0.082 | 0.011 |
| **median, abundance removed** | **+0.042** | **-0.019** | **0.00057** |
| MAX (most activating substitution) | +0.473 | +0.463 | 0.71 |
| MIN (most damaging substitution) | -0.575 | -0.620 | 0.33 |

There **is** a real activating signal at the interface: mutating it shifts signalling up by about
0.06 on average, p = 0.00057, which is the direction autoinhibition predicts - break the clamp,
signal more.

But the **MAX statistic shows nothing (p = 0.71)**. The interface is not where the strongest
activators sit. The correct description is a **weak, diffuse activating surface rather than a switch
with hotspots** - consistent with a clamp that is released by degrading the contact overall rather
than by flipping one residue.

Both earlier statements are therefore superseded: the interface is (a) strongly destabilising when
mutated, p = 5.5e-05, and (b) mildly activating when mutated, p = 0.00057, with no hotspot structure.

### 28.3 "Position 678 is the activating hotspot" - not supported as stated

On the direction-sensitive MAX statistic, position 678 ranks **715th of 1187 positions, the 60th
percentile**. Its single most-activating substitution (+0.561) is unremarkable; hundreds of
positions have a stronger one.

**678's distinction is the ordering, not the magnitude.** The volume-signalling correlation at this
position (rho = +0.548) sits in the 99.1st percentile, but the effect sizes are ordinary. Calling it
"the activating hotspot" overstates it; the accurate statement is that substituting 678 produces an
unusually clean and physically interpretable gradient.

This raises the bar for the experiment now running. V678I versus V678F is asking whether our models
track a **subtle, graded** signal, not whether they detect an outlier. A null result there would be
much less damning than it would have been under the earlier framing.

---

## 29. What V678 actually touches in 4OLI (2026-10-20, night)

An earlier note speculated that bulk at 678 levers the 672-674 interface patch apart. That was
inferred from the interface residue list and never measured. Measured now:

| measurement | value |
|---|--:|
| 678 -> JH1, nearest heavy atom | **14.0 A** |
| 678 -> nearest interface residue | 8.3 A |
| 678 -> 672 | 15.5 A |
| 678 -> 674 | 11.0 A |
| 678 SASA in JH2 alone | 75.9 A^2 = **43.6 % exposed** |
| 678 dSASA on JH1 docking | **0.0 A^2** |

Heavy-atom neighbours within 5 A: C677, R679 (chain-adjacent), then **Y656, G680, E682, Q586, N683,
V584, V676**.

**The speculation was wrong in its specifics.** 678 is 11-15 A from 672/674 and makes no contact
with them. It does contact **V584 and Q586** at ~4 A, and those sit immediately beside interface
residues 579/580/582, so a second-shell path 678 -> 584/586 -> 579-582 -> JH1 is geometrically
available. That is a corrected hypothesis, not a result; the identity of the 8.3 A interface
neighbour has not been confirmed.

**678 is a surface residue, 44 % solvent-exposed.** This undercuts a simple steric-displacement
story - a bulky substitution has room there - and makes the measured abundance effect of F (-0.323)
and W (-0.361) genuinely puzzling, since strong destabilisation at a near-half-exposed position is
not what packing defects usually look like. An exposed aromatic creating an aggregation-prone or
degron-like patch would explain it, but that is speculation and is flagged as such.

**Current honest position on V678: the experimental behaviour is established (hydrophobic bulk
activates, aromatics destabilise) and there is no structural mechanism for either.** The contact
geometry rules out direct interface action and makes a simple packing explanation unlikely.

---

## 30. The V678 substitution series: our signal tracks abundance, not activation (2026-10-21)

Four substitutions at position 678 have now been run at 64/256, the only TYK2 depth with dynamic
range, and compared against the measured deep mutational scan values.

| variant | our compact | fraction | measured signalling (1 U) | measured abundance |
|---|--:|--:|--:|--:|
| **F** | 0/24 | 0.000 | +0.390 | -0.323 |
| **W** | 2/16 | 0.125 | +0.227 | **-0.361** |
| M | 4/16 | 0.250 | +0.561 | +0.002 |
| I | 5/16 | 0.312 | +0.520 | -0.088 |
| WT | 8/24 | 0.333 | - | - |

Rank correlation of our compact fraction against each measured axis:

| axis | Spearman rho | p |
|---|--:|--:|
| **abundance** | **+0.600** | 0.285 |
| signalling | -0.200 | 0.747 |

**The two destabilising substitutions (F, W) sit at one end of our ordering and the two stable ones
(M, I) sit with wild type at the other.** That is the abundance ordering. The signalling ordering is
the opposite of what our models produce: M and I are the strongest activators measured and are the
two our method calls closest to wild type.

**Interpretation.** What this pipeline detects at position 678 is whether the substituted sequence
still encodes a stable fold, not whether the variant activates the kinase. This is consistent with
two other findings from the same day: standard predictors (PolyPhen, SIFT, REVEL, AlphaMissense)
correlate 2-3x better with abundance than with signalling (section 27), and the 4OLI interface shows
a strong abundance signal but only a weak diffuse activating one (sections 26, 28).

**Consequence for the headline result.** The V678F finding (0/24 vs 8/24, p = 0.0003) stands as a
measurement but its interpretation must change. "V678F abolishes TYK2's approaches to the closed
arrangement" is defensible; "V678F is an activating mutation and our method detects that" is not
supported, because the two substitutions that activate more strongly (M, I) are the two our method
scores closest to wild type.

### Caveats, stated plainly

- rho = +0.600 on five points is **p = 0.285** - suggestive, not established.
- Only **F** reaches significance individually (p = 0.0003). **W** is a trend (2/16 vs 8/24,
  p = 0.14). M and I are flat.
- Wild type is pinned at 0 on both measured axes by construction, which inflates any correlation
  that includes it.
- V678F remains confounded: it is both the most-studied substitution at this position (the JAK2
  V617F analogue) and one of the two most destabilising. Those cannot be separated with the data in
  hand.

### The test still running

A (-0.139), G (-0.098) and D (-0.201) are all **mildly** destabilising. Under the abundance account
they should land **between W and M** - intermediate, not null. That is a graded prediction over three
further points and is a sharper test than any single pairwise comparison. If instead they come back
flat at wild-type levels, the abundance account weakens and the result reduces to "F and W are
special", which would need a different explanation.

---

## 31. Two retractions from the same night (2026-10-21)

Both were mine, both came from reading an n = 8 half as if it were a result, and both are recorded
rather than quietly corrected.

**31.1 "V678W refutes the foldability account."** At n = 8, V678W was 2/8 compact and I described it
as "dead null" and wrote that the foldability hypothesis was refuted. At n = 16 it is **2/16**, the
second-lowest of the series after F, and it **supports** the account rather than refuting it. The
error was treating 2/8 as informative immediately after noting that four of five n = 8 results in
this campaign had evaporated.

**31.2 The memorisation hypothesis.** On the strength of that bad reading I proposed that our models
might be *recognising* V678F because the JAK2 V617F analogue is among the most-studied kinase
mutations in existence, and described it as "the hypothesis I would now put first". There is no
evidence for it, and the abundance account explains the data more simply. **Withdrawn.** It remains
a legitimate concern in principle - V678F is the only substitution at this position with a large
literature footprint - but it was proposed on the basis of a result that was not real.

**The standing rule, now violated twice in one night by its own author: no n = 8 half is
interpretable in this assay.** Record it, do not reason from it.

---

## 32. Duplicate run folders are replicate data, and three of four fail reproducibility (2026-10-21)

Twelve duplicate run folders accumulated across the campaign, created when a supervisor relaunch
replayed a queue from the top. The first instinct was to delete them. They should be **kept**: four
of the nine duplicated groups are genuine recomputations - the same seeds and the same configuration
re-run on a different sandbox - and they are the only replicate data the project has.

Five groups are mere re-pushes of the same completed inference (identifiable in the logs by a run
time of `in 2 min`) and carry no information. The other four do:

| group | median abs delta FERM-JH1 | max |
|---|--:|--:|
| JAK2 WT, default MSA | **0.4 A** | 1.0 A |
| JAK2 WT 32/64 | 6.8 A | 8.9 A |
| **JAK1 WT 128/512** | **18.0 A** | **52.4 A** |
| **TYK2 V678L 64/256** | **14.7 A** | **52.1 A** |

### The same seed does not reproduce the same structure

TYK2 V678L at 64/256, per seed, run A versus run B:

| seed | run A | run B | delta |
|--:|--:|--:|--:|
| 0 | 82.0 | 92.0 | 10.0 |
| 1 | **40.6** | **91.2** | **50.6** |
| 2 | 80.9 | 91.6 | 10.7 |
| 3 | 83.8 | 92.2 | 8.4 |
| 4 | 60.0 | 87.5 | 27.5 |
| 5 | **40.5** | **92.6** | **52.1** |
| 6 | 77.9 | 94.3 | 16.4 |
| 7 | 81.6 | 94.6 | 13.0 |

Seeds 1 and 5 move between a **compact** state (~40 A) and a **fully open** one (~92 A) purely by
re-running. Expressed as the statistic the project actually reports, those two runs give
**~2-3 of 8 compact** versus **0 of 8**. JAK1 wild type at 128/512 behaves the same way: **0/5
versus 2/5** compact across two runs with identical seeds and identical configuration.

### Three consequences

1. **Run-to-run variation is the same size as the effects being called significant.** A 2/8 shift
   from re-running alone is the magnitude of most positive results in this campaign.
2. **Reported numbers are partly arbitrary where duplicates exist.** `all_results.py` deduplicates
   by seed number with later runs overwriting earlier ones, so it reports whichever copy was pushed
   last. For V678L that choice alone moves the result between 0/8 and 2-3/8.
3. **The headline comparison is not fully controlled.** V678F (0/24) and wild type (8/24) were run
   at different times on different sandboxes. Some unknown fraction of that gap is run-to-run
   variation rather than the mutation, and the present data cannot bound that fraction.

Note the one group that *does* reproduce: JAK2 wild type at the default deep MSA, median delta
**0.4 A**. That is the mode-collapsed regime, where every seed returns the same answer anyway. The
irreproducibility appears exactly where the ensemble has dynamic range - which is the regime the
whole campaign depends on.

### Likely cause, untested

The MSA is re-fetched from the ColabFold API on every run. If the returned alignment differs between
fetches, the model input differs, and the random seed only controls sampling *given* an input - so
"same seed, different run" is not a controlled comparison at all. This is testable by hashing the
MSA across runs and has **not** been done.

### The experiment this calls for, when it becomes a priority

Run wild type at 64/256 three times with identical seeds and measure the spread of the compact
count. That calibrates every p-value reported in this document. Until it is done, the p-values here
should be read as upper bounds on confidence rather than as calibrated significance.

---

## 33. Correction to section 32: the duplicate runs are sampling noise, not a broken assay (2026-10-21)

Section 32 reported that re-running identical seeds moved TYK2 V678L from ~3/8 compact to 0/8 and
concluded that **"run-to-run variation is the same size as the effects being called significant"**
and that **"the headline comparison is not fully controlled"**. Both statements are **withdrawn**.

### What was actually tested

Fisher exact on the compact counts of every genuinely recomputed duplicate pair:

| group | run A | run B | Fisher p |
|---|--:|--:|--:|
| TYK2 V678L 64/256 seeds 0-7 | 2/8 | 0/8 | 0.467 |
| JAK1 WT 128/512 seeds 0-4 | 0/5 | 2/5 | 0.444 |
| JAK2 WT 32/64 seeds 0-4 | 5/5 | 5/5 | 1.000 |
| JAK2 WT default MSA seeds 0-4 | 5/5 | 5/5 | 1.000 |

**Every pair is compatible with independent sampling.** None shows batch-level variation beyond
what binomial noise produces. The error in section 32 was treating a per-seed disagreement as
evidence of an uncontrolled experiment without testing whether the *counts* disagreed.

### Why per-seed results do not reproduce, and why that is fine

Inference runs with `--stochastic_dropout`, which is what generates seed-to-seed diversity in the
first place; dropout is normally disabled at inference. The random seed therefore labels a draw
rather than identifying a reproducible computation. **Exact reproducibility is not required - only
statistical reproducibility is**, and each seed remains an independent sample from the variant's
distribution, which is precisely what the pooled comparison assumes.

Two supporting checks confirm the input was held constant:

- **MSA is deterministic.** Across 50 run logs and 16 variants, every variant recorded the same MSA
  depth on every run (e.g. V678F 7529 across 6 runs, V678M 7519 across 5). Zero variation. The
  earlier speculation that a re-fetched alignment explained the divergence is refuted.
- **Hardware and software were constant.** All 204 GPU records across every run log are
  `NVIDIA RTX PRO 6000 Blackwell Server Edition`, with torch `2.11.0+cu130` throughout, including
  both members of the diverging V678L pair.

### Consequence

**The reported p-values stand as computed.** V678F at 0/24 against wild type's 8/24, p = 0.0003,
compares independent draws and requires no deflation. The same applies to every other comparison in
this document.

### The limit that does remain

Four pairs of 5-8 seeds have **low power** to detect a moderate batch effect, so this is "no
evidence of excess run-to-run variation", not "proven none". Duplicates are worth keeping and
accumulating opportunistically, but a dedicated replicate-calibration experiment is no longer
urgent.

The one thing section 32 got right: **do not delete the duplicate folders.** They are the only
replicate data the project has, and they are what made this test possible.

---

## 34. What the extended state of JAK3 actually is (2026-10-21)

`conclusions_20261016_150500.md` recorded an open question: every JAK3 run carried only one
reference (AF2 JAK3, itself compact at 41.5 A), so every structure was "nearest AF2" by default and
**the extended state was never identified** - open, 7T6F-like, or other. That classification was
listed as needing no GPU. It has now been done.

### Method

All 14 JAK3 runs push `selected_open.pdb` and `selected_closed.pdb`, so coordinates were available
without re-running anything. Each of the 28 structures was compared against six references mapped
onto JAK3 numbering by global pairwise sequence alignment: AF2 JAK3, Jeanpierre closed JAK1,
Jeanpierre open JAK1, 7T6F (active dimer, mouse JAK2), 8EWY (open dimer, mouse JAK2) and 4OLI
(closed TYK2). Metric as used throughout: superpose JH2 onto the reference's JH2, then measure the
JH1 Calpha RMSD without further movement.

### Result

| JAK3 state | FERM-JH1 | best-matching reference | RMSD |
|---|--:|---|--:|
| extended | ~94 A | **Jeanpierre open JAK1** | **1.6-3.5 A** |
| compact | ~41-44 A | **AF2 JAK3 / Jeanpierre closed JAK1** | **2.0-5.6 A** |
| intermediate | ~47-57 A | **none** | >= 44 A to all six |

**1. The extended state of JAK3 is the canonical open state.** It matches Jeanpierre's open JAK1
model to **1.6 A** - a near-perfect cross-paralogue match. The question is answered, and the answer
is ordinary: nothing novel is going on at the open end.

**2. JAK3 never reaches the 7T6F active-dimer arrangement.** Across all 28 structures the closest
approach is **46.3 A**, against a ~10 A match threshold. JAK1 enters that arrangement readily - it
is the "third arrangement" of section 3, matched to 4.9 A, and JAK1 V658F drives 16/16 seeds into
it at 96/384. **JAK3 does not, at any depth or in any variant.** The third arrangement is therefore
not a general JAK behaviour but something specific to JAK1 in this pipeline.

**3. A large class of JAK3 structures matches nothing at all.** Many sit at FERM-JH1 47-57 A -
inside the "compact" bin as the project defines it (< 60 A) - yet lie 86-120 A from every reference
including the closed ones. The compact bin has been pooling genuinely closed structures with these
unassigned ones. This is the same compact-is-not-closed problem documented for TYK2 (where 15/15
seeds at 32/64 were compact and 0/15 closed), now quantified for JAK3.

**4. A side-result worth keeping.** The JAK3 closed arrangement agrees with Jeanpierre's
independently built closed JAK1 model to ~5 A, and AF2 JAK3 has the **lowest inter-domain PAE of
the four paralogues** (18.5 A FERM-JH1, against 21.0 JAK2, 23.1 TYK2, 25.8 JAK1). Two independent
models converging is weak corroboration that the JAK3 closed arrangement is real. That is more than
can be said for TYK2, whose AF2 closed state has PAE 23.1 and no independent model to check against.

### Consequence

The JAK3 variant classes reported earlier - "closed state abolished" (M592F, A572V, Y581C) versus
"tightened" (M511I, A573V, R657Q) - were derived against AF2 alone. The reference set now shows that
what a JAK3 variant moves *away from* is the canonical closed arrangement, and what it moves
*towards* is either the canonical open state or the unassigned intermediate - **never the active
dimer**. Any mechanistic reading of those classes should say so explicitly.

## 35. Correction to section 34: 7T6F and 8EWY are mouse JAK1, not mouse JAK2 (2026-10-22)

Section 34 labels the two EM dimer references as "7T6F (active dimer, mouse JAK2)" and "8EWY (open
dimer, mouse JAK2)". **Both are mouse JAK1.** The earlier text of this document (section 18) had it
right - "JAK1 dimer, 7T6F" - and the relabelling introduced in section 34 was the error.

### How it was settled

Neither entry carries a UniProt cross-reference in the PDB, which is how the mistake survived. The
kinase chain of each was therefore aligned against four reference sequences with BLOSUM62 global
alignment:

| reference | identity to 7T6F chain A | identity to 8EWY chain A |
|---|--:|--:|
| **JAK1_MOUSE (P52332)** | **98.0 %** | **98.0 %** |
| JAK1_HUMAN (P23458) | 93.3 % | 93.3 % |
| JAK2_MOUSE (Q62120) | 43.1 % | 43.1 % |
| JAK2_HUMAN (O60674) | 43.1 % | 43.1 % |

Both chains are 1173 residues and give identical numbers, so the two entries are the same construct
in two arrangements. 98 % versus 43 % is not a close call. The accession quoted in session notes as
"mouse JAK2, P52332" was itself self-contradictory: P52332 *is* JAK1_MOUSE.

Entry metadata, for the record: 7T6F, "Structure of active Janus Kinase (JAK) dimer complexed with
cytokine receptor intracellular domain", cryo-EM, released 2022-03-16, Glassman et al., *Science*
2022. 8EWY, "Structure of Janus Kinase (JAK) dimer complexed with cytokine receptor intracellular
domain", cryo-EM, released 2023-03-08, *Cell Reports* 2023. Both *Mus musculus*; 7T6F's second
entity is interferon lambda receptor 1, consistent with a JAK1-bearing complex.

### What this changes

The numbers in section 34 are unaffected - the coordinates were right, only the label was wrong -
but two readings of them improve:

1. **Section 34 point 2 is less surprising than it was written.** "JAK1 enters the 7T6F arrangement
   readily, JAK3 does not at any depth" is a comparison of JAK1 against *its own* experimental
   structure, not against a JAK2 one. A paralogue matching its own EM dimer to 4.9 A while a
   different paralogue stays 46.3 A away is the expected ordering, so the claim that the third
   arrangement is "specific to JAK1 in this pipeline" is now partly circular: it may be specific to
   *having an experimental reference*. It still stands as an observation about JAK3 - JAK3 never
   reaches that arrangement - but it is no longer evidence that JAK1 is special among paralogues.
2. **Every experimental multi-domain JAK reference in this project is JAK1.** 7T6F and 8EWY were the
   only two entries in the family found to contain FERM and JH1 together (section 24). With both
   being mouse JAK1, there is **no experimental multi-domain structure for JAK2, JAK3 or TYK2 at
   all** - the family's entire measured arrangement evidence rests on one paralogue in one organism.
   Every closed-state TYK2 number in this document is a comparison against either a predicted model
   or a cross-paralogue JAK1 structure.

## 36. Is our 93 A open state really open? Answered against experiment (2026-10-22)

Section 18 recorded the open question: our template-free TYK2 runs produce a 93 A FERM-JH1 state,
every experimental extended JAK structure sits at ~84 A, and FERM-JH1 centroid distance alone cannot
tell "canonically open" from "merely far apart". The eight template-free TYK2 structures with
FERM-JH1 > 80 A were therefore superposed on six references by the project's standard arrangement
metric - superpose JH2, then measure JH1 Calpha RMSD with no further movement.

| our structure | FERM-JH1 | 8EWY open (exp, JAK1) | 7T6F active (exp, JAK1) | AF2 TYK2 closed | Jeanpierre open | Jeanpierre closed |
|---|--:|--:|--:|--:|--:|--:|
| 128/512 run, open pick | 93.5 | **5.1** | 47.1 | 82.5 | **2.8** | 81.4 |
| 128/512 run, closed pick | 93.4 | **5.0** | 47.5 | 82.0 | **3.6** | 80.9 |
| 96/384 run, closed pick | 93.8 | **6.0** | 48.0 | 82.5 | **4.4** | 81.3 |
| 96/384 run, open pick | 89.8 | 40.3 | 61.7 | 90.6 | 39.3 | 88.6 |
| 64/256 run, closed pick | 87.4 | 43.8 | 63.2 | 89.3 | 43.2 | 87.4 |
| 64/256 run, open pick | 89.7 | 45.0 | 67.9 | 91.0 | 44.6 | 88.4 |
| 64/256 run, closed pick | 84.4 | 50.4 | 64.8 | 88.8 | 49.7 | 87.1 |
| 64/256 run, open pick | 84.0 | 59.1 | 63.4 | 95.6 | 57.4 | 94.8 |

("open pick" and "closed pick" are the per-run selection labels the pipeline writes; they are
*within-run* extremes, which is why a run's "closed" pick can still be 93 A. They are not state
assignments and should not be read as such.)

### Answer: yes for three of eight, and no for the other five

**1. The 93 A state is the canonical open state.** The three structures at 93.4-93.8 A match the
experimental open dimer 8EWY to **5.0-6.0 A** and Jeanpierre's independently built open model to
**2.8-4.4 A**. A 2.8 A cross-paralogue arrangement match is as good as this metric gets. The
reservation recorded in section 18 - "our 93 A state has no experimental counterpart" - was too
strong: it has no *TYK2* counterpart, but it reproduces the arrangement of the one experimentally
determined extended JAK to within the metric's resolution. That is a real result and it is the first
time anything in this project has been validated against a measured multi-domain arrangement.

**2. Open by distance is not open by arrangement.** The five structures at 84.0-89.8 A are **40-59 A
from 8EWY** and equally far from every other reference. They are extended, they are not the open
state, and they are not the active dimer either (63-68 A from 7T6F). FERM-JH1 > 80 A has been used
throughout this document as the open criterion; on this evidence it is wrong in 5 of 8 cases. This is
the same failure already documented at the other end - "compact < 60 A" pooling genuine closed
structures with unassigned ones (sections 24, 34) - and it now closes the loop: **neither bin of the
centroid-distance classifier is a state.** Only the superposition metric assigns states.

**3. The split is by depth, and it is the inverse of the usual story.** All three canonical-open
structures come from the two *deeper* MSA settings (128/512, 96/384); all five unassigned extended
ones come from 64/256 and one 96/384 run. Deeper MSA gives the clean, reproducible, experimentally
matching open state; shallower MSA gives extended structures that match nothing. 64/256 has been
treated as the one informative TYK2 depth because it is the only one with dynamic range (WT 7/16
compact). Its range is now partly an artefact: it is producing a population of arrangements that are
not states, and any mutation effect measured there is measured against that background.

### Consequence for the mutation results

Every TYK2 variant comparison in sections 25-31 was scored at 64/256 or 96/384 with the FERM-JH1
threshold. Those comparisons are internally consistent - the same classifier was applied to variant
and wild type alike - so the reported contrasts do not become wrong. But "the variant opens the
structure" cannot be asserted from them, because at 64/256 the extended structures are mostly not
the open state. The claim that survives is the weaker one: the variant moves the structure *out of
the closed arrangement*. Re-scoring the variant series with the superposition metric is the next
analysis-only task, and it needs no GPU time.

## 37. Consequence of the section 35 correction: the 7T6F and 8EWY numbers themselves were wrong (2026-10-22)

The mislabelling corrected in section 35 was not only a label. The arrangement metric maps residues
between two structures by sequence alignment and then selects the JH2 and JH1 windows **using each
protein's own domain boundaries**, looked up by paralogue name. With 7T6F and 8EWY entered as JAK2,
every comparison against them used the JAK2 windows - JH2 536-827, JH1 849-1124 - on what is
actually a JAK1 chain, whose windows are JH2 583-855 and JH1 875-1154. The selected residues were
offset by roughly 30-50 positions at each boundary. Four analysis scripts shared the error.

All affected comparisons have been recomputed with `JAK1` boundaries. The corrected version of the
section 36 table:

| our structure | FERM-JH1 | 8EWY open (exp, JAK1) | 7T6F active (exp, JAK1) | AF2 TYK2 closed | Jeanpierre open | Jeanpierre closed |
|---|--:|--:|--:|--:|--:|--:|
| 128/512 run, open pick | 93.5 | **5.8** | 46.8 | 82.5 | **2.8** | 81.4 |
| 128/512 run, closed pick | 93.4 | **5.8** | 47.2 | 82.0 | **3.6** | 80.9 |
| 96/384 run, closed pick | 93.8 | **6.8** | 47.7 | 82.5 | **4.4** | 81.3 |
| 96/384 run, open pick | 89.8 | 42.3 | 63.0 | 90.6 | 39.3 | 88.6 |
| 64/256 run, closed pick | 87.4 | 46.1 | 64.6 | 89.3 | 43.2 | 87.4 |
| 64/256 run, open pick | 89.7 | 47.1 | 69.2 | 91.0 | 44.6 | 88.4 |
| 64/256 run, closed pick | 84.4 | 52.8 | 66.5 | 88.8 | 49.7 | 87.1 |
| 64/256 run, open pick | 84.0 | 61.4 | 65.6 | 95.6 | 57.4 | 94.8 |

### What moved, and what did not

The 8EWY column for the three canonical-open structures moves from 5.0-6.0 A to **5.8-6.8 A**, and
for the five unassigned extended ones from 40-59 A to **42-61 A**. The 7T6F column moves by about
0.5-2 A. Columns that never involved the two EM entries - AF2 TYK2, both Jeanpierre models, and the
two SWISS-MODEL TYK2 templates - are untouched, which is the expected signature of this specific bug
and is how the size of the effect was checked.

**Every conclusion in section 36 survives.** The three deep-MSA structures still match the
experimental open arrangement within the metric's resolution; the five shallow-MSA ones are still
40-60 A from everything; the split by MSA depth is unchanged; and "FERM-JH1 > 80 A" still fails as an
open criterion in 5 of 8 cases. The correction shifts digits, not findings. It is recorded because
the shift is large enough (up to 1.8 A on the headline match) that the published numbers would not
have reproduced.

### Note on the method

The useful detail is *why* a ~40-residue window offset produced only a ~1 A change: the metric
superposes on JH2 and then measures JH1 displacement, and both domains are globular and internally
rigid, so dropping or adding a turn at each end barely moves either centre of mass. The metric is
robust to boundary error - which is reassuring for its use throughout this project, and is also
exactly why the error was invisible for so long. It will not announce itself; it has to be checked
at the source. Both paralogue assignments in the reference set are now verified against UniProt
sequences rather than taken from notes.

## 38. JAK3 re-classified with corrected JAK1 boundaries, and its open state matches experiment too (2026-10-22)

Section 34 classified all 28 JAK3 structures against six references, with 7T6F and 8EWY entered
under JAK2 boundaries - the error of sections 35 and 37. The full run has been repeated with `JAK1`
boundaries. Columns not involving those two entries are identical, as expected.

| JAK3 run | pick | FERM-JH1 | AF2 JAK3 | Jeanpierre closed | Jeanpierre open | 7T6F active | 8EWY open | 4OLI closed |
|---|---|--:|--:|--:|--:|--:|--:|--:|
| WT 512/8192 | open | 94.4 | 82.3 | 81.6 | **1.6** | 46.0 | **5.8** | 80.2 |
| WT 512/8192 | closed | 94.0 | 82.3 | 81.5 | **1.9** | 46.8 | **5.9** | 80.2 |
| WT 256/1024 | open | 94.1 | 82.1 | 81.2 | **2.6** | 47.3 | **4.9** | 79.9 |
| M592F 128/512 | closed | 94.2 | 83.1 | 82.3 | **3.5** | 47.6 | **7.6** | 81.0 |
| Y581C 128/512 | closed | 95.3 | 83.9 | 83.2 | **2.8** | 46.9 | **7.6** | 81.9 |
| M511I 128/512 | closed | 41.5 | **2.0** | 4.9 | 80.7 | 80.6 | 79.0 | **3.0** |
| A573V 128/512 | closed | 41.6 | **2.3** | 5.3 | 80.7 | 80.5 | 78.9 | **3.1** |
| R657Q 128/512 | closed | 42.4 | **3.0** | 5.6 | 80.2 | 80.1 | 78.4 | **3.2** |
| WT 256/1024 | closed | 43.1 | 15.7 | 12.4 | 87.1 | 90.1 | 85.2 | 15.8 |
| WT 128/512 | closed | 43.7 | 16.2 | 13.3 | 87.3 | 90.2 | 85.5 | 16.4 |
| A572V 128/512 | closed | 44.6 | 17.8 | 14.5 | 87.9 | 91.5 | 85.9 | 18.0 |
| M511I 128/512 | closed | 44.8 | 22.0 | 18.5 | 89.5 | 93.8 | 87.5 | 21.8 |
| A572V 128/512 | open | 47.8 | 47.7 | 44.5 | 92.0 | 101.1 | 91.0 | 47.1 |
| 14 further structures | - | 46.9-56.8 | 66.6-92.4 | 64.4-93.6 | 91.5-106.2 | 80.0-101.3 | 94.9-109.4 | 65.9-92.8 |

**1. The JAK3 extended state matches an experimental structure, not only a model.** Section 34
established the match to Jeanpierre's open JAK1 model (1.6-3.5 A, unchanged). With the boundaries
fixed, the same five structures sit **4.9-7.6 A from 8EWY**, the cryo-EM open JAK1 dimer. Section 34
had this as 4.7-5.5 A from a wrongly-windowed reference; the corrected range is wider but the
conclusion is stronger than stated at the time, because a match to a measured structure carries
weight that a match to another prediction does not. Together with section 36, **both TYK2 and JAK3
reproduce the experimental open JAK1 arrangement to within 5-8 A at deep MSA**, from sequence alone,
with no template.

**2. JAK3 still never reaches the active dimer.** The closest approach over all 28 structures is
**46.0 A** (was 46.3 A), against a ~10 A match threshold. Claim 2 of section 34 stands, with the
caveat added in section 35: 7T6F is a JAK1 structure, so "JAK1 reaches it and JAK3 does not" is a
paralogue matching its own experimental reference, not evidence that JAK1 is conformationally
special.

**3. The closed bin splits three ways, which section 34 understated.** Three structures (M511I,
A573V, R657Q closed picks, all 41.5-42.4 A) match AF2 JAK3 to **2.0-3.0 A** and 4OLI to 3.0-3.2 A -
genuinely closed. Four more (WT 128/512 and 256/1024, A572V, M511I, 43.1-44.8 A) sit at **15.7-22.0
A** from AF2: the same bin, the same FERM-JH1 range, but a measurably different arrangement, and
outside the project's own 15 A match threshold. Section 34 reported the closed range as "2.0-5.6 A",
which described only the first group. Fourteen structures at 46.9-56.8 A match nothing at all, as
reported.

So the compact end of the JAK3 distribution contains three populations, not one: canonically closed
(3), a near-closed arrangement 16-22 A away (4), and unassigned (14). The "closed state abolished"
versus "tightened" variant classes of the earlier work were drawn across this structure without
resolving it.

## 39. The whole TYK2 campaign re-scored by arrangement, not by FERM-JH1 bins (2026-10-22)

Section 36 ended by naming the next task: every TYK2 variant comparison was scored with the
centroid-distance bins ("compact < 60 A", "open > 80 A"), and both bins had just been shown not to
be states. All 200 TYK2 run folders were therefore pulled and every `selected_open.pdb` and
`selected_closed.pdb` re-scored against five references by the arrangement metric, with assignment
to a reference when within the project's own 15 A match threshold.

### A data-integrity finding first

The 200 folders hold **394 structures but only 138 distinct computations.** Two depths account for
almost all of the inflation: 65 folders labelled 256/1024 and 41 labelled 512/8192, every one of them
timestamped between 19:30 and 22:56 on 2026-10-21, every one carrying the same config and
`random_seeds: "0"`. They are the repeated notebook reruns caused by the controller bug fixed earlier
tonight: each rerun minted a fresh `RUN_DIR` and re-pushed the *same* inference output. Structures
were deduplicated by geometric identity - identical FERM-JH1 and identical distances to all five
references to 0.01 A means the same computation under a new name, not a new sample.

Checked and clear: `all_results.py` keys seeds on `(seed, value)`, so identical values collapse and
the master table was never inflated by this. Any count taken directly from the folder listing would
have been.

### The result

| variant | MSA | mode | n | closed | open | active dimer | unassigned | old bins: < 60 A | > 80 A |
|---|---|---|--:|--:|--:|--:|--:|--:|--:|
| WT | 512/8192 | free | 4 | 0 | **4** | 0 | 0 | 0 | 4 |
| WT | 256/1024 | free | 4 | 0 | **4** | 0 | 0 | 0 | 4 |
| WT | 128/512 | free | 2 | 0 | **2** | 0 | 0 | 0 | 2 |
| WT | 96/384 | free | 2 | 0 | 1 | 0 | 1 | 0 | 2 |
| WT | 64/256 | free | 6 | 0 | 0 | 0 | **6** | 2 | 4 |
| WT | 32/64 | free | 2 | 0 | 0 | 0 | **2** | 2 | 0 |
| WT | 128/512 | rel3 | 16 | **16** | 0 | 0 | 0 | 16 | 0 |
| WT | 128/512 | tmpl | 2 | **2** | 0 | 0 | 0 | 2 | 0 |
| V678F | 128/512 | rel3 | 26 | **26** | 0 | 0 | 0 | 26 | 0 |
| V678M | 128/512 | rel3 | 16 | **16** | 0 | 0 | 0 | 16 | 0 |
| V678I | 128/512 | rel3 | 4 | **4** | 0 | 0 | 0 | 4 | 0 |
| V678F | 96/384 | free | 4 | 0 | **4** | 0 | 0 | 0 | 4 |
| P982A | 96/384 | free | 2 | 0 | 0 | 0 | 2 | 0 | 2 |
| P982A | 128/512 | free | 2 | 0 | **2** | 0 | 0 | 0 | 2 |
| V678A | 64/256 | free | 4 | 0 | 2 | 0 | 2 | 0 | 4 |
| V678G | 64/256 | free | 4 | 0 | 2 | 0 | 2 | 0 | 4 |
| V678F | 64/256 | free | 6 | 0 | 2 | 0 | 4 | 0 | 6 |
| V678D | 64/256 | free | 4 | 0 | 1 | 0 | 3 | 2 | 2 |
| V678M | 64/256 | free | 4 | 0 | 1 | 0 | 3 | 0 | 3 |
| V678L | 64/256 | free | 6 | **1** | 0 | 0 | 5 | 2 | 3 |
| V678I | 64/256 | free | 4 | 0 | 0 | 0 | 4 | 3 | 1 |
| V678W | 64/256 | free | 4 | 0 | 0 | 0 | 4 | 1 | 2 |
| P982A | 64/256 | free | 4 | 0 | 0 | 0 | 4 | 1 | 3 |
| P982A, V678F, WT | 32/64 | free | 8 | 0 | 0 | 0 | **8** | 8 | 0 |

Totals by mode: **free n = 74 - 1 closed, 25 open, 0 active dimer, 48 unassigned.
rel3 n = 62 - 62 closed. tmpl n = 2 - 2 closed.**

**1. Template-free TYK2 prediction essentially never produces the closed state.** One structure out
of 74 (a V678L pick at 64/256) lands within 15 A of 4OLI or AF2. Every other closed structure in the
entire campaign - 64 of them - came from a run that was given 4OLI, either throughout or for the
first three recycles. This is the single most consequential re-reading: the closed basin in this
pipeline is **template-induced, not predicted.** Section 18's caution ("the closed basin exists and
is stable once entered; free prediction at 128/512 simply never enters it") turns out to hold at
*every* depth tried, not just 128/512.

**2. The compact bin contains no closed structures at all.** Of 14 free-run structures with FERM-JH1
< 60 A, **zero** are the closed arrangement. The "WT 7/16 compact at 64/256" figure that made 64/256
the project's one informative depth was never counting closed structures. It was counting
unassigned compact ones.

**3. The depth ladder is cleaner by arrangement than by distance.** Wild type is canonically open at
every depth from 96/384 up (11 of 12 structures) and never open below it (0 of 8). The transition is
between 96/384 and 64/256, and below it the model does not produce a state at all - it produces
arrangements that match nothing. "Shallow MSA opens the closed state" is wrong in both halves:
shallow MSA does not reach the closed state, and it does not reach the open one either.

**4. No variant differs from wild type at 64/256.** Testing the fraction reaching canonical open:

| variant | open / n | Fisher p vs WT |
|---|--:|--:|
| WT | 0/6 | reference |
| V678A | 2/4 | 0.133 |
| V678G | 2/4 | 0.133 |
| V678F | 2/6 | 0.455 |
| V678D | 1/4 | 0.400 |
| V678M | 1/4 | 0.400 |
| V678I, V678L, V678W, P982A | 0/4-0/6 | 1.000 |
| **all variants pooled** | **8/40** | **0.571** |

Nothing is significant, and the pooled test is not even in a suggestive direction. The ordering is
mildly interesting - the small residues A and G reach open most often, W and I never - but at n = 4-6
per variant it is noise.

**5. The release assay is confirmed by a second, independent metric.** 62 of 62 release structures
across WT, V678F, V678M and V678I are within 15 A of the closed reference. No substitution at 678
releases the closed state. This was already the conclusion from FERM-JH1 and the arrangement RMSD
separately; it now also holds under threshold-based assignment, and it is the one TYK2 result in this
document that has never wobbled.

### What this retracts

The variant contrasts of sections 25-31, where they rested on compact-versus-open counts at 64/256 or
96/384, do not survive. They were comparisons between two populations neither of which is a state:
"compact" structures that are not closed, and "open" structures that at 64/256 are mostly not open.
The honest summary of the TYK2 mutation work is now: **the release assay shows no V678 substitution
destabilises the closed state (n = 62, unanimous), and the template-free runs have no measured
variant effect on arrangement at any depth.** The abundance correlation of section 30 (rho = +0.62
over the V678 series) was computed on the compact fraction and inherits the same problem; it needs
recomputing on arrangement assignments before it can be quoted again.

## 40. Coverage limit of section 39, and what it does and does not let us say (2026-10-22)

Section 39 re-scored "all 200 TYK2 run folders". It is worth being exact about what that covers,
because it changes how two of its five claims should be read.

Each run pushes exactly **two** structures to the repository - `selected_open.pdb` and
`selected_closed.pdb` - not one per seed and certainly not one per recycle. A 64/256 run with 8 seeds
contributes 8 x 15 = 120 structures to the master results table and **2** to the repository. So the
138 distinct computations of section 39 are 138 *run representatives*, and the per-variant n of 4-6
is a count of representatives, not of samples. Section 30's counts (0/24, 2/16, 4/16, 5/16, 8/24) are
per-seed and come from the master table, which is why they are larger.

### Claim 1 survives, and the reason is worth recording

"Template-free prediction essentially never reaches the closed state (1 of 74)" is **not** weakened
by sampling only representatives, because `selected_closed.pdb` is the run's own best closed
candidate. Checked explicitly: it is the better match to a closed reference than the open pick in
**192 of 197** runs. If a run's best closed candidate is more than 15 A from both 4OLI and AF2, no
structure in that run is within 15 A. Sampling the extreme is the right sampling for an existence
claim, so claim 1 is if anything conservative. The same argument carries claims 2, 3 and 5.

### Claim 4 is underpowered, not negative

"No variant differs from wild type at 64/256" was computed on 4-6 representatives per variant. The
correct reading is **not established** rather than **no effect**: a representative is an extreme, so
the fraction of representatives reaching canonical open is not an unbiased estimate of the fraction
of seeds that do. The Fisher tests in section 39 should be treated as uninformative about variant
effects, and the sentence in that section's retraction - "the template-free runs have no measured
variant effect on arrangement at any depth" - is too strong. It should read: **no variant effect on
arrangement has been measured, because the per-seed structures needed to measure it were never
pushed.**

### The DMS correlation cannot be settled from the repository

Section 39 said the rho = +0.600 abundance correlation of section 30 "needs recomputing on
arrangement assignments". Recomputed on the representatives, over the same nine points:

| score used | rho vs IFN-alpha 1 U | p | rho vs abundance | p |
|---|--:|--:|--:|--:|
| compact fraction (< 60 A) | -0.070 | 0.858 | **+0.000** | 1.000 |
| open by distance (> 80 A) | -0.190 | 0.625 | +0.069 | 0.860 |
| canonical open (arrangement) | -0.369 | 0.329 | -0.026 | 0.946 |

All three are null. But the first row is the *same score* section 30 used, and on representatives it
gives 0.000 where the per-seed data gave +0.600. **So this table does not refute section 30 - it
shows that representatives cannot reproduce it either way.** The change from +0.600 to 0.000 is
attributable to the sampling, not to the metric, and nothing can be concluded about whether
arrangement-based scoring would preserve or destroy the abundance correlation.

Section 30's rho = +0.600 therefore stands exactly as it was already qualified there: p = 0.285 on
five points, with wild type pinned at zero on both axes by construction. It is neither strengthened
nor weakened by tonight's work.

### What this queues

To score arrangement per seed rather than per run, the pipeline has to push per-seed structures. Two
options, both cheap: push `seed_NNN/.../recycle15_unrelaxed.pdb` for every seed alongside the two
selected files, or compute the arrangement metric inside the notebook - where every recycle of every
seed is already in memory - and push the numbers rather than the coordinates. The second is better:
it costs one extra column in the results JSON and no storage, and it would have let all of sections
24, 34, 36 and 39 be read off the existing table instead of requiring 394 downloads. **This is the
single highest-value change to the pipeline identified so far**, and it needs no GPU time to
implement, only a notebook edit applied on the next run.

## 41. Retraction of section 40, and the TYK2 variant effect measured at full power (2026-10-22)

### Retraction first

Section 40 stated that "the per-seed structures needed to measure it were never pushed" and queued a
pipeline change to start pushing them. **That is wrong.** Every run folder already contains
`all/index.csv` plus `all/seed_NNN/recycle_NN.pdb.gz` for all 15 recycles of all 8 seeds - 120
structures per run - and `all/seed_NNN/metrics.json` and `recycle_metrics.jsonl` besides. The data
has been in the repository all along. The claim was made after listing a run folder's top level and
not opening the `all/` directory. The queued pipeline change in section 40 is withdrawn: nothing
needs to be pushed that is not already there.

Section 39's claim 4 ("no variant differs from wild type at 64/256") is likewise withdrawn. It was
computed on 4-6 run representatives, and with the per-seed data the opposite is true.

### The measurement

The final recycle of every seed of all 26 template-free 64/256 runs was scored by the arrangement
metric against five references - 4OLI, AF2 TYK2, 8EWY, 7T6F, Jeanpierre open - and assigned to the
nearest within 15 A. 208 structures, 16-32 per variant, the same power as the master results table.

| variant | n | canonical open | fraction | closed | unassigned | Fisher p vs WT | Holm |
|---|--:|--:|--:|--:|--:|--:|--:|
| WT | 24 | 2 | 0.083 | 0 | 22 | reference | - |
| **V678F** | 24 | **18** | **0.750** | 0 | 6 | 4.6e-06 | **<0.0001** |
| **V678A** | 16 | **10** | **0.625** | 0 | 6 | 4.2e-04 | **0.0033** |
| **V678I** | 24 | **13** | **0.542** | 0 | 11 | 1.4e-03 | **0.0094** |
| V678D | 16 | 7 | 0.438 | 0 | 9 | 0.018 | 0.105 |
| V678G | 24 | 9 | 0.375 | 0 | 15 | 0.036 | 0.182 |
| P982A | 16 | 5 | 0.312 | 0 | 11 | 0.094 | 0.377 |
| V678M | 16 | 4 | 0.250 | 0 | 12 | 0.195 | 0.586 |
| V678L | 32 | 6 | 0.188 | 2 | 24 | 0.444 | 0.888 |
| V678W | 16 | 1 | 0.062 | 0 | 15 | 1.000 | 1.000 |

**1. Three variants open the structure, and the effect is large and survives correction for nine
comparisons.** V678F takes wild type from 8 % to 75 % canonical open; V678A to 63 %, V678I to 54 %.
These are not threshold artefacts - "canonical open" here means within 15 A of the cryo-EM open JAK1
dimer or of Jeanpierre's open model, by superposition. This is the first well-powered,
multiple-testing-corrected, experimentally-referenced variant effect in the project.

**2. The closed state is confirmed absent.** 2 of 208 structures (both V678L) are within 15 A of a
closed reference. Section 39's claim 1 holds at per-seed resolution: template-free TYK2 prediction
does not reach the closed arrangement at 64/256, for wild type or for any variant.

### The correlation with the deep mutational scan collapses

Both scores were computed on the same 208 structures and correlated against the measured data over
the nine V678 points with wild type pinned at zero:

| score | rho vs IFN-alpha 1 U | p | rho vs abundance | p | rho vs IFN-alpha 100 U | p |
|---|--:|--:|--:|--:|--:|--:|
| **canonical open (arrangement)** | -0.017 | 0.966 | **-0.083** | 0.831 | -0.017 | 0.966 |
| compact fraction (< 60 A) | +0.213 | 0.582 | **+0.528** | 0.144 | +0.630 | 0.069 |

The two scores order the variants almost oppositely. By compact fraction, V678F and V678G are at the
bottom (0.00) - they *leave* the compact bin. By open fraction, V678F is at the top (0.75) - it
*arrives* at the open state. Compact fraction is a measure of failing to stay put; open fraction is a
measure of reaching a specific destination. They are not two views of one axis.

**Section 30's finding is reproduced and localised, not overturned.** Its rho = +0.600 against
abundance reappears here as +0.528 on the same score with more seeds, and the stronger relation is
actually with signalling at 100 U (+0.630, p = 0.069) - which section 30 did not test. But that
correlation belongs to the *compact fraction* specifically. The arrangement-based score, which is the
one tied to experimental references and the one that yields the significant variant effects above,
correlates with **neither** measured axis (|rho| < 0.09).

So the pipeline's two scores answer different questions and only one of them has external support:
- **compact fraction** correlates weakly with the measured data (abundance, and signalling at high
  dose) but counts structures that are not a state, and has no significant per-variant effects after
  correction;
- **canonical open fraction** gives large, corrected, experimentally-anchored variant effects but is
  uncorrelated with anything measured about those variants.

The straightforward reading is that V678F, V678A and V678I genuinely destabilise whatever holds the
model's compact arrangement together, that the model then relaxes into the canonical open state, and
that **this has no detectable relationship to either the abundance or the activity of the real
protein.** The earlier framing - "our signal tracks abundance, not activation" (section 30) - should
now be stated as: one of our two scores tracks abundance weakly and non-significantly; the score with
the real statistical power tracks nothing measured at all.

### What would settle it

The nine V678 substitutions span the measured abundance range from +0.002 (M) to -0.361 (W) and the
measured signalling range from -0.479 (D) to +0.561 (M), so the DMS axes are well sampled and the
null results are not a range problem. What is not sampled is **position**: all nine are at 678.
P982A is the only other site, and it sits mid-table at 0.312 (Holm 0.377). A second position with
four or five substitutions spanning the DMS range would tell us whether the open-fraction score is
measuring something position-specific or nothing at all. H582W, already queued for the release assay,
is the obvious candidate - measured IFN-alpha +1.339 (99.9th percentile) with abundance intact at
-0.083, which is the opposite corner of the DMS plane from V678W.

## 42. The whole TYK2 campaign at per-seed resolution, and a deduplication correction to section 41 (2026-10-22)

The per-seed scoring of section 41 has been extended from the 64/256 runs to every TYK2 run: the
final recycle of every seed of all 197 run folders, scored by the arrangement metric against 4OLI,
AF2 TYK2, 8EWY, 7T6F and Jeanpierre open, assigned to the nearest within 15 A. **323 distinct
structures.**

### Correction to section 41 first

Section 41's table counted V678I as 13/24 and V678G as 9/24. Both were inflated: one V678I run and
one V678G run are byte-identical re-pushes of another run. Verified by fingerprinting the full
`index.csv` - all 120 (seed, recycle) rows agree to three decimals on openness **and** to two
decimals on mean pLDDT:

- `TYK2_V678I_20261020_212231` == `TYK2_V678I_20261020_224133` (seeds 8-15)
- `TYK2_V678G_20261021_045409` == `TYK2_V678G_20261021_073753` (seeds 8-15)
- `TYK2_V678L_20261021_022531` == `TYK2_V678L_20261021_034851` (seeds 0-7)

Worth separating from the opposite case: `TYK2_V678L_20261020_235544` also carries seeds 0-7 and is
**not** identical to those two. Same seed numbers, different trajectories - exactly as expected,
since inference runs with stochastic dropout and a seed number is not a reproducibility handle. Only
byte-identical trajectory sets were dropped; same-seed independent draws were all kept.

Corrected, with Holm over the same nine comparisons:

| variant | open / n | fraction | Fisher p vs WT | Holm |
|---|--:|--:|--:|--:|
| WT | 2/24 | 0.083 | reference | - |
| **V678F** | 18/24 | **0.750** | 4.6e-06 | **<0.0001** |
| **V678A** | 10/16 | **0.625** | 4.2e-04 | **0.0033** |
| **V678I** | 8/16 | **0.500** | 6.8e-03 | **0.0479** |
| V678D | 7/16 | 0.438 | 0.018 | 0.105 |
| V678G | 6/16 | 0.375 | 0.042 | 0.210 |
| P982A | 5/16 | 0.312 | 0.094 | 0.377 |
| V678M | 4/16 | 0.250 | 0.195 | 0.586 |
| V678L | 3/24 | 0.125 | 1.000 | 1.000 |
| V678W | 1/16 | 0.062 | 1.000 | 1.000 |

The three significant variants survive, but **V678I is now marginal** (Holm 0.0479, against 0.0094 in
section 41). Only V678F and V678A are comfortably significant. The headline of section 41 stands;
its third entry should be reported as borderline.

### The whole campaign

| variant | MSA | mode | n | closed | open | dimer | unassigned | median FERM-JH1 |
|---|---|---|--:|--:|--:|--:|--:|--:|
| WT | 32/64 | free | 8 | 0 | 0 | 0 | **8** | 46.3 |
| WT | 64/256 | free | 24 | 0 | 2 | 0 | **22** | 91.0 |
| WT | 96/384 | free | 8 | 0 | **7** | 0 | 1 | 93.6 |
| WT | 128/512 | free | 8 | 0 | **8** | 0 | 0 | 93.5 |
| WT | 256/1024 | free | 2 | 0 | **2** | 0 | 0 | 93.6 |
| WT | 512/8192 | free | 2 | 0 | **2** | 0 | 0 | 93.4 |
| P982A | 32/64 | free | 24 | 0 | 0 | 0 | **24** | 40.6 |
| P982A | 64/256 | free | 16 | 0 | 5 | 0 | 11 | 93.4 |
| P982A | 96/384 | free | 8 | 0 | 2 | **2** | 4 | 91.0 |
| P982A | 128/512 | free | 8 | 0 | **8** | 0 | 0 | 93.2 |
| V678F | 32/64 | free | 8 | 0 | 0 | 0 | **8** | 49.8 |
| V678F | 64/256 | free | 24 | 0 | **18** | 0 | 6 | 94.7 |
| V678F | 96/384 | free | 16 | 0 | **16** | 0 | 0 | 93.4 |
| WT | 128/512 | tmpl | 16 | **16** | 0 | 0 | 0 | 39.2 |
| WT | 128/512 | rel3 | 8 | **8** | 0 | 0 | 0 | 39.0 |
| V678F | 128/512 | rel3 | 13 | **13** | 0 | 0 | 0 | 39.1 |
| V678M | 128/512 | rel3 | 8 | **8** | 0 | 0 | 0 | 38.7 |
| V678I | 128/512 | rel3 | 2 | **2** | 0 | 0 | 0 | 39.7 |

Totals: **template-free n = 276 - 2 closed, 109 open, 2 active-dimer, 163 unassigned. Release
n = 31 - 31 closed. Template-throughout n = 16 - 16 closed.**

**1. The wild-type depth ladder, by arrangement rather than by distance.** Fraction reaching
canonical open: 32/64 **0.00**, 64/256 **0.08**, 96/384 **0.88**, 128/512 **1.00**, 256/1024 **1.00**,
512/8192 **1.00**. The transition is a step between 64/256 and 96/384, not a gradient, and above it
the model is completely locked. Tonight's two new depths were run to fill a gap in this ladder and
they confirm saturation: nothing changes between 128/512 and 512/8192.

**2. 32/64 produces no state at any variant.** 40 structures across WT, P982A and V678F: zero closed,
zero open, all 40 unassigned, median FERM-JH1 40-50 A. The shallowest depth makes compact structures
that are not the closed state - the point of sections 24 and 39, now with 40 samples instead of 8.

**3. The only active-dimer structures in the entire TYK2 campaign are 2 of 8 P982A at 96/384.** Out
of 323 structures. Given that 7T6F is a JAK1 structure (section 35) and n = 2, this is a curiosity to
note, not a finding.

**4. The release assay is unanimous at per-seed resolution: 31/31.** Plus 16/16 for the
template-throughout runs. 47 structures, four sequences, every one closed, median FERM-JH1 38.7-39.7
A. No V678 substitution releases the closed state - including V678F, which is the substitution with
the largest template-free effect in the table above (0.75 open at 64/256). **A variant can open the
model completely when prediction starts from sequence and hold the closed state completely when
prediction starts from 4OLI.** That contrast, now measured at full power on both sides, is the
cleanest statement the TYK2 work supports.

### The compact-fraction correlation, deduplicated

| score | rho vs IFN-alpha 1 U | p | rho vs abundance | p | rho vs IFN-alpha 100 U | p |
|---|--:|--:|--:|--:|--:|--:|
| canonical open (arrangement) | -0.017 | 0.966 | -0.083 | 0.831 | -0.017 | 0.966 |
| compact fraction (< 60 A) | +0.205 | 0.596 | +0.556 | 0.120 | **+0.667** | **0.050** |

Unchanged in substance from section 41, and the strongest relation remains the one section 30 never
tested: compact fraction against signalling at **100 U**, rho = +0.667 at p = 0.050 on nine points.
That is one uncorrected test selected from six, so it is a hypothesis and not a result - but it is
the specific hypothesis worth testing next, and it points the opposite way from section 30's
conclusion. Section 30 compared against signalling at 1 U, found rho = -0.200, and concluded the
pipeline tracks abundance rather than activation. At 100 U the sign flips and the magnitude is the
largest in the table. **Which dose the scan is read at decides whether the pipeline looks like an
abundance sensor or an activation sensor**, and that should be settled on a second position before
either claim is repeated.

## 43. pLDDT cannot see the arrangement, and the guided-recycling objective is built on it (2026-10-22)

With 323 per-seed structures each carrying both a mean pLDDT and a measured distance to the nearest
reference arrangement, the question the project has never tested directly can now be asked: **does
the model's own confidence know which arrangement it produced?**

| state | n | median pLDDT | IQR | median FERM-JH1 |
|---|--:|--:|---|--:|
| closed (within 15 A of 4OLI / AF2) | 49 | 80.2 | 80.0-80.4 | 39.0 |
| canonical open (within 15 A of 8EWY / Jeanpierre) | 109 | 80.4 | 80.1-81.1 | 93.7 |
| active-dimer-like | 2 | 81.1 | 81.0-81.2 | 85.7 |
| **unassigned (> 15 A from everything)** | **163** | **80.1** | **79.2-80.5** | 82.3 |

Across all 323 structures pLDDT runs from 69.7 to 82.5 with an interquartile width of **0.7 points**,
while FERM-JH1 runs from 39 to 95 A. The four classes are indistinguishable: a structure that
reproduces a cryo-EM arrangement to within 15 A and a structure that is 40 A from every known
arrangement are assigned the same confidence to within a fraction of a point. The unassigned class is
not model failure - half of its members are **more than 40 A from every reference** (median 39.2 A,
maximum 75.7 A) and they are as confident as everything else.

### The apparent correlation is a depth confound

Pooled over all template-free structures, pLDDT does appear to track arrangement quality: Spearman
rho = **-0.468** (p = 2e-16) against distance to the nearest reference, i.e. higher confidence, closer
to a known state. That is Simpson's paradox. Split by MSA depth:

| depth | n | pLDDT range | median | rho(pLDDT, distance) | p |
|---|--:|---|--:|--:|--:|
| 32/64 | 40 | 69.7-79.2 | 77.2 | +0.018 | 0.914 |
| 64/256 | 184 | 78.7-81.2 | 80.2 | +0.138 | 0.061 |
| 96/384 | 32 | 80.3-81.4 | 81.0 | -0.277 | 0.125 |
| 128/512 | 16 | 81.4-82.0 | 81.6 | +0.057 | 0.833 |

**Within every depth the correlation is absent and not significant, and the signs disagree.** The
pooled relation is entirely the fact that shallow MSA lowers pLDDT *and* separately produces
arrangements far from any reference. Depth drives both; neither drives the other.

### Why this matters for the method

The pipeline selects structures by minimising **J = (1 - pLDDT_norm) + 0.1 x violation_loss**, across
recycles and across seeds **at a fixed MSA depth**. That is precisely the regime the table above
covers, and in that regime pLDDT carries no information about which arrangement was produced. So the
guided-recycling objective is not selecting for a conformational state, and the `selected_open.pdb` /
`selected_closed.pdb` picks are made on a signal blind to the thing they are named for. (The picks
are still *useful* - section 40 verified the closed pick is the better closed match in 192 of 197
runs - but that is because the notebook's selection also consults a reference distance, not because J
does.)

This also closes a loop with the AlphaFold confidence findings already in this document. Every
AlphaFold JAK model has FERM-JH1 PAE of 18.5-25.8 A against a ceiling of about 31 A (sections 24, 34)
- the network openly reports that it does not know the inter-domain arrangement. pLDDT is a
**per-residue** confidence and is near-blind to global arrangement by construction; it is high
whenever each domain is individually well-folded, which it always is here. The two measures agree:
**nothing in the model's confidence output constrains the arrangement**, and no amount of recycling
guided by pLDDT will change that.

### Consequence

The conformational results in this document rest on *where the structures actually land*, measured
against external references - not on the model preferring them. Stated plainly: the MSA depth is the
only control variable that works, the arrangement metric against experimental structures is the only
readout that works, and the pLDDT-based objective at the heart of the pipeline contributes nothing to
either. Any future selection among seeds should use the reference distance directly, and the honest
description of the method is "MSA subsampling plus external-reference classification", not "guided
recycling".

## 44. The whole family at per-seed resolution, and what the reference set actually is (2026-10-22)

The per-seed arrangement scoring was extended from TYK2 to JAK1, JAK2 and JAK3: the final recycle of
every seed of all 65 run folders in those three campaigns, added to TYK2's 323. **860 structures**,
scored against 4OLI, the two cryo-EM JAK1 dimers, both Jeanpierre models and the AlphaFold model of
each paralogue.

### First: the reference set is not what its labels say

Before any comparison, every reference was measured rather than assumed. FERM-JH1 centroid distance:

| reference | FERM-JH1 | by distance |
|---|--:|---|
| **4OLI (X-ray, TYK2)** | **no FERM in the structure** | JH2-JH1 only |
| AF2 TYK2 (P29597) | 39.7 | compact |
| Jeanpierre closed JAK1 | 40.0 | compact |
| AF2 JAK3 (P52333) | 41.5 | compact |
| 7T6F (cryo-EM, JAK1) | 84.1 | extended |
| **AF2 JAK1 (P23458)** | **92.3** | **extended** |
| Jeanpierre open JAK1 | 92.6 | extended |
| **AF2 JAK2 (O60674)** | **93.8** | **extended** |
| 8EWY (cryo-EM, JAK1) | 94.2 | extended |

Two things here have been assumed wrongly throughout this project.

**1. AlphaFold does not predict a compact JAK.** It predicts TYK2 and JAK3 compact (39.7, 41.5 A) and
JAK1 and JAK2 **extended** (92.3, 93.8 A). "The AlphaFold model is compact" is true for two
paralogues and false for the other two. Every cross-paralogue argument built on an AF2 closed state
needs checking against this. It also reframes the PAE observation: AlphaFold reports FERM-JH1 PAE of
18.5-25.8 A for all four (sections 24, 34) - it is not confident about any of them - and when it is
not confident it does not even pick the same answer twice across paralogues.

**2. 4OLI contains no FERM domain.** It is the TYK2 JH2-JH1 crystal structure. So "FERM-JH1 distance
in the closed state, 40-45 A" was never measured from 4OLI; it comes from AF2 TYK2 and from
Jeanpierre's closed JAK1 model, both predictions. Matching 4OLI constrains only how the kinase domain
sits on the pseudokinase. Every statement of the form "closed, like 4OLI, with FERM at 40 A" is two
claims, one measured and one extrapolated.

### The two readouts are formally independent and empirically never disagree

The project has two metrics and they measure different things. FERM-JH1 centroid distance says where
FERM sits. The arrangement metric superposes JH2 and measures JH1 displacement, and **never looks at
FERM at all** - so in principle a structure could match a compact reference's JH2-JH1 arrangement
while placing FERM anywhere. Checked across all 860 structures, in every case where both axes are
defined:

| matched reference is... | and the structure's FERM axis is compact | intermediate | extended |
|---|--:|--:|--:|
| a compact reference | **138** | 0 | 0 |
| an extended reference | 0 | 0 | **325** |
| 4OLI (no FERM) | **25** | 0 | 0 |

**488 of 488 agree; zero disagreements.** In this family the JH2-JH1 arrangement and the FERM
placement are tightly coupled, so either metric predicts the other. That is a useful validation of
both - and it is the reason the project's conclusions have survived being recomputed several times
tonight. It also means 4OLI-matching structures are compact in FERM (25/25) even though 4OLI itself
cannot say so.

### Paralogue behaviour, template-free

| paralogue | n | compact-ref | 4OLI | open model/dimer | active dimer | unmatched |
|---|--:|--:|--:|--:|--:|--:|
| JAK1 | 129 | 3 | 2 | 55 | **35** | 34 |
| JAK2 | 237 | 42 | 0 | 96 | 0 | 99 |
| JAK3 | 136 | 34 | 0 | 28 | 0 | 74 |
| TYK2 | 276 | 2 | 0 | 109 | 2 | 163 |

**1. The active-dimer arrangement is reached by JAK1 and essentially nothing else.** 35 of 129 JAK1
structures, against 0 of 237 JAK2, 0 of 136 JAK3 and 2 of 276 TYK2. **JAK1 V658F at 96/384 is 16/16
active-dimer** (median FERM-JH1 83.8 A against 7T6F's 84.1 A), and JAK1 wild type reaches it 4/5 at
64/256. This confirms section 3 at per-seed resolution - and with the correction of section 35 it
carries its proper caveat: 7T6F is a mouse **JAK1** structure, so this is a paralogue reproducing its
own experimental reference. It is a positive control that the pipeline can hit a measured
arrangement, not evidence that JAK1 is conformationally special.

**2. JAK2 never reaches the open or active arrangements at all** - 0 of 237 - yet 96 of its structures
match extended AF2 JAK2. JAK2 goes extended without going to either experimentally characterised
extended state. Its compact structures (42) all match Jeanpierre's closed model.

**3. TYK2 is the opposite of JAK2.** 109 open-model matches, 2 compact. Together with section 42's
finding that TYK2 reaches a compact JH2-JH1 arrangement only with a template, the paralogues split
cleanly: **JAK2 and JAK3 access the compact arrangement from sequence alone; JAK1 and TYK2 do not.**
JAK1 manages 3 of 129 and TYK2 2 of 276, against JAK2 42 of 237 and JAK3 34 of 136.

**4. Unmatched structures are 40 % of the family** (370 of 860, counting all modes). Every paralogue
produces them, at every depth below its transition. This is the largest single class in the data and
nothing is known about it beyond "more than 15 A from all nine references".

### Methodological note worth keeping

Two bugs were found and fixed in the course of this, both in code written tonight, both of the same
kind: **a cached intermediate reused across inputs it was not valid for.**

- The residue-alignment map was cached keyed on the reference alone. JAK1's runs mix a full-length
  1154-residue target with an early 586-residue JH2-JH1 construct renumbered from 1, so the truncated
  construct's map was reused for every full-length model. It turned a genuine 6.1 A match into a
  reported 79.5 A non-match and would have produced a spurious retraction of section 3. The key now
  includes the model construct.
- Domain windows were selected using the *model's* residue numbers, which returns zero pairs on any
  renumbered construct. Membership is now decided from the residue number in the reference via the
  alignment. Verified not to change full-length results before switching: 50.95 vs 50.95, 48.41 vs
  48.41, 79.85 vs 79.95, 89.39 vs 90.33 A - worst case 0.94 A, from a few residues at a window edge.

Checked and clear: TYK2 is a single uniform construct across the whole campaign (1187 residues,
numbered 1-1187, N-terminus MPLRHWGM, verified on five runs spanning every phase), as are JAK2 (1132)
and JAK3 (1124). The cache was only unsafe for JAK1. Sections 36-43 are unaffected.

**Three of the four 32/64 JAK1 runs are also not full-length JAK1** - they are that 586-residue
JH2-JH1 construct. Any JAK1 depth-ladder figure that pools them with the rest is comparing two
different targets, and no FERM-JH1 number can be quoted for them at all.

## 45. What `openness_A` actually measures, when runs commit, and the cheapest experiment available (2026-10-22)

Every run folder carries `all/index.csv` with one row per (seed, recycle) - 120 rows for an 8-seed
run - holding `openness_A`, `mean_plddt`, `J`, `violation_loss` and `selected`. None of tonight's
analysis had used it. It answers three questions without downloading a single structure.

### Correction: `openness_A` is the JH2-JH1 distance, not FERM-JH1

For run `TYK2_20261021_225030` seed 0, `index.csv` gives `openness_A = 46.585`. That run's own RESULT
payload reports **JH2-JH1 = 46.582** and **FERM-JH1 = 93.1**. The column is the JH2-JH1 centroid
distance.

This matters because the thresholds quoted throughout this document - "closed 40-45 A, open 90+" -
are **FERM-JH1** figures. A reader taking `openness_A` for the project's openness metric would see
46-50 A and conclude every TYK2 run is closed, when the same structures have FERM-JH1 of 90-95 A and
are extended. The per-seed trajectory tables in each run's `conclusions.md` are *not* affected: they
are built from the FERM-JH1 column and are labelled correctly. Only `index.csv` is ambiguous, and it
is the file an outside reader would reach for first.

### Runs commit early: 15 recycles is mostly wasted compute

For each of the 184 seed trajectories at 64/256 template-free, the commitment recycle is the first
recycle after which `openness_A` never again moves by more than 5 A:

| commitment recycle | 1 | 2 | 3 | 4 | 5 | 6 | 8+ |
|---|--:|--:|--:|--:|--:|--:|--:|
| seeds | 32 | 35 | 49 | 32 | 16 | 12 | 8 |

**Median 3. 63 % of seeds are committed by recycle 3, 89 % by recycle 5.** Recycles 6-15 change the
arrangement in 11 % of seeds and are pure cost in the other 89 %. Inference is run at 15 recycles
throughout the project.

Cutting to 6 recycles would save roughly **60 % of GPU time per run** while changing the outcome for
about one seed in nine - and those seeds could be recovered by spending the savings on more seeds,
which is the axis that actually carries the statistics. At the current rate (13 min per seed at
256/1024, 19 min at 512/8192) that is the difference between 8 seeds and 20 seeds per hour. This is
the single cheapest improvement available and it needs one config change, no new code. It should be
validated first by re-scoring recycle 6 against recycle 15 for seeds already in the repository -
also free, since every recycle of every seed is already pushed.

### The arrangement metric is far more sensitive than either centroid distance

The same 184 structures, wild type against V678F, by three readouts:

| readout | test | p |
|---|---|--:|
| FERM-JH1 centroid distance | Mann-Whitney | 0.012 |
| JH2-JH1 centroid distance | Mann-Whitney | 0.001 |
| canonical-open fraction (superposition) | Fisher | **4.6e-06** |

Four orders of magnitude between the best centroid distance and the superposition metric, on
identical data. The reason is visible in the per-variant medians:

| variant | median FERM-JH1 | median JH2-JH1 | open fraction |
|---|--:|--:|--:|
| V678F | 94.6 | 48.6 | **0.75** |
| V678A | 93.3 | 48.2 | 0.62 |
| V678I | 93.9 | 49.0 | 0.50 |
| V678D | 93.6 | 48.4 | 0.44 |
| V678G | 94.6 | 49.6 | 0.38 |
| P982A | 93.3 | 49.0 | 0.31 |
| V678M | 89.7 | 48.6 | 0.25 |
| V678L | 89.8 | 49.4 | 0.12 |
| WT | 90.5 | 50.0 | 0.08 |
| V678W | **93.6** | 50.2 | **0.06** |

**V678W and V678F have almost the same FERM-JH1 (93.6 vs 94.6) and opposite open fractions (0.06 vs
0.75).** A distance of 93.6 A is reached both by structures that reproduce the cryo-EM open
arrangement and by structures 40-60 A away from it, because the distance says nothing about
orientation. Across the ten variants, median FERM-JH1 predicts the open fraction only weakly
(rho = +0.62, p = 0.054) while median JH2-JH1 does better (rho = -0.81, p = 0.005) - but both are
variant-level aggregates, and neither separates individual structures the way superposition does.

Taken with section 43 - pLDDT is blind to arrangement within a depth - the readout hierarchy for this
project is now settled: **superposition against an experimental reference is the only metric that
resolves anything; the centroid distances are coarse proxies; pLDDT is noise.**

### The cheapest experiment: delete FERM from the input

Three of the earliest JAK1 runs used a 586-residue **JH2-JH1 construct** rather than full-length JAK1
(section 44). That accident is the most interesting unreplicated result in the repository. At 32/64,
the two seeds available give:

| construct | depth | 4OLI | Jeanpierre closed | pLDDT |
|---|---|--:|--:|--:|
| JH2-JH1 only, seed 0 | 32/64 | **7.3** | **6.8** | 88.1 |
| JH2-JH1 only, seed 1 | 32/64 | 17.5 | 14.4 | 87.9 |
| full-length JAK1, 20 seeds | 32/64 | 36.9-61.4 | 36.8-43.4 | 69.7-79.2 |

With FERM removed from the input, the model places the kinase domain on the pseudokinase as the
crystal structure does - **7 A on one seed, 17 A on the other** - and its confidence rises by about
10 pLDDT points. With FERM present, at the same depth, it is never closer than 37 A. 4OLI is itself a
JH2-JH1 crystal, so this is the positive control the project has never had: the pipeline **can**
reproduce a measured arrangement when asked only for the part that was measured.

n = 2, so this is a hint, not a result. But it is the cheapest decisive experiment on the list - one
8-seed run of a JH2-JH1 construct, for TYK2 as well as JAK1 - and it tests the question the whole
campaign is really about: **is FERM what the model cannot place, and does its presence degrade the
JH2-JH1 arrangement it would otherwise get right?** If the answer is yes, every closed-state result
in this document is a statement about FERM placement failing, not about the kinase-pseudokinase
interface - and the interface work (sections 26, 28, 29) is on firmer ground than the arrangement
work.

## 46. Retraction: the recycle-cut proposal of section 45 is wrong (2026-10-22)

Section 45 proposed cutting inference from 15 recycles to 6, on the grounds that 89 % of seeds stop
moving by recycle 5, and claimed this would save about 60 % of GPU time while changing the outcome
for roughly one seed in nine. **That is wrong.** It was tested before being acted on, which is the
only good thing to say about it.

Every recycle of every seed is already in the repository, so the test was free: re-score recycles 6,
10 and 12 of all 184 seeds at 64/256 template-free by the arrangement metric and compare the state
assignment against recycle 15.

| compared against recycle 15 | recycle 6 | recycle 10 | recycle 12 |
|---|--:|--:|--:|
| same state assignment | **77.7 %** | 84.2 % | 86.4 % |
| unassigned -> open | 39 | 23 | 14 |
| open -> unassigned | 2 | 6 | 11 |

And the effect sizes the whole variant result rests on:

| open fraction | recycle 6 | recycle 10 | recycle 12 | recycle 15 |
|---|--:|--:|--:|--:|
| wild type | 0.00 | 0.08 | 0.08 | 0.08 |
| **V678F** | **0.33** | 0.50 | 0.54 | **0.75** |
| V678A | 0.38 | 0.50 | 0.56 | 0.62 |
| V678I | 0.12 | 0.31 | 0.38 | 0.50 |

At recycle 6 the significant set after Holm correction is **V678A, V678F, V678D** - a *different*
three from recycle 15's **V678F, V678A, V678I**. The ranking is not stable, so 6 recycles is not even
adequate for ordering the variants, let alone for quoting fractions.

### Why the commitment analysis was misleading

The 39 seeds that become open between recycle 6 and 15 are not borderline cases drifting across a
threshold. At recycle 6 they sit a median of **39.8 A** from the nearest reference; at recycle 15,
**8.4 A**. Recycles 7-15 move them most of the way to the open arrangement.

The JH2-JH1 centroid distance, meanwhile, barely changes over that span - which is exactly what the
commitment analysis measured, and why it reported everything settled by recycle 5. **The domains stay
the same distance apart while the kinase keeps rotating into place.** Section 45 demonstrated, two
paragraphs before making this proposal, that centroid distance and superposition differ by four
orders of magnitude in sensitivity and that distance says nothing about orientation - and then used
the distance to draw a conclusion about the state assignment. The error was using the coarse proxy to
reason about the sensitive readout, immediately after documenting that they disagree.

### What the data does support

The direction of the disagreements is the informative part. At recycle 6 they are **39 up against 2
down** - systematic, one-way convergence, with structures still travelling towards the open
arrangement. By recycle 12 they are **14 up against 11 down** - balanced, which is what threshold
noise looks like once refinement has finished. So:

- **Refinement continues to about recycle 12.** The 15-recycle setting is justified by the data and
  should not be reduced. There is no cheap compute saving here.
- **Recycles 13-15 are the only plausibly spare ones**, worth at most a 20 % saving, and the 13.6 %
  residual disagreement at recycle 12 is seeds sitting near the 15 A cut, not structures still
  moving. Shaving them would trade a real risk of reclassification for very little.
- **Seeds remain the right place to spend compute**, but the saving has to come from somewhere other
  than recycles.

The section 45 claims that stand are unaffected by this: `openness_A` is the JH2-JH1 distance
(verified against a run's own RESULT payload), superposition is four orders of magnitude more
sensitive than either centroid distance (computed on final-recycle structures), and the JH2-JH1
construct experiment is still the cheapest decisive one available. Only the recycle-cut proposal is
withdrawn.

## 47. The unassigned class is not noise: it contains reproducible arrangements (2026-10-22)

Sections 42 and 44 left 40 % of the family - 370 of 860 structures - classified only as "more than
15 A from all nine references". That is a statement about what they are not. The 118 unassigned
structures at 64/256 template-free (the depth every mutation conclusion rests on) were therefore
compared against **each other** by the same arrangement metric used against the references, and the
6903-pair distance matrix was clustered by average linkage.

### They cluster

26 % of all pairs are within 15 A of each other, and at a 15 A cut there are only **5 singletons
among 118 structures**. This is not a diffuse cloud.

| cluster | n | internal RMSD median (max) | median FERM-JH1 | 4OLI | AF2 | 8EWY | 7T6F | JPopen |
|---|--:|--:|--:|--:|--:|--:|--:|--:|
| **1** | **54** | **7.5 (19.5)** | **94.6** | 89.4 | 90.5 | 26.6 | 51.9 | **22.7** |
| 3 | 11 | 6.2 (13.9) | 89.5 | 90.1 | 91.5 | 41.9 | 59.7 | 38.3 |
| 4 | 11 | 8.5 (14.2) | 82.3 | 86.1 | 87.5 | 51.2 | 64.1 | 47.9 |
| 13 | 10 | 8.3 (19.7) | 51.3 | 47.6 | 49.6 | 87.1 | 99.6 | 88.7 |
| 12 | 9 | 7.8 (17.1) | 58.2 | 56.6 | 58.5 | 83.7 | 98.7 | 85.0 |
| 10 | 5 | 6.8 (11.8) | 43.8 | **33.1** | 35.1 | 88.1 | 97.3 | 90.2 |

**The dominant cluster is a displaced open state.** Cluster 1 holds 54 structures - 46 % of the
unassigned set - with FERM-JH1 of 94.6 A (range 91.3-96.1), identical extension to the canonical open
class. Its nearest reference is Jeanpierre's open model for **all 54**, at a median of 22.7 A. But
its members are a median of **7.5 A from each other** - three times closer to one another than to the
reference they are nearest. They are not a diffuse shell around the open state; they are a distinct
recurring arrangement displaced from it. It appears in **all ten variants** (V678W 10, WT 8, V678G 7,
V678L 7, V678F 6, P982A 5, V678D 4, V678M 3, V678A 2, V678I 2) across **20 distinct runs**, with
pLDDT 80.3 - indistinguishable from everything else, as section 43 would predict.

**Three compact clusters are not the closed state either.** Clusters 13, 12 and 10 sit at FERM-JH1
43.8-58.2 A - inside the project's "compact < 60 A" bin - yet 33-57 A from 4OLI and AF2 TYK2, with
internal spreads of 6.8-8.3 A. These are the structures that made section 39's claim 2 ("the compact
bin contains no closed structures") true, and they are now resolved into three reproducible
arrangements rather than one undifferentiated bin.

### The 15 A threshold cuts through a continuum

Distance to the nearest reference, all 184 structures at 64/256:

| 0-5 | 5-10 | 10-15 | 15-20 | 20-25 | 25-30 | 30-35 | 35-40 | 40+ |
|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| 25 | 20 | 21 | 20 | 15 | 15 | 9 | 11 | 48 |

**There is no gap at 15 A.** 21 structures fall in 10-15 A and 20 in 15-20 A. The threshold was
inherited from the project's own "conformations within 15 A" column and it separates two halves of a
smooth distribution, not two modes. Every *categorical* statement in sections 41, 42 and 46 -
"V678F is 0.75 canonical open" - therefore depends on where that line is drawn, and should be quoted
with the threshold attached.

### But the comparative result does not depend on the threshold

| cut | WT open | V678F open | Fisher p |
|---|--:|--:|--:|
| 8 A | 1/24 | 12/24 | 7.0e-04 |
| 10 A | 1/24 | 14/24 | 8.9e-05 |
| 12 A | 2/24 | 16/24 | 5.8e-05 |
| **15 A** | **2/24** | **18/24** | **4.6e-06** |
| 18 A | 5/24 | 19/24 | 1.2e-04 |
| 20 A | 6/24 | 20/24 | 1.1e-04 |
| 25 A | 8/24 | 23/24 | 8.5e-06 |
| 30 A | 10/24 | 24/24 | 8.1e-06 |

V678F separates from wild type at **every cut from 8 to 30 A**, p = 7e-4 to 5e-6 across a near
four-fold range. The headline finding of sections 41 and 42 is robust; only the absolute fractions
move. Stated threshold-free: **V678F moves the structure substantially closer to the experimentally
determined open arrangement than wild type does, at every distance scale tested.**

### What this changes

"Unassigned" should stop being used as a residual category. At 64/256 it resolves into one large
displaced-open arrangement (46 %), three compact arrangements that are not the closed state, and a
remainder. The honest description of what shallow MSA does to TYK2 is not "produces nothing" but
**"produces several reproducible arrangements, none of which is a known state"** - and the largest of
them is a near-miss of the open state, 23 A away, found in every variant.

Whether cluster 1 is biologically meaningful or a systematic artefact of the pipeline cannot be
settled from this data. The test is cheap and obvious: it should appear in the JAK1, JAK2 and JAK3
unassigned sets too if it is a pipeline artefact, and its absence there would make it TYK2-specific.
That comparison needs no GPU time and is the next thing to run.
