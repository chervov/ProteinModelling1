import json, base64, os
S=json.load(open("stats.json"))
LAB={"esm1b":"ESM-1b","alphamissense":"AlphaMissense","ddg_closed":"ddG closed","ddg_open":"ddG open",
     "ddg_delta":"ddG delta","cadd":"CADD","foldx":"FoldX ddG","sift":"SIFT","polyphen2":"PolyPhen-2",
     "blosum62":"BLOSUM62","clinpred":"ClinPred"}
def img(n, cap):
    b=base64.b64encode(open(f"figs/{n}.png","rb").read()).decode()
    return (f'<figure><img src="data:image/png;base64,{b}" alt="{cap}">'
            f'<figcaption>{cap}</figcaption></figure>')
g=S["gnomad"]
def G(src,c,k): 
    d=g[src]; return (d[str(c)] if str(c) in d else d[c])[k]
KA="all variants"; KD="dbNSFP-defined (all 11 features)"; KM="dbNSFP-missing (8 features)"; KG="in gnomAD r4"
A=S["auc_subsets"]
N=S["auc_n"]
def cell(f,k,bold=False):
    v=A[f][k]
    if v is None: return "<td class='n'>&mdash;</td>"
    t=f"<b>{v:.4f}</b>" if bold else f"{v:.4f}"
    return f"<td class='n'>{t}<br><span style='color:var(--mut);font-size:11px'>n={N[f][k]:,}</span></td>"
sub_rows="".join(
  f"<tr><td>{LAB[f]}</td>"+cell(f,KA)+cell(f,KD,True)+cell(f,KM)+cell(f,KG)+"</tr>"
  for f in sorted(A, key=lambda f:-(A[f][KD] or 0)))
auc_rows="".join(
  f"<tr><td>{LAB[f]}</td><td>{S['auc'][f]['cov']:.1f}%</td>"
  f"<td class='n'>{S['auc'][f]['paper']:.4f}</td><td class='n'>{S['auc'][f]['rebuilt']:.4f}</td>"
  f"<td class='n'>{(S['auc_gnomad'][f] or 0):.4f}</td></tr>"
  for f in sorted(LAB, key=lambda f:-(S['auc'][f]['paper'] or 0)))
strat_rows="".join(
  f"<tr class='{'hi' if r['name']=='both' else 'lo' if r['name']=='neither' else ''}'>"
  f"<td>{r['name']}</td><td class='n'>{r['n']:,}</td><td class='n'>{r['agree']}%</td>"
  f"<td class='n'><b>{r['ari']:.3f}</b></td></tr>" for r in S["strat"])
cov_rows="".join(f"<tr><td class='n'>{r['k']}</td><td class='n'>{r['n']:,}</td>"
                 f"<td class='n'>{r['dis']}%</td></tr>" for r in S["cov_table"])
bc_rows="".join(f"<tr><td>{r['band']}</td><td class='n'>{r['n']:,}</td><td class='n'>{r['all']}%</td>"
                f"<td class='n'>{r['lo'] if r['lo'] is not None else '—'}%</td>"
                f"<td class='n'>{r['hi'] if r['hi'] is not None else '—'}%</td></tr>" for r in S["band_cov"])
af_rows="".join(f"<tr><td>{k}</td><td class='n'>{v['n']:,}</td><td class='n'>{v['pct_in_C2_paper']}%</td>"
                f"<td class='n'>{v['pct_in_C2_rebuilt']}%</td></tr>" for k,v in S["gnomad_by_af"].items())

HTML=f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK1 clustering analysis</title>
<style>
:root{{--bg:#fbfaf8;--card:#fff;--fg:#17181a;--fg2:#4a4d52;--mut:#7b7f87;--line:#e3e1dd;
--accent:#1f5fa8;--good:#1a7a3c;--bad:#b02020;--chip:#f1efeb;color-scheme:light}}
@media(prefers-color-scheme:dark){{:root:not([data-theme=light]){{--bg:#121316;--card:#1b1d21;--fg:#eceef1;
--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--good:#5cc48a;--bad:#ef8e86;--chip:#24272c;
color-scheme:dark}}}}
*{{box-sizing:border-box}}
body{{background:var(--bg);color:var(--fg);margin:0;font:15px/1.65 "Source Serif 4",Georgia,serif}}
.wrap{{max-width:1080px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));
padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:30px 80px}}
h1{{font:600 30px/1.2 "Source Sans 3",system-ui,sans-serif;margin:0 0 6px;text-wrap:balance}}
h2{{font:600 20px/1.3 "Source Sans 3",system-ui,sans-serif;margin:42px 0 10px;padding-top:14px;
border-top:1px solid var(--line)}}
h3{{font:600 15px "Source Sans 3",system-ui,sans-serif;margin:24px 0 6px;color:var(--fg2)}}
p,li{{color:var(--fg2);max-width:74ch}} a{{color:var(--accent)}}
.sub{{color:var(--mut);font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 20px}}
.lede{{font-size:16.5px;color:var(--fg)}}
figure{{margin:18px 0;background:var(--card);border:1px solid var(--line);border-radius:10px;padding:12px}}
img{{width:100%;height:auto;display:block;border-radius:5px}}
figcaption{{font:12.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:9px}}
.scroll{{overflow-x:auto}}
table{{border-collapse:collapse;font:12.8px "Source Sans 3",system-ui,sans-serif;width:100%}}
th,td{{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left}}
th{{color:var(--mut);font-weight:600}} td.n,th.n{{text-align:right}}
tr.hi td{{background:rgba(26,122,60,.10)}} tr.lo td{{background:rgba(176,32,32,.10)}}
.key{{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 9px 9px 0;padding:12px 16px;margin:16px 0;font-size:14px}}
.key b{{color:var(--fg)}}
.grid{{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(220px,1fr))}}
.stat{{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}}
.stat .v{{font:700 25px "Source Sans 3",system-ui,sans-serif;color:var(--fg)}}
.stat .l{{font:12px "Source Sans 3",system-ui,sans-serif;color:var(--mut)}}
code{{font:12.5px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 5px;border-radius:4px}}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600;700&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
</head><body><div class="wrap">

<h1>JAK1 variant clustering — exploratory analysis</h1>
<p class="sub">All {S['n']:,} substitutions from <code>jak1_clustering_rebuilt.csv</code> &middot;
paper's Dataset EV1 clustering vs the rebuild &middot; gnomAD r4 &middot; generated 3 November 2026</p>

<p class="lede">Two clusterings of the same {S['n']:,} JAK1 missense substitutions — the one published
in Dataset EV1 and the one rebuilt here — agree on 84.9% of variants, ARI 0.484. This report asks
what the features look like, how well each separates the clusters, where the two disagree, and
whether either agrees with population genetics.</p>

<div class="grid">
<div class="stat"><div class="v">{S['n']:,}</div><div class="l">substitutions, 19 × 1,154</div></div>
<div class="stat"><div class="v">0.484</div><div class="l">ARI, all variants</div></div>
<div class="stat"><div class="v" style="color:var(--good)">0.786</div><div class="l">ARI where data is complete</div></div>
<div class="stat"><div class="v">{G('paper',1,'frac')/G('paper',2,'frac'):.2f}&times;</div><div class="l">gnomAD depletion, damaging cluster</div></div>
</div>

<div class="key"><b>Cluster identity.</b> Nothing in Dataset EV1 states which label means what.
From the data it is unambiguous: <b>cluster 1 = tolerant</b> (AlphaMissense median 0.166),
<b>cluster 2 = damaging</b> (median 0.953). All of this report uses that convention.</div>

<h2>1. Feature distributions</h2>
<p>Eleven features, each shown separately for the paper's two clusters. Coverage is in the panel
title: five features are complete, three sit at 31.3% because dbNSFP indexes only single-nucleotide
changes, and FoldX is at 94.9%.</p>
{img("hist_by_cluster","Per-feature distributions split by the paper's EV1 cluster. Densities, not counts, so the two clusters are comparable despite their different sizes.")}
<p>AlphaMissense, PolyPhen-2 and ClinPred are strongly bimodal and separate the clusters almost
completely. The two state-specific ΔΔG features are shifted but heavily overlapping, and
<code>ddg_delta</code> is all but identical between clusters.</p>
<div class="key"><b>Sign convention, easy to get wrong.</b> The Rosetta columns are
ΔΔG = ΔG<sub>WT</sub> − ΔG<sub>mut</sub>, so <b>negative = destabilising</b> — the opposite of FoldX
in the same table, where positive = destabilising
(<code>build_rosetta_ddg_jak1_info.md</code> §2). Everything in this report is oriented so that
larger always means more damaging. Scored with the wrong sign, ΔΔG closed appears to have
AUC 0.26; oriented correctly it is 0.74.</div>

<h2>2. Feature correlation</h2>
<p>Spearman ρ on pairwise-complete observations, every feature oriented so that larger means more
damaging, so all genuine agreement appears positive.</p>
{img("corr","Spearman correlation between features, oriented so + = more damaging.")}
<div class="key"><b>BLOSUM62 is the outlier</b> — it is the only position-blind feature, a 20×20
lookup, so every V→F scores the same wherever it sits. The ΔΔG features correlate strongly with each
other and weakly with everything else, which is expected: they measure thermodynamic stability,
while the rest measure evolutionary or clinical pathogenicity. These are different quantities.</div>

<h2>3. How well does each feature separate the clusters?</h2>
<p>AUC for discriminating cluster 2 (damaging), <b>computed on each feature's own coverage</b> — so
the rows are <i>not</i> directly comparable, since ClinPred, CADD and SIFT are scored on 6,873
variants and the rest on 21,926. The next subsection fixes that. The third
column asks a different question: can the feature tell a variant that is <i>observed in gnomAD</i>
from one that is not? That is an external check, since no clustering used gnomAD.</p>
{img("auc","Per-feature AUC against both clusterings. Coverage in parentheses.")}
<div class="scroll"><table><thead><tr><th>Feature</th><th class="n">Coverage</th>
<th class="n">AUC vs paper</th><th class="n">AUC vs rebuilt</th><th class="n">AUC vs gnomAD</th></tr></thead>
<tbody>{auc_rows}</tbody></table></div>

<h3>The same comparison on matched subsets</h3>
<p>The table above is not a fair race. ClinPred, CADD and SIFT are scored on only 31.3% of variants —
the ones reachable by a single nucleotide change — while AlphaMissense, PolyPhen-2 and ESM-1b are
scored on all of them. Restricting every feature to the <b>same</b> variants changes the ranking.</p>
{img("auc_subsets","Left: each feature on all variants (grey) against the matched dbNSFP subset (blue). Right: the easier dbNSFP-defined subset against the harder complement.")}
<div class="scroll"><table><thead><tr><th>Feature</th>
<th class="n">own coverage<br><span style="font-weight:400">(subset 21,926)</span></th>
<th class="n">dbNSFP-defined<br><span style="font-weight:400">(subset 6,873)</span></th>
<th class="n">dbNSFP-missing<br><span style="font-weight:400">(subset 15,053)</span></th>
<th class="n">in gnomAD<br><span style="font-weight:400">(subset 982)</span></th></tr></thead>
<tbody>{sub_rows}</tbody></table></div>
<p style="font-size:13.5px"><b>Read the first column carefully.</b> AUC is computed on each feature's
own non-missing rows, so "own coverage" is <i>not</i> 21,926 for every feature — it is 6,873 for
ClinPred, CADD and SIFT and 20,805 for FoldX. The <code>n=</code> under each value is what was
actually used. That silent mismatch is precisely why the matched columns are needed: only there is
every feature scored on identical variants.</p>
<div class="key"><b>On equal footing, AlphaMissense is the best feature</b> — 0.9470 against ClinPred's
0.9463 — and PolyPhen-2 (0.9423) overtakes CADD (0.9284). The apparent lead of ClinPred and CADD in
the previous table is an artefact of <i>which</i> variants they are scored on, not of how well they
score them.<br><br>
<b>The dbNSFP subset is intrinsically easier.</b> Every feature with full coverage gains on it:
AlphaMissense +0.061, PolyPhen-2 +0.058, BLOSUM62 +0.022, FoldX +0.018. Single-nucleotide-reachable
substitutions are the milder, better-characterised ones, so a clustering evaluated only there looks
better than it is.<br><br>
<b>ESM-1b is the most robust.</b> It is the only strong feature that barely moves between the two
halves (0.8964 → 0.8884) and it is the <b>best feature on the harder half</b>, ahead of AlphaMissense
(0.8551) and PolyPhen-2 (0.8515). Where the genomic predictors cannot go at all, the protein language
model still works — which is the argument for weighting it more heavily than its all-variant AUC
suggests.</div>

<h2>4. gnomAD enrichment — the external validation</h2>
<p>gnomAD r4 holds {S['gnomad_total']} missense variants for JAK1, {S['n_gnomad']} of which match a
substitution in this dataset. Neither clustering used gnomAD, so the extent to which observed human
variation avoids the damaging cluster is an independent test of both.</p>
{img("gnomad_enrich","Percentage of each cluster observed in gnomAD r4. Both clusterings deplete the damaging cluster by about 2.5-fold.")}
<div class="key"><b>Both clusterings pass, and they pass equally.</b> The paper's damaging cluster is
<b>{G('paper',1,'frac')/G('paper',2,'frac'):.2f}&times; depleted</b> of gnomAD-observed variants
(7.46% vs 2.91%, Fisher p = {g['paper']['p']:.1e}); the rebuild gives
<b>{G('rebuilt',1,'frac')/G('rebuilt',2,'frac'):.2f}&times;</b> (7.15% vs 2.82%, p = {g['rebuilt']['p']:.1e}).
Purifying selection is recovered by an unsupervised split that never saw population data. Critically,
<b>the two clusterings are indistinguishable on this criterion</b> despite disagreeing on one variant
in seven — so ARI 0.484 does not mean one is right and the other wrong.</div>

<h3>Does allele frequency track the call?</h3>
{img("gnomad_af","Percentage assigned to the damaging cluster, by gnomAD allele-frequency band.")}
<div class="scroll"><table><thead><tr><th>gnomAD band</th><th class="n">n</th>
<th class="n">% called damaging, paper</th><th class="n">% called damaging, rebuilt</th></tr></thead>
<tbody>{af_rows}</tbody></table></div>
<p>The gradient runs the right way: the commoner a variant is in the population, the less often
either clustering calls it damaging. Variants absent from gnomAD are called damaging most often of
all — as they should be, since they include everything purifying selection has removed.</p>

<h3>Along the protein</h3>
{img("along_protein","Damaging fraction (red, left axis) and gnomAD observation rate (green, right axis) in 25-residue windows, with UniProt domains shaded.")}
<p>The two curves run opposite: Spearman ρ = <b>{S['window_anticorr']['rho']}</b>
(p = {S['window_anticorr']['p']:.1e}, {S['window_anticorr']['n_windows']} windows). The JH1 kinase
domain is the most damaging-dense and the most gnomAD-depleted region of the protein; the
FERM–SH2 linker region is the most tolerant.</p>

<h2>5. Where the two clusterings disagree</h2>
<p>3,318 variants (15.1%) receive different labels. They are not randomly placed — two independent
effects concentrate them.</p>
{img("disagreement","Left: disagreement by number of features present. Right: AlphaMissense band crossed with coverage.")}
<div class="scroll" style="max-width:520px"><table><thead><tr><th class="n">Features present</th>
<th class="n">n</th><th class="n">Disagreement</th></tr></thead><tbody>{cov_rows}</tbody></table></div>
<h3>Band and coverage are independent</h3>
<div class="scroll"><table><thead><tr><th>AlphaMissense band</th><th class="n">n</th>
<th class="n">overall</th><th class="n">≤8 features</th><th class="n">≥10 features</th></tr></thead>
<tbody>{bc_rows}</tbody></table></div>
<p>Within every band, coverage still costs 6.8 to 16.1 percentage points. The band effect is 3.0×,
the coverage effect 2.1×, and they multiply — a 30-fold spread from the best cell (confident
damaging at high coverage, 1.2%) to the worst (intermediate-low at low coverage, 36.5%).</p>

<h2>6. What this does to the headline ARI</h2>
{img("ari_strat","ARI against the paper's clustering, restricted to progressively better-determined subsets.")}
<div class="scroll"><table><thead><tr><th>Subset</th><th class="n">n</th>
<th class="n">Agreement</th><th class="n">ARI</th></tr></thead><tbody>{strat_rows}</tbody></table></div>
<div class="key"><b>The reproduction is substantially better than ARI 0.484 suggests.</b> Where both
clusterings have the data to decide — at least 10 of 11 features and an unambiguous AlphaMissense
score — they agree <b>94.3%</b> at <b>ARI 0.786</b>. The headline is dragged down by 4,976 variants
with sparse features <i>and</i> an intermediate score, which disagree 68% of the time at ARI 0.130,
barely above the 53.6% permutation null. Those are substitutions needing two or three nucleotide
changes, so CADD, SIFT and ClinPred are absent by construction, leaving Gower distance over 7–8
dimensions on a variant that is ambiguous anyway. <b>Neither label is trustworthy there.</b></div>
<p>This reorders the candidate explanations for the gap. Dropping all three ΔΔG features moves ARI
0.484 → 0.492; the HumDiv/HumVar choice is worth about ΔARI 0.090. Stratifying by data quality moves
it 0.484 → 0.786 — an order of magnitude more explanatory power than either. The dominant cause is
<b>missingness interacting with the Gower distance</b>, not a methodological difference between the
two pipelines.</p>

<h2>7. What follows</h2>
<ul>
<li><b>Both clusterings are externally valid and equally so.</b> 2.5× gnomAD depletion each,
p ≈ 10<sup>−50</sup>, from a split that never saw population data.</li>
<li><b>The published assignment carries very different per-variant confidence, and EV1 does not mark
which.</b> A variant in the well-determined set (n = 4,931) is solid; one in the ill-determined set
(n = 4,976) is close to arbitrary. A confidence field — feature count plus distance to the decision
boundary — would be more useful than further tuning of the clustering.</li>
<li><b>The ΔΔG features discriminate, but do not help.</b> Oriented correctly, ΔΔG closed and open
reach AUC 0.74 — on a par with FoldX at 0.72 — so they are not uninformative. Yet dropping all
three <i>improves</i> agreement with the paper (ARI 0.484 → 0.492), which says they are largely
redundant with FoldX while adding their own noise. <code>ddg_delta</code> is the genuine null at
AUC 0.497.</li>
<li><b>Coverage is the lever worth pulling.</b> The three 31.3% features are missing precisely where
the clustering is least certain. Running SIFT and CADD natively, as PolyPhen-2 already was, would
close most of the ill-determined set.</li>
</ul>

<h2>Methods</h2>
<p>Source <code>JAK1/clustering/jak1_clustering_rebuilt.csv</code> (21,926 rows, 11 features, both
cluster labels). gnomAD r4 missense variants fetched from the GraphQL API by gene symbol and matched
on (position, alternate residue); {S['n_gnomad']} of {S['gnomad_total']} matched. AUC computed as the
rank-sum statistic on each feature's own coverage, with features oriented so larger = more damaging.
Enrichment tested by Fisher's exact test. ARI is the standard adjusted Rand index. Scripts:
<code>fetch_gnomad.py</code>, <code>analyse.py</code>, <code>plots.py</code>, <code>plots2.py</code>,
<code>build_html.py</code>.</p>
<p class="sub">Part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a>
&middot; companion to <code>README.md</code> and <code>clustering_jak1_results.md</code></p>
</div></body></html>"""
open("jak1_clustering_analysis.html","w").write(HTML)
print(f"wrote jak1_clustering_analysis.html — {len(HTML)/1e6:.2f} MB")
