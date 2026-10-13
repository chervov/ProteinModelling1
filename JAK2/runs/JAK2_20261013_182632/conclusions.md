# JAK2_20261013_182632: JAK2 conformations vs AlphaFold-open and Shan-closed

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
| 0 | 11 | 83.2 | 51.8 | 47.6 | 91.9 | 71.4 | 4.67 / 3.16 |
| 1 | 18 | 82.4 | 52.7 | 52.4 | 91.5 | 47.7 | 4.69 / 3.15 |
| 2 | 6 | 82.4 | 55.1 | 47.7 | 97.9 | 72.8 | 4.69 / 3.11 |
| 3 | 16 | 83.0 | 54.0 | 46.2 | 97.6 | 70.8 | 4.69 / 3.12 |
| 4 | 13 | 82.7 | 57.9 | 44.7 | 97.5 | 76.9 | 4.66 / 3.12 |

## All conformations
- Structurally intact (max consecutive Cα–Cα ≤ 4.5 Å): 64 of 100; pLDDT 60.4–83.2.
- JH2–JH1 distance 34.1–68.4 Å; FERM–JH1 16.0–58.9 Å.
- Closest to **CLOSED** (Shan): seed 3, recycle 7 — JH1 | fit JH2 39.9 Å (pLDDT 82.5).
- Closest to **OPEN** (AlphaFold): seed 4, recycle 2 — JH1 | fit JH2 66.3 Å (pLDDT 76.3).
- Within 15 Å of a reference's JH1 position (intact structures): open-like 0, closed-like 0.
- Pipeline selection (centroid-distance extremes): open = seed 4 (57.92 Å), closed = seed 0 (51.81 Å).

## Conclusions
- **5 of 5** selected structures have JH1 closer to its CLOSED (Shan) position than to its OPEN (AlphaFold) position.
- Domain shapes agree with Shan (JH2 4.66–4.69 Å, JH1 3.11–3.16 Å); differences are in the JH2/JH1 arrangement.
- No conformation reaches the closed arrangement (best 39.9 Å from Shan's JH1 position; the references differ by 83.5 Å).
- No conformation reaches the open (AlphaFold) arrangement (best 66.3 Å).
- Mean selected JH2–JH1 distance 54.3 Å vs open 45.9 / closed 40.9 Å; mean FERM–JH1 47.7 Å vs open 93.8 Å.

## Earlier runs in this campaign

| run | recycles | seeds | closest to CLOSED (Å) | closest to OPEN (Å) | selected closer to CLOSED |
|--|--:|--|--:|--:|--:|
| JAK2_20261013_173657 | 20 | 0,1,2,3,4 | 25.3 | 82.8 | 5/5 |
