# Overnight plan, 15–16 Oct 2026 (started ~18:00 CEST)

All runs: OpenFold model_1, guided recycling, **no template, 15 recycles**. Each run pushes to `<TARGET>/runs/<run>/`
with conclusions.md (per-seed trajectories, comparison with references); the main summary
(`conclusions_<datetime>.md`) is updated after each notable result.
Main question: **does the activating mutation (JAK1 V658F / JAK2 V617F) shift the balance between the open, closed and
7T6F-like (active-dimer) arrangements?**, plus more seeds for the JAK2 wild-type open/closed fraction.

| resource | queue (in order) |
|---|---|
| molab JAK1 (sb-976a…) | **V658F**: 128/512 (seeds 0–14, running since 17:34) → 96/384 (0–15) → 64/256 (0–15) → 32/64 (0–15) → 128/512 seed 15 → 512/8192 (0–15) |
| molab JAK2 (sb-05b7…) | **V617F**: 128/512 (0–15) → 64/256 (0–15) → 96/384 (0–15); then **WT** 64/256 (5–15) → WT 96/384 (5–15) |
| Colab A100 #1 | JAK2 **WT** 512/8192 (seeds 5–15) → WT 256/1024 (5–15) — with seeds 0–4 already done: 16 seeds per depth |
| Colab A100 #2 | JAK2 **V617F** 512/8192 (0–15) → V617F 256/1024 (0–7) |
| Colab L4 | JAK2 WT 64/256 (0–4, running) → WT 96/384 (0–4) |

Wild-type comparisons already available: JAK1 MSA scan ([JAK1/MSA_scan_summary.md](JAK1/MSA_scan_summary.md));
JAK2 no template: 512/8192 3 of 5 closed-like, 256/1024 all open, 128/512 (15 seeds) mostly in between.
molab sandboxes last ~7.5–8.5 h; runs not finished then continue on new notebooks.

## Update 21:20 — JAK2 molab sandbox shut down
The JAK2 molab sandbox (sb-05b7…) was shut down at 21:19 (HTTP 410), ~3 h after it was created, during V617F 64/256.
Done there: V617F 128/512 ([JAK2_V617F_20261015_162017](JAK2/runs/JAK2_V617F_20261015_162017)). The rest moved to Colab A100s,
queued after the current A100 jobs: V617F 64/256 (0–15), V617F 96/384 (0–15), WT 64/256 (5–15), WT 96/384 (5–15).

## Update 23:57 — JAK1 molab sandbox shut down; everything on Colab
The JAK1 molab sandbox (sb-976a…) was shut down at ~22:18, right after V658F 96/384 had been pushed. All remaining runs are on
Colab (max. 2 × A100 at once + L4):

| Colab lane | queue |
|---|---|
| A100 (lane 1) | JAK2 WT 256/1024 seeds 5–15 (running) → **JAK1 V658F 512/8192 (0–9)** → JAK2 V617F 64/256 (0–15) → JAK2 WT 64/256 (5–15) |
| A100 (lane 2) | JAK2 V617F 256/1024 (0–7, running) → JAK2 V617F 96/384 (0–15) → **JAK1 V658F 64/256 (0–15)** → JAK2 WT 96/384 (5–15) |
| L4 | JAK1 V658F 32/64 (0–4) |
