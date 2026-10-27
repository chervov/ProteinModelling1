# JAK2 without template — closed, open and a detached-JH1 intermediate

Analysis of the JAK2 no-template runs (final recycle of each seed) against the references; JAK1 structures (ma-l9b1f, ma-a1sai,
cryo-EM 7T6F) are mapped onto JAK2 numbering by sequence alignment (JAK1–JAK2 identity 0.466). Script and data:
[intermediate_analysis/](intermediate_analysis/).

## Summary
- **JAK2 reaches the real closed state without any template** at the deepest MSA (512/8192): seed 0 is **0.7 Å** from the
  closed JAK2 obtained with the template (experiment A) and 2.7 Å from the JAK1 closed model ma-l9b1f; seed 2 is 5.0 Å; seed 3
  13 Å. The template-derived closed JAK2 is therefore a state the network also finds on its own.
- **The 'in-between' JAK2 structures (all 5 seeds at 64/256, 10 of 15 at 128/512) are a detached-JH1 arrangement**, not the
  7T6F-like active-dimer arrangement found for JAK1: 64–100 Å from every reference (including 7T6F mapped to JAK2), JH2–JH1
  centroid distance 48–60 Å (open 46, closed 40), and JH1 makes almost no contacts (0–7 residue pairs with JH2, none with
  FERM; open/closed: 22–41). JH1 itself is well folded (pLDDT ~89); only its placement is undefined.
- At 128/512 three seeds are partially closed (21–42 Å from the closed references, 19–30 JH1–JH2 contacts) and one is open.
- Difference to JAK1: at shallow MSA JAK1 adopts a defined third arrangement matching the active dimer 7T6F ([JAK1/JAK1_third.md](../JAK1/JAK1_third.md));
  JAK2 instead loses the JH1 placement.

## Geometry (Å; JH1 RMSD after superposing JH2)

| structure | FERM–JH1 | JH2–JH1 | vs open AF2 | vs closed JAK2 (exp. A) | vs ma-l9b1f (JAK1, mapped) | vs Shan JAK2 | vs 7T6F (JAK1, mapped) | JH1–JH2 contacts | JH1–FERM contacts |
|---|--:|--:|--:|--:|--:|--:|--:|--:|--:|
| AF2 JAK2 (open) | 93.8 | 45.9 | 0.0 | 81.7 | 81.2 | 83.5 | 47.3 | 25 | 0 |
| closed JAK2 (exp. A, seed 0) | 45.4 | 39.3 | 81.7 | 0.0 | 2.6 | 6.9 | 82.7 | 35 | 1 |
| ma-l9b1f (JAK1 closed, mapped) | 42.2 | 39.8 | 81.2 | 2.6 | 0.0 | 8.7 | 83.1 | 46 | 3 |
| 7T6F (JAK1 active dimer, mapped) | 84.4 | 44.7 | 47.3 | 82.7 | 83.1 | 83.2 | 0.0 | 15 | 0 |
| JAK1 third arrangement (mapped) | 83.5 | 44.1 | 46.2 | 80.7 | 81.1 | 81.3 | 4.8 | 15 | 0 |
| **512/8192 (no template)** | | | | | | | | | |
| 512/8192 seed 0 | 45.9 | 39.3 | 81.6 | 0.7 | 2.7 | 6.5 | 82.5 | 41 | 0 |
| 512/8192 seed 1 | 95.1 | 46.3 | 1.5 | 81.5 | 81.0 | 83.3 | 47.9 | 22 | 0 |
| 512/8192 seed 2 | 48.9 | 42.1 | 83.5 | 6.2 | 5.0 | 11.2 | 86.0 | 31 | 0 |
| 512/8192 seed 3 | 49.4 | 45.3 | 86.7 | 14.6 | 13.3 | 19.2 | 90.7 | 25 | 0 |
| 512/8192 seed 4 | 95.1 | 46.4 | 1.0 | 81.9 | 81.4 | 83.7 | 48.0 | 22 | 0 |
| **128/512 (no template)** | | | | | | | | | |
| 128/512 seed 0 | 49.7 | 47.9 | 88.9 | 21.9 | 20.5 | 26.6 | 94.6 | 19 | 0 |
| 128/512 seed 1 | 60.4 | 53.2 | 88.3 | 43.4 | 41.8 | 47.3 | 101.4 | 30 | 0 |
| 128/512 seed 2 | 64.4 | 48.6 | 74.1 | 85.6 | 85.7 | 88.0 | 75.2 | 2 | 0 |
| 128/512 seed 3 | 72.0 | 54.3 | 72.2 | 95.1 | 95.7 | 96.1 | 65.7 | 0 | 0 |
| 128/512 seed 4 | 59.2 | 53.6 | 83.8 | 88.5 | 89.0 | 90.0 | 76.8 | 6 | 0 |
| 128/512 seed 5 | 60.3 | 48.3 | 77.0 | 83.7 | 84.1 | 85.7 | 76.7 | 2 | 2 |
| 128/512 seed 6 | 94.6 | 46.3 | 0.7 | 81.9 | 81.3 | 83.6 | 47.4 | 25 | 0 |
| 128/512 seed 7 | 60.7 | 56.9 | 85.4 | 91.7 | 92.6 | 92.0 | 71.0 | 12 | 0 |
| 128/512 seed 8 | 56.7 | 51.7 | 89.5 | 34.1 | 32.6 | 38.5 | 99.0 | 24 | 0 |
| 128/512 seed 9 | 60.7 | 56.0 | 84.6 | 91.3 | 92.0 | 92.2 | 75.0 | 7 | 0 |
| 128/512 seed 10 | 55.4 | 48.2 | 80.6 | 80.8 | 81.3 | 82.4 | 79.3 | 2 | 0 |
| 128/512 seed 11 | 59.0 | 48.8 | 78.6 | 84.2 | 84.6 | 85.9 | 75.6 | 1 | 2 |
| 128/512 seed 12 | 61.5 | 49.5 | 77.5 | 86.1 | 86.5 | 87.8 | 74.4 | 1 | 0 |
| 128/512 seed 13 | 55.9 | 48.4 | 80.3 | 81.9 | 82.4 | 83.6 | 77.9 | 1 | 0 |
| 128/512 seed 14 | 56.0 | 50.5 | 82.3 | 85.7 | 86.0 | 87.4 | 74.1 | 7 | 0 |
| **64/256 (no template)** | | | | | | | | | |
| 64/256 seed 0 | 58.7 | 59.2 | 89.7 | 90.8 | 91.1 | 92.9 | 85.4 | 1 | 4 |
| 64/256 seed 1 | 63.7 | 59.9 | 87.1 | 95.4 | 95.8 | 97.0 | 77.8 | 0 | 4 |
| 64/256 seed 2 | 67.3 | 56.3 | 77.3 | 95.0 | 95.7 | 95.4 | 65.2 | 10 | 0 |
| 64/256 seed 3 | 61.5 | 58.7 | 85.9 | 93.5 | 93.8 | 95.2 | 81.1 | 4 | 3 |
| 64/256 seed 4 | 64.7 | 54.5 | 77.4 | 92.1 | 92.9 | 92.2 | 63.9 | 6 | 0 |

Runs: 512/8192 [JAK2_20261015_134643](runs/JAK2_20261015_134643), 128/512 [JAK2_20261015_134222](runs/JAK2_20261015_134222),
64/256 [JAK2_20261015_134839](runs/JAK2_20261015_134839).

## Caveats
- 5 seeds at 512/8192 and 64/256; the overnight runs add seeds (WT 512/8192 and 256/1024 seeds 5–15, 64/256 and 96/384) and
  the V617F mutant at all depths.
- Mapping JAK1 structures onto JAK2 uses a sequence alignment (47% identity); domain-level comparisons are robust to this.
