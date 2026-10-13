# JAK2_20261013_173657: JAK2 conformations vs AlphaFold-open and Shan-closed

Generated automatically after the run (2026-10-13 21:16).

## Run
- Target: JAK2 (UniProt O60674), **full length**; model `model_1`, guided recycling with the tensor-copy fix; MSA 32/64.
- Recycles: **20**, seeds: **0,1,2,3,4** → 100 conformations (every recycle of every seed in `all/`).
- Metric domains (UniProt): JH2 545–809, JH1 849–1124; FERM 37–380.

## References
- **OPEN**: AlphaFold DB `AF-O60674-F1_open.pdb` (full length): JH2–JH1 distance 45.90 Å, FERM–JH1 93.8 Å.
- **CLOSED**: Shan et al. 2014 model (JH2–JH1 only): JH2–JH1 distance 40.88 Å.
- Open vs closed reference: JH1 position after superposing JH2 differs by **83.5 Å** (scale of the transition).

## Selected structure per seed (recycle chosen by the objective J)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | JH1 \| fit JH2 vs OPEN (Å) | JH1 \| fit JH2 vs CLOSED (Å) | JH2 / JH1 shape vs Shan (Å) |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 0 | 8 | 82.7 | 52.8 | 44.7 | 94.7 | 44.0 | 4.77 / 3.21 |
| 1 | 20 | 83.3 | 51.0 | 45.6 | 94.4 | 30.2 | 4.76 / 3.15 |
| 2 | 17 | 82.9 | 58.7 | 40.4 | 107.6 | 54.5 | 4.66 / 3.21 |
| 3 | 12 | 82.7 | 62.6 | 55.1 | 108.1 | 78.4 | 4.81 / 3.00 |
| 4 | 14 | 82.3 | 63.3 | 47.8 | 109.9 | 73.7 | 4.69 / 3.02 |

## All conformations
- Structurally intact (max consecutive Cα–Cα ≤ 4.5 Å): 76 of 100; pLDDT 58.1–83.3.
- JH2–JH1 distance 41.8–68.7 Å; FERM–JH1 16.9–56.3 Å.
- Closest to **CLOSED** (Shan): seed 1, recycle 17 — JH1 | fit JH2 25.3 Å (pLDDT 82.5).
- Closest to **OPEN** (AlphaFold): seed 1, recycle 5 — JH1 | fit JH2 82.8 Å (pLDDT 78.0).
- Within 15 Å of a reference's JH1 position (intact structures): open-like 0, closed-like 0.
- Pipeline selection (centroid-distance extremes): open = seed 4 (63.30 Å), closed = seed 1 (51.02 Å).

## Conclusions
- **5 of 5** selected structures have JH1 closer to its CLOSED (Shan) position than to its OPEN (AlphaFold) position.
- Domain shapes agree with Shan (JH2 4.66–4.81 Å, JH1 3.00–3.21 Å); differences are in the JH2/JH1 arrangement.
- No conformation reaches the closed arrangement (best 25.3 Å from Shan's JH1 position; the references differ by 83.5 Å).
- No conformation reaches the open (AlphaFold) arrangement (best 82.8 Å).
- Mean selected JH2–JH1 distance 57.7 Å vs open 45.9 / closed 40.9 Å; mean FERM–JH1 46.7 Å vs open 93.8 Å.
