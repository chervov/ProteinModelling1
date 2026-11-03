# Where the Rosetta ΔΔG in this directory came from

A signpost, not a duplicate. The three columns `ddg_closed`, `ddg_open` and `ddg_delta` used by the
JAK1 clustering were not computed here — they come from an overnight run on four molab CPU boxes,
22–23 October 2026, and are documented where the computation lives.

## Start here

**[`../../data/ddg/DDG_COMPUTATION_REPORT.md`](../../data/ddg/DDG_COMPUTATION_REPORT.md)** — the
protocol, the scripts, why the raw values are not free energies, and an index of every analysis of
them.

## The one-paragraph version

PyRosetta `ref2015`. Each structure relaxed once with FastRelax under coordinate constraints
(~35 min), then per position the wild type is repacked in an 8 Å shell and **that same repacked
reference is reused across all 19 substitutions** — exact, and ~19× cheaper. JAK1 was scored on
**Jeanpierre's own open and closed models**, so these are the paper's own quantity on the paper's
own structures: the most faithful feature in this directory, and the only one that did not have to
be substituted or approximated. All **21,926** substitutions, complete.

**ΔΔG = ΔG_WT − ΔG_mut, so negative = destabilising** — the opposite of FoldX in the same feature
table. Scored with the wrong sign `ddg_closed` appears to have AUC 0.26 against the EV1 clusters;
oriented correctly it is 0.74. That error has been made twice in this project.

## What to read, and for what

| question | document |
|---|---|
| How was it computed? What scripts? | [`data/ddg/DDG_COMPUTATION_REPORT.md`](../../data/ddg/DDG_COMPUTATION_REPORT.md) |
| The code itself | [`pipeline/ddg/`](../../pipeline/ddg/) — `worker.py` is the computation |
| How it was run overnight, and the failure modes | [`data/ddg/RUNBOOK.md`](../../data/ddg/RUNBOOK.md) |
| **Why are some values −3,000?** | [`ddg_by_target_aa.md`](../../ddg_by_target_aa.md) — the F/P/W/Y finding and its two mechanisms |
| Which column should I actually use? | [`build_rosetta_ddg_jak1_info.md`](build_rosetta_ddg_jak1_info.md) §3 — read `within_15` |
| QC on the dual-state columns | [`data/ddg/rosetta_dualstate_qc.md`](../../data/ddg/rosetta_dualstate_qc.md) |
| How these columns behave in the clustering | [`clustering_jak1_results.md`](clustering_jak1_results.md) §5–6 |

## The two things that matter when using these columns here

**The raw values carry a clash tail.** 26.9% of the TYK2 values fall below −10 and the minimum is
−3,048; `clash_diagnosis.json` shows the entire difference is the Lennard-Jones repulsive term in
those cases. The extremes concentrate in four target residues — **F, P, W, Y** — recovered
independently by k-means in both proteins on unrelated structure pairs, by **two different
mechanisms**: Trp/Tyr/Phe are the largest aromatics clashing in a minority of positions, while
proline is only 113 Å³ and is penalised near-uniformly because it has no backbone N–H and locks φ
near −60°. Volume explains r = −0.62 across all 20 residues, −0.84 with proline removed.

**And they do not help this clustering.** `ddg_delta` is inert — AUC 0.4966, p = 0.25 — and dropping
all three ΔΔG features gives the *closest* agreement with the paper of anything tried
(ARI 0.484 → 0.492). The two state-specific columns do discriminate at AUC ≈ 0.74, on a par with
FoldX at 0.72, but largely redundantly with it. They are not blank; they are superfluous here.
