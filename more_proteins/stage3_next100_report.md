# Stage 3 report (partial) — kinases 105–204 by JAK similarity

Scope was reduced from the full remaining kinome (376) to the next 100 at the user's request.
Of those 100, **40 carry two or more UniProt Domain features**; the pipeline produced 695
observations with no failures.

## Numbering is now validated per file

The author-numbering problem found in Stage 2 is handled automatically rather than by excluding a
provider wholesale. Each candidate chain is scored by how often its residue *names* match the
UniProt sequence at their own residue numbers, and a chain is used only above 80% agreement. The
gate kept 160 PDB-provider rows — entries whose author numbering does happen to equal UniProt
numbering — and silently rejected the rest, alongside 317 SWISS-MODEL model rows and 218
AlphaFold rows. This recovers data that the blanket Stage 2 exclusion discarded while preventing
the artifact.

## Genuine multi-conformer evidence

52 domain pairs have two or more distinct experimental parent templates, 9 of them above 20 Å of
spread. Two findings are well evidenced.

**CSF1R has a real bent-versus-extended ectodomain.** Its Ig1-to-Ig5 distance is 75.6 Å on
template 4LIQ and 115.0 Å on 4WRM — both 100% identity, i.e. structures of CSF1R itself — with a
45%-identity homolog (8DFM) at 134.8 Å. Ig1-to-Ig4 behaves the same way, 38.2 Å versus 89.0 and
97.4 Å. Two structures of the same protein differing by 39 Å in one distance is the clearest
single-protein conformational evidence in the project so far, and AlphaFold (78.1 Å) sits with the
compact 4LIQ form.

**The insulin receptor family is the best-sampled system.** INSR's FN3-2-to-FN3-3 distance spans
35.4–67.7 Å across **25 distinct parent templates**, and FN3-1-to-FN3-2 spans 6.8–25.6 Å; IGF1R
(8 parents) and INSRR (11 parents) show the same pattern at 17–27 Å. This is the known large-scale
ectodomain rearrangement of the insulin receptor, recovered here without any prior knowledge of it.

By contrast **KIT's ectodomain is rigid** across 5 parents (Ig1-to-Ig5 132.4–140.9 Å), as are
BRAF's RBD-to-kinase arrangement (4 parents, 38.9–39.2 Å) and FLT4's Ig pairs (4 parents, 8.6–12.2 Å).

## A reproducible AlphaFold offset in AKT

AKT1's PH-to-kinase distance is essentially invariant across **11 distinct experimental parents**,
spanning only 24.0–26.3 Å, yet AlphaFold places it at 34.7 Å — outside the experimental range.
AKT2 and AKT3 repeat this exactly: experimental 24.1 Å against AlphaFold 35.0 and 33.0 Å. Three
paralogs showing the same directional offset against a tightly clustered experimental arrangement
is a systematic error rather than noise, and it matters because the PH-to-kinase arrangement is
the regulatory switch in this family.

Across the batch AlphaFold falls outside the structural range in **13 of 52 pairs (25%)** — the
same rate found independently in the 104-kinase set, on a disjoint set of proteins.

## Coverage gaps

No template spans an ectodomain domain and the kinase domain for any type-III receptor in this
batch: every Ig-to-kinase pair in KIT, CSF1R, FLT1/3/4, PDGFRA and KDR has zero structural parents,
so the transmembrane-spanning arrangement remains unassessable, exactly as for the JAK long-range
pairs. PAK1 and PAK4 give no CRIB-to-kinase templates at all. 60 of the 100 proteins are
single-domain by UniProt annotation and were not assessed.
