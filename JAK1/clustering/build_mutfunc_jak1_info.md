# "MutFunc score" for JAK1 — what it means, and the better substitute

Covers [`jak1_foldx.csv`](jak1_foldx.csv). Written 2 November 2026.

The appendix lists, verbatim:

> • MutFunc score (Wagih et al, 2018) (92.07% missing)

Singular "score", no column named. mutfunc returns **four** different scores, so the first job was
working out which one — and the answer turned out to make the feature obtainable at **94.9%**
instead of 7.9%.

---

## 1. What mutfunc is, and its current state

**mutfunc** (Wagih, Galardini, Busby, Memon, Typas & Beltrao, *Mol Syst Biol* 2018;14:e8430 —
*"A resource of variant effect predictions of single nucleotide variants in model organisms"*)
precomputes *mechanistic* consequences rather than a single pathogenicity call.

**It is live**, at `http://www.mutfunc.com/` — now hosted at ETH Zürich (Beltrao lab). Two practical
notes: **HTTP only**, port 443 refuses connections, so anything that forces HTTPS fails; and it is a
JavaScript application, so `curl` returns only an empty shell and it has to be driven in a browser.

It accepts **protein-level** input directly — `P00533 R132C`, or rsIDs, or genomic coordinates —
and states "We currently only support human variants".

## 2. Which score? There are four

Submitting four JAK1 variants returned these columns:

| Input | Pathogenicity | **Stability (ddG)** | pDockQ | Pocket score |
|---|--:|--:|--:|--:|
| P23458 A1005E | 1.00 | **5.02** | 0.97 | |
| P23458 I617T | 0.19 | **2.39** | | monomer |
| P23458 A1005D | *not mapped* | | | |
| P23458 H647Q | *not mapped* | | | |

So "MutFunc score" could mean Pathogenicity, Stability ΔΔG, pDockQ or the pocket score. Since the
paper lists its own PyRosetta ΔΔG separately, **Pathogenicity** is the likeliest intent — but it is
genuinely ambiguous.

**And today's mutfunc is not the 2018 resource the paper cited.** The build string is `26.06`, and
**pDockQ postdates the paper** (it is a 2022 method), as does the pocket score. Values fetched today
would not reproduce the paper's feature even if the right column were known. That alone makes exact
reproduction of this feature impossible.

## 3. Coverage: ~8%, and the reason

**Two of four test variants did not map at all.** Notably `A1005D` needs two nucleotide changes, but
so does nothing about `H647Q` (reachable by one, and present in dbNSFP) — yet that one is missing
too. So the limit is not the single-nucleotide ceiling; it is **structural coverage**: mutfunc needs
a structure or model at that residue to compute FoldX ΔΔG, pDockQ and pocket scores.

That matches the paper's **92.07% missing** (7.93% present, ≈ 1,739 of 21,926) — by far the sparsest
feature in its set, and consistent with structure-limited rather than variant-limited coverage.

Driving a browser form 21,926 times for a feature that covers 8% is not a reasonable plan, and there
is no documented API.

## 4. The decisive finding: the Stability column is FoldX, and we already have it

mutfunc's Stability ΔΔG is **FoldX on a structural model**. This repository already contains exactly
that, for all four JAKs, in `external_data/protvar_foldx_jak_src.csv` — FoldX v5 run on AlphaFold2
models, extracted from EBI **ProtVar**:

| protein | substitutions with FoldX |
|---|--:|
| **P23458 (JAK1)** | **20,805** |
| O60674 (JAK2) | 20,349 |
| P29597 (TYK2) | 20,178 |
| P52333 (JAK3) | 20,045 |

**It agrees with mutfunc numerically:**

| variant | mutfunc "Stability (ddG)" | ProtVar FoldX |
|---|--:|--:|
| A1005E | **5.02** | **5.0164** |
| I617T | **2.39** | **2.3933** |

Same quantity, same model family — at **94.9% coverage instead of 7.9%**, already in the repository,
no web scraping. So `jak1_foldx.csv` supersedes any attempt to pull mutfunc's stability column.

What ProtVar does **not** give is mutfunc's *other* three columns — Pathogenicity, pDockQ and the
pocket score. If the paper meant one of those, it is not substitutable, and given §2 it is not
faithfully reproducible either.

## 5. The file

[`jak1_foldx.csv`](jak1_foldx.csv) — 23,080 rows, EV1 order, conventions as in the README.

```csv
variant_id,wt,pos,alt,cluster,foldx_ddg,plddt
```

| | |
|---|--:|
| populated | **20,805 of 21,926 (94.9%)** |
| positions covered | **1,095 of 1,154** |
| ΔΔG range | −6.31 … **+72.50** kcal/mol |
| median | **+1.135** kcal/mol |
| pLDDT where covered | median 92.7, minimum 28.5 |
| duplicate substitutions | 0 — one value each, nothing to aggregate |

**Sign convention: positive = destabilising** (FoldX's native convention, and the *opposite* of the
PyRosetta ΔΔG in `data/ddg/`, which uses ΔG_WT − ΔG_mut). Mixing the two without flipping one would
put two stability features on opposite axes.

**The 59 uncovered positions are the disordered N-terminus** — positions 1–20 and similar stretches,
where the AlphaFold model has no usable structure. Blank here means "no structural model", not "no
effect", and the gap is systematic rather than random.

**The +72.50 kcal/mol maximum is not an energy.** FoldX produces steric-clash artefacts exactly as
PyRosetta does, and the diagnosis in `conclusions_ddG_difference_feature.md` §§8–10 applies: no
folding free energy approaches 72 kcal/mol. The median of 1.135 is the honest scale. Rank these
values; do not read the tail as kcal/mol.

## 6. Where this leaves the paper's feature list

| feature | paper | here |
|---|--:|--:|
| ESM-1b | 100% | 100% |
| AlphaMissense | 29.7% | **100%** |
| BLOSUM62 | 56.3% | **100%** |
| PolyPhen-2 | 56.3% | **100%** |
| **"MutFunc score"** | **7.9%** | **94.9%** as FoldX ΔΔG — *not* the same column if they meant Pathogenicity |
| SIFT | 56.3% | 31.3% |
| CADD | not stated | 31.3% |
| ClinPred | 14.25% | 31.3% |
| ΔΔG closed / open / difference | 100% | 2.3% (500 variants) |

The three PyRosetta ΔΔG features remain the real gap: 500 variants exist against the paper's claimed
100%, and recomputing them is the one genuinely expensive item left.
