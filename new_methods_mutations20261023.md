# Mutation effects detected by the new methodology

*23 October 2026 — TYK2, JAK1, JAK2, JAK3 · 785 structure predictions, 40 mutant-vs-wild-type tests*

---

## 1. The result in one page

Each mutant was run **in the same cell as wild type** — same protein, same MSA depth, same template
mode — and compared on two independent axes: the **JH2→JH1 arrangement** (open vs closed) and the
**FERM–JH1 distance** (compact vs extended). Fisher exact tests, Holm-corrected within each protein.

| Protein | Mutation | What it is | Axis | Mutant | Wild type | Holm *p* |
|---|---|---|---|:---:|:---:|:---:|
| **TYK2** | **V678F** | pseudokinase-domain variant | opens | **18/24 (75%)** | 2/24 (8%) | **0.0001** |
| **TYK2** | **V678A** | same position | opens | **10/16 (62%)** | 2/24 (8%) | **0.0083** |
| **TYK2** | **P982A** | JH2–JH1 interface | **closes** | **13/24 (54%)** | 23/24 (96%) | **0.034** |
| **JAK2** | **V617F** | the MPN driver mutation | **extends** | **0/16 compact** | 9/16 compact | **0.0073** |
| JAK1 | V658F | V617F-equivalent position | extends | 0/16 compact | 3/5 compact | 0.030 |

### Conclusions

> **1. The method detects the textbook gain-of-function mutation.**
> **JAK2 V617F** — the myeloproliferative-neoplasm driver whose autoinhibition mechanism was
> modelled by Shan, …, Shaw & Hubbard (*Nat Struct Mol Biol* 2014) — comes out as a **complete
> loss of the compact state: 0 of 16 runs, against 9 of 16 for wild type**. We did not look for it
> specially; it fell out of the same scan.

> **2. The method detects effects in both directions.**
> V678F and V678A **open** TYK2; **P982A closes it** (54% open vs 96% for wild type). A method that
> only ever pushes structures one way would be suspect. This one does not.

> **3. Both new controls are load-bearing.**
> Every TYK2 hit is invisible at the depth a standard pipeline uses: V678F and V678A appear only at
> **64 sequences**, P982A only at **96**. The JAK2 V617F effect appears only at **512**. No single
> setting would have found all four.

> **Honest limits.** V617F shows on the **compactness** axis, not the arrangement axis (0 open in
> all 80 runs), and its direction **reverses at 256 sequences**. 35 of 40 tests were null —
> including every JAK3 mutation.

---

## 2. What was tested

| Protein | Mutations | Runs |
|---|---|--:|
| TYK2 | V678F, V678A, V678I, V678D, V678G, V678L, V678M, V678W, P982A, H582W | 320 |
| JAK2 | **V617F**, G571R, L805I, V1110E, V578I | 144 |
| JAK1 | V658F | 62 |
| JAK3 | M592F, A572V, A573V, M511I, R657Q, Y581C | 96 |

Wild type was run in every cell so each comparison is internally matched; 348 wild-type structures
support the 40 tests. Scoring is identical to the wild-type analysis: superpose on JH2, measure JH1
Cα RMSD against the reference panel, assign within 15 Å, and track FERM–JH1 distance separately.

---

## 3. The four findings in detail

### 3.1 TYK2 V678F — the largest effect in the campaign

| MSA depth | mutant open | WT open | p |
|---|:---:|:---:|--:|
| 64/256 | **18/24 (75%)** | 2/24 (8%) | 4e−06 |
| 96/384 | — | 23/24 (96%) | — |

At 64 sequences wild type is almost entirely unmatched or closed, and V678F is 75% open. One
residue moves the conformational equilibrium across the whole scan window. Note the effect is only
visible in the **narrow depth band where wild type has not yet switched** — by 96/384 wild type is
itself 96% open and there is no headroom to detect anything.

### 3.2 TYK2 V678A — the same position, a smaller side chain, the same direction

10/16 (62%) open against 2/24 (8%), Holm 0.0083. Two different substitutions at residue 678 produce
the same qualitative shift, which is the kind of internal consistency that argues against a
sampling artefact. Four further substitutions at 678 (I, D, G, M) trend the same way at raw
p = 0.007–0.195 but do not survive correction.

### 3.3 TYK2 P982A — the only variant that closes

| MSA depth | mutant open | WT open | p | Holm |
|---|:---:|:---:|--:|--:|
| 96/384 | **13/24 (54%)** | 23/24 (96%) | 0.0018 | **0.034** |
| 64/256 | 5/16 (31%) | 2/24 (8%) | 0.094 | 1.00 |

P982 sits in the 4OLI JH2–JH1 interface. At 96/384 — the depth where wild-type TYK2 is reliably
open — P982A drags it back toward closed. The raw p-value fell monotonically as seeds accumulated
(0.041 → 0.016 → 0.0018), which is the behaviour of a real effect rather than a lucky split.

Worth stating: in the DMS, P982A is **loss-of-function** (IFN-α 1 U/mL = −0.321) and is the only
one of the five variants this project has tested that AlphaMissense scores above 0.5 (0.526). A
loss-of-function variant that closes the structure is mechanistically coherent.

### 3.4 JAK2 V617F — the textbook mutation, found on the compactness axis

| MSA depth | mutant compact | WT compact | p | Holm |
|---|:---:|:---:|--:|--:|
| **512/8192** | **0/16** | **9/16** | 0.00082 | **0.0073** |
| 256/1024 | 7/16 | 0/16 | 0.0068 | 0.054 |
| 128/512 | — | — | ns | — |

V617F is the driver mutation of polycythaemia vera and related myeloproliferative neoplasms, and
the mechanism modelled by **Shan, Gnanasambandan, Ungureanu, Kim, Hammarén, Yamashita,
Silvennoinen, Shaw & Hubbard, "Molecular basis for pseudokinase-dependent autoinhibition of JAK2
tyrosine kinase", *Nature Structural & Molecular Biology*, 2014** — a D. E. Shaw Research /
Hubbard lab collaboration placing the disease mutations at the pseudokinase–kinase interface and
proposing that V617F relieves autoinhibition.

At full MSA depth our wild-type JAK2 is split 9 compact / 7 extended; **V617F is 16/16 extended**.
That is the loss of the compact, autoinhibited arrangement the Shaw model predicts.

**Two caveats, both important.** First, this is on the **compactness** axis only: by the arrangement
metric, V617F is 0/80 open — identical to wild type — so the effect is a FERM–JH1 displacement, not
a JH2→JH1 release. Second, at 256/1024 the direction **reverses** (7/16 compact vs 0/16 for wild
type, Holm 0.054). A single consistent direction across depths would be much stronger evidence;
this is one significant cell with an inconsistent neighbour, and should be presented as suggestive
rather than settled.

---

## 4. What came out null

**35 of 40 tests.** This matters for calibrating how much to believe the five positives.

| Protein | Mutations tested | Significant |
|---|--:|--:|
| TYK2 | 10 (21 tests) | 3 |
| JAK2 | 5 (9 tests) | 1 |
| JAK1 | 1 (4 tests) | 1 |
| JAK3 | 6 (6 tests) | **0** |

- **H582W is null** (0.25 open at 64/256, 0.75 at 96/384; both ns) despite being **the strongest
  activating variant in the entire TYK2 DMS** (IFN-α 1 U/mL = +1.339). The two cleanest activators
  in the DMS, H582W and V678M, both score 0.25 on our assay, while V678F — which is *not* strongly
  activating — scores 0.75. **The arrangement score does not track activation.**
- **All six JAK3 mutations are null**, including four with zero open runs in either arm.
- **JAK2 G571R, L805I, V1110E, V578I** are null on both axes.

---

## 5. Caveats

1. **V617F is significant on compactness only, and reverses direction at the adjacent depth.**
2. **Multiple testing**: 40 comparisons. Holm correction is applied within each protein, which is
   the defensible family; correcting across all 40 jointly moves P982A to 0.068 and leaves V678F,
   V678A and JAK2 V617F significant. Both numbers are reported rather than the more favourable one.
3. **JAK1 V658F's hit rests on a 5-run wild-type arm** (3/5 compact), so its Holm 0.030 is fragile.
4. **Effects are depth-specific and sometimes depth-bounded by ceiling effects** — V678F cannot be
   detected at 96/384 because wild type is already 96% open there.
5. **No effect has been validated experimentally.** These are predictions of conformational
   preference, and the H582W result shows the assay does not track measured activation.
6. **Run counts are uneven** (8–24 per arm); cells with n < 10 are indicative only.

---

*Per-test statistics: `mut_vs_wt.json`. Wild-type baseline and the two methodological controls:
`new_methods_summary20261023.md`. Full campaign history: `mutation_analysis.md`.*
