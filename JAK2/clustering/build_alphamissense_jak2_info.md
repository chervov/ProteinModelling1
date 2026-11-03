# AlphaMissense for JAK2 — fetched from source, 100% coverage

Companion to [`build_alphamissense.py`](build_alphamissense.py), which writes
[`jak2_alphamissense.csv`](jak2_alphamissense.csv). Written 3 November 2026.

**21,508 of 21,508 — complete.** About **28 seconds**.

---

## 1. The source

Cheng J, Novati G, Pan J, et al. *Accurate proteome-wide missense variant effect prediction with
AlphaMissense.* **Science** 2023;381:eadg7492.
doi:[10.1126/science.adg7492](https://doi.org/10.1126/science.adg7492)

DeepMind publish the full predictions on Zenodo, **CC BY-NC-SA 4.0**, no registration:

| file | size | contents |
|---|--:|---|
| **`AlphaMissense_aa_substitutions.tsv.gz`** | **1.21 GB** | **71 M substitutions, all human canonical — the one used here** |
| `AlphaMissense_isoforms_aa_substitutions.tsv.gz` | 2.46 GB | all isoforms |
| `AlphaMissense_hg38.tsv.gz` | 0.64 GB | keyed by genomic coordinate |
| `AlphaMissense_isoforms_hg38.tsv.gz` | 1.18 GB | |
| `AlphaMissense_hg19.tsv.gz` | 0.62 GB | |
| `AlphaMissense_gene_hg38.tsv.gz` | < 0.01 GB | per-gene summaries |

Record: <https://zenodo.org/records/10813168>

The canonical-substitutions file is keyed exactly as needed — no coordinate mapping, no transcript
choice:

```
uniprot_id   protein_variant   am_pathogenicity   am_class
A0A024R1R8   M1A               0.4673             ambiguous
```

## 2. One protein without keeping the archive

Unlike the ESM-1b zip, **gzip has no random access**, so a range request cannot jump to one
protein. But the file is **sorted by accession**, which allows the next best thing: stream it,
collect the target's rows, and stop the moment the accession changes.

```python
if uid == acc:
    found[variant] = (float(score), klass)
elif found:
    break          # sorted, so the block has ended
```

For JAK2 (`O60674`) that reads **21,235,827 of ~71 M rows in 28 seconds** and then stops. Nothing
is written to disk; the archive is consumed as a stream. Cost scales with where the accession falls
alphabetically — early accessions finish in seconds, late ones read most of the file. Either way it
is one short-lived download rather than a 1.21 GB artefact to store and keep current.

## 3. Checks

- Every returned variant's wild-type residue is verified against
  [`JAK2_O60674_1132aa.txt`](JAK2_O60674_1132aa.txt); a mismatch aborts.
- Written against [`jak2_variant_universe.csv`](jak2_variant_universe.csv) in the canonical order —
  **by position, then substituted-in residue**.
- **21,508 of 21,508** populated.

## 4. Values

| | |
|---|---|
| direction | **higher = more pathogenic** |
| range for JAK2 | 0.0362 … 1.0000 |
| thresholds | the paper's classes: **benign < 0.34**, ambiguous, **pathogenic > 0.564** |

The `am_class` column is carried through as the authors assign it. For JAK2:

| class | n | share |
|---|--:|--:|
| pathogenic | 11,163 | 51.9% |
| benign | 7,590 | 35.3% |
| ambiguous | 2,755 | 12.8% |

## 5. The from-source pipeline reproduces the reference copy exactly

The Liao & Lehner proteome release on this machine also carries AlphaMissense for JAK2, derived
from the same DeepMind release. Comparing all 21,508 shared variants:

**identical to four decimal places on every one; maximum absolute difference 0.000000.**

So for this feature the from-source route and the cached copy agree perfectly — which is the result
that makes the pipeline trustworthy for proteins where no cached copy exists. It is *not* the case
for ESM-1b, where the local file holds a different model entirely
([`build_esm1b_jak2_info.md`](build_esm1b_jak2_info.md) §7).

## 6. Related

- [`build_esm1b_jak2_info.md`](build_esm1b_jak2_info.md) — the companion feature, fetched by range
  request from a zip rather than by streaming
- [`README.md`](README.md) — directory conventions and the variant universe
