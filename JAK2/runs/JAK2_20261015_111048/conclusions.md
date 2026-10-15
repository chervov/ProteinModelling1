# JAK2_20261015_111048 — JAK2 experiment A_release3_msa-default

**Run on Google Colab (A100-SXM4 40 GB)** — repeat of experiment A from molab (run [JAK2_20261015_082903](../JAK2_20261015_082903), RTX PRO 6000) to compare the two platforms. Template-release test: is the closed JAK2 stable once the template is switched off? JAK1 closed model ma-l9b1f as template in recycles 1–3 only; from recycle 4 on the template masks are zero and the selected structure comes only from template-free recycles.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA model_1 default 512/5120; templates: ModelArchive ma-l9b1f (recycles 1–3 only). Run time 103 min (whole notebook incl. setup, Google Colab A100; ~11 compute units).

Template identity to JAK2: `{"aligned": 1087, "identical": 507, "identity_aligned": 0.466, "identity_vs_shorter": 0.448}`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |
| template ma-l9b1f (mapped) | 39.8 | 42.2 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | vs template ma-l9b1f | nearest |
|--:|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 14 | 86.0 | 39.0 | 44.1 | 81.9 | 6.7 | 3.6 | template ma-l9b1f |
| 1 | 8 | 86.1 | 39.1 | 44.5 | 81.7 | 6.3 | 3.4 | template ma-l9b1f |
| 2 | 4 | 86.0 | 39.5 | 44.0 | 82.2 | 7.3 | 2.9 | template ma-l9b1f |
| 3 | 4 | 86.1 | 39.4 | 44.0 | 82.1 | 7.1 | 2.8 | template ma-l9b1f |
| 4 | 4 | 86.0 | 39.5 | 44.4 | 82.0 | 6.9 | 2.7 | template ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 81.4 | 1 | 9 | 85.9 | 0 |
| Shan 2014 (closed, JH2–JH1) | 5.9 | 1 | 11 | 85.8 | 75 |
| template ma-l9b1f (mapped) | 1.5 | 1 | 1 | 85.6 | 75 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 | vs template ma-l9b1f |
|--:|--:|--:|--:|--:|--:|
| 1 (template) | 85.4 | 45.2 | 82.2 | 7.5 | 1.8 |
| 2 (template) | 86.1 | 43.8 | 82.0 | 7.1 | 2.6 |
| 3 (template) | 86.3 | 44.0 | 82.1 | 7.2 | 2.6 |
| 4 | 86.0 | 44.1 | 82.1 | 7.1 | 2.9 |
| 5 | 85.8 | 44.5 | 81.9 | 6.4 | 3.2 |
| 6 | 85.8 | 44.6 | 81.9 | 6.4 | 3.2 |
| 7 | 85.9 | 44.5 | 81.8 | 6.4 | 3.3 |
| 8 | 85.9 | 44.5 | 81.8 | 6.4 | 3.3 |
| 9 | 85.8 | 44.7 | 81.8 | 6.5 | 3.2 |
| 10 | 85.8 | 44.7 | 81.8 | 6.4 | 3.3 |
| 11 | 85.8 | 44.6 | 81.7 | 6.3 | 3.4 |
| 12 | 85.8 | 44.6 | 81.8 | 6.5 | 3.2 |
| 13 | 85.9 | 44.6 | 81.8 | 6.4 | 3.3 |
| 14 | 85.8 | 44.5 | 81.8 | 6.3 | 3.5 |
| 15 | 85.8 | 44.6 | 81.7 | 6.3 | 3.3 |

pLDDT 85.0–86.4; JH2–JH1 38.9–40.4 Å; FERM–JH1 43.6–45.9 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: template ma-l9b1f 75.

## Comparison with the same experiment on molab

| | molab (RTX PRO 6000) [JAK2_20261015_082903](../JAK2_20261015_082903) | Colab (A100) this run |
|---|---|---|
| pLDDT, selected | 85.6–86.2 | 86.0–86.1 |
| FERM–JH1 (Å), selected | 44.4–45.0 | 44.0–44.5 |
| JH2–JH1 (Å), selected | 39.0–39.3 | 39.0–39.5 |
| JH1 vs Shan JAK2 (Å), selected | 6.0–6.9 | 6.3–7.3 |
| JH1 vs template ma-l9b1f (Å), selected | 2.5–3.6 | 2.7–3.6 |
| JH1 vs open AF2 (Å), selected | 81.5–81.8 | 81.7–82.2 |
| FERM–JH1 range, all 75 conformations (Å) | 43.7–46.1 | 43.6–45.9 |
| nearest reference, all conformations | {'template ma-l9b1f (mapped)': 75} | {'template ma-l9b1f (mapped)': 75} |
| selected recycle per seed (0–4) | 4, 15, 14, 7, 4 | 14, 8, 4, 4, 4 |

Mean over seeds per recycle, molab / Colab:

| recycle | FERM–JH1 (Å) | vs Shan JAK2 (Å) | pLDDT |
|--:|---|---|---|
| 1 (template) | 45.4 / 45.2 | 7.1 / 7.5 | 85.4 / 85.4 |
| 2 (template) | 44.3 / 43.8 | 6.8 / 7.1 | 85.9 / 86.1 |
| 3 (template) | 44.1 / 44.0 | 7.1 / 7.2 | 86.1 / 86.3 |
| 4 | 44.7 / 44.1 | 6.5 / 7.1 | 85.8 / 86.0 |
| 5 | 45.0 / 44.5 | 6.2 / 6.4 | 85.7 / 85.8 |
| 6 | 44.8 / 44.6 | 6.3 / 6.4 | 85.7 / 85.8 |
| 7 | 44.9 / 44.5 | 6.2 / 6.4 | 85.8 / 85.9 |
| 8 | 44.9 / 44.5 | 6.3 / 6.4 | 85.7 / 85.9 |
| 9 | 44.8 / 44.7 | 6.4 / 6.5 | 85.6 / 85.8 |
| 10 | 44.9 / 44.7 | 6.4 / 6.4 | 85.7 / 85.8 |
| 11 | 45.0 / 44.6 | 6.3 / 6.3 | 85.6 / 85.8 |
| 12 | 44.9 / 44.6 | 6.4 / 6.5 | 85.5 / 85.8 |
| 13 | 44.7 / 44.6 | 6.3 / 6.4 | 85.6 / 85.9 |
| 14 | 44.6 / 44.5 | 6.3 / 6.3 | 85.8 / 85.8 |
| 15 | 44.7 / 44.6 | 6.6 / 6.3 | 85.7 / 85.8 |

## Interpretation

- **Colab reproduces the molab result.** Same state in every seed and every recycle: closed (FERM–JH1 43.6–45.9 Å vs 43.7–46.1 Å on molab), all 75 conformations nearest to the closed template, none near the open AF2 model.
- **Numbers agree to a few tenths of an Å:** per-recycle means of FERM–JH1 differ by ≤ 0.6 Å, distances to Shan's JAK2 by ≤ 0.6 Å, pLDDT by ≤ 0.3. The same drift towards Shan's JAK2 after the template is switched off is seen on both (7.1 → 6.3–6.6 Å on molab, 7.5 → 6.3 Å on Colab).
- Results are not bit-identical (different GPU, floating point; the selected recycles per seed differ), as expected. For a clear-cut (non-bistable) setting like this the platform does not matter: Colab runs can be pooled with molab runs.
- Colab notebook: [colab/JAK2_openfold_colab.ipynb](../../../colab/JAK2_openfold_colab.ipynb) (this run used the same code with experiment A settings and the GitHub push on).
