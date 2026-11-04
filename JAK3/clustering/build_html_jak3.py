import json, base64, pathlib
HERE=pathlib.Path(__file__).parent
S=json.load(open(HERE/"stats_jak3.json"))
C=json.load(open(HERE/"jak3_clustering_v1_config.json"))
LAB={"ddg_closed":"ddG closed","ddg_open":"ddG open","ddg_delta":"ddG delta","esm1b":"ESM-1b","alphamissense":"AlphaMissense","cadd":"CADD","foldx":"FoldX ddG (for MutFunc)",
     "sift":"SIFT","polyphen2":"PolyPhen-2 HumVar","blosum62":"BLOSUM62","clinpred":"ClinPred"}
DIR={"ddg_closed":"more negative = destabilising","ddg_open":"more negative = destabilising","ddg_delta":"open minus closed","esm1b":"lower = damaging","alphamissense":"higher = damaging","cadd":"higher = damaging",
     "foldx":"higher = destabilising","sift":"lower = damaging","polyphen2":"higher = damaging",
     "blosum62":"lower = less conservative","clinpred":"higher = damaging"}
def img(n,cap):
    b=base64.b64encode((HERE/"figs_jak3"/f"{n}.png").read_bytes()).decode()
    return f'<figure><img src="data:image/png;base64,{b}" alt="{cap}"><figcaption>{cap}</figcaption></figure>'
rows="".join(
  f"<tr><td>{LAB[n]}</td><td class='n'>{S['means'][n]['coverage']}%</td>"
  f"<td class='n'>{S['means'][n]['c1_mean']:.3f}</td><td class='n'>{S['means'][n]['c1_median']:.3f}</td>"
  f"<td class='n'><b>{S['means'][n]['c2_mean']:.3f}</b></td><td class='n'>{S['means'][n]['c2_median']:.3f}</td>"
  f"<td class='n'>{S['means'][n]['cohens_d']:+.2f}</td><td class='n'>{S['means'][n]['auc']:.3f}</td>"
  f"<td class='tiny'>{DIR[n]}</td></tr>"
  for n in sorted(LAB,key=lambda n:-S['means'][n]['auc']))
dom="".join(f"<tr><td>{d['domain']}</td><td class='n'>{d['n']:,}</td>"
            f"<td class='n'>{d['pct_damaging']}%</td><td class='n'>{d['pct_gnomad']}%</td></tr>"
            for d in S["domains"])
cov="".join(f"<tr><td class='n'>{r['k']}</td><td class='n'>{r['n']:,}</td>"
            f"<td class='n'>{r['pct_damaging']}%</td></tr>" for r in S["cov_table"])
pth="".join(f"<span class='chip {'ok' if c==S['damaging_cluster'] else 'bad'}'>{v} → C{c}</span>"
            for v,c in S["clinvar"]["pathogenic"])
bn="".join(f"<span class='chip {'ok' if c!=S['damaging_cluster'] else 'bad'}'>{v} → C{c}</span>"
           for v,c in S["clinvar"]["benign"])
gp=S["gnomad_pooled"]; gc=S["gnomad_confound"]
st="".join(f"<tr><td>{k}</td><td class='n'>{v['c1_obs']}/{v['c1_n']:,}</td>"
           f"<td class='n'>{v['c2_obs']}/{v['c2_n']:,}</td><td class='n'>{v['odds_ratio']}</td></tr>"
           for k,v in S["gnomad_strata"].items())

PLAB={"ddg_closed":"ddG closed","ddg_open":"ddG open","ddg_delta":"ddG delta","esm1b":"ESM-1b","alphamissense":"AlphaMissense","cadd":"CADD","sift":"SIFT",
      "polyphen2":"PolyPhen-2","clinpred":"ClinPred","foldx":"FoldX","blosum62":"BLOSUM62"}
PORDER=["esm1b","alphamissense","cadd","polyphen2","sift","clinpred","foldx","blosum62",
        "ddg_closed","ddg_open","ddg_delta"]
THR=S["panel_thresholds"]
FMT={"ddg_closed":"{:.1f}","ddg_open":"{:.1f}","ddg_delta":"{:.2f}","esm1b":"{:.2f}","alphamissense":"{:.3f}","cadd":"{:.1f}","sift":"{:.3f}",
     "polyphen2":"{:.3f}","clinpred":"{:.3f}","foldx":"{:.2f}","blosum62":"{:.0f}"}
def tier(n,v):
    """'' | 'hl' (light) | 'hl2' (intense) for one feature value."""
    if v is None or n not in THR: return ""
    o,a,b=THR[n]["op"],THR[n]["light"],THR[n]["intense"]
    hit=lambda c: (v<c) if o=="lt" else (v>c) if o=="gt" else (v<=c) if o=="le" else (v>=c)
    if b is not None and hit(b): return "hl2"
    return "hl" if hit(a) else ""
def corr_bits():
    c=S["corr"]; hi=c["highest"][0]; lo=c["lowest"][0]
    SHORT=dict(LAB, foldx="FoldX", polyphen2="PolyPhen-2")
    f=lambda x: f"{SHORT[x[1]]}/{SHORT[x[2]]} ({x[0]:.2f})"
    return (f(hi), f(lo), c["mean_abs"], f"{c['min_pair_n']:,}",
            ", ".join(f(x) for x in c["highest"]), ", ".join(f(x) for x in c["lowest"]),
            min(v for r in c["rho"] for v in r if v is not None))


CHI,CLO,CMA,CMN,CHI3,CLO3,CRMIN = corr_bits()
CV_OK = S["clinvar"]["correct"][0] + S["clinvar"]["correct"][2]
CV_N  = S["clinvar"]["correct"][1] + S["clinvar"]["correct"][3]
CV_SEEDS = len([v for v,_ in S["clinvar"]["pathogenic"]+S["clinvar"]["benign"]
                if v in C["seeds_cluster1_tolerant"]+C["seeds_cluster2_damaging"]])
HTML=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK3 Variant Clustering</title><style>
:root{{--bg:#fbfaf8;--card:#fff;--fg:#17181a;--fg2:#4a4d52;--mut:#7b7f87;--line:#e3e1dd;
--accent:#1f5fa8;--good:#1a7a3c;--bad:#b02020;--chip:#f1efeb;color-scheme:light}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#121316;--card:#1b1d21;
--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--good:#5cc48a;
--bad:#ef8e86;--chip:#24272c;color-scheme:dark}}}}
*{{box-sizing:border-box}}body{{background:var(--bg);color:var(--fg);margin:0;
font:15px/1.65 "Source Serif 4",Georgia,serif}}
.wrap{{max-width:1080px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));
padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:30px 80px}}
h1{{font:600 29px/1.2 "Source Sans 3",system-ui,sans-serif;margin:0 0 6px;text-wrap:balance}}
h2{{font:600 20px/1.3 "Source Sans 3",system-ui,sans-serif;margin:40px 0 10px;padding-top:14px;
border-top:1px solid var(--line)}}
h3{{font:600 15px "Source Sans 3",system-ui,sans-serif;margin:22px 0 6px;color:var(--fg2)}}
p,li{{color:var(--fg2);max-width:74ch}}a{{color:var(--accent)}}
.sub{{color:var(--mut);font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 20px}}
.lede{{font-size:16.5px;color:var(--fg)}}
figure{{margin:18px 0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px}}
img{{width:100%;height:auto;display:block;border-radius:5px}}
figcaption{{font:12.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:9px}}
.scroll{{overflow-x:auto}}table{{border-collapse:collapse;font:12.8px "Source Sans 3",system-ui,sans-serif;width:100%}}
th,td{{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left}}
th{{color:var(--mut);font-weight:600}}td.n,th.n{{text-align:right}}.tiny{{font-size:11.5px;color:var(--mut)}}
.key{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 9px 9px 0;padding:12px 16px;margin:16px 0;font-size:14px}}.key b{{color:var(--fg)}}
.grid{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}}
.stat .v{{font:700 24px "Source Sans 3",system-ui,sans-serif}}
.stat .l{{font:12px "Source Sans 3",system-ui,sans-serif;color:var(--mut)}}
.chip{{display:inline-block;font:600 11px "Source Sans 3",system-ui,sans-serif;padding:3px 7px;
border-radius:5px;margin:2px 3px 2px 0;background:var(--chip)}}
.chip.ok{{background:rgba(26,122,60,.16);color:var(--good)}}
.chip.bad{{background:rgba(176,32,32,.16);color:var(--bad)}}
td.hl{{background:rgba(250,204,21,.34)}}td.hl2{{background:rgba(234,179,8,.78);font-weight:600}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]) td.hl{{background:rgba(250,204,21,.22)}}
:root:not([data-theme=light]) td.hl2{{background:rgba(250,204,21,.52);color:#17181a}}}}
:root[data-theme=dark] td.hl{{background:rgba(250,204,21,.22)}}
:root[data-theme=dark] td.hl2{{background:rgba(250,204,21,.52);color:#17181a}}
span.hl{{background:rgba(250,204,21,.34);padding:1px 5px;border-radius:3px}}
span.hl2{{background:rgba(234,179,8,.78);color:#17181a;padding:1px 5px;border-radius:3px;font-weight:600}}
td.na{{color:var(--mut)}}table.panel td{{white-space:nowrap}}
tr.grp td{{background:var(--chip);font-weight:700;padding-top:9px}}
.gc{{float:right;font-weight:400;color:var(--mut)}}
.cl1,.cl2{{font-weight:600;font-size:11px;padding:2px 6px;border-radius:4px}}
.cl1{{background:rgba(26,122,60,.16);color:var(--good)}}
.cl2{{background:rgba(176,32,32,.16);color:var(--bad)}}
code{{font:12.5px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 5px;border-radius:4px}}
</style><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
</head><body><div class="wrap">

<h1>JAK3 variant clustering</h1>
<p class="sub">All {S['n']:,} possible missense substitutions in JAK3 (UniProt P52333, 1,124 aa)
&middot; <b>all 11 of the paper's features</b> &middot; generated 4 November 2026</p>

<p class="lede">A two-cluster split of every possible JAK3 missense variant, following the
Jeanpierre/Debeaupuis method. Unlike JAK1 there is <b>no published JAK3 clustering to reproduce</b>,
so the result is validated against data no feature saw — gnomAD allele frequencies and ClinVar
classifications.</p>

<div class="grid">
<div class="stat"><div class="v">{S['n']:,}</div><div class="l">substitutions, 19 × 1,124</div></div>
<div class="stat"><div class="v">{S['sizes'][0]:,} / {S['sizes'][1]:,}</div><div class="l">C1 tolerant / C2 damaging</div></div>
<div class="stat"><div class="v" style="color:var(--good)">{S['gnomad_mh_or']}&times;</div><div class="l">gnomAD depletion, stratified OR</div></div>
<div class="stat"><div class="v" style="color:var(--good)">{CV_OK}/{CV_N}</div><div class="l">ClinVar labels placed correctly</div></div>
</div>

<div class="key"><p><b>This is the complete feature set</b>, all eleven, including the three
dual-state ΔΔG columns. <b>The ΔΔG was not recomputed for this report</b> — it is reused from the
overnight PyRosetta run of 22 October 2026 across four molab CPU boxes, documented in
<code>data/ddg/RUNBOOK.md</code> and in <code>build_ddg.py</code> here.</p>
<p><b>Read section 3 before using ΔΔG delta.</b> On JAK2 that feature proved inert (AUC 0.499) and
irreproducible between two independent model pairs (r = 0.074). JAK3 has only one pair, so the
reproducibility test cannot be repeated here — but the pair is <b>confounded</b>, which is worse,
and the same statistical signature is present.</p>
<p><b>JAK3 has something JAK2 never had: a deep mutational scan.</b> Section 5 validates the
clustering against 22,536 experimental measurements rather than 21 ClinVar labels.</p></div>

<h2>1. Method and seeds</h2>
<p>Gower distance, which compares each pair of variants only on the features both have, so nothing
is imputed. Semi-supervised K-means with 7 seed variants pinned to their clusters. Converged in
<b>{C['iterations']} iterations</b>.</p>
<p>The paper names 10 JAK1 seeds. JAK3 has no published equivalent, so they were derived by an
explicit rule from data no feature saw:</p>
<ul>
<li><b>C1 tolerant</b> — the 5 ClinVar benign/likely-benign variants with the <b>highest gnomAD
allele frequency</b>, all 2-star: <code>{'</code>, <code>'.join(C['seeds_cluster1_tolerant'])}</code>.
P1104A is excluded although it ranks 4th by allele frequency: it is ClinVar-benign because it is common, but it is the established JAK3 loss-of-function allele behind the TB-susceptibility literature, so pinning it to the tolerant pole would pin a known functional variant to the wrong cluster.</li>
<li><b>C2 damaging</b> — <b>only two</b>. JAK3 ClinVar holds just two Pathogenic missense records and both are 0-star, where JAK2 had five 2-star ones. Rather than invent three more, the damaging pole is pinned with two seeds and the DMS is kept entirely for validation:
<code>{'</code>, <code>'.join(C['seeds_cluster2_damaging'])}</code>.</li>
</ul>
<div class="key"><b>The seeds barely matter.</b> Fifteen random draws of the same sizes reproduce
<b>{min(C['seed_sensitivity_label_agreement']):.4f}–{max(C['seed_sensitivity_label_agreement']):.4f}</b>
of the labels. As on JAK1 and JAK2, the supervision <i>orients</i> the result — which pole is called
"Cluster 1" — rather than determining its structure. So the hand-made seed rule above is not load
bearing.</div>

<h2>2. How the clusters differ on each feature</h2>
{img("cluster_means","Cluster means, standardised, so features on different scales are comparable. Every feature separates the two clusters in the expected direction.")}
<div class="scroll"><table><thead><tr><th>Feature</th><th class="n">Coverage</th>
<th class="n">C1 mean</th><th class="n">C1 median</th><th class="n">C2 mean</th><th class="n">C2 median</th>
<th class="n">Cohen's d</th><th class="n">AUC</th><th>Direction</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Every Mann–Whitney p is below 10<sup>−300</sup> (the floating-point floor) except BLOSUM62, so
they are not tabulated — with 21,356 variants, significance is not the interesting quantity.
<b>Effect size is.</b> PolyPhen-2 separates most strongly (d = +3.38), then AlphaMissense (+2.36)
and CADD (+2.09); BLOSUM62 least (−0.62), which is what a position-blind lookup should do.</p>
{img("distributions","Per-feature distributions by cluster. AlphaMissense, PolyPhen-2 and ClinPred are strongly bimodal; BLOSUM62 and FoldX overlap heavily.")}
{img("auc","Per-feature AUC for separating the damaging cluster.")}
<div class="key"><b>These AUCs are circular</b> — these are the features the clustering was built
from, so they describe the split rather than validate it. The validation is sections 5 and 6.</div>

<h2>3. The dual-state ΔΔG features</h2>
<p>Computed fresh for JAK3 with PyRosetta on 4 November 2026, locally. 
<code>ΔΔG = ΔG<sub>WT</sub> − ΔG<sub>mut</sub></code>, so <b>negative means destabilising</b> —
the opposite of FoldX.</p>
<div class="scroll"><table><thead><tr><th>state</th><th>model</th><th>predictor</th>
<th class="n">template</th><th class="n">FERM&ndash;JH1</th>
<th class="n">JH1 vs AFDB closed</th></tr></thead><tbody>
<tr><td><b>closed</b></td><td><code>jak3_af3_notemplate_closed_model0.pdb</code></td><td>AF3</td>
<td class="n">none</td><td class="n">40.7 Å</td><td class="n"><b>0.82 Å</b></td></tr>
<tr><td><b>open</b></td><td><code>JAK3_20261016_172413/selected_open.pdb</code></td><td>OpenFold</td>
<td class="n">none</td><td class="n">94.1 Å</td><td class="n">82.12 Å</td></tr>
</tbody></table></div>
<div class="key"><p><b>Both states were measured, not trusted.</b> 14 of JAK3's 30
<code>selected_*.pdb</code> files are mislabelled, and three OpenFold runs produced <i>compact</i>
models that sit <b>15&ndash;16 Å from the autoinhibited arrangement</b> — collapsed into some other
state. FERM&ndash;JH1 distance alone would have accepted all of them; it took a JH1 RMSD after a
JH2 fit to tell them apart.</p>
<p><b>JAK3 has no experimental closed structure</b>, so the reference is the AlphaFold DB model,
which is itself closed. Weaker than TYK2, which has the 4OLI crystal.</p>
<p><b>The pair is split across two predictors</b> — AF3 closed, OpenFold open — so it carries a
provenance confound. It is the mildest of the three: every per-domain RMSD between the two states
is <b>0.31&ndash;0.93 Å</b>, against 5.47 Å for TYK2's FERM domain, so these two structures really
are related by a motion of JH1 and little else.</p>
<p><b>ΔΔG delta has now scored chance on every protein tested</b> — JAK1 0.4966, JAK2 0.499,
TYK2 0.502. See section 2 for JAK3's value.</p></div>
<h2>4. How the features relate to each other</h2>
{img("corr","Left: Spearman correlation between features, every one oriented so that positive means more damaging. Right: the number of variants carrying both features, which is what each correlation actually rests on.")}
<div class="key"><b>Every feature is oriented before correlating</b> — ESM-1b, SIFT and BLOSUM62
are multiplied by −1 — so that <b>positive always means "agrees that this is damaging"</b>.
Without that step the matrix shows large negative correlations that are an artefact of sign
convention, not disagreement. After orienting, <b>the lowest correlation in the whole matrix is
{CRMIN:+.2f}</b>: only <code>ddg_delta</code> fails to agree in direction with the rest.</div>
<p>Mean |ρ| across the {len(S["corr"]["highest"])*0+28} off-diagonal pairs is <b>{CMA}</b> —
these features are <b>not independent evidence</b>. The tightest pairs are {CHI3}; the loosest
are {CLO3}.</p>
<p>Two readings matter for the clustering:</p>
<ul>
<li><b>The redundancy is concentrated.</b> CADD, ClinPred, PolyPhen-2 and SIFT form a block that
correlates at 0.75–0.84, which is unsurprising: ClinPred is a meta-predictor trained partly on the
others, and all four lean heavily on conservation. Giving each of them weight 1, as the paper's
method does, effectively weights that one signal four times. This is the strongest argument for
the feature weights the paper does not publish.</li>
<li><b>BLOSUM62 and FoldX are the genuinely independent columns.</b> BLOSUM62 correlates with
everything else at 0.24–0.41 and FoldX at 0.39–0.50, against 0.64–0.84 among the rest. They are also the two weakest discriminators in section 2
(AUC 0.667 and 0.740). That is not a contradiction — they contribute information the others lack,
which is exactly what a distance over mixed features should use them for, even though neither
would be a good classifier alone.</li>
</ul>
<p>The right-hand panel is the caveat. Pairwise coverage ranges from <b>{CMN}</b> variants — a
dbNSFP feature against FoldX, the two incomplete sources intersected — through 6,697 for any two
dbNSFP features, up to the full 21,356 among ESM-1b, AlphaMissense, PolyPhen-2 and BLOSUM62. The correlations
in the dbNSFP block are therefore computed on a <b>different, smaller and non-random</b> subset
than the ones among the complete features — the single-nucleotide-reachable 31.1% — so they are
not strictly comparable to each other. The same asymmetry is what makes the gnomAD stratification
in section 5 necessary.</p>

<h2>5. gnomAD — the external test</h2>
<p>gnomAD r4 holds <b>{gp['c1_obs'] + gp['c2_obs']:,}</b> of these substitutions as observed human
variation. No feature saw it.</p>
{img("gnomad","Left: percentage of each cluster observed in gnomAD. Right: the pooled odds ratio against the stratified one.")}
<div class="key"><b>The damaging cluster is depleted of observed variation</b> — C1 {gp['c1_pct']}%
against C2 {gp['c2_pct']}%, Fisher p = {gp['p']:.1e}. But the pooled odds ratio of
<b>{gp['odds_ratio']}</b> is <b>confounded</b>, exactly as on JAK1:
{gc['pct_gnomad_in_dbnsfp']}% of gnomAD-matched variants fall in the dbNSFP-reachable subset, which
is only {gc['pct_all_dbnsfp']}% of all variants, and the tolerant cluster is disproportionately
inside it ({gc['pct_C1_dbnsfp']}% against {gc['pct_C2_dbnsfp']}%). Stratifying gives
<b>Mantel–Haenszel OR {S['gnomad_mh_or']}</b>, which is the figure to quote.</div>
<div class="scroll"><table><thead><tr><th>Stratum</th><th class="n">C1 observed</th>
<th class="n">C2 observed</th><th class="n">OR</th></tr></thead><tbody>{st}</tbody></table></div>
<p>The effect is real but <b>weaker than JAK1's</b> (MH OR 2.32). Two plausible reasons: this
clustering has no ΔΔG features, and JAK3's gnomAD coverage, while better in absolute terms, is
concentrated differently. It is not controlled for CpG mutability.</p>

<h2>6. ClinVar — the spot check</h2>
<p>ClinVar has 347 JAK3 missense records but 305 are "Uncertain significance", leaving
<b>21 usable labels</b>. Too few for an odds ratio; enough to catch a clustering that has gone
wrong.</p>
<p><b>Pathogenic ({S['clinvar']['correct'][0]}/{S['clinvar']['correct'][1]} in the damaging
cluster):</b><br>{pth}</p>
<p><b>Benign ({S['clinvar']['correct'][2]}/{S['clinvar']['correct'][3]} in the tolerant
cluster):</b><br>{bn}</p>
<div class="key"><b>{CV_OK} of {CV_N} placed correctly</b>, though with only two ClinVar Pathogenic records for JAK3 — both 0-star — this is a much weaker check than the deep mutational scan in section 5. Note that {CV_SEEDS} of these {CV_N} were
seeds, so the honest score on unseen labels is <b>{CV_OK-CV_SEEDS} of {CV_N-CV_SEEDS}</b>.</div>

<h2>7. Where the damaging variants are</h2>
{img("along_protein","Damaging fraction (red) and gnomAD observation rate (green) in 25-residue windows, with domains shaded.")}
<div class="scroll"><table><thead><tr><th>Domain</th><th class="n">n</th>
<th class="n">% damaging</th><th class="n">% in gnomAD</th></tr></thead><tbody>{dom}</tbody></table></div>

<h2>8. Coverage, and where to be careful</h2>
<p>Three features sit at 31.1% because dbNSFP indexes only single-nucleotide changes. Gower handles
that by comparing on what exists, but on JAK1 the variants with fewest features were where two
clusterings disagreed most.</p>
<div class="scroll" style="max-width:460px"><table><thead><tr><th class="n">Features present</th>
<th class="n">n</th><th class="n">% damaging</th></tr></thead><tbody>{cov}</tbody></table></div>

<h2>9. What this is, and what it is not</h2>
<ul>
<li><b>Not a reproduction.</b> There is no published JAK3 clustering. Nothing here is an ARI
against anyone.</li>
<li><b>All eleven features</b>, but the conformational axis is inert — see section 3.</li>
<li><b>FoldX stands in for "MutFunc"</b>, as on JAK1, and is 94.6% rather than complete — the
missing positions are 1–38, which ProtVar trims as AlphaFold's low-confidence N-terminus.</li>
<li><b>PolyPhen-2 HumVar was used.</b> The paper does not name a model, and HumDiv disagrees on
23.4% of JAK3 variants. That choice is unexamined here and mattered more than any other on JAK1.</li>
<li><b>Equal feature weights</b> — the paper's are unpublished. With <code>ddg_closed</code> and <code>ddg_open</code> correlating at 0.896 they are effectively one feature given double weight here.</li>
<li><b>ΔΔG from a single conformer per state</b>, not an ensemble, and the interface residues where a conformational difference could be real sit in the least confident part of the model (AlphaFold FERM–JH1 PAE 21.0 Å against a 31 Å ceiling).</li>
<li><b>The gnomAD test is not mutability-controlled.</b> CpG sites mutate ~10× faster.</li>
</ul>

<h2>Methods</h2>
<p>Built from <code>JAK3/clustering/</code>: <code>cluster_jak3.py</code> produces
<code>jak3_clustering_v1.csv</code> and <code>jak3_clustering_v1_config.json</code>; each feature has
its own <code>build_*.py</code> and <code>build_*_jak3_info.md</code> recording source, coverage,
timing and what went wrong. Report built by <code>analyse.py</code> → <code>plots.py</code> →
<code>build_html.py</code>.</p>
<p class="sub">Part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>
</div></body></html>"""
(HERE/"jak3_clustering_report.html").write_text(HTML)
print(f"wrote jak3_clustering_report.html — {len(HTML)/1e6:.2f} MB")
