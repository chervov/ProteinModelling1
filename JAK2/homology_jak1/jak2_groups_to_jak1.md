# 24 JAK2 variants mapped onto JAK1 — two groups, and a test of the JAK1 clustering

**Group 1** — 14 gain-of-function variants previously reported.
**Group 2** — 10 variants identified in the study.
Written 3 November 2026. Built by [`map_jak2_groups_to_jak1.py`](map_jak2_groups_to_jak1.py);
table in [`jak2_groups_to_jak1.csv`](jak2_groups_to_jak1.csv). Method as in
[`jak2_four_variants_to_jak1.md`](jak2_four_variants_to_jak1.md) — pairwise global alignment of
JAK2 (O60674) against JAK1 (P23458), BLOSUM62, affine gaps, 44.8% overall identity.

Because Group 1 is **independently known** to be gain-of-function, it is a test of whether the
JAK1 clustering carries signal that transfers across the paralog boundary. That test is run below
and the answer depends entirely on filtering the mappings first — which is the main lesson here.

---

## 1. Checks before any interpretation

| check | result |
|---|---|
| wild-type residue matches O60674 | **24 / 24** ✓ |
| mapping unanimous across 5 gap-penalty settings | **23 / 24** (only `G571R` fails) |
| **wild type conserved in JAK1** | **12 / 24 — only half** |
| local identity ≥ 0.25 around the site | 19 / 24 |
| gets a JAK1 cluster label | 22 / 24 |

Two variants legitimately get no label, and the reasons are different:

- **`R426X` is a nonsense variant.** `X` is a stop codon, not an amino acid. It maps cleanly to
  JAK1 `R466` (Arg conserved, local identity 0.64) but **no missense predictor and no cluster
  applies to it** — AlphaMissense, BLOSUM62, PolyPhen-2 and the clustering are all defined over
  amino-acid substitutions. A truncation at residue 466 of 1,132 removes the entire JH2 and JH1
  kinase domains; that is a mechanistic statement, not a score.
- **`L805I` → `I845I` is a self-substitution** — JAK1 already carries Ile at the homologous
  position (§4).

**The 12/24 conservation rate is the dominant caveat.** Half of these mappings place a *different*
residue at the JAK1 position, so the "equivalent" variant is a different physical event. `E846D`
maps to JAK1 `K872D` — Asp-for-Lys, not Asp-for-Glu, a charge reversal rather than a conservative
swap. `L611S` maps to `Y652S`. These are positional homologies, not substitution homologies.

## 2. The mapping

| group | JAK2 | → JAK1 | JAK1 wt | equivalent | wt cons. | local id | unanim. | JAK1 domain | **EV1** | **new** |
|---|---|--:|:-:|---|:-:|--:|:-:|---|:-:|:-:|
| 1 | T108A | 101 | **M** | M101A | no | **0.09** | yes | FERM | 1 | 1 |
| 1 | Y317H | 366 | **F** | F366H | no | **0.18** | yes | FERM | 2 | 2 |
| 1 | H345L | 385 | **N** | N385L | no | 0.64 | yes | FERM | 1 | 1 |
| 1 | H608N | 649 | H | H649N | **yes** | 0.55 | yes | JH2 | **2** | **2** |
| 1 | L611S | 652 | **Y** | Y652S | no | 0.73 | yes | JH2 | 1 | 1 |
| 1 | V617I | 658 | V | V658I | **yes** | 0.64 | yes | JH2 | **2** | **2** |
| 1 | **V617F** | 658 | V | **V658F** | **yes** | 0.64 | yes | JH2 | **2** | **2** |
| 1 | V625F | 666 | V | V666F | **yes** | 0.64 | yes | JH2 | **2** | **2** |
| 1 | E846D | 872 | **K** | K872D | no | 0.64 | yes | linker | 2 | 2 |
| 1 | R867Q | 893 | R | R893Q | **yes** | 0.64 | yes | JH1 | **2** | 1 |
| 1 | T875N | 901 | T | T901N | **yes** | 0.73 | yes | JH1 | **2** | **2** |
| 1 | S755R | 795 | **K** | K795R | no | 0.27 | yes | JH2 | 2 | 2 |
| 1 | R938Q | 965 | **K** | K965Q | no | 0.64 | yes | JH1 | 2 | 2 |
| 1 | R1063H | 1090 | **K** | K1090H | no | 0.45 | yes | JH1 | 1 | 1 |
| 2 | P37A | 34 | P | P34A | **yes** | **0.18** | yes | FERM | 1 | 1 |
| 2 | F240V | 251 | F | F251V | **yes** | **0.18** | yes | FERM | 2 | 2 |
| 2 | H380Y | 420 | H | H420Y | **yes** | **0.91** | yes | FERM | **2** | **2** |
| 2 | **R426X** | 466 | R | **R466X** | yes | 0.64 | yes | SH2-like | **—** | **—** |
| 2 | C427R | 467 | **W** | W467R | no | 0.64 | yes | SH2-like | 2 | 2 |
| 2 | **G571R** | **610/612** | G or S | G610R / S612R | ambig. | **0.09** | **no** | JH2 | 1 / 1 | **2 / 1** |
| 2 | V578I | 619 | V | V619I | **yes** | 0.45 | yes | JH2 | 1 | **2** |
| 2 | **L805I** | 845 | **I** | **I845I** | no | 0.55 | yes | JH2 | **—** | **—** |
| 2 | I1065T | 1092 | I | I1092T | **yes** | 0.36 | yes | JH1 | 1 | **2** |
| 2 | V1110E | 1136 | **P** | P1136E | no | 0.36 | yes | JH1 | 1 | 1 |

`EV1` is the paper's cluster label for the JAK1 equivalent, `new` the rebuild in
`JAK1/clustering/`. **Cluster 1 = the gnomAD-common pole, Cluster 2 = the reported-GOF pole.**

### 2.1 Group 2 on its own — the study's variants, in the order given

| JAK2 | → JAK1 | JAK1 wt | equivalent | wt cons. | local id | unanim. | domain | **EV1** | **new** | AlphaMiss. | ESM-1b | PolyPhen-2 | SIFT | CADD | ClinPred | BLOSUM62 | FoldX | mapping |
|---|--:|:-:|---|:-:|--:|:-:|---|:-:|:-:|--:|--:|--:|--:|--:|--:|--:|--:|---|
| **P37A** | 34 | P | P34A | yes | **0.18** | yes | FERM | 1 | 1 | **0.058** | −3.00 | **0.007** | 0.080 | **6.8** | **0.093** | −1 | — | weak alignment |
| **F240V** | 251 | F | F251V | yes | **0.18** | yes | FERM | **2** | **2** | **0.993** | −10.22 | 0.996 | 0.003 | 27.6 | 0.992 | −1 | 3.71 | weak alignment (4 gaps) |
| **H380Y** | 420 | H | H420Y | **yes** | **0.91** | yes | FERM | **2** | **2** | 0.830 | −9.17 | 0.982 | 0.003 | 27.5 | 0.985 | +2 | −0.20 | **best in the set** |
| **R426X** | 466 | R | **R466X** | yes | 0.64 | yes | SH2-like | **—** | **—** | — | — | — | — | — | — | — | — | **nonsense — see §1** |
| **C427R** | 467 | **W** | W467R | **no** | 0.64 | yes | SH2-like | **2** | **2** | **0.996** | −7.54 | **1.000** | 0.069 | **30.0** | 0.990 | −3 | 4.11 | position only |
| **G571R** | **610/612** | G or S | G610R / S612R | ambig. | **0.09** | **no** | JH2 | 1 / 1 | **2 / 1** | 0.130 | −3.29 | 0.263 | — | — | — | −1 | 1.36 | **unusable** |
| **V578I** | 619 | V | V619I | **yes** | 0.45 | yes | JH2 | 1 | **2** | 0.355 | −7.56 | 0.970 | — | — | — | **+3** | 1.25 | good |
| **L805I** | 845 | **I** | **I845I** | no | 0.55 | yes | JH2 | **—** | **—** | — | — | — | — | — | — | — | — | **self-substitution** |
| **I1065T** | 1092 | I | I1092T | **yes** | 0.36 | yes | JH1 | 1 | **2** | **0.204** | −7.22 | 0.861 | **0.001** | **33.0** | 0.974 | −1 | 2.87 | moderate |
| **V1110E** | 1136 | **P** | P1136E | no | 0.36 | yes | JH1 | 1 | 1 | 0.690 | −7.53 | **0.246** | — | — | — | −1 | 2.17 | position only |

Blank cells are genuinely absent, not zero: SIFT, CADD and ClinPred exist only for substitutions
reachable by a single nucleotide change (the 31.3% dbNSFP ceiling), and `R426X` / `L805I` have no
missense scores at all for the reasons in §1.

Reading down the "mapping" column first, before any score:

- **`H380Y` is the one Group-2 variant with a genuinely reliable mapping** — 0.91 local identity,
  wild type conserved, unanimous. Cluster 2 in both clusterings and every predictor agrees it is
  damaging. If any Group-2 result should be trusted, it is this one.
- **`P37A` is consistently benign across independent predictors** — AlphaMissense 0.058,
  PolyPhen-2 0.007, CADD **6.8** (unusually low; the JAK1 median is 24.8), ClinPred 0.093. Cluster 1
  in both. The caveat is the 0.18 local identity, so the *mapping* is weak even though the scores
  are unanimous.
- **`C427R` and `V1110E` map to a different residue** (Trp and Pro respectively). Both are
  positional homologies only, and for `C427R` this matters mechanistically — losing a cysteine may
  break a disulphide or a structural contact, which substituting into a tryptophan position does
  not model at all.
- **`I1065T` is where AlphaMissense disagrees with everything else**: 0.204 (benign-looking) against
  SIFT 0.001, CADD **33.0** (top ~0.05% of all human SNVs), ClinPred 0.974, PolyPhen-2 0.861. It
  also moves from Cluster 1 to Cluster 2 between the two clusterings. Worth a second look.
- **`F240V`** scores strongly damaging on everything, but sits in a window with 0.18 identity and
  four gaps — so the JAK1 label supports it only weakly.
- **`V578I`** has BLOSUM62 **+3**, the most conservative substitution in the group, yet PolyPhen-2
  0.970; and it is a clustering disagreement case.
- **`G571R`** remains unusable from JAK1 homology (§5).

Three of the ten (`R426X`, `L805I`, `G571R`) cannot be argued from the JAK1 clustering at all, and
four more (`P37A`, `F240V`, `C427R`, `V1110E`) rest on mappings I would not lean on. That leaves
**`H380Y`, `V578I` and `I1065T`** as the ones where this analysis contributes something — and of
those, two are clustering disagreement cases.

## 3. Does the JAK1 clustering recognise the known GOF variants?

**On all mapped variants, no.** Cluster 2 holds 61.7% of JAK1 substitutions in the rebuild and
65.5% in EV1, so that is the base rate to beat:

| clustering | Group 1 (known GOF) | vs base rate | Group 2 |
|---|---|--:|---|
| EV1 | 10/14 in Cluster 2 (71.4%) | **p = 0.44** | 3/8 (37.5%) |
| new | 9/14 in Cluster 2 (64.3%) | **p = 0.54** | 5/8 (62.5%) |

71.4% against a 65.5% base rate is nothing. Taken at face value this says the clustering has no
transferable signal.

**But that pools trustworthy and untrustworthy mappings.** Restricting to mappings that pass all
three filters — wild type conserved, local identity ≥ 0.25, unanimous across gap settings — leaves
6 Group-1 and 3 Group-2 variants, and the picture inverts:

| clustering | Group 1, filtered | | Group 2, filtered |
|---|---|--:|---|
| **EV1** | **6/6 in Cluster 2 (100%)** | **p = 0.079** | 1/3 |
| new | 5/6 (83%) | p = 0.26 | 3/3 |

**All six well-mapped known GOF variants land in the paper's Cluster 2** — `H649N`, `V658I`,
`V658F`, `V666F`, `R893Q`, `T901N`. Six out of six is the maximum the data can give at n = 6, and
p = 0.079 is as low as a one-sided binomial against a 65.5% base rate can go with six trials. It
is not significant at 0.05, and n = 6 cannot make it so; but the point estimate is 100% rather than
marginally above chance, which is a different situation from the unfiltered result.

**The honest reading: the unfiltered negative result is an artefact of bad mappings, not evidence
that the clustering fails.** The four Group-1 variants in Cluster 1 are `M101A` (local identity
0.09), `N385L` (non-conserved), `Y652S` (non-conserved) and `K1090H` (non-conserved) — every one
excluded by the filters. The rebuild moves `R893Q` to Cluster 1, which is why it scores 5/6 rather
than 6/6; that is one of the 2,080 variants the two clusterings disagree about.

This is suggestive, not established. Six variants is a small test, and the filters were chosen
after seeing that half the mappings were non-conserved — so this is a post-hoc subgroup, and it
should be confirmed on variants not used to motivate the filter before it is relied on.

## 4. AlphaMissense fails on these variants, systematically

The clearest result in this analysis, and it does not depend on the clustering:

| | |
|---|--:|
| median AlphaMissense, the 14 known GOF equivalents | **0.332** |
| median AlphaMissense, all 21,926 JAK1 substitutions | **0.684** |
| known GOF variants **below AlphaMissense's own 0.34 benign cutoff** | **7 / 14 (50%)** |

**The known gain-of-function variants score as a group *below* the typical JAK1 substitution.**
Individually:

| JAK2 | JAK1 | AlphaMissense | percentile | PolyPhen-2 |
|---|---|--:|--:|--:|
| S755R | K795R | **0.0837** | **4.4%** | 0.996 |
| T108A | M101A | **0.1064** | **8.0%** | 0.006 |
| L611S | Y652S | 0.1802 | 18.1% | 0.150 |
| V617I | V658I | **0.1951** | **19.6%** | 0.938 |
| R1063H | K1090H | 0.2042 | 20.6% | 0.990 |
| R867Q | R893Q | **0.2208** | **22.1%** | 0.999 |
| H345L | N385L | 0.2278 | 22.8% | 0.076 |
| H608N | H649N | 0.4354 | 37.1% | 1.000 |
| **V617F** | **V658F** | **0.4396** | **37.3%** | 0.997 |
| T875N | T901N | 0.7125 | 51.5% | 1.000 |
| R938Q | K965Q | 0.8197 | 57.5% | 1.000 |
| E846D | K872D | 0.8980 | 63.4% | 0.965 |
| Y317H | F366H | 0.9705 | 74.4% | 1.000 |
| V625F | V666F | 0.9858 | 80.1% | 0.999 |

**PolyPhen-2 does far better**: median 0.996, and 11 of 14 above 0.93. Its three low calls —
`M101A` (0.006), `N385L` (0.076), `Y652S` (0.150) — are precisely three of the untrustworthy
mappings from §1. So PolyPhen-2's apparent failures coincide with bad homology rather than with
PolyPhen-2 missing the biology.

This is the expected failure mode and the project has seen it before: **AlphaMissense is calibrated
on loss of function.** A gain-of-function variant that releases an autoinhibitory contact does not
look like protein damage, and `V617F` — the single most consequential variant in this family — sits
at the 37th percentile. Any screen for activating variants built on AlphaMissense alone will miss
roughly half of them.

Consistent with that, **FoldX finds Group 1 *less* destabilising than Group 2** (median 0.537
against 2.171 kcal/mol, Mann–Whitney p = 0.067). Known activating variants are not the
destabilising ones. Group 1 and Group 2 are otherwise indistinguishable on AlphaMissense
(p = 0.73), ESM-1b (p = 0.92) and PolyPhen-2 (p = 0.24).

## 5. Per-variant notes worth carrying forward

- **`V617F` → `V658F`** is the literature-established equivalence and comes out correct, which is
  the control for the whole method.
- **`V617I` → `V658I`** maps equally well. AlphaMissense 0.195 and BLOSUM62 **+3** (a conservative
  swap) — it looks benign on sequence grounds yet is a reported GOF variant. Cluster 2 in both
  clusterings; PolyPhen-2 0.938.
- **`L805I` → `I845I`**: JAK1 natively carries the residue the variant introduces. The strongest
  tolerance argument available from homology, and it needs no score.
- **`R426X`**: maps to a conserved Arg but is a truncation. Treat mechanistically — it removes JH2
  and JH1 entirely — not with missense predictors.
- **`G571R`**: still the one unstable mapping, 610 or 612 by gap penalty, local identity 0.09, and
  the two choices give different rebuilt labels. `G610R` has the conserved Gly and is the
  better-supported of the two, but the variant should not be argued from JAK1 homology.
- **`H380Y` → `H420Y`** has the best local alignment in the set (0.91) with the wild type conserved,
  so it is the most reliable Group-2 mapping — Cluster 2 in both clusterings, AlphaMissense 0.830,
  PolyPhen-2 0.982.
- **`T108A` → `M101A`**: local identity 0.09 and Met where JAK2 has Thr. The weakest mapping in the
  set. Its benign-looking scores should not be read as evidence about T108A.

## 6. Caveats

- **Half the mappings do not conserve the wild type** (§1), and five sit in regions of < 0.25 local
  identity. A JAK1 position is not a JAK1 equivalent.
- **The filtered GOF test is post-hoc** and rests on 6 variants (§3). It is a reason to take the
  clustering seriously, not a validation of it.
- **Pairwise alignment only.** `data/ddg/jak_family_msa.fasta` exists; a profile or structure-based
  alignment would likely improve the FERM-domain and JH2-insertion mappings, which is where the
  failures are concentrated.
- **Cluster labels are not clinical truth** — two unsupervised partitions agreeing on 84.87% of
  variants. Transferring one across a paralog boundary compounds both uncertainties.
- **Group 2 is not a negative control.** These are variants found in the study; their true effects
  are not established, so nothing here should be read as showing they are benign.
