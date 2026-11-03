import json, base64, pathlib
HERE=pathlib.Path(__file__).parent
S=json.load(open(HERE/"stats.json"))
C=json.load(open(HERE/"jak2_clustering_v1_config.json"))
LAB={"esm1b":"ESM-1b","alphamissense":"AlphaMissense","cadd":"CADD","foldx":"FoldX ddG (for MutFunc)",
     "sift":"SIFT","polyphen2":"PolyPhen-2 HumVar","blosum62":"BLOSUM62","clinpred":"ClinPred"}
DIR={"esm1b":"lower = damaging","alphamissense":"higher = damaging","cadd":"higher = damaging",
     "foldx":"higher = destabilising","sift":"lower = damaging","polyphen2":"higher = damaging",
     "blosum62":"lower = less conservative","clinpred":"higher = damaging"}
def img(n,cap):
    b=base64.b64encode((HERE/"figs"/f"{n}.png").read_bytes()).decode()
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

HTML=f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK2 clustering v1</title><style>
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
code{{font:12.5px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 5px;border-radius:4px}}
</style><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
</head><body><div class="wrap">

<h1>JAK2 variant clustering — v1, without the dual-state ΔΔG</h1>
<p class="sub">All {S['n']:,} possible missense substitutions in JAK2 (UniProt O60674, 1,132 aa)
&middot; 8 of the paper's 11 features &middot; generated 3 November 2026</p>

<p class="lede">A two-cluster split of every possible JAK2 missense variant, following the
Jeanpierre/Debeaupuis method. Unlike JAK1 there is <b>no published JAK2 clustering to reproduce</b>,
so the result is validated against data no feature saw — gnomAD allele frequencies and ClinVar
classifications.</p>

<div class="grid">
<div class="stat"><div class="v">{S['n']:,}</div><div class="l">substitutions, 19 × 1,132</div></div>
<div class="stat"><div class="v">{S['sizes'][0]:,} / {S['sizes'][1]:,}</div><div class="l">C1 tolerant / C2 damaging</div></div>
<div class="stat"><div class="v" style="color:var(--good)">{S['gnomad_mh_or']}&times;</div><div class="l">gnomAD depletion, stratified OR</div></div>
<div class="stat"><div class="v" style="color:var(--good)">19/21</div><div class="l">ClinVar labels placed correctly</div></div>
</div>

<div class="key"><b>Why "wo_ddg_oc".</b> Three of the paper's eleven features are ΔΔG in the closed
state, in the open state, and their difference. Those need a dual-state Rosetta run on JAK2, which
does not exist — so this version has <b>eight features and no conformational axis</b>. On JAK1 those
three were the weakest of the set (<code>ddg_delta</code> AUC 0.4966, and dropping all three
<i>improved</i> agreement with the paper, ARI 0.484 → 0.492), so the loss is real but probably
small. A v2 with them is the obvious next step.</div>

<h2>1. Method and seeds</h2>
<p>Gower distance, which compares each pair of variants only on the features both have, so nothing
is imputed. Semi-supervised K-means with 10 seed variants pinned to their clusters. Converged in
<b>{C['iterations']} iterations</b>.</p>
<p>The paper names 10 JAK1 seeds. JAK2 has no published equivalent, so they were derived by an
explicit rule from data no feature saw:</p>
<ul>
<li><b>C1 tolerant</b> — the 5 ClinVar benign/likely-benign variants with the <b>highest gnomAD
allele frequency</b>, all 2-star: <code>{'</code>, <code>'.join(C['seeds_cluster1_tolerant'])}</code>.
Mirrors the paper's "common in the general population (from gnomAD v4)".</li>
<li><b>C2 damaging</b> — the 5 ClinVar pathogenic/likely-pathogenic variants by <b>review stars</b>:
<code>{'</code>, <code>'.join(C['seeds_cluster2_damaging'])}</code>. Mirrors "clinically reported to
cause gain-of-function".</li>
</ul>
<div class="key"><b>The seeds barely matter.</b> Fifteen random 5+5 draws reproduce
<b>{min(C['seed_sensitivity_label_agreement']):.4f}–{max(C['seed_sensitivity_label_agreement']):.4f}</b>
of the labels. As on JAK1, the supervision <i>orients</i> the result — which pole is called
"Cluster 1" — rather than determining its structure. So the hand-made seed rule above is not load
bearing.</div>

<h2>2. How the clusters differ on each feature</h2>
{img("cluster_means","Cluster means, standardised, so features on different scales are comparable. Every feature separates the two clusters in the expected direction.")}
<div class="scroll"><table><thead><tr><th>Feature</th><th class="n">Coverage</th>
<th class="n">C1 mean</th><th class="n">C1 median</th><th class="n">C2 mean</th><th class="n">C2 median</th>
<th class="n">Cohen's d</th><th class="n">AUC</th><th>Direction</th></tr></thead><tbody>{rows}</tbody></table></div>
<p>Every Mann–Whitney p is below 10<sup>−300</sup> (the floating-point floor) except BLOSUM62, so
they are not tabulated — with 21,508 variants, significance is not the interesting quantity.
<b>Effect size is.</b> PolyPhen-2 separates most strongly (d = +3.38), then AlphaMissense (+2.36)
and CADD (+2.09); BLOSUM62 least (−0.62), which is what a position-blind lookup should do.</p>
{img("distributions","Per-feature distributions by cluster. AlphaMissense, PolyPhen-2 and ClinPred are strongly bimodal; BLOSUM62 and FoldX overlap heavily.")}
{img("auc","Per-feature AUC for separating the damaging cluster.")}
<div class="key"><b>These AUCs are circular</b> — these are the features the clustering was built
from, so they describe the split rather than validate it. The validation is section 3.</div>

<h2>3. gnomAD — the external test</h2>
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
clustering has no ΔΔG features, and JAK2's gnomAD coverage, while better in absolute terms, is
concentrated differently. It is not controlled for CpG mutability.</p>

<h2>4. ClinVar — the spot check</h2>
<p>ClinVar has 347 JAK2 missense records but 305 are "Uncertain significance", leaving
<b>21 usable labels</b>. Too few for an odds ratio; enough to catch a clustering that has gone
wrong.</p>
<p><b>Pathogenic ({S['clinvar']['correct'][0]}/{S['clinvar']['correct'][1]} in the damaging
cluster):</b><br>{pth}</p>
<p><b>Benign ({S['clinvar']['correct'][2]}/{S['clinvar']['correct'][3]} in the tolerant
cluster):</b><br>{bn}</p>
<div class="key"><b>19 of 21 placed correctly</b>, and critically <b>V617F is in the damaging
cluster</b> — the canonical JAK2 gain-of-function mutation, and the one result that would have
invalidated the whole exercise had it come out the other way. Note that five of these 21 were
seeds, so the honest score on unseen labels is <b>14 of 16</b>.</div>

<h2>5. Where the damaging variants are</h2>
{img("along_protein","Damaging fraction (red) and gnomAD observation rate (green) in 25-residue windows, with domains shaded and V617F marked.")}
<div class="scroll"><table><thead><tr><th>Domain</th><th class="n">n</th>
<th class="n">% damaging</th><th class="n">% in gnomAD</th></tr></thead><tbody>{dom}</tbody></table></div>

<h2>6. Coverage, and where to be careful</h2>
<p>Three features sit at 31.1% because dbNSFP indexes only single-nucleotide changes. Gower handles
that by comparing on what exists, but on JAK1 the variants with fewest features were where two
clusterings disagreed most.</p>
<div class="scroll" style="max-width:460px"><table><thead><tr><th class="n">Features present</th>
<th class="n">n</th><th class="n">% damaging</th></tr></thead><tbody>{cov}</tbody></table></div>

<h2>7. What this is, and what it is not</h2>
<ul>
<li><b>Not a reproduction.</b> There is no published JAK2 clustering. Nothing here is an ARI
against anyone.</li>
<li><b>Eight features, not eleven.</b> No conformational axis at all.</li>
<li><b>FoldX stands in for "MutFunc"</b>, as on JAK1, and is 94.6% rather than complete — the
missing positions are 1–38, which ProtVar trims as AlphaFold's low-confidence N-terminus.</li>
<li><b>PolyPhen-2 HumVar was used.</b> The paper does not name a model, and HumDiv disagrees on
23.4% of JAK2 variants. That choice is unexamined here and mattered more than any other on JAK1.</li>
<li><b>Equal feature weights</b> — the paper's are unpublished.</li>
<li><b>The gnomAD test is not mutability-controlled.</b> CpG sites mutate ~10× faster.</li>
</ul>

<h2>Methods</h2>
<p>Built from <code>JAK2/clustering/</code>: <code>cluster_jak2.py</code> produces
<code>jak2_clustering_v1.csv</code> and <code>jak2_clustering_v1_config.json</code>; each feature has
its own <code>build_*.py</code> and <code>build_*_jak2_info.md</code> recording source, coverage,
timing and what went wrong. Report built by <code>analyse.py</code> → <code>plots.py</code> →
<code>build_html.py</code>.</p>
<p class="sub">Part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>
</div></body></html>"""
(HERE/"jak2_clustering_v1_wo_ddg_oc.html").write_text(HTML)
print(f"wrote jak2_clustering_v1_wo_ddg_oc.html — {len(HTML)/1e6:.2f} MB")
