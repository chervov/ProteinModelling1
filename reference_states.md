# Reference states and the open/closed criteria

All four JAKs, every reference structure available, measured the same way. Structures from one
paralogue were renumbered onto the others by global sequence alignment (BLOSUM62, free end gaps);
cross-mapping identity is 44–59 %.

Domains (UniProt numbering): JAK1 FERM 34–420, JH2 583–855, JH1 875–1154 · JAK2 FERM 37–380,
JH2 536–827, JH1 849–1124 · JAK3 FERM 24–356, JH2 521–781, JH1 822–1111 · TYK2 FERM 26–431,
JH2 589–875, JH1 897–1176.

## 1. Centroid distances in each structure's own protein

| structure | protein | FERM–JH1 (Å) | JH2–JH1 (Å) | state |
|---|---|--:|--:|---|
| **4OLI crystal** | TYK2 | – *(no FERM)* | **39.0** | **experimental closed** |
| **7T6F cryo-EM** | JAK1 (mouse) | **84.1** | 45.0 | **experimental active dimer** |
| ma-l9b1f (Jeanpierre) | JAK1 | **40.0** | 39.5 | closed model |
| ma-a1sai (Jeanpierre) | JAK1 | **92.6** | 46.1 | open model |
| Shan 2014 | JAK1 | – | 38.0 | closed model (JH2–JH1 only) |
| Shan 2014 | JAK2 | – | 39.6 | closed model (JH2–JH1 only) |
| our prediction | JAK2 | 45.0 | 39.0 | closed, predicted |
| our prediction | JAK3 | 43.7 | 44.9 | closed, predicted |
| **AF2 model** | **JAK1** | **92.3** | 46.3 | **open** |
| **AF2 model** | **JAK2** | **93.8** | 46.1 | **open** |
| **AF2 model** | **JAK3** | **41.5** | 38.3 | **closed** |
| **AF2 model** | **TYK2** | **39.7** | 37.2 | **closed** |

## 2. The same references mapped onto every target

Remarkably consistent — the criteria transfer across paralogues.

| reference | → JAK1 | → JAK2 | → JAK3 | → TYK2 |
|---|--:|--:|--:|--:|
| **FERM–JH1** | | | | |
| ma-l9b1f (closed) | 40.0 | 42.0 | 42.4 | 40.2 |
| 7T6F (active) | 84.1 | 84.0 | 84.1 | 83.9 |
| ma-a1sai (open) | 92.6 | 92.9 | 93.6 | 92.2 |
| **JH2–JH1** | | | | |
| 4OLI (closed, exp.) | 39.2 | 38.6 | 39.0 | 39.0 |
| ma-l9b1f (closed) | 39.5 | 39.1 | 39.9 | 39.6 |
| 7T6F (active) | 45.0 | 45.2 | 44.7 | 45.0 |
| ma-a1sai (open) | 46.1 | 45.5 | 45.8 | 45.8 |

## 3. Criteria

**FERM–JH1 separates the states cleanly** — three well-resolved bands, consistent across all four proteins:

| state | FERM–JH1 |
|---|---|
| **closed / autoinhibited** | **40–45 Å** |
| **active dimer (7T6F-like)** | **~84 Å** |
| **open** | **92–94 Å** |

**JH2–JH1 does not.** Closed sits at 38–40 Å and open at 45–46 Å — a separation of only ~7 Å, far too
small to classify a single structure. This is why the **domain-arrangement metric** (JH1 RMSD after
superposing JH2) is used instead of the JH2–JH1 centroid distance.

**Arrangement metric, JH1 RMSD after superposing JH2 (Å):**

| | closed ma-l9b1f | open ma-a1sai | active 7T6F | closed 4OLI |
|---|--:|--:|--:|--:|
| closed ma-l9b1f | 0.0 | 81.8 | 83.0 | **4.1** |
| open ma-a1sai | 81.8 | 0.0 | 46.2 | 80.4 |
| active 7T6F | 83.0 | 46.2 | 0.0 | 81.0 |
| closed 4OLI | **4.1** | 80.4 | 81.0 | 0.0 |

Open and closed are **~81 Å apart** on this measure, and the two independent closed references — a model
(ma-l9b1f) and a crystal structure of a different paralogue (4OLI) — agree to **4.1 Å**. The active dimer
is a genuinely third state, 46 Å from open and 81–83 Å from closed.

**Working thresholds:** < 25 Å = that state; > 60 Å = not that state; in between = intermediate.

## 4. A trap: "vs AF2" means opposite things in different proteins

| | AF2 FERM–JH1 | AF2 represents |
|---|--:|---|
| JAK1 | 92.3 | **open** (3.4 Å from ma-a1sai) |
| JAK2 | 93.8 | **open** |
| JAK3 | 41.5 | **closed** |
| TYK2 | 39.7 | **closed** (1.6 Å from 4OLI) |

**The AlphaFold models of JAK1 and JAK2 are open; those of JAK3 and TYK2 are closed.** Any analysis
reporting distance "vs AF2" therefore measures distance-from-open for JAK1/JAK2 and distance-from-closed
for JAK3/TYK2. In this project the JAK3 and TYK2 runs carried AF2 as their only reference, so "vs AF2"
there is a closed-state measure — correct as used, but the sign reverses for the JAK1 and JAK2 runs and
the two must never be pooled without checking.

AF2 TYK2 is only **1.6 Å** from the experimental 4OLI arrangement, so for TYK2 the AlphaFold model is an
excellent stand-in for the crystal structure.
