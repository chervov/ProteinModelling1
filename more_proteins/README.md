# more_proteins — inter-domain centroid variation across the human kinome

Measures how far a protein's domains move relative to one another, by comparing the
**inter-domain centroid distance** of the same domain pair across many structural models of the
same protein. Centroid distance is rotation-invariant, so no superposition is required; the cost
is that it is blind to a pure hinge rotation that preserves the distance, which is why the JAK
JH2–JH1 pair looks quiet (10.8 Å) while FERM–JH1 does not (54.5 Å).

## Method

1. **Domains** come from UniProt `Domain` features (`rest.uniprot.org/uniprotkb/<acc>.json`).
2. **Templates** come from the SWISS-MODEL Repository
   (`swissmodel.expasy.org/repository/uniprot/<acc>.json`): its own homology models, PDB-relayed
   entries, each labelled with the **parent template** it was built on. The AlphaFold v6 model is
   treated as one further template. ModelArchive entries are fetched as
   `www.modelarchive.org/doi/10.5452/<id>.cif`.
3. **Numbering gate.** Every candidate chain is scored on how often its residue *names* match the
   UniProt sequence at their own residue numbers; a chain is used only above **80% agreement**.
4. **Centroids** are Cα means over each UniProt domain range, requiring ≥50% of the domain present.
5. **Independence.** Models sharing a parent template are collapsed to one observation, and only
   templates at **≥40% identity** are used.

## Two pitfalls that will bite a re-runner

**Residue numbering is not uniform across SWISS-MODEL file types.** Models it builds itself and
AlphaFold models are in UniProt numbering (match ≈ 1.00). Files it *relays for PDB entries* are in
PDB **author** numbering, which for most entries is offset (match 0.05–0.09). Slicing UniProt
domain boundaries into an author-numbered file silently returns coordinates for the wrong
residues. This produced a spurious 26.4 Å SH3-to-kinase spread for SRC that would have contradicted
the independent PAE result; under the gate the same pair spans 36.3–37.7 Å and SRC is rigid. The
80% match gate handles this per file, and also picks the correct chain in complexes, where
selecting by residue-number overlap can land on a partner protein.

**Parent templates are not independent observations.** Only 57 distinct parents underlie the
original 104-protein set, and popular ones are reused widely — 1Y57 is the parent for models of 13
different proteins. When two paralogs report the same distance to 0.1 Å (e.g. 85.2 Å for BTK, TEC
and ITK on parent 8GMB) that is one conformational observation seen three times. Always read
`n_parents` alongside `spread`.

A third, narrower caveat: UniProt `Domain` features do **not** cover receptor tyrosine kinase
ectodomain subdomains, so EGFR, ERBB2, ERBB4 and LTK appear single-domain and are absent from these
tables despite being strong candidates. Switching to InterPro boundaries would close this.

## Files

| file | contents |
|---|---|
| `kinome480_report.md` | full reviewed kinome (480 proteins): method, results, limits |
| `kinome480_centroid_distances.csv` | every observation: acc, gene, provider, parent, identity, pair, distance |
| `kinome480_pair_variation.csv` | per (protein, pair): n_parents, min, max, spread, AlphaFold value and whether it is outside the range |
| `kinome480_variation.png` | largest-variation pairs, structural range vs AlphaFold |
| `criterion3_coverage.csv` | the 41 genes of `kinase_targets_for_modelling.md` scored for measured multi-domain coverage |
| `stage1_jak_report.md`, `jak_*.csv`, `jak_stage1.png` | JAK family: block rigidity, open/closed states, ortholog pooling |
| `search2_104.md`, `kinase104_*` | the 104-kinase set (`_regated` uses the numbering gate and supersedes the earlier file) |
| `stage3_next100_report.md`, `kinase_next100_*` | kinases 105–204 by JAK similarity |
| `kinase_rest276_centroid_distances.csv` | the remaining 276 reviewed kinases |

Downloaded coordinate files (~3,000) are deliberately not committed; they are reproducible from the
accession and parent-template columns.

## Headline results

- The JAK **FERM–SH2–JH2 block is rigid** (internal SDs 0.7–2.1 Å) while JH1 moves against it,
  displacement growing with distance along the block — a hinge at the JH2–JH1 junction.
- **233 of 480** kinases have ≥2 annotated domains; **270 pairs across 86 proteins** have ≥2
  distinct parent templates; **46 pairs exceed 20 Å** of spread.
- Best-evidenced motions: **PRKCA/PRKCG** C2↔kinase (40.3–76.4 Å, 5 parents), **CSF1R** Ig1↔Ig5
  (75.6 vs 115.0 Å between two 100%-identity structures), **INSR** FN3-2↔FN3-3 (25 parents),
  the **Eph** receptors LBD↔FN3-2 (26–34 Å across 11 paralogs).
- **AlphaFold falls outside the template-derived range in 28% of pairs** (75/269), directionally by
  family — compact for Tec SH3↔kinase, extended for Eph LBD↔FN3-2 — and it reproduces the AKT1–3
  PH↔kinase arrangement ~10 Å away from an experimental set that is invariant across 11 parents.
- **No template anywhere in the kinome** spans an ectodomain domain together with the kinase domain
  for a type-III receptor, so that arrangement is unassessable by this method.
