# Computing ΔΔG for large-scale human variant analysis

Research date: **28 October 2026**. Prepared for Alexander Chervov.

This file contains the original user prompts, the complete substantive survey, source links, the execution checks performed during the research, and supplementary methodological guidance from the preceding discussion. Chat-specific citation markers have been replaced by portable Markdown references. Availability and software observations refer to the research date; no new large-scale computations have been performed for this document.

## Original prompts

Initial prompt, verbatim:

> best practices to compute delta-delta-G

Detailed research prompt, verbatim:

> best practices to compute delta-delta-G for estimation of the mutation effect ? Are there precomputed databases for human variants ? What are the packages ? how fast they are ? how well-supported ? What the literature - some surveys and benchamarks ? Make me deep study of these topics. Add more relevant questions by yourself. My goal is to compute ddG for large number of variants for human genes. And it should be done by you. Next step I will ask you to make such computations for many genes and their variants.

File-creation prompt, verbatim:

> create an md file ddg_computations_survey.md include my promt there and put all there

## Recommendation

**For large numbers of missense variants across human genes, retrieve existing ΔΔG predictions first, use ThermoMPNN for new calculations, evaluate SPURS as an additional predictor, and reserve FoldX/Rosetta recalculation for selected cases.** Running FoldX or molecular dynamics independently for every variant would usually be an inefficient starting point.

The literature search materially changes the initial recommendation: extensive human precomputed datasets exist, including a **2026 proteome-wide ThermoMPNN resource**. There is independent human experimental evidence supporting ThermoMPNN, while SPURS is a promising newer option.

This assessment is based on publications, software documentation, repository checks, and a live API test performed on **28 October 2026**. Published timings are distinguished from measurements actually made.

## 1. Define the output as folding ΔΔG, with annotations for other mechanisms

For single amino-acid substitutions, standardize every method to:

\[
\Delta\Delta G_{\mathrm{fold}}
=\Delta G_{\mathrm{fold,mutant}}
-\Delta G_{\mathrm{fold,WT}},
\qquad
\Delta G_{\mathrm{fold}}=G_F-G_U.
\]

Thus **positive = destabilizing**, negative = stabilizing, in kcal/mol.

Some packages use the opposite convention. DDGun, for example, reports changes in *unfolding* free energy; its signs must be inverted before comparison with this convention. Preserve both original and normalized scores. [DDGun documentation](https://github.com/biofold/ddgun)

Folding ΔΔG estimates only one component of mutation effect:

| Quantity | What it describes | Can folding ΔΔG substitute for it? |
|---|---|---|
| Folding ΔΔG | Change in folded-versus-unfolded equilibrium | Our primary target |
| Binding ΔΔG | Change in affinity for a partner, DNA, RNA, or ligand | No |
| Conformational equilibrium | Shift between active/inactive or other folded states | No |
| Cellular abundance | Effects involving folding, degradation, expression, trafficking | Only partially |
| Functional activity/pathogenicity | Combined biological consequences | No |
| ΔTm | Change in melting temperature | No universal conversion to ΔΔG |

This distinction matters especially for signaling proteins and kinases. A mutation can preserve folding yet alter activity through allostery. A recent human-proteome study explicitly separates destabilization from functional disruption, including allosteric mechanisms. **A near-zero folding ΔΔG is not evidence that a variant is functionally harmless.** [Liao & Lehner, 2026](https://doi.org/10.1038/s41467-026-74517-8)

## 2. Precomputed human datasets

These include predictions for *all possible amino-acid substitutions* in covered proteins, so a variant need not already occur in ClinVar or gnomAD.

| Resource | What is available | Coverage and limitations | Proposed use |
|---|---|---|---|
| **ProtVar / FoldX** | FoldX v5 predictions using human AlphaFold structures; API and bulk data | Over 200 million precomputed stability changes; structural filtering and fragment/version issues require checking | First source for empirical energy-function predictions |
| **RaSP human proteome** | Approximately 230 million predictions | Archive covers 23,391 AlphaFold v2 structure files; these are not 23,391 distinct genes | Retrieve as a complementary score |
| **ThermoMPNN proteome predictions, Liao & Lehner 2026** | Stability predictions together with ESM-1v scores | Analysis retained 19,288 proteins; excludes some proteins through length, fragmentation, and matching filters | High-priority source for the main ML score |
| **StabilitySort** | Human proteome predictions based on **MAESTRO**, plus prioritization metrics | Canonical mapping and older source versions; do not confuse Z-scores with kcal/mol | Optional fourth source |
| **SPURS study resources** | Code, checkpoints, benchmark data, and proteome-scale analyses | Released software/data links verified, but not a convenient complete human lookup table | Compute selected/new predictions rather than assume database coverage |

ProtVar's paper documents the FoldX calculation and public programmatic interface. Its preparation removes some low-confidence regions; therefore “missing prediction” must remain distinct from “predicted neutral.” [ProtVar paper](https://doi.org/10.1093/nar/gkae413), [API documentation](https://www.ebi.ac.uk/ProtVar/api/docs), [bulk stability directory](https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/)

The [RaSP archive](https://erda.ku.dk/archives/338b8e4a2a6124883ccd9f0fba9d37cc/published-archive.html) explicitly describes its AlphaFold v2 files and alternative directory/dataframe formats. The repository also provides a [share-link route](https://sid.erda.dk/sharelink/fFPJWflLeE) including individual protein files.

The 2026 ThermoMPNN study used AlphaFold structures, excluded proteins shorter than 16 or longer than 2,700 residues, and retained those with matching ESM-1v data. Its [Zenodo deposit](https://zenodo.org/records/18386427) contains a **5.7 GB compressed archive**. The file listing was verified through the Zenodo API, but that entire archive was not downloaded during this review. [Study](https://doi.org/10.1038/s41467-026-74517-8)

StabilitySort's underlying predictor is MAESTRO, not FoldX. Its published download route is [stabilitysort.org/download](https://www.stabilitysort.org/download/), with a separate [resource bundle](https://data.mendeley.com/datasets/x62w68yj28/1). See the [StabilitySort paper](https://doi.org/10.1093/bioinformatics/btac465) and [2025 application study](https://doi.org/10.1038/s41467-025-57757-y).

### Actual retrieval verified in this environment

Calling the [ProtVar FoldX endpoint for TP53 R175H](https://www.ebi.ac.uk/ProtVar/api/prediction/foldx/P04637/175?variantAA=H) returned:

| Field | Returned value |
|---|---:|
| UniProt | P04637 |
| Mutation | R175H |
| FoldX ΔΔG | +11.3998 kcal/mol |
| Residue pLDDT | 96.38 |
| AlphaFold fragment | F1 |
| Request time in this session | 4.88 seconds |

This was a **database lookup, not a new calculation or an experimental measurement**. The extreme numerical value should not be interpreted as experimentally accurate to four decimal places.

The returned JSON was:

```json
[
  {
    "proteinAcc": "P04637",
    "position": 175,
    "afId": "F1",
    "afPos": 175,
    "wildType": "R",
    "mutatedType": "H",
    "foldxDdg": 11.3998,
    "plddt": 96.38,
    "numFragments": 1,
    "variantKey": "P04637:175:H"
  }
]
```

The ProtVar bulk FTP endpoint, StabilitySort download page, and a direct RaSP archive request returned errors from this environment. That does not establish that those resources are generally unavailable. ProtVar's individual prediction API worked.

## 3. Packages for new calculations

The recommendations in the last column are an assessment for this workload, not a universal accuracy ranking.

| Package | Inputs and approach | Automation/support assessment | Role for us |
|---|---|---|---|
| **[ThermoMPNN](https://github.com/Kuhlman-Lab/ThermoMPNN)** | WT structure; ProteinMPNN-derived neural model trained on stability measurements | MIT license; weights, inference scripts, CPU installation option, batch examples | **Default new predictor** |
| **[SPURS](https://github.com/luo-group/SPURS)** | WT sequence and structure; combines ESM2 and ProteinMPNN representations | MIT license; documentation, downloadable checkpoints; older main environment plus Python 3.11 compatibility branch | **Promising additional model; pilot first** |
| **[FoldX](https://foldxsuite.crg.eu/)** | Atomistic structure; empirical energy function and local remodeling | Mature CLI/documentation; academic license and registration needed for download | Retrieve existing scores; recalculate selected variants |
| **[MutateX](https://github.com/ELELAB/mutatex)** | Automates FoldX saturation mutagenesis and structural ensembles | Documented pipeline; GPL-3.0 wrapper; still requires FoldX | Preferred orchestration option for larger FoldX jobs |
| **[Rosetta Cartesian ΔΔG](https://docs.rosettacommons.org/docs/latest/cartesian-ddG)** | Structure; packing, minimization, limited backbone adaptation | Extensive ecosystem; substantial installation/computation; noncommercial licensing conditions | Detailed analysis of a shortlist |
| **[RaSP](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg)** | Local atomic environments; neural surrogate trained on Rosetta scores | Code/weights available, but legacy dependencies; current README says Colab no longer works | **Prefer precomputed results** |
| **[DDGun / DDGun3D](https://github.com/biofold/ddgun)** | Sequence/evolutionary features, optionally structure | Standalone and Docker; HH-suite and sequence database setup | Useful complementary baseline |
| **[MAESTRO](https://pbwww.services.came.sbg.ac.at/?page_id=477)** | Structure-based ensemble predictor | Downloadable CLI binaries, mutation scanning; free for noncommercial use | Optional CPU alternative / StabilitySort source |
| **[PROSTATA](https://github.com/mitiau/PROSTATA)** | Sequence-based transformer predictor | Code, environments, model workflow and notebooks; Apache-2.0 | Sequence-only comparator |
| **[DDMut](https://biosig.lab.uq.edu.au/ddmut/)** | Structural graph features and neural prediction | Documented web API; server dependence | Selected cross-checks |
| **[DDGemb](https://ddgemb.biocomp.unibo.it/)** | Sequence embeddings; single and multiple substitutions | Published web service and datasets; an equally straightforward local batch package was not established | Interesting benchmark comparator |
| **[GeoStab / GeoDDG](https://github.com/Gonglab-THU/GeoStab)** | Geometric learning with structural/sequence features | Code and reproducible capsule; broader dependency chain includes FoldX | Secondary candidate after the simpler pipeline |

ThermoMPNN documents custom-PDB saturation scans, larger datasets, and CPU installation. SPURS exposes all-position/all-amino-acid predictions through its inference interface. [ThermoMPNN documentation](https://github.com/Kuhlman-Lab/ThermoMPNN), [SPURS documentation](https://github.com/luo-group/SPURS)

MutateX is a workflow around FoldX, not an independent predictor. DDGun supplies standalone/Docker execution but requires substantial sequence-search infrastructure. Its documented UniClust database download is approximately 25 GB. [MutateX](https://github.com/ELELAB/mutatex), [DDGun](https://github.com/biofold/ddgun)

The other implementation routes above are documented by their authors. GeoStab is less attractive as our first deployment because of its dependencies; DDMut's API is convenient but does not eliminate remote-service limits. [GeoStab paper](https://doi.org/10.1038/s43588-024-00716-2), [DDMut paper](https://academic.oup.com/nar/article/51/W1/W122/7191416), [DDGemb paper](https://doi.org/10.1093/bioinformatics/btaf019)

### Support and maintenance

“Well supported” should mean more than a recent paper. Current GitHub metadata was checked:

| Repository | Latest push reported during this check | Important qualification |
|---|---|---|
| ThermoMPNN | 9 September 2026 | CPU and modern package-manager instructions exist |
| SPURS | 15 July 2026 | Main instructions still specify Python 3.7/PyTorch 1.12; compatibility branch needs validation |
| RaSP | 15 April 2026 | Recent activity does not resolve its documented dependency problems |
| MutateX | 9 March 2026 | FoldX itself remains a separate dependency |

These are repository activity observations, **not guarantees of response time, installation success, or long-term maintenance**. RaSP's explicit dependency warning is particularly relevant. Its README states that Colab no longer supports its dependencies and recommends local installation. [RaSP repository](https://github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg)

FoldX is free for eligible academic/nonprofit research but is not an unrestricted open-source dependency. Rosetta also has noncommercial/commercial distinctions. We should use the applicable licensed distribution when computation requires it. [FoldX licensing](https://foldxsuite.crg.eu/node/737), [FoldX academic access](https://foldxsuite.crg.eu/academic-license-info), [Rosetta getting started](https://docs.rosettacommons.org/docs/latest/getting_started/Getting-Started)

## 4. Speed and scaling

Speed must be measured per protein as well as per variant. For an all-substitution model, predicting one mutation and predicting thousands of substitutions in the same protein may have similar costs. For FoldX/Rosetta, the number of variants and structural replicates matters much more.

| Method | Published/documented timing evidence | Interpretation |
|---|---|---|
| Precomputed lookup | The single ProtVar request took 4.88 s | Network latency; millions of individual requests would be inefficient |
| ThermoMPNN | A deployed implementation describes full saturation scans on the order of seconds | Hardware-specific; local inference was not timed |
| SPURS | Authors report all substitutions for 118 proteins, mean length 492 aa, in under 20 s on one A40 GPU | Model benchmark, not download/setup/annotation time |
| RaSP | Approximately 0.4 s per residue for saturation scanning after preparation | About 200 s for a 500-residue protein under the reported conditions |
| FoldX / Rosetta | Much slower and highly protocol-dependent | Benchmark preparation, repetitions, and parallelism together |
| DDGun | Search/profile construction plus inexpensive scoring | Reuse one profile across all variants of a protein |

The [ThermoMPNN deployment timing](https://support.levitate.bio/bench/thermo_mpnn/) and [SPURS benchmark](https://doi.org/10.1038/s41467-025-67609-4) support rapid saturation scanning, but neither is a runtime promise for this session.

A concrete comparison comes from the [RaSP paper, Table 4](https://elifesciences.org/articles/82593). For saturation scanning of **GCK, 434 residues**, it reports approximately:

| Method | Preparation | Prediction |
|---|---:|---:|
| RaSP | 11 s | 173 s |
| Rosetta | 7,996 s | 118,361 s |
| FoldX | 728 s | 309,762 s |

RaSP used a V100 GPU; FoldX/Rosetta used a 64-core CPU server and three calculations per mutation. **These results should not be generalized into “FoldX is always slower than Rosetta.”** They demonstrate how strongly throughput depends on implementation and protocol.

For this workload, estimate runtime from:

\[
T_{\mathrm{total}}=
T_{\mathrm{download/index}}
+\sum_p T_{\mathrm{preparation},p}
+\sum_p T_{\mathrm{inference},p}
+T_{\mathrm{mapping/QC}}.
\]

For many variants concentrated in a few genes, preparation amortizes well. For one variant in each of thousands of genes, structure retrieval and preparation can dominate.

## 5. Accuracy and benchmarks

Accuracy is useful for prioritization, but substantially weaker than some headline metrics suggest. There is no defensible single ranking across all proteins, mutation types, and experimental endpoints.

| Benchmark | Main evidence | Relevance to this project |
|---|---|---|
| **Pancotti et al., 2022: S669** | 669 newly curated variants; 21 tools; direct-variant Pearson correlations roughly 0.21–0.50 | Strong warning about generalization and inflated historical benchmarks |
| **Human Domainome 1, 2025** | More than 500,000 variants across more than 500 human domains; cellular abundance assay | Especially relevant independent human validation |
| **SPURS evaluation, 2025/2026** | Reports improvements over ThermoMPNN across multiple datasets | Promising, but conducted by the method developers |

S669 also evaluates reverse mutations and finds problems with antisymmetry, compressed prediction ranges, and strongly stabilizing variants. It was new relative to methods available then; **a 2026 model does not automatically inherit “blind-test” status on S669.** [Pancotti et al.](https://doi.org/10.1093/bib/bbab555)

In the original Domainome comparison, ThermoMPNN was the best tested predictor, with median Spearman correlation around **0.50**, increasing to **0.57 after excluding zinc-finger domains**. The study reports poor performance of stability predictors on small zinc fingers requiring metal binding. These are abundance correlations, not kcal/mol errors. [Human Domainome 1](https://doi.org/10.1038/s41586-024-08370-4)

SPURS reports median per-protein Spearman **0.83 versus 0.77** for ThermoMPNN on its Megascale test comparison, and Domainome correlation **0.54 versus 0.49** under its evaluation. These are encouraging but are not interchangeable with the original Domainome statistics. The paper has a March 2026 correction replacing Figure 5 and its source data; use the corrected release. [SPURS paper](https://doi.org/10.1038/s41467-025-67609-4), [correction](https://doi.org/10.1038/s41467-026-70929-8)

A further independent study found FoldX and Rosetta strongest among its tested methods for agreement with functional DMS assays, emphasizing complex structures. That does not contradict the stability benchmarks: **the endpoint and method set differ.** [Gerasimavicius, Livesey & Marsh, 2023](https://doi.org/10.1002/pro.4688)

For our own evaluation, require:

- **Protein/family-separated testing**, including reverse-mutant leakage checks.
- MAE/RMSE in kcal/mol **only against thermodynamic labels**.
- Per-protein rank correlation as well as pooled correlation.
- Coverage and failure rates, not accuracy only on successfully scored variants.
- Separate results for buried/exposed sites, low-confidence regions, metals/disulfides, membrane proteins, and mutation classes.
- Protein-level bootstrap uncertainty; variants within one protein are not independent samples.
- Comparison against simple baselines such as solvent exposure and substitution type.

Avoid treating model agreement as a calibrated confidence interval. ThermoMPNN and SPURS share important training/model ingredients; RaSP was trained on Rosetta predictions. Their errors are not independent.

## 6. Experimental databases

Experimental databases are valuable, but differ from precomputed prediction databases.

| Resource | Use | Important caveat |
|---|---|---|
| **FireProtDB 2.0** | Curated experimental stability-related data and API | Approximately 5.5 million experiments include heterogeneous endpoints; not millions of independent human kcal/mol ΔΔGs |
| **ProThermDB / ThermoMutDB** | Historical thermodynamic mutation measurements | Conditions, constructs, duplicates, and sign conventions need harmonization |
| **Megascale, Tsuboyama et al.** | Large standardized folding-stability dataset | Mostly small domains; many modern predictors train on it |
| **Human Domainome 1** | Human domain abundance effects | Not direct equilibrium ΔΔG measurements |
| **MaveDB / individual DMS datasets** | Functional or abundance validation | Assay-specific endpoints must remain separate |

FireProtDB 2.0 integrates multiple sources, supports more mutation types, and exposes API documentation. Its size should not be confused with the number of unique thermodynamic measurements relevant to a particular gene. [Paper](https://doi.org/10.1093/nar/gkaf1211), [API documentation](https://loschmidt.chemi.muni.cz/fireprotdb/api-docs/)

Megascale contains approximately 776,000 high-quality folding-stability measurements across natural and designed domains, largely **40–72 residues long**. This is transformative training data, but applying a model learned from it to large multidomain human proteins is still a generalization problem. [Tsuboyama et al.](https://doi.org/10.1038/s41586-023-06328-6)

## 7. Best practices for the pipeline

### Validate the exact protein sequence before scoring

A gene name and `R123H` are insufficient if multiple isoforms exist. For each variant, resolve genome assembly where relevant, transcript/version, protein accession, reference residue, and structural residue mapping. A mismatch must produce a flagged failure, never a silently shifted prediction.

### Use domain-aware structural handling

For a long protein, a confidently folded domain may be usable even when interdomain orientation is uncertain. Conversely, a high pLDDT at one residue does not prove that its modeled contacts with another domain are correct. Record local confidence, domain boundaries, neighboring confidence, and interdomain uncertainty.

### Do not automatically generate an AlphaFold mutant structure for every substitution

The principal high-throughput models discussed here use the WT structure. Mutant structure prediction adds substantial work without directly providing folding free energies; changes in pLDDT are not ΔΔG.

### Match preparation to the method

FoldX recommends `RepairPDB` before mutation modeling; `BuildModel` creates a matched WT reference so that equivalent neighbors move in WT and mutant. Rosetta has its own Cartesian relaxation and scoring requirements. Applying one generic minimization pipeline to every method can change the intended protocol. [RepairPDB](https://foldxsuite.crg.es/command/RepairPDB), [BuildModel](https://foldxsuite.crg.eu/command/BuildModel), [Rosetta Cartesian ΔΔG](https://docs.rosettacommons.org/docs/latest/cartesian-ddG)

### Keep biological assemblies and chemistry explicit

Flag interface sites, metal ligands, disulfide cysteines, ligand-dependent folds, membrane regions, and post-translational modifications. Monomer predictions can miss these mechanisms.

### Keep numerical scores separate from interpretation

Initially report “predicted destabilization,” “small/uncertain predicted change,” and “method disagreement,” rather than impose a universal pathogenicity threshold. Differences of a few tenths of a kcal/mol often do not justify precise ranking.

### Preserve missingness

Use reasons such as `reference_mismatch`, `isoform_not_covered`, `structure_missing`, `low_confidence`, `unsupported_variant`, and `calculation_failed`. Never replace missing scores with zero.

## 8. Additional questions before scaling

| Question | Proposed default / consequence |
|---|---|
| All possible substitutions, or only supplied variants? | Score only supplied variants for lookup; saturation inference can still be economical per protein |
| Which transcript? | Use supplied versioned transcript; otherwise propose a canonical mapping and report ambiguity |
| Single variants or haplotypes? | Treat separately; summing single ΔΔGs does not capture epistasis |
| Missense only, or indels/stops/splice variants? | Standard pipeline covers missense; other classes need separate methods |
| Full-length protein or isolated domain? | Preserve the construct definition; use domain models where justified |
| Do we need binding effects? | Add a separate partner-specific analysis rather than reinterpret folding scores |
| Is the goal within-gene ranking or comparison across genes? | Cross-gene calibration requires extra validation |
| What counts as uncertainty? | Separate mapping/structure quality, repeat variability, model disagreement, and benchmark error |
| Could disease result from excessive stabilization? | Yes; do not assume stabilizing always means beneficial |
| Does the protein have a small stability margin already? | ΔΔG alone does not specify the resulting folded fraction without baseline stability |

Multiple mutations deserve particular caution: a dedicated benchmark found that existing stability models often fail to capture epistatic interactions. Dedicated double-mutant models are worth investigating if the input includes phased combinations. [Protein stability models fail to capture epistatic interactions of double point mutations](https://pmc.ncbi.nlm.nih.gov/articles/PMC11659742/)

## 9. Prioritized surveys and benchmark literature

| Reading | Why it is useful |
|---|---|
| **Qiu, Huang & Cai, 2024 — “Review of predicting protein stability changes upon variations.”** [DOI](https://doi.org/10.1002/pmic.202300371) | Broad survey of methods, datasets, and experimental techniques |
| **Peccati et al., 2025 — “Computation of Protein Thermostability and Epistasis.”** [DOI](https://doi.org/10.1002/wcms.70045) | Conceptual limitations, unfolded-state treatment, sampling, and multiple mutations |
| **Pancotti et al., 2022 — “Predicting protein stability changes upon single-point mutation: a thorough comparison of the available tools on a new dataset.”** [DOI](https://doi.org/10.1093/bib/bbab555) | Essential independent benchmark and antisymmetry analysis |
| **Gerasimavicius, Livesey & Marsh, 2023 — “Correspondence between functional scores from deep mutational scans and predicted effects on protein stability.”** [DOI](https://doi.org/10.1002/pro.4688) | Explains how stability prediction relates to function and complex structures |
| **Tsuboyama et al., 2023 — “Mega-scale experimental analysis of protein folding stability in biology and design.”** [DOI](https://doi.org/10.1038/s41586-023-06328-6) | Understand the training data behind modern predictors |
| **Dieckhaus et al., 2024 — “Transfer learning to leverage larger datasets for improved prediction of protein stability changes” (ThermoMPNN).** [DOI](https://doi.org/10.1073/pnas.2314853121) | Main practical ML candidate |
| **Blaabjerg et al., 2023 — “Rapid protein stability prediction using deep learning representations” (RaSP).** [DOI](https://doi.org/10.7554/eLife.82593) | Proteome-scale data, surrogate modeling, and runtime comparisons |
| **“Site-saturation mutagenesis of 500 human protein domains,” 2025.** [DOI](https://doi.org/10.1038/s41586-024-08370-4) | Most directly relevant large human experimental benchmark |
| **Li & Luo — “Generalizable and scalable protein stability prediction with rewired protein generative models” (SPURS), online December 2025; 2026 volume.** [DOI](https://doi.org/10.1038/s41467-025-67609-4) | Newer scalable predictor; read with the correction |
| **“VenusMutHub: A systematic evaluation of protein mutation effect predictors on small-scale experimental data,” 2025.** [Paper](https://www.sciencedirect.com/science/article/pii/S2211383525001650) | Broader benchmark spanning direct biochemical properties, beyond DMS proxies |
| **Liao & Lehner, 2026 — “Allostery is a widespread cause of loss-of-function variant pathogenicity.”** [DOI](https://doi.org/10.1038/s41467-026-74517-8) | Human ThermoMPNN data and the limits of folding-only interpretation |

The two reviews are useful introductions; VenusMutHub adds 905 small experimental datasets across 527 proteins and 23 models, although its scope is broader than ΔΔG.

Additional useful method and resource references:

- [DDGun: an untrained predictor of protein stability changes upon amino acid variants](https://academic.oup.com/nar/article/50/W1/W222/6582160).
- [MutateX: an automated pipeline for in-silico saturation mutagenesis of protein structures and structural ensembles](https://doi.org/10.1093/bib/bbac074).
- [ProtVar: mapping and contextualizing human missense variation](https://doi.org/10.1093/nar/gkae413).
- [Predicted mechanistic impacts of human protein missense variants](https://pmc.ncbi.nlm.nih.gov/articles/PMC11160786/).
- [StabilitySort: assessment of protein stability changes on a genome-wide scale to prioritize potentially pathogenic genetic variation](https://doi.org/10.1093/bioinformatics/btac465).
- [FireProtDB 2.0: large-scale manually curated database of the protein stability data](https://doi.org/10.1093/nar/gkaf1211).
- [DDGemb: predicting protein stability change upon single- and multi-point variations with embeddings and deep learning](https://doi.org/10.1093/bioinformatics/btaf019).
- [Improving the prediction of protein stability changes upon mutations by geometric learning and a pre-training strategy](https://doi.org/10.1038/s43588-024-00716-2).
- [PROSTATA: a framework for protein stability assessment using transformers](https://pubmed.ncbi.nlm.nih.gov/37935419/).

## 10. Proposed execution workflow

1. **Normalize and validate variants.** Preserve original identifiers; resolve protein sequences and reject reference mismatches.
2. **Produce a coverage audit.** Count mapped variants and availability in ProtVar, ThermoMPNN, RaSP, and experimental datasets.
3. **Retrieve existing predictions.** Use cached/bulk data where economical; avoid millions of individual API calls.
4. **Run new ThermoMPNN predictions for gaps or consistent rescoring.** Benchmark a representative pilot before estimating the full run.
5. **Evaluate SPURS on the pilot.** Include small domains, larger proteins, and difficult structural contexts. Decide whether its added information justifies deployment.
6. **Investigate important disagreements.** Use alternative structures and selected FoldX/Rosetta calculations where they address a specific uncertainty.
7. **Deliver auditable tables.** Include raw and standardized scores, source versions, structure confidence, mapping/QC flags, method agreement, and separate functional annotations.

The output should retain **one column per method**, rather than immediately collapse everything into an unexplained average. A calibrated consensus can be added if suitable validation data support it.

The assistant can perform retrieval, mapping, coding, quality control, and available local calculations. **Verified during this study:** AlphaFold and GitHub retrieval, Zenodo metadata access, and a real ProtVar prediction lookup. **Unverified:** local predictor installation/inference, full archive downloads, and large-batch runtime. This session lacked PyTorch and an exposed NVIDIA GPU, so GPU-scale timings cannot be promised here.

For the next step, a variant table with **gene, versioned transcript or UniProt accession, and amino-acid change** is ideal. A VCF also works if the genome assembly is specified. Begin with the coverage audit and a representative pilot, then carry out the full workload using the validated route.

## Appendix A. Supplementary guidance from the initial discussion

The initial answer assumed protein mutations and covered both folding stability and binding affinity. Its broad recommendation was to define the thermodynamic quantity, prepare matched WT/mutant systems, and assess structural and sampling sensitivity. A single energy difference from two minimized structures is not a rigorous free-energy estimate.

### Binding ΔΔG and its sign

\[
\Delta\Delta G_{\mathrm{bind}}
=\Delta G_{\mathrm{bind,mut}}-\Delta G_{\mathrm{bind,WT}}
=RT\ln\frac{K_{d,\mathrm{mut}}}{K_{d,\mathrm{WT}}}.
\]

Positive values mean weaker binding. At 298 K, a tenfold increase in dissociation constant corresponds to approximately +1.36 kcal/mol. Always state the convention, units, temperature, and experimental conditions.

### Alchemical thermodynamic cycles

For a protein mutation affecting binding:

\[
\Delta\Delta G_{\mathrm{bind}}
=\Delta G_{\mathrm{WT}\rightarrow\mathrm{mut}}^{\mathrm{complex}}
-\Delta G_{\mathrm{WT}\rightarrow\mathrm{mut}}^{\mathrm{unbound\ protein}}.
\]

For folding, replace “complex/unbound protein” with “folded/unfolded.” Representing the unfolded ensemble is a substantial extra challenge; a short peptide reference is an approximation.

For rigorous alchemical calculations, use independent replicates, check overlap between neighboring alchemical states, inspect convergence with simulation length, and handle net-charge changes with an appropriate electrostatic correction or validated protocol. Stable RMSD alone does not establish free-energy convergence. These methods are most appropriate for a small, carefully selected set rather than an initial human-proteome scan.

Reference: [Mey et al., Best Practices for Alchemical Free Energy Calculations](https://doi.org/10.33011/livecoms.2.1.18378), [open full text](https://pmc.ncbi.nlm.nih.gov/articles/PMC8388617/).

### Structure preparation and repeat calculations

- Check sequence numbering, missing residues, alternate conformations, and the biological assembly.
- Inspect protonation, histidine tautomers, disulfides, cofactors, metals, and relevant waters.
- Use the same preparation and sampling protocol for WT and mutant.
- For FoldX, run `RepairPDB` before `BuildModel`, and use the mutation-specific WT reference generated by `BuildModel`.
- Five FoldX runs are a reasonable initial convergence check, not a universal requirement or guarantee of accuracy.
- For Rosetta, follow the Cartesian relaxation protocol and keep score-function settings consistent. Raw Rosetta energy units must not be labeled kcal/mol without the appropriate protocol-specific calibration.
- ThermoMPNN is a folding-stability predictor, not a binding-affinity predictor. Rosetta documents Cartesian ΔΔG primarily for monomer stability and cautions that its interface mode is less thoroughly benchmarked.

References: [FoldX RepairPDB](https://foldxsuite.crg.es/command/RepairPDB), [FoldX BuildModel](https://foldxsuite.crg.eu/command/BuildModel), [Rosetta Cartesian ΔΔG](https://docs.rosettacommons.org/docs/latest/cartesian-ddG).

### Uncertainty and model comparison

Compare predictions across plausible input structures and complementary methods. Treat disagreement as a reason to inspect the mutation rather than blindly average scores. Report replicate variability separately from predictive accuracy: repeated calculations can agree closely while sharing a systematic error.

Validate against mutations measured under comparable conditions whenever possible. Benchmark-wide error is not a confidence interval for an individual mutation. ThermoMPNN's authors report variation in performance with protein size and mutation type. [ThermoMPNN paper](https://doi.org/10.1073/pnas.2314853121)

The initial screening proposal was ThermoMPNN plus repaired FoldX, followed by inspection of disagreements, selected Rosetta refinement, and experimental validation. **For the large-scale human use case, the main survey supersedes that proposal with a retrieval-first workflow**, reducing unnecessary recalculation.

## Appendix B. Execution evidence and limits

| Check | Outcome on 28 October 2026 |
|---|---|
| Python logical CPU count | 9 |
| NumPy / pandas | Available |
| PyTorch / BioPython | Not installed at the time of inspection |
| NVIDIA tooling | `nvidia-smi` not found; no NVIDIA GPU exposed by the checks performed |
| Raw GitHub ThermoMPNN README | HTTP 200 |
| AlphaFold API for P04637 | HTTP 200 |
| GitHub repository metadata | Retrieved for ThermoMPNN, SPURS, RaSP, and MutateX |
| ProtVar OpenAPI schema | Retrieved at `/ProtVar/api/docs` |
| ProtVar TP53 R175H FoldX lookup | Successful; response reproduced above |
| Zenodo record 18386427 metadata | Successful; archive size 5,718,868,398 bytes |
| ProtVar bulk FTP / StabilitySort / direct RaSP archive access | HTTP errors during direct requests |
| Local model installation or inference | Not performed |
| Full human prediction archive download | Not performed |

A successful metadata or single-variant request verifies that route at that time, not bulk throughput or complete coverage. Published benchmark results in this file are literature findings, not newly reproduced experiments.
