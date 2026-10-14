# JAK1_20261014_115803 — no template, whole MSA (512 clusters + 8192 extra)

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0–4, **no template**.
MSA: all 7390 sequences of the JAK1 MSA (ColabFold/MMseqs2): max_msa_clusters 512 (as in AF2 training),
max_extra_msa 8192 (model_1 default 5120 would leave ~1750 sequences out). Inference took 77 min (RTX PRO 6000).

## References (JH1 RMSD after superposing JH2, Å)
| | JH2–JH1 / FERM–JH1 (Å) | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan |
|---|---|---|---|---|---|
| AF2 AF-P23458-F1 | 46.3 / 92.2 | 0 | 3.4 | 81.0 | 82.5 |
| ma-a1sai (open) | 46.1 / 92.5 | | 0 | 81.7 | 82.9 |
| ma-l9b1f (closed) | 39.5 / 40.1 | | | 0 | 11.7 |
| Shan 2014 (closed, JH2–JH1) | 38.0 / – | | | | 0 |

## Our 75 conformations (5 seeds × 15 recycles)
| | vs AF2 | vs ma-a1sai | vs ma-l9b1f | vs Shan |
|---|---|---|---|---|
| closest (Å) | 1.8 | **0.5** | 81.1 | 82.5 |
| selected per seed (Å) | 3.2–4.6 | **1.0–2.3** | 81.4–82.2 | 82.7–83.4 |
| within 15 Å | 75/75 | 75/75 | 0 | 0 |

JH2–JH1 46.2–48.7 Å, FERM–JH1 92.4–96.3 Å, pLDDT 83.4–86.0: **open** in every seed and recycle.
Recycle 1 is less converged (9.6 Å from AF2, 7.1 Å from ma-a1sai); from recycle 2 on it stays 0.8–1.7 Å from ma-a1sai.

## Conclusions
- Without any template, the deep MSA alone gives the **open** JH2/JH1 arrangement, closest to Orianne's open
  model ma-a1sai (1.0–2.3 Å; even closer than to the AF2 DB model, 3.2–4.6 Å).
- No closed conformation appears (> 81 Å from ma-l9b1f and Shan).
- Earlier template-free runs with a **shallow** MSA (32 clusters / 64 extra) kept JH1 near FERM
  (FERM–JH1 ≤ 53–59 Å, lower pLDDT) and never came closer than 61.5 Å to the open state. So MSA depth decides
  the result: the deep MSA (strong coevolution signal) favours the open state; the shallow MSA gave
  closed-like / FERM-bound, less confident structures.
- Comparison with templates: the AF2 template (JAK1_20261014_095758) copied AF2 (open); for JAK2 the JAK1 closed
  template gave closed (JAK2_20261014_115511). With no template the network chooses open.
- Next: intermediate MSA depths (e.g. 64/256, 128/512, 256/1024) to find where the state switches, and/or
  the JAK1 closed template for JAK1 itself.
