# Non-kinase human proteins, batch 3 — the screen exhausted

This batch closes the non-kinase screen. Rather than take an arbitrary 200 or 300, the
**entire eligible pool was screened**: all 3,397 reviewed human non-kinase proteins with two or
more UniProt Domain features in the 200–3,000 aa range. 150 were already analysed in batches 1–2;
the remaining 3,247 were screened here, and exactly **204 have two or more distinct multi-domain
PDB entries** — the minimum needed to measure variation at all. All 204 were analysed.

There is no "next chunk" after this one. Of the 3,397 eligible proteins, **354 are now measured**
and the other 3,043 are not excluded by choice: they have fewer than two templates spanning two or
more domains, so no inter-template comparison exists for them.

**2,167 observations**, 202 of 204 proteins returning data. **83 domain pairs across 38 proteins**
have two or more distinct entries; 17 exceed 15 Å of spread and 10 exceed 20 Å. AlphaFold falls
outside the experimental range in **19 of 82 pairs (23%)**, matching batch 2's 21%.

## Why 38 of 204, and not more

This batch is much thinner than batch 2 (83 pairs versus 436) for a reason worth recording. These
are the least-studied proteins in the pool — median 4 multi-domain entries against batch 2's 12 —
and they appear predominantly as subunits of large complexes. SWISS-MODEL serves those entries in
**PDB author numbering**, which the residue-identity gate correctly rejects: among the structure
files fetched for the first 60 proteins, **223 of 359 failed the gate, every one of them
PDB-provider**. The gate is doing its job — it is what prevents the false 26 Å SRC result found
earlier — but it means this batch measures mostly SWISS-MODEL-built models (612 observations)
rather than deposited coordinates (127). Recovering those entries needs author-to-UniProt residue
mapping through PDBe SIFTS; that is the single highest-value improvement left in the pipeline, and
it would mostly benefit exactly these under-sampled proteins.

## Paralogues reproduce earlier findings — with the template sharing quantified

Five batch-3 proteins are paralogues of batch-1/2 hits. Agreement between them is only meaningful
to the extent they rest on *different* templates, so the overlap is given explicitly:

| batch 3 | prior batch | shared entries | verdict |
|---|---|---|---|
| EHD2 vs EHD3 (both here) | — | **0 of 2 and 3** | fully independent |
| DNM2 68.6–142.9 Å (n=3) | DNM1 68.6–115.0 Å (n=3) | 1 (5A3F) | largely independent |
| ACTN4 250.2–278.6 Å (n=2) | ACTN2 250.2–278.1 Å (n=2) | 1 of 2 (1SJJ) | half-shared — see below |
| SMARCA2 36.4–84.8 Å (n=4) | SMARCA4 36.9–94.7 Å (n=10) | 3 of 4 | weak replicate |
| MYH2 47.8–81.2 Å (n=7) | MYH7 43.9–80.9 Å (n=22) | 5 of 7 | weak replicate |

**EHD2 and EHD3 are the cleanest result in the batch.** They share no template entry at all, and
independently give G-domain-to-EH of 35.6–52.8 Å and 35.5–52.5 Å, with the internal EF-hand-to-EH
distance pinned at 2.8–3.0 Å in both. Two proteins, disjoint evidence, the same ~17 Å motion.

For **SMARCA2 and MYH2** the overlap is large enough that the agreement is close to a restatement
of the earlier measurement, not a confirmation of it. They are reported, not leaned on.

## ACTN4 confirms the α-actinin AlphaFold collapse

ACTN2 in batch 2 showed AlphaFold folding a 280 Å rod down to ~57 Å. ACTN4 reproduces it:
CH2-to-EF-hand-2 at 250.2–278.6 Å from templates, AlphaFold at **56.4 Å** — outside the range,
the same ~200 Å error, in an independently predicted model.

The template evidence is partly shared and must be read carefully: ACTN4's 250.2 Å comes from
**1SJJ, the very same entry that gave ACTN2 its 250.2 Å** — one observation counted twice across
two reports, not two. The independent parts are ACTN4's second entry (9SIS, 278.6 Å, versus ACTN2's
9SIR at 278.1 Å) and its own AlphaFold model. So the *rod* is independently supported and the
*collapse* is independently reproduced, while the lower bound is not.

## Other motions

**SMARCAD1** gives the largest spread in the batch, helicase ATP-binding to helicase C-terminal at
28.2–105.0 Å over 3 entries, with AlphaFold at the compact end (29.0 Å). Three further entries put
it at 131–134 Å but were removed by the 40% identity filter, so the true range is probably wider
than reported. **DNM2** mirrors dynamin-1 with a clean three-step ladder (68.6, 122.2, 142.9 Å).
**Pyruvate carboxylase (PC)** moves its biotinyl-binding domain 43.4→80.9 Å — the expected swinging-arm
carrier motion. **XRCC6/Ku70** Ku-to-SAP spans 44.5–69.8 Å. **CAPN1** and **PIK3R1** show smaller
but consistent changes.

## Caveats

As before: centroid distance is blind to distance-preserving rotations; UniProt Domain features
miss some subdomain architectures; and pairs resting on 2 entries are provisional. Specific to this
batch — the PDB-numbering loss described above is the dominant limitation, the 40% identity filter
is demonstrably conservative for SMARCAD1, and 2 of 204 proteins returned no usable observation.
