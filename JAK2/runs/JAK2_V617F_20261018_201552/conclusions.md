# JAK2_V617F_20261018_201552 — JAK2 V617F_free_msa256-1024_s8-15

JAK2 V617F at MSA 256/1024, seeds 8-15, no template: second half of JAK2_V617F_20261015_215648 (seeds 0-7), run to resolve the sharpest internal contradiction in the campaign. V617F appeared to significantly CLOSE JAK2 at 256/1024 (wild type 16/16 open -> mutant 4/8, Fisher p = 0.0066) while significantly OPENING it at 512/8192 (7/16 -> 16/16, p = 0.0008). With only 8 seeds on the 256/1024 arm, batch variance was the leading explanation. Paired with wild type JAK2_20261015_134817 + JAK2_20261015_201144 (16 seeds, same depth).

Settings: OpenFold model_1, guided recycling, 15 recycles x seeds 8-15; MSA 256 clusters / 1024 extra; no template.



## References (centroid distances, Å)

| reference | JH2–JH1 | FERM–JH1 |
|---|--:|--:|
| AF2 (AF-O60674-F1) | 45.9 | 93.8 |

## Selected structure per seed (JH1 RMSD after superposing JH2, Å)

| seed | recycle | pLDDT | JH2–JH1 (Å) | FERM–JH1 (Å) | vs AF2 | nearest |
|--:|--:|--:|--:|--:|--:|---|
| 8 | 9 | 85.1 | 46.9 | 49.8 | 88.2 | AF2 |
| 9 | 14 | 85.9 | 46.2 | 94.6 | 1.3 | AF2 |
| 10 | 4 | 85.9 | 46.2 | 94.6 | 1.9 | AF2 |
| 11 | 7 | 85.9 | 46.1 | 94.6 | 1.8 | AF2 |
| 12 | 7 | 84.6 | 41.8 | 47.1 | 83.8 | AF2 |
| 13 | 4 | 85.1 | 46.8 | 48.2 | 89.1 | AF2 |
| 14 | 10 | 85.9 | 46.2 | 94.7 | 2.1 | AF2 |
| 15 | 11 | 86.1 | 46.3 | 94.7 | 2.3 | AF2 |

## All conformations

| reference | closest (Å) | seed | recycle | pLDDT | within 15 Å |
|---|--:|--:|--:|--:|--:|
| AF2 (AF-O60674-F1) | 0.5 | 10 | 3 | 85.4 | 69 |

## Mean over seeds per recycle (Å)

| recycle | pLDDT | FERM–JH1 | vs AF2 |
|--:|--:|--:|--:|
| 1 | 82.5 | 59.0 | 70.7 |
| 2 | 84.8 | 79.0 | 38.6 |
| 3 | 85.3 | 77.7 | 34.2 |
| 4 | 85.5 | 77.4 | 34.0 |
| 5 | 85.3 | 77.5 | 33.4 |
| 6 | 85.3 | 77.6 | 33.2 |
| 7 | 85.4 | 77.6 | 33.7 |
| 8 | 85.3 | 77.7 | 33.2 |
| 9 | 85.4 | 77.7 | 33.5 |
| 10 | 85.3 | 77.7 | 33.4 |
| 11 | 85.5 | 77.5 | 33.4 |
| 12 | 85.5 | 77.6 | 33.4 |
| 13 | 85.4 | 77.7 | 33.2 |
| 14 | 85.4 | 77.5 | 33.1 |
| 15 | 85.3 | 77.4 | 33.0 |

pLDDT 81.4–86.1; JH2–JH1 26.3–49.0 Å; FERM–JH1 47.1–95.1 Å. (JAK2 open/closed: open ~95 A, compact ~45-62 A.)
Nearest reference over all conformations: AF2 120.
## Per-seed trajectories (FERM–JH1 centroid distance, Å; open ~90+, closed ~40–45)

| seed | recycles 1–15 | final |
|--:|---|---|
| 8 | 51 50 49 49 50 50 50 50 50 49 49 49 49 49 48 | closed-like (< 50) |
| 9 | 60 84 95 94 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 10 | 62 95 94 95 94 95 94 94 95 94 95 94 95 95 94 | open-like (> 80) |
| 11 | 61 94 95 95 94 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 12 | 63 58 50 49 47 48 47 47 47 48 47 48 47 47 48 | closed-like (< 50) |
| 13 | 59 61 49 48 50 50 50 51 51 51 50 51 52 51 49 | closed-like (< 50) |
| 14 | 55 95 94 95 94 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |
| 15 | 62 95 95 95 95 95 95 95 95 95 95 95 95 95 95 | open-like (> 80) |

## Resolution: the V617F "depth reversal" is an artifact of wild type, not of the mutation

Pooled with seeds 0-7, V617F at 256/1024 is **9/16 open**, and the two halves agree exactly
(4/8 vs 5/8, Fisher p = 1.00). The effect is reproducible, so batch variance is ruled out:
V617F really does produce fewer open seeds than wild type at this depth (16/16 vs 9/16, Fisher p = 0.0068).

Placing it in the full depth scan dissolves the contradiction:

| open seeds (FERM-JH1 > 80 A) | 64/256 | 128/512 | 256/1024 | 512/8192 |
|---|---|---|---|---|
| JAK2 wild type | 0/16 | 1/15 | **16/16** | 7/16 |
| JAK2 V617F | 0/16 | 6/16 | 9/16 | 16/16 |

**V617F is monotonic: 0 -> 6 -> 9 -> 16 open as the MSA deepens. Wild type is not: 0 -> 1 -> 16 -> 7.**

Wild type spikes to fully open at 256/1024 and falls back to 7/16 at 512/8192, while being almost entirely
compact at 128/512 (1/15) and 64/256 (0/16). That single anomalous point is the only depth at which V617F
appears to "close" JAK2. At every other depth V617F is as open as, or more open than, wild type
(128/512: 6/16 vs 1/15, p = 0.083; 512/8192: 16/16 vs 7/16, p = 0.0008; 64/256: both at the 0/16 floor).

So the mutation behaves consistently and in the expected direction — more open, increasingly so with MSA
depth. **The thing that needs explaining is JAK2 wild type at 256/1024**, which is reproducible across its
own two runs (n5 + n11, MW p = 0.72) yet sits far off the trend set by its neighbouring depths.

Until that anomaly is understood, 256/1024 should not be used as a comparison depth for JAK2, and the
earlier "V617F closes JAK2" reading should be retired.

Note on the reference: AF2 JAK2 (AF-O60674-F1) is itself the open arrangement (FERM-JH1 93.8 A), and the
open seeds here sit 1.3-2.3 A from it, i.e. they reproduce the deposited model almost exactly.
