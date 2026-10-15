# JAK2_20261015_134643 — JAK2 experiment JAK2_notemplate_msa512-8192

JAK2 no-template MSA-depth scan (does JAK2 close on its own, like JAK1 at 128/512?). OpenFold model_1, guided recycling, no template. MSA 512 clusters / 8192 extra (all 7738 sequences).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4; MSA 512 clusters / 8192 extra; no template. Run time 119 min (whole Colab session incl. setup, Google Colab A100).

Template identity to JAK2: `null`

## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |
| Shan 2014 (closed, JH2–JH1) | 40.9 | nan |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | vs Shan 2014 | nearest |
|--:|--:|--:|--:|--:|--:|--:|---|
| 0 | 13 | 85.0 | 39.5 | 45.6 | 81.8 | 6.9 | Shan 2014 |
| 1 | 8 | 86.3 | 46.4 | 95.1 | 2.1 | 83.3 | AF2 |
| 2 | 13 | 85.2 | 43.8 | 48.0 | 85.6 | 15.6 | Shan 2014 |
| 3 | 8 | 85.2 | 45.7 | 49.6 | 87.1 | 19.1 | Shan 2014 |
| 4 | 7 | 86.4 | 46.1 | 94.7 | 1.2 | 83.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.7 | 4 | 14 | 86.1 | 27 |
| Shan 2014 (closed, JH2–JH1) | 6.5 | 0 | 15 | 84.9 | 16 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 | vs Shan 2014 |
|--:|--:|--:|--:|--:|
| 1 | 83.4 | 63.4 | 83.1 | 46.2 |
| 2 | 84.7 | 67.4 | 60.0 | 46.9 |
| 3 | 85.4 | 67.5 | 52.6 | 45.8 |
| 4 | 85.4 | 67.5 | 51.4 | 42.7 |
| 5 | 85.5 | 67.2 | 51.5 | 42.8 |
| 6 | 85.4 | 66.8 | 51.5 | 41.5 |
| 7 | 85.6 | 66.8 | 51.9 | 42.8 |
| 8 | 85.6 | 66.5 | 51.9 | 42.5 |
| 9 | 85.4 | 66.6 | 51.1 | 41.9 |
| 10 | 85.4 | 66.6 | 51.6 | 42.2 |
| 11 | 85.5 | 66.4 | 51.8 | 42.5 |
| 12 | 85.4 | 66.5 | 51.7 | 42.1 |
| 13 | 85.5 | 66.5 | 51.2 | 41.0 |
| 14 | 85.3 | 66.7 | 50.8 | 40.9 |
| 15 | 85.5 | 66.9 | 50.9 | 40.8 |

pLDDT 83.0–86.4; JH2–JH1 39.3–51.6 Å; FERM–JH1 45.0–95.6 Å (open AF2 93.8 Å, closed ma-l9b1f mapped to JAK2 42.2 Å; FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: Shan 2014 47, AF2 28.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~94, closed ~42)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 60 49 46 46 46 46 45 45 45 46 45 45 46 46 46 | closed-like (< 50) |
| 1 | 68 96 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 2 | 68 51 50 50 50 48 48 48 48 48 48 48 48 49 49 | closed-like (< 50) |
| 3 | 57 50 51 51 50 50 50 50 50 49 49 49 49 49 49 | closed-like (< 50) |
| 4 | 65 91 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |

## Interpretation
- **JAK2 closes without any template, even with the deepest MSA (all 7738 sequences).** 3 of 5 seeds end next to
  FERM (FERM–JH1 45–50 Å from recycle 2–3 on) and stay there for all 15 recycles; **seed 0 is 6.9 Å from Shan's
  closed JAK2 model** — as close as the template-based closed JAK2 runs (6.0–7.3 Å). Seeds 2 and 3 are closed-like
  but further from Shan (15.6, 19.1 Å). Seeds 1 and 4 are open (1.2–2.1 Å from AF2).
- **Unlike JAK1:** JAK1 was open in every seed at 512/8192, 256/1024 and 160/640 and closed only at 128/512.
  For JAK2 at 256/1024 all 5 seeds were open ([JAK2_20261015_134817](../JAK2_20261015_134817)), so the closed
  fraction is not monotonic in MSA depth at 5 seeds — more seeds are needed.
- pLDDT is similar for closed (85.0–85.2) and open (86.3–86.4) seeds.
- Structure comparison ([JAK2_intermediate.md](../../JAK2_intermediate.md)): seed 0 is 0.7 Å from the closed JAK2 of experiment A and 2.7 Å from ma-l9b1f (mapped) — the same closed state as with the template; seed 2 5.0 Å, seed 3 13 Å.
