# JAK3_M511I_20261018_173145 — JAK3 M511I_msa128-512_s8-15

JAK3 M511I, NO template, MSA 128/512, seeds 8-15: second half of JAK3_M511I_20261016_191613 (seeds 0-7), bringing M511I to 16 seeds like the other JAK3 mutants (M592F, A573V, A572V). M511I is a reported activating JAK3 mutation in the SH2-JH2 linker and the most frequent JAK3 hotspot in T-ALL. Paired with wild type JAK3_20261016_125830 (16 seeds, same depth).

Settings: OpenFold model_1, guided recycling, 15 recycles x seeds 8,9,10,11,12,13,14,15; MSA 128 clusters / 512 extra; no template. The first attempt in this sandbox failed at once (a leftover TYK2.fasta from an earlier TYK2 run in the shared fasta/ folder made the runner try to predict TYK2 with no matching alignment); the file was moved aside and the run restarted. Run time ~65 min.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P52333-F1) | 38.3 | 41.5 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 9 | 84.0 | 38.1 | 41.5 | 2.0 | AF2 |
| 9 | 15 | 83.7 | 45.2 | 44.5 | 14.7 | AF2 |
| 10 | 12 | 83.6 | 38.5 | 42.9 | 1.7 | AF2 |
| 11 | 13 | 83.8 | 47.3 | 45.7 | 20.6 | AF2 |
| 12 | 15 | 84.1 | 63.0 | 54.5 | 91.5 | AF2 |
| 13 | 13 | 83.2 | 38.5 | 42.3 | 1.4 | AF2 |
| 14 | 9 | 84.0 | 61.4 | 54.4 | 88.5 | AF2 |
| 15 | 13 | 83.7 | 38.5 | 42.7 | 1.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P52333-F1) | 1.0 | 13 | 7 | 82.8 | 67 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 77.5 | 44.3 | 58.2 |
| 2 | 83.2 | 57.7 | 42.7 |
| 3 | 83.5 | 49.3 | 33.2 |
| 4 | 83.5 | 46.5 | 27.9 |
| 5 | 83.1 | 46.0 | 27.8 |
| 6 | 83.3 | 46.6 | 27.8 |
| 7 | 83.4 | 46.7 | 27.6 |
| 8 | 83.4 | 46.2 | 28.1 |
| 9 | 83.5 | 46.0 | 26.9 |
| 10 | 83.5 | 45.3 | 27.8 |
| 11 | 83.3 | 46.0 | 27.7 |
| 12 | 83.5 | 45.4 | 27.1 |
| 13 | 83.6 | 45.8 | 27.4 |
| 14 | 83.3 | 45.3 | 26.6 |
| 15 | 83.7 | 45.4 | 26.9 |

pLDDT 75.7–84.1; JH2–JH1 20.5–64.4 Å; FERM–JH1 18.2–66.8 Å. (JAK3 open/closed: open ~94 A, compact/closed ~42-56 A; see the JAK3 depth-profile conclusions.)
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 18 51 45 44 42 42 42 42 41 42 42 42 42 42 42 | closed-like (< 50) |
| 9 | 24 54 45 44 44 44 45 44 44 43 44 44 45 44 45 | closed-like (< 50) |
| 10 | 61 57 45 43 43 43 43 43 43 43 43 43 43 43 44 | closed-like (< 50) |
| 11 | 50 60 50 47 45 45 46 46 46 44 46 45 46 44 44 | closed-like (< 50) |
| 12 | 60 63 57 56 53 55 54 55 53 54 55 53 53 54 54 | intermediate |
| 13 | 52 54 45 42 42 42 42 42 42 42 43 43 42 42 42 | closed-like (< 50) |
| 14 | 45 67 62 52 56 56 58 53 54 52 51 50 52 51 51 | intermediate |
| 15 | 44 55 45 44 44 44 44 44 44 43 43 43 43 42 42 | closed-like (< 50) |

## Combined: JAK3 wild type vs M511I at 128/512, 16 seeds per arm

Runs: wild type JAK3_20261016_125830 (16 seeds); M511I JAK3_M511I_20261016_191613 (seeds 0–7) +
JAK3_M511I_20261018_173145 (seeds 8–15). Selected FERM–JH1 per seed (Å):

| | seeds 0–7 | seeds 8–15 | median | < 50 Å |
|---|---|---|--:|--:|
| wild type | 43 56 55 52 46 52 56 44 | 54 55 43 44 54 44 54 45 | 51.9 | 7/16 |
| M511I | 53 53 54 53 45 53 55 53 | 42 45 43 46 55 42 54 43 | 52.9 | 7/16 |

M511I vs wild type: Mann-Whitney p = 0.44; Fisher on counts below 50 Å p = 1.00.

**Conclusion: M511I has no detectable effect on JAK3's FERM–JH1 arrangement at 128/512.** Both arms are compact in
all 32 seeds (41–56 Å, versus ~94 Å for the open arrangement) with identical medians and identical counts below 50 Å.
This matches A573V/A572V being subtle and contrasts with M592F, which pushed 5/16 seeds fully open (p = 0.011).

**Batch heterogeneity, this time in the mutant arm.** M511I's two halves differ (1/8 vs 6/8 below 50 Å,
Mann-Whitney p = 0.083) while wild type's halves agree (3/8 vs 4/8, p = 0.64). The second half also contains four
seeds within 2.0 Å of the AF2 model (67 of its 120 conformations are within 15 Å), whereas the first half came no
closer than 22 Å. Two 8-seed batches of the same condition, run two days apart on different sandboxes, landed in
noticeably different places; the pooled 16-seed comparison is the one to quote, not either half.

This is the third instance of batch-to-batch spread in this campaign (after JAK3 A572V and TYK2 wild type at 64/256),
and here it is large enough to have produced a spurious "more compact" result had only seeds 8–15 been run.
Where the pooled arms agree as closely as they do here, the null is solid.
