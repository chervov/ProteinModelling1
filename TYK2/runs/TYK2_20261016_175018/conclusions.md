# TYK2_20261016_175018 — TYK2 WT_free_msa128-512_s0-7

TYK2 wild type, NO template, MSA 128/512, 8 seeds. Reordered to run first after the 4OLI release test showed no dynamic range: with 4OLI released at recycle 3 all 16 seeds stayed 1.4-1.9 A from the template through every recycle (run TYK2_20261016_130845), so the template assay cannot discriminate wild type from a mutant. This asks the cleaner question instead - where does TYK2 go unaided? Note AF2 TYK2 (FERM-JH1 39.7, JH2-JH1 37.2) and 4OLI (JH2-JH1 39.0) are both compact, so free prediction plausibly reaches the experimental closed state by itself.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 128 clusters / 512 extra; no template. Run time 84 min (whole notebook incl. setup, RTX PRO 6000).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 11 | 82.0 | 46.6 | 93.7 | 81.9 | AF2 |
| 1 | 6 | 81.9 | 46.5 | 93.4 | 82.0 | AF2 |
| 2 | 11 | 82.0 | 46.6 | 93.8 | 82.2 | AF2 |
| 3 | 7 | 82.2 | 46.6 | 93.5 | 82.1 | AF2 |
| 4 | 12 | 82.1 | 46.6 | 93.2 | 82.1 | AF2 |
| 5 | 4 | 82.0 | 46.7 | 93.5 | 82.5 | AF2 |
| 6 | 12 | 82.1 | 46.6 | 93.8 | 82.1 | AF2 |
| 7 | 7 | 82.1 | 46.7 | 93.7 | 82.2 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 24.7 | 1 | 1 | 74.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 74.1 | 31.0 | 35.8 |
| 2 | 80.5 | 83.8 | 79.3 |
| 3 | 81.8 | 93.9 | 83.2 |
| 4 | 81.9 | 93.5 | 82.0 |
| 5 | 81.8 | 93.5 | 82.0 |
| 6 | 81.8 | 93.5 | 82.1 |
| 7 | 82.0 | 93.7 | 82.2 |
| 8 | 81.8 | 93.6 | 82.1 |
| 9 | 81.8 | 93.6 | 82.3 |
| 10 | 81.8 | 93.6 | 82.1 |
| 11 | 81.9 | 93.8 | 82.2 |
| 12 | 81.9 | 93.5 | 82.0 |
| 13 | 81.7 | 93.4 | 81.7 |
| 14 | 81.8 | 93.4 | 82.0 |
| 15 | 81.7 | 93.5 | 82.0 |

pLDDT 73.3–82.2; JH2–JH1 29.5–49.2 Å; FERM–JH1 14.7–94.5 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 35 74 94 93 94 94 94 94 94 94 94 93 93 94 94 | open-like (> 80) |
| 1 | 30 68 94 93 94 93 94 94 94 93 94 94 94 93 94 | open-like (> 80) |
| 2 | 26 94 94 94 94 94 94 93 94 94 94 94 94 94 94 | open-like (> 80) |
| 3 | 15 94 94 94 94 93 94 94 94 94 94 93 93 93 93 | open-like (> 80) |
| 4 | 20 92 94 94 94 93 94 93 93 94 94 93 93 93 93 | open-like (> 80) |
| 5 | 60 94 94 94 94 94 94 94 94 94 94 94 94 94 94 | open-like (> 80) |
| 6 | 40 61 94 93 93 94 94 94 94 94 94 94 93 93 93 | open-like (> 80) |
| 7 | 21 93 93 94 93 94 94 94 94 94 94 94 93 93 93 | open-like (> 80) |
