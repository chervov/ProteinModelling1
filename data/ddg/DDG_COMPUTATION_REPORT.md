# Dual-state PyRosetta ΔΔG — how it was computed, and what the numbers do and do not mean

*Written 3 November 2026, after the fact, as a single entry point to a computation that is spread
across several directories. Everything here is sourced from the committed scripts and outputs, not
from recollection.*

**What exists:** near-complete saturation ΔΔG for two JAK-family proteins, each scored twice —
once in a closed structure and once in an open one. JAK1 is complete; TYK2 is 17 variants short.

| protein | variants | structures | run |
|---|--:|---|---|
| **TYK2** | 22,536 of 22,553 (99.92%, 1,187 positions) | matched AF3 closed/open pair | 22–23 Oct 2026 |
| **JAK1** | 21,926 — **complete**, 19 × 1,154 | **Jeanpierre's own open and closed models** | 22–23 Oct 2026 |

Outputs: [`data/ddg/ddg_TYK2_all.json`](ddg_TYK2_all.json),
[`data/ddg/ddg_JAK1_all.json`](ddg_JAK1_all.json), records of
`{pos, wt, alt, ddg_closed, ddg_open, delta}`.

---

## 1. The protocol

Per structure, once:

1. Fetch the PDB, score with Rosetta's full-atom `ref2015` function.
2. **FastRelax with coordinate constraints** — constraints applied through
   `CoordinateConstraintGenerator`, so the pose relaxes into the score function without drifting
   from the deposited geometry. ~35 min per structure.
3. Cache the relaxed pose to disk, so a restarted worker never repeats it.

Then, per position:

```python
# the WT repack is computed ONCE per position per state and reused across
# that position's 19 substitutions — exact, and ~19x cheaper
mutate_residue(p, pos, wt, pack_radius=8.0)
base[tag] = SF(p)
for w, alt in alts:
    mutate_residue(p, pos, alt, pack_radius=8.0)
    rec[f"ddg_{tag}"] = round(base[tag] - SF(p), 4)
rec["delta"] = round(rec["ddg_open"] - rec["ddg_closed"], 4)
```

The wild-type reference is **repacked identically to the mutant** — same 8 Å shell, same score
function — so the subtraction cancels everything outside that shell exactly rather than
approximately.

### Sign convention — the thing most likely to be got wrong

**ΔΔG = ΔG_WT − ΔG_mut, so negative = destabilising.** This is the paper's convention and the
opposite of FoldX, which sits in the same feature tables. Scored with the wrong sign, `ddg_closed`
appears to have AUC 0.26 against the JAK1 clusters; oriented correctly it is 0.74. That mistake has
been made twice in this project and caught both times.

### Validation

The protocol reproduces PyRosetta's published ddG tutorial (PagP set) to four decimals — 0.3590
against their 0.3590768, and 0.6712 against their 0.6720891 excluding proline
([`pipeline/ddg/README.md`](../../pipeline/ddg/README.md)).

## 2. How it was run — four molab boxes, overnight

22,536 + 21,926 variants with a ~35 min relax per structure does not fit in one session.
[`data/ddg/RUNBOOK.md`](RUNBOOK.md) is the operational record; the architecture guards against
failures that had already happened earlier in the project:

- **Workers are detached OS processes** (`start_new_session=True`), not marimo cells. The kernel
  stays idle, so polling it cannot kill the run. Probing a *busy* marimo kernel kills the running
  cell — that is how one box was lost.
- **Sandboxes expire at ~4 h with HTTP 410.** Every 30-minute cycle pulls results to local disk and
  pushes the merged file to git, so nothing lives only in a sandbox. Two had already been lost that
  way.
- **Positions are processed in shuffled order**, so a partial set at any stopping point is an
  unbiased random sample rather than a biased prefix.
- **Results are appended as JSONL and fsync'd** after every position.
- **Shards overlap deliberately** — shard 0 was also carried by three other boxes — so no single
  box being unrecoverable loses coverage. The merge deduplicates on `(pos, alt)`.

Progress is visible in the commit trail: `269999fba` (launch, 0 variants) → `d8cacda63` (JAK1 190) →
`6d31adbee` (JAK1 12,000) → `fa5d8294a` (JAK1 21,926, complete).

### The scripts

All in [`pipeline/ddg/`](../../pipeline/ddg/). **The molab notebooks are not the artifact** — each
sandbox's `notebook.py` is an empty 81-byte marimo shell, and the computation is `worker.py`,
injected at deploy time and run detached.

| script | role |
|---|---|
| [`worker.py`](../../pipeline/ddg/worker.py) | **the computation** — fetch, relax, ΔΔG for every substitution in both states, JSONL out |
| [`build_deploys.py`](../../pipeline/ddg/build_deploys.py) | recomputes what is still missing and splits it across however many boxes are live; safe to re-run |
| [`collect.py`](../../pipeline/ddg/collect.py) | pulls results in gzip+base64 chunks under the 1 MB output cap, merges, deduplicates, pushes |
| [`cycle.py`](../../pipeline/ddg/cycle.py) | one supervision cycle: check alive, relaunch, collect, analyse |
| [`watch_ddg2.sh`](../../pipeline/ddg/watch_ddg2.sh) | the supervisor — 2 min polling until launch, then 30 min cycles |
| [`analyse_ddg.py`](../../pipeline/ddg/analyse_ddg.py) | regenerates [`ddg_overnight.md`](../../ddg_overnight.md) |
| [`analyse_pairs.py`](../../pipeline/ddg/analyse_pairs.py) | ΔΔG across structure pairs: correlations, ensembles, incremental value |
| [`diagnose_clash.py`](../../pipeline/ddg/diagnose_clash.py) | the clash diagnosis below |
| [`notebook_clash_diagnosis.py`](../../pipeline/ddg/notebook_clash_diagnosis.py) | the same, as a runnable marimo notebook |

Reproducible without a sandbox: [`colab/tyk2_ddg_clash_diagnosis.ipynb`](../../colab/tyk2_ddg_clash_diagnosis.ipynb)
is Run-all in Colab, and downloads the already-relaxed pose from
[`TYK2_relaxed_closed.pdb.gz`](TYK2_relaxed_closed.pdb.gz) rather than spending 35 minutes on
FastRelax.

---

## 3. The raw values are not free energies

**26.9% of TYK2 values fall below −10 kcal/mol and the minimum is −3,048.** No thermodynamic
quantity looks like that. The cause is established rather than suspected:
[`clash_diagnosis.json`](clash_diagnosis.json) shows `frac_rep ≈ 1.0` for the extreme cases —
essentially the entire score difference is the Lennard-Jones **repulsive** term. A side chain is
being inserted into a backbone rigid enough that it cannot move out of the way.

Only the **ordering** is meaningful. Downstream work clips to ±10 and says so.

### The extreme values concentrate in four target residues: F, P, W, Y

Full analysis: **[`ddg_by_target_aa.md`](../../ddg_by_target_aa.md)**.

Sorting the 20 target residues by raw mean ΔΔG shows one dominant break, and **it is the same in
both proteins, scored on unrelated structure pairs**:

| protein | largest gap in sorted means | next largest | k-means on the 20 means |
|---|---|---|---|
| TYK2 | **65.9** between F (−124.4) and R (−58.5) | 34.6 | **FPWY** \| rest |
| JAK1 | **66.4** between F (−126.6) and R (−60.3) | 37.0 | **FPWY** \| rest |

k-means recovers the same four residues without being told where to cut.

### One group, two different mechanisms

**Trp, Tyr, Phe — steric.** The three largest aromatics, 228, 194 and 190 Å³. A bulky side chain
cannot be accommodated in a fixed backbone, so `fa_rep` dominates. Their raw *medians* are only −7
to −5: the mean is dragged down by a **minority of positions that clash catastrophically**, not by a
uniform penalty.

**Proline — backbone.** Only **113 Å³**, smaller than arginine (173) or leucine (167), both of which
sit comfortably in the low group. It arrives by a different route: no backbone N–H to donate a
hydrogen bond, and the ring locks φ near −60°, so it is incompatible with regular secondary
structure *wherever it lands*. Its raw median is **−190** against a mean of −178 — the penalty is
uniform, not a tail.

The volume correlation across all 20 residues is **r = −0.62**, but **−0.84 once proline is
excluded** — which is the quantitative signature of two mechanisms rather than one.

### Is the split biological? Largely not

Tested against the 22,553-variant TYK2 deep mutational scan, the FPWY group is worse on abundance
(median −0.099 vs −0.070, p = 9e−36) and at IFN-α 100 U/mL. But:

**at 1 U/mL the two groups are indistinguishable — 10.1% vs 10.0% loss of function, p = 0.74** —
while ΔΔG scores FPWY as roughly 4-fold worse by median and ~50-fold by raw mean. A group that the
energy function treats as catastrophic does not break the protein any more often at low stimulus.
**The split is mostly an artefact of the fixed backbone, not a statement about biology.**

## 4. Related analyses

| document | what it covers |
|---|---|
| **[`ddg_by_target_aa.md`](../../ddg_by_target_aa.md)** | the FPWY split, both mechanisms, and the DMS test above |
| [`rosetta_dualstate_qc.md`](rosetta_dualstate_qc.md) | QC on the dual-state columns; where clash contamination bites |
| [`conclusions_ddG_difference_feature.md`](../../conclusions_ddG_difference_feature.md) | §9 measures the repulsive fraction directly; §8.1 the volume correlation |
| [`ddg_overnight.md`](../../ddg_overnight.md) | the run's own summary, regenerated by `analyse_ddg.py` |
| [`JAK1/clustering/build_rosetta_ddg_jak1_info.md`](../../JAK1/clustering/build_rosetta_ddg_jak1_info.md) | how these columns enter the JAK1 clustering, and why `within_15` is the column to read |
| [`ddg_approximation.md`](ddg_approximation.md) · [`ddg_approximation_review.md`](ddg_approximation_review.md) | an analytic approximation attempted first, and why it was abandoned for real force-field work |
| [`external_data/ddg_benchmark_local.md`](../../external_data/ddg_benchmark_local.md) | ThermoMPNN vs RaSP vs ProtVar FoldX on 386 held-out human measurements |
| [`external_data/ddg_precomputed_human.md`](../../external_data/ddg_precomputed_human.md) | what can be downloaded instead of computed |

## 5. If you use these numbers

- **Clip to ±10 and say so.** Raw means are dominated by the clash tail.
- **Prefer ranks to values.** The ordering survives the clash contamination; the magnitudes do not.
- **Mind the sign.** Negative = destabilising here, positive = destabilising in FoldX.
- **`delta` (open − closed) is not a stability measure.** It is inert against the JAK1 clusters —
  AUC 0.4966, p = 0.25 — and dropping all three ΔΔG features *improves* agreement with the paper's
  clustering (ARI 0.484 → 0.492). The two state-specific columns do discriminate (AUC ≈ 0.74), but
  largely redundantly with FoldX.
- **Treat any FPWY substitution's magnitude with suspicion**, and proline's especially: its penalty
  is near-uniform and backbone-driven rather than position-specific.
