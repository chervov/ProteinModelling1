"""Self-contained 3D viewer for the five JAK3 models -> jak3_models_3d.html.

Uses 3Dmol.js with a cartoon trace, matching more_proteins/top10/*.html, which is the
pattern already proven in this project. 3Dmol is inlined (0.5 MB) rather than loaded from a
CDN, so the page works offline and keeps working when copied anywhere on its own. Structures
are inlined as Ca-only PDB with pLDDT in the B-factor column: cartoon style 'trace' needs
nothing more, and full-atom records would be ~8x the bytes for no visible gain.

Earlier versions of this file used Plotly. Replaced because 3Dmol gives a real molecular
cartoon, costs a seventh of the bytes, and is what the rest of the repository already uses.
"""
import base64, json, pathlib, sys, urllib.request

import numpy as np

HERE = pathlib.Path(__file__).parent
S = json.load(open(HERE / "model_analysis.json"))
LIB_URL = "https://cdn.jsdelivr.net/npm/3dmol@2.4.2/build/3Dmol-min.js"
LIB = HERE / "vendor" / "3Dmol-2.4.2-min.js"

DCOL = {"FERM": "#4878d0", "SH2": "#6acc64", "JH2": "#ee854a", "JH1": "#d65f5f"}
DOM = S["domains"]
ORDER = ["af3_closed", "openfold_open", "afdb"]
LAB = {m["key"]: m["label"] for m in S["models"]}
MET = {m["key"]: m for m in S["models"]}
AA3 = "ALA"  # residue name is irrelevant to a trace; keep the records minimal and uniform


def ca_pdb(key, coords=None):
    """Ca-only PDB text, B-factor = pLDDT."""
    t = S["traces"][key]
    xyz = coords if coords is not None else np.array(t["xyz"], float)
    out = []
    for i, (r, p) in enumerate(zip(t["res"], t["plddt"]), 1):
        x, y, z = xyz[i - 1]
        out.append(f"ATOM  {i:5d}  CA  {AA3} A{r:4d}    "
                   f"{x:8.3f}{y:8.3f}{z:8.3f}  1.00{p:6.2f}           C")
    return "\n".join(out)


# pair1_closed expressed in pair1_open's JH2 frame, for the overlay panel.
A, B = S["traces"]["af3_closed"], S["traces"]["openfold_open"]
bi = {r: i for i, r in enumerate(B["res"])}
lo, hi = DOM["JH2"]
sh = [(i, bi[r]) for i, r in enumerate(A["res"]) if lo <= r <= hi and r in bi]
P = np.array([A["xyz"][i] for i, _ in sh], float)
Q = np.array([B["xyz"][j] for _, j in sh], float)
pm, qm = P.mean(0), Q.mean(0)
V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
fitted = (np.array(A["xyz"], float) - pm) @ R + qm
print(f"JH2 fit RMSD {np.sqrt((((P - pm) @ R + qm - Q) ** 2).sum(1).mean()):.2f} A "
      f"over {len(sh)} residues")

MODELS = [{"id": f"v{i}", "key": k, "pdb": ca_pdb(k)} for i, k in enumerate(ORDER)]
OVERLAY = {"closed": ca_pdb("af3_closed", fitted), "open": ca_pdb("openfold_open")}


def b64img(name, cap):
    f = HERE / "figs" / f"{name}.png"
    return "" if not f.exists() else (
        f'<figure><img src="data:image/png;base64,{base64.b64encode(f.read_bytes()).decode()}"'
        f' alt="{cap}"><figcaption>{cap}</figcaption></figure>')


def cards():
    out = []
    for m in MODELS:
        k = m["key"]; c = S["centroids"][k]
        st = "closed" if c["FERM-JH1"] < 60 else "open"
        out.append(f"""<div class="card"><div class="hd"><b>{LAB[k]}</b>
<span class="pill {st}">{st}</span></div>
<div class="v3d" id="{m['id']}"></div>
<div class="btns"><button class="btn on" onclick="setmode('{m['id']}','dom',this)">domain</button>
<button class="btn" onclick="setmode('{m['id']}','plddt',this)">pLDDT</button></div>
<div class="facts">FERM&ndash;JH1 <b>{c['FERM-JH1']:.0f}</b> &middot;
JH2&ndash;JH1 {c['JH2-JH1']:.0f} &middot; JH1 vs Shan {S['vs_shan'][k]['jh1_rmsd']:.1f} &middot;
pLDDT {MET[k]['plddt']:.1f}<br><span class="tmpl">template: {MET[k]['template']}</span></div>
</div>""")
    return "".join(out)


def rows():
    return "".join(
        f"<tr><td>{LAB[k]}</td><td>{MET[k]['template']}</td>"
        f"<td><b>{'closed' if S['centroids'][k]['FERM-JH1'] < 60 else 'open'}</b></td>"
        + "".join(f"<td class='n'>{S['centroids'][k][p]:.1f}</td>" for p in S["domain_pairs"])
        + f"<td class='n'>{S['vs_shan'][k]['jh1_rmsd']:.1f}</td>"
          f"<td class='n'>{MET[k]['plddt']:.1f}</td></tr>" for k in ORDER)


def pair_rows():
    out = []
    for kk, v in S["pairwise"].items():
        a, b = kk.split("|")
        out.append(f"<tr><td>{LAB[a]}</td><td>{LAB[b]}</td><td class='n'>{v['global_rmsd']:.2f}</td>"
                   f"<td class='n'><b>{v['jh1_after_jh2_fit']:.2f}</b></td>"
                   + "".join(f"<td class='n'>{v['per_domain_rmsd'][d]:.2f}</td>"
                             for d in ("FERM", "SH2", "JH2", "JH1")) + "</tr>")
    return "".join(out)


def pae_rows():
    p = S["afdb_pae"]
    ks = ["SH2-SH2", "JH2-JH2", "JH1-JH1", "FERM-FERM", "FERM-SH2", "SH2-JH2", "FERM-JH2",
          "JH2-JH1", "SH2-JH1", "FERM-JH1"]
    return "".join(f"<tr><td>{k}</td><td class='n'>{p[k]:.1f}</td>"
                   f"<td><span class='bar' style='width:{100*p[k]/S['afdb_pae_max']:.0f}%'></span></td>"
                   f"</tr>" for k in ks)


HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK3 Model Viewer</title>
<style>
:root{--bg:#fbfaf8;--card:#fff;--fg:#17181a;--fg2:#4a4d52;--mut:#7b7f87;--line:#e3e1dd;
--accent:#1f5fa8;--chip:#f1efeb;--good:#1a7a3c;--bad:#b02020;color-scheme:light}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#121316;--card:#1b1d21;
--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--chip:#24272c;
--good:#5cc48a;--bad:#ef8e86;color-scheme:dark}}
:root[data-theme=dark]{--bg:#121316;--card:#1b1d21;--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;
--line:#2d3036;--accent:#7fb0ef;--chip:#24272c;--good:#5cc48a;--bad:#ef8e86;color-scheme:dark}
*{box-sizing:border-box}body{background:var(--bg);color:var(--fg);margin:0;
font:15px/1.62 "Source Serif 4",Georgia,serif}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));
padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 72px}
h1{font:600 27px/1.2 "Source Sans 3",system-ui,sans-serif;margin:0 0 5px;text-wrap:balance}
h2{font:600 19px "Source Sans 3",system-ui,sans-serif;margin:36px 0 10px;padding-top:13px;
border-top:1px solid var(--line)}
p,li{color:var(--fg2);max-width:74ch}a{color:var(--accent)}
.sub{color:var(--mut);font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 18px}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(248px,1fr))}
.card{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:11px;
min-width:0}
.hd{font:13.5px "Source Sans 3",system-ui,sans-serif;display:flex;justify-content:space-between;
align-items:center;gap:8px;margin-bottom:7px}
.pill{font:600 10.5px "Source Sans 3",system-ui,sans-serif;padding:2px 7px;border-radius:5px}
.pill.closed{background:rgba(176,32,32,.16);color:var(--bad)}
.pill.open{background:rgba(26,122,60,.16);color:var(--good)}
.v3d{position:relative;width:100%;height:250px;border-radius:7px;background:var(--chip);
overflow:hidden}
.v3d canvas{border-radius:7px}
#big{height:470px}
.btns{display:flex;gap:6px;margin-top:8px}
.btn{font:600 11.5px "Source Sans 3",system-ui,sans-serif;padding:5px 11px;border-radius:6px;
border:1px solid var(--line);background:transparent;color:var(--fg2);cursor:pointer}
.btn.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.facts{font:11.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:8px;
line-height:1.5}
.tmpl{font-size:11px}
.leg{display:flex;flex-wrap:wrap;gap:13px;font:12px "Source Sans 3",system-ui,sans-serif;
color:var(--mut);margin:10px 2px}
.sw{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;
vertical-align:-1px}
figure{margin:16px 0;background:var(--card);border:1px solid var(--line);border-radius:11px;
padding:10px;min-width:0}
figure img{display:block;width:100%;height:auto;border-radius:6px;background:#fff}
figcaption{font:12.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:9px}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;
font:12.6px "Source Sans 3",system-ui,sans-serif}
th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left;white-space:nowrap}
th{color:var(--mut);font-weight:600}td.n,th.n{text-align:right}
.bar{display:inline-block;height:8px;border-radius:4px;background:var(--accent);min-width:2px}
.key{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 9px 9px 0;padding:12px 16px;margin:15px 0;font-size:14px}
.key b{color:var(--fg)}
</style></head><body><div class="wrap">

<h1>JAK3 full-length models</h1>
<p class="sub">Five models of P52333, 1,124 residues &middot; C&alpha; cartoon trace via 3Dmol.js
&middot; drag to rotate, scroll to zoom</p>
<p>Three full-length models. <b>JAK3 has no experimental closed structure</b>, so the reference
here is the AlphaFold&nbsp;DB model, which is itself closed (FERM&ndash;JH1 41.5&nbsp;&Aring;) &mdash;
a weaker anchor than TYK2's 4OLI crystal.</p>
<p><b>The two states are a near-rigid-body motion of JH1.</b> Every per-domain RMSD between the
closed and open models is 0.31&ndash;0.93&nbsp;&Aring;, so unlike TYK2 &mdash; where the FERM domain
alone differed by 5.47&nbsp;&Aring; &mdash; these two structures differ in the arrangement and
almost nothing else.</p>
<p><b>The AlphaFold&nbsp;DB model is closed for JAK3</b>, as for TYK2, and open for JAK2. Two of
three: the default AlphaFold state is not constant across this family.</p>

<h2>1. The five models</h2>
<div class="leg">__LEG__</div>
<div class="grid">__CARDS__</div>

<h2>2. Open against closed, superposed on JH2</h2>
<p>The two AF3 models fitted on their JH2 domains, so JH1's displacement is shown in its own
frame. <b>Closed in colour, open in grey.</b> JH1 moves 82.1&nbsp;&Aring; between the two.</p>
<div class="card"><div class="v3d" id="big"></div>
<div class="btns"><button class="btn on" onclick="ovmode('dom',this)">domain</button>
<button class="btn" onclick="ovmode('plddt',this)">pLDDT</button>
<button class="btn" onclick="ovmode('both',this)">both in colour</button></div></div>

<h2>3. Static views</h2>
<p>The same comparisons as figures, embedded in this file. They need no WebGL, so they survive a
browser or remote session where the viewers above do not. <b>All 3D panels share one scale</b>, so
the compact closed state and the extended open state are directly comparable.</p>
__FIG1__
__FIG2__
__FIG3__
__FIG4__

<h2>4. Domain centroid distances</h2>
<div class="scroll"><table><thead><tr><th>model</th><th>template</th><th>state</th>
__PH__<th class="n">JH1 vs Shan</th><th class="n">pLDDT</th></tr></thead>
<tbody>__ROWS__</tbody></table></div>
<p><b>Only the three JH1 columns change.</b> FERM&ndash;SH2 is 35.7&ndash;35.9 in every model,
SH2&ndash;JH2 39.4&ndash;39.8, FERM&ndash;JH2 47.9&ndash;49.0.</p>

<h2>5. Mutual superposition</h2>
<div class="scroll"><table><thead><tr><th>A</th><th>B</th><th class="n">global RMSD</th>
<th class="n">JH1 after JH2 fit</th><th class="n">FERM</th><th class="n">SH2</th>
<th class="n">JH2</th><th class="n">JH1</th></tr></thead><tbody>__PAIRS__</tbody></table></div>
<div class="key"><p><b>The closed model is the AFDB arrangement.</b> The AF3 no-template model
sits 0.82&nbsp;&Aring; from it after a JH2 fit &mdash; two independent predictions of the same
autoinhibited state. There is no crystal to check either against.</p>
<p><b>The pair is split across two predictors</b> &mdash; AF3 for the closed state, OpenFold for
the open &mdash; so it carries a provenance confound, as TYK2's does. It is milder here: the
per-domain RMSDs stay under 1&nbsp;&Aring;, so the two structures really are related by a motion of
JH1 rather than differing throughout.</p>
<p>Three OpenFold runs produced <i>compact</i> JAK3 models that are <b>15&ndash;16&nbsp;&Aring;
from this arrangement</b> &mdash; collapsed into some other state, not autoinhibited. FERM&ndash;JH1
distance alone would have accepted all of them.</p></div>

<h2>6. AlphaFold DB PAE</h2>
<p>Our OpenFold runs use <code>model_1</code>, which emits no PAE. The AlphaFold&nbsp;DB download
includes it, and it is the most important caveat on this page. PAE at (<i>i</i>,&nbsp;<i>j</i>) is
the error AlphaFold expects in residue <i>j</i>'s position when the prediction is aligned on
residue <i>i</i> &mdash; so the off-diagonal blocks measure confidence in the <b>relative placement
of two domains</b>, which per-residue pLDDT cannot express.</p>
__FIG5__
<div class="scroll" style="max-width:520px"><table><thead><tr><th>block</th>
<th class="n">mean PAE (&Aring;)</th><th>&nbsp;</th></tr></thead><tbody>__PAE__</tbody></table></div>
<div class="key">Within domains AlphaFold is confident (2.4&ndash;5.4&nbsp;&Aring;). Between FERM
and JH1 it is at <b>21.0&nbsp;&Aring;, 68% of the 31&nbsp;&Aring; ceiling</b> &mdash; it has
essentially no idea where JH1 sits. That does not invalidate a dual-state &Delta;&Delta;G, since
&Delta;&Delta;G is local and the domains themselves are confidently modelled, but the
<b>interface</b> residues that generate the difference between states are in the least certain
part of the model.</div>

<p class="sub">Full write-up in <code>README.md</code> &middot; part of
<a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>

<script>__LIB__</script>
<script>
var MODELS=__MODELS__, OVERLAY=__OVERLAY__, DOMS=__DOMS__;
function domcol(p){for(var d in DOMS){if(p>=DOMS[d][0]&&p<=DOMS[d][1])return DOMS[d][2];}
  return '#9aa0a8';}
function plcol(b){return b>=90?'#0053d6':b>=70?'#65cbf3':b>=50?'#ffdb13':'#ff7d45';}
var VW={};
function paint(id,mode){var v=VW[id];if(!v)return;
  v.setStyle({},{cartoon:{style:'trace',thickness:0.75,colorfunc:function(a){
    return mode==='plddt'?plcol(a.b):domcol(a.resi);}}});
  v.render();}
function setmode(id,mode,btn){var g=btn.parentNode.querySelectorAll('.btn');
  for(var i=0;i<g.length;i++)g[i].className='btn';btn.className='btn on';paint(id,mode);}
var OV=null;
function ovpaint(mode){if(!OV)return;
  OV.setStyle({model:0},{cartoon:{style:'trace',thickness:0.85,colorfunc:function(a){
    return mode==='plddt'?plcol(a.b):domcol(a.resi);}}});
  OV.setStyle({model:1},{cartoon:{style:'trace',thickness:0.6,colorfunc:function(a){
    return mode==='plddt'?plcol(a.b):(mode==='both'?domcol(a.resi):'#9aa0a6');}}});
  OV.render();}
function ovmode(mode,btn){var g=btn.parentNode.querySelectorAll('.btn');
  for(var i=0;i<g.length;i++)g[i].className='btn';btn.className='btn on';ovpaint(mode);}
(function(){
  if(typeof $3Dmol==='undefined'){
    document.querySelectorAll('.v3d').forEach(function(e){
      e.innerHTML='<p style="padding:14px;font:12px/1.5 system-ui;color:#888">3Dmol.js did not '+
      'load, so the interactive views are unavailable. The static figures in section 3 and every '+
      'number on this page are unaffected.</p>';});
    return;}
  MODELS.forEach(function(m){var el=document.getElementById(m.id);if(!el)return;
    var v=$3Dmol.createViewer(el,{backgroundAlpha:0});VW[m.id]=v;
    v.addModel(m.pdb,'pdb');paint(m.id,'dom');v.zoomTo();v.render();});
  var el=document.getElementById('big');
  if(el){OV=$3Dmol.createViewer(el,{backgroundAlpha:0});
    OV.addModel(OVERLAY.closed,'pdb');OV.addModel(OVERLAY.open,'pdb');
    ovpaint('dom');OV.zoomTo();OV.render();}
})();
</script></div></body></html>"""

if "--link-lib" in sys.argv:
    lib = f'</script><script src="{LIB_URL}">'
else:
    if not LIB.exists():
        LIB.parent.mkdir(exist_ok=True)
        print(f"fetching {LIB_URL}")
        urllib.request.urlretrieve(LIB_URL, LIB)
    lib = LIB.read_text()

FIGS = {"__FIG1__": ("models_overview",
         "The five models, two viewing angles each. Closed is compact, open extended; only JH1 "
         "(red) changes position."),
        "__FIG2__": ("open_vs_closed",
         "Pair 1: closed in colour, open in grey, both fitted on JH2. JH1 moves 81.9 A."),
        "__FIG3__": ("plddt", "Confidence along the chain: high inside domains, collapsing in the linkers."),
        "__FIG5__": ("pae",
         "Left: the full 1,124 x 1,124 PAE matrix, dark green = confident. The four domains are "
         "boxed; the dashed box is the FERM-JH1 block. Right: mean PAE per block against the "
         "31 A ceiling."),
        "__FIG4__": ("metrics",
         "Left: centroid distances, only the three JH1 pairs change. Middle: JH1 RMSD after JH2 "
         "fit between every pair. Right: AlphaFold DB PAE, confident within domains, not between.")}
for tok, (n, c) in FIGS.items():
    HTML = HTML.replace(tok, b64img(n, c))

out = (HTML
       .replace("__LIB__", lib)
       .replace("__MODELS__", json.dumps(MODELS, separators=(",", ":")))
       .replace("__OVERLAY__", json.dumps(OVERLAY, separators=(",", ":")))
       .replace("__DOMS__", json.dumps({d: [DOM[d][0], DOM[d][1], DCOL[d]] for d in DCOL},
                                       separators=(",", ":")))
       .replace("__LEG__", "".join(f'<span><span class="sw" style="background:{c}"></span>{d}'
                                   f'</span>' for d, c in DCOL.items())
                + '<span><span class="sw" style="background:#9aa0a8"></span>linker</span>')
       .replace("__CARDS__", cards())
       .replace("__PH__", "".join(f'<th class="n">{p}</th>' for p in S["domain_pairs"]))
       .replace("__ROWS__", rows()).replace("__PAIRS__", pair_rows()).replace("__PAE__", pae_rows()))

(HERE / "jak3_models_3d.html").write_text(out)
print(f"wrote jak3_models_3d.html  {len(out)/1e6:.2f} MB"
      + ("  (links 3Dmol from CDN)" if "--link-lib" in sys.argv
         else "  (self-contained: 3Dmol and all figures inlined)"))
