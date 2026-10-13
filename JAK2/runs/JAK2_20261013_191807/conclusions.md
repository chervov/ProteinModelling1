# JAK2_20261013_191807: JAK2 conformations vs AlphaFold-open and Shan-closed

Generated automatically after the run (2026-10-13 23:39).

## Run
- Target: JAK2 (UniProt O60674), **full length**; model `model_1`, guided recycling with the tensor-copy fix; MSA 32/64.
- Recycles: **30**, seeds: **0,1,2,3,4,5,6,7,8,9** → 300 conformations (every recycle of every seed in `all/`).
- Metric domains (UniProt): JH2 545–809, JH1 849–1124; FERM 37–380.

## References
- **OPEN**: AlphaFold DB `AF-O60674-F1_open.pdb` (full length): JH2–JH1 distance 45.90 Å, FERM–JH1 93.8 Å.
- **CLOSED**: Shan et al. 2014 model (JH2–JH1 only): JH2–JH1 distance 40.88 Å.
- Open vs closed reference: JH1 position after superposing JH2 differs by **83.5 Å** (scale of the transition).

## Selected structure per seed (recycle chosen by the objective J)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | JH1 \| fit JH2 vs OPEN (Å) | JH1 \| fit JH2 vs CLOSED (Å) | JH2 / JH1 shape vs Shan (Å) |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 0 | 24 | 82.8 | 63.1 | 44.1 | 109.7 | 77.6 | 4.82 / 3.09 |
| 1 | 17 | 82.8 | 61.0 | 46.1 | 106.7 | 76.9 | 4.80 / 3.03 |
| 2 | 22 | 83.2 | 59.4 | 44.0 | 109.6 | 61.8 | 4.69 / 3.07 |
| 3 | 24 | 82.5 | 60.0 | 44.0 | 108.0 | 66.6 | 4.79 / 3.09 |
| 4 | 22 | 82.5 | 60.4 | 46.3 | 109.0 | 69.0 | 4.79 / 3.01 |
| 5 | 26 | 82.7 | 62.1 | 48.6 | 106.4 | 80.8 | 4.80 / 3.11 |
| 6 | 26 | 82.1 | 63.0 | 47.2 | 109.3 | 78.0 | 4.81 / 3.03 |
| 7 | 24 | 78.9 | 63.8 | 41.5 | 112.5 | 72.1 | 4.74 / 3.09 |
| 8 | 11 | 79.0 | 63.3 | 43.1 | 109.8 | 75.1 | 4.77 / 3.10 |
| 9 | 19 | 82.1 | 60.9 | 46.4 | 110.0 | 67.9 | 4.83 / 3.19 |

## All conformations
- Structurally intact (max consecutive Cα–Cα ≤ 4.5 Å): 245 of 300; pLDDT 59.9–83.2.
- JH2–JH1 distance 40.9–80.2 Å; FERM–JH1 18.4–53.0 Å.
- Closest to **CLOSED** (Shan): seed 2, recycle 2 — JH1 | fit JH2 48.5 Å (pLDDT 74.0).
- Closest to **OPEN** (AlphaFold): seed 6, recycle 1 — JH1 | fit JH2 87.5 Å (pLDDT 61.1).
- Within 15 Å of a reference's JH1 position (intact structures): open-like 0, closed-like 0.
- Pipeline selection (centroid-distance extremes): open = seed 7 (63.81 Å), closed = seed 2 (59.39 Å).

## Conclusions
- **10 of 10** selected structures have JH1 closer to its CLOSED (Shan) position than to its OPEN (AlphaFold) position.
- Domain shapes agree with Shan (JH2 4.69–4.83 Å, JH1 3.01–3.19 Å); differences are in the JH2/JH1 arrangement.
- No conformation reaches the closed arrangement (best 48.5 Å from Shan's JH1 position; the references differ by 83.5 Å).
- No conformation reaches the open (AlphaFold) arrangement (best 87.5 Å).
- Mean selected JH2–JH1 distance 61.7 Å vs open 45.9 / closed 40.9 Å; mean FERM–JH1 45.1 Å vs open 93.8 Å.

## Earlier runs in this campaign

| run | recycles | seeds | closest to CLOSED (Å) | closest to OPEN (Å) | selected closer to CLOSED |
|--|--:|--|--:|--:|--:|
| JAK2_20261013_173657 | 20 | 0,1,2,3,4 | 25.3 | 82.8 | 5/5 |
| JAK2_20261013_182632 | 20 | 0,1,2,3,4 | 39.9 | 66.3 | 5/5 |
