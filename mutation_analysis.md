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
