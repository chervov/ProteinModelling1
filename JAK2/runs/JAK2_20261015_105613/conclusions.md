# JAK2_20261015_105613 — JAK2 experiment B_release3_msa128-512

As experiment A (ma-l9b1f template in recycles 1–3 only, then switched off) with a shallower MSA (128 clusters / 512 extra).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 128 clusters / 512 extra; templates: ModelArchive ma-l9b1f (recycles 1–3 only). Run time 86 min (whole notebook incl. setup, RTX PRO 6000).

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
| 0 | 12 | 85.5 | 39.0 | 45.3 | 81.3 | 5.9 | 3.5 | template ma-l9b1f |
| 1 | 7 | 85.4 | 39.2 | 45.4 | 81.5 | 6.0 | 3.5 | template ma-l9b1f |
| 2 | 4 | 85.7 | 39.3 | 44.2 | 81.6 | 6.5 | 2.7 | template ma-l9b1f |
| 3 | 5 | 85.6 | 39.0 | 45.1 | 81.4 | 6.2 | 3.2 | template ma-l9b1f |
| 4 | 7 | 85.4 | 39.2 | 45.3 | 81.5 | 6.1 | 3.1 | template ma-l9b1f |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 81.2 | 0 | 6 | 85.3 | 0 |
| Shan 2014 (closed, JH2–JH1) | 5.7 | 3 | 6 | 85.4 | 75 |
| template ma-l9b1f (mapped) | 1.6 | 0 | 1 | 85.3 | 75 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 | vs template ma-l9b1f |
|--:|--:|--:|--:|--:|--:|
| 1 (template) | 85.3 | 45.6 | 81.8 | 7.4 | 1.7 |
| 2 (template) | 85.9 | 44.5 | 81.6 | 7.1 | 2.0 |
| 3 (template) | 86.3 | 44.1 | 81.9 | 7.4 | 2.0 |
| 4 | 85.4 | 44.5 | 81.7 | 6.8 | 2.6 |
| 5 | 85.4 | 45.0 | 81.5 | 6.1 | 3.2 |
| 6 | 85.4 | 45.1 | 81.3 | 6.0 | 3.4 |
| 7 | 85.4 | 45.3 | 81.4 | 6.0 | 3.3 |
| 8 | 85.2 | 45.2 | 81.4 | 6.1 | 3.3 |
| 9 | 85.2 | 44.8 | 81.5 | 6.2 | 3.3 |
| 10 | 85.3 | 45.1 | 81.4 | 6.1 | 3.3 |
| 11 | 85.3 | 44.7 | 81.5 | 6.1 | 3.4 |
| 12 | 85.4 | 45.0 | 81.3 | 6.0 | 3.4 |
| 13 | 85.2 | 45.0 | 81.6 | 6.2 | 3.2 |
| 14 | 85.3 | 45.1 | 81.5 | 6.2 | 3.2 |
| 15 | 85.3 | 45.1 | 81.6 | 6.4 | 3.0 |

pLDDT 85.0–86.5; JH2–JH1 38.9–40.0 Å; FERM–JH1 43.5–46.0 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: template ma-l9b1f 75.

## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–3 (template) | recycles 4–15 (no template) |
|---|---|---|
| 0 | 46 45 44 | 45 45 45 45 45 45 45 45 45 45 45 45 |
| 1 | 46 44 44 | 44 45 45 45 45 45 45 45 45 45 45 45 |
| 2 | 45 44 44 | 44 45 45 45 45 44 45 44 44 44 44 45 |
| 3 | 46 45 44 | 44 45 45 45 45 45 45 45 45 45 46 45 |
| 4 | 46 45 44 | 45 45 45 45 46 45 45 45 45 45 46 45 |

## Interpretation
- **Same answer as experiment A (default MSA): the closed JAK2 stays closed after the template is switched off, also
  with the shallower MSA (128/512).** All 5 seeds keep FERM–JH1 at 44–46 Å for the 12 template-free recycles; all 75
  conformations are nearest to the closed template, none within 80 Å of the open AF2 model.
- **Without the template the structure moves from the JAK1 template towards Shan's JAK2 model:** mean distance to the
  template grows from 1.7–2.0 Å (template recycles) to ~3.3 Å, while the distance to Shan's JAK2 drops from 7.4 to
  ~6.1 Å (selected structures 5.9–6.5 Å). So the JAK2 sequence/MSA adjusts the JAK1-derived arrangement towards the
  JAK2-specific one once the template no longer holds it.
- pLDDT 85.4–85.7 (selected), essentially the same as with the default MSA (experiment A: ~85.7).
- Contrast with JAK1 at the same MSA depth and no template at all (JAK1_20261015_082811): bistable, 2/5 seeds closed.
  Here, once started closed, JAK2 never opens: the closed state is self-consistent for JAK2 at both MSA depths tested.
- Note: this run was interrupted by a kernel restart; the detached inference finished, and the rerun of the notebook
  repeated the inference (fixed since by a done-marker watcher in the sandbox).
