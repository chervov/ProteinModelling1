# PolyPhen-2 for JAK1 at 100% coverage — everything found, and the code

How all 21,926 JAK1 missense substitutions were scored with PolyPhen-2, when the usual route
(dbNSFP) covers only 31.3%. Written 2 November 2026 from a run done the same day. Every number
below was measured in that run, not quoted from documentation.

---

## 1. Why dbNSFP caps at 31.3%, and why PolyPhen-2 itself does not

**dbNSFP is indexed on genomic variants.** A row exists only where a single nucleotide change
produces the substitution. Of the 19 × 1,154 = 21,926 possible JAK1 substitutions, only **6,873
(31.3%)** are reachable that way; the rest need two or three nucleotide changes in one codon and
therefore have no genomic SNV to look up.

**PolyPhen-2 is a protein-level method.** Its batch query accepts a UniProt accession, a position
and two amino acids. Nothing in that input is genomic, so the ceiling does not apply.

This was confirmed rather than assumed. `A1005D` requires two nucleotide changes (GCA → GAC).
PolyPhen-2 logged a complaint and **scored it anyway**:

```
(P23458:1005:A/D)  ERROR: find_gene: Not a single-nucleotide AA substitution: A(GCA)>D
```

That message comes from stage 4's genomic-annotation step and is **non-fatal** — A1005D appears in
the output with `prediction = probably damaging, pph2_prob = 1`. This is the entire basis of the
coverage gain.

---

## 2. The servers

| purpose | URL |
|---|---|
| batch query page (the form) | `https://genetics.bwh.harvard.edu/pph2/bgi.shtml` |
| **submit / status endpoint** | `https://genetics.bwh.harvard.edu/ggi/cgi-bin/ggi2.cgi` |
| results | `https://genetics.bwh.harvard.edu/ggi/pph2/<session>/<batch>/pph2-{short,full,log}.txt` |
| support (for large batches) | `ivan_adzhubey@hms.harvard.edu` |

Notes earned the hard way:

- `http://` returns **301** to `https://`. Use https directly.
- The submit path is **`/ggi/cgi-bin/ggi2.cgi`**. The plausible-looking `/cgi-bin/ggi/ggi2.cgi`
  returns **404** — the segments are the other way round.
- `POST`, `enctype=multipart/form-data`. A GET on the endpoint returns the management page (200).

### Session handling — no email required

Submitting returns a session cookie:

```
Set-Cookie: polyphenweb2=<40 hex chars>; domain=genetics.bwh.harvard.edu;
            path=ggi/cgi-bin; expires=Sun, 31 Jan 2027; HttpOnly; SameSite=Strict
```

**That cookie is the handle to the batch.** Keep it and you can poll status and fetch results
without giving the server an email address. The `NOTIFYME` field exists if you prefer email
notification, but it is optional. The cookie's long expiry means a batch stays retrievable for
months — the session ids from this run are recorded in `pph2_sessions.txt`.

The submit response also contains a hidden field `lastJobSubmitted` with the numeric job id
(655187 for the HumVar run here), useful for cross-referencing with the grid display.

### Form fields

| field | value used | notes |
|---|---|---|
| `_ggi_project` | `PPHWeb2` | hidden, required |
| `_ggi_origin` | `query` to submit, `manage` for status | hidden |
| `_ggi_batch_file` | the input file | or `_ggi_batch` as a textarea for small jobs |
| `description` | free text | max 60 chars; shows in the batch table |
| `NOTIFYME` | *(left empty)* | email, max 48 chars, optional |
| `uploaded_sequences_1` | *(unused)* | optional FASTA upload if your protein is not in UniProt |
| **`MODELNAME`** | `HumVar` / `HumDiv` | **the classifier choice — see §5** |
| `UCSCDB` | `hg19` | or `hg18`; only affects genomic annotation |
| `SNPFILTER` | `1` | 0 = all transcripts, 1 = canonical, 3 = CCDS |
| `SNPFUNC` | `m` | '' = all, c = coding, m = missense |
| `_ggi_target_pipeline` | `Submit Batch` | the submit button |
| `_ggi_target_manage` | `Check Status` | the status button |

### Input format

One substitution per line, whitespace separated:

```
P23458 1005 A C
P23458 1005 A D
P23458 617 I T
```

`<UniProt accession> <position> <from> <to>`. The server also accepts entry names
(`XRCC1_HUMAN 399 R Q`), RefSeq proteins (`NP_005792 59 L P`), rsIDs (`rs1799931`) and genomic
coordinates (`chr1:1267483 G/A`) — but only the protein forms avoid the 31.3% ceiling.

### Limits

- **150,000 amino-acid substitutions** per batch, or 5 million SNP chromosome coordinates.
- Our 21,926 is **15% of one batch**, so JAK1 fits comfortably; so would all four JAK genes at once
  (~87,000).
- The site asks you **not to submit whole-proteome batches without contacting support first**, and
  states that large batches of non-human variants may be terminated without notice. One protein is
  well inside the stated limit; a proteome-scale job is not.

### Measured waiting times

| job | variants | time to results |
|---|--:|---|
| probe | 3 | **< 30 s** |
| JAK1 HumVar | 21,926 | **≈ 4 min** (at 2 min: 127 pending / 33 running; done by 4 min) |
| JAK1 HumDiv | 21,926 | **≈ 3 min** (at 1 min: 259/1; at 2 min: 3/10; done by 3 min) |

The pipeline reports **7 stages**: validating input, mapping genomic SNPs, collecting output,
building MSA and annotating proteins, collecting output, scoring, collecting output. Grid load
showed as "Light" throughout. Polling every 60–120 s is ample; anything faster is just load on a
free academic service.

### Output files (for 21,926 variants)

| file | size | contents |
|---|--:|---|
| `pph2-short.txt` | 2.76 MB | 13 columns — the feature you want |
| `pph2-full.txt` | 10.4 MB | ~60 columns — every intermediate, including structural detail |
| `pph2-log.txt` | 1.37 MB | per-stage errors and warnings |

`pph2-short.txt` columns: `o_acc, o_pos, o_aa1, o_aa2, rsid, acc, pos, aa1, aa2, prediction,
pph2_prob, pph2_FPR, pph2_TPR`. Tab separated **with space padding**, so strip each field.

`pph2-full.txt` adds the things worth keeping for diagnosis: `based_on`, `pph2_class`, `dScore`,
`Score1`, `Score2`, `MSAv`, `Nobs`, `Nstruct`, `Nfilt`, `PDB_id`, `PDB_ch`, `ident`, `dVol`,
`dProp`, `SecStr`, `NormASA`, `B-fact`, `PfamHit`, `IdPmax`, `IdQmin`.

### Provenance stamped in every output

```
Predictions: PolyPhen-2 v2.2.3r408
Sequences:   UniProtKB/UniRef100 Release 2011_12 (14-Dec-2011)
Structures:  PDB/DSSP Snapshot 25-May-2021 (178229 Structures)
Genes:       UCSC MultiZ46Way GRCh37/hg19 (08-Oct-2009)
```

**The sequence database is from 2011.** That is inherent to PolyPhen-2 v2.2.3, not a choice, and it
matters when weighing this feature against ESM-1b or AlphaMissense, whose alignments are current.
The structure snapshot, by contrast, is recent — and that asymmetry explains §6.

---

## 3. Input validation the server performs

PolyPhen-2 checks the wild-type residue against its own copy of the sequence. A mismatch is fatal
for that line:

```
(P23458:617:V/F)  ERROR: Neither AA1 (V) nor AA2 (F) in input matches
                         P23458 query sequence residue (I) at position (617)
```

This was a real error of mine — I wrote `V617F` out of JAK2 habit, but **JAK1 has I617**. Useful
safety net: a numbering or isoform error cannot pass silently. Check your own wild types against
the sequence first (see `build_features.py`, which does this for all 23,080 EV1 rows).

---

## 4. The code

Submit, poll, parse. Written as it was actually run.

```python
"""PolyPhen-2 batch for every possible substitution in one protein.

Three steps: submit a batch, poll with the session cookie until the result links appear,
parse pph2-short.txt into a feature table. No email, no API key - the session cookie that
comes back from the submission is the only handle needed.
"""
import gzip
import io
import time

import pandas as pd
import requests

ENDPOINT = "https://genetics.bwh.harvard.edu/ggi/cgi-bin/ggi2.cgi"
RESULTS = "https://genetics.bwh.harvard.edu/ggi/pph2/{session}/{batch}/{name}"


def submit(variants, acc="P23458", model="HumVar", description="batch"):
    """variants: iterable of (pos, wt, alt). Returns (session_cookie, requests.Session).

    The batch goes up as a file rather than in the textarea: 21,926 lines is far past
    what a form field is meant to carry, and the file upload has no such limit.
    """
    body = "\n".join(f"{acc} {pos} {wt} {alt}" for pos, wt, alt in variants)
    s = requests.Session()                      # keeps the polyphenweb2 cookie for us
    r = s.post(
        ENDPOINT,
        data={
            "_ggi_project": "PPHWeb2",
            "_ggi_origin": "query",
            "description": description[:60],
            "MODELNAME": model,                 # HumVar or HumDiv - NOT interchangeable
            "UCSCDB": "hg19",                   # only affects genomic annotation
            "SNPFILTER": "1",                   # canonical transcript
            "SNPFUNC": "m",                     # missense only
            "_ggi_target_pipeline": "Submit Batch",
        },
        files={"_ggi_batch_file": ("batch.txt", body, "text/plain")},
        timeout=600,
    )
    r.raise_for_status()
    session = s.cookies.get("polyphenweb2")
    if not session:
        raise RuntimeError("no polyphenweb2 cookie - the batch was not accepted")
    return session, s


def wait(s, session, batch=1, tries=90, every=60):
    """Poll the management view until the result links exist, then return the short table.

    The status page is the same endpoint with _ggi_origin=manage. Result links only
    appear once the 7-stage pipeline has finished, so their presence is the done signal.
    """
    for attempt in range(1, tries + 1):
        r = s.post(ENDPOINT, data={"_ggi_project": "PPHWeb2", "_ggi_origin": "manage",
                                   "_ggi_target_manage": "Check Status"}, timeout=180)
        if "pph2-short.txt" in r.text:
            url = RESULTS.format(session=session, batch=batch, name="pph2-short.txt")
            return s.get(url, timeout=600).text
        time.sleep(every)                       # 60 s is plenty; the jobs took 3-4 min
    raise TimeoutError(f"not finished after {tries * every / 60:.0f} min; "
                       f"session {session} stays retrievable")


def parse(short_text):
    """pph2-short.txt -> DataFrame. Tab separated but space padded, so strip every field."""
    rows = []
    for line in short_text.splitlines():
        if line.startswith("#") or not line.strip():
            continue                            # '#' covers both header and the ## footer
        f = [c.strip() for c in line.split("\t")]
        if len(f) < 12:
            continue
        rows.append({
            "variant_id": f"{f[2]}{f[1]}{f[3]}",          # wt + pos + alt
            "pos": int(f[1]), "wt": f[2], "alt": f[3],
            "prediction": f[9],                            # benign / possibly / probably
            "prob": pd.to_numeric(f[10], errors="coerce"), # pph2_prob, the feature
            "fpr": pd.to_numeric(f[11], errors="coerce"),
        })
    return pd.DataFrame(rows)


if __name__ == "__main__":
    # all 19 substitutions at every position of the canonical sequence
    seq = "".join(l.strip() for l in open("JAK1_P23458.fasta").readlines()[1:])
    variants = [(i + 1, wt, alt)
                for i, wt in enumerate(seq)
                for alt in "ACDEFGHIKLMNPQRSTVWY" if alt != wt]
    print(f"{len(variants):,} substitutions")              # 21,926 for JAK1

    for model in ("HumVar", "HumDiv"):                     # both: they disagree on 25.7%
        session, s = submit(variants, model=model, description=f"JAK1 all {model}")
        print(f"{model}: session {session}")               # record it - it is the handle
        df = parse(wait(s, session))
        print(f"{model}: {len(df):,} scored, "
              f"{df.prob.notna().sum():,} with a probability")
        df.to_csv(f"jak1_polyphen2_{model.lower()}.csv", index=False)
```

To align with Dataset EV1 afterwards, map onto the EV1 row order rather than reindexing — EV1 has
23,080 rows because it includes the 1,154 self-substitutions, which have no PolyPhen-2 score:

```python
base = pd.read_csv("jak1_blosum62.csv")[["variant_id", "wt", "pos", "alt", "cluster"]]
look = df.drop_duplicates("variant_id").set_index("variant_id")
base["polyphen2_humvar_prob"] = base.variant_id.map(look["prob"])   # blank for self-subs
```

---

## 5. HumDiv and HumVar

PolyPhen-2 is one algorithm with **two classifiers**, differing only in training data.

| | **HumDiv** | **HumVar** |
|---|---|---|
| damaging class | ~3,000 UniProt alleles with known effects on molecular function causing Mendelian disease | **all** ~22,000 human disease-causing mutations in UniProt |
| neutral class | differences between human proteins and closely related mammalian homologues, assumed harmless | **common human nsSNPs (MAF > 1%)** with no disease annotation |
| behaviour | calls damaging more readily | **more conservative** |
| recommended for | rare alleles in complex phenotypes, dense mapping under GWAS peaks, studies of natural selection | **diagnosing Mendelian disease** — separating drastic effects from mildly deleterious alleles |

The asymmetry follows from the neutral class. HumVar was trained to call *common human variants*
benign, and many of those are mildly deleterious; so it demands stronger evidence before calling
damaging. HumDiv's neutral examples are cross-species differences, a cleaner set, so its threshold
sits lower in effect.

Both report `pph2_prob` in [0, 1] plus a three-way call: `benign`, `possibly damaging`,
`probably damaging`. The class boundaries are model-specific and FPR-calibrated, which is why the
same probability can carry a different label between models.

---

## 6. Results, and the difference between the models

Both models: **21,926 of 21,926 — 100% coverage.** dbNSFP gives 6,873 (31.3%).

| | HumDiv | HumVar |
|---|--:|--:|
| probably damaging | **14,343 (65.4%)** | **11,212 (51.1%)** |
| possibly damaging | 3,304 (15.1%) | 3,754 (17.1%) |
| benign | 4,279 (19.5%) | 6,960 (31.7%) |
| mean `pph2_prob` | 0.790 | 0.663 |
| median in EV1 cluster 1 | 0.428 | 0.096 |
| median in EV1 cluster 2 | 1.000 | 0.994 |
| AUC vs the EV1 clusters | 0.8798 | **0.8848** |

**The two models disagree on 5,633 of 21,926 substitutions — 25.7%.** Pearson 0.871,
Spearman 0.940. HumDiv calls 28% more variants "probably damaging" in absolute terms.

**Why this matters for reproducing the paper.** Its appendix lists only "PolyPhen2 pathogenicity
score (Adzhubei et al, 2013)" and does not name a model. With a quarter of variants labelled
differently, that is a real fork in the feature matrix, not a detail. Both columns are therefore
provided, and the choice is explicit. HumVar is the better default here: it is the model
PolyPhen-2 recommends for Mendelian-disease work, and it scores marginally better against the EV1
clusters.

### Validation against the dbNSFP values already in the repository

On the 423 variants that have a score in both:

| | HumVar | HumDiv |
|---|--:|--:|
| Pearson | 0.9575 | 0.9608 |
| Spearman | 0.9733 | 0.9657 |
| median absolute difference | 0.0010 | 0.0000 |
| differing by > 0.1 | 56 (13.2%) | 63 (14.9%) |
| worst case | 0.688 | 0.820 |

High correlation, but 13–15% differing by more than 0.1 is too much to dismiss. The cause is
specific and testable: PolyPhen-2 mixes **sequence** and **structural** features, and this run's
PDB/DSSP snapshot (25-May-2021, 178,229 structures) is newer than whatever dbNSFP used. If that is
the explanation, variants scored without a structure should agree exactly. Splitting on whether a
`PDB_id` was used:

| | n | median absolute difference | differing > 0.1 |
|---|--:|--:|--:|
| **alignment only** | 109 | **0.0000** | **0.0%** |
| **a structure contributed** | 314 | 0.0065 | **17.8%** |

Confirmed. Where the inputs are identical the reproduction is **exact**; every disagreement
involves a structure. For context, `based_on` across all 21,926 is: alignment 21,210,
`alignment_mz` 323, structure 241, sequence annotation 152 — and **78.4% have a usable `PDB_id`**,
so the structural component is in play for most variants even when the prediction is "based on"
the alignment. (Example: E1133G used PDB **4OLI** chain A at 54% identity.)

**Consequence: the new column is preferable for clustering**, not merely more complete. It is
internally consistent — one tool version, one sequence database, one structure snapshot across all
21,926 — whereas the dbNSFP column is a mixture of whatever was current when each value was
computed.

### One result that looks like a regression and is not

The AUC against the EV1 clusters is **0.88** here, below the **0.9425** the repository reports for
PolyPhen-2 at 31.3% coverage. That is expected, not a loss. The 31% subset is exactly the
single-nucleotide-reachable one, which is chemically conservative — its BLOSUM62 mean is about
−0.54 against −1.76 for the unreachable remainder. An easier subset gives a higher AUC. Measuring
on all 21,926 is the harder and more honest test, and the apparent drop is a clean illustration of
the sampling bias that comes with scoring only what dbNSFP happens to cover.

---

## 7. Files this produced

| file | contents |
|---|---|
| `pph2_input_jak1.txt` | the 21,926-line batch input, in EV1 order |
| `jak1_polyphen2_humvar.csv` | HumVar, 23,080 rows in EV1 order (`prob`, `pred`) |
| `jak1_polyphen2_humdiv.csv` | HumDiv, same shape |
| `jak1_pph2_humvar_raw.txt.gz` | raw `pph2-short.txt`, 251 KB gzipped from 2.76 MB |
| `jak1_pph2_humdiv_raw.txt.gz` | the same for HumDiv |
| `pph2_sessions.txt` | session ids — the batches stay retrievable until Jan 2027 |
| `build_polyphen.py` | parse + align to EV1 + validate against dbNSFP |
| `compare_models.py` | HumDiv vs HumVar, and both against the EV1 clusters |
| `explain_diff.py` | the structure-vs-alignment split in §6 |

`pph2-full.txt` (10.4 MB each) is **not** in the repository. Fetch it from the session URL if the
structural columns are ever needed; `explain_diff.py` shows how they are read.

---

## 8. For the other three JAK genes

The same route applies unchanged — only the accession and sequence differ:

| gene | UniProt | length | substitutions |
|---|---|--:|--:|
| JAK1 | P23458 | 1,154 | 21,926 ✔ done |
| JAK2 | O60674 | 1,132 | 21,508 |
| JAK3 | P52333 | 1,124 | 21,356 |
| TYK2 | P29597 | 1,187 | 22,553 |

All four together are **87,343** substitutions — still inside the 150,000 single-batch limit,
though submitting one gene per batch keeps the bookkeeping simpler and is politer to a shared
service. Expect three to five minutes per gene per model.
