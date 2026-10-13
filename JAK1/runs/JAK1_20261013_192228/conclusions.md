# JAK1_20261013_192228: JAK1 conformations vs ModelArchive open (ma-a1sai) and closed (ma-l9b1f)

Generated automatically after the run (2026-10-14 00:02).

## Run
- Target: JAK1 (UniProt P23458), **full length**; model `model_1`, guided recycling with the tensor-copy fix; MSA 32/64.
- Recycles: **30**, seeds: **0,1,2,3,4,5,6,7,8,9** → 300 conformations (every recycle of every seed in `all/`).
- Metric domains (UniProt): JH2 583–855, JH1 875–1153; FERM 34–420.

## References
- **OPEN**: ModelArchive `ma-a1sai_Open_WT_JAK1.pdb` (full length): JH2–JH1 distance 46.05 Å, FERM–JH1 92.5 Å.
- **CLOSED**: ModelArchive `ma-l9b1f_Closed_WT_JAK1.pdb` (full length): JH2–JH1 distance 39.53 Å, FERM–JH1 40.1 Å.
- Open vs closed reference: JH1 position after superposing JH2 differs by **81.7 Å** (scale of the transition).

## Selected structure per seed (recycle chosen by the objective J)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | JH1 \| fit JH2 vs OPEN (Å) | JH1 \| fit JH2 vs CLOSED (Å) | JH2 / JH1 shape vs CLOSED (Å) |
|--:|--:|--:|--:|--:|--:|--:|--:|
| 0 | 22 | 80.5 | 54.9 | 54.6 | 104.6 | 41.0 | 3.04 / 0.89 |
| 1 | 28 | 81.5 | 56.0 | 47.9 | 106.2 | 43.7 | 2.13 / 0.79 |
| 2 | 13 | 81.4 | 54.1 | 54.0 | 102.8 | 32.2 | 2.30 / 0.72 |
| 3 | 14 | 80.9 | 56.2 | 43.0 | 105.7 | 38.7 | 2.44 / 0.79 |
| 4 | 9 | 82.0 | 56.8 | 50.2 | 106.5 | 42.8 | 1.89 / 0.87 |
| 5 | 26 | 80.8 | 58.3 | 43.8 | 106.5 | 43.4 | 2.68 / 0.88 |
| 6 | 24 | 81.7 | 55.8 | 44.4 | 104.7 | 37.5 | 1.36 / 0.86 |
| 7 | 24 | 81.5 | 54.4 | 55.5 | 104.2 | 40.0 | 3.61 / 0.85 |
| 8 | 20 | 80.5 | 55.6 | 54.2 | 105.1 | 40.2 | 3.78 / 0.71 |
| 9 | 14 | 80.8 | 55.4 | 43.2 | 104.7 | 35.8 | 2.50 / 0.80 |

## All conformations
- Structurally intact (max consecutive Cα–Cα ≤ 4.5 Å): 243 of 300; pLDDT 55.4–82.0.
- JH2–JH1 distance 42.5–69.5 Å; FERM–JH1 29.7–59.4 Å.
- Closest to **CLOSED** (ma-l9b1f): seed 2, recycle 1 — JH1 | fit JH2 16.3 Å (pLDDT 58.6).
- Closest to **OPEN** (ma-a1sai): seed 8, recycle 1 — JH1 | fit JH2 61.5 Å (pLDDT 57.1).
- Within 15 Å of a reference's JH1 position (intact structures): open-like 0, closed-like 0.
- Pipeline selection (centroid-distance extremes): open = seed 5 (58.31 Å), closed = seed 2 (54.05 Å).

## Conclusions
- **10 of 10** selected structures have JH1 closer to its CLOSED (ma-l9b1f) position than to its OPEN (ma-a1sai) position.
- Domain shapes vs the closed reference (JH2 1.36–3.78 Å, JH1 0.71–0.89 Å); differences are in the JH2/JH1 arrangement.
- No conformation reaches the closed arrangement (best 16.3 Å from the closed reference's JH1 position; the references differ by 81.7 Å).
- No conformation reaches the open (ma-a1sai) arrangement (best 61.5 Å).
- Mean selected JH2–JH1 distance 55.7 Å vs open 46.0 / closed 39.5 Å; mean FERM–JH1 49.1 Å vs open 92.5 Å.
