# JAK2_V617F_20261015_161914 — JAK2 V617F, no template, MSA 512/8192 (all sequences), seeds 0–15, run on Google Colab A100

JAK2 V617F, no template, MSA 512/8192 (all sequences), seeds 0–15, run on Google Colab A100. Compare with wild type at the same depth: 16 seeds → 7 open, 7 closed, 2 next to FERM (JAK2_20261015_134643 + JAK2_20261015_161033).

Settings: MSA 512/8192, seeds 0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15, 15 recycles, mutations ['V617F'], no template. (conclusions.md written from the run files: the notebook's summary cell failed on Colab.)

Classification of the final recycle: ≤ 10 Å (JH1 RMSD after superposing JH2) from open (AF2), closed (closed JAK2 of experiment A) or
7T6F (JAK1 active dimer, mapped); otherwise next to FERM (FERM–JH1 < 55 Å, ≥ 10 JH1–JH2 contacts), detached JH1 (< 10 contacts) or other.

## Final states

| class | seeds |
|---|---|
| open | 16: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 |

## Per seed (final recycle; Å) and FERM–JH1 trajectory (recycles 1–15)

| seed | FERM–JH1 | vs open | vs closed | vs 7T6F | JH1–JH2 contacts | class | trajectory |
|--:|--:|--:|--:|--:|--:|---|---|
| 0 | 95.0 | 1.6 | 81.7 | 48.1 | 23 | open | 93 96 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 1 | 95.0 | 1.5 | 81.5 | 47.6 | 24 | open | 94 96 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 2 | 95.3 | 2.3 | 81.5 | 48.5 | 22 | open | 70 96 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 3 | 94.6 | 1.2 | 81.5 | 47.5 | 23 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 4 | 95.1 | 2.2 | 81.2 | 48.0 | 23 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 5 | 94.9 | 1.4 | 81.5 | 48.0 | 23 | open | 72 63 96 95 95 95 95 95 95 95 95 95 95 95 95 |
| 6 | 94.8 | 1.4 | 81.4 | 47.5 | 24 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 7 | 95.1 | 2.4 | 81.2 | 48.2 | 22 | open | 61 55 96 95 95 95 95 95 95 95 95 95 95 95 95 |
| 8 | 95.0 | 1.5 | 81.5 | 47.6 | 23 | open | 96 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 9 | 95.2 | 2.3 | 81.4 | 48.5 | 22 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 10 | 95.0 | 0.7 | 81.9 | 47.7 | 23 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 11 | 95.1 | 2.1 | 81.6 | 48.7 | 23 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 12 | 95.0 | 1.6 | 81.7 | 48.4 | 23 | open | 94 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 13 | 94.8 | 0.9 | 81.8 | 47.5 | 23 | open | 94 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 14 | 95.0 | 2.0 | 81.3 | 48.1 | 25 | open | 95 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 15 | 94.8 | 1.2 | 81.5 | 47.7 | 23 | open | 93 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
