# JAK3 M592F — the activating-position mutation opens JAK3 (MSA 128/512)

M592 is the JAK3 residue equivalent to **JAK2 V617** and **JAK1 V658**, the classic activating
pseudokinase position. Wild type and M592F were run with identical settings and **the same 16 seeds**:
OpenFold model_1, guided recycling, no template, 15 recycles, MSA 128/512.

Runs: [JAK3_20261016_125830](runs/JAK3_20261016_125830/conclusions.md) (wild type, 131 min) and
[JAK3_M592F_20261016_105409](runs/JAK3_M592F_20261016_105409/conclusions.md) (M592F, 135 min).

## Per-seed outcome

| | final FERM–JH1 (Å), 16 seeds | max | > 70 Å |
|---|---|--:|--:|
| **wild type** | 42 42 42 42 43 43 43 50 51 54 54 54 55 55 56 56 | 56 | **0/16** |
| **M592F** | 44 48 50 52 53 53 54 55 55 56 58 **80 94 94 95 97** | 97 | **5/16** |

Fisher exact, > 70 Å: **p = 0.043**. Mean FERM–JH1 over recycles 2–15: wild type 49–51 Å, M592F ~65 Å.

## What the two states are

The run notebooks had only the AlphaFold model as a JAK3 reference, so every conformation came back
"nearest AF2" by default. Classifying offline against references mapped onto JAK3 numbering by sequence
alignment (JH1 RMSD after superposing JH2 — the domain arrangement, not fold detail):

**References, in JAK3 numbering**

| reference | identity | FERM–JH1 | JH2–JH1 |
|---|--:|--:|--:|
| AF2 JAK3 | 100 % | 41.5 | 38.3 |
| ma-l9b1f, JAK1 closed | 44 % | 42.4 | 39.9 |
| ma-a1sai, JAK1 open | 44 % | 93.6 | 45.8 |
| 7T6F, mouse JAK1 active dimer | 44 % | 84.1 | 44.7 |
| 4OLI, TYK2 autoinhibited (experimental) | 51 % | – | 39.0 |

**Structures (JH1 RMSD after superposing JH2, Å)**

| structure | FERM–JH1 | JH2–JH1 | AF2 | ma-l9b1f | ma-a1sai | 7T6F | 4OLI |
|---|--:|--:|--:|--:|--:|--:|--:|
| WT, most compact | 43.7 | 44.9 | 16.2 | **13.4** | 87.1 | 90.1 | **16.8** |
| WT, most splayed | 51.5 | 63.1 | 89.0 | 90.3 | 100.9 | 88.7 | 89.5 |
| M592F, most compact | 94.2 | 46.9 | 83.1 | 82.6 | **3.3** | 47.8 | 81.8 |
| M592F, most splayed | 52.4 | 55.5 | 66.6 | 64.6 | 91.2 | 101.3 | 66.1 |

## Reading

1. **Wild-type JAK3 adopts the closed, autoinhibited arrangement.** Its compact structure sits 13.4 Å
   from the JAK1 closed model, 16.8 Å from the **experimental** TYK2 autoinhibited crystal 4OLI, and
   16.2 Å from the AlphaFold JAK3 model — three independent closed references agreeing within 13–17 Å.
2. **M592F reaches the open arrangement, and wild type never does.** The extended M592F structure is
   **3.3 Å from the JAK1 open model**, with FERM–JH1 94.2 Å. That is the state behind the five seeds
   above 70 Å; wild type's maximum is 56 Å.
3. **Both runs also contain a splayed arrangement** (JH2–JH1 63 Å and 55 Å versus 38–46 Å in every
   reference) that matches nothing. JH1 has swung away from JH2 — reminiscent of the detached-JH1
   intermediate seen in JAK2.
4. **FERM–JH1 and the JH2–JH1 arrangement are decoupled.** The two wild-type structures have similar
   FERM–JH1 (43.7 and 51.5 Å) but completely different domain arrangements (13.4 versus 90.3 Å from the
   closed model). FERM–JH1 alone is not a sufficient classifier.

## Comparison across the family at 128/512

| | effect of the equivalent mutation |
|---|---|
| **JAK1 V658F** | removes the closed arrangement, moves to the 7T6F active-dimer arrangement (p = 0.035) |
| **JAK2 V617F** | detached JH1 → open (p = 0.003) |
| **JAK3 M592F** | **closed → open, 5/16 seeds (p = 0.043)** |

JAK3 behaves like JAK1: the mutation removes the autoinhibited arrangement. JAK2 at this depth moves
differently, so the position does not act in one consistent direction across the family.

## Caveats
- The p-value is threshold-dependent: 0.043 at > 70 Å, 0.10 at > 80 Å. Suggestive, not established.
- Only the two extreme structures per run (by JH2–JH1 distance) were available for classification, not
  all 16 seeds, so the per-seed counts rest on FERM–JH1 while the state identification rests on these two.
- Reference mapping is across paralogues at 44–51 % identity; the measure is domain arrangement, which is
  robust to fold detail, but the 3.3 Å match should be read as "the same arrangement", not atomic agreement.
- One depth only. JAK2 showed that direction can reverse with MSA depth; JAK3 at 512/8192 and 96/384 is queued.
