# Two new methodological steps for conformational prediction in the JAK family

*23 October 2026 — TYK2, JAK1, JAK2, JAK3 · 348 wild-type structure predictions*

---

## 1. The result in one page

The published pipeline (Jeanpierre, Debeaupuis et al., *EMBO Mol Med* 2025) runs structure
prediction **one way**: deep MSA, no template. We added two controls — **use a template** and
**vary MSA depth** — and both unlock conformations the single setting cannot reach.

| Protein | Default-style run<br>(deep MSA, no template) | What **templates** add | What **varying MSA depth** adds | Conformations<br>reachable |
|---|---|---|---|:---:|
| **TYK2** | **open only — 26 / 26 runs** | **closed: 24 / 24** | open appears only at 96+ | **1 → 2** |
| **JAK3** | one state per depth | not tested | **closed** at 128 (7/16), **open** at 256 (15/16), **new form** (9/16) | **1 → 3** |
| **JAK1** | open 23, closed 6 (of 35) | not tested | **active-dimer** only at 64 (4/5) — invisible at deep MSA | **2 → 3** |
| **JAK2** | closed 33 / 47 | closed (confirms) — 35/35 | never opens — 0 / 128 runs | **1 → 1** *(AF3 reaches open; our pipeline does not)* |

### Conclusions

> **1. The closed form of TYK2 is unreachable without a template.**
> **0 of 89** template-free runs produced it, at any MSA depth. **24 of 24** runs given the closed
> 4OLI template did. The autoinhibited state — the drug target — is invisible to the standard method.

> **2. MSA depth is a conformational dial, and the switch is sharp.**
> TYK2 goes from **8% open at 64 sequences to 96% open at 96 sequences**. States live in narrow
> windows: JAK1's active-dimer exists at 64 and is gone by 128.

> **3. Varying depth reveals forms no single setting shows — including a candidate new JAK3 form.**
> JAK3 yields closed (128), open (256) and an **unmatched conformation in 9 of 16 runs at 128**.

> **4. JAK2's open state exists — our pipeline just cannot reach it.**
> AlphaFold 3 returns **open JAK2 in 5/5 models with templates and 5/5 without** (2.3–7.2 Å from the
> Jeanpierre open reference). Our pipeline returns **0 open in 128 template-free runs** and 0 in 35
> template runs. The template is not the discriminating variable — the **model** is.

> **Honest limit: MSA depth alone never opened JAK2** — 0 of 128 template-free runs. It took the
> third control to get there, and TYK2's closed state still needs a specified template.

---

## 2. What the two controls are

**Template control.** AlphaFold can be given an experimental structure as a starting point, or
denied one. The published pipeline does not vary this. We ran both, and a third mode
("template + release") in which template recycles are followed by unrestrained recycles, to test
whether the model would leave the template basin.

**Template *source* is worth distinguishing but is not what decides JAK2.** Our campaign always
*specified* the template (`pdb:4OLI:A`, the closed TYK2 crystal); AlphaFold 3's server offers
`useStructureTemplate: True`, which searches the PDB itself. On JAK2 both AF3 modes — template and
no-template — return open, so the template is not the operative difference (section 4).

**MSA depth control.** AlphaFold's input is a multiple sequence alignment of evolutionary
relatives. Depth is written here as `clusters/extra_sequences`, from 32/64 up to 512/8192. The
published pipeline uses full depth. Subsampling the MSA is an established way to expose
alternative conformations; what is new here is using it **systematically across a protein family,
jointly with the template switch**, and scoring every structure against the same reference panel.

**Scoring.** Each prediction is superposed on the pseudokinase domain (JH2) of each reference and
the kinase domain (JH1) Cα RMSD is measured. A structure is assigned to the nearest reference
within **15 Å**; beyond that it is reported as **unmatched**. References: 4OLI (TYK2 closed,
X-ray), AF2 models, 8EWY and 7T6F (JAK1, cryo-EM), and the Jeanpierre open/closed JAK1 models.
Compactness (FERM–JH1 centroid distance) is tracked separately — it is a **different axis**, and
the two disagree often enough that compactness must not be used as a proxy for the closed state.

---

## 3. The TYK2 result in full

TYK2 is the cleanest case because the two controls separate perfectly.

| Mode | MSA depth | n | closed | open | unmatched | median FERM–JH1 |
|---|---|--:|--:|--:|--:|--:|
| template-free | 32/64 | 15 | 0 | 0 | **15** | 45.1 Å |
| template-free | 64/256 | 24 | 0 | 2 | **22** | 91.0 Å |
| template-free | 96/384 | 24 | 0 | **23** | 1 | 93.6 Å |
| template-free | 128/512 | 8 | 0 | **8** | 0 | 93.5 Å |
| template-free | 256/1024 | 9 | 0 | **9** | 0 | 93.2 Å |
| template-free | 512/8192 | 9 | 0 | **9** | 0 | 93.3 Å |
| **template** | 128/512 | 16 | **16** | 0 | 0 | 39.2 Å |
| **template + release** | 128/512 | 8 | **8** | 0 | 0 | 39.0 Å |

Two things to read off this table.

**The template is the only route to closed.** Summed over all template-free settings: **0 closed in
89 runs**. With a template: **24 of 24**. No MSA depth substitutes for it.

**The open transition is sharp and sits between 64 and 96 clusters.** 8% open at 64/256, 96% at
96/384. A pipeline sampling only full depth sees one side of this switch and never knows the
switch exists.

**Release recycles change nothing** (39.0 Å vs 39.2 Å). Once the model is in the template basin it
stays there, so "template + release" cannot be used as an independent conformational assay. This
is a negative result about our own method and is reported as such.

---

## 4. The rest of the family

| Protein | Mode | MSA depth | n | closed | open | dimer | unmatched |
|---|---|---|--:|--:|--:|--:|--:|
| JAK1 | free | 32/64 | 17 | 2 | 0 | 0 | 15 |
| JAK1 | free | 64/256 | 5 | 0 | 0 | **4** | 1 |
| JAK1 | free | 96/384 | 5 | 0 | 0 | 2 | 3 |
| JAK1 | free | 128/512 | 20 | 6 | 8 | 1 | 5 |
| JAK1 | free | 160/640 → 512/8192 | 15 | 0 | **15** | 0 | 0 |
| JAK2 | free | 32/64 → 128/512 | 56 | 1 | **0** | 0 | 55 |
| JAK2 | free | 256/1024 → 512/8192 | 32 | **32** | **0** | 0 | 0 |
| JAK2 | template / release | all | 35 | **35** | 0 | 0 | 0 |
| JAK3 | free | 128/512 | 16 | 7 | 0 | 0 | **9** |
| JAK3 | free | 256/1024 | 16 | 1 | **15** | 0 | 0 |
| JAK3 | free | 512/8192 | 8 | 0 | **8** | 0 | 0 |

**JAK1 — a state that exists only in a narrow window.** The active-dimer arrangement (matching
7T6F) appears in 4 of 5 runs at 64/256 and in 1 of 20 at 128/512. At 160+ it is gone entirely. A
single deep-MSA setting would never show it.

**JAK3 — three forms from one protein.** Closed at 128/512 (7/16), open at 256/1024 (15/16), and
**9 of 16 runs at 128/512 matching no reference**. This is the most interesting candidate in the
set, because it occurs at *moderate* depth where the model is otherwise confident (pLDDT 84),
rather than at shallow depth where non-convergence explains everything.

**JAK2 — our pipeline cannot reach its open state; AlphaFold 3 reaches it trivially.** No setting
of ours opens JAK2: 0 open in 128 template-free runs, 0 in 35 template runs. AlphaFold 3 opens it
in every model, with or without templates:

| AF3 run | templates | models open | JH1 RMSD to JP-open | to JP-closed | FERM–JH1 |
|---|---|--:|--:|--:|--:|
| `JAK2/af3_template/` | `useStructureTemplate: True` | **5 / 5** | 2.7 Å | 82.8 Å | 94.4–94.9 Å |
| `JAK2/af3_notemplate/` | **False** | **5 / 5** | 2.3–7.2 Å | 82.4–84.7 Å | 93.8–94.6 Å |

All well inside the 15 Å assignment threshold, verified on the **arrangement** axis specifically —
JAK2 elsewhere sits closed-by-arrangement yet extended-by-distance, the exact trap that makes
compactness an unsafe proxy.

**The 2×2 isolates the cause:**

| | our pipeline (OpenFold / AF2-based) | AlphaFold 3 |
|---|--:|--:|
| no template | **0 / 128 open** | **5 / 5 open** |
| with template | 0 / 35 open (closed 4OLI supplied) | 5 / 5 open (auto) |

Templates change nothing *within* either tool. The difference is the **model version**. A closed
template explains why our template runs stay closed, but not why 128 template-free runs never
opened — AF3 opens JAK2 from no template at all.

**This corrects two earlier claims in this document.** An earlier version said templates give closed
in 59/59 runs and JAK2 "never opens". The first holds only for *specified closed* templates. The
second is true of our pipeline but false of JAK2 as a protein. A further intermediate version
attributed the difference to template *source*; the no-template AF3 run rules that out.

**What it means for the method.** This is a limitation of our pipeline, not a discovery about JAK2 —
and it bounds the claim in section 1: MSA-depth subsampling is a real conformational control, but
it cannot manufacture a state the underlying model will not produce. Confidence on the AF3 models
is modest (pTM 0.76), so an experimental structure or a third method would be needed to decide
which tool is right.

## 5. How to read "unmatched"

126 of 348 wild-type structures (36%) matched no reference within 15 Å. These are **not** all
discoveries:

- At **shallow depth** (32–64) they dominate — TYK2 15/15, JAK2 20/20 — and pLDDT is lowest there
  (TYK2 76.8 vs 82.5 at full depth). This is the model failing to converge, and should be read as
  *unresolved*, not *novel*.
- At **moderate depth with high confidence** — the JAK3 128/512 case — the same label means
  something different and is worth following up experimentally.

The distinction matters, and conflating the two would overstate the result. Throughout this
project the conservative reading is used.

---

## 6. Caveats

1. **JAK2 did not open.** The approach is not universal.
2. **Templates were tested on TYK2 and JAK2 only.** JAK1 and JAK3 template runs were not done, so
   their "1 → 3" gains come from MSA depth alone and the template column is blank, not negative.
3. **"New form" means unmatched against a five-structure reference panel.** A larger panel might
   assign some of them.
4. **The 15 Å assignment threshold is a choice.** It was fixed before these comparisons and not
   tuned afterwards, but a different threshold would move counts at the margin.
5. **Run counts are uneven** (8–47 per cell) because the campaign grew incrementally; cells with
   n < 10 should be read as indicative.
6. **Compactness is not conformation.** JAK2 at 256/1024 is closed by arrangement yet extended by
   FERM–JH1 distance (94.8 Å) — the two axes genuinely come apart.

---

*Underlying per-structure data: `wt_simulation_summary.json`. Methods and the full campaign
history: `mutation_analysis.md`.*
