# TYK2_V678F_20261018_165935 — TYK2 V678F_free_msa64-256_s0-7 (positive control)

TYK2 V678F, NO template, MSA 64/256, seeds 0–7. **Positive control for the assay**: V678F is the TYK2 equivalent of the activating JAK2 V617F / JAK1 V658F pseudokinase mutation. P982A showed no FERM–JH1 state change at any depth (32/64, 64/256, 128/512), which is only informative if this assay can detect a known activating mutation in TYK2 at all. Run at 64/256 because that is the depth where TYK2 wild type is mixed (7/16 compact, 8/16 extended), so a shift in either direction is visible. Compared with wild type TYK2_20261018_084732 + TYK2_20261018_101316 and P982A TYK2_P982A_20261018_084539 + TYK2_P982A_20261018_101316 (16 seeds each).

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 64 clusters / 256 extra; no template. Run time ~80 min (incl. a fresh MSA for the mutant query).



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 7 | 80.3 | 50.8 | 92.9 | 92.1 | AF2 |
| 1 | 10 | 80.2 | 52.1 | 92.3 | 94.8 | AF2 |
| 2 | 11 | 80.1 | 51.3 | 93.8 | 93.1 | AF2 |
| 3 | 7 | 80.9 | 52.5 | 93.3 | 94.3 | AF2 |
| 4 | 7 | 80.6 | 49.0 | 89.0 | 90.7 | AF2 |
| 5 | 6 | 80.2 | 51.6 | 91.6 | 94.4 | AF2 |
| 6 | 9 | 80.4 | 49.6 | 88.3 | 91.3 | AF2 |
| 7 | 10 | 80.1 | 52.4 | 93.7 | 94.7 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 29.0 | 5 | 2 | 75.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 66.7 | 47.2 | 41.1 |
| 2 | 76.5 | 42.2 | 33.9 |
| 3 | 79.2 | 45.3 | 46.6 |
| 4 | 79.9 | 55.4 | 62.0 |
| 5 | 80.1 | 75.3 | 81.4 |
| 6 | 80.0 | 82.7 | 88.1 |
| 7 | 80.2 | 84.2 | 87.6 |
| 8 | 80.0 | 91.9 | 87.8 |
| 9 | 80.1 | 93.2 | 90.2 |
| 10 | 80.1 | 93.2 | 93.0 |
| 11 | 80.1 | 94.1 | 89.9 |
| 12 | 80.0 | 94.6 | 90.1 |
| 13 | 79.9 | 94.6 | 88.0 |
| 14 | 80.1 | 93.9 | 89.2 |
| 15 | 80.1 | 94.3 | 88.9 |

pLDDT 66.1–80.9; JH2–JH1 48.1–56.4 Å; FERM–JH1 39.0–95.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 47 41 43 53 81 91 93 94 95 95 95 95 95 95 95 | open-like (> 80) |
| 1 | 51 44 47 48 50 50 52 78 94 92 95 95 95 94 95 | open-like (> 80) |
| 2 | 45 42 44 47 84 91 93 95 94 92 94 95 95 95 95 | open-like (> 80) |
| 3 | 39 39 43 86 94 91 93 95 95 95 96 96 95 95 95 | open-like (> 80) |
| 4 | 53 39 45 50 71 85 89 94 92 92 93 92 94 92 93 | open-like (> 80) |
| 5 | 58 43 45 55 83 92 92 94 93 92 93 94 94 92 94 | open-like (> 80) |
| 6 | 41 47 49 53 69 76 74 91 88 93 94 93 94 93 94 | open-like (> 80) |
| 7 | 44 42 47 51 69 86 88 95 94 94 95 95 95 95 95 | open-like (> 80) |

## Positive control verdict: wild type vs V678F vs P982A at 64/256

| | n | median FERM–JH1 | range | extended (> 80 Å) | compact (< 60 Å) |
|---|--:|--:|---|--:|--:|
| wild type | 16 | 80.0 | 34–95 | 8/16 | 7/16 |
| P982A | 16 | 89.5 | 46–96 | 13/16 | 3/16 |
| **V678F** | 8 | 92.6 | 88–94 | **8/8** | 0/8 |

Against pooled wild type: V678F Mann-Whitney p = 0.061, Fisher on extended counts p = 0.022;
P982A p = 0.27 / 0.14.

**Taken at face value this says the assay detects V678F and not P982A. It does not survive a batch check.**

| | extended | median | V678F vs this batch |
|---|--:|--:|---|
| wild type seeds 0–7 | 1/8 | 56.3 | Fisher p = 0.0014, MW p = 0.0002 |
| wild type seeds 8–15 | 7/8 | 92.1 | **Fisher p = 1.00, MW p = 0.96** |
| V678F seeds 0–7 | 8/8 | 92.6 | – |

V678F is **indistinguishable from wild type's own second batch** and differs only from its first batch. The entire
V678F signal against pooled wild type comes from wild type's two halves disagreeing (1/8 vs 7/8 extended,
Fisher p = 0.041), not from the mutation. The two wild-type batches differ from each other as strongly as V678F
differs from wild type.

**Conclusion: at 64/256 this assay cannot distinguish any of these mutations from wild type, because batch-to-batch
variance between 8-seed runs is as large as the effect being measured.** The positive control fails to validate the
assay at this depth: it neither confirms detection (V678F matches one wild-type batch exactly) nor rules it out.
This also retracts the direction previously read into P982A at 64/256 (13/16 vs 8/16 extended, p = 0.27) — that
comparison rests on the same unstable wild-type baseline.

What this does not affect: the 32/64 result (all 30 seeds compact in both arms, both halves agreeing) and the
128/512 result (all 16 seeds extended in both arms) are internally consistent across batches, so P982A having no
state effect at those depths stands.

Next steps, in order of value:
1. **V678F seeds 8–15 and more wild-type batches at 64/256.** If V678F stays 16/16 extended while wild type keeps
   flipping between batches, the batch variance is a wild-type property near its switch point and V678F genuinely
   sits past it. This is the only way to rescue the 64/256 comparisons.
2. **V678F at 32/64**, where wild type is reproducibly compact in 15/15 seeds across two independent batches. That
   is the only depth in this scan with a stable baseline, so it is the only place a mutation effect can currently
   be measured cleanly. If V678F opens seeds there, the assay works and P982A's null at that depth is real.

Option 2 is the stronger test: it uses the one depth where the baseline is known to be reproducible.
