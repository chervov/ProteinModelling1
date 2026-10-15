# JAK2_20261015_082903 — JAK2 experiment A_release3_msa-default

Template-release test: is the closed JAK2 stable once the template is switched off? JAK1 closed model ma-l9b1f as template in recycles 1–3 only; from recycle 4 on the template masks are zero and the selected structure comes only from template-free recycles.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA model_1 default 512/5120; templates: ModelArchive ma-l9b1f (recycles 1–3 only). Run time 67 min (whole notebook incl. setup, RTX PRO 6000).

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
| 0 | 4 | 86.0 | 39.3 | 45.0 | 81.7 | 6.9 | 2.5 | template ma-l9b1f |
| 1 | 15 | 85.9 | 39.2 | 44.8 | 81.8 | 6.4 | 3.2 | template ma-l9b1f |
| 2 | 14 | 86.2 | 39.2 | 44.4 | 81.7 | 6.0 | 3.5 | template ma-l9b1f |
| 3 | 7 | 85.6 | 39.0 | 45.0 | 81.5 | 6.0 | 3.6 | template ma-l9b1f |
| 4 | 4 | 85.9 | 39.2 | 44.6 | 81.7 | 6.4 | 3.1 | template ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 81.5 | 0 | 8 | 85.8 | 0 |
| Shan 2014 (closed, JH2–JH1) | 5.9 | 2 | 10 | 85.8 | 75 |
| template ma-l9b1f (mapped) | 2.1 | 1 | 1 | 85.4 | 75 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 | vs template ma-l9b1f |
|--:|--:|--:|--:|--:|--:|
| 1 (template) | 85.4 | 45.4 | 82.0 | 7.1 | 2.3 |
| 2 (template) | 85.9 | 44.3 | 81.9 | 6.8 | 2.8 |
| 3 (template) | 86.1 | 44.1 | 82.1 | 7.1 | 2.7 |
| 4 | 85.8 | 44.7 | 81.7 | 6.5 | 2.9 |
| 5 | 85.7 | 45.0 | 81.6 | 6.2 | 3.3 |
| 6 | 85.7 | 44.8 | 81.7 | 6.3 | 3.2 |
| 7 | 85.8 | 44.9 | 81.7 | 6.2 | 3.4 |
| 8 | 85.7 | 44.9 | 81.6 | 6.3 | 3.3 |
| 9 | 85.6 | 44.8 | 81.7 | 6.4 | 3.3 |
| 10 | 85.7 | 44.9 | 81.7 | 6.4 | 3.2 |
| 11 | 85.6 | 45.0 | 81.7 | 6.3 | 3.3 |
| 12 | 85.5 | 44.9 | 81.7 | 6.4 | 3.3 |
| 13 | 85.6 | 44.7 | 81.7 | 6.3 | 3.3 |
| 14 | 85.8 | 44.6 | 81.7 | 6.3 | 3.3 |
| 15 | 85.7 | 44.7 | 81.8 | 6.6 | 3.1 |

pLDDT 84.9–86.3; JH2–JH1 39.0–40.0 Å; FERM–JH1 43.7–46.1 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: template ma-l9b1f 75.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–3 (template) | recycles 4–15 (no template) |
|---|---|---|
| 0 | 45 45 45 | 45 45 45 45 45 45 45 46 46 45 45 45 |
| 1 | 46 44 44 | 45 45 45 45 45 45 45 45 45 45 45 45 |
| 2 | 45 44 44 | 44 45 45 45 45 45 45 45 45 45 44 44 |
| 3 | 46 44 44 | 45 45 45 45 44 44 45 45 45 44 44 44 |
| 4 | 45 44 44 | 45 45 45 45 45 45 45 45 45 45 45 45 |

## Interpretation
- **The closed JAK2 is stable once the template is switched off.** All 5 seeds stay closed for the 12 template-free
  recycles: FERM–JH1 44–46 Å throughout (open would be ~94 Å), JH2–JH1 39.0–40.0 Å, and every one of the 75
  conformations is nearest to the closed template; none comes within 80 Å of the open AF2 model.
- **It is not a frozen copy:** without the template the structure stays 2.5–3.6 Å from ma-l9b1f and 6.0–6.9 Å from
  Shan's JAK2 model — as close to Shan as the run with the template in all recycles (JAK2_20261014_115511: 6.6–6.8 Å).
- **Confidence barely changes:** pLDDT ~85.7 without the template vs ~86.5 with it in all recycles.
- So with the default MSA (512/5120) the closed JAK2 is a self-consistent state for the network: once reached, the JAK2
  sequence and MSA keep it. (With no template at all the deep MSA gave open for JAK1, so the template is what brings it
  there; this run shows it does not need the template to stay there.)
