"""Self-contained page for the JAK1 third arrangement. 3Dmol inlined, as elsewhere in the repo."""
import base64, json, pathlib, urllib.request

import numpy as np

HERE = pathlib.Path(__file__).parent
S = json.load(open(HERE / "third_analysis.json"))
LIB_URL = "https://cdn.jsdelivr.net/npm/3dmol@2.4.2/build/3Dmol-min.js"
LIB = HERE / "vendor" / "3Dmol-2.4.2-min.js"
DCOL = {"FERM": "#4878d0", "SH2": "#6acc64", "JH2": "#ee854a", "JH1": "#d65f5f"}
DOM = S["domains"]
ORDER = ["third_a", "third_b", "exp_7t6f", "exp_8ewy", "open", "afdb", "closed"]
GROUP = {"third_a": "third", "third_b": "third", "exp_7t6f": "third",
         "exp_8ewy": "open", "open": "open", "afdb": "open", "closed": "closed"}
L, NOTE = S["labels"], S["note"]
PAIRS = [c for c in S["centroids"]["third_a"] if c != "n_ca"]


def ca_pdb(k):
    t = S["traces"][k]
    return "\n".join(
        f"ATOM  {i:5d}  CA  ALA A{r:4d}    {x:8.3f}{y:8.3f}{z:8.3f}  1.00 50.00           C"
        for i, (r, (x, y, z)) in enumerate(zip(t["res"], t["xyz"]), 1))


MODELS = [{"id": f"v{i}", "key": k, "pdb": ca_pdb(k)} for i, k in enumerate(ORDER)]

# Panel 2 superposes third_a onto each reference on JH2. 3Dmol does NOT fit models, so the
# fitted coordinates are computed here with numpy and inlined - the same fix the JAK2 viewer
# needed. Without it the two chains render side by side and the panel looks like a failure.
def _ca(k):
    t = S["traces"][k]
    return {r: np.array(x, float) for r, x in zip(t["res"], t["xyz"])}

def fitted_pdb(src, ref):
    A, B = _ca(src), _ca(ref)
    f = [r for r in range(*DOM["JH2"]) if r in A and r in B]
    P = np.array([A[r] for r in f]); Q = np.array([B[r] for r in f])
    pm, qm = P.mean(0), Q.mean(0)
    V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
    R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
    rms = float(np.sqrt((((P - pm) @ R + qm - Q) ** 2).sum(1).mean()))
    rs = sorted(A)
    X = (np.array([A[r] for r in rs]) - pm) @ R + qm
    print(f"  panel 2 fit third_a -> {ref}: JH2 RMSD {rms:.2f} A over {len(f)} residues")
    return "\n".join(
        f"ATOM  {i:5d}  CA  ALA A{r:4d}    {x:8.3f}{y:8.3f}{z:8.3f}  1.00 50.00           C"
        for i, (r, (x, y, z)) in enumerate(zip(rs, X), 1))

FITTED = {k: fitted_pdb("third_a", k) for k in ("exp_7t6f", "open", "closed")}

cen = "".join(
    f"<tr class='{'hi' if k.startswith(('third','exp_7')) else ''}'><td>{L[k]}</td>"
    f"<td class='tiny'>{NOTE[k]}</td>"
    + "".join(f"<td class='n{' key' if c=='FERM-JH1' else ''}'>{S['centroids'][k][c]:.1f}</td>"
              for c in PAIRS) + "</tr>" for k in ORDER)

def cell(a, b):
    v = S["jh1_rmsd"][a][b]
    if v is None: return "<td class='n'>&mdash;</td>"
    cls = "m0" if v < 2 else "m1" if v < 12 else "m2" if v < 60 else "m3"
    return f"<td class='n {cls}'>{v:.1f}</td>"
mat = "".join(f"<tr><td class='rh'>{L[a]}</td>" + "".join(cell(a, b) for b in ORDER) + "</tr>"
              for a in ORDER)
mhdr = "<tr><th></th>" + "".join(f"<th class='n'>{L[k].split(' (')[0]}</th>" for k in ORDER) + "</tr>"

HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK1 Third Arrangement</title><style>
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
p,li{color:var(--fg2);max-width:76ch}a{color:var(--accent)}
.sub{color:var(--mut);font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 18px}
.lede{font-size:16.5px;color:var(--fg)}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(230px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:11px;
min-width:0}
.card.third{border-color:var(--accent);border-width:2px}
.card.exp{border-color:var(--good);border-width:2px}
.hd{font:13.5px "Source Sans 3",system-ui,sans-serif;display:flex;justify-content:space-between;
gap:8px;align-items:center;margin-bottom:7px}
.pill{font:600 10px "Source Sans 3",system-ui,sans-serif;padding:2px 7px;border-radius:5px;
background:var(--chip)}
.pill.third{background:rgba(31,95,168,.16);color:var(--accent)}
.pill.open{background:rgba(26,122,60,.16);color:var(--good)}
.pill.closed{background:rgba(176,32,32,.16);color:var(--bad)}
.v3d{position:relative;width:100%;height:215px;border-radius:7px;background:var(--chip);
overflow:hidden}
#big{height:470px}
.facts{font:11.3px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:7px;
line-height:1.5}
.btns{display:flex;gap:6px;margin-top:8px;flex-wrap:wrap}
.btn{font:600 11.5px "Source Sans 3",system-ui,sans-serif;padding:5px 11px;border-radius:6px;
border:1px solid var(--line);background:transparent;color:var(--fg2);cursor:pointer}
.btn.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.leg{display:flex;flex-wrap:wrap;gap:13px;font:12px "Source Sans 3",system-ui,sans-serif;
color:var(--mut);margin:10px 2px}
.sw{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;
vertical-align:-1px}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;
font:12.5px "Source Sans 3",system-ui,sans-serif}
th,td{padding:6px 9px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}
th{color:var(--mut);font-weight:600}td.n,th.n{text-align:right}
tr.hi td{background:var(--hi)}
td.key{font-weight:700}
td.rh{font-weight:600;color:var(--fg)}
td.m0{background:rgba(26,122,60,.30);font-weight:700}
td.m1{background:rgba(26,122,60,.13)}
td.m2{background:rgba(234,179,8,.18)}
td.m3{background:rgba(176,32,32,.13)}
.tiny{font-size:11px;color:var(--mut);white-space:normal}
.key-box{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 9px 9px 0;padding:12px 16px;margin:15px 0;font-size:14px}
.key-box b{color:var(--fg)}
.stat{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px}
.stat .v{font:700 25px "Source Sans 3",system-ui,sans-serif}
.stat .l{font:12px "Source Sans 3",system-ui,sans-serif;color:var(--mut)}
code{font:12.3px ui-monospace,Menlo,monospace;background:var(--chip);padding:1px 5px;
border-radius:4px}
</style></head><body><div class="wrap">

<h1>JAK1: a third domain arrangement, and the experimental structure it matches</h1>
<p class="sub">Neither open nor closed &middot; produced by OpenFold from wild-type JAK1 sequence
with a shallow MSA and no template &middot; C&alpha; cartoon via 3Dmol.js</p>

<p class="lede">OpenFold, given the wild-type JAK1 sequence, a shallow MSA and <b>no template</b>,
produced a JH2&ndash;JH1 arrangement that is neither of the two states the project was looking
for. It turns out to be the arrangement seen in <b>7T6F</b>, the cryo-EM structure of the
<b>active JAK1 dimer</b> &mdash; a real, measured conformation that was not given to the model in
any form.</p>

<div class="grid" style="margin:18px 0">
<div class="stat"><div class="v" style="color:var(--good)">4.9 Å</div>
<div class="l">from 7T6F, the experimental active dimer</div></div>
<div class="stat"><div class="v">47 Å</div><div class="l">from the open state</div></div>
<div class="stat"><div class="v">83 Å</div><div class="l">from the closed state</div></div>
<div class="stat"><div class="v">6 / 7</div><div class="l">structures reaching it, 2 MSA depths</div></div>
</div>

<h2>1. The structures</h2>
<div class="leg">__LEG__</div>
<div class="grid">__CARDS__</div>

<h2>2. The third arrangement against 7T6F, superposed on JH2</h2>
<p>Our model in colour, the experimental cryo-EM structure in grey, both fitted on their JH2
domains so JH1's position is shown in its own frame. They land on top of each other.</p>
<div class="card"><div class="v3d" id="big"></div>
<div class="btns">
<button class="btn on" onclick="ov('exp_7t6f',this)">vs 7T6F (experimental)</button>
<button class="btn" onclick="ov('open',this)">vs open</button>
<button class="btn" onclick="ov('closed',this)">vs closed</button></div></div>

<h2>3. Domain centroid distances</h2>
<p>Å, C&alpha; centroids. Domains FERM 34&ndash;420, SH2 439&ndash;544, JH2 583&ndash;855,
JH1 875&ndash;1153. Rows in the third arrangement are highlighted.</p>
<div class="scroll"><table><thead><tr><th>structure</th><th>what it is</th>
__CHDR__</tr></thead><tbody>__CEN__</tbody></table></div>
<div class="key-box"><b>FERM&ndash;JH1 resolves three bands, not two.</b> Closed sits at
40&nbsp;Å, the third arrangement at <b>84&nbsp;Å</b>, open at 92&ndash;94&nbsp;Å. The third state
is <i>not</i> a slightly-less-open open state: its <b>SH2&ndash;JH1</b> distance is
52&ndash;55&nbsp;Å against 78&nbsp;Å for open &mdash; JH1 has swung to a different place, not
simply moved less far. Note also that <b>JH2&ndash;JH1 cannot tell these apart at all</b>
(44&ndash;48&nbsp;Å for all three non-closed states), which is why the project stopped selecting
structures on it.</div>

<h2>4. The decisive table: JH1 position after superposing JH2</h2>
<p>RMSD in Å. This is the measure that says <i>which</i> arrangement a structure is in, rather
than merely how extended it is. <span class="tiny">green &lt; 2 · pale green &lt; 12 ·
amber &lt; 60 · red &ge; 60</span></p>
<div class="scroll"><table><thead>__MHDR__</thead><tbody>__MAT__</tbody></table></div>
<div class="key-box"><p><b>Read the first row.</b> Our third arrangement is <b>4.9&nbsp;Å</b> from
the experimental 7T6F, <b>47.1&nbsp;Å</b> from open and <b>83.0&nbsp;Å</b> from closed. It is an
order of magnitude closer to a measured structure than to either reference state.</p>
<p><b>And the second cryo-EM structure is a control.</b> <b>8EWY</b>, also a JAK1 dimer, is
<b>6.3&nbsp;Å from open</b> and 48.5&nbsp;Å from 7T6F. So the two experimental JAK1 dimer
structures are themselves in different arrangements, and our models reproduce <i>both</i> — the
third arrangement matches one, our open models match the other. That is strong evidence the
4.9&nbsp;Å is a real correspondence and not an artefact of how the metric is defined.</p>
<p><b>Closed is 80&ndash;84&nbsp;Å from everything else</b>, and the open-family members
(8EWY, ma-a1sai, AFDB) agree with each other to 3.4&ndash;6.3&nbsp;Å. The metric is calibrated:
same-state pairs land under ~6&nbsp;Å, different-state pairs above 45&nbsp;Å. 4.9&nbsp;Å is
same-state.</p></div>

<h2>5. What the arrangement is</h2>
<p>From <a href="JAK1_third.md"><code>JAK1_third.md</code></a>, the original analysis:</p>
<ul>
<li><b>JH1 is rotated ~130&ndash;150°</b> relative to the open state (~100&ndash;120° relative to
closed). It has turned, not just translated.</li>
<li><b>JH1 touches only JH2</b>, through a <b>small interface of its own</b>: JH2 residues ~750
and 798&ndash;807, JH1 residues ~930&ndash;941 and 997. This interface shares almost nothing with
either the open or the closed JH2&ndash;JH1 interface, and <b>does not involve the V658 region</b>
that is central to the closed interface.</li>
<li><b>It is one arrangement, not a scatter.</b> Six of the seven structures sit within
0.7&ndash;9.5&nbsp;Å of one another; the seventh (64/256 seed 4) is 14&ndash;22&nbsp;Å away and is
treated as a variant.</li>
<li><b>The domains are intact.</b> Each domain is within 1.3&nbsp;Å C&alpha; RMSD of the AF2 model
and JH1 pLDDT is 87&ndash;91, as high as in the open and closed models. These are not broken or
low-confidence structures.</li>
</ul>

<h2>6. Where it appears</h2>
<div class="scroll" style="max-width:560px"><table><thead><tr><th>MSA depth</th>
<th>seeds in the third arrangement</th></tr></thead><tbody>
<tr><td>64 / 256</td><td>all 5 (from recycle ~3&ndash;5; seed 4 a variant)</td></tr>
<tr><td>96 / 384</td><td>2 of 5 (seeds 2 and 4, after recycles 4&ndash;7)</td></tr>
<tr><td>128 / 512 and deeper</td><td>none &mdash; open or closed only</td></tr>
</tbody></table></div>
<p>No template, 15 recycles, wild-type sequence. <b>The arrangement appears only at shallow MSA
depth</b> and disappears as the alignment deepens — the deeper MSA pulls the prediction to the
AlphaFold default, which for JAK1 is open.</p>

<h2>7. What this is, and what it is not</h2>
<div class="key-box"><p><b>It is a positive control, not a discovery.</b> 7T6F is a JAK1
structure, so a JAK1 prediction reproducing it shows the pipeline can reach a measured
arrangement from sequence alone. It does not show JAK1 is special, and it does not predict
anything that was not already known experimentally.</p>
<p><b>The active-dimer arrangement is JAK1-only in our runs</b> — 35 hits of 129 for JAK1 against
0, 0 and 2 for JAK2, JAK3 and TYK2. Related: <b>JAK2 never reaches an experimentally
characterised extended state</b> (0 of 237) even though 96 of its structures match extended AF2
JAK2. In the words of the overnight summary, it "goes extended without going anywhere known".</p>
<p><b>A correction underlies all of this.</b> 7T6F and 8EWY are <b>mouse JAK1</b>, not JAK2 —
98.0% identity to JAK1_MOUSE against 43.1% to JAK2. An earlier note in this project had them as
mouse JAK2, citing P52332, which is itself JAK1_MOUSE. The consequence is substantive and still
constrains the rest of the work: <b>there is no experimental multi-domain structure for JAK2,
JAK3 or TYK2 at all</b>, so every closed-state number for those three is measured against a
prediction or against a cross-paralogue JAK1 structure.</p></div>

<h2>Sources and files</h2>
<div class="scroll" style="max-width:720px"><table><thead><tr><th>file</th><th>what</th>
</tr></thead><tbody>
<tr><td><code>JAK1_third.md</code></td><td>the original analysis: contacts, interface residues, caveats</td></tr>
<tr><td><code>analyse.py</code>, <code>analysis.json</code></td><td>the original scripts and results</td></tr>
<tr><td><code>analyse_third.py</code> &rarr; <code>third_analysis.json</code></td><td>the tables on this page</td></tr>
<tr><td><code>structures/</code></td><td>all seven structures, including 7T6F and 8EWY from the PDB</td></tr>
</tbody></table></div>
<p class="sub">7T6F: Glassman et al., <i>Science</i> 2022,
<a href="https://doi.org/10.1126/science.abn8933">10.1126/science.abn8933</a> &middot;
8EWY: Caveney et al., <i>Cell Reports</i> 2023 &middot;
part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>

<script>__LIB__</script>
<script>
var MODELS=__MODELS__, DOMS=__DOMS__, GROUP=__GROUP__, PDB=__PDBMAP__, FITTED=__FITTED__;
function domcol(p){for(var d in DOMS){if(p>=DOMS[d][0]&&p<=DOMS[d][1])return DOMS[d][2];}return '#9aa0a8';}
var VW={};
function paint(v){v.setStyle({},{cartoon:{style:'trace',thickness:0.75,
  colorfunc:function(a){return domcol(a.resi);}}});v.render();}
var OV=null,OVCUR='exp_7t6f';
function ov(which,btn){
  if(btn){var g=btn.parentNode.querySelectorAll('.btn');
    for(var i=0;i<g.length;i++)g[i].className='btn';btn.className='btn on';}
  OVCUR=which; if(!OV)return;
  OV.removeAllModels();
  OV.addModel(FITTED[which],'pdb');   // third_a already fitted onto `which` on JH2
  OV.addModel(PDB[which],'pdb');
  OV.setStyle({model:0},{cartoon:{style:'trace',thickness:0.9,
    colorfunc:function(a){return domcol(a.resi);}}});
  OV.setStyle({model:1},{cartoon:{style:'trace',thickness:0.6,color:'#9aa0a6',opacity:0.75}});
  OV.zoomTo();OV.render();}
(function(){
  if(typeof $3Dmol==='undefined'){
    document.querySelectorAll('.v3d').forEach(function(e){
      e.innerHTML='<p style="padding:14px;font:12px/1.5 system-ui;color:#888">3Dmol.js did not '+
      'load, so the 3D views are unavailable. Every table on this page is unaffected.</p>';});
    return;}
  MODELS.forEach(function(m){var el=document.getElementById(m.id);if(!el)return;
    var v=$3Dmol.createViewer(el,{backgroundAlpha:0});VW[m.id]=v;
    v.addModel(m.pdb,'pdb');paint(v);v.zoomTo();v.render();});
  var el=document.getElementById('big');
  if(el){OV=$3Dmol.createViewer(el,{backgroundAlpha:0});ov('exp_7t6f',null);}
})();
</script></div></body></html>"""

if not LIB.exists():
    LIB.parent.mkdir(exist_ok=True)
    print(f"fetching {LIB_URL}")
    urllib.request.urlretrieve(LIB_URL, LIB)

cards = "".join(
    f"""<div class="card {'third' if k.startswith('third') else 'exp' if k.startswith('exp') else ''}">
<div class="hd"><b>{L[k]}</b><span class="pill {GROUP[k]}">{GROUP[k]}</span></div>
<div class="v3d" id="v{i}"></div>
<div class="facts">{NOTE[k]}<br>FERM&ndash;JH1 <b>{S['centroids'][k]['FERM-JH1']:.0f}</b> &middot;
SH2&ndash;JH1 {S['centroids'][k]['SH2-JH1']:.0f} &middot;
JH1 vs 7T6F <b>{S['jh1_rmsd'][k]['exp_7t6f']:.1f}</b> Å</div></div>"""
    for i, k in enumerate(ORDER))

out = (HTML.replace("__LIB__", LIB.read_text())
       .replace("__MODELS__", json.dumps(MODELS, separators=(",", ":")))
       .replace("__PDBMAP__", json.dumps({m["key"]: m["pdb"] for m in MODELS}, separators=(",", ":")))
       .replace("__FITTED__", json.dumps(FITTED, separators=(",", ":")))
       .replace("__DOMS__", json.dumps({d: [DOM[d][0], DOM[d][1], DCOL[d]] for d in DCOL},
                                       separators=(",", ":")))
       .replace("__GROUP__", json.dumps(GROUP, separators=(",", ":")))
       .replace("__LEG__", "".join(f'<span><span class="sw" style="background:{c}"></span>{d}</span>'
                                   for d, c in DCOL.items()))
       .replace("__CARDS__", cards)
       .replace("__CHDR__", "".join(f'<th class="n">{c}</th>' for c in PAIRS))
       .replace("__CEN__", cen).replace("__MHDR__", mhdr).replace("__MAT__", mat))
(HERE / "jak1_third_structure.html").write_text(out)
print(f"wrote jak1_third_structure.html  {len(out)/1e6:.2f} MB")
