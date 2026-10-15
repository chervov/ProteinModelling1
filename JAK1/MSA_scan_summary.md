# JAK1 MSA-depth scan — no template (OpenFold model_1, guided recycling)

All runs: JAK1 full length, no template, seeds 0–4. JH1 position after superposing JH2 is compared with Orianne's
open (ma-a1sai) and closed (ma-l9b1f) models; FERM–JH1 centroid distance: open ~92 Å, closed ~40 Å
(see [open_close.md](../open_close.md)).

| MSA (clusters / extra) | recycles | run | result per seed | best vs closed ma-l9b1f | best vs open ma-a1sai |
|---|--:|---|---|--:|--:|
| 512 / 8192 (all 7390 sequences) | 15 | [JAK1_20261014_115803](runs/JAK1_20261014_115803) | 5 × open | – (> 80 Å) | 0.5 Å |
| 256 / 1024 | 15 | [JAK1_20261015_104236](runs/JAK1_20261015_104236) | 5 × open (from recycle 2) | 19.0 Å (recycle 1) | 0.6 Å |
| 160 / 640 | 15 | [JAK1_20261015_131035](runs/JAK1_20261015_131035) | 5 × open (from recycle 2) | 10.4 Å (recycle 1) | 0.4 Å |
| **128 / 512** | 15 | [JAK1_20261015_082811](runs/JAK1_20261015_082811) | **2 × closed, 2 × open, 1 switching** | **2.4 Å** | 2.5 Å |
| **128 / 512**, seeds 5–14 | 15 | [JAK1_20261015_114024](runs/JAK1_20261015_114024) | **4 × next to FERM, 5 × open, 1 switching** | **1.2 Å** | 1.2 Å |
| **128 / 512, pooled 15 seeds** | 15 | – | **7 open, 6 next to FERM (2 closed match, 2 near), 2 switching** | 1.2 Å | 1.2 Å |
| 128 / 512 | 8 | [JAK1_20261014_135749](runs/JAK1_20261014_135749) | 5 × open by recycles 4–8 | 17.2 Å (recycle 1) | 1.0 Å |
| 96 / 384 | 15 | [JAK1_20261015_135849](runs/JAK1_20261015_135849) | **no open**: 3 × next to FERM (12–19 Å from closed), 2 × third arrangement | 3.8 Å (recycle 3) | 43.3 Å |
| 64 / 256 | 15 | [JAK1_20261015_095803](runs/JAK1_20261015_095803) | 5 × a third arrangement (JH1 off FERM, 47–52 Å from open) | 31.8 Å | 35.6 Å |
| 32 / 64 | 30 | e.g. [JAK1_20261013_192228](runs/JAK1_20261013_192228) | compact, FERM-bound, low pLDDT, never open | – | ≥ 61.5 Å |

## Conclusions
- **Deep MSA (≥ 256/1024) → open**, confidently and in every seed; the network settles by recycle 2.
- **128/512 is the bistable depth:** the only template-free setting so far that produces the real closed JAK1
  (seed 4: 2.4 Å from ma-l9b1f, pLDDT ~84, the same confidence as the open seeds). Which seeds close is not
  reproducible run-to-run (the 8-recycle run went all open); the fraction of closed seeds is the meaningful number,
  and 15 recycles are needed for it to settle.
- **Shallower MSA (≤ 64/256) → neither reference:** a consistent third arrangement at 64/256, compact FERM-bound
  low-confidence structures at 32/64.
- Recycle 1 is FERM-bound at every depth; with enough MSA signal the network leaves it at recycle 2 (open).

## Update (all depths done)
- From deep to shallow MSA the behaviour goes **open → open/closed (128/512) → next to FERM or third arrangement,
  no open (96/384) → third arrangement (64/256) → compact (32/64)**. The window in which both real states appear is
  narrow (160/640 already all open, 96/384 no open).

## Next
- More seeds at 128/512 (and e.g. 96/384, 160/640) to measure the closed fraction and how sharp the window is.
- The same scan for JAK2 without a template.
