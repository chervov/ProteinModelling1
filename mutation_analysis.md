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
