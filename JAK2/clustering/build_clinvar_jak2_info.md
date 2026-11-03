# ClinVar for JAK2 — the secondary criterion, and why it is thin

Companion to [`build_clinvar.py`](build_clinvar.py), which writes
[`jak2_clinvar.csv`](jak2_clinvar.csv). Written 3 November 2026.

**347 of 21,508 have a ClinVar record — 1.61%. Of those, only 21 carry a usable label.**

---

## 1. Source and method

NCBI E-utilities against the `clinvar` database:

```
esearch.fcgi?db=clinvar&term=JAK2[gene] AND "missense variant"[molecular consequence]
esummary.fcgi?db=clinvar&id=...
```

347 records, collected in one search and two summary batches, in about 15 s.

**The bulk alternative also works from here**, unlike EBI's:
`https://ftp.ncbi.nlm.nih.gov/pub/clinvar/tab_delimited/variant_summary.txt.gz`, **458 MB**,
HTTP 200. E-utilities is used because one gene is a few hundred records; for a gene with thousands
of entries the bulk file would be the better choice, and the script's docstring says so.

## 2. The position trap, and how it is avoided

The `protein_change` field returned by esummary lists **every isoform's numbering at once**:

```
protein_change: 'I218V, I474V, I623V'
```

Three positions, one variant — unusable directly, and a silent source of error if the first were
taken. The record `title` carries the canonical transcript instead:

```
NM_004972.4(JAK2):c.1867A>G (p.Ile623Val)
```

`NM_004972` is the MANE Select transcript, and its protein `NP_004963.1` is **byte-identical to
UniProt O60674** — verified independently during the 24-variant panel work. The parse therefore
requires `NM_004972` in the title and **then checks the wild-type residue against the pinned
sequence anyway**.

Result: **347 of 347 parsed, 0 on another transcript, 0 wild-type mismatches.**

Where a substitution has several records, the **best-reviewed** one is kept, ranked by ClinVar's
gold stars (practice guideline 4, expert panel 3, multiple submitters 2, single submitter 1, no
criteria 0).

## 3. Spot-check against known variants

| variant | captured as | stars | accession |
|---|---|--:|---|
| **V617F** | Pathogenic/Likely pathogenic | 2 | VCV000014662 |
| V617I | Pathogenic | 0 | VCV000029763 |
| R867Q | Likely pathogenic | 2 | VCV002136731 |
| R938Q | Likely pathogenic | 1 | VCV004813688 |
| R1063H | Benign/Likely benign | 2 | VCV000134555 |
| E846D | Conflicting classifications | 1 | VCV000134553 |
| T875N | *not in ClinVar* | — | — |
| L611S | *not in ClinVar* | — | — |

Every one matches what the independent
[`JAK2/variant_panel_24`](../../JAK2/variant_panel_24/README.md) work found, including the two
genuine absences. The pipeline is right.

## 4. The problem: 88% of JAK2's ClinVar is "Uncertain significance"

| classification | n |
|---|--:|
| **Uncertain significance** | **305** |
| Conflicting classifications | 15 |
| Likely benign | 10 |
| Benign/Likely benign | 4 |
| Likely pathogenic | 3 |
| Pathogenic | 3 |
| Pathogenic/Likely pathogenic | 1 |
| not provided / other / blank | 6 |

| review status | n |
|---|--:|
| 2 stars | 51 |
| 1 star | 279 |
| 0 stars | 17 |

Stripping to variants with an actual direction leaves **21 labels out of 21,508 — 0.098%**:

- **7 pathogenic**: K539L, K607N, V617F, V617I, R867Q, R938Q, P1095L
- **14 benign**: T7M, G13V, R122H, G127D, K244R, N337D, L383V, V392M, C480F, N490S, L892V,
  Y1021F, R1063H, D1096E

## 5. What that means for using it

**ClinVar cannot validate a JAK2 clustering on its own.** Twenty-one labels, seven of them
pathogenic, will not support an odds ratio worth quoting. gnomAD, with 1,498 observed variants,
has to be the primary external criterion
([`build_gnomad_jak2_info.md`](build_gnomad_jak2_info.md)).

ClinVar is worth keeping for two narrower jobs:

1. **A sanity check with named variants.** If a clustering puts V617F in the tolerant cluster,
   something is wrong, and that is worth knowing even from a sample of seven.
2. **Seeding.** The paper seeded its JAK1 clustering with 5 common gnomAD variants and 5 reported
   gain-of-function variants. JAK2 has no published seed list, and these 21 labels are the obvious
   place to draw an equivalent from — with the caveat that they are a biased sample, since
   V617F-adjacent positions are far better characterised than the rest of the protein.

**One circularity to watch.** AlphaMissense and ESM-1b are trained, directly or indirectly, on
data overlapping ClinVar. Validating a clustering built from those features against ClinVar is not
fully independent. gnomAD is the cleaner test — allele frequencies are an observation, not a
prediction.

## 6. Output

[`jak2_clinvar.csv`](jak2_clinvar.csv), 21,508 rows in the canonical order, columns
`index, variant, wt, pos, alt, clinvar_accession, clinvar_significance, clinvar_review_status,
clinvar_stars, clinvar_conditions`.

Blank means no ClinVar record. The `clinvar_stars` column is there so the 279 single-submitter
records can be separated from the 51 with multiple concordant submitters, which matter rather
differently.
