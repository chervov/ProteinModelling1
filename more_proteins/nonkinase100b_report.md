# Non-kinase human proteins, batch 2 — inter-domain centroid variation

The next 100 proteins from the same screen (ranks 51–150 by distinct multi-domain parent template
count), disjoint from the first 50. All 100 returned data: **4,885 observations**, no failures.
Templates are collapsed to **distinct PDB entries** from the outset in this batch — the chain-suffix
fix identified after batch 1, so `6gfe.1.A` and `6gfe.1.B` count once, not twice.

**436 domain pairs across 78 proteins** have two or more distinct entries; 76 exceed 15 Å of spread
and 48 exceed 20 Å. AlphaFold falls outside the experimental range in **85 of 414 pairs (21%)**.

## The integrin result reproduces across paralogues

ITGB1 and ITGB2 independently recover the bent-to-extended switch found for ITGB3 in batch 1, with
near-identical numbers over **5 distinct PDB entries each**:

| protein | VWFA ↔ I-EGF-4 | entries | AlphaFold |
|---|---|--:|--:|
| ITGB3 (batch 1) | 32.5–142.5 Å | 12 | 36.6 Å (bent) |
| ITGB1 | 37.8–142.4 Å | 5 | 107.7 Å (extended) |
| ITGB2 | 39.3–142.3 Å | 5 | 41.2 Å (bent) |

Three β subunits converging on ~40 Å bent and ~142 Å extended, from separate template sets, is the
strongest family replicate in the project. Note that AlphaFold picks **different states for
different paralogues** — extended for ITGB1, bent for ITGB2 and ITGB3 — the same arbitrariness seen
earlier when AlphaFold flipped JAK2 between orthologues above 90% identity.

## ABC transporters: the transport cycle, heavily sampled

The nucleotide-binding domains separate and re-dimerise through the catalytic cycle, and that is
visible with more sampling than almost anything else measured here: **CFTR** NBD1-to-NBD2 spans
26.4–69.6 Å over **21 entries**, **ABCB1** (P-glycoprotein) 25.8–61.9 Å over **23**, and **ABCC2**
over 17. AlphaFold sits at the closed/separated end in each (CFTR 29.8 Å, ABCB1 44.1 Å) and inside
the range, so here it is not wrong — just not informative about the cycle.

## Other well-supported motions

**SMARCA4** HSA-to-helicase spans 36.9–94.7 Å over 10 entries; **NF1** Ras-GAP-to-CRAL-TRIO 39.0–77.0 Å
over 8; **CD163** SRCR2-to-SRCR7 82.3–117.0 Å over 5; **SNRPB2** RRM1-to-RRM2 25.1–83.1 Å over 19,
with AlphaFold just outside at 23.8 Å. **DNM1** (dynamin-1) gives G-domain-to-PH 68.6–115.0 Å and
PH-to-GED 35.2–71.4 Å over 3 entries each, with AlphaFold outside both.

**IGF2R** produces the largest spreads after the integrins — MRH10-to-MRH14 at 46.1–121.4 Å — but
each pair rests on only **2 entries**, so it is suggestive rather than established.

## The sharpest AlphaFold failure in the project

**ACTN2 (α-actinin-2) is an elongated rod and AlphaFold folds it up.** Two templates (1SJJ at 82%
identity, 9SIR at 100%) place CH2 and the EF-hands 250–278 Å apart in a single chain, and the
coordinates confirm it directly: 859 modelled residues spanning 280 Å end to end. AlphaFold places
the same pairs at **56.7–70.3 Å** — an error of roughly 190 Å, consistent across all four
CH-to-EF-hand pairs. The internal EF-hand-1-to-EF-hand-2 distance is 11.9 Å in both the templates
and the AlphaFold model, so the domains themselves are fine; it is the long-range arrangement that
collapses. This was checked specifically because the number looked implausible, and it survived.

## Caveats

Unchanged from batch 1: parent templates are shared across related proteins, so repeated identical
values are one observation seen several times; UniProt Domain features omit some subdomain
architectures; and centroid distance is blind to distance-preserving rotations. Two additions
specific to this batch — pairs resting on only 2 entries (IGF2R, TMPRSS15, IGHG4, ACTN2) should be
treated as provisional, and **NF1 has no AlphaFold value** because at 2,839 residues it exceeds the
AlphaFold DB single-fragment limit, so its row compares templates only.
