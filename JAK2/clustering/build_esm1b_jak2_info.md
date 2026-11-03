# ESM-1b for JAK2 — fetched from source, 100% coverage

Companion to [`build_esm1b.py`](build_esm1b.py), which writes
[`jak2_esm1b.csv`](jak2_esm1b.csv). Written 3 November 2026.

**21,508 of 21,508 — complete.** About **3 seconds**, without downloading the 1.34 GB archive it
comes from.

---

## 1. Why this is fetched rather than copied

The JAK1 directory did **not** obtain ESM-1b from source. `build_features.py` there reads
`sources/orianne/jak1_features.json`, a file supplied with the project. That is fine for JAK1 and
useless for anything else: there is no such file for JAK2, or for the next protein. This script
exists so the feature can be built for **any** human protein from its UniProt accession alone.

## 2. The source

Brandes N, Goldman G, Wang CH, Ye CJ, Ntranos V. *Genome-wide prediction of disease variant
effects with a deep protein language model.* **Nature Genetics** 2023;55:1512–1522.
doi:[10.1038/s41588-023-01465-0](https://doi.org/10.1038/s41588-023-01465-0)

The authors publish precomputed log-likelihood ratios for **every human protein isoform**:

| | |
|---|---|
| portal | <https://huggingface.co/spaces/ntranoslab/esm_variants> |
| file | `ALL_hum_isoforms_ESM1b_LLR.zip` |
| size | **1,335,361,543 bytes — 1.34 GB** |
| members | **42,289**, one CSV per isoform |
| member naming | by UniProt accession — `O60674_LLR.csv` |
| code | <https://github.com/ntranoslab/esm-variants> |

## 3. One protein without downloading the archive

HuggingFace serves `Accept-Ranges: bytes`, so the zip can be read **remotely**. The script
implements a small seekable file over HTTP range requests, hands it to Python's `zipfile`, which
reads the central directory, and extracts the single member wanted:

```python
class HttpFile(io.RawIOBase):
    def read(self, n=-1):
        hi = min(self.pos + n, self.size) - 1
        req = urllib.request.Request(self.url, headers={"Range": f"bytes={self.pos}-{hi}"})
        ...
zf = zipfile.ZipFile(HttpFile(ZIP_URL))
raw = zf.read("content/ALL_hum_isoforms_ESM1b_LLR/O60674_LLR.csv")
```

**175,227 bytes transferred instead of 1.34 GB** — a factor of 7,600 — in about 3 seconds. Changing
`ACC` is all that is needed for another protein; the archive covers all 42,289 human isoforms, and
the script exits with a clear message if the accession is absent.

## 4. The file format, and the transposition

The per-isoform CSV is a **matrix**, not a variant list: 20 rows, one per substituted-in residue,
and one column per position headed `"<wt> <pos>"`.

```
        , M 1  , G 2  , M 3  , A 4  , ...
   K    ,-5.969,-3.564,-2.582,-3.363, ...
   R    ,-5.766,-3.864,-2.669,-3.429, ...
```

It is transposed into this directory's canonical row order — **by position, then substituted-in
residue alphabetically** — and written against
[`jak2_variant_universe.csv`](jak2_variant_universe.csv), so it joins to every other feature file
on `variant`.

## 5. Checks

- The header carries the archive's own wild-type residue at each position. It agrees with
  [`JAK2_O60674_1132aa.txt`](JAK2_O60674_1132aa.txt) at **all 1,132** positions, and the matrix
  covers every position. A mismatch aborts rather than being silently mapped.
- Diagonal entries (`alt == wt`) are skipped, so no self-substitutions enter.
- **21,508 of 21,508** populated.

## 6. Values

| | |
|---|---|
| quantity | log-likelihood ratio, variant against wild type |
| direction | **lower = more damaging** |
| range for JAK2 | −24.094 … +3.444 |
| threshold | the paper's cutoff is **≤ −7.5**, giving 81% TPR and 82% TNR on their benchmarks |

## 7. ESM-1b is not ESM-1v

The Liao & Lehner proteome release on this machine carries **ESM-1v** for JAK2, and it would have
been one line to use it. Against the ESM-1b obtained here, over all 21,508 shared variants:

**Pearson r = +0.652.**

Correlated, plainly not interchangeable. JAK1 used ESM-1b, so substituting ESM-1v would have made
the two proteins incomparable on this feature and changed the clustering. That is the practical
reason this script fetches from the Brandes release rather than reading the local file.

## 8. Related

- [`build_alphamissense_jak2_info.md`](build_alphamissense_jak2_info.md) — the companion feature,
  and the one case where the local copy does match from-source exactly
- [`README.md`](README.md) — directory conventions and the variant universe
