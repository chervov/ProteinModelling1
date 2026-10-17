# TYK2_P982A_20261017_181325 — TYK2 P982A_free_msa128-512_s0-7

TYK2 P982A, NO template, MSA 128/512, 8 seeds. Paired with wild type TYK2_20261016_175018 (same settings: all 8 seeds open-like, FERM–JH1 93.2–93.8 Å, JH2–JH1 46.5–46.7 Å). P982A was queued as the free-prediction mutant after the 4OLI template assay showed no dynamic range (TYK2_20261016_130845); the earlier template-based P982A attempt died of CUDA OOM after 11 of 16 seeds.

Settings: OpenFold model_1, guided recycling, 15 recycles × seeds 0,1,2,3,4,5,6,7; MSA 128 clusters / 512 extra; no template. Inference ~79 min on molab; the notebook was interrupted twice during setup (weight unpacking, tensorrt install) by monitoring requests and resumed, which did not affect inference.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-P29597-F1) | 37.2 | 39.7 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 0 | 3 | 82.2 | 46.7 | 93.0 | 82.3 | AF2 |
| 1 | 15 | 81.8 | 46.6 | 92.9 | 82.6 | AF2 |
| 2 | 14 | 81.5 | 46.7 | 93.2 | 82.4 | AF2 |
| 3 | 7 | 81.9 | 46.8 | 93.6 | 82.6 | AF2 |
| 4 | 14 | 81.6 | 46.6 | 93.0 | 82.1 | AF2 |
| 5 | 14 | 81.6 | 46.5 | 93.4 | 81.8 | AF2 |
| 6 | 14 | 81.5 | 46.5 | 93.4 | 82.1 | AF2 |
| 7 | 14 | 81.7 | 46.4 | 93.0 | 81.9 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-P29597-F1) | 46.7 | 2 | 1 | 72.7 | 0 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 73.1 | 38.7 | 64.5 |
| 2 | 79.7 | 63.0 | 73.6 |
| 3 | 81.4 | 93.8 | 84.4 |
| 4 | 81.4 | 93.5 | 82.8 |
| 5 | 81.4 | 93.4 | 82.7 |
| 6 | 81.5 | 93.4 | 82.4 |
| 7 | 81.6 | 93.4 | 82.4 |
| 8 | 81.3 | 93.4 | 82.4 |
| 9 | 81.3 | 93.3 | 82.5 |
| 10 | 81.4 | 93.3 | 82.4 |
| 11 | 81.4 | 93.3 | 82.6 |
| 12 | 81.5 | 93.3 | 82.6 |
| 13 | 81.5 | 93.2 | 82.1 |
| 14 | 81.7 | 93.2 | 82.1 |
| 15 | 81.6 | 93.2 | 82.3 |

pLDDT 72.6–82.2; JH2–JH1 33.2–58.2 Å; FERM–JH1 15.9–94.7 Å (open = AF2 TYK2; closed reference: JAK1 ma-l9b1f mapped (see TYK2 analysis); FERM–JH1 > ~80 Å = open, < ~50 Å = closed).
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 0 | 62 92 93 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 1 | 45 89 94 93 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 2 | 18 93 94 93 93 93 94 93 94 93 94 93 93 93 93 | open-like (> 80) |
| 3 | 22 33 92 94 93 94 94 94 94 94 93 93 93 93 93 | open-like (> 80) |
| 4 | 41 66 94 93 94 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |
| 5 | 43 36 94 93 93 94 94 94 94 94 94 94 94 93 93 | open-like (> 80) |
| 6 | 17 16 94 94 94 94 94 94 94 94 94 94 94 93 93 | open-like (> 80) |
| 7 | 63 78 95 94 93 93 93 93 93 93 93 93 93 93 93 | open-like (> 80) |

## Comparison with wild type (TYK2_20261016_175018, same settings)

| | median FERM–JH1 | range | median JH2–JH1 | open-like seeds |
|---|--:|--:|--:|--:|
| wild type | 93.6 | 93.2–93.8 | 46.6 | 8/8 |
| **P982A** | 93.1 | 92.9–93.6 | 46.6 | 8/8 |

Mann-Whitney on the selected FERM–JH1 values: p = 0.013.

**Conclusion: no conformational effect of P982A at 128/512.** All 8 mutant seeds are open-like, like all 8 wild-type seeds. The selected FERM–JH1 values are 0.5 Å lower for P982A (median 93.1 vs 93.6 Å); the ranges overlap, but the shift is statistically detectable (p = 0.013), but it is a ~0.5 % change within the same extended state, against the ~50 Å open/closed difference, so it is not a state change.

Wild type already sits entirely in the extended arrangement at this depth, so the assay cannot show a further opening. TYK2 at 128/512 behaves like JAK3 at full depth (512/8192), not like JAK3 at 128/512, where wild type is fully compact. Testing P982A needs a depth at which TYK2 wild type is compact: a shallower MSA (e.g. 64/128 or 32/64). The queued 512/8192 runs would only push further towards the extended state.
