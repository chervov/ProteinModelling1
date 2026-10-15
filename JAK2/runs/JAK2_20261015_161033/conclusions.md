# JAK2_20261015_161033 — JAK2 wild type, no template, MSA 512/8192 (all sequences), seeds 5–15, run on Google Colab A100

JAK2 wild type, no template, MSA 512/8192 (all sequences), seeds 5–15, run on Google Colab A100. With seeds 0–4 the closed fraction at deep MSA from 16 seeds.

Settings: MSA 512/8192, seeds 5,6,7,8,9,10,11,12,13,14,15, 15 recycles, mutations [], no template. (conclusions.md written from the run files: the notebook's summary cell failed on Colab.)

Classification of the final recycle: ≤ 10 Å (JH1 RMSD after superposing JH2) from open (AF2), closed (closed JAK2 of experiment A) or
7T6F (JAK1 active dimer, mapped); otherwise next to FERM (FERM–JH1 < 55 Å, ≥ 10 JH1–JH2 contacts), detached JH1 (< 10 contacts) or other.

## Final states

| class | seeds |
|---|---|
| open | 5: 5, 6, 8, 9, 14 |
| closed | 5: 10, 11, 12, 13, 15 |
| next to FERM (not closed) | 1: 7 |

**Pooled with [JAK2_20261015_134643](../JAK2_20261015_134643) (5 seeds): 16 seeds** — open 7, closed 7, next to FERM (not closed) 2.

## Per seed (final recycle; Å) and FERM–JH1 trajectory (recycles 1–15)

| seed | FERM–JH1 | vs open | vs closed | vs 7T6F | JH1–JH2 contacts | class | trajectory |
|--:|--:|--:|--:|--:|--:|---|---|
| 5 | 94.9 | 1.8 | 81.5 | 48.2 | 23 | open | 81 96 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 6 | 95.2 | 1.5 | 81.7 | 48.1 | 22 | open | 65 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 7 | 49.3 | 85.2 | 11.4 | 88.6 | 31 | next to FERM (not closed) | 57 50 49 50 49 49 49 49 49 48 49 49 49 49 49 |
| 8 | 95.1 | 1.2 | 81.7 | 47.7 | 22 | open | 64 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 9 | 95.4 | 2.0 | 81.7 | 48.7 | 22 | open | 57 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 10 | 49.6 | 84.2 | 8.9 | 87.3 | 33 | closed | 53 50 49 49 49 48 49 49 49 48 49 48 49 49 50 |
| 11 | 44.9 | 81.9 | 0.8 | 82.7 | 43 | closed | 49 46 45 46 46 46 45 45 45 45 45 45 45 45 45 |
| 12 | 46.9 | 83.2 | 4.6 | 85.2 | 34 | closed | 57 49 50 49 49 49 47 47 47 47 47 46 47 47 47 |
| 13 | 47.0 | 82.6 | 3.6 | 84.4 | 38 | closed | 58 50 49 48 46 46 46 46 46 46 46 46 46 46 47 |
| 14 | 95.1 | 1.3 | 81.7 | 47.9 | 21 | open | 52 95 95 95 95 95 95 95 95 95 95 95 95 95 95 |
| 15 | 47.9 | 82.8 | 3.8 | 84.5 | 34 | closed | 50 48 48 48 48 47 47 47 47 47 47 48 47 48 48 |
