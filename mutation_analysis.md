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
