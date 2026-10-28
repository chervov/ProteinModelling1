# Precomputed stability / ddG for HUMAN variants — what you can download instead of computing

*Compiled 28 October 2026. Every row count, file size, HTTP status and column list below was obtained
by fetching the resource from this sandbox, not quoted from a paper. Where a number could only be
taken from a publication or a repository README, it is labelled as such. Numbers I could not verify
are marked **unverified**, and the few figures that are bounds or arithmetic on measured counts
rather than direct counts say so explicitly.*

Training and benchmark sets (ThermoMPNN `data_all/`, FireProtDB, S669, Ssym) are covered in the
earlier memo `ddg_precomputed.md` and are not repeated here.

## Short answer

One download gives near-proteome coverage: **ProtVar's FoldX table at the EBI**,
208,792,558 precomputed ddG values over 20,437 UniProt accessions, CC BY 4.0, no registration.
It covers **76.0 % of reviewed human canonical residues**. Everything else is either a small
experimental set (Domainome, MaveDB/ProteinGym) or unreachable from here (RaSP, MAVISp).

---

## Resource table

| Resource | Kind | Proteins | Variants | Keyed to | Sign / units | Licence | Reachable |
|---|---|--:|--:|---|---|---|---|
| **ProtVar FoldX** (EBI) | predicted (FoldX v5 on AF2) | 20,437 acc. | 208,792,558 rows | UniProt acc + canonical-isoform position | **+ = destabilising**, kcal/mol | CC BY 4.0 | yes, 200 |
| **ProtVar per-gene bundles** | predicted + clinical annotation | 1,048 genes | ~3.9 k rows/gene | genomic coord + UniProt canonical isoform | as above, inside one column | CC BY 4.0 | yes, 200/206 |
| **ProtVar MAVE mirror** | experimental (MaveDB v4) | 537 human acc. | 3,423,249 human rows | UniProt acc + offset | assay score, **not ddG** | CC0 1.0 | yes, 200 |
| **MaveDB bulk dump** | experimental | all MaveDB | 1.81 GB zip | MaveDB URN | assay score | CC0 1.0 | yes, 200 |
| **Human Domainome 1.0, Table 2** | experimental (aPCA) | 434 acc. / 522 domains | 546,537 missense | UniProt acc + position | fitness (normalised), **not ddG** | CC BY 4.0 | yes, 200 |
| **Human Domainome 1.0, Table 4** | predicted (homolog-averaged) | 1,761 genes | 4,107,436 rows | UniProt acc + gene + position | **+ = destabilising**, kcal/mol (scaled) | CC BY 4.0 | yes, 200 |
| **ProteinGym substitutions** | experimental (DMS) | 81 human mnemonics | 329,664 human singles | UniProt *mnemonic* only | assay score, **not ddG** | MIT | yes, 200 |
| **RaSP human proteome** | predicted (deep learning → Rosetta) | 23,391 (README) | ~230 M (abstract) | UniProt acc (AF2 UP000005640) | + = destabilising, kcal/mol | **unverified** | **no — TLS reset** |
| **MAVISp database** | predicted (FoldX + Rosetta) | **unverified** | **unverified** | UniProt acc | + = destabilising | **unverified** | **no — host blocked** |
| **Mega-scale human subset** | experimental (cDNA proteolysis) | 50 PDB domains | 46,955 rows | PDB id, no UniProt | see prior memo | — | yes, via ThermoMPNN |

---

## 1. ProtVar FoldX — the one to download

**URL** `https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/2025.02.10_foldx_energy.csv.gz`
— HTTP 200, **1.5 GB** gzipped. Sample (100 lines, HTTP 200):
`.../2025.02.10_foldx_energy_sample.csv`. Licence CC BY 4.0 (`/pub/databases/ProtVar/LICENCE`).

Verified by streaming and counting the **entire** file:

| quantity | value |
|---|--:|
| rows | 208,792,558 |
| unique UniProt accessions | 20,437 |
| (accession, position, fragment) groups | 10,989,614 |
| **distinct (accession, position) pairs** | **9,091,699** |
| groups carrying exactly 19 rows and 19 distinct mutant residues | 10,988,603 (99.9908 %) |
| rows with pLDDT < 70 | 34,838,191 (16.7 %) |
| rows with pLDDT ≥ 70 | 173,954,367 |

Columns (from the file header, not the README):
`uniprot_accession, uniprot_position, alphafold_fragment_id, alphafold_fragment_position, wild_type, mutated_type, foldx_ddg, plddt`

**Sign convention and units.** Per the directory README: *"The ddg between the wild type and variant
sequence. Positive values indicate that the variant sequence has a destabilising effect."* FoldX v5.0
on AlphaFold2 models, so the unit is FoldX kcal/mol.

**Keyed to** the UniProt canonical isoform position (README) and to the AlphaFold2 model fragment.
Joining to an accession list is a direct string match on `uniprot_accession`; no mapping needed.
Non-canonical isoforms are **not** covered.

### Three gotchas, all verified here

1. **The README is out of date and contradicts the data.** It states *"Only positions with pLDDT over
   70 are included"*, and describes a `2024.05.28` release. The current `2025.02.10` file contains
   34,838,191 rows with pLDDT < 70 — including the very first rows of the sample file (pLDDT 56.90).
   Filter on `plddt` yourself; do not assume it was done.
2. **Rows double-count positions in long proteins.** AlphaFold2 fragments overlap, and the file has
   one row per *fragment* position. Counted over the whole file: 10,989,614 (accession, position,
   fragment) groups resolve to only **9,091,699 distinct (accession, position) pairs**, so
   **1,897,915 groups — 17.3 % — are repeat appearances of a position in a second fragment**.
   A separate full pass confirmed that 10,988,603 of the 10,989,614 groups (99.99 %) carry exactly 19
   rows and 19 distinct mutant residues, so the redundancy is ~36.1 million rows, and the number of
   distinct (accession, position, mutant) triples is **between 172,724,083 and 172,742,281** — a
   bound, not a direct count, since counting triples outright needs more memory than this machine
   has. Deduplicate on `(uniprot_accession, uniprot_position, mutated_type)` before counting or
   averaging, or long proteins will be silently over-weighted.
3. **The API examples in the README return 404.** Both the README's own example
   `https://www.ebi.ac.uk/ProtVar/api/foldx/Q9NUW8/493?variantAA=R` and the equivalent for P04637
   return HTTP 404 (the Swagger UI at `/ProtVar/api/` returns 200). Per-variant lookups must go
   through the bulk file or the current Swagger-documented paths, not the README.

## 2. ProtVar per-gene annotation bundles — the ClinVar/gnomAD-linked route

**URL** `https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/1048genes_annotations.tar.gz`
— **538 MB**, HTTP 200 (206 on range request). Undocumented: the 2024 README does not mention it.

Verified by decompressing the first 2 MB and extracting the first member: the archive holds one
`<ACCESSION>-fun-pop-str.csv.zip` per gene ("function–population–structure"). The first member,
`A2IDD5-fun-pop-str.csv.zip` (CCDC78), contains 3,943 rows and **43 columns**, including:

`Chromosome, Coordinate, Reference_allele, Alternative_allele, Gene, CADD_phred_like_score,
MANE_transcript, Uniprot_canonical_isoform_(non_canonical), Alternative_isoform_mappings,
Amino_acid_position, Amino_acid_change, Residue_function_(evidence), Predicted_pockets(...),
Predicted_interactions(...), `**`Foldx_prediction(foldxDdg;plddt)`**`, Conservation_score,
AlphaMissense_pathogenicity(class), EVE_score(class), ESM1b_score, Genomic_location,
Diseases_associated_with_variant, Variants_colocated_at_residue_position, Position_in_structures`

This is the closest reachable thing to a ClinVar/gnomAD-joined stability table: FoldX ddG sits
alongside GRCh38 coordinates, MANE transcript, disease association and three pathogenicity
predictors, with explicit alternative-isoform mappings. Restricted to 1,048 genes (filename; the
per-gene list was not enumerated — **unverified** which 1,048).

## 3. Experimental human data

### Human Domainome 1.0 (Beltran et al., Nature 2025, [10.1038/s41586-024-08370-4](https://doi.org/10.1038/s41586-024-08370-4) — resolves, CrossRef 200)

Zenodo [10.5281/zenodo.13629491](https://zenodo.org/records/13629491) (HTTP 200, CC BY 4.0);
latest version of the same concept is `10.5281/zenodo.14356805`, which ships the same tables zipped
and smaller. Both reachable. Downloaded and read in full:

**Table 2 — aPCA abundance (experiment).** `Supplementary_Table_2_fitness_scores_normalized_domainranks.txt.zip`,
29.3 MB zipped / 116.3 MB raw. **602,882 rows**, of which **546,537 single missense** (the rest are
stops/synonymous), **522 domains**, **434 UniProt accessions**, 29,699 distinct positions. Domains
span 19–97 positions (median 58). Columns: `domain_ID, uniprot_ID, aa_seq, wt_aa, position, mut_aa,
STOP, input/output counts ×3, mean_input_count, fitness, fitness_sigma, normalized_fitness,
normalized_fitness_sigma, quality_rank`. The score is **normalised aPCA fitness, not ddG**; lower =
less abundant. (The paper headlines 563,534 variants; my verified single-missense count on the
distributed table is 546,537 — the difference is a filtering definition I did not reconstruct.)

**Table 4 — homolog-averaged ddG (prediction).** `Supplementary_Table_4_homolog_predictions.txt.zip`,
20.3 MB zipped / 319.1 MB raw. **4,107,436 rows**, **1,761 UniProt accessions = 1,761 gene symbols**,
7,271 Pfam domain entries, 216,607 distinct positions. Columns: `PFAM_entry, uniprot_ID, gene_ID,
pos, wt_aa, mut_aa, mean_kcalmol_scaled, std_kcalmol_scaled`.

*Sign convention established empirically* (the column name does not state it): mean value by mutant
residue runs from Glu −0.104 and Asp −0.038 up to Pro +0.364 and Trp +0.424 kcal/mol, and wild-type
Cys is the most positive (+0.680). Proline and tryptophan substitutions being the most positive means
**positive = destabilising**, the standard convention. Median +0.088, 1st–99th percentile −0.557 to
+1.124 kcal/mol.

This table is the most useful *human, UniProt-keyed, kcal/mol* resource after ProtVar — but it is
domain-restricted (see coverage, below).

### MaveDB, via ProtVar's mirror

`https://ftp.ebi.ac.uk/pub/databases/ProtVar/mave/` (HTTP 200). Two files per release:
`2026_10_15_protvar_mave_score.csv.gz` (98 MB) and `2026_10_15_protvar_mave_identifier.csv` (157 kB).
Imported from the MaveDB v4 export, CC0 1.0, restricted to score sets whose target maps to UniProt.

Verified from the identifier file: **1,993 score sets**, of which **1,173 are human (taxid 9606)**,
covering **537 unique UniProt accessions** and **3,423,249 variant rows**. Columns give
`uniprot` plus `uniprotoffset` — *the offset you must add to MAVE positions to get UniProt
positions* — which is exactly what makes this joinable; the raw MaveDB HGVS strings are relative to
each study's own target sequence. Score file columns: `urn, variant_num, hgvs_nt, hgvs_pro,
is_simple_p, score` (`is_simple_p = t` marks single substitutions).

Scores are study-specific functional values, **not ddG and not comparable across score sets**.
VAMP-seq abundance assays are in here, but you must select them by study.

Full MaveDB dump: Zenodo record 18511521, `mavedb-dump.20260206153444.zip`, **1,805.1 MB**, CC0
(HTTP 200). `api.mavedb.org` is blocked by the sandbox allowlist; the Zenodo dump and the ProtVar
mirror make it unnecessary.

### ProteinGym

Distributed from Zenodo [10.5281/zenodo.15293562](https://zenodo.org/records/15293562) (HTTP 200,
**MIT licence**) and from `https://marks.hms.harvard.edu/proteingym/ProteinGym_v1.3/` (HTTP 200 after
the domain was allowlisted on request; the un-versioned path 404s and the directory index is 403).
`DMS_ProteinGym_substitutions.zip` = **43,021,128 bytes**, 218 members. Index
`reference_files/DMS_substitutions.csv` on GitHub, 217 assays.

From the index (verified):

- **96 human assays**, 81 unique UniProt mnemonics, **329,664 single mutants**.
- `selection_type == "Stability"`: only **3 assays**, 2 of them human (PTEN, TPMT; 8,731 singles).
- **Protein-abundance / VAMP-seq assays: 6, all human** — CP2C9 (6,370), HXK4 (8,396), PTEN (5,083),
  S22A1 (9,803), TPMT (3,648), VKOR1 (2,695) singles.
- `selection_type == "cDNA display proteolysis"` (the Tsuboyama mega-scale import): **64 assays,
  65,887 singles, 117,811 total**, sequence length 37–72 aa; **22 of the 64 are human**.

**What is actually distributed per assay** is minimal — verified by opening
`VKOR1_HUMAN_Chiasson_2020_abundance.csv`: `mutant, mutated_sequence, DMS_score, DMS_score_bin`
(2,695 rows). There is no accession, no position column and no ddG. The index's `UniProt_ID` is a
UniProt **mnemonic** (`PTEN_HUMAN`), not an accession, so joining to an accession list needs a
mnemonic→accession lookup.

### Mega-scale (Tsuboyama) human-domain subset

Measured directly on the ThermoMPNN splits (train+val+test, 272,712 rows, 298 unique wild-type
domains): 181 domains carry a PDB identifier, 117 are de novo designs. Querying RCSB for source
organism resolved all 181, of which **50 are human**.

- **Human-domain rows: 46,955 = 17.2 %** of the 272,712.
- De novo design rows: 94,499 = 34.7 %.
- Other organisms are led by *Gallus gallus* (17 entries), *Mus musculus* and *E. coli* (8 each).

Caveat: this measures the ThermoMPNN-split subset (298 domains), not the full Zenodo release of 331
natural + 148 de novo domains. The human fraction of the full release is **unverified**. Either way
the domains are 40–72 aa and carry no UniProt accession, so joining to a gene list requires PDB →
UniProt mapping (SIFTS).

## 4. Unreachable resources

### RaSP — the resource that would have been best, and is not downloadable here

Blaabjerg et al. 2023 eLife [10.7554/elife.82593](https://doi.org/10.7554/elife.82593) (CrossRef 200).

Download location, from the authors' repository README (`KULL-Centre/_2022_ML-ddG-Blaabjerg`,
fetched, HTTP 200): **`https://sid.erda.dk/sharelink/fFPJWflLeE`**, holding

- `rasp_preds_alphafold_UP000005640_9606_HUMAN_v2[.zip]` — "all **23,391** human RaSP ddG predictions"
- `..._prism_dir[.zip]` — same, in PRISM tree layout (`P12345` → `P1/23/45/`)
- `..._vaex_dataframe.zip` — single-file Vaex version
- `rasp_preds_exp_strucs_gnomad_clinvar.csv` — **predictions mapped to gnomAD and ClinVar annotations**

**Status: blocked, then allowlisted on request, then still unreachable.** `sid.erda.dk` and
`erda.ku.dk` were initially refused by the sandbox proxy; after both were granted, the proxy
`CONNECT` succeeds (`HTTP/1.1 200 Connection Established`) but the TLS handshake is terminated by the
server: `SSLEOFError: EOF occurred in violation of protocol` / `curl: (35)`. This reproduces with
`requests`, with `curl`, and with TLS 1.2, TLS 1.3, HTTP/1.1 and IPv4 forced. It is a server-side or
egress-IP rejection, not an allowlist problem, and I could not work around it. **No file size, row
count, column list or licence for RaSP is verified.** The repository carries no `LICENSE` file
(404).

Scale, from publications only: the eLife abstract states *"∼230 million stability changes for nearly
all single amino acid changes in the human proteome"*. As a sanity check, 11,418,237 reviewed human
canonical residues × 19 = 216,946,503, so ~230 M is consistent with full-proteome saturation.
**Version warning:** the open-access PDF that resolves for this DOI is the bioRxiv preprint v1, whose
abstract reports *"∼8.8 million stability changes ... in 1,381 human proteins"* — a different and much
smaller analysis. Do not mix the two figures. The paper reports predicted ddG in **kcal/mol** trained
against Rosetta, positive = destabilising (benign ClinVar variants median ΔΔG 0.54 kcal/mol, 95 %
within −0.9 to 2.7).

**PRISM** is not a separate database: it is the Lindorff-Larsen lab's file format and directory
convention, and the lab's precomputed human ddG resource *is* this RaSP release, shipped in
`prism_dir` layout. No separate reachable PRISM human download was found.

### MAVISp

`https://services.healthtech.dtu.dk/services/MAVISp-1.0/` — blocked by the sandbox allowlist
(ProxyError). Not requested, since ProtVar already supersedes it on scale and MAVISp covers a
curated protein set rather than the proteome. The web-app repository (`ELELAB/MAVISp`) is reachable
and states the database is distributed as CSV files from that Download page; its `CHANGELOG.md` was
last updated 06/12/2023 and carries no protein counts. Paper: Protein Science 2026,
[10.1002/pro.70548](https://doi.org/10.1002/pro.70548) (CrossRef 200). **Protein and variant counts
unverified.** MAVISp is the resource to chase if you need Rosetta-and-FoldX consensus ddG with
ClinVar/gnomAD annotation on curated proteins — ask for `services.healthtech.dtu.dk` to be
allowlisted.

---

## 5. Coverage assessment for an arbitrary human gene list

**Reference denominator**: 20,431 reviewed (Swiss-Prot) human entries, **11,418,237 canonical
residues** (UniProt REST, fetched 28 Oct 2026). Saturation missense = 19 substitutions per residue
→ 216,946,503 possible canonical missense variants.

### What fraction already has a precomputed value

| resource | proteins hit | residues covered | % of 11,418,237 |
|---|--:|--:|--:|
| ProtVar FoldX | 20,173 / 20,431 | 8,681,608 | **76.0 %** |
| Domainome Table 4 (ddG) | 1,761 | 216,607 | 1.9 % |
| Domainome Table 2 (aPCA) | 434 | 29,699 | 0.26 % |

So for a *typical* gene list, **expect ~76 % of canonical missense variants to have a FoldX ddG
already computed, and essentially nothing else**. Protein-level coverage is near-complete (98.7 % of
reviewed entries have at least one row); the shortfall is *within* proteins.

### Where the gaps are — measured, not assumed

Per-protein coverage (distinct ProtVar positions ÷ UniProt length), by length band:

| length (aa) | proteins | residues | covered | coverage | median per-protein |
|---|--:|--:|--:|--:|--:|
| ≤ 100 | 776 | 57,701 | 51,652 | 89.5 % | 1.000 |
| 101–500 | 11,601 | 3,429,635 | 2,936,435 | 85.6 % | 0.929 |
| 501–1,000 | 5,647 | 3,881,910 | 2,900,945 | 74.7 % | 0.795 |
| 1,001–2,700 | 2,191 | 3,157,721 | 2,022,846 | **64.1 %** | 0.703 |
| > 2,700 | 216 | 891,270 | 769,730 | 86.4 % | 1.000 |

- **Long multi-domain proteins are the main gap**, but not the longest ones. Coverage falls
  monotonically from 89.5 % to 64.1 % up to 2,700 aa, then *recovers* to 86.4 % above 2,700 aa,
  where AlphaFold's overlapping-fragment models give dense coverage. The 1,001–2,700 aa band —
  precisely the multi-domain proteins in this project — is the worst served.
- **Disordered regions are the mechanism.** The release retains 34.8 M rows below pLDDT 70, so
  low-confidence positions are not uniformly dropped, yet 24 % of residues have no row at all; the
  length dependence tracks the known increase of disorder content with protein length. Worst
  individual cases are long low-complexity proteins: P0DPF2 (5,207 aa, 10 positions), Q8NDH2
  (7,081 aa, 146), Q9H195 (13,477 aa, 415).
- **Membrane proteins are *not* a gap.** Proteins with a UniProt transmembrane feature (5,231 of
  20,431) are covered at **82.7 %** versus 73.8 % for non-TM — better, because TM helices model at
  high pLDDT. FoldX ddG on a membrane protein is computed in an implicit-solvent context with no
  lipid, so treat the *values* with caution even though the *coverage* is good.
- **Non-canonical isoforms are entirely absent.** ProtVar positions are canonical-isoform only, and
  Domainome Table 4 is keyed to one accession per gene. Any variant you hold in transcript
  coordinates must be mapped to the canonical isoform first; variants unique to alternative isoforms
  have no precomputed value anywhere I verified.
- **Domain-level resources miss most genes outright.** Of nine reference genes I checked (JAK1,
  JAK2, JAK3, TYK2, TP53, BRCA1, PTEN, CFTR, TTN), **none** appears in Domainome Table 4. Where it
  does cover a protein, it covers a median of only 17.6 % of residues, and just 36 of its 1,761
  proteins carry a transmembrane feature. It is a Pfam-domain resource, not a protein resource.
- **258 reviewed human entries have no FoldX row at all** — these need computing from scratch
  regardless.

### Practical consequence

For a multi-domain human gene list you can expect roughly three quarters of canonical missense
positions to be answerable by download, with the missing quarter concentrated in the disordered and
inter-domain-linker regions of 1–2.7 kaa proteins — which is where inter-domain interface variants
of interest to this project actually sit. Those regions, plus non-canonical isoforms, are what
would have to be computed locally. Note also that *every* large precomputed set here is built on
AlphaFold2 monomer models, so none of them represents an inter-domain interface in a specific
conformational state.

## Recommended download order

1. **ProtVar FoldX** `2025.02.10_foldx_energy.csv.gz` (1.5 GB) — the backbone; dedupe fragments and
   filter pLDDT yourself.
2. **ProtVar `1048genes_annotations.tar.gz`** (538 MB) — if ClinVar/gnomAD-linked context is wanted
   for the genes it covers.
3. **Domainome Table 4** (20.3 MB zipped) — independent, experiment-anchored kcal/mol ddG for 1,761
   genes; good as an orthogonal check on FoldX.
4. **Domainome Table 2** (29.3 MB zipped) — the experimental aPCA ground truth for 434 proteins.
5. **ProtVar MAVE mirror** (98 MB) — experimental scores with UniProt offsets already resolved;
   prefer over raw MaveDB.
6. **ProteinGym substitutions** (43 MB) — only if you need the curated benchmark framing.
7. **RaSP** — request `sid.erda.dk` egress from a network that can complete its TLS handshake; it is
   the only full-proteome alternative to ProtVar and the only one with a ready-made gnomAD/ClinVar join.

## Sample files pulled

- [protvar_foldx_energy_sample.csv]({{artifact:3d2dae18-4804-44c2-9ad8-b7112ffca04a}}) — first 100 lines of the ProtVar FoldX table
- [protvar_mave_identifier.csv]({{artifact:87d9eb60-1396-4f61-88e7-a2dad85e03aa}}) — all 1,993 MaveDB score sets with UniProt accession and position offset
- [protvar_mave_score_sample.csv]({{artifact:6a28b220-63b2-4bdc-8cca-5a2b6dd09ae6}}) — first 100 MAVE score rows
- [protvar_A2IDD5_fun_pop_str_head.csv]({{artifact:e22e0663-6509-4085-8790-a12e4d5f6daa}}) — first 60 rows of a per-gene annotation bundle, all 43 columns
- [domainome_T4_homolog_ddG_head200.csv]({{artifact:7e794101-bc85-4af0-b363-7eadbc6e7680}}) — Domainome homolog-averaged ddG, 200 rows
- [domainome_T2_aPCA_head200.csv]({{artifact:688faed9-8b2d-47af-8c2c-820e71c8b8ee}}) — Domainome aPCA fitness, 200 rows
- [proteingym_assay_index_trimmed.csv]({{artifact:2fc24e00-a7a4-4738-8f6d-3f101afb3926}}) — all 217 ProteinGym assays with organism, selection type and mutant counts
- [proteingym_PTEN_abundance_head100.csv]({{artifact:dc6a09d0-41cb-4949-957a-ff2e6cf52cb5}}) — a distributed ProteinGym assay file, 100 rows
- [protvar_coverage_by_protein.csv]({{artifact:c6e17644-bba0-4b65-b114-18532ae0f38c}}) — per-protein ProtVar coverage for all 20,431 reviewed human entries
