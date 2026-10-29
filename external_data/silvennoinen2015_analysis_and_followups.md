# Silvennoinen & Hubbard 2015 — analysis, and where the structural line went

*Compiled 29 October 2026. Citation counts are OpenAlex values retrieved on that date and will
drift. Every paper below was resolved through OpenAlex or NCBI; none is cited from recollection.*

**Paper:** Silvennoinen O, Hubbard SR. *Molecular insights into regulation of JAK2 in
myeloproliferative neoplasms.* Blood 2015;125(22):3388–3392.
[10.1182/blood-2015-01-621110](https://doi.org/10.1182/blood-2015-01-621110) ·
PMID 25824690 · PMC4447858 · **review** · 41 references · ~80 citations.

> **Scope limit, stated up front.** PMC serves only the abstract and metadata for this article
> (1,945 bytes; `open-access: no`, no PDF). The body was **not readable**. Everything below is
> built from the abstract, the complete 41-reference list (retrieved in full), and the primary
> literature those references point to. No claim is made about the review's figures or internal
> argument.

## 1. What it is

A *Blood* **Spotlight** review, not primary research. The authorship is the point: Silvennoinen and
Hubbard led the two labs that produced most of the JAK2 pseudokinase structural work, so this is a
synthesis of their own results. The abstract's claim is narrow — mutations in the **JH2 pseudokinase
domain** drive constitutive JAK2 activation, and the mechanism had been unclear.

"Its methods" are therefore the methods it reviews:

| approach | key reference in its list | cites |
|---|---|--:|
| X-ray crystallography of the **isolated JH2 domain** | Crystal structures of the JAK2 pseudokinase domain and the pathogenic mutant V617F (2012) | 244 |
| Biochemical dissection of **JH2→JH1 autoinhibition** | Molecular basis for pseudokinase-dependent autoinhibition of JAK2 (2014) | 162 |
| JH2 as a **real dual-specificity kinase** | The pseudokinase domain of JAK2 is a dual-specificity protein kinase (2011) | 277 |
| **ATP binding to JH2** required for pathogenic activation | (2015) | 112 |
| V617F mechanism — π-stacking, F595 | (2010) | 44, 90 |
| Receptor-driven activation | Mechanism of Activation of Protein Kinase JAK2 by the Growth Hormone Receptor (2014) | 418 |

## 2. Does it extend to the other JAKs? It already had

Answerable from the review's own reference list rather than speculation — by 2015 the
isolated-domain approach had already crossed the family:

- **TYK2 JH2–JH1**, Lupardus et al. 2014 PNAS, 229 cites
  ([10.1073/pnas.1401180111](https://doi.org/10.1073/pnas.1401180111)) — the first two-domain
  structure. **This is PDB 4OLI, the "closed" TYK2 template used by this project's centroid screen.**
- **JAK1** — *Structure of a pseudokinase-domain switch that controls oncogenic activation of JAK
  kinases* (2013), 109 cites.
- **JAK3** — pseudokinase-domain mutations characterised 1997–2000.

So the domain-level method transferred immediately. What did **not** transfer was the whole
molecule: crystallography of isolated domains cannot see how FERM–SH2, JH2 and JH1 sit relative to
one another.

## 3. The structural follow-up line (verified)

Note that the review's own ~80 citations are overwhelmingly clinical/MPN — diagnostics, inhibitor
trials, case reports. The structural lineage must be traced through its *references* instead.
Tracing forward from Lupardus 2014 (236 citers) and the 2012 JAK2 JH2 structure (254 citers):

| year | work | venue | cites | contribution |
|---|---|---|--:|---|
| 2022 | Structure of a Janus kinase cytokine receptor complex reveals the basis for dimeric activation | **Science** | **186** | the step change — **full-length JAK1 dimer by cryo-EM**; this is 7T6F / 8EWY, already in this project's template set |
| 2022 | Unlocking the secrets to Janus kinase activation | Science | 6 | commentary on the above |
| 2023 | Constitutive activation and oncogenicity mediated by loss of helical structure | eLife | 10 | refines the V617F mechanism |
| 2024 | Molecular basis of JAK2 activation in erythropoietin receptor and pathogenic JAK2 signaling | Sci. Adv. | 26 | extends the receptor-complex approach from JAK1 to **JAK2** |
| 2024 | Structural basis of MPL activation by thrombopoietin | Blood Vessels Thromb. | 6 | the receptor side |
| 2024 | **A novel approach to study multi-domain motions in JAK1's activation mechanism based on energy landscape** ([10.1093/bib/bbae079](https://doi.org/10.1093/bib/bbae079)) | Brief. Bioinform. | 9 | **closest to this project's own method** — inter-domain motion, but via energy landscapes and on JAK1 only |
| 2024 | The JAK-STAT pathway: from structural biology to cytokine engineering | Signal Transduct. Target. Ther. | 143 | current synthesis |
| 2025 | Molecular Dynamics Simulation Analysis of JAK1 Initial Activation | Life | 0 | dynamics |

## 4. Beyond the JAKs — the non-JAK pseudokinases

The transferable idea is not "JAK2 has a pseudokinase" but **"a catalytically dead domain regulates
its active neighbour in cis."** The generalisation runs through another paper in the same reference
list — Murphy et al., *A robust methodology to subclassify pseudokinases based on their
nucleotide-binding properties*, Biochem J 2013
([10.1042/bj20131174](https://doi.org/10.1042/bj20131174)), 274–278 cites. Of its 274 citing works,
97 are system-specific and non-JAK. They are **very unevenly distributed.**

### MLKL — the system that went furthest

The closest structural analogue to JAK2: a dead pseudokinase domain restraining an adjacent
effector, released by mutation.

| year | work | venue | cites |
|---|---|---|--:|
| 2014 | Activation of the pseudokinase MLKL unleashes the four-helix bundle domain | PNAS | **598** |
| 2018 | Conformational switching of the pseudokinase domain promotes human MLKL activation | Nat. Commun. | 192 |
| 2016 | The pseudokinase MLKL mediates programmed hepatocellular necrosis | J. Clin. Invest. | 157 |
| 2016 | Evolutionary divergence of the necroptosis effector MLKL | Cell Death Differ. | 129 |
| 2021 | Human RIPK3 maintains MLKL in an inactive conformation prior to cell death | Nat. Commun. | 121 |
| 2019 | Viral MLKL homologs subvert necroptotic cell death | Cell Rep. | 120 |
| 2021 | Conformational interconversion of MLKL and disengagement from RIPK3 | Nat. Commun. | 106 |
| 2020 | Identification of MLKL membrane translocation as a checkpoint | PNAS | 94 |
| 2020 | **Distinct pseudokinase domain conformations underlie divergent activation** | Nat. Commun. | 62 |

That last one compares pseudokinase-domain conformations **across orthologues** to explain divergent
activation — the same comparative design this project applies to the JAKs, already executed for MLKL.

### The others got much less

- **Tribbles** — real but modest: TRIB1's recruitment of C/EBPα (*Structure* 2015, 110);
  TRIB2 binds ATP and autophosphorylates (*Biochem J* 2015, 77); review (*Trends Cell Biol* 2016, 232).
- **HER3 / ERBB3** — allosteric activation structure (*JBC* 2011, 454) and the **HER2–HER3–NRG1β
  complex revealing a dynamic dimer interface** (*Nature* 2021, 139). But this is receptor-dimer
  work, not intramolecular pseudokinase→kinase regulation.
- **STRADα–LKB1–MO25** — peaked early: *Science* 2009 (368) and the ATP/MO25α conformational-state
  paper (*PLoS Biol* 2009, 148). Little since.
- **KSR–RAF** — the conspicuous gap. A targeted search for KSR scaffold / BRAF / MEK cryo-EM returns
  only **20 matches**, mostly reviews; the nearest primary work is a Ras–Raf signalosome model
  (*NSMB* 2021, 70). Thin, for a system this central to cancer biology.
- RAF generally: *Kinases and Pseudokinases: Lessons from RAF* (*Mol. Cell. Biol.* 2014, 140).

## 5. Two conclusions

**The method generalised; the field fragmented.** Isolated-domain crystallography transferred
instantly across the JAKs and to every pseudokinase above, but nobody carried the *comparative*
step across families. MLKL's orthologue comparison and the JAK structural work both cite Murphy 2013
and largely not each other.

**The regulatory logic is not one logic.** JAK2 JH2 regulates a kinase in cis; MLKL's regulates a
pore-forming helical bundle; TRIB1's regulates a degron; STRADα's activates a *different* protein in
trans. Only the first two are structurally the same problem. This bounds the method: inter-domain
distance is the right instrument for cis-regulation and the wrong one for trans-activation.

## 6. Bearing on this project

The review's generation of methods could see one domain at a time, and the field needed until 2022
for a full-length JAK. The centroid screen in `more_proteins/` measured the whole-molecule question
directly: **JH1 moves against a rigid FERM–SH2–JH2 block** (FERM–JH2 SD 0.8 Å versus FERM–JH1 spread
54.5 Å), placing the hinge at the JH2–JH1 junction — using 4OLI at the closed end and 7T6F/8EWY at
the open end, i.e. the products of exactly this lineage. The `Shan2014JAK1JAK2` folder in this repo
is a third pillar of the same reference list.

**Two actionable gaps:**

1. **No cross-family comparison exists.** The Briefings paper does JAK1 alone; the cryo-EM papers do
   one receptor complex at a time. A systematic JH2↔JH1 geometry comparison across all four JAKs
   *and* their orthologues is absent from this citation tree — and the data for it is already in
   `more_proteins/jak_all_observations.csv`.
2. **ERBB3 is in the 480-kinase set but drops out of the centroid screen**, because UniProt `Domain`
   features do not annotate RTK ectodomain subdomains — EGFR, ERBB2, ERBB4 and LTK vanish silently
   for the same reason. Switching those to InterPro boundaries would put the HER family in scope, and
   the 2021 HER2–HER3 structure supplies a template with a documented dynamic interface to test.
