# Overnight ddG run - operational notes (2026-10-22 21:25)

## What is running
Dual-state PyRosetta ddG for **TYK2 on the matched AF3 pair** and then **JAK1 on Jeanpierre's
own open/closed models**, across 4 molab CPU boxes (20 cores, 172 GB each).

| box | sandbox | shard | status at launch |
|---|---|---|---|
| box3 | sb-71d2926a648eb0a5 | TYK2 shard 0 + JAK1 shard 0 | kernel blocked by an earlier relax; retried each cycle |
| box4 | sb-55f1bd4930605189 | TYK2 shard 1 + JAK1 shard 1 + 1/3 of shard 0 | running |
| box5 | sb-89533ba213dad84e | TYK2 shard 2 + JAK1 shard 2 + 1/3 of shard 0 | running |
| box6 | sb-8c8acb38bb9602ad | TYK2 shard 3 + JAK1 shard 3 + 1/3 of shard 0 | running |

Shard 0 is covered by boxes 4-6 as a trailing `TYK2B` job, so **all 22,536 TYK2 variants are
reachable even if box3 never revives**. Duplicates are harmless: the merge deduplicates on
(pos, alt).

## Design, and the failure modes it guards against
- **Workers are detached OS processes** (`start_new_session=True`), not marimo cells. The kernel
  stays idle, so polling it cannot kill the run. (Probing a *busy* kernel kills the running cell -
  this is why box3 is blocked.)
- **Sandboxes expire at ~4h with HTTP 410.** Every 30-min cycle pulls new results to
  `/Users/chervov/ddg_overnight/` and pushes the merged files to git, so nothing lives only in a
  sandbox. Two sandboxes were lost this way earlier in the project.
- **Positions are processed in shuffled order**, so the partial set at any stopping point is an
  unbiased random sample, not a biased prefix. This is what makes AUC against the DMS valid even
  if a box dies at 40%.
- **Results are appended as JSONL and fsync'd** after every position.
- **A transient probe failure is not death.** molab returns intermittent 530s; only 3 consecutive
  failures mark a box down, and a down box needs a fresh URL from the user.
- **A dead worker with an incomplete shard is relaunched** automatically; `jobs.json` is refreshed
  on every redeploy, and a redeploy refuses to start a second copy.
- The WT repack is computed **once per position** and reused across that position's 19
  substitutions. Exact (identical 8 A shell), ~19x cheaper.

## Files
| path | what |
|---|---|
| `~/watch_ddg.sh` | supervisor: 24 cycles, 30 min apart (must run as a *tracked* background task) |
| `~/cycle.py` | one cycle: ensure alive -> relaunch if needed -> collect -> analyse |
| `~/collect.py` | incremental pull (gzip+base64 chunks, under the 1 MB output cap), merge, git push |
| `~/analyse_ddg.py` | regenerates `ddg_overnight.md` and pushes it |
| `~/boxes.txt` | shard index, sandbox id, name |
| `~/ddg_overnight/state.json` | per-box lines already retrieved + consecutive failure count |
| `~/ddg_overnight/ddg_{TYK2,JAK1}_all.json` | merged, deduplicated results |

## Restarting by hand
    cd /Users/chervov && python3 cycle.py          # one cycle
    python3 analyse_ddg.py                         # just the report
The supervisor must be launched as a tracked background task - `nohup ... &` detaches it and it
will never wake Claude.

## If a box is dead
A new sandbox URL + token is required from the user. Then edit `~/boxes.txt` with the new sandbox
id and run `python3 cycle.py`; the worker is self-healing and will re-relax and resume from
whatever is already in its JSONL.
