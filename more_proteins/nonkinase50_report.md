# Phase 4 (first batch) — non-kinase human proteins with multi-domain mobility

## Selection

3,397 reviewed human non-kinase proteins carry two or more UniProt Domain features in the
200–3,000 residue range. Selecting on literature evidence first would have been the wrong order:
the kinome scan showed that the binding constraint is **template availability**, not architecture —
12 of the 41 genes in `kinase_targets_for_modelling.md` failed purely because no structure spans
the regulatory module. So the 300 candidates with the most PDB cross-references were screened for
templates that genuinely span two or more annotated domains, and the **50 with the most distinct
multi-domain parent templates** were analysed. Raw PDB count is a poor proxy on its own — BRD4 has
618 entries, almost all isolated bromodomain — which is what the screen removes.

The 50 produced **3,473 observations** with no failures: 162 domain pairs across 39 proteins have
two or more distinct parent templates, 30 exceed 15 Å of spread and 18 exceed 20 Å.

## What moves

**ITGB3 (integrin β3) is the largest range of motion measured anywhere in this project, 110 Å.**
(The α-actinins found later in batch 2/3 reach larger *absolute* distances, ~280 Å, but vary by
only ~28 Å across templates — a long rod rather than a large motion.) Its VWFA-to-I-EGF-4
distance spans **32.5–142.5 Å across 12 distinct parent templates** — a 110 Å range — with
VWFA-to-I-EGF-3 at 72 Å over the same 12. This is the bent-to-extended ectodomain switch
([Nishida et al. 2006](https://doi.org/10.1016/j.immuni.2006.07.016);
[Shi et al. 2007](https://doi.org/10.1074/jbc.m701670200)), recovered without being sought.
AlphaFold (36.6 Å) sits at the bent extreme.

**MYH7 (β-cardiac myosin)** gives motor-to-IQ 43.9–80.9 Å and SH3-like-to-IQ 35.4–73.3 Å, both
across 22 parents — the lever-arm swing that converts nucleotide state into displacement
([Llinas et al. 2015](https://doi.org/10.1016/j.devcel.2015.03.025)).

**The immunoglobulin heavy chains** behave as expected of a hinged molecule: IGHG1 Ig1-to-Ig3 spans
16.8–87.7 Å, IGHE Ig1-to-Ig4 34 Å, IGHM Ig1-to-Ig3 23 Å, consistent with cryo-EM of IgG hinge
motion ([Chen et al. 2022](https://doi.org/10.1038/s41467-022-34090-2)) and Fc plasticity in
solution ([Remesh et al. 2018](https://doi.org/10.1016/j.str.2018.03.017)).

**SUPT5H (SPT5)** is the most heavily sampled system in the project — 34–43 parents per pair — with
KOW1-to-KOW4 spanning 30.4–81.5 Å. Its KOW domains thread around RNA polymerase II on long linkers
([Martinez-Rucobo et al. 2011](https://doi.org/10.1038/emboj.2011.64)), so wide variation is the
expected signature rather than a surprise.

**C3** shows anaphylatoxin-to-NTR variation of 22.6 Å over 5 parents, the C3-to-C3b activation
rearrangement ([Janssen et al. 2006](https://doi.org/10.1038/nature05172)), and **HGF** varies by
18–30 Å across its kringle and peptidase domains.

## What does not move, and why that matters

**SHP2 (PTPN11) is the instructive failure.** It is the canonical autoinhibited-to-open phosphatase
([Anselmi & Hub 2023](https://doi.org/10.1038/s42003-023-05682-5)), yet across **20 distinct parent
templates** its N-SH2-to-C-SH2 distance spans just 2.1 Å and both SH2-to-phosphatase distances under
1.5 Å. AlphaFold sits inside that range. Two readings are possible and this analysis cannot separate
them: either the deposited templates are overwhelmingly the closed form, or the activating transition
is a rotation of the N-SH2 that barely changes centroid separation. Either way, a protein whose
two-state behaviour is textbook is invisible to this metric.

PIK3CA is the same story at larger sampling — 22 parents, maximum spread 6.6 Å across all its
domain pairs — as are RIGI (17 parents, 11.8 Å) and AGO2 (34 parents, 10.4 Å). **Heavy template
sampling does not imply measurable variation**, and the absence of variation is not evidence of
rigidity.

## AlphaFold

AlphaFold falls outside the template-derived range in **28 of 162 pairs (17%)**, well below the 28%
seen across the kinome. The clear misses are PIK3C3 (C2-to-PIK-helical, 41.2 Å against an
experimental 72.8–91.2 Å) and IGHM Ig1-to-Ig4 (72.9 Å against 92.5–111.2 Å).

## Caveats

The same two limits as the kinome apply: parent templates are reused, so repeated identical values
are one observation seen many times, and UniProt Domain features omit some subdomain architectures.
Added here is a third, now demonstrated rather than hypothesised — **centroid distance is blind to
distance-preserving rotations**, which is the most likely explanation for the SHP2 result and was
flagged at the outset as the known weakness of a rotation-invariant metric.
