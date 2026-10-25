# ddG pipeline — how to reproduce

Everything needed to recompute the dual-state PyRosetta ddG results in this repository.

**The molab notebooks are not the artifact.** Each sandbox's `notebook.py` is an empty 81-byte
marimo shell — the computation is `worker.py`, injected into the sandbox at deploy time and run as
a detached OS process. Saving notebook copies would preserve nothing, so the code is saved instead.

## Files

| file | what it does |
|---|---|
| `worker.py` | **the computation.** Fetches two structures, FastRelax with coordinate constraints, then for each position computes ddG for every substitution in both states. Writes JSONL incrementally. |
| `build_deploys.py` | recomputes what is still missing from the merged results and splits it evenly across however many boxes are listed, so it is safe to re-run whenever a box is added or replaced |
| `collect.py` | pulls new results from each box in gzip+base64 chunks (under the 1 MB output cap), merges and deduplicates, pushes to git |
| `cycle.py` | one supervision cycle: ensure each worker is alive, relaunch if not, collect, analyse |
| `watch_ddg2.sh` | the supervisor: polls every 2 min until workers launch, then 30-min cycles |
| `analyse_ddg.py` | regenerates `ddg_overnight.md` from the merged full-coverage results |
| `analyse_pairs.py` | compares ddG across structure pairs: correlations, ensembles, incremental value |
| `diagnose_clash.py` | **why the magnitudes are not energies.** Reproduces the protocol on selected variants, decomposes the score into terms, and re-runs with a mobile backbone. Output: `data/ddg/clash_diagnosis.json` |
| `notebook_clash_diagnosis.py` | the same diagnosis as a **marimo notebook**: open it on a molab box and run all. Installs PyRosetta if absent, caches the relax, renders a table and chart. See `conclusions_ddG_difference_feature.md` section 9 |
| `sample_TYK2.json`, `sample_JAK1.json` | the fixed 5,000-variant samples (seed 99) shared by every structure pair, so results are directly comparable and can be averaged per variant |
| `pair_assignments.json` | which structure pair ran where, and why |

## Protocol

Verified against PyRosetta's own published ddG tutorial (PagP set) to four decimals: **0.3590**
against their 0.3590768, and **0.6712** against their 0.6720891 excluding proline.

- FastRelax with coordinate constraints on each structure, cached to disk
- `mutate_residue(pose, pos, aa, pack_radius=8.0)`
- the **native is repacked identically**, so neither side is favoured
- sign convention ΔΔG = ΔG_WT − ΔG_mut, so **negative = destabilizing** (inverted from Rosetta)
- the WT repack is computed **once per position** and reused across that position's 19
  substitutions — exact, since the 8 Å shell is identical, and ~19× cheaper

The amplitudes are **not energies**: `diagnose_clash.py` measures the extreme values as ~100%
`fa_rep` (steric overlap), and a mobile backbone shrinks them 10-150x. A ddG of -3000 implies a
mutant scoring +311 REU, which no folded protein does. Rank the values; never quote them as kcal/mol.

## Running it

1. Create molab sandboxes. From a notebook page, the sandbox id is
   `[...document.querySelectorAll('iframe')].map(f=>new URL(f.src).host)` with the `-session`
   suffix stripped. The molab agent token is **account-scoped**, so one saved token works for any
   sandbox. Opening a dead notebook starts a fresh sandbox.
2. List them in `boxes.txt` as `<index> <sandbox-id> <name>`, one per line.
3. `python3 build_deploys.py` — writes one `deploy<index>.py` per box.
4. Run each `deploy<index>.py` in its sandbox via `execute-code`. It installs nothing; it writes
   `worker.py` and `jobs.json` and launches the worker detached.
5. `./watch_ddg2.sh` as a **tracked** background task.

## Things that will bite you

- **Sandboxes expire at ~4 h with HTTP 410.** Pull results every cycle; never leave them only in a
  sandbox. Two were lost that way on 2026-10-22.
- **Positions are processed in shuffled order** so partial output at any stopping point is an
  unbiased random sample rather than a biased prefix. This is what makes AUC valid at 40%
  completion.
- **Sandboxes restore cached state**, including a stale `/tmp/ddg/jobs.json`. Clear `/tmp/ddg`
  before redeploying a different job, and verify what `jobs.json` actually contains afterwards —
  a deploy that prints the right job can still be overwritten moments later.
- **`deploy<index>.py` files are keyed on the index in `boxes.txt`.** Reusing indices across
  campaigns silently reruns the previous campaign's jobs. This happened on 2026-10-23.
- **Probing a busy marimo kernel kills the running cell.** Workers run as detached OS processes
  (`start_new_session=True`) precisely so the kernel stays idle and safe to poll.
- **`nohup ... &` inside a tracked task does not survive** the task ending. Launch long-running
  local jobs with `subprocess.Popen(..., start_new_session=True)` and check the PPID is 1.
- **Clipping to [−10,10] costs ≈0.01 AUC.** Raw or rank-transformed values score slightly better;
  only the ordering is meaningful, since the extreme values are clash artefacts rather than
  energies.

## Credentials

No secrets are stored here. `collect.py` reads a GitHub token from a path outside the repo, and the
molab token is read from a local file at deploy time. Neither is ever written into a notebook, a
log, or this repository.
