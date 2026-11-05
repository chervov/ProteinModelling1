"""Self-contained HTML for the ddG method survey."""
import base64, json, pathlib
H = pathlib.Path(__file__).parent
S = json.load(open(H / "ddg_survey.json"))
SH = {"rosetta_closed":"Rosetta closed","rosetta_open":"Rosetta open","rosetta_delta":"Rosetta delta",
      "thermompnn":"ThermoMPNN","foldx":"FoldX","rsa":"RSA","alphamissense":"AlphaMissense",
      "polyphen2":"PolyPhen-2","esm1b":"ESM-1b","cadd":"CADD"}
STAB = {"rosetta_closed","rosetta_open","rosetta_delta","thermompnn","foldx","rsa"}
PROTS = list(S["proteins"])

def img(n, cap):
    f = H / "figs" / f"{n}.png"
    return "" if not f.exists() else (
        f'<figure><img src="data:image/png;base64,{base64.b64encode(f.read_bytes()).decode()}"'
        f' alt="{cap}"><figcaption>{cap}</figcaption></figure>')

# .describe() table, all proteins
STATS = ["count","mean","std","min","25%","50%","75%","max"]
def desc_tbl():
    out = []
    for p in PROTS:
        d = S["proteins"][p]["describe"]
        out.append(f"<tr class='grp'><td colspan='{len(STATS)+2}'>{p}</td></tr>")
        for m in [k for k in SH if k in d]:
            r = d[m]
            out.append(f"<tr><td>{SH[m]}</td><td class='n tiny'>{S['proteins'][p]['coverage'][m]}%</td>"
                       + "".join(f"<td class='n'>{('' if r.get(s) is None else (f'{r[s]:,.0f}' if s=='count' else f'{r[s]:.2f}'))}</td>"
                                 for s in STATS) + "</tr>")
    return "".join(out)

def cluster_tbl():
    out = []
    for p in PROTS:
        bc = S["proteins"][p].get("by_cluster", {})
        out.append(f"<tr class='grp'><td colspan='6'>{p}</td></tr>")
        for m in sorted(bc, key=lambda x: -bc[x]["auc"]):
            v = bc[m]
            cls = "stab" if m in STAB else ""
            out.append(f"<tr class='{cls}'><td>{SH[m]}</td><td class='n'>{v['c1_mean']:.3f}</td>"
                       f"<td class='n'>{v['c2_mean']:.3f}</td><td class='n'>{v['c1_median']:.3f}</td>"
                       f"<td class='n'>{v['c2_median']:.3f}</td>"
                       f"<td class='n'><b>{v['auc']:.3f}</b></td></tr>")
    return "".join(out)

def dms_tbl():
    D = S["tyk2_dms"]
    ms = sorted(D, key=lambda m: -abs(D[m].get("abundance", {}).get("spearman", 0)))
    return "".join(
        f"<tr class='{'stab' if m in STAB else ''}'><td>{SH[m]}</td>"
        f"<td class='n'>{D[m].get('abundance',{}).get('n',0):,}</td>"
        f"<td class='n'><b>{abs(D[m].get('abundance',{}).get('spearman',0)):.3f}</b></td>"
        f"<td class='n'>{abs(D[m].get('ifn_100U',{}).get('spearman',0)):.3f}</td></tr>" for m in ms)

def outlier_tbl():
    B = S["proteins"]["JAK2"]["by_target_aa"]
    aas = sorted(B["rosetta_closed"], key=lambda a: -B["rosetta_closed"][a]["pct_extreme"])
    g = lambda m, a: B.get(m, {}).get(a, {}).get("pct_extreme")
    return "".join(
        f"<tr class='{'hi' if a in 'FPWY' else ''}'><td><b>{a}</b></td>"
        f"<td class='n'>{g('rosetta_closed',a):.1f}%</td>"
        f"<td class='n'>{(f'{g(chr(102)+chr(111)+chr(108)+chr(100)+chr(120),a):.1f}%' if g('foldx',a) is not None else '&mdash;')}</td>"
        f"<td class='n'>{(f'{g(chr(116)+chr(104)+chr(101)+chr(114)+chr(109)+chr(111)+chr(109)+chr(112)+chr(110)+chr(110),a):.1f}%' if g('thermompnn',a) is not None else '&mdash;')}</td>"
        f"</tr>" for a in aas)

def corr_tbl(p):
    v = S["proteins"][p]; cols = v["corr_cols"]; C = v["corr_spearman"]
    def cell(x):
        if x is None: return "<td class='n'>&mdash;</td>"
        cl = "c3" if abs(x) > .75 else "c2" if abs(x) > .5 else "c1" if abs(x) > .25 else ""
        return f"<td class='n {cl}'>{x:.2f}</td>"
    hdr = "<tr><th></th>" + "".join(f"<th class='n'>{SH[c]}</th>" for c in cols) + "</tr>"
    body = "".join(f"<tr><td class='rh'>{SH[a]}</td>" + "".join(cell(C[a][b]) for b in cols) + "</tr>"
                   for a in cols)
    return f"<table><thead>{hdr}</thead><tbody>{body}</tbody></table>"

HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK ΔΔG Method Survey</title><style>
:root{--bg:#fbfaf8;--card:#fff;--fg:#17181a;--fg2:#4a4d52;--mut:#7b7f87;--line:#e3e1dd;
--accent:#1f5fa8;--chip:#f1efeb;--good:#1a7a3c;--bad:#b02020;--hi:#fff6d8;color-scheme:light}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#121316;--card:#1b1d21;
--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--chip:#24272c;
--good:#5cc48a;--bad:#ef8e86;--hi:#36301c;color-scheme:dark}}
:root[data-theme=dark]{--bg:#121316;--card:#1b1d21;--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;
--line:#2d3036;--accent:#7fb0ef;--chip:#24272c;--good:#5cc48a;--bad:#ef8e86;--hi:#36301c;
color-scheme:dark}
*{box-sizing:border-box}body{background:var(--bg);color:var(--fg);margin:0;
font:15px/1.62 "Source Serif 4",Georgia,serif}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));
padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 72px}
h1{font:600 28px/1.2 "Source Sans 3",system-ui,sans-serif;margin:0 0 5px;text-wrap:balance}
h2{font:600 19px "Source Sans 3",system-ui,sans-serif;margin:38px 0 10px;padding-top:13px;
border-top:1px solid var(--line)}
h3{font:600 15px "Source Sans 3",system-ui,sans-serif;margin:22px 0 6px;color:var(--fg2)}
p,li{color:var(--fg2);max-width:76ch}a{color:var(--accent)}
.sub{color:var(--mut);font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 18px}
.lede{font-size:16.5px;color:var(--fg)}
figure{margin:16px 0;background:var(--card);border:1px solid var(--line);border-radius:11px;
padding:10px;min-width:0}
figure img{display:block;width:100%;height:auto;border-radius:6px;background:#fff}
figcaption{font:12.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:9px}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;
font:12.4px "Source Sans 3",system-ui,sans-serif}
th,td{padding:5px 9px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}
th{color:var(--mut);font-weight:600}td.n,th.n{text-align:right}
tr.grp td{background:var(--chip);font-weight:700}
tr.hi td{background:var(--hi)}
tr.stab td:first-child{font-weight:700;color:var(--accent)}
td.rh{font-weight:600;color:var(--fg)}
td.c1{background:rgba(31,95,168,.07)}td.c2{background:rgba(31,95,168,.18)}
td.c3{background:rgba(31,95,168,.34)}
.tiny{font-size:11px;color:var(--mut)}
.key{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 9px 9px 0;padding:12px 16px;margin:15px 0;font-size:14px}.key b{color:var(--fg)}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(200px,1fr))}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}
.stat .v{font:700 24px "Source Sans 3",system-ui,sans-serif}
.stat .l{font:12px "Source Sans 3",system-ui,sans-serif;color:var(--mut)}
code{font:12.3px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 5px;
border-radius:4px}
.tabs{display:flex;gap:6px;margin:12px 0}
.tab{font:600 12px "Source Sans 3",system-ui,sans-serif;padding:6px 13px;border-radius:6px;
border:1px solid var(--line);background:transparent;color:var(--fg2);cursor:pointer}
.tab.on{background:var(--accent);color:#fff;border-color:var(--accent)}
</style></head><body><div class="wrap">

<h1>ΔΔG for the JAK family: what exists, what we computed, and what it is worth</h1>
<p class="sub">Four proteins, 87,343 substitutions, three ΔΔG methods plus RSA, measured against
each other, against the clustering and against the one experimental dataset &middot;
5 November 2026</p>

<div class="grid">
<div class="stat"><div class="v">0.52&ndash;0.56</div><div class="l">agreement between ΔΔG methods (ρ)</div></div>
<div class="stat"><div class="v" style="color:var(--good)">RSA</div><div class="l">beats all three at separating the clusters</div></div>
<div class="stat"><div class="v" style="color:var(--bad)">92.5%</div><div class="l">of X&rarr;P extreme in Rosetta, 2.5% in FoldX</div></div>
<div class="stat"><div class="v">0.26&ndash;0.42</div><div class="l">best |ρ| against experimental DMS</div></div>
</div>

<p class="lede">Three ΔΔG methods cover these proteins completely, and they agree with each other
only moderately. A single geometric number &mdash; relative solvent accessibility &mdash;
tracks them nearly as well as they track each other, and beats all three at the job we actually
use them for. The extreme-value tail that disfigures our PyRosetta numbers turns out to be
largely a PyRosetta artefact, and the proline part of it entirely so.</p>

<h2>1. What methods exist</h2>
<div class="scroll"><table><thead><tr><th>family</th><th>methods</th><th>note</th></tr></thead>
<tbody>
<tr><td>force field</td><td><b>FoldX</b>, Rosetta <code>ddg_monomer</code>, Rosetta <code>cartesian_ddg</code></td><td>cartesian_ddg is most robust to modelling error</td></tr>
<tr><td>statistical potential</td><td>PoPMuSiC, mCSM, DUET, SDM, DDMut</td><td>fast; graph / environment features</td></tr>
<tr><td>learned, structure-aware</td><td><b>ThermoMPNN</b>, RaSP, Stability Oracle, SPURS, ThermoNet</td><td>trained on mega-scale data</td></tr>
<tr><td>sequence / evolution</td><td>GEMME, EVE, TranceptEVE, ESM-2, ProSST, SaProt</td><td>not ΔΔG, but competitive on stability DMS</td></tr>
<tr><td><b>two-feature baseline</b></td><td><b>RSALOR</b> = log-odds ratio &times; RSA</td><td>see section 5</td></tr>
</tbody></table></div>
<div class="key"><b>The field's real ceiling.</b> On genuinely unseen single mutations the best
methods reach <b>r ≈ 0.5&ndash;0.6</b>, not the 0.7&ndash;0.8 advertised — the gap is
training-set leakage, direct+reverse evaluation, and random rather than homology-aware splits.
Experimental noise caps the achievable value at r ≈ 0.7&ndash;0.8. For interpreting human
missense variants ΔΔG is a <b>weak classifier</b> (AUC ≈ 0.66&ndash;0.68), because many
pathogenic variants do not act by destabilisation. And there is <b>no benchmark on large
multi-domain proteins</b> — which is what the JAKs are. Sources, with DOIs, in
<code>external_data/ddg_literature.md</code>.</div>

<h2>2. Distributions</h2>
__FIG_HIST__
<h3>Summary statistics</h3>
<div class="scroll"><table><thead><tr><th>method</th><th class="n">cov</th>
__DHDR__</tr></thead><tbody>__DESC__</tbody></table></div>

<h2>3. How the methods agree</h2>
__FIG_CORR__
<div class="tabs" id="ctabs"></div>
<div class="scroll" id="cbox"></div>
<div class="key"><p><b>The ΔΔG methods agree only moderately</b> — Rosetta against the other two at
0.52&ndash;0.56, FoldX against ThermoMPNN at 0.69&ndash;0.70. The figure above shows the same
pattern in all four proteins, to ±0.03.</p>
<p><b>Now read the RSA row against the Rosetta row.</b> RSA correlates with ThermoMPNN at
<b>0.59</b>; PyRosetta — a full force-field calculation costing ~1.5 h per protein — correlates
with the same ThermoMPNN at <b>0.54</b>. The free number does better.</p>
<p><b><code>ddg_delta</code> is flat against everything</b> (|ρ| ≤ 0.02), as it is against the
clustering and the DMS.</p></div>

<h2>4. The four-residue outlier tail &mdash; is it Rosetta's?</h2>
__FIG_OUT__
<div class="scroll" style="max-width:620px"><table><thead><tr><th>substituted-in</th>
<th class="n">Rosetta ΔΔG &lt; &minus;10</th><th class="n">FoldX &gt; +10</th>
<th class="n">ThermoMPNN &gt; +10</th></tr></thead><tbody>__OUT__</tbody></table></div>
<div class="key"><p><b>Three separate conclusions.</b></p>
<p><b>ThermoMPNN has no tail at all</b> — 0.0% for all twenty residues. A bounded neural-net
output cannot produce a &minus;2,900 kcal/mol value, so the comparison is partly unfair; but it
does establish that the tail is not a property of the substitutions themselves.</p>
<p><b>FoldX reproduces the aromatic ranking</b> — W, Y, F are its top three (14.1 / 11.0 / 7.0%).
So the <b>steric mechanism is real</b>: forcing a large aromatic into a packed core genuinely
clashes.</p>
<p><b>FoldX does not reproduce proline</b> — 2.5% against Rosetta's <b>92.5%</b>. That part is a
backbone-geometry failure specific to our protocol: <code>mutate_residue</code> with an 8 Å
repack does not re-sample the backbone, and proline's ring constrains φ, so a proline forced
into a non-proline backbone registers an enormous clash that relaxation would relieve.</p>
<p><b>Practical consequence:</b> winsorise or rank-transform the Rosetta ΔΔG before use, and do
not interpret raw X&rarr;P values at all.</p></div>

<h2>5. RSA, and the two-feature baseline</h2>
__FIG_RSA__
<div class="key"><p><b>Tsishyn, Pucci &amp; Rooman, <i>Bioinformatics</i> 2025 — RSALOR</b>
(<a href="https://doi.org/10.1093/bioinformatics/btaf322">10.1093/bioinformatics/btaf322</a>).
Two features — log-odds ratio from an MSA &times; relative solvent accessibility — benchmarked on
ProteinGym (~700,000 mutations, 218 DMS sets) against 27 predictors including 19 protein language
models. On the <b>Stability</b> slice: ProSST-2048 0.638, SaProt 0.565, <b>RSALOR 0.551</b>,
ESM2-650M 0.496, <b>&minus;RSA alone 0.480</b>, conservation alone 0.447 (Spearman).</p>
<p><b>RSA alone beats ESM2-650M on stability</b>, and the two-feature model beats most deep
models. Our numbers reproduce the shape of that result on the JAKs independently.</p></div>
<p>We have RSALOR output for JAK2 already (<code>data/ddg/rsalor_jak2_family.csv</code>) but have
not yet used it as a clustering feature. It is the clearest cheap improvement available.</p>

<h2>6. Separating the clusters</h2>
__FIG_CLU__
<div class="scroll"><table><thead><tr><th>method</th><th class="n">C1 mean</th>
<th class="n">C2 mean</th><th class="n">C1 median</th><th class="n">C2 median</th>
<th class="n">AUC</th></tr></thead><tbody>__CLU__</tbody></table></div>
<div class="key"><b>RSA beats every ΔΔG method on every protein</b> — AUC 0.765&ndash;0.816
against 0.711&ndash;0.791 — and it is the cheapest quantity in the table. Note also that these
AUCs are partly circular for FoldX and Rosetta, which <i>are</i> clustering features; RSA is not,
and still wins.</div>

<h2>7. Against experimental data</h2>
__FIG_DMS__
<div class="scroll" style="max-width:640px"><table><thead><tr><th>method</th><th class="n">n</th>
<th class="n">abundance (stability)</th><th class="n">IFN 100 U (function)</th></tr></thead>
<tbody>__DMS__</tbody></table></div>
<div class="key"><p><b>The conservation-based predictors beat the stability methods at predicting
measured protein abundance.</b> Abundance is close to a direct readout of folding stability —
exactly what ΔΔG computes — and AlphaMissense, which never sees a force field, is 60% better at
it than PyRosetta.</p>
<p><b>RSA alone (0.288) beats both FoldX and Rosetta.</b> Again.</p>
<p>In the methods' defence: these are single-point correlations over a whole multi-domain protein,
the hardest possible setting, and the independent literature ceiling is r ≈ 0.5&ndash;0.6 on
curated single-domain sets. 0.26&ndash;0.30 is poor but not anomalous.</p></div>

<h2>8. Recommendations</h2>
<ol>
<li><b>Do not use <code>ddg_delta</code>.</b> Inert on four proteins; on JAK2 it also fails to
reproduce between two model pairs (r = 0.074).</li>
<li><b>Winsorise Rosetta ΔΔG and drop X&rarr;P values.</b></li>
<li><b>Add RSA as a feature.</b> Free, already present at 100% coverage, and it outperforms all
three ΔΔG methods.</li>
<li><b>Consider replacing Rosetta with ThermoMPNN</b> in the feature set: better AUC, better
agreement with FoldX, no outlier tail, no 1.5 h per protein, 100% coverage. Keep Rosetta for the
dual-state question it was computed for.</li>
<li><b>Try RSALOR properly</b> — the JAK2 output is already on disk.</li>
</ol>

<h2>Literature</h2>
<p>The full survey, with 33 DOIs all resolved against CrossRef and independent assessments tagged,
is <code>external_data/ddg_literature.md</code>. The datasets memo is
<code>external_data/ddg_precomputed.md</code>. Directly relevant here:</p>
<div class="scroll"><table><thead><tr><th>paper</th><th>year</th><th>what it establishes</th>
</tr></thead><tbody>
<tr><td><b>Tsishyn, Pucci &amp; Rooman — RSALOR</b>, <i>Bioinformatics</i><br>
<a href="https://doi.org/10.1093/bioinformatics/btaf322">10.1093/bioinformatics/btaf322</a></td>
<td>2025</td><td><b>RSA &times; evolution beats most deep models on stability.</b> The paper behind section 5</td></tr>
<tr><td>Dieckhaus et al. — ThermoMPNN, <i>PNAS</i><br>
<a href="https://doi.org/10.1073/pnas.2314853121">10.1073/pnas.2314853121</a></td>
<td>2024</td><td>the learned method used here; Ssym direct PCC 0.72, S669 0.43</td></tr>
<tr><td>Akdel et al., <i>Nat. Struct. Mol. Biol.</i><br>
<a href="https://doi.org/10.1038/s41594-022-00849-w">10.1038/s41594-022-00849-w</a></td>
<td>2022</td><td>ΔΔG from AlphaFold models ≈ from experimental structures; homology models degrade below 40% identity</td></tr>
<tr><td>Nielsen, Stein &amp; Lindorff-Larsen, <i>CSBJ</i><br>
<a href="https://doi.org/10.1016/j.csbj.2022.11.048">10.1016/j.csbj.2022.11.048</a></td>
<td>2022</td><td>independently reproduces the 40% threshold; Rosetta <code>cartesian_ddg</code> most robust</td></tr>
<tr><td>Notin et al. — ProteinGym<br>
<a href="https://doi.org/10.1101/2023.12.07.570727">10.1101/2023.12.07.570727</a></td>
<td>2023</td><td>the benchmark RSALOR is measured on; shows split choice moves scores from 0.579 to 0.064</td></tr>
<tr><td>Thiltgen &amp; Goldstein, <i>PLoS ONE</i><br>
<a href="https://doi.org/10.1371/journal.pone.0046084">10.1371/journal.pone.0046084</a></td>
<td>2012</td><td>the antisymmetry statistic δ = ΔΔG<sub>dir</sub> + ΔΔG<sub>inv</sub>, later used by Pucci and Pancotti</td></tr>
<tr><td>Montanucci et al., <i>Bioinformatics</i><br>
<a href="https://doi.org/10.1093/bioinformatics/bty880">10.1093/bioinformatics/bty880</a></td>
<td>2019</td><td>the theoretical ceiling imposed by experimental noise, r ≈ 0.7&ndash;0.8</td></tr>
<tr><td>Li &amp; Luo — SPURS, <i>Nat. Commun.</i><br>
<a href="https://doi.org/10.1038/s41467-025-67609-4">10.1038/s41467-025-67609-4</a></td>
<td>2025</td><td>current state of the art claim; per-dataset values not in retrieved text</td></tr>
</tbody></table></div>

<p class="sub">Full write-up: <code>DDG_METHODS_SURVEY.md</code> &middot; numbers:
<code>ddg_survey.json</code> &middot; per-variant tables: <code>{jak1,jak2,jak3,tyk2}_methods.csv</code>
&middot; part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>

<script>
var CORR=__CORR__, PROTS=__PROTS__;
var tabs=document.getElementById('ctabs'), box=document.getElementById('cbox');
PROTS.forEach(function(p,i){var b=document.createElement('button');
  b.className='tab'+(i===0?' on':'');b.textContent=p;
  b.onclick=function(){[].forEach.call(tabs.children,function(c){c.className='tab'});
    b.className='tab on';box.innerHTML=CORR[p];};
  tabs.appendChild(b);});
box.innerHTML=CORR[PROTS[0]];
</script></div></body></html>"""

out = (HTML
       .replace("__FIG_HIST__", img("histograms", "JAK2: distribution of each ΔΔG-like method. Log y axis, clipped at the 0.5–99.5 percentiles — without clipping the Rosetta panels are unreadable, which is itself the point of section 4."))
       .replace("__FIG_CORR__", img("correlations", "Spearman correlations, every feature oriented so + = more damaging. The same structure appears in all four proteins."))
       .replace("__FIG_OUT__", img("outliers_by_residue", "Fraction of substitutions beyond an extreme threshold, by substituted-in residue. F, P, W, Y in red. Note the y axis: 0–100% for Rosetta, 0–20% for the other two."))
       .replace("__FIG_RSA__", img("rsa_vs_ddg", "RSA against each ΔΔG method, JAK2. Hexbin, log density, clipped at 1–99%."))
       .replace("__FIG_CLU__", img("by_cluster", "AUC for separating the two clusters. Stability methods and RSA in red, sequence predictors in grey."))
       .replace("__FIG_DMS__", img("tyk2_dms", "TYK2 against the Howard 2026 deep mutational scan — the only experimental anchor in the project."))
       .replace("__DHDR__", "".join(f'<th class="n">{s}</th>' for s in STATS))
       .replace("__DESC__", desc_tbl()).replace("__CLU__", cluster_tbl())
       .replace("__DMS__", dms_tbl()).replace("__OUT__", outlier_tbl())
       .replace("__CORR__", json.dumps({p: corr_tbl(p) for p in PROTS}, separators=(",", ":")))
       .replace("__PROTS__", json.dumps(PROTS)))
(H / "ddg_methods_survey.html").write_text(out)
print(f"wrote ddg_methods_survey.html  {len(out)/1e6:.2f} MB")
