# JAK2 V617F vs wild type — no template, MSA 128/512

V617F (JH2, at the JH2–JH1 autoinhibitory interface) is the most common activating JAK2 mutation in myeloproliferative
neoplasms. Both series: OpenFold model_1, guided recycling, no template, MSA 128/512, 15 recycles; wild type seeds 0–14
([JAK2_20261015_134222](runs/JAK2_20261015_134222)), V617F seeds 0–15 ([JAK2_V617F_20261015_162017](runs/JAK2_V617F_20261015_162017)).
Classification of the final recycle: ≤ 10 Å (JH1 RMSD after superposing JH2) from open (AF2), closed (closed JAK2 of experiment A)
or 7T6F (JAK1 cryo-EM active dimer, mapped); otherwise 'next to FERM' (FERM–JH1 < 55 Å and ≥ 10 JH1–JH2 contacts), 'detached JH1'
(< 10 JH1–JH2 residue contacts) or 'other' (JH1 packed on JH2 in another position).

## Result

| final state | wild type (15) | **V617F (16)** | Fisher p |
|---|--:|--:|--:|
| open | 1 | **6** | 0.083 |
| closed | 0 | 1 (8.9 Å) | |
| next to FERM, not closed | 1 | 3 | |
| JH1 on JH2, other position | 3 | 4 | |
| **detached JH1** | **10** | **2** | **0.003** |
| 7T6F-like | 0 | 0 | |

- **V617F largely removes the detached-JH1 intermediate** (10/15 → 2/16, p = 0.003): with the mutation JH1 is placed against
  JH2 (open, FERM-bound or other packed positions) instead of floating.
- More seeds reach the open state (1 → 6, p = 0.083); one seed ends near the closed state (8.9 Å).
- Unlike JAK1 V658F, no JAK2 seed adopts the 7T6F-like (JAK1 active-dimer) arrangement at this depth.
- More depths are running (V617F 64/256, 96/384 on molab; 512/8192 and 256/1024 on Colab; wild type extra seeds).

## Per seed (final recycle; Å)

| seed | WT: FERM–JH1 / vs open / vs closed / contacts → class | V617F: FERM–JH1 / vs open / vs closed / contacts → class |
|--:|---|---|
| 0 | 49.7 / 88.9 / 21.9 / 19 → **next to FERM (not closed)** | 62.0 / 80.9 / 44.4 / 71 → **other** |
| 1 | 60.4 / 88.3 / 43.4 / 30 → **other** | 66.8 / 70.4 / 84.2 / 3 → **detached JH1** |
| 2 | 64.4 / 74.1 / 85.6 / 2 → **detached JH1** | 49.1 / 89.2 / 18.4 / 22 → **next to FERM (not closed)** |
| 3 | 72.0 / 72.2 / 95.1 / 0 → **detached JH1** | 58.3 / 87.9 / 41.2 / 27 → **other** |
| 4 | 59.2 / 83.8 / 88.5 / 6 → **detached JH1** | 95.3 / 1.8 / 83.1 / 16 → **open** |
| 5 | 60.3 / 77.0 / 83.7 / 2 → **detached JH1** | 95.5 / 7.6 / 85.9 / 11 → **open** |
| 6 | 94.6 / 0.7 / 81.9 / 25 → **open** | 61.3 / 86.5 / 43.4 / 31 → **other** |
| 7 | 60.7 / 85.4 / 91.7 / 12 → **other** | 55.1 / 88.2 / 36.6 / 39 → **other** |
| 8 | 56.7 / 89.5 / 34.1 / 24 → **other** | 51.3 / 89.0 / 22.9 / 25 → **next to FERM (not closed)** |
| 9 | 60.7 / 84.6 / 91.3 / 7 → **detached JH1** | 52.3 / 87.0 / 19.0 / 23 → **next to FERM (not closed)** |
| 10 | 55.4 / 80.6 / 80.8 / 2 → **detached JH1** | 94.5 / 0.9 / 81.7 / 23 → **open** |
| 11 | 59.0 / 78.6 / 84.2 / 1 → **detached JH1** | 94.5 / 1.4 / 81.5 / 25 → **open** |
| 12 | 61.5 / 77.5 / 86.1 / 1 → **detached JH1** | 94.4 / 2.0 / 81.2 / 26 → **open** |
| 13 | 55.9 / 80.3 / 81.9 / 1 → **detached JH1** | 48.6 / 84.5 / 8.9 / 29 → **closed** |
| 14 | 56.0 / 82.3 / 85.7 / 7 → **detached JH1** | 56.3 / 80.1 / 81.1 / 2 → **detached JH1** |
| 15 | – | 94.6 / 1.0 / 81.7 / 24 → **open** |
