# FoldX ddG for JAK2 — the source, the blocker, and three ways round it

Companion to [`build_foldx.py`](build_foldx.py), which writes [`jak2_foldx.csv`](jak2_foldx.csv).
Written 3 November 2026.

**20,349 of 21,508 — 94.6%.** Obtained today from a committed extract because the source host is
unreachable from this machine; the script tries the source first and will use it the moment it
returns.

---

## 1. What this feature is, and why it is a substitute

The paper's seventh feature is the **"MutFunc score"**. The JAK1 directory established that
today's mutfunc cannot reproduce what the paper used
([`JAK1/clustering/build_mutfunc_jak1_info.md`](../../JAK1/clustering/build_mutfunc_jak1_info.md) §2),
and substituted FoldX ddG from ProtVar. JAK2 does the same, so the two proteins stay comparable.

This is a **substitution, not the paper's value**, and should be read as such.

## 2. The source

| | |
|---|---|
| file | `2025.02.10_foldx_energy.csv.gz` |
| host | `https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/` |
| size | **1.5 GB** gzipped |
| rows | **208,792,558** across 20,437 UniProt accessions |
| columns | `uniprot_accession, uniprot_position, alphafold_fragment_id, alphafold_fragment_position, wild_type, mutated_type, foldx_ddg, plddt` |
| licence | CC BY 4.0 |
| method | FoldX v5 on AlphaFold2 models |
| sorted by | accession — so a stream can stop early, as for AlphaMissense |

## 3. The blocker

**`ftp.ebi.ac.uk` does not connect from this sandbox.**

```
URLError: <urlopen error [SSL: UNEXPECTED_EOF_WHILE_READING] EOF occurred in violation of protocol>
curl: http 000 after 10.07 s
```

Measured on 3 November 2026, repeatedly, on both `urllib` and `curl`, with and without a range
header. It is **host-specific, not a general network problem**: `www.ebi.ac.uk` returns 200 in under
a second from the same shell. The same failure class hit ERDA (the RaSP proteome set) earlier in
this project, so it is probably egress filtering on this environment rather than anything at EBI.

**It is not permanent.** The host was reachable on **28 October 2026**, when a prior session
downloaded the full 1.5 GB file and extracted the JAK family from it
(commit `0817a8325`). That extract is what route 2 reads.

## 4. Three ways round it, and why the script does what it does

### Route 1 — stream from source (preferred, currently failing)

```python
with urllib.request.urlopen(req, timeout=30) as fh:
    for line in gzip.GzipFile(fileobj=fh):
        if f[0] == acc:  found[...] = ...
        elif found:      break      # sorted, the block has ended
```

gzip has no random access, so the ESM-1b range-request trick does not apply. But the file is
sorted by accession, so the stream stops once past the target — the same pattern as
[`build_alphamissense.py`](build_alphamissense.py). **This is the route that works for an
arbitrary protein**, and the only reason the script is not simply a file reader.

### Route 2 — the committed extract (what ran today)

[`external_data/protvar_foldx_jak_src.csv`](../../external_data/protvar_foldx_jak_src.csv),
89,927 variants across JAK1, JAK2, JAK3, TYK2 and SRC, of which **20,349 are JAK2**. Pulled from
the archive above, same version stamp (2025.02.10), carrying per-position pLDDT.

This is **an extract of the same file, not a different dataset** — the values are identical by
construction. The script reports which route it used, and the `source` column in the output CSV
records it per row.

### Route 3 — mutfunc (verified identical, but unusable at scale)

mutfunc returns a `pred_ddg` column which **is the same FoldX number**. Checked on JAK1 across the
range, including a clash artefact
([`JAK1/clustering/verify_mutfunc_ddg.py`](../../JAK1/clustering/verify_mutfunc_ddg.py)):

| variant | pLDDT | ProtVar FoldX | mutfunc `pred_ddg` |
|---|--:|--:|--:|
| G1068W | 97.8 | **72.5022** | **72.5022** |
| E667M | 96.4 | −6.1182 | −6.1182 |
| A1005G | 96.2 | 1.1230 | 1.1230 |
| A1005S | 96.2 | 0.9601 | 0.9601 |
| A146E | 67.3 | 0.8096 | 0.8096 |

Maximum absolute difference **0.000050**. Whether one sources the other, or both ran FoldX on the
same AlphaFold2 model, is not visible from outside and does not matter in use.

**Two reasons it is not the answer here.**

**Coverage.** mutfunc returned **6 of 12** requested JAK1 variants, and the misses are not explained
by model confidence: `G1068Y` and `G1068F` are absent at pLDDT 97.8 while `G1068W` at the *same
position* is present. Patchy per substitution, not per position, for reasons not visible from
outside. Roughly **8% against ProtVar's 94.6%** — about 1,700 of 21,508 variants for JAK2.

**No API.** mutfunc has no public interface: `/about` 404s and there is no download page. It is a
Dash app, so the only backend is `POST /_dash-update-component`, driven through the callback graph
read from `/_dash-dependencies`
([`JAK1/clustering/fetch_mutfunc.py`](../../JAK1/clustering/fetch_mutfunc.py)). That works, but it
is an undocumented internal endpoint on an academic server, and it would be an odd thing to depend
on for 8% of a feature we already have at 94.6%.

### Routes considered and rejected

- **ProtVar REST API** — `www.ebi.ac.uk/ProtVar/api/mapping/O60674` returns 200, but no documented
  endpoint serves the stability table, and `/api/v3/api-docs` 404s. Probed and abandoned rather
  than guessed at.
- **A different mirror** — none found for this file.
- **Recomputing FoldX locally** — FoldX is licensed software and not installed here; and the point
  is to use the same numbers JAK1 used.

## 5. Output

[`jak2_foldx.csv`](jak2_foldx.csv), 21,508 rows in the canonical order, columns
`index, variant, wt, pos, alt, foldx, plddt, source`.

| | |
|---|--:|
| populated | **20,349 (94.6%)** |
| range | −4.49 … **+69.53** |
| direction | **positive = destabilising** |
| pLDDT < 70 | 1,083 rows (5.3%) |
| missing | 61 positions, range 1–840 |

**Sign.** Positive is destabilising here — the **opposite** of this project's Rosetta ddG, where
ΔΔG = ΔG_WT − ΔG_mut. Both conventions appear in the same feature table. Getting it backwards has
happened twice in this project.

**The +69.53 maximum is a clash artefact, not a free energy** — the same phenomenon documented for
the Rosetta values in [`ddg_by_target_aa.md`](../../ddg_by_target_aa.md). Use ranks, or clip.

**The missing 1,159.** 61 positions, of which **1–38 is the whole N-terminus**: AlphaFold's
low-confidence region, which ProtVar trims. Those variants have ESM-1b, AlphaMissense, BLOSUM62 and
PolyPhen-2 but no FoldX, so Gower will compare them on the features they have.

**pLDDT is carried through** because ProtVar's 2025 file no longer filters on it. 5.3% of rows sit
below 70, where the underlying structure is unreliable and so is any ddG computed on it.

## 6. Timing

| route | time |
|---|---|
| route 1, stream from EBI | fails in ~10 s (unreachable); would be ~1–2 min when working, by analogy with AlphaMissense |
| route 2, committed extract | **< 1 s** |

## 7. What to do when the host returns

Nothing. `python3 build_foldx.py` tries route 1 first on every run. To confirm it is working:

```bash
python3 build_foldx.py --source     # source only, fails loudly instead of falling back
```

and to check the two routes agree, run both and diff `jak2_foldx.csv` — they should be identical,
since one is an extract of the other.
