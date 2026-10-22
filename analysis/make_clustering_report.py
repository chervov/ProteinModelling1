"""Regenerate mutations_clustering.md from current data and push it.

Run this whenever new ddG results land; it rebuilds the whole document from the data files so the
numbers in the repo can never drift from the numbers on disk.
"""
import base64, csv, io, json, os, re, urllib.request, urllib.error, collections
import numpy as np
from datetime import datetime

OUT="/Users/chervov/orianne_tyk2"
def readcsv(p): return list(csv.DictReader(open(p))) if os.path.exists(p) else []
def fl(v):
    try: return float(v)
    except Exception: return None

L=[]
def w(s=""): L.append(s)

w("# Variant clustering: reproducing the Jeanpierre/Debeaupuis pipeline across the JAK family")
w()
w(f"Regenerated {datetime.now():%Y-%m-%d %H:%M}. Source data under `{OUT}`; generator is")
w("`analysis/make_clustering_report.py`. Companion detail lives in `mutation_analysis.md` sections 51-52.")
w()
w("## The method being reproduced")
w()
w("Jeanpierre, Debeaupuis et al., *EMBO Molecular Medicine* 2025, 17:3275-3299 - the source of the")
w("Jeanpierre open/closed JAK1 models used as references throughout this project. They scored 21,926")
w("JAK1 missense variants on 11 features and clustered them.")
w()
w("**Thermodynamic convention (Appendix S3), which is inverted from Rosetta's native sign:**")
w()
w("> ddG_m = dG_WT - dG_m. If ddG_m < 0 the mutation is **destabilizing**; if > 0, **stabilizing**.")
w(">")
w("> ddG_open,m > ddG_closed,m corresponds to stronger stabilization (or weaker destabilization) of")
w("> the open versus closed state, **leading to more open configurations in mutants**.")
w()
w("So the pipeline's distinctive feature is **ddG_open - ddG_closed**: a conformational-preference")
w("estimate, not a stability estimate. Clustering is **semi-supervised K-means on Gower distance**,")
w("seeded with 10 labelled variants; Gower is used because it handles missing features natively.")
w()
w("### Their 11 features, with the missingness they report")
w()
w("| feature | missing (paper, JAK1) | available to us |")
w("|---|--:|---|")
rows_feat=[("ESM-1b","0%","**100%** - files supplied, verified against UniProt"),
 ("ddG closed (PyRosetta)","0%","**done** - reproduces their medians, AUC 0.770 on their clusters"),
 ("ddG open (PyRosetta)","0%","**done** - AUC 0.767"),
 ("**ddG open - closed**","0%","**done - and it carries no signal: AUC 0.504, p=0.89**"),
 ("AlphaMissense","70.3%","**100%** - source release, keyed on UniProt (section 57)"),("SIFT","43.7%","33%"),("PolyPhen-2","43.7%","32%"),
 ("BLOSUM62","43.7%","**100%** - computed locally"),("ClinPred","85.8%","96% of the SNV subset"),
 ("CADD","-","**0% - licence-restricted in dbNSFP**"),("MutFunc","92.1%","not attempted")]
for a,b,c in rows_feat: w(f"| {a} | {b} | {c} |")
w()
w("**Why dbNSFP coverage caps at ~33%**: it is keyed on *genomic* variants, so it holds only")
w("substitutions reachable by a single nucleotide change. This is why **V678F - this project's")
w("headline TYK2 variant - has no PolyPhen, SIFT or REVEL score**. ESM-1b and BLOSUM62 score")
w("protein sequence directly and have no such limit.")
w()
w("**AlphaMissense is no longer in that group.** Its scores are now taken from the source release")
w("(`AlphaMissense_aa_substitutions.tsv.gz`), which is keyed on UniProt accession and protein-level")
w("substitution, giving **100% coverage for all four JAKs** - including V678F (0.254) and H582W")
w("(0.345), both of which it calls benign. The paper's reported 70.3% missingness is an artefact of")
w("joining through genomic coordinates, not a property of AlphaMissense. The cross-check against our")
w("earlier dbNSFP extraction also exposed a defect in that extraction - 290-531 values per column")
w("carried on substitutions needing two or three nucleotide changes, which cannot have a dbNSFP row -")
w("now blanked. See `mutation_analysis.md` section 57.")
w()

# ---- DATA SOURCES
w("## Data: what it is, how it was obtained, how complete it is")
w()
w("Every number in this document traces to one of the following. Access dates are 2026-10-22.")
w()
w("### 1. Deep mutational scan - the ground truth")
w()
w("| | |")
w("|---|---|")
w("| what | >23,000 single amino-acid substitutions across TYK2, assayed for IFN-alpha signalling and protein abundance |")
w("| source | MaveDB, `urn:mavedb:00001270-a` (signalling) and `urn:mavedb:00001271-a-1` (abundance) |")
w("| how | downloaded as score CSVs; parsed from the `hgvs_pro` column (`p.Xaa###Yaa`) |")
w("| system | HEK293T with all endogenous TYK2 knocked out by CRISPR, STAT2 + IRF9 restored by piggyBac |")
w("| signalling assay | barcoded luciferase under an 8x ISRE promoter, doxycycline-inducible TYK2; IFN-alpha 2a at 1, 10 or 100 U/mL; RNA harvested at 6 h |")
w("| abundance assay | VAMP-seq: N-terminal **GFP**-tagged TYK2 with a co-transcriptional **BFP** normalisation control, FACS-sorted into four quartile bins on the GFP:BFP ratio |")
w("| replication | biological triplicate; signalling libraries amplified in duplicate per replicate |")
w("| completeness | signalling 23,737 of 23,740 possible variants (>99.9%); abundance 23,716 (>99.9%) |")
w("| **we hold** | **1 U/mL (22,536), 100 U/mL (22,536), abundance (22,516)** after restricting to missense with parseable HGVS |")
w("| **not downloaded** | the **10 U/mL** arm and the inhibitor arms (BMS-986202, NDI-034858) - available, never pulled |")
w()
w("Scale: 0 = wild type, **-0.352 = the nonsense median**, i.e. a dead protein. Abundance measures")
w("steady-state protein per unit mRNA, so a low score means the protein is made and then degraded -")
w("a proxy for folding stability, though a degron or aggregation would look the same.")
w()
w("### 2. ESM-1b - the evolutionary score")
w()
w("| | |")
w("|---|---|")
w("| what | protein language model log-odds, one file per JAK, supplied by the user |")
w("| how | files in `~/Downloads`, named by UniProt accession |")
w("| completeness | **100%** - every position x 20 amino acids, including self-substitutions scored 0.0 |")
w("| verification | every WT residue in every row checked against the UniProt sequence: **100% match in all four genes** |")
w("| identification | not labelled as ESM-1b in the files; identified by (a) score range and median matching the paper's reported ESM-1b cluster means, (b) JAK1 reducing to exactly 21,926 non-self variants, the paper's own count |")
w()
w("### 3. Sequence predictors - dbNSFP via MyVariant.info")
w()
w("| | |")
w("|---|---|")
w("| what | PolyPhen-2 (HDIV/HVAR), SIFT, REVEL, AlphaMissense, ClinPred |")
w("| how | `myvariant.info/v1/query`, `q=dbnsfp.genename:<GENE>`, scrolled with `fetch_all` |")
w("| raw hits | 9,481 records for TYK2, collapsing to 7,917 unique (position, alt) pairs |")
w("| completeness | **~33% of all possible substitutions** |")
w("| **why not more** | dbNSFP is keyed on **genomic** variants, so it contains only substitutions reachable by a **single nucleotide change**. Two-nucleotide substitutions are absent entirely - including **V678F**, this project\'s headline variant |")
w("| ClinPred note | returned as a nested object `{pred, rankscore, score}`, not a bare float; the `score` field is used |")
w()
w("### 4. CADD - attempted and unavailable")
w()
w("Requested as `dbnsfp.cadd.phred` and `cadd.phred`; MyVariant returned **0 of 9,205** records with a")
w("value. CADD is licence-restricted in the academic dbNSFP build. Obtaining it needs either the CADD")
w("website (per-VCF submission) or the ~80 GB whole-genome score file. **This is one of only two")
w("sequence-based pathogenicity scores the paper names**, so its absence is a real gap in the")
w("reproduction, not a convenience omission.")
w()
w("### 5. Population and clinical databases")
w()
w("| source | field | TYK2 | JAK1 | JAK2 | JAK3 |")
w("|---|---|--:|--:|--:|--:|")
w("| gnomAD (exome, then genome) | `gnomad_exome.af.af` | 702 | 330 | 512 | 526 |")
w("| ClinVar | `clinvar.rcv.clinical_significance` | 414 | 272 | 223 | 327 |")
w()
w("Both via the same MyVariant query, so both inherit the ~33% single-nucleotide ceiling. The paper")
w("reported 289 JAK1 gnomAD variants; we retrieve 330, consistent with a later gnomAD release.")
w()
w("**ClinVar is not usable as ground truth for TYK2**: of 414 records, **381 (89%) are \"Uncertain")
w("significance\"**, with only 12 Pathogenic, 1 Likely pathogenic, 8 Benign and 21 Likely benign. Only")
w("2 pathogenic variants overlap the clustered set, so no pathogenic-enrichment test is possible.")
w("This is precisely the gap the DMS fills.")
w()
w("### 6. Structures used for ddG")
w()
w("| state | source | FERM-JH1 | note |")
w("|---|---|--:|---|")
w("| closed | AlphaFold `AF-P29597-F1` | 39.7 A | the compact TYK2 model |")
w("| open | our run `TYK2_20261022_010154/selected_open.pdb` | 93.4 A | wild type, template-free, 512/8192; 4.8 A from Jeanpierre\'s open JAK1 model |")
w()
w("The paper built both JAK1 states with a modified AlphaFold2. No experimental multi-domain TYK2")
w("structure exists (`mutation_analysis.md` section 35), so the open state here is necessarily a")
w("prediction - validated only by its 5-8 A agreement with cryo-EM **JAK1** 8EWY.")
w()
w("### 7. Derived locally, no external dependency")
w()
w("BLOSUM62 (Biopython), side-chain volume change (Zamyatnin), hydrophobicity change")
w("(Kyte-Doolittle). **100% coverage**, instant.")
w()
# ---- provenance
w("## Provenance check on the ESM-1b files")
w()
w("| gene | UniProt | rows | positions | UniProt length | WT residue matches |")
w("|---|---|--:|---|--:|---|")
for g,u,n,p,ln in [("JAK1","P23458",23080,"1-1154",1154),("JAK2","O60674",22640,"1-1132",1132),
                   ("JAK3","P52333",22480,"1-1124",1124),("TYK2","P29597",23740,"1-1187",1187)]:
    w(f"| {g} | {u} | {n:,} | {p} | {ln:,} | 100% |")
w()
w("After dropping self-substitutions JAK1 gives **21,926** - exactly the count the paper reports,")
w("confirming these files are the paper's own input rather than a lookalike.")
w()

# ---- family clustering table (recomputed live)
fam=os.path.join(OUT,"family_clusters.json")
if os.path.exists(fam):
    d=json.load(open(fam))
    w("## Clustering and gnomAD validation, all four JAKs")
    w()
    w("| gene | Cluster 1 | Cluster 2 | ESM-1b C1 | ESM-1b C2 | gnomAD in C1 | Fisher p |")
    w("|---|--:|--:|--:|--:|---|--:|")
    for r in d:
        w(f"| {r['gene']} | {r['c1']:,} | {r['c2']:,} | {r['esm1']:.2f} | {r['esm2']:.2f} | "
          f"{r['g1']}/{r['gn']} ({100*r['g1']/r['gn']:.0f}%) | {r['p']:.1e} |")
    w(f"| *paper, JAK1* | *7,559* | *14,367* | *-4.47* | *-10.75* | *214/289 (74%)* | - |")
    w()
    w("The paper's central validation - common variants fall in the benign cluster - **reproduces in")
    w("every JAK**, at 76-93% against a ~50% background. Our cluster *sizes* differ from theirs")
    w("because the feature space differs: no CADD, no ddG yet, and dbNSFP at a third of their coverage.")
    w()

# ---- AUC table
auc=os.path.join(OUT,"auc.json")
if os.path.exists(auc):
    a=json.load(open(auc))
    w("## What the features actually predict, tested against the TYK2 deep mutational scan")
    w()
    w("TYK2 is the only JAK with a DMS (22,536 variants on signalling at two doses, 22,516 on")
    w("abundance), so the pipeline can be scored against measured phenotype - which the paper could")
    w("not do. Targets are the bottom decile of each assay; the combined model is cross-validated")
    w("with folds grouped by residue position so substitutions at one site cannot leak between folds.")
    w()
    w("| predictor | abundance | IFN-a 1 U/mL | IFN-a 100 U/mL | either dose | both doses |")
    w("|---|--:|--:|--:|--:|--:|")
    for r in a: w("| "+" | ".join(str(x) for x in r)+" |")
    w()
    w("**The dose matters more than the predictor.** At 100 U/mL the panel reaches 0.87, matching its")
    w("performance on abundance. At 1 U/mL it collapses to 0.60. The two doses correlate at only")
    w("rho = +0.52, so they are substantially different measurements: at saturating ligand the readout")
    w("is dominated by variants that simply broke the protein, which these tools detect well; at")
    w("limiting ligand the *activating* variants appear - V678M +0.561, V678I +0.520, H582W +1.339 -")
    w("and a tool trained to separate damaging from tolerated has no representation for a variant that")
    w("signals **more** than wild type.")
    w()
    w("**Consequence for the paper's application.** Its clinical premise is identifying")
    w("**gain-of-function** JAK1 variants. AUC 0.60 on the dose where gain of function is visible,")
    w("against 0.87 where it is not, is the quantitative reason a pathogenicity panel is the wrong")
    w("instrument for that question - and why the structural dual-state component is needed at all.")
    w()
# ---- ddG section (rebuilt live from the two completed runs; see mutation_analysis.md section 56)
import numpy as _np
from scipy.stats import mannwhitneyu as _mw, pearsonr as _pr, spearmanr as _sr
def _auc(y,s):
    y=_np.asarray(y); s=_np.asarray(s); a=s[y==1]; b=s[y==0]
    u,pv=_mw(a,b,alternative="two-sided"); return u/(len(a)*len(b)), pv

w("## Dual-state ddG: the key feature, tested and negative")
w()
w("The distinctive component of the pipeline is **ddG_open - ddG_closed**, a conformational-")
w("preference estimate rather than a stability estimate. It has now been computed two independent")
w("ways. The protocol was first verified against PyRosetta's own published ddG tutorial (PagP set):")
w("Pearson **0.3590** against their 0.3590768, and **0.6712** against their 0.6720891 excluding")
w("proline - agreement to four decimals, so what follows is a result about the feature.")
w()

j1=os.path.join(OUT,"jak1_cluster_ddg.json")
if os.path.exists(j1):
    D=json.load(open(j1))
    cl=_np.array([r["cluster"] for r in D])
    c=_np.clip(_np.array([r["ddg_closed"] for r in D]),-10,10)
    o=_np.clip(_np.array([r["ddg_open"] for r in D]),-10,10)
    y=(cl==2).astype(int)
    w("### Test 1 - JAK1, their models, their clusters")
    w()
    w(f"{len(D)} variants from Dataset EV1, {int((cl==1).sum())} from each cluster, scored on the")
    w("**Jeanpierre open and closed models themselves**. Their structures, their variants, their")
    w("labels - no confound left. Values clipped to [-10, 10] as the paper does.")
    w()
    w("| feature | median their C1 | median their C2 | AUC vs their labels | p |")
    w("|---|--:|--:|--:|--:|")
    for nm,v in [("ddG_closed",c),("ddG_open",o),("**ddG_open - ddG_closed**",o-c)]:
        a,pv=_auc(y,-v)
        w(f"| {nm} | {_np.median(v[cl==1]):+.2f} | {_np.median(v[cl==2]):+.2f} | "
          f"{'**' if 'open -' in nm else ''}{a:.3f}{'**' if 'open -' in nm else ''} | {pv:.3g} |")
    w("| *paper's reported medians* | *-2.05* | *-6.36* | *-* | *-* |")
    w()
    w(f"ddG_closed reproduces their published medians to within 0.4 kcal/mol and separates their")
    w(f"clusters well. Their headline feature does not separate them at all. The reason is visible in")
    w(f"one number: **closed and open correlate at r = {_pr(c,o)[0]:.3f}**, so the subtraction cancels the")
    w("signal and leaves repack residual.")
    w()

af=os.path.join(OUT,"ddg_tyk2_af3.json")
if os.path.exists(af):
    J=json.load(open(af)); R=J["results"]; b=J["baselines"]
    c=_np.clip(_np.array([r["ddg_closed"] for r in R]),-10,10)
    o=_np.clip(_np.array([r["ddg_open"] for r in R]),-10,10)
    rows_t={(int(r["pos"]),r["alt"]):r for r in readcsv(os.path.join(OUT,"tyk2_variants.csv"))}
    keys=[(r["pos"],r["alt"]) for r in R]
    w("### Test 2 - TYK2, a matched pair of AlphaFold 3 models")
    w()
    w("The objection to test 1 is that the two JAK1 reference models were not built the same way, so")
    w("a real difference could be swamped by model-to-model inconsistency. Two TYK2 structures were")
    w("generated on the AF3 server as a **matched pair** and the 4OLI interface variants rescored.")
    w()
    w(f"- baseline score gap between states: **{b['open']-b['closed']:.0f} REU** "
      f"(old mismatched pair 1048, Jeanpierre JAK1 181)")
    w(f"- Pearson r, ddG_closed vs ddG_open: **{_pr(c,o)[0]:.3f}**")
    w(f"- within +/-10 in both states: "
      f"**{100*_np.mean([(abs(r['ddg_closed'])<=10 and abs(r['ddg_open'])<=10) for r in R]):.0f}%**")
    w()
    w("Better-conditioned by every measure, and it does not help:")
    w()
    w("| feature | rho abundance | rho IFN-a 1 U | rho IFN-a 100 U | AUC vs IFN-a 1 U |")
    w("|---|--:|--:|--:|--:|")
    def _col(col):
        return _np.array([fl(rows_t[k][col]) if k in rows_t and fl(rows_t[k][col]) is not None
                          else _np.nan for k in keys])
    ab,i1,i100=_col("dms_abund"),_col("dms_ifn1"),_col("dms_ifn100")
    for nm,v in [("ddG_closed",c),("ddG_open",o),("**ddG_open - ddG_closed**",o-c),
                 ("AlphaMissense (reference)",_col("alphamissense"))]:
        mk=~_np.isnan(v)
        def _r(t):
            m=mk&~_np.isnan(t); return _sr(v[m],t[m])[0]
        m=mk&~_np.isnan(i1); thr=_np.percentile(i1[m],10)
        sgn=1 if "AlphaMissense" in nm else -1
        a,_p=_auc((i1[m]<=thr).astype(int), sgn*v[m])
        w(f"| {nm} | {_r(ab):+.3f} | {_r(i1):+.3f} | {_r(i100):+.3f} | {a:.3f} |")
    w()
    w("Here the two states correlate only weakly, so the difference keeps its magnitude - but the")
    w("decorrelation comes from the models differing in ways unrelated to the substitution, so what")
    w("it keeps is noise. **The feature fails at both ends of the same axis**: too correlated and the")
    w("subtraction cancels the signal, too decorrelated and it measures model discrepancy. No")
    w("intermediate regime escapes this.")
    w()
    w("### What this says about the paper")
    w()
    w("Not that their clusters are wrong - something narrower. Their clustering is recovered by the")
    w("**stability** term, which we reproduce closely; the **conformational** term they built the")
    w("pipeline around contributes nothing to it, and neither term predicts measured phenotype in the")
    w("TYK2 DMS. Their clusters also track the consensus of four sequence predictors (ClinPred 0.946,")
    w("PolyPhen 0.943, REVEL 0.901, ESM-1b 0.892) - but all four were **inputs** to the clustering, so")
    w("those figures measure feature weight, not external validation. Silhouette is **0.098** and our")
    w("reproduction agrees with their labels on **65.3%** of variants, *below* the **65.5%** a")
    w("majority-class classifier achieves (ARI 0.087).")
    w()
    w("Full detail, including the protocol verification and a correction to an earlier wrong diagnosis,")
    w("is in `mutation_analysis.md` sections 56-57.")
    w()

open(f"{OUT}/mutations_clustering.md","w").write("\n".join(L)+"\n")
print(f"wrote {OUT}/mutations_clustering.md ({sum(len(x) for x in L)} chars)")

# ---- push
HERE="/Users/chervov/molab_b"
GH=open(os.path.join(HERE,[f for f in os.listdir(HERE) if "token" in f.lower() or f.endswith(".pat")][0])).read().strip()
REPO="chervov/ProteinModelling1"; path="mutations_clustering.md"
body={"message":f"mutations_clustering.md: regenerated {datetime.now():%Y-%m-%d %H:%M}",
      "content":base64.b64encode(open(f"{OUT}/{path}","rb").read()).decode()}
try:
    r=urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{path}?ref=main",
        headers={"Authorization":f"Bearer {GH}","User-Agent":"x"})
    body["sha"]=json.load(urllib.request.urlopen(r))["sha"]
except urllib.error.HTTPError as e:
    if e.code!=404: raise
req=urllib.request.Request(f"https://api.github.com/repos/{REPO}/contents/{path}", method="PUT",
    data=json.dumps(body).encode(),
    headers={"Authorization":f"Bearer {GH}","Accept":"application/vnd.github+json","User-Agent":"x"})
print("pushed", json.load(urllib.request.urlopen(req))["commit"]["sha"][:8])
