# Stage 2 report — the 104-kinase set

## Scope

Of the 104 kinases, **77 carry two or more UniProt-annotated Domain features** and can yield a
domain pair at all; 27 are single-domain by that definition. One systematic gap matters: UniProt
annotates receptor tyrosine kinase ectodomain subdomains under feature types other than Domain,
so EGFR, ERBB2, ERBB4 and LTK appear single-domain here and were excluded despite being prime
candidates. Using a single definition source keeps the analysis coherent across stages, but this
gap should be closed with InterPro boundaries before the proteome stage is taken as complete.

## A numbering pitfall that invalidated the first pass

The SWISS-MODEL Repository serves two kinds of coordinate file. Models it builds itself
(`provider=SWISSMODEL`) and AlphaFold models are numbered in UniProt coordinates — verified by
scoring each residue name against the UniProt sequence at its own number, which returns a match
fraction of **1.00**. Files it relays for PDB entries (`provider=PDB`) are served in **PDB author
numbering**, which for most entries is offset: the same test returns **0.05–0.09**. Domain
boundaries taken from UniProt therefore select the wrong residues in those files.

Dropping `provider=PDB` rows removed **372** of 1502 observations. A separate filter excluding
SWISS-MODEL models built on templates below 40% identity — the cross-family guard carried over
from Stage 1 — removed a further **260**, leaving 870. The numbering fix and the identity guard
are independent; only the first 372 are attributable to the numbering problem. The correction is
not cosmetic.
On the uncorrected data SRC appeared to show a 26.4 Å spread in its SH3-to-kinase distance across
nine structures, which would have directly contradicted the earlier PAE call that SRC is a single
rigid body. Measured on verified sources — including a model built on 1Y57, the activated Src
template — the same pair spans only **36.3 to 37.7 Å**. SRC is rigid by this metric and the two
methods agree. The apparent contradiction was an artifact.

Because models built on an experimental template reproduce that template's arrangement in UniProt
numbering, the parent-template label still carries the structural evidence. Distinct parent
templates are therefore counted as independent conformational observations, which is how Stage 1
was already constructed.

## Verified variation

Across verified sources, 42 proteins give 139 domain pairs with two or more distinct experimental
parent templates, of which **23 pairs exceed 20 Å of spread**. Three groups dominate.

The **Eph receptors** are the most consistent signal: the ligand-binding domain to
fibronectin-III-2 distance spans 26–34 Å in eleven receptors (EPHA1, A3, A5, A6, A7, A8, A10,
EPHB1–B4), with absolute distances of 112–147 Å. Agreement across eleven independently modelled
paralogs is harder to dismiss than any single protein's range. The same receptors show a
kinase-to-SAM spread near 23 Å.

The **Tec family** shows the largest single-protein range. BTK's SH3-to-kinase distance is 63.8,
79.9 and 85.2 Å on three distinct experimental parents, with AlphaFold far more compact at 33.0 Å;
its PH-to-SH3 distance spans 48.0 to 75.0 Å. ITK and TEC behave the same way. This is consistent
with the conformational literature on full-length BTK retrieved earlier, where the PH-TH module is
heterogeneous and inhibitor binding shifts the whole-protein arrangement.

The **JAKs** independently reproduce the Stage 1 finding: SH2-to-JH1 spreads 23.8–24.9 Å in JAK1,
JAK3 and TYK2, which is the 7T6F-versus-8EWY difference recovered through a different route.

## Where AlphaFold sits

For the **139** pairs where an AlphaFold model coexists with **two or more** template-derived
models — the only pairs where a genuine range is spanned — AlphaFold falls **outside** that range
in **35 cases (25%)**, 19 more compact and 16 more extended. Widening the comparison to all 183
pairs that have at least one template-derived model raises the count to 56 (31%), but 44 of those
pairs have a single template model, so 21 of the 56 compare against one point rather than a range
and are not evidence of falling outside anything. The deviations are directional by family:
AlphaFold is at the compact extreme for Tec-family SH3-to-kinase and at the extended extreme for
Eph LBD-to-FN3-2. It is not a neutral sample of the conformational range.

## Two caveats on independence

57 distinct parent templates underlie the whole set, and the popular ones are reused widely —
1Y57 is the parent for models of 13 different proteins, 1OPL for 7. When two paralogs report an
identical distance, that is one conformational observation seen twice, not two. Values repeated to
0.1 Å across BTK, TEC and ITK (85.2 Å on parent 8GMB) are exactly this case.

Separately, template enumeration remains conservative. SWISS-MODEL's stated `from`-`to` range
understates what a file actually contains — AXL's 2C5D entry is reported as 34–225 but its chain
spans 23–420 — so templates whose stated range touched only one domain were skipped and some
assessable pairs are missing. The relaxed re-run that would close this gap was blocked pending
approval and has not been performed.
