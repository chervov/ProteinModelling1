# Four JAK2 variants mapped onto JAK1 — and what the JAK1 clustering says about them

`V1110E`, `G571R`, `V578I`, `L805I`. Written 3 November 2026.

Method: global pairwise alignment of JAK2 (O60674, 1,132 aa) against JAK1 (P23458, 1,154 aa),
BLOSUM62, affine gaps — computed fresh in [`align_jak2_to_jak1.py`](align_jak2_to_jak1.py) and
checked against the family position map already in `external_data/` and the earlier
`JAK2-four-variant-alignments.json`. Overall identity **44.8%** (507/1,132).

**`V617F` is carried through every step as a positive control**, because its JAK1 equivalent is
established in the literature. It comes out as **V658F**, which is correct — so the method is
sound where the sequences align well.

---

## 1. The mapping

| JAK2 | → JAK1 | JAK1 wt | equivalent | wt conserved? | JAK1 domain | local identity (±5) | robust? |
|---|--:|:-:|---|:-:|---|--:|:-:|
| **V617F** *(control)* | 658 | V | **V658F** | **yes** | JH2 pseudokinase | **0.64** | **yes** |
| **V578I** | 619 | V | **V619I** | **yes** | JH2 pseudokinase | 0.45 | **yes** |
| **L805I** | 845 | **I** | **I845I** | no | JH2 pseudokinase | 0.55 | **yes** |
| **V1110E** | 1136 | **P** | **P1136E** | no | JH1 kinase | 0.36 | yes |
| **G571R** | **610 or 612** | **G or S** | **G610R / S612R** | ambiguous | JH2 pseudokinase | **0.09** | **no** |

"Robust" means the mapping does not move when the gap penalties change. Tested at five settings
(open/extend −11/−1, −10/−0.5, −12/−2, −8/−2, −14/−1): four of the five positions are identical at
every setting. `G571R` is not.

## 2. The headline result: L805I installs the residue JAK1 already has

**JAK1 carries isoleucine at position 845**, the residue JAK2 L805I introduces. The mapping is
robust and the local alignment is good (0.55 identity, no gaps, `RPSFRAII` against `RPFFRAIM`).

So the JAK2 variant converts the JAK2 residue to the one its closest paralog carries natively at the
same structural position. That is about as direct a tolerance argument as homology can supply: the
substituted state is not hypothetical, it is wild type in a protein that performs the same job.

A practical consequence worth noting: the JAK1 equivalent is `I845I`, a **self-substitution**, so it
has **no scores at all** in the feature files — those 1,154 rows are deliberately blank (README
conventions). This is not missing data; no predictor scores a residue against itself. The homology
argument here has to be made in words, not by borrowing a number.

## 3. G571R has no trustworthy JAK1 equivalent

The two alignments in hand disagree:

| source | JAK1 position | equivalent |
|---|--:|---|
| the repo's earlier `JAK2-four-variant-alignments.json` | **610** | `G610R` (Gly conserved) |
| this alignment (−11/−1) | **612** | `S612R` (Ser, not conserved) |

and gap penalties flip it: −10/−0.5 and −8/−2 give **610**, while −11/−1, −12/−2 and −14/−1 give
**612**. The reason is visible in the sequences — this is the JH2 N-lobe insertion region, where
JAK2 and JAK1 share almost nothing:

```
JAK2  R R E V G D - - - Y G Q L H E T E V L L K
                |                     |   | |
JAK1  L M D Y K D D E G T S E E K K I K V I L K
```

**Local identity 0.09 over an 11-residue window, with a 3-residue gap at the site.** An alignment
can place a gap on either side of an unalignable stretch at nearly equal cost, and that is exactly
what happens.

**And the choice changes the answer**, so this cannot be waved away:

| equivalent | EV1 cluster | rebuilt cluster | AlphaMissense | PolyPhen-2 HumVar |
|---|:-:|:-:|--:|--:|
| `G610R` | 1 | **2** | 0.1418 | **0.955** |
| `S612R` | 1 | **1** | 0.1298 | **0.263** |

One maps to a variant the rebuilt clustering calls GOF-like with PolyPhen-2 0.955; the other to one
it calls benign-like at 0.263. **The honest answer for G571R is that homology to JAK1 is
uninformative here** — not that it maps to either residue. That the repository already contains a
file named `JAK2-G571R-alternative-JAK1-mapping.json` suggests this was found before.

## 4. What the JAK1 clustering says about the equivalents

From the clustering rebuilt yesterday (`JAK1/clustering/`), for the mappings worth reading:

| JAK2 | JAK1 | EV1 | rebuilt | AlphaMissense | ESM-1b | PolyPhen-2 | FoldX | ddG closed/open |
|---|---|:-:|:-:|--:|--:|--:|--:|--:|
| **V617F** *(control)* | V658F | **2** | **2** | 0.4396 | −9.470 | **0.997** | 0.87 | −3.98 / −5.34 |
| **V578I** | V619I | **1** | **2** | 0.3550 | −7.563 | **0.970** | 1.25 | −5.02 / −7.20 |
| **V1110E** | P1136E | 1 | 1 | 0.6898 | −7.531 | 0.246 | 2.17 | −6.94 / −7.28 |
| **L805I** | I845I | — | — | — | — | — | — | — |

Three observations, in order of how much they matter:

**The control lands correctly but not impressively.** `V658F` is in Cluster 2 (the GOF-anchored pole)
in both the paper's clustering and the rebuild. Good — but Cluster 2 holds 65% of all variants, so
membership alone is weak evidence. What is striking is that **AlphaMissense gives V658F only
0.4396 — the 37th percentile among all 21,926 JAK1 substitutions.** The JAK1 equivalent of the most
consequential gain-of-function driver in myeloproliferative disease scores *below the median*. That
is the expected failure mode for pathogenicity predictors trained on loss-of-function: V617F does
not break the protein, it releases an autoinhibitory contact. PolyPhen-2 (0.997) does flag it.

**V578I is a disagreement case.** `V619I` is Cluster 1 in the paper and Cluster 2 in the rebuild —
one of the 2,080 variants that moved. Its features pull in opposite directions (AlphaMissense 0.355
benign-ish, PolyPhen-2 0.970 damaging), which is precisely the intermediate band where the two
clusterings part company (`clustering_jak1_results.md` §4). So the JAK1 equivalent gives **no stable
signal** for V578I. The mapping is trustworthy; the label it points at is not.

**V1110E maps to a proline.** JAK1 has Pro at 1136 where JAK2 has Val, in a region of 0.36 local
identity — the mapping is stable under gap penalties but the residue is not conserved, and
substituting Glu for Pro is a different physical event from substituting it for Val. `P1136E` sits
in Cluster 1 in both clusterings with AlphaMissense 0.69. Treat this as weak, indirect evidence.

## 5. So — what do we get?

| JAK2 variant | what the JAK1 alignment gives |
|---|---|
| **L805I** | **The most useful result.** JAK1 natively carries Ile at the homologous position, so the variant installs a residue a close paralog already uses. Robust mapping, good local alignment. Argues tolerance — and requires no predictor score. |
| **V617F** *(control)* | Maps correctly to V658F, confirming the method. Incidentally exposes that AlphaMissense rates it at the 37th percentile. |
| **V578I** | Mapping is solid (conserved Val → V619I), but the JAK1 variant is one the two clusterings disagree about. Homology transfers the position, not a conclusion. |
| **V1110E** | Mapping stable but the residue is not conserved (Val→Pro). Weak, indirect. |
| **G571R** | **Nothing reliable.** Position is ambiguous between 610 and 612 by gap penalty, local identity 0.09, and the two choices give opposite cluster labels. Homology to JAK1 should not be used for this variant. |

The general point: paralog alignment is only as good as the local alignment quality, and that varies
enormously **within** one protein pair — 0.64 at V617F against 0.09 at G571R, in the same domain of
the same two proteins. A single overall identity figure of 44.8% would have hidden that completely.
Any homology-based argument in this project should carry its local identity and a gap-penalty
robustness check alongside it.

## 6. Caveats

- **Pairwise alignment only.** A profile or structure-based alignment would likely resolve the
  G571R region better than BLOSUM62 with affine gaps; `data/ddg/jak_family_msa.fasta` exists and was
  not used here. A structural superposition of the JH2 domains is the better tool for that site.
- **The JAK1 cluster labels are not clinical truth.** They are the output of an unsupervised
  two-means split (EV1) and of the rebuild, agreeing on only 84.87% of variants. Transferring a
  cluster label across a paralog boundary compounds that uncertainty with the alignment's.
- **Domain boundaries** are UniProt annotations for P23458, used only to say which domain a position
  falls in.
- Reproducible from [`align_jak2_to_jak1.py`](align_jak2_to_jak1.py) and
  [`lookup_jak1_equivalents.py`](lookup_jak1_equivalents.py); tables in
  [`jak2_to_jak1_with_clustering.csv`](jak2_to_jak1_with_clustering.csv).
