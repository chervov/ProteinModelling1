# JAK2_20261014_115511 — full MSA + JAK1 closed model (ma-l9b1f) as template

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0–4, full MSA (model_1 defaults 512/5120),
custom template = ModelArchive ma-l9b1f (JAK1 closed, Orianne et al.), aligned to JAK2 by kalign:
1087 of 1132 residues covered, 45% identical (54–56% in JH2/JH1). OpenFold's 90% identity check lowered to 0.3;
unaligned residues get no template coordinates. Inference took 61 min (RTX PRO 6000).

## References (JH1 RMSD after superposing JH2, Å)
| | JH2–JH1 / FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | vs template |
|---|---|---|---|---|
| AF2 AF-O60674-F1 (open) | 45.9 / 93.8 | 0 | 83.5 | 81.2 |
| Shan 2014 JAK2 (closed, JH2–JH1) | 40.9 / – | | 0 | 8.7 |
| template ma-l9b1f, mapped to JAK2 | 39.8 / 42.2 | | | 0 |

## Our 75 conformations (5 seeds × 15 recycles)
| | vs AF2 | vs Shan 2014 | vs template |
|---|---|---|---|
| closest (Å) | 81.6 | 6.5 | 1.6 |
| selected per seed (Å) | 81.7–81.9 | 6.6–6.8 | 2.6–3.1 |
| mean, recycle 1 → 15 (Å) | 82.4 → 81.9 | 7.9 → 6.9 | 1.8 → 2.9 |

JH2–JH1 39.2–40.6 Å, FERM–JH1 43.6–45.7 Å, pLDDT 84.6–86.7: **closed** in every seed and recycle.

## Conclusions
- The JAK1 closed template gives a **closed JAK2**: JH1 packed against FERM, as in the template.
  This is the first JAK2 run with a closed structure close to Shan's JAK2 model.
- The structure follows the template closely (2.6–3.1 Å), but over the recycles it drifts slightly away from it
  and **towards Shan's JAK2 model** (7.9 → 6.9 Å; the template itself is 8.7 Å from Shan). So the JAK2 sequence/MSA
  adjusts the arrangement rather than copying it exactly.
- pLDDT (~86.5) is lower than with the identical-sequence AF2 template (~94.7), but still high.
- The variation across seeds and recycles is small (< 1.5 Å), so again the template dominates.
  Together with the AF2-template run (JAK2_20261014_095758: open, copied AF2), this shows that the template decides
  open vs closed; on its own this does not tell which state the sequence prefers.
