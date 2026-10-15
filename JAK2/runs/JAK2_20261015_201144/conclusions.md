# JAK2_20261015_201144 — JAK2 wild type, no template, MSA 256/1024, seeds 5–15, run on Google Colab A100

JAK2 wild type, no template, MSA 256/1024, seeds 5–15, run on Google Colab A100. With seeds 0–4 (all open) the open/closed fraction from 16 seeds.

Settings: MSA 256/1024, seeds 5,6,7,8,9,10,11,12,13,14,15, 15 recycles, mutations [], no template. (conclusions.md written from the run files: the notebook's summary cell failed on Colab.)

Classification of the final recycle: ≤ 10 Å (JH1 RMSD after superposing JH2) from open (AF2), closed (closed JAK2 of experiment A) or
7T6F (JAK1 active dimer, mapped); otherwise next to FERM (FERM–JH1 < 55 Å, ≥ 10 JH1–JH2 contacts), detached JH1 (< 10 contacts) or other.

## Final states

| class | seeds |
|---|---|
| open | 11: 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |

**Pooled with [JAK2_20261015_134817](../JAK2_20261015_134817) (5 seeds): 16 seeds** — open 16.

## Per seed (final recycle; Å) and FERM–JH1 trajectory (recycles 1–15)

| seed | FERM–JH1 | vs open | vs closed | vs 7T6F | JH1–JH2 contacts | class | trajectory |
|--:|--:|--:|--:|--:|--:|---|---|
| 5 | 94.7 | 1.5 | 81.4 | 47.7 | 26 | open | 94 94 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 6 | 94.8 | 2.0 | 81.6 | 48.7 | 26 | open | 94 94 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 7 | 94.8 | 1.4 | 81.6 | 47.9 | 23 | open | 95 94 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 8 | 94.9 | 0.8 | 81.9 | 47.3 | 23 | open | 95 94 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 9 | 94.9 | 1.0 | 81.8 | 47.3 | 23 | open | 95 94 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 10 | 94.9 | 2.7 | 81.2 | 48.3 | 23 | open | 95 94 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 11 | 94.8 | 1.7 | 81.4 | 48.0 | 24 | open | 94 94 95 94 95 95 95 95 95 95 95 95 95 95 95 |
| 12 | 94.8 | 0.6 | 82.0 | 47.7 | 24 | open | 94 94 95 94 95 95 95 95 95 95 95 95 95 95 95 |
| 13 | 94.6 | 2.4 | 81.4 | 48.9 | 24 | open | 94 94 94 95 94 95 95 95 95 95 94 95 95 95 95 |
| 14 | 94.8 | 2.9 | 81.3 | 49.0 | 25 | open | 95 94 94 95 95 95 95 95 95 95 95 95 95 95 95 |
| 15 | 94.7 | 0.9 | 81.6 | 47.6 | 25 | open | 95 94 94 95 94 95 95 95 95 95 94 95 95 95 95 |
