# Review of `more_proteins/` — how reasonable is the selection analysis?

*Written 28 October 2026 by an independent session. Every number below was recomputed from the
committed CSVs, not read from the reports. Reproduction commands are in §8.*

---

## 0. Verdict

**The method is sound, the bookkeeping is honest, and every headline number reproduces exactly. But
the screen as actually run would not have found JAK.**

That is the finding that matters. Applied to JAK1, the production pipeline reports the FERM–JH1
pair as **9.0 Å — effectively rigid**. The 54.5 Å open/closed spread that the whole project rests on
was recovered in Stage 1 only by adding two sources the later stages dropped: ModelArchive models
and pooled vertebrate orthologs. The 480-kinase and 3,247-protein screens used SWISS-MODEL plus
AlphaFold, human only.

So the instrument is calibrated to miss the phenomenon it is searching for. Everything else below
is secondary to fixing that.

Second finding: **76% of the ">20 Å" hits rest on a single structure of the target protein.** The
reported range is mostly target-versus-homolog, not one protein moving. The reports flag this for
ROS1; it is systematic.

---

## 1. What reproduces, and what is genuinely good

Every headline figure in `kinome480_report.md` is exact:

| claim | recomputed |
|---|---|
| 270 domain pairs | **270** ✅ |
| across 86 proteins | **86** ✅ |
| 64 pairs > 15 Å | **64** ✅ |
| 46 pairs > 20 Å | **46** ✅ |
| AlphaFold outside in 75/269 (28%) | **75/269 = 28%** ✅ |

That is rare and worth saying. I have reviewed documents in this repository where the prose and the
tables disagreed; these do not.

**Three design choices are better than standard practice:**

1. **The 80% residue-name gate.** Catching that SWISS-MODEL serves its own models in UniProt numbering but relays PDB entries in *author* numbering is a subtle, high-consequence bug — slicing a UniProt domain range into an author-numbered file silently returns the wrong residues. The reports document it finding a spurious 26.4 Å SRC result that would have contradicted an independent PAE call. Most pipelines would have shipped that number.
2. **Tracking parent templates and collapsing on them.** The observation that only 57 distinct parents underlie 104 proteins, and that 1Y57 is the parent for 13 of them, is the kind of thing that turns an impressive-looking table into an honest one.
3. **Registering predictions before the run and reporting the two that failed** (`stage1_jak_report.md`, "Predictions versus outcome"). That is better epistemic hygiene than most published work.

**The strongest single result is correct as stated.** CSF1R Ig1↔Ig5, checked at the observation level:

```
4liq.1.A   100.0% identity    75.6 Å
AF2_v6     100.0%             78.1 Å
4wrm.1.A   100.0% identity   115.0 Å
8dfm.1.B    44.7% identity   134.8 Å
```

Two structures **of CSF1R itself**, both at 100% identity, 39 Å apart. That is a real
conformational observation and the report is right to call it the clearest single-protein case.

---

## 2. The serious problem: the production method misses JAK

The JAKs *are* in the kinome480 table, which is reassuring — but look at which pair fires:

| gene | pair | range | spread | n_parents |
|---|---|---|--:|--:|
| JAK3 | SH2 ↔ JH1 | 54.0–78.9 | **24.9** | 2 |
| JAK1 | SH2 ↔ JH1 | 53.7–78.4 | **24.7** | 2 |
| TYK2 | SH2 ↔ JH1 | 55.2–79.1 | **23.8** | 2 |
| JAK1 | **FERM ↔ JH1** | 85.2–94.2 | **9.0** | 2 |
| TYK2 | FERM ↔ JH1 | 85.0–93.5 | 8.4 | 2 |
| TYK2 | JH2 ↔ JH1 | 37.8–48.0 | 10.3 | 3 |

Stage 1 reports FERM–JH1 at **39.7–94.2 Å, spread 54.5 Å**. The kinome run reports **9.0 Å**. The
observation list explains why:

```
JAK1 FERM|Protein kinase 2 — all three observations in kinome480
  SWISSMODEL  7t6f.1.A   94.5%   85.2 Å   ← extended cryo-EM
  ALPHAFOLD   AF2_v6    100.0%   92.2 Å   ← extended
  SWISSMODEL  8ewy.1.A   94.5%   94.2 Å   ← extended
```

**All three are the extended state.** The closed arrangement enters only through ModelArchive
(`ma-l9b1f`, 40.1 Å) and through orthologs where AlphaFold happens to pick compact — neither of
which the kinome or non-kinase stages used. Stage 1 says this plainly:

> every full-length SWISS-MODEL homology model descends from 7T6F or 8EWY and is therefore extended
> by construction … **no SWISS-MODEL template lineage yields the closed state**

The consequence is not drawn, and it is the important one: **a second JAK, screened by this
pipeline, would be reported as rigid.** Any protein whose alternative state exists only in
ModelArchive, in a non-human ortholog, or in no deposited model at all is invisible. Since the
project's premise is that JAK's closed state is barely represented in the PDB, the screen is
systematically blind to exactly the class of protein it wants.

**This is fixable and should be fixed before the candidate list is used.** Add ModelArchive and
ortholog pooling to the production path, re-run the 86 multi-domain-covered kinases, and see how
many "invariant" verdicts flip. Stage 1 took FERM–JH1 from 10 observations to 41 by pooling; the
same lift applied kinome-wide is the single highest-value action here.

---

## 3. The second problem: most hits are homolog comparisons

For each of the 46 pairs with spread > 20 Å, I restricted to templates at **≥99% identity** — i.e.
structures of the target protein itself — and recomputed the range:

| outcome | pairs |
|---|--:|
| **fewer than 2 same-protein templates** — range is target vs homolog | **35 (76%)** |
| survives (≥50% of spread retained) | 8 |
| **collapses** (<50% retained) | 3 |

The 8 that survive are only **4 distinct biological systems**: CSF1R Ig-domain pairs (5 pairs),
EPHA2 kinase↔SAM, EPHB2 LBD↔FN3, INSR FN3-1↔FN3-?. So the headline "46 pairs exceed 20 Å" is, on
same-protein evidence, closer to **four observations**.

The three that collapse matter because two are presented as well-supported:

| pair | reported | same-protein only |
|---|---|---|
| **INSR** FN3-2↔FN3-3 | 35.4–67.7 (**32.3 Å**, "best-sampled at 25 parents") | 46–60 (**14 Å**) |
| IGF1R FN3-1↔FN3-? | 26.6–53.2 (26.6 Å) | 30–42 (12 Å) |
| IGF1R FN3-3↔FN3-? | 38.0–63.8 (25.8 Å) | 48–53 (**6 Å**) |

INSR's 25 parents are real, but most are structures of *relatives*. Its own conformational range is
less than half what the table reports.

### The "cleanest new find" needs restating

`kinome480_report.md` calls PRKCA/PRKCG "the cleanest new find … across **five** parent templates
(8SE1, 8SE3, 8SE4, 3PFQ)". The observation list:

```
PRKCA C2|Protein kinase
  ALPHAFOLD   AF2_v6     100.0%   39.4 Å
  SWISSMODEL  8se3.1.A    80.5%   40.3 Å
  SWISSMODEL  8se1.2.A    80.7%   50.7 Å
  SWISSMODEL  8se4.2.A    80.5%   56.1 Å
  SWISSMODEL  8se1.1.A    80.7%   57.5 Å
  SWISSMODEL  3pfq.1.A    80.6%   76.4 Å
```

**Zero experimental templates of PRKCA.** All five are at 80.5–80.7% identity — a paralog. And
`8se1.1.A` / `8se1.2.A` are two chains of one PDB entry, so it is **four entries, not five**.

The underlying claim is probably still true — four structures of a close paralog spanning 36 Å is
good evidence that PKC's C2↔kinase arrangement is mobile, and at 80% identity transfer is
reasonable. But "five parent templates" reads as five structures of PRKCA, and that is not what the
data says. The honest version: *"36 Å across four entries of an 80%-identity paralog; no
experimental PRKCA structure spans the pair."*

### A quantified but minor defect

`nonkinase100b_report.md` says chain suffixes were collapsed to distinct PDB entries after batch 1.
**The kinome480 tables were not re-run.** 88 of 270 pairs (33%) have `n_parents` exceeding their
distinct-entry count — INSR 26→22, LRRK2 35→32, IGF1R 9→7.

To its credit this changes no conclusion: after collapsing, **all 46 of the >20 Å pairs still retain
≥2 distinct experimental entries.** `n_parents` is inflated by up to 15%, but no finding depends on
the inflation. Worth a footnote, not a re-run.

---

## 4. Is "spread" measuring mobility or sampling?

A fair worry: more templates mechanically find more spread. Tested:

```
Spearman(n_parents, spread) = +0.249   p = 3.5e-05   n = 270
```

Weak — so **spread is not primarily a sampling artefact.** Good. But the bucket breakdown is
revealing:

| n_parents | pairs | median spread | max spread |
|---|--:|--:|--:|
| 2 | 123 | **1.3 Å** | **109.2 Å** |
| 3–4 | 95 | 10.3 Å | 59.3 Å |
| 5–9 | 31 | 3.5 Å | 36.1 Å |
| 10+ | 21 | 5.5 Å | 32.3 Å |

**Two-parent pairs are mostly rigid (median 1.3 Å) yet produce the largest outliers (109 Å).** That
is the signature of a heavy-tailed error process: with two observations, one bad template produces
an extreme. All four 100 Å+ ROS1 values sit here, on two 80%-identity templates — which the report
does flag.

Practical rule the tables should enforce rather than merely caption: **do not report a spread from
2 parents as a finding.** That removes 17 of the 46 >20 Å hits.

---

## 5. Three conceptual issues

### 5.1 Rotation blindness is under-stated

The README states it: centroid distance is "blind to a pure hinge rotation that preserves the
distance". The consequence deserves more weight than a caveat line.

**JAK's own JH2–JH1 pair — the drug-relevant motion, the basis of the allosteric TYK2 inhibitor work
and of our P982A result — spreads only 10.3 Å, which ranks 87th of 270 pairs (top 32%).** Nothing
would flag it. The pair that *does* fire for JAK is SH2↔JH1, a lever-arm consequence rather than
the motion of interest.

So the metric finds proteins whose domains **translate**, and misses those whose domains **rotate**.
A JAK-like protein of the second kind scores as rigid. Adding a superposition-based measure (JH1 Cα
RMSD after superposing JH2 — the metric already used in `reference_states.md`) on the ~155
committed structures would close this, and the structures are already downloaded.

### 5.2 The non-kinase screen ranks by data availability

`nonkinase_screen_full.csv` has 3,247 proteins with columns `n_parents, n_entries, n_dom, n_pdb`,
and the batches are "the next 100 proteins … by distinct multi-domain parent template count". That
is a ranking by **how well-studied a protein is**, not by how mobile it is.

The consequence shows in the results: integrins, CFTR, P-glycoprotein, dynamin, α-actinin. Their
conformational cycles are textbook. The screen is confirming known biology — which is a legitimate
*validation* of the method, but it is not discovery, and it will systematically miss a mobile
protein with two structures the way JAK has two.

Ranking by data availability also interacts badly with §4: the proteins most likely to yield a
*novel* finding are those with exactly 2–3 entries, which is precisely the regime where the metric
is least reliable.

### 5.3 The PAE evidence is not in this folder

You described the selection as using "pdb-templates for gene and his homologs, **and pae plots**".
PAE appears in `more_proteins/` only as three retrospective mentions — "the independent PAE
result", "the earlier PAE call that SRC is a single rigid unit", "the high inter-module PAE". **No
PAE data, plots, or per-gene scores are committed here.**

That is a missed cross-validation, and it would be the most valuable one available: **PAE is
independent of template availability.** It comes from AlphaFold's own confidence and is defined for
every protein, including the ones with zero multi-domain templates — the 12 criterion-3 failures and
the type-III receptors the method declares unassessable. If inter-module PAE and centroid spread
agree where both exist, each validates the other; where they disagree, that is the interesting list.

Joining the two is the second-highest-value action after §2.

---

## 6. Self-criticism in the reports: unusually good, with one gap

Worth recording what the reports already get right, so a reader does not mistake this review for a
list of things they missed:

- numbering-gate bug, diagnosed and fixed, with the spurious SRC number named
- parent-template non-independence, with the 1Y57-for-13-proteins example
- rotation blindness
- UniProt Domain features omitting RTK ectodomains (EGFR/ERBB2/ERBB4/LTK absent)
- "no template anywhere in the kinome" spans ectodomain + kinase for type-III receptors
- ROS1's 109 Å called out as "the largest raw numbers but the weakest support"
- ACTN2's 190 Å AlphaFold error "checked specifically because the number looked implausible"
- the ModelArchive closed JAK1 model recorded as **missed in the first pass**
- criterion-3 scoring applied to the project's own target table, reporting **12 failures including three Tier 1 entries**
- NF1 has no AlphaFold value (2,839 residues exceeds the single-fragment limit)
- AlphaFold flipping state between >90%-identity orthologs, and between integrin paralogs

The gap is not candour, it is **consequence**. The same-protein-template limitation is stated for
ROS1 but not measured across the set; the SWISS-MODEL-lineage limitation is stated for JAK but not
carried forward as "therefore this screen cannot find a second JAK". Both are one computation away
from being quantified, and both change what the candidate list means.

---

## 7. Is it reasonable? — direct answer

**As a method: yes.** Rotation-invariant distances over gated, provenance-tracked templates is a
defensible way to survey inter-domain mobility at proteome scale, and the execution is careful.

**As a selection of JAK-like candidates: not yet**, for three reasons in priority order:

1. **It cannot detect the JAK phenomenon.** Demonstrated on JAK itself: 9.0 Å where the truth is 54.5 Å. Fix by adding ModelArchive and ortholog pooling to the production path.
2. **It measures translation, not rotation.** JAK's own functionally important pair ranks in the top 32% — i.e. unremarkable. Fix by adding the superposition metric already used elsewhere in the project.
3. **It ranks candidates by how well-studied they are.** Fix by reporting spread-per-entry or by stratifying the ranking on `n_entries`.

And two accuracy fixes: **restate PRKCA/PRKCG and INSR/IGF1R** on same-protein evidence, and
**suppress 2-parent spreads** from the headline counts.

### If I were to do one thing

Re-run the 86 multi-domain-covered kinases with ModelArchive + orthologs **and** the superposition
metric, then check how many change verdict. If JAK goes from "FERM–JH1 rigid at 9 Å" to "54 Å", the
same lift will surface candidates the current table calls invariant — and those, not the integrins,
are where a second JAK would be hiding.

---

## 8. Reproduction

```python
import csv, collections, re
pv = list(csv.DictReader(open('kinome480_pair_variation.csv')))
cd = list(csv.DictReader(open('kinome480_centroid_distances.csv')))
by = collections.defaultdict(list)
for r in cd: by[(r['acc'], r['pair'])].append(r)

# 3: how many >20 A pairs have <2 same-protein templates
big = [r for r in pv if float(r['spread']) > 20]
for r in big:
    self_ = [float(o['dist']) for o in by[(r['acc'], r['pair'])]
             if float(o['identity']) >= 99]
    print(r['gene'], r['pair'], r['spread'], len(self_),
          (max(self_) - min(self_)) if len(self_) >= 2 else None)

# 3 (minor): chain-suffix inflation
pdbid = lambda p: re.match(r'^([0-9a-zA-Z]{4})\.', p).group(1).lower()
for r in pv:
    obs = by[(r['acc'], r['pair'])]
    if len({o['parent'] for o in obs}) > len({pdbid(o['parent']) for o in obs
                                              if '.' in o['parent']}):
        print('inflated:', r['gene'], r['pair'], r['n_parents'])

# 4: sampling artefact
from scipy.stats import spearmanr
print(spearmanr([int(r['n_parents']) for r in pv],
                [float(r['spread']) for r in pv]))
```

| check | result |
|---|---|
| all five kinome480 headline numbers | reproduce exactly |
| JAK1 FERM–JH1 in production pipeline | 9.0 Å over 3 observations, all extended |
| >20 Å pairs with <2 same-protein templates | 35/46 (76%) |
| >20 Å pairs that collapse on same-protein restriction | 3/11 testable |
| PRKCA experimental templates at ≥99% identity | **0** |
| CSF1R Ig1↔Ig5 same-protein templates | 2 at 100% identity, 39 Å apart ✅ |
| chain-suffix inflation in kinome480 | 88/270 pairs; changes no conclusion |
| Spearman(n_parents, spread) | +0.249 |
| PAE data committed under `more_proteins/` | none |
