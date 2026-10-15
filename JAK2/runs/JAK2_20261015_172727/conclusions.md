# JAK2_20261015_172727 — JAK2 wild type, no template, MSA 96/384, seeds 0–4, run on a Google Colab L4

JAK2 wild type, no template, MSA 96/384, seeds 0–4, run on a Google Colab L4. Baseline for JAK2 V617F at the same depth.

Settings: MSA 96/384, seeds 0,1,2,3,4, 15 recycles, mutations [], no template. (conclusions.md written from the run files: the notebook's summary cell failed on Colab.)

Classification of the final recycle: ≤ 10 Å (JH1 RMSD after superposing JH2) from open (AF2), closed (closed JAK2 of experiment A) or
7T6F (JAK1 active dimer, mapped); otherwise next to FERM (FERM–JH1 < 55 Å, ≥ 10 JH1–JH2 contacts), detached JH1 (< 10 contacts) or other.

## Final states

| class | seeds |
|---|---|
| next to FERM (not closed) | 4: 0, 1, 3, 4 |
| detached JH1 | 1: 2 |

## Per seed (final recycle; Å) and FERM–JH1 trajectory (recycles 1–15)

| seed | FERM–JH1 | vs open | vs closed | vs 7T6F | JH1–JH2 contacts | class | trajectory |
|--:|--:|--:|--:|--:|--:|---|---|
| 0 | 52.1 | 89.5 | 25.3 | 96.2 | 19 | next to FERM (not closed) | 44 53 58 55 53 54 55 51 54 53 51 50 52 52 52 |
| 1 | 49.0 | 88.8 | 18.4 | 93.5 | 18 | next to FERM (not closed) | 36 50 52 50 48 48 49 48 50 50 49 48 50 49 49 |
| 2 | 58.4 | 88.0 | 90.5 | 84.3 | 4 | detached JH1 | 43 51 59 58 58 62 59 61 60 61 60 60 61 61 58 |
| 3 | 50.1 | 87.0 | 16.0 | 91.6 | 18 | next to FERM (not closed) | 45 45 51 49 48 48 48 50 52 52 51 50 51 51 50 |
| 4 | 53.7 | 88.8 | 36.6 | 98.1 | 20 | next to FERM (not closed) | 44 48 53 52 52 52 50 50 52 52 51 51 56 51 54 |
