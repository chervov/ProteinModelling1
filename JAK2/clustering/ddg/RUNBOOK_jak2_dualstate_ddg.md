# JAK2 dual-state ΔΔG — operational notes

Started **4 November 2026, 08:58 CET**, running locally. This supplies the three features the
clustering is missing (`ddg_closed`, `ddg_open`, `ddg_delta`), which is why
`jak2_clustering_v1_wo_ddg_oc` carries that name.

## What is running

PyRosetta dual-state ΔΔG over **all 21,508 JAK2 missense substitutions, twice** — once on each
model pair — for 43,016 ΔΔG pairs in total.

| job | closed | open | provenance |
|---|---|---|---|
| **JAK2P1** (first) | `pair1/jak2_pair1_closed_untemplated.pdb` | `pair1/jak2_pair1_open_untemplated.pdb` | one untemplated run, `JAK2_20261015_161033` |
| **JAK2P2** (second) | `pair2/jak2_pair2_closed_tmpl_ma-l9b1f.pdb` | `pair2/jak2_pair2_open_tmpl_af2.pdb` | templated; runs differ only in the template |

Pair 1 runs first because it is the recommended pair: both states from a single untemplated run,
so nothing differs between them except the conformation. Pair 2 is the sensitivity check — the two
closed models are only 1.53 Å apart, so a material change in ΔΔG_closed between them means the
feature is reporting on the model rather than on the protein.

## Where it runs, and why not molab

**Locally**, on 8 cores with 6 worker processes. The sandbox URL supplied for this run
(`sb-b9dd24b107a5d8e5`) returned **HTTP 410** — molab sandboxes expire at ~4 h and this one was
issued the previous evening. PyRosetta turned out to be installed locally
(`/opt/anaconda3/lib/python3.13/site-packages/pyrosetta`), which is strictly better for a job of
this length: no 4-hour expiry, no sandbox recovery, no browser in the loop. The trade is 6 workers
instead of 18, so it is slower but it cannot die at 4 h.

## Design

Reuses `pipeline/ddg/worker.py` unchanged except for two lines (`W`, and `NPROC` capped at 6 for
a 16 GB machine). The guarantees that matter, inherited from the overnight JAK1/TYK2 runs:

- **The WT repack is computed once per position per state** and reused across that position's 19
  substitutions — exact, since the 8 Å repack shell is identical, and ~19× cheaper.
- **Positions are processed in a pre-shuffled order** (`random.seed(42)`), so the partial set at
  **any** stopping point is an unbiased random sample, not a biased prefix. Any analysis of a
  partial run is therefore valid.
- **Results are appended as JSONL and fsync'd after every position**, so a kill loses at most one
  position.
- **The worker resumes** from whatever is already in the JSONL; re-running never recomputes.
- **Every 30 minutes a tracked supervisor** merges, deduplicates on `(pos, alt)`, writes
  `data/ddg/ddg_JAK2P{1,2}_all.json` and pushes. Nothing lives only on this machine.

### Sign convention

`ddg = dG_WT − dG_mut`, i.e. **negative = destabilising**, matching `pipeline/ddg/worker.py` and
the Jeanpierre convention used for JAK1. This is the *opposite* of FoldX and ProtVar, where
positive = destabilising. Getting this backwards once already cost an inverted AUC (0.26 instead
of 0.74) earlier in the project.

`delta = ddg_open − ddg_closed`.

## Pre-flight checks done

All four staged structures were verified residue-by-residue against the canonical O60674
sequence before launch: **1,132 Cα each, zero mismatches**. A silent off-by-one or a wrong chain
would have produced 21,508 plausible numbers for the wrong protein.

## Files

| path | what |
|---|---|
| `~/ddg_jak2/worker.py` | the worker (adapted from `pipeline/ddg/worker.py`) |
| `~/ddg_jak2/jobs.json` | both jobs, 1,132 shuffled positions each |
| `~/ddg_jak2/results_JAK2P{1,2}.jsonl` | append-only raw output |
| `~/ddg_jak2/JAK2P{1,2}_relaxed_{closed,open}.pdb` | cached FastRelax, computed once per state |
| `~/ddg_jak2/run.log` | worker log, with per-5-position progress and rate |
| `~/ddg_jak2/collect_jak2.py` | merge → `data/ddg/` → git push |
| `data/ddg/ddg_JAK2P{1,2}_all.json` | the committed results |
| `data/ddg/jak2_ddg_progress.json` | last snapshot's counts |

## Restarting by hand

```bash
cd ~/ddg_jak2
pgrep -f ddg_jak2/worker.py || nohup python3 -u worker.py >> run.log 2>&1 &
python3 collect_jak2.py          # merge + push once
```

The worker is idempotent: it skips any job with a `DONE_<gene>` flag and resumes any partial
shard from the JSONL.

## When it finishes

1. `python3 collect_jak2.py` for the final merge.
2. Build the three feature CSVs (`jak2_ddg_closed.csv`, `_open.csv`, `_delta.csv`) in the
   canonical variant order, as for every other feature in `JAK2/clustering/`.
3. Re-run the clustering **with 11 features** as `v2`, and compare against
   `jak2_clustering_v1_wo_ddg_oc` — on JAK1 these three were the weakest of the set and dropping
   them *improved* agreement with the paper, so the honest expectation is a small change.
4. Compare ΔΔG_closed between pair 1 and pair 2 as the model-sensitivity check.
