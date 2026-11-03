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
| 2. **eight of the paper's eleven features** | **done** |
| 3. gnomAD and ClinVar as external validation | next |
| 4. the clustering | |
| 5. analysis report | |
| — | |
| ΔΔG closed / open / delta | deferred; see *Differences from JAK1* |

### Features built

| feature | coverage | source | time | document |
|---|--:|---|--:|---|
| **ESM-1b** | **100%** | HuggingFace zip, one member by range request | 3 s | [info](build_esm1b_jak2_info.md) |
| **AlphaMissense** | **100%** | DeepMind Zenodo, streamed with early stop | 28 s | [info](build_alphamissense_jak2_info.md) |
| **BLOSUM62** | **100%** | computed, matrix cross-checked | 0.2 s | [info](build_blosum62_jak2_info.md) |
| **PolyPhen-2 HumVar** | **100%** | PolyPhen-2 server, batch submission | 2 min | [info](build_polyphen_jak2_info.md) |
| **PolyPhen-2 HumDiv** | **100%** | same | 2 min | [info](build_polyphen_jak2_info.md) |
| FoldX (for "MutFunc") | 94.6% | ProtVar; **EBI host blocked**, committed extract used | < 1 s | [info](build_foldx_jak2_info.md) |
| CADD | 31.1% | dbNSFP via myvariant | 48 s | [info](build_dbnsfp_jak2_info.md) |
| SIFT | 31.1% | same | — | same |
| ClinPred | 31.1% | same | — | same |

Every feature file has the same shape: 21,508 rows in the canonical order, `index, variant, wt,
pos, alt, <feature>`, joined on `variant`. Blank means **not available**, never 0.

## Files

| file | contents |
|---|---|
| [`JAK2_O60674.fasta`](JAK2_O60674.fasta) | UniProt O60674 canonical sequence, 1,132 aa, standard FASTA |
| [`JAK2_O60674_1132aa.txt`](JAK2_O60674_1132aa.txt) | the same sequence as **plain text, unwrapped on a single line**, after one `#` comment line carrying the accession, length and md5. For pasting into a web form, or reading with one `readline()`. Accession and length are in the filename too, so a truncated copy is obvious. |
| [`jak2_sequence_info.json`](jak2_sequence_info.json) | accession, entry version, md5/sha256, domain bounds — so the numbering is pinned to one sequence version |
| [`jak2_variant_universe.csv`](jak2_variant_universe.csv) | **the canonical index**: `index`, `variant`, 21,508 rows |
| [`build_universe.py`](build_universe.py) | reproduces all four, with the checks |
| [`jak2_esm1b.csv`](jak2_esm1b.csv) | ESM-1b LLR, **21,508 / 21,508** — [`build_esm1b_jak2_info.md`](build_esm1b_jak2_info.md) |
| [`jak2_alphamissense.csv`](jak2_alphamissense.csv) | AlphaMissense + class, **21,508 / 21,508** — [`build_alphamissense_jak2_info.md`](build_alphamissense_jak2_info.md) |
| [`build_esm1b.py`](build_esm1b.py), [`build_alphamissense.py`](build_alphamissense.py) | fetch both from source, for any accession |

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
| language model | ESM-1b, from a project-supplied JSON | **ESM-1b, fetched from the Brandes release** — matching JAK1, not the ESM-1v the local file holds |
| dual-state Rosetta ΔΔG | complete, on Jeanpierre's own models | **not computed** — see [`../../data/ddg/DDG_COMPUTATION_REPORT.md`](../../data/ddg/DDG_COMPUTATION_REPORT.md) |

### Features are fetched from source, not copied

JAK1 read ESM-1b and AlphaMissense out of `sources/orianne/jak1_features.json`, a file supplied
with the project. No such file exists for JAK2 or for the next protein, so both are fetched here
from the original releases, keyed only on a UniProt accession:

| feature | source | archive | what is actually transferred |
|---|---|--:|---|
| ESM-1b | [HuggingFace, Brandes 2023](https://huggingface.co/spaces/ntranoslab/esm_variants) | 1.34 GB zip, 42,289 members | **175 KB** — one member, by HTTP range request, ~3 s |
| AlphaMissense | [Zenodo, DeepMind](https://zenodo.org/records/10813168) | 1.21 GB gz, 71 M rows | streamed, stops early at the accession, ~28 s, nothing stored |

Two validations came out of that. AlphaMissense from source is **identical to four decimal places**
to the cached Liao & Lehner copy on all 21,508 variants. ESM-1b is **not** the same as the ESM-1v in
that file — Pearson r = +0.652 — so using the local copy would have broken comparability with JAK1.

And without a Rosetta run JAK2 has ThermoMPNN and FoldX but
no closed-versus-open ΔΔG — the one feature that carries conformational information. Whether that is
worth an overnight molab run is a decision for after step 5; if it is, the Shan JAK2 model is the
closed state to use, and **not** AlphaFold, which places JH2–JH1 on a different surface entirely
(4–5 shared interface residues out of ~32).
