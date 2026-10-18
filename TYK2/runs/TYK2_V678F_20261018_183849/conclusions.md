# TYK2_V678F_20261018_183849 — TYK2 V678F_free_msa32-64_s0-7 (positive control, stable-baseline depth)

TYK2 V678F at MSA 32/64, seeds 0-7, no template. Positive control re-run at the only TYK2 depth with a reproducible wild-type baseline: wild type is 15/15 compact at 32/64 across two independent batches, whereas at 64/256 its two batches disagree (1/8 vs 7/8 extended, p = 0.041) and V678F there was indistinguishable from wild type's own second batch. Paired with wild type TYK2_20261018_135623 + TYK2_20261018_153027 and with P982A TYK2_P982A_20261018_135623 + TYK2_P982A_20261018_153019 (15 seeds each). Second half: TYK2_V678F_20261018_204500.

Settings: OpenFold model_1, guided recycling, 15 recycles x seeds 0,1,2,3,4,5,6,7; MSA 32 clusters / 64 extra; no template. Run time ~100 min on a fresh molab sandbox.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 14 | 78.9 | 55.7 | 50.8 | 48.5 | AF2 |
| 1 | 6 | 78.8 | 59.2 | 48.6 | 68.0 | AF2 |
| 2 | 7 | 78.9 | 56.4 | 48.9 | 45.6 | AF2 |
| 3 | 7 | 76.3 | 58.4 | 38.7 | 58.9 | AF2 |
| 4 | 7 | 79.0 | 52.6 | 43.3 | 62.2 | AF2 |
| 5 | 13 | 79.0 | 40.4 | 51.4 | 42.3 | AF2 |
| 6 | 7 | 79.3 | 55.9 | 50.6 | 54.1 | AF2 |
| 7 | 14 | 76.5 | 60.7 | 44.6 | 46.4 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 30.7 | 0 | 4 | 76.6 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 56.9 | 46.5 | 43.3 |
| 2 | 71.4 | 48.5 | 50.4 |
| 3 | 74.6 | 47.6 | 49.9 |
| 4 | 76.2 | 46.9 | 48.1 |
| 5 | 77.5 | 47.2 | 49.8 |
| 6 | 77.9 | 46.8 | 53.3 |
| 7 | 78.1 | 47.5 | 54.0 |
| 8 | 78.0 | 48.2 | 53.2 |
| 9 | 77.6 | 48.0 | 52.7 |
| 10 | 76.4 | 46.9 | 52.3 |
| 11 | 77.8 | 48.2 | 55.9 |
| 12 | 77.5 | 48.2 | 55.4 |
| 13 | 78.0 | 46.9 | 54.3 |
| 14 | 78.1 | 47.0 | 52.9 |
| 15 | 77.7 | 47.9 | 52.8 |

pLDDT 54.5–79.3; JH2–JH1 40.2–63.0 Å; FERM–JH1 38.0–56.5 Å. (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 48 44 42 44 47 50 53 52 54 47 51 54 49 51 55 | intermediate |
| 1 | 49 50 51 51 51 49 48 48 48 47 51 49 48 48 47 | closed-like (< 50) |
| 2 | 48 57 55 52 51 49 49 50 49 50 49 49 50 50 50 | closed-like (< 50) |
| 3 | 47 50 52 46 41 39 39 40 40 41 40 42 39 40 42 | closed-like (< 50) |
| 4 | 48 46 42 41 43 42 43 45 45 46 45 44 43 44 44 | closed-like (< 50) |
| 5 | 49 51 53 53 51 51 52 56 54 51 52 52 51 49 52 | intermediate |
| 6 | 38 42 42 44 47 49 51 52 51 53 53 53 51 50 50 | closed-like (< 50) |
| 7 | 46 48 43 45 48 44 45 44 43 41 44 43 42 45 44 | closed-like (< 50) |

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
