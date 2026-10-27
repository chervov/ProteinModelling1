# Stage 1 report — JAK family inter-domain centroid analysis

## What was measured

Domain definitions came from UniProt (FERM, SH2, Protein kinase 1 = JH2 pseudokinase,
Protein kinase 2 = JH1 kinase). Templates were enumerated from the SWISS-MODEL Repository,
which returns PDB entries and homology models already renumbered to UniProt coordinates and,
critically, names each model's **parent template** — so models that inherit one template's
conformation can be identified as non-independent. The AlphaFold v6 model was treated as one
further template, and the parent cryo-EM structures were additionally measured directly from
RCSB coordinates.

344 templates were found across the four human JAKs; 35 span two or more annotated domains.
With 11 vertebrate orthologs pooled in, the final set is 310 pair observations over 70 templates.

## The block is rigid; JH1 is the mobile unit

Restricting to JAK-lineage templates, the three distances internal to the FERM–SH2–JH2 block
are nearly invariant, while every distance involving JH1 varies:

| pair | n | range (Å) | spread (Å) | SD (Å) |
|---|---|---|---|---|
| FERM–JH2 | 10 | 45.8–48.1 | 2.3 | 0.8 |
| SH2–JH2 | 10 | 39.7–41.9 | 2.2 | 0.7 |
| FERM–SH2 | 12 | 35.6–42.1 | 6.5 | 2.1 |
| JH2–JH1 | 17 | 37.2–48.0 | 10.8 | 4.2 |
| SH2–JH1 | 10 | 51.9–79.1 | 27.1 | 13.3 |
| FERM–JH1 | 10 | 39.7–94.2 | 54.5 | 21.3 |

The displacement grows with distance along the block — small against JH2, larger against SH2,
largest against FERM. That is the geometric signature of a hinge at the JH2–JH1 junction: a
rotation about that joint barely moves JH1 relative to its neighbour but swings it far from the
far end of the block. The ordering confirms the stated architecture, with the stable block and
the kinase domain travelling on it.

## Two experimental conformations exist, and they differ only in JH1

Measured directly on the deposited coordinates of the two murine full-length cryo-EM structures:

| structure | FERM–SH2 | FERM–JH2 | SH2–JH2 | JH2–JH1 | SH2–JH1 | FERM–JH1 |
|---|---|---|---|---|---|---|
| 7T6F (3.6 Å) | 38.8 | 47.7 | 39.9 | 45.0 | 53.9 | 84.1 |
| 8EWY (5.5 Å) | 38.8 | 47.7 | 39.9 | 46.9 | 79.0 | 94.1 |

The block distances are identical to 0.1 Å while SH2–JH1 differs by 25.1 Å and FERM–JH1 by
10.0 Å. Two chains per structure gave identical values, as expected for a C2 homodimer. The
exact agreement of the block across two different maps suggests the block was rigid-body placed
from shared coordinates, so the block identity is partly a modelling choice rather than
independent corroboration; the JH1 difference, however, is a real difference between two
deposited experimental structures.

Separately, 4OLI — the human TYK2 pseudokinase–kinase crystal structure at 2.8 Å — gives a
JH2–JH1 distance of 39.0 Å, the compact end of that pair's range, confirming it as the closed
autoinhibited arrangement.

## The compact state comes only from AlphaFold

Classifying every template by FERM–JH1 with a 60 Å cut gives 33 extended and 8 compact
observations across the pooled family. **All 8 compact observations are AlphaFold predictions;
none come from a template-derived model**, because every full-length homology model descends
from 7T6F or 8EWY and is therefore extended by construction.

AlphaFold's choice is not consistent within the family or even within one gene. Human TYK2
(39.7 Å) and human JAK3 (41.5 Å) are compact, whereas human JAK1 (92.2 Å) and human JAK2
(93.8 Å) are extended and land almost exactly on the 8EWY value of 94.1 Å. Across orthologs the
same gene flips state: JAK2 is extended in human (93.8 Å), mouse (93.6 Å) and pig (93.9 Å) but
compact in rat (46.0 Å), orangutan (45.7 Å) and chicken (43.0 Å). Sequences above 90% identity
receiving opposite arrangements is strong evidence that AlphaFold's placement of JH1 relative to
the block is arbitrary rather than informative — which is exactly what the high inter-module PAE
for these pairs already indicated.

One consistency worth noting: TYK2's AlphaFold JH2–JH1 distance of 37.2 Å closely matches the
4OLI crystal value of 39.0 Å, so where AlphaFold does produce a compact arrangement it
reproduces the known closed pseudokinase–kinase geometry rather than inventing one.

## Predictions versus outcome

Of the five predictions registered before the run, three held and two need correcting.

Held: FERM–SH2 is rigid (SD 2.1 Å); JH2–JH1 shows real but modest variation (spread 10.8 Å);
homolog pooling materially raises coverage, taking FERM–JH1 from 10 to 41 observations.

Corrected: the claim that long-range FERM-to-JH1 pairs are **unassessable** was wrong — two
deposited experimental structures differ measurably in exactly those pairs. And the prediction
that AlphaFold would sit in a compact arrangement holds for only half the family; for JAK1 and
JAK2 it reproduces the extended murine geometry almost exactly.

## Consequence for the remaining stages

Two filters carry forward. Cross-family templates must be excluded: models of JAK SH2–JH2 built
on ABL1 (1OPL), SRC (1Y57) or FAK (2J0J/2J0K) at 22–26% identity inflate that pair's spread from
SD 0.7 Å to SD 8.3 Å and are measuring the template's architecture, not the target's. And
apparent variation must be attributed by provenance, since in this family the entire open/closed
contrast would have been reported as biology had the parent template and the prediction source
not been tracked.
