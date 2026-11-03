"""Interactive 3D viewer for the five JAK2 models -> jak2_models_3d.html.

Plotly from cdnjs, data inlined as JSON, so the page is one self-contained file.
Backbone Ca traces only: 1,132 residues x 5 models is plenty to see the domain
arrangement, and full atoms would be ~70x the data for no gain at this scale.
"""
import base64, json, os, pathlib, sys

HERE = pathlib.Path(__file__).parent
S = json.load(open(HERE / "model_analysis.json"))
LAB = {m["key"]: m["label"] for m in S["models"]}
TMPL = {m["key"]: m["template"] for m in S["models"]}
PL = {m["key"]: m["plddt"] for m in S["models"]}
DCOL = {"FERM": "#4878d0", "SH2": "#6acc64", "JH2": "#ee854a", "JH1": "#d65f5f", "linker": "#b0b0b0"}

# Panel 2 needs pair1_closed expressed in pair1_open's JH2 frame. Done here with numpy
# rather than in the browser: a hand-rolled Kabsch in JS is exactly the kind of thing that
# silently produces a plausible-looking wrong rotation.
import numpy as np
A, B = S["traces"]["pair1_closed"], S["traces"]["pair1_open"]
bi = {r: i for i, r in enumerate(B["res"])}
lo, hi = S["domains"]["JH2"]
sh = [(i, bi[r]) for i, r in enumerate(A["res"]) if lo <= r <= hi and r in bi]
P = np.array([A["xyz"][i] for i, _ in sh], float)
Q = np.array([B["xyz"][j] for _, j in sh], float)
pm, qm = P.mean(0), Q.mean(0)
V, _, W = np.linalg.svd((P - pm).T @ (Q - qm))
R = V @ np.diag([1, 1, np.sign(np.linalg.det(V @ W))]) @ W
fitted = ((np.array(A["xyz"], float) - pm) @ R + qm)
fit_rmsd = float(np.sqrt((((P - pm) @ R + qm - Q) ** 2).sum(1).mean()))
print(f"panel 2 JH2 fit RMSD {fit_rmsd:.2f} A over {len(sh)} residues")

data = {k: {"res": S["traces"][k]["res"], "xyz": S["traces"][k]["xyz"],
            "plddt": S["traces"][k]["plddt"]} for k in LAB}
data["pair1_closed"]["fitted"] = [[round(float(c), 1) for c in p] for p in fitted]
meta = {k: {"label": LAB[k], "template": TMPL[k], "plddt": PL[k],
            "state": "closed" if S["centroids"][k]["FERM-JH1"] < 60 else "open",
            "fermjh1": S["centroids"][k]["FERM-JH1"],
            "jh2jh1": S["centroids"][k]["JH2-JH1"],
            "shan": S["vs_shan"][k]["jh1_rmsd"]} for k in LAB}

PLOTLY_URL = "https://cdnjs.cloudflare.com/ajax/libs/plotly.js/2.27.0/plotly.min.js"
PLOTLY = HERE / "vendor" / "plotly-2.27.0.min.js"
# The output is ONE self-contained file: Plotly and every figure are inlined. An earlier
# version referenced vendor/plotly-*.js relatively, which broke the moment the html was
# copied anywhere on its own - the common case, since the point of the page is to be shared.
# vendor/ is only a build-time cache and is gitignored.
LINK_VENDOR = "--link-vendor" in sys.argv


def b64img(name, cap):
    f = HERE / "figs" / f"{name}.png"
    if not f.exists():
        return ""
    return (f'<figure><img src="data:image/png;base64,{base64.b64encode(f.read_bytes()).decode()}"'
            f' alt="{cap}"><figcaption>{cap}</figcaption></figure>')


HTML = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>JAK2 Model Viewer</title>
<script src="vendor/plotly-2.27.0.min.js"></script>
<style>
:root{--bg:#fbfaf8;--card:#fff;--fg:#17181a;--fg2:#4a4d52;--mut:#7b7f87;--line:#e3e1dd;
--accent:#1f5fa8;--chip:#f1efeb;color-scheme:light}
@media(prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#121316;--card:#1b1d21;
--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--chip:#24272c;
color-scheme:dark}}
:root[data-theme=dark]{--bg:#121316;--card:#1b1d21;--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;
--line:#2d3036;--accent:#7fb0ef;--chip:#24272c;color-scheme:dark}
*{box-sizing:border-box}body{background:var(--bg);color:var(--fg);margin:0;
font:15px/1.6 "Source Serif 4",Georgia,serif}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));
padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 70px}
h1{font:600 27px/1.2 "Source Sans 3",system-ui,sans-serif;margin:0 0 5px;text-wrap:balance}
h2{font:600 19px "Source Sans 3",system-ui,sans-serif;margin:34px 0 10px;padding-top:13px;
border-top:1px solid var(--line)}
p{color:var(--fg2);max-width:74ch}a{color:var(--accent)}
.sub{color:var(--mut);font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 18px}
.ctl{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:14px 0;
font:13px "Source Sans 3",system-ui,sans-serif}
button{font:600 12.5px "Source Sans 3",system-ui,sans-serif;padding:7px 12px;border-radius:7px;
border:1px solid var(--line);background:var(--card);color:var(--fg);cursor:pointer}
button.on{background:var(--accent);color:#fff;border-color:var(--accent)}
.plot{background:var(--card);border:1px solid var(--line);border-radius:11px;padding:8px;
margin:14px 0;min-width:0}
.cap{font:12.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:8px}
.leg{display:flex;flex-wrap:wrap;gap:12px;font:12px "Source Sans 3",system-ui,sans-serif;
color:var(--mut);margin:8px 2px}
.sw{display:inline-block;width:11px;height:11px;border-radius:3px;margin-right:5px;
vertical-align:-1px}
figure{margin:16px 0;background:var(--card);border:1px solid var(--line);border-radius:11px;
padding:10px;min-width:0}
figure img{display:block;width:100%;height:auto;border-radius:6px;background:#fff}
figcaption{font:12.5px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:9px}
.scroll{overflow-x:auto}table{border-collapse:collapse;width:100%;
font:12.6px "Source Sans 3",system-ui,sans-serif}
th,td{padding:6px 10px;border-bottom:1px solid var(--line);text-align:left}
th{color:var(--mut);font-weight:600}td.n,th.n{text-align:right}
.key{background:var(--card);border:1px solid var(--line);border-left:3px solid var(--accent);
border-radius:0 9px 9px 0;padding:12px 16px;margin:15px 0;font-size:14px}
.key b{color:var(--fg)}
</style></head><body><div class="wrap">
<h1>JAK2 full-length models</h1>
<p class="sub">Five models of O60674, 1,132 residues &middot; C&alpha; backbone &middot;
drag to rotate, scroll to zoom</p>
<p>The open&rarr;closed transition moves <b>JH1 and nothing else</b>: FERM&ndash;SH2&ndash;JH2 is
a rigid body in all five structures, and every per-domain RMSD across these models is
0.10&ndash;0.66&nbsp;&Aring;. Rotate the first panel and the ~50&nbsp;&Aring; swing of the red
JH1 domain is the whole story.</p>

<h2>1. Static views &mdash; these always work</h2>
<p>Rendered with matplotlib and embedded in this file, so they need no network, no WebGL and no
other file beside this one. <b>All panels share one scale</b>, so the compact closed state and
the extended open state are directly comparable; scaling each to its own extent would hide the
very thing these figures exist to show.</p>
__FIG1__
__FIG2__
__FIG3__
__FIG4__

<h2>2. Interactive &mdash; all five models, coloured by domain</h2>
<div class="ctl" id="pick"></div>
<div class="leg" id="leg"></div>
<div class="plot"><div id="g1" style="height:560px"></div></div>

<h2>3. Open against closed, superposed on JH2</h2>
<p>Both models of pair&nbsp;1 fitted on their JH2 domains, so the JH1 displacement is shown in
its own frame. JH1 moves 81.9&nbsp;&Aring; between the two states.</p>
<div class="plot"><div id="g2" style="height:540px"></div></div>

<h2>4. Coloured by pLDDT</h2>
<p>Confidence is high inside domains and collapses in the linkers. For the AlphaFold DB model we
also have PAE, which puts the FERM&ndash;JH1 block at <b>21.0&nbsp;&Aring;</b> against a
31&nbsp;&Aring; ceiling &mdash; the network is confident about each domain and close to
uninformative about where JH1 sits.</p>
<div class="ctl" id="pick3"></div>
<div class="plot"><div id="g3" style="height:540px"></div></div>

<h2>Models</h2>
<div class="scroll"><table><thead><tr><th>model</th><th>template</th><th>state</th>
<th class="n">FERM&ndash;JH1</th><th class="n">JH2&ndash;JH1</th><th class="n">JH1 vs Shan</th>
<th class="n">pLDDT</th></tr></thead><tbody id="tb"></tbody></table></div>
<div class="key"><b>Pair 1 is the recommended dual-state pair</b> &mdash; both states from one
untemplated run, so nothing differs between them but the conformation. Pair 2's open model sits
0.33&nbsp;&Aring; from the AlphaFold DB model it was templated on, so it is a control, not a
second opinion. Full write-up in <code>README.md</code>.</div>
<p class="sub">Part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>

<script>
if(typeof Plotly==='undefined'){
  document.querySelectorAll('.plot').forEach(d=>{d.style.height='auto';
    d.innerHTML='<p style="padding:22px;margin:0;color:var(--mut)">The 3D viewer needs '+
    'Plotly, which did not load. <b>The static views in section 1 and every number below '+
    'are unaffected.</b> This page normally has Plotly inlined, so if you are seeing this '+
    'the file was built with <code>--link-vendor</code> and <code>vendor/</code> is missing.</p>';
    d.querySelectorAll('div[id]').forEach(x=>x.remove())})}
const DATA=__DATA__, META=__META__, DOM=__DOM__, DCOL=__DCOL__;
const dark=()=>document.documentElement.dataset.theme==='dark'||
  (!document.documentElement.dataset.theme&&matchMedia('(prefers-color-scheme: dark)').matches);
const domOf=r=>{for(const d in DOM){if(r>=DOM[d][0]&&r<=DOM[d][1])return d}return 'linker'};
function segs(m){ // split the chain into runs of one domain so each is a separate line
  const d=DATA[m],out=[];let cur=null;
  d.res.forEach((r,i)=>{const dm=domOf(r);
    if(!cur||cur.dm!==dm){cur={dm,x:[],y:[],z:[],t:[]};out.push(cur)}
    cur.x.push(d.xyz[i][0]);cur.y.push(d.xyz[i][1]);cur.z.push(d.xyz[i][2]);
    cur.t.push(`${r} ${dm}`)});
  return out}
const layout=t=>({margin:{l:0,r:0,t:t?28:0,b:0},title:t?{text:t,font:{size:13}}:undefined,
  paper_bgcolor:'rgba(0,0,0,0)',showlegend:false,
  font:{color:dark()?'#b9bdc4':'#4a4d52',family:'Source Sans 3,system-ui,sans-serif',size:10},
  scene:{aspectmode:'data',xaxis:{visible:false},yaxis:{visible:false},zaxis:{visible:false},
    bgcolor:'rgba(0,0,0,0)'}});
const CFG={displayModeBar:false,responsive:true};
// start with pair 1 only: five overlaid models is ~45 WebGL traces and a slow first
// paint. The other three are one click away.
let shown=['pair1_closed','pair1_open'];
function draw1(){
  const tr=[];
  shown.forEach(m=>segs(m).forEach(s=>tr.push({type:'scatter3d',mode:'lines',x:s.x,y:s.y,z:s.z,
    text:s.t,hovertemplate:`<b>${META[m].label}</b><br>%{text}<extra></extra>`,
    line:{color:DCOL[s.dm],width:shown.length>2?2.5:4},
    opacity:shown.length>2?0.75:1})));
  Plotly.react('g1',tr,layout(null),CFG)}
function draw3(m){
  const d=DATA[m];
  Plotly.react('g3',[{type:'scatter3d',mode:'lines',x:d.xyz.map(p=>p[0]),y:d.xyz.map(p=>p[1]),
    z:d.xyz.map(p=>p[2]),line:{width:5,color:d.plddt,colorscale:[[0,'#d65f5f'],[0.5,'#f4e04d'],
    [0.7,'#8ec7e8'],[1,'#2b5fa5']],cmin:50,cmax:100,colorbar:{title:{text:'pLDDT',font:{size:10}},
    thickness:11,len:.6}},text:d.res.map((r,i)=>`${r} ${domOf(r)} pLDDT ${d.plddt[i]}`),
    hovertemplate:'%{text}<extra></extra>'}],layout(META[m].label),CFG)}
// panel 2: pair1 closed (pre-fitted on JH2 in analyse/build, not here) vs open
function fitJH2(){
  const A=DATA.pair1_closed,B=DATA.pair1_open,tr=[];
  [[A.fitted,A.res,'pair1_closed'],[B.xyz,B.res,'pair1_open']].forEach(([xyz,res,m])=>{
    const by={};res.forEach((r,i)=>{const d=domOf(r);(by[d]=by[d]||[]).push(xyz[i])});
    for(const d in by)tr.push({type:'scatter3d',mode:'lines',
      x:by[d].map(p=>p[0]),y:by[d].map(p=>p[1]),z:by[d].map(p=>p[2]),
      line:{color:m==='pair1_closed'?DCOL[d]:'#9aa0a6',width:m==='pair1_closed'?4:2.5},
      opacity:m==='pair1_closed'?1:.55,
      hovertemplate:`<b>${META[m].label}</b><br>${d}<extra></extra>`})});
  Plotly.react('g2',tr,layout('closed in colour, open in grey, both in the JH2 frame'),CFG)}
// controls
const pick=document.getElementById('pick');
Object.keys(DATA).forEach(m=>{const b=document.createElement('button');
  b.textContent=META[m].label;b.className=shown.includes(m)?'on':'';
  b.onclick=()=>{shown=shown.includes(m)?shown.filter(x=>x!==m):[...shown,m];
    b.className=shown.includes(m)?'on':'';draw1()};pick.appendChild(b)});
document.getElementById('leg').innerHTML=Object.entries(DCOL).map(([d,c])=>
  `<span><span class="sw" style="background:${c}"></span>${d}</span>`).join('');
const p3=document.getElementById('pick3');
Object.keys(DATA).forEach((m,i)=>{const b=document.createElement('button');
  b.textContent=META[m].label;b.className=i===0?'on':'';
  b.onclick=()=>{[...p3.children].forEach(c=>c.className='');b.className='on';draw3(m)};
  p3.appendChild(b)});
document.getElementById('tb').innerHTML=Object.keys(META).map(m=>{const v=META[m];
  return `<tr><td>${v.label}</td><td>${v.template}</td><td><b>${v.state}</b></td>
  <td class="n">${v.fermjh1.toFixed(1)}</td><td class="n">${v.jh2jh1.toFixed(1)}</td>
  <td class="n">${v.shan.toFixed(1)}</td><td class="n">${v.plddt.toFixed(1)}</td></tr>`}).join('');
if(typeof Plotly!=='undefined'){draw1();fitJH2();draw3('pair1_closed');}
if(typeof Plotly!=='undefined')matchMedia('(prefers-color-scheme: dark)').addEventListener('change',()=>{
  draw1();fitJH2();draw3(Object.keys(DATA)[[...p3.children].findIndex(c=>c.className==='on')]||'pair1_closed')});
</script></div></body></html>"""

FIGS = {
    "__FIG1__": ("models_overview",
        "The five models, two viewing angles each. Closed is compact, open is extended; "
        "only JH1 (red) changes position."),
    "__FIG2__": ("open_vs_closed",
        "Pair 1: closed in colour, open in grey, both fitted on JH2. JH1 moves 81.9 A."),
    "__FIG3__": ("plddt", "Confidence along the chain: high inside domains, collapsing in the linkers."),
    "__FIG4__": ("metrics",
        "Left: centroid distances - only the three JH1 pairs change. Middle: JH1 RMSD after JH2 fit "
        "between every pair of models. Right: AlphaFold DB PAE, confident within domains and not between."),
}
for tok, (name, cap) in FIGS.items():
    HTML = HTML.replace(tok, b64img(name, cap))

if not LINK_VENDOR:
    if not PLOTLY.exists():
        import urllib.request
        PLOTLY.parent.mkdir(exist_ok=True)
        print(f"fetching {PLOTLY_URL}")
        urllib.request.urlretrieve(PLOTLY_URL, PLOTLY)
    HTML = HTML.replace('<script src="vendor/plotly-2.27.0.min.js"></script>',
                        "<script>" + PLOTLY.read_text() + "</script>")

out = (HTML.replace("__DATA__", json.dumps(data, separators=(",", ":")))
           .replace("__META__", json.dumps(meta, separators=(",", ":")))
           .replace("__DOM__", json.dumps(S["domains"], separators=(",", ":")))
           .replace("__DCOL__", json.dumps(DCOL, separators=(",", ":"))))
(HERE / "jak2_models_3d.html").write_text(out)
print(f"wrote jak2_models_3d.html  {len(out)/1e6:.2f} MB"
      + ("  (links vendor/ - not self-contained)" if LINK_VENDOR
         else "  (self-contained: Plotly and all figures inlined)"))
