# PolyPhen-2 for JAK2 at 100% — by running the tool, not reading dbNSFP

Companion to [`build_polyphen.py`](build_polyphen.py), which writes
[`jak2_polyphen2_humvar.csv`](jak2_polyphen2_humvar.csv) and
[`jak2_polyphen2_humdiv.csv`](jak2_polyphen2_humdiv.csv). Written 3 November 2026.

**21,508 of 21,508 on both classifiers — 100%, about 2 minutes each.** Against 31.1% from dbNSFP.

---

## 1. Why not dbNSFP

dbNSFP caps PolyPhen-2 at 31.1% because it is indexed on *genomic* variants, and substitutions
needing two or three nucleotide changes have no row
([`build_dbnsfp_jak2_info.md`](build_dbnsfp_jak2_info.md) §2). **PolyPhen-2 itself has no such
limit** — it is protein-level, and its batch query takes `O60674 617 V F` directly. Running it
turns 31.1% into 100% for one protein, in two minutes.

## 2. The interface

There is no API. This drives the same web form a person would use, with the endpoints and quirks
documented by the JAK1 run
([`JAK1/clustering/build_polyphen_jak1_info.md`](../../JAK1/clustering/build_polyphen_jak1_info.md)):

| | |
|---|---|
| submit / status | `https://genetics.bwh.harvard.edu/ggi/cgi-bin/ggi2.cgi` — **POST, multipart/form-data** |
| results | `https://genetics.bwh.harvard.edu/ggi/pph2/<session>/<batch>/pph2-short.txt` |
| session | a `polyphenweb2` cookie, 40 hex chars, valid for months — **no email required** |

Traps recorded by that run, and avoided here: `http://` 301-redirects to `https://`; the submit
path is `/ggi/cgi-bin/ggi2.cgi` and the plausible-looking `/cgi-bin/ggi/ggi2.cgi` 404s; a GET on
the endpoint returns the management page rather than an error.

Form fields used: `_ggi_project=PPHWeb2`, `_ggi_origin=query`, `_ggi_batch_file=<file>`,
`MODELNAME=HumVar|HumDiv`, `UCSCDB=hg19`, `SNPFILTER=1` (canonical transcript), `SNPFUNC=m`
(missense), `_ggi_target_pipeline=Submit Batch`.

## 3. Courtesy, and the limits

- The batch limit is **150,000 substitutions**. JAK2's 21,508 is **14%** of one batch.
- The site asks that whole-proteome batches not be submitted without contacting support first.
  One protein is well inside what it invites; a proteome-scale job is not. The script sends a
  `User-Agent` identifying the run and the protein.
- Polling is every 60 s. Anything faster is just load on a free academic service.

## 4. What happened

| | JAK2 HumVar | JAK2 HumDiv | (JAK1, for comparison) |
|---|---|---|---|
| session | `d9adbd1586571c76…` | `443a7fbee8208dea…` | recorded in `pph2_sessions.txt` |
| job id | 657201 | 657208 | 655187 |
| time to results | **121 s** | **121 s** | ~4 min / ~3 min |
| `pph2-short.txt` | 2.77 MB | 2.77 MB | 2.76 MB |
| scored | **21,508 / 21,508** | **21,508 / 21,508** | 21,926 / 21,926 |

No errors, no retries, nothing dropped. Sessions are recorded in
[`pph2_sessions_jak2.txt`](pph2_sessions_jak2.txt) and remain valid for months, so the output can
be re-fetched without resubmitting; `python3 build_polyphen.py --parse` re-parses what is already
on disk.

## 5. Both models, because the paper does not say which

The paper says only "PolyPhen2 pathogenicity score". The two classifiers differ, and on JAK1 the
choice was the **single most consequential ambiguity** in reproducing the clustering
(leave-one-out ΔARI −0.090, twice the next five features combined). So both are kept.

| | HumVar | HumDiv |
|---|--:|--:|
| probably damaging | 10,600 (49.3%) | 13,581 (63.1%) |
| possibly damaging | 4,186 (19.5%) | 3,269 (15.2%) |
| benign | 6,722 (31.3%) | 4,658 (21.7%) |

**They disagree on the class for 5,025 variants — 23.4%** (JAK1: 25.7%). HumVar is the more
conservative model and the one PolyPhen-2 recommends for Mendelian-disease diagnostics; on JAK1 it
also scored marginally better against the paper's clusters (AUC 0.8848 vs 0.8798). Which to use in
the clustering is a decision to make explicitly, not by default.

## 6. A caveat inherent to the tool

PolyPhen-2 v2.2.3r408's sequence database is **UniRef100 release 2011_12** — fifteen years old.
Not a choice we made, and worth weighing when comparing this feature against ESM-1b or
AlphaMissense, both of which are recent. Its structural component also depends on a PDB/DSSP
snapshot, which is why the JAK1 run differed slightly from dbNSFP's cached values **only** on
structure-scored variants (median absolute difference 0.0065, against 0.0000 for
alignment-only ones).

## 7. Output

Two files, 21,508 rows each in the canonical order, columns
`index, variant, wt, pos, alt, polyphen2_<model>, polyphen2_<model>_pred`.

Raw server output is kept at `pph2_humvar/pph2-short.txt` and `pph2_humdiv/pph2-short.txt`, with
the batch input at [`pph2_input_jak2.txt`](pph2_input_jak2.txt), so the parse can be redone without
touching the network.

`pph2-short.txt` is tab separated **with space padding** — every field needs stripping, which is
the one parsing trap.
