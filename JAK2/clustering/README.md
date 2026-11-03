# JAK2 clustering — built step by step

Variant clustering for JAK2, following the method of the Jeanpierre/Debeaupuis JAK1 paper but
**without a published clustering to reproduce**. Started 3 November 2026.

That absence is the defining difference from [`../../JAK1/clustering/`](../../JAK1/clustering/).
There, Dataset EV1 supplied both the variant order and a target to measure against, and success
meant a high ARI against the authors' labels. Here there is no EV1: the clustering has to be
produced and then **validated externally**, against data no feature saw — gnomAD population
frequencies and ClinVar classifications. JAK2 is unusually well supplied with both, thanks to
V617F and the myeloproliferative-neoplasm literature.

## Status

| step | state |
|---|---|
| 1. sequence pinned, variant universe | **done** |
| 2. complete features — AlphaMissense, ESM-1v, ThermoMPNN, BLOSUM62 | next |
| 3. FoldX, dbNSFP block, PolyPhen-2 native run | |
| 4. gnomAD and ClinVar as external validation | |
| 5. the clustering | |
| 6. analysis report | |

## Files

| file | contents |
|---|---|
| [`JAK2_O60674.fasta`](JAK2_O60674.fasta) | UniProt O60674 canonical sequence, 1,132 aa |
| [`jak2_sequence_info.json`](jak2_sequence_info.json) | accession, entry version, md5/sha256, domain bounds — so the numbering is pinned to one sequence version |
| [`jak2_variant_universe.csv`](jak2_variant_universe.csv) | **the canonical index**: `index`, `variant`, 21,508 rows |
| [`build_universe.py`](build_universe.py) | reproduces all three, with the checks |

## The sequence

**UniProt O60674 / JAK2_HUMAN, 1,132 aa**, entry version 251, sequence md5
`06a47ffcc300...` — the full value is in `jak2_sequence_info.json`, so any later file can assert it
is numbering against the same sequence. Domains, from the same record:

| domain | residues |
|---|--:|
| FERM | 37–380 |
| SH2 (atypical) | 401–482 |
| **JH2 pseudokinase** | 545–809 |
| **JH1 kinase** | 849–1124 |

## The variant universe

**21,508 = 19 × 1,132.** Every possible single amino-acid substitution, and nothing else.

**Self-substitutions are excluded.** JAK1 kept its 1,154 (`A1005A`) purely to match EV1 row-for-row.
With no EV1 to match, they would be 1,132 permanently blank rows whose only non-null value would be
a BLOSUM62 diagonal.

### Order: by position, then by substituted-in residue

```
M1A, M1C, M1D, … M1Y, A2C, A2D, …  …  G1132V, G1132W, G1132Y
```

This is deliberately **not** what any source ships, because no two sources agree:

| source | its own order |
|---|---|
| JAK1 EV1 | lexicographic on the variant string — puts 1022 before 1034 before 110 before 39 |
| Liao & Lehner (AlphaMissense, ESM-1v, ThermoMPNN) | the same lexicographic sort |
| ProtVar FoldX | by position |
| dbNSFP (CADD, SIFT, ClinPred, REVEL) | **no stable order** — see below |

dbNSFP cannot define one even in principle. It is keyed on *nucleotide* variants, not amino-acid
substitutions, so the mapping is many-to-one: querying JAK2 codon 618 returns `C618S` **twice**, by
two different nucleotide routes, alongside the stop codon `C618X`, and the rows are not sorted by
genomic position either. Codon 617 returns 6 of the 19 substitutions, in the order
V617L, V617F, V617G, V617D, V617I, V617A.

Position order is the natural one for everything positional — plots along the protein, grouping by
domain — and costs nothing, because **every join in this directory is on `variant`, never on row
position.** JAK1 could join by row position only because every file there was built to one external
order; here the sources disagree, so key-joins are mandatory regardless, which leaves the order free
to be the readable one.

### Checks passed

- Wild-type residue matches O60674 at **all 21,508** rows
- No duplicates, no self-substitutions
- **Identical set** to the Liao & Lehner release (21,508), which supplies AlphaMissense, ESM-1v and
  ThermoMPNN at 100% — so that source joins cleanly, just not by row position
- ProtVar FoldX is a **subset**: 20,349 of 21,508. The 1,159 absentees sit at 61 positions,
  including the whole of 1–38 — AlphaFold's low-confidence N-terminus, which ProtVar trims

## Differences from the JAK1 directory, in one place

| | JAK1 | JAK2 |
|---|---|---|
| target clustering | Dataset EV1, 23,080 rows | **none** |
| validation | ARI against the paper | gnomAD + ClinVar, external |
| rows | 23,080 incl. self-substitutions | **21,508**, excluded |
| order | EV1's lexicographic | **by position** |
| language model | ESM-1b | **ESM-1v** (what the Liao & Lehner release carries) |
| dual-state Rosetta ΔΔG | complete, on Jeanpierre's own models | **not computed** — see [`../../data/ddg/DDG_COMPUTATION_REPORT.md`](../../data/ddg/DDG_COMPUTATION_REPORT.md) |

The last two matter for interpretation. ESM-1b and ESM-1v are different models, so that feature is
not comparable between the two proteins. And without a Rosetta run JAK2 has ThermoMPNN and FoldX but
no closed-versus-open ΔΔG — the one feature that carries conformational information. Whether that is
worth an overnight molab run is a decision for after step 5; if it is, the Shan JAK2 model is the
closed state to use, and **not** AlphaFold, which places JH2–JH1 on a different surface entirely
(4–5 shared interface residues out of ~32).
