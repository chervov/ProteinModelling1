# TYK2_V678F_20261018_204500 — TYK2 V678F_free_msa32-64_s8-15 (rebuilt from backup)

TYK2 V678F at MSA 32/64, seeds 8-15, no template: second half of TYK2_V678F_20261018_183849, giving 16 seeds at the one TYK2 depth with a reproducible wild-type baseline. The sandbox kernel was lost mid-run (a monitoring request disconnected and marimo interrupted it); the OpenFold process was reparented to init, finished all 8 seeds, and this folder was rebuilt from the monitor's incremental backup. Every recycle of every seed is present; there is no pipeline selection_report.json or selected open/closed structure.

Settings: OpenFold model_1, guided recycling, 15 recycles x seeds 8-15; MSA 32 clusters / 64 extra; no template.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 13 | 79.3 | 51.5 | 52.6 | 64.6 | AF2 |
| 9 | 14 | 77.5 | 57.5 | 39.5 | 50.3 | AF2 |
| 10 | 11 | 71.7 | 52.1 | 49.1 | 60.3 | AF2 |
| 11 | 13 | 78.6 | 50.1 | 51.8 | 27.5 | AF2 |
| 12 | 11 | 78.4 | 48.1 | 51.0 | 44.3 | AF2 |
| 13 | 12 | 75.0 | 54.7 | 42.3 | 53.0 | AF2 |
| 14 | 12 | 74.6 | 55.4 | 51.8 | 59.3 | AF2 |
| 15 | 13 | 78.2 | 50.0 | 52.8 | 48.5 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 27.2 | 11 | 12 | 78.1 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 55.2 | 41.0 | 74.5 |
| 2 | 62.9 | 48.4 | 76.8 |
| 3 | 67.9 | 54.4 | 62.5 |
| 4 | 71.5 | 50.8 | 57.5 |
| 5 | 72.4 | 48.5 | 48.9 |
| 6 | 74.1 | 48.1 | 46.1 |
| 7 | 74.8 | 48.7 | 46.8 |
| 8 | 75.2 | 50.8 | 48.3 |
| 9 | 75.4 | 48.7 | 47.3 |
| 10 | 75.0 | 47.5 | 49.8 |
| 11 | 76.1 | 48.7 | 47.9 |
| 12 | 76.4 | 49.5 | 50.3 |
| 13 | 76.4 | 48.6 | 50.2 |
| 14 | 75.9 | 48.5 | 51.6 |
| 15 | 75.7 | 49.8 | 52.6 |

pLDDT 45.4–79.3; JH2–JH1 41.7–63.9 Å; FERM–JH1 21.9–65.9 Å (FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 45 54 56 47 40 44 44 50 47 48 48 51 53 51 55 | intermediate |
| 9 | 45 54 56 50 40 40 40 40 43 38 41 39 40 40 41 | closed-like (< 50) |
| 10 | 48 44 53 50 47 47 53 51 50 51 49 54 50 51 52 | intermediate |
| 11 | 22 42 49 41 41 41 47 51 52 59 56 53 52 53 53 | intermediate |
| 12 | 45 51 53 48 48 48 50 53 49 48 51 51 51 53 51 | intermediate |
| 13 | 49 48 57 57 63 58 55 55 48 40 43 42 42 41 42 | closed-like (< 50) |
| 14 | 34 48 60 66 62 64 55 57 53 51 50 52 49 49 50 | closed-like (< 50) |
| 15 | 40 47 50 48 45 43 45 50 48 47 51 54 53 50 56 | intermediate |

## Positive control at 32/64: wild type vs V678F vs P982A, 15–16 seeds per arm

Runs: wild type `TYK2_20261018_135623` + `TYK2_20261018_153027`; P982A `TYK2_P982A_20261018_135623` +
`TYK2_P982A_20261018_153019`; V678F `TYK2_V678F_20261018_183849` + `TYK2_V678F_20261018_204500`.

| | n | median FERM–JH1 | range | open (> 80 Å) | median JH2–JH1 | range |
|---|--:|--:|---|--:|--:|---|
| wild type | 15 | 45.2 | 38.4–52.3 | 0/15 | 49.3 | 41.4–60.2 |
| P982A | 15 | 42.4 | 36.4–53.9 | 0/15 | 53.5 | 43.7–63.3 |
| **V678F** | 16 | 49.9 | 38.7–52.8 | **0/16** | **55.0** | 40.4–60.7 |

vs wild type (Mann-Whitney): V678F FERM–JH1 p = 0.063, **JH2–JH1 p = 0.028**; P982A FERM–JH1 p = 0.10,
JH2–JH1 p = 0.097. V678F's own two halves agree (FERM–JH1 p = 0.16), so this is not batch variance.

**Conclusion: V678F does not open TYK2 at 32/64, but it does significantly loosen the JH2–JH1 contact.**

- **FERM–JH1 has no dynamic range at this depth.** All 46 seeds across the three arms are compact (0 open), so
  the measurement is at its floor and cannot report an opening. The positive control therefore does not
  validate FERM–JH1 as a readout for TYK2 at 32/64, and P982A's null on that coordinate stays uninformative.
- **JH2–JH1 does respond.** V678F separates the pseudokinase and kinase domains by ~6 Å relative to wild type
  (55.0 vs 49.3 Å, p = 0.028) while staying inside the compact basin. P982A shifts the same way but weaker
  (53.5 Å, p = 0.097). Both TYK2 mutations push in the same direction on this coordinate, and the known
  activating one pushes harder.
- **Practical consequence: for TYK2, report JH2–JH1 as well as FERM–JH1.** FERM–JH1 is saturated at both ends
  of the depth scan (0/15 open at 32/64, 8/8 open at 128/512) and unstable in between (wild type's batches
  disagree at 64/256, p = 0.041). JH2–JH1 is the only coordinate in this campaign that has so far separated a
  known activating TYK2 mutation from wild type with a reproducible baseline.

This also re-reads the earlier 64/256 result. V678F was 8/8 extended there (Fisher p = 0.022 against pooled
wild type) but identical to wild type's own second batch (p = 1.00). Combined with 0/16 open here, the
64/256 "effect" is best explained as batch variance rather than a mutation effect on FERM–JH1.
