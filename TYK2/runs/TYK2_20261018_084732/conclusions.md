# TYK2_20261018_084732 — TYK2 WT_free_msa64-256_s0-7

TYK2 wild type, NO template, MSA 64/256, 8 seeds. Paired with TYK2_P982A_20261018_084539 (same settings, run at the same time in a second sandbox). Shallower-MSA follow-up to the 128/512 pair (TYK2_20261016_175018 / TYK2_P982A_20261017_181325), where wild type and P982A were both entirely extended (FERM–JH1 ~93 Å). An earlier attempt at this pair (2026-10-17 evening) was lost when both sandboxes were terminated overnight.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time ~80 min (whole notebook incl. setup, molab).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 4 | 80.2 | 52.9 | 40.3 | 42.2 | AF2 |
| 1 | 4 | 80.6 | 50.5 | 56.5 | 61.7 | AF2 |
| 2 | 5 | 80.5 | 50.2 | 56.1 | 64.7 | AF2 |
| 3 | 4 | 81.0 | 53.9 | 77.1 | 92.0 | AF2 |
| 4 | 14 | 80.6 | 48.6 | 87.4 | 89.3 | AF2 |
| 5 | 4 | 80.1 | 56.1 | 34.2 | 46.4 | AF2 |
| 6 | 12 | 80.2 | 49.8 | 57.3 | 58.9 | AF2 |
| 7 | 5 | 80.3 | 48.8 | 51.1 | 51.1 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 26.3 | 7 | 3 | 78.3 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 69.3 | 54.4 | 53.1 |
| 2 | 76.9 | 31.0 | 43.5 |
| 3 | 79.2 | 44.7 | 45.4 |
| 4 | 80.4 | 50.2 | 55.5 |
| 5 | 80.3 | 56.0 | 63.4 |
| 6 | 80.0 | 55.2 | 64.1 |
| 7 | 79.9 | 58.7 | 65.6 |
| 8 | 80.2 | 61.2 | 67.5 |
| 9 | 80.1 | 59.3 | 64.7 |
| 10 | 80.2 | 60.7 | 67.1 |
| 11 | 80.2 | 58.4 | 66.1 |
| 12 | 80.3 | 56.9 | 63.2 |
| 13 | 80.1 | 65.7 | 72.4 |
| 14 | 80.1 | 63.0 | 69.0 |
| 15 | 80.1 | 65.3 | 70.9 |

pLDDT 68.0–81.0; JH2–JH1 29.4–56.5 Å; FERM–JH1 10.6–91.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 51 11 38 40 49 43 45 54 47 45 47 46 66 49 49 | closed-like (< 50) |
| 1 | 61 35 49 56 60 62 60 61 60 62 59 58 61 59 60 | intermediate |
| 2 | 58 32 46 48 56 65 66 73 63 77 73 64 75 71 72 | intermediate |
| 3 | 48 42 72 77 81 83 89 87 85 86 84 84 87 83 87 | open-like (> 80) |
| 4 | 63 32 47 52 58 60 60 61 59 68 61 57 74 87 92 | open-like (> 80) |
| 5 | 54 27 31 34 38 18 37 42 46 35 29 37 48 36 47 | closed-like (< 50) |
| 6 | 49 35 47 52 54 57 58 57 59 60 59 57 60 61 61 | intermediate |
| 7 | 51 35 27 43 51 55 55 55 55 53 55 53 56 58 55 | intermediate |

## Comparison with P982A at 64/256 (TYK2_P982A_20261018_084539, same settings)

| | median FERM–JH1 | range | median JH2–JH1 | compact (< 60 Å) | extended (> 80 Å) |
|---|--:|--:|--:|--:|--:|
| **wild type** | 56.3 | 34.2–87.4 | 50.4 | 6/8 | 1/8 |
| P982A | 85.6 | 46.0–94.2 | 48.9 | 3/8 | 5/8 |

Mann-Whitney on the selected FERM–JH1 values: p = 0.19. Fisher's exact test on compact counts: p = 0.31.

**Conclusion: 64/256 is the first depth at which TYK2 wild type is mostly compact, and P982A points towards the extended state, but 8 seeds per arm cannot confirm it.**

- Wild type: 6/8 seeds compact (selected FERM–JH1 34–57 Å), 1/8 extended (87 Å), seed 3 at 77 Å and still rising. At 128/512 all 8 wild-type seeds were extended (~93 Å), so the MSA depth switch for TYK2 lies between 64/256 and 128/512, one step shallower than for JAK3 (between 128/512 and 256/1024).
- P982A: 5/8 extended (85–94 Å), 3/8 compact (46–53 Å). Median FERM–JH1 85.6 vs 56.3 Å for wild type.
- The direction matches JAK3 M592F at its compact depth (more seeds pushed into the extended arrangement), but the difference is not significant with n = 8 per arm (Mann-Whitney p = 0.19; Fisher on compact counts p = 0.31).

Next: seeds 8–15 for both wild type and P982A at 64/256 (16 per arm, as for the JAK3 mutants). If the current proportions hold at 16 per arm (extended 2/16 vs 10/16), Fisher's test on extended counts would give p ≈ 0.009; on compact counts (12/16 vs 6/16) only p ≈ 0.07.
