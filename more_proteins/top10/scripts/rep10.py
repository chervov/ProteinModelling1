import json, os, math, html, sys
D = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, D)
J = lambda f: json.load(open(os.path.join(D, f)))

META, STATES, DDG, MF, CL, POCK, SEQS, LIT = (J(f) for f in
    ("meta.json","states.json","ddg.json","mutfeat.json","clusters.json","pockets.json","seqs.json","lit.json"))

AA3 = {"ALA":"A","ARG":"R","ASN":"N","ASP":"D","CYS":"C","GLN":"Q","GLU":"E","GLY":"G","HIS":"H",
       "ILE":"I","LEU":"L","LYS":"K","MET":"M","PHE":"F","PRO":"P","SER":"S","THR":"T","TRP":"W",
       "TYR":"Y","VAL":"V","MSE":"M","SEC":"U"}

def ca(path, chain=None):
    """CA atoms from PDB or minimal mmCIF -> [(num, aa1, x, y, z, bfac)]"""
    p = os.path.join(D, path); out = []
    if path.endswith(".cif"):
        hdr, rows, inloop = [], [], False
        for ln in open(p):
            if ln.startswith("_atom_site."): hdr.append(ln.strip().split(".")[1]); inloop = True; continue
            if inloop:
                if ln.startswith(("#","loop_","_")) or not ln.strip(): 
                    if rows: break
                    continue
                rows.append(ln.split())
        ix = {k: i for i, k in enumerate(hdr)}
        for f in rows:
            if len(f) < len(hdr): continue
            if f[ix["label_atom_id"]].strip('"') != "CA": continue
            if chain and f[ix.get("auth_asym_id", ix["label_asym_id"])] != chain: continue
            try: n = int(f[ix.get("auth_seq_id", ix["label_seq_id"])])
            except Exception: continue
            out.append((n, AA3.get(f[ix["label_comp_id"]], "X"),
                        float(f[ix["Cartn_x"]]), float(f[ix["Cartn_y"]]), float(f[ix["Cartn_z"]]),
                        float(f[ix["B_iso_or_equiv"]]) if f[ix["B_iso_or_equiv"]] not in (".","?") else 0.0))
        return out
    for ln in open(p):
        if not ln.startswith(("ATOM","HETATM")): continue
        if ln[12:16].strip() != "CA": continue
        if chain and ln[21] != chain: continue
        if ln[16] not in " A": continue
        try: n = int(ln[22:26])
        except ValueError: continue
        try: b = float(ln[60:66])
        except ValueError: b = 0.0
        out.append((n, AA3.get(ln[17:20].strip(), "X"), float(ln[30:38]), float(ln[38:46]), float(ln[46:54]), b))
    return out

def offset(atoms, canon):
    """author numbering -> canonical offset, by best sequence identity (same rule as ddg.py)"""
    if not atoms: return 0, 0
    nums = [a[0] for a in atoms]
    def score(off):
        h = n = 0
        for a in atoms[::max(1, len(atoms)//400)]:
            p = a[0] + off
            if 1 <= p <= len(canon): n += 1; h += canon[p-1] == a[1]
        return h, n
    h0, n0 = score(0)
    if n0 and h0 >= 0.8*n0: return 0, round(100*h0/max(n0,1))
    best = (0, -1, 1)
    for off in range(-max(nums)-5, len(canon)+5):
        h, n = score(off)
        if h > best[1]: best = (off, h, max(n,1))
    return best[0], round(100*best[1]/best[2])

def capdb(atoms, off):
    """CA-only PDB in canonical numbering; B-factor carries pLDDT/B"""
    L = []
    for i, (n, aa, x, y, z, b) in enumerate(atoms, 1):
        r = {v: k for k, v in AA3.items()}.get(aa, "GLY")
        L.append("ATOM  %5d  CA  %3s A%4d    %8.3f%8.3f%8.3f  1.00%6.2f           C" %
                 (i, r, n+off, x, y, z, min(b, 999)))
    L.append("END")
    return "\n".join(L)

def paegrid(acc, nb=200):
    f = os.path.join(D, "pae", acc + ".json")
    if not os.path.exists(f): return None
    d = json.load(open(f))
    m = (d[0] if isinstance(d, list) else d)["predicted_aligned_error"]
    n = len(m); nb = min(nb, n); edges = [round(i*n/nb) for i in range(nb+1)]
    g = []
    for i in range(nb):
        row = []
        for j in range(nb):
            s = c = 0
            for a in range(edges[i], max(edges[i]+1, edges[i+1])):
                ra = m[a]
                for b in range(edges[j], max(edges[j]+1, edges[j+1])):
                    s += ra[b]; c += 1
            row.append(round(s/max(c,1), 1))
        g.append(row)
    return {"n": n, "nb": nb, "g": g}

DCOL = ["#2563eb","#c2410c","#047857","#7c3aed","#b91c1c","#0e7490","#a16207","#be185d","#4d7c0f","#1e3a8a"]

def domof(pos, doms):
    for i,(nm,a,b) in enumerate(doms):
        if a <= pos <= b: return i, nm
    return -1, "linker/other"

def esc(s): return html.escape(str(s if s is not None else ""))
def fnum(v, nd=2, dash="&ndash;"):
    if v is None: return dash
    try: return f"{float(v):.{nd}f}"
    except Exception: return esc(v)

# ---------- per-mutation mechanism ----------
def num(v):
    """ddG cells may hold a status string (e.g. wt_mismatch) instead of a number"""
    return v if isinstance(v, (int, float)) else None

def stat(v):
    return v if isinstance(v, str) else None

def mechanism(r, dd, iface, pk, doms):
    """assembled from the computations, not from the literature"""
    pos = r["pos"]; cl = num(dd.get("closed")); op = num(dd.get("open"))
    miss = [k for k in ("closed","open") if stat(dd.get(k))]
    fl = dd.get("flag", {}) or {}
    bits = []; tag = []
    unusable = any(fl.get(k) == "clash" for k in ("closed","open"))
    if miss:
        bits.append("the wild-type residue is absent or different at this position in the <b>" +
                    "/".join(miss) + "</b> structure, so only the other state could be computed (<code>" +
                    esc(stat(dd.get(miss[0]))) + "</code>)")
        tag.append("one state only")
    if cl is not None and op is not None and not unusable:
        diff = cl - op
        if cl > 1.0 and diff > 2.0:
            bits.append(f"destabilises the <b>closed</b> state selectively (&Delta;&Delta;G closed {cl:+.2f} vs open {op:+.2f} REU, &Delta; {diff:+.2f})")
            tag.append("shifts toward OPEN")
        elif op > 1.0 and diff < -2.0:
            bits.append(f"destabilises the <b>open</b> state selectively (open {op:+.2f} vs closed {cl:+.2f} REU)")
            tag.append("shifts toward CLOSED")
        elif cl > 2.0 and op > 2.0:
            bits.append(f"destabilises <b>both</b> states ({cl:+.2f} / {op:+.2f} REU) &mdash; a folding/stability lesion rather than a conformational switch")
            tag.append("destabilising, both states")
        elif abs(cl) < 1.5 and abs(op) < 1.5:
            bits.append(f"energetically near-neutral in both states ({cl:+.2f} / {op:+.2f} REU)")
            tag.append("ΔΔG-neutral")
        else:
            bits.append(f"&Delta;&Delta;G closed {cl:+.2f}, open {op:+.2f} REU")
    elif unusable:
        bits.append(f"&Delta;&Delta;G repulsion-dominated (closed {fnum(cl)}, open {fnum(op)} REU) &mdash; <b>not usable as a free energy</b>, see caveats")
        tag.append("ΔΔG unusable")
    if r.get("in_iface"):
        bits.append("sits <b>in the inter-domain interface</b> of the moving pair, so the substitution acts directly on the contact that defines closed vs open")
        tag.append("interface")
    pock = r.get("pockets") or []
    if pock:
        bits.append("lies in high-confidence predicted pocket" + ("s " if len(pock)>1 else " ") +
                    ", ".join("#"+str(p) for p in pock) + " &mdash; a ligand/drug-binding cavity, so the likely consequence is altered small-molecule binding rather than altered domain arrangement")
        tag.append("pocket")
    ra = r.get("rasa")
    if ra is not None:
        bits.append(f"relative solvent accessibility {ra:.2f} ({'buried' if ra < 0.15 else 'partly buried' if ra < 0.4 else 'exposed'})")
    pl = r.get("plddt_af")
    if pl is not None and pl < 70:
        bits.append(f"local pLDDT {pl:.1f} &mdash; the model is unreliable here, so every structure-based number for this site is weak")
        tag.append("low pLDDT")
    if not tag: tag = ["no clear structural mechanism"]
    return "; ".join(bits) + ".", tag

# ---------- page ----------
HEAD = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1">\n')

CSS = """
<style>
:root{--bg:#fbfaf8;--card:#fff;--fg:#17181a;--fg2:#4a4d52;--mut:#7b7f87;--line:#e2e0dc;--accent:#1f5fa8;--accent2:#b24a0e;--good:#107a46;--bad:#b3261e;--warn:#8a5a00;--chip:#f1efeb;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]){--bg:#121316;--card:#1b1d21;--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--accent2:#f0a16a;--good:#5cc48a;--bad:#ef8e86;--warn:#d9ad52;--chip:#24272c;color-scheme:dark}}
:root[data-theme="dark"]{--bg:#121316;--card:#1b1d21;--fg:#eceef1;--fg2:#b9bdc4;--mut:#878c95;--line:#2d3036;--accent:#7fb0ef;--accent2:#f0a16a;--good:#5cc48a;--bad:#ef8e86;--warn:#d9ad52;--chip:#24272c;color-scheme:dark}
*{box-sizing:border-box}
body{background:var(--bg);color:var(--fg);font:15px/1.6 "Source Serif 4",Georgia,serif;margin:0}
.wrap{max-width:1180px;margin:0 auto;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px));padding-block:28px 72px}
h1{font:600 30px/1.2 "Source Sans 3",system-ui,sans-serif;margin:0 0 4px;text-wrap:balance}
h2{font:600 20px/1.3 "Source Sans 3",system-ui,sans-serif;margin:40px 0 10px;padding-top:14px;border-top:1px solid var(--line);text-wrap:balance}
h3{font:600 15px/1.3 "Source Sans 3",system-ui,sans-serif;margin:22px 0 6px;color:var(--fg2)}
p,li{color:var(--fg2);max-width:76ch}
a{color:var(--accent)}
.sub{color:var(--mut);font:13px/1.5 "Source Sans 3",system-ui,sans-serif;margin:0 0 18px}
.lede{font-size:16px;color:var(--fg)}
code,.mono{font:12.5px/1.5 ui-monospace,"SF Mono",Menlo,monospace}
.card{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin:14px 0}
.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
table{border-collapse:collapse;font:12.5px/1.45 "Source Sans 3",system-ui,sans-serif;min-width:0}
th,td{padding:5px 9px;text-align:right;border-bottom:1px solid var(--line);white-space:nowrap}
th{font-weight:600;color:var(--mut);text-align:right;position:sticky;top:0;background:var(--card)}
td:first-child,th:first-child{text-align:left}
tbody tr:hover{background:var(--chip)}
.chip{display:inline-block;font:600 10.5px/1 "Source Sans 3",system-ui,sans-serif;padding:4px 7px;border-radius:5px;background:var(--chip);color:var(--fg2);margin:1px 2px 1px 0;text-transform:uppercase;letter-spacing:.04em;vertical-align:middle}
.c-gof{background:#fde8d8;color:#8a3b06}.c-lof{background:#dbe7fa;color:#17457f}.c-res{background:#f5dcf0;color:#7a1764}
.c-path{background:#fadddb;color:#8f1d16}.c-ben{background:#dcf0e2;color:#0c5c34}.c-vus{background:#eceaf6;color:#443a74}.c-prot{background:#e2f2f6;color:#0b5467}
@media (prefers-color-scheme:dark){:root:not([data-theme="light"]) .c-gof{background:#4a2a10;color:#f3b183}:root:not([data-theme="light"]) .c-lof{background:#14294a;color:#9dc2f2}:root:not([data-theme="light"]) .c-res{background:#3d1434;color:#e6a3d7}:root:not([data-theme="light"]) .c-path{background:#471713;color:#f2a39d}:root:not([data-theme="light"]) .c-ben{background:#123a24;color:#8bd6a6}:root:not([data-theme="light"]) .c-vus{background:#262142;color:#b7aee6}:root:not([data-theme="light"]) .c-prot{background:#0e3b45;color:#8fd0de}}
:root[data-theme="dark"] .c-gof{background:#4a2a10;color:#f3b183}:root[data-theme="dark"] .c-lof{background:#14294a;color:#9dc2f2}:root[data-theme="dark"] .c-res{background:#3d1434;color:#e6a3d7}:root[data-theme="dark"] .c-path{background:#471713;color:#f2a39d}:root[data-theme="dark"] .c-ben{background:#123a24;color:#8bd6a6}:root[data-theme="dark"] .c-vus{background:#262142;color:#b7aee6}:root[data-theme="dark"] .c-prot{background:#0e3b45;color:#8fd0de}
.pos{color:var(--bad)}.neg{color:var(--good)}
.dombar{display:flex;height:26px;border-radius:5px;overflow:hidden;border:1px solid var(--line);margin:8px 0 4px;font:600 10px/26px "Source Sans 3",system-ui,sans-serif;color:#fff;text-align:center}
.grid{display:grid;gap:14px;grid-template-columns:repeat(auto-fit,minmax(330px,1fr))}
.grid>*{min-width:0}
.v3d{position:relative;width:100%;aspect-ratio:1/0.82;max-width:100%;border:1px solid var(--line);border-radius:8px;overflow:hidden;background:var(--bg)}
.vhead{display:flex;flex-wrap:wrap;gap:6px;align-items:baseline;justify-content:space-between;margin-bottom:5px}
.vttl{font:600 13px "Source Sans 3",system-ui,sans-serif;color:var(--fg)}
.btn{font:600 11px "Source Sans 3",system-ui,sans-serif;padding:4px 9px;border:1px solid var(--line);background:var(--card);color:var(--fg2);border-radius:5px;cursor:pointer}
.btn[aria-pressed="true"]{background:var(--accent);color:#fff;border-color:var(--accent)}
.leg{font:11px "Source Sans 3",system-ui,sans-serif;color:var(--mut);margin-top:5px;display:flex;flex-wrap:wrap;gap:4px 12px}
.sw{display:inline-block;width:9px;height:9px;border-radius:2px;margin-right:4px;vertical-align:-1px}
.note{border-left:3px solid var(--warn);background:var(--chip);padding:10px 14px;border-radius:0 7px 7px 0;margin:14px 0;font-size:13.5px}
.note b{color:var(--fg)}
.note.ok{border-left-color:var(--good)}
.refs li{margin-bottom:9px;font-size:13.5px}
.mech{margin:10px 0;padding:11px 14px;border:1px solid var(--line);border-radius:8px;background:var(--card);font-size:13.5px}
.mech .m-h{font:600 13.5px "Source Sans 3",system-ui,sans-serif;color:var(--fg)}
svg{max-width:100%;height:auto;display:block}
.tiny{font-size:12px;color:var(--mut)}
.nav{font:13px "Source Sans 3",system-ui,sans-serif;margin:0 0 20px}
.nav a{margin-right:14px;white-space:nowrap}
</style>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Source+Sans+3:wght@400;600&family=Source+Serif+4:opsz,wght@8..60,400;8..60,600&display=swap">
<script src="https://cdn.jsdelivr.net/npm/3dmol@2.4.2/build/3Dmol-min.js"></script>
"""

LBL = {"GOF":"c-gof","LOF":"c-lof","resistance":"c-res","pathogenic":"c-path","benign":"c-ben","VUS":"c-vus","protective":"c-prot"}

def build(acc):
    m = META[acc]; gene = m["gene"]; doms = m["domains"]; L = m["length"]
    st = STATES.get(acc, {}); dd = (DDG.get(acc) or {}).get("ddg", {}) or {}
    rows = (MF.get(acc) or {}).get("rows", []); cl = CL.get(acc, {})
    canon = SEQS[acc]; pk = POCK.get(acc, [])
    iface = set(st.get("iface") or [])
    hi = [p for p in pk if float(p["score"]) >= 800]
    o = []
    A = o.append

    # ---- structures: coordinates + numbering offsets
    models = []
    for s in m["structures"]:
        at = ca(s["file"], s.get("chain"))
        if not at: continue
        off, idp = offset(at, canon)
        g = next((x for x in m["geom_all"] if x["label"] == s["label"]), None)
        bmax = max(a[5] for a in at)
        # SWISS-MODEL writes per-residue QMEANDisCo (0-1) into the B column, AlphaFold writes
        # pLDDT (0-100), experimental files write a real B-factor. Rescale the first so that the
        # colour ramp and the median column mean the same thing in every panel.
        bsc = 100.0 if bmax <= 1.5 else 1.0
        blab = ("QMEANDisCo x100" if bsc != 1.0 else
                "pLDDT" if s["kind"] == "prediction" else "B-factor")
        if bsc != 1.0: at = [(a[0], a[1], a[2], a[3], a[4], a[5]*bsc) for a in at]
        models.append({"label": s["label"], "kind": s["kind"], "src": s.get("src"),
                       "identity": s.get("identity"), "pdb": capdb(at, off), "off": off,
                       "idp": idp, "nres": len(at), "blab": blab,
                       "plddt": round((g or {}).get("plddt_med", 0)*bsc, 1) if (g or {}).get("plddt_med") is not None else None,
                       "lo": min(a[0]+off for a in at), "hi": max(a[0]+off for a in at)})
    stl = {s["label"]: s for s in m["structures"]}
    cls_lbl = (st.get("closed") or {}).get("label"); opn_lbl = (st.get("open") or {}).get("label")

    A(HEAD + f"<title>{gene} conformational report</title>" + CSS + "</head>\n<body>")
    A('<div class="wrap">')
    A(f"<h1>{gene} &mdash; {esc(m['name'])}</h1>")
    A(f'<p class="sub">UniProt <a href="https://www.uniprot.org/uniprotkb/{acc}">{acc}</a> &middot; {L} aa &middot; '
      f'{len(doms)} annotated domains &middot; {len(models)} structures analysed &middot; '
      f'{len(rows)} literature mutations &middot; generated 2026-10-29</p>')
    A('<p class="nav">' + " ".join(f'<a href="#{i}">{t}</a>' for i, t in [
        ("s1","1. Structures"),("s2","2. All-pairs domain geometry"),("s3","3. PAE"),
        ("s4","4. Templates &amp; homologs"),("s5","5. Clustering &amp; gnomAD"),
        ("s6","6. Mutations"),("s7","7. pLDDT at mutated sites"),("s8","8. Mechanisms"),
        ("s9","9. Literature"),("s10","10. Caveats")]) + "</p>")
    A(f'<p class="lede">{esc(m["why"])}</p>')

    # domain bar
    A('<div class="dombar">')
    cur = 1
    for i,(nm,a,b) in enumerate(doms):
        if a > cur: A(f'<div style="flex:{a-cur};background:var(--line)"></div>')
        A(f'<div style="flex:{b-a+1};background:{DCOL[i%10]}" title="{esc(nm)} {a}-{b}">{esc(nm) if b-a>60 else ""}</div>')
        cur = b+1
    if cur <= L: A(f'<div style="flex:{L-cur+1};background:var(--line)"></div>')
    A('</div><div class="leg">' + "".join(
        f'<span><span class="sw" style="background:{DCOL[i%10]}"></span>{esc(nm)} {a}&ndash;{b}</span>'
        for i,(nm,a,b) in enumerate(doms)) + '<span><span class="sw" style="background:var(--line)"></span>linker / disordered</span></div>')

    # ===== 1. structures
    A('<h2 id="s1">1. Structures and 3D views</h2>')
    A('<p>Every structure is drawn twice: coloured by <b>domain</b> and coloured by <b>pLDDT</b> '
      '(AlphaFold), QMEANDisCo rescaled to the same 0&ndash;100 range (SWISS-MODEL), or crystallographic '
      'B-factor (experimental, where the colour is <i>not</i> a confidence &mdash; the Measure column says which). '
      'All coordinates are C&alpha; traces renumbered into canonical UniProt positions; '
      'the sequence-identity column reports how well that renumbering reproduces the canonical sequence.</p>')
    A('<div class="scroll"><table><thead><tr><th>Structure</th><th>Type</th><th>Source</th>'
      '<th>Template id %</th><th>Cα</th><th>Range</th><th>Offset</th><th>Numbering id %</th><th>Median confidence / B</th><th>Measure</th><th>Role</th></tr></thead><tbody>')
    for s in models:
        role = []
        if s["label"] == cls_lbl: role.append("<b>CLOSED</b>")
        if s["label"] == opn_lbl: role.append("<b>OPEN</b>")
        A(f'<tr><td>{esc(s["label"])}</td><td>{esc(s["kind"])}</td><td>{esc(s["src"])}</td>'
          f'<td>{fnum(s["identity"],1)}</td><td>{s["nres"]}</td><td>{s["lo"]}&ndash;{s["hi"]}</td>'
          f'<td>{s["off"]:+d}</td><td>{s["idp"]}</td><td>{fnum(s["plddt"],1)}</td><td>{" / ".join(role) or "&ndash;"}</td></tr>')
    A('</tbody></table></div>')
    A('<div class="grid">')
    for i, s in enumerate(models):
        vid = f"v{i}"
        A(f'<div><div class="vhead"><span class="vttl">{esc(s["label"])}</span>'
          f'<span><button class="btn" aria-pressed="true" onclick="setmode(\'{vid}\',\'dom\',this)">domains</button> '
          f'<button class="btn" aria-pressed="false" onclick="setmode(\'{vid}\',\'plddt\',this)">pLDDT</button></span></div>'
          f'<div class="v3d" id="{vid}"></div></div>')
    A('</div>')
    A('<div class="leg">pLDDT scale: '
      '<span><span class="sw" style="background:#0053d6"></span>&ge;90 very high</span>'
      '<span><span class="sw" style="background:#65cbf3"></span>70&ndash;90 confident</span>'
      '<span><span class="sw" style="background:#ffdb13"></span>50&ndash;70 low</span>'
      '<span><span class="sw" style="background:#ff7d45"></span>&lt;50 very low</span></div>')

    # ===== 2. all-pairs geometry
    A('<h2 id="s2">2. Inter-domain geometry &mdash; all domain pairs, every structure</h2>')
    pairs = sorted({p for g in m["geom_all"] for p in g["pairs"]})
    A(f'<p>All {len(pairs)} ordered domain pairs are reported for each of the {len(models)} structures, '
      'so that a pair which does not move is as visible as one that does. '
      '<b>Centroid distance</b> (&Aring;) is the C&alpha; centroid separation; it is rotation-blind. '
      '<b>Contacts</b> counts residue pairs with any C&alpha; within 10&nbsp;&Aring; across the two domains; '
      'it has no geometric failure mode and is the measure used to call open vs closed. '
      '<b>Coverage</b> is the percentage of each domain actually present in the model &mdash; a pair with low coverage '
      'gives a distance that cannot be compared with the full-length one.</p>')
    for what, key, nd in (("Centroid distance (&Aring;)","dist",1), ("Inter-domain contacts (C&alpha; &lt; 10&nbsp;&Aring;)","contacts",0)):
        A(f'<h3>{what}</h3><div class="scroll"><table><thead><tr><th>Domain pair</th>' +
          "".join(f'<th>{esc(s["label"][:30])}</th>' for s in m["geom_all"]) + '</tr></thead><tbody>')
        for p in pairs:
            tds = []
            for g in m["geom_all"]:
                v = g["pairs"].get(p)
                if not v: tds.append("<td>&ndash;</td>"); continue
                cov = v.get("cov") or [100,100]
                lo = min(cov) < 70
                tds.append(f'<td{" style=\"color:var(--mut)\"" if lo else ""} title="coverage {cov[0]}%/{cov[1]}%">'
                           f'{fnum(v[key],nd)}{"*" if lo else ""}</td>')
            A(f'<tr><td>{esc(p).replace("|"," &harr; ")}</td>' + "".join(tds) + "</tr>")
        A('</tbody></table></div>')
    A('<p class="tiny">* at least one domain is under 70% present in that model; the value is not comparable with the full-length structures.</p>')

    A('<h3>How much each pair moves across the structure set</h3>')
    mv = sorted(m["movement"].items(), key=lambda kv: -kv[1]["spread"])
    A('<div class="scroll"><table><thead><tr><th>Domain pair</th><th>n models</th><th>min dist</th><th>max dist</th>'
      '<th>spread (&Aring;)</th><th>min contacts</th><th>max contacts</th><th>closest in</th><th>furthest in</th></tr></thead><tbody>')
    for p, v in mv:
        A(f'<tr><td>{esc(p).replace("|"," &harr; ")}</td><td>{v["n"]}</td><td>{fnum(v["dmin"],1)}</td>'
          f'<td>{fnum(v["dmax"],1)}</td><td><b>{fnum(v["spread"],1)}</b></td><td>{v["cmin"]}</td><td>{v["cmax"]}</td>'
          f'<td>{esc(v["at_min"])}</td><td>{esc(v["at_max"])}</td></tr>')
    A('</tbody></table></div>')
    if st.get("pair"):
        A(f'<div class="note ok">The pair carried forward as the <b>open/closed axis</b> is '
          f'<b>{esc(st["pair"]).replace("|"," &harr; ")}</b>: closed = {esc(cls_lbl)} '
          f'({st["closed"]["contacts"]} contacts, {fnum(st["closed"]["dist"],1)}&nbsp;&Aring;), '
          f'open = {esc(opn_lbl)} ({st["open"]["contacts"]} contacts, {fnum(st["open"]["dist"],1)}&nbsp;&Aring;). '
          f'{len(iface)} residues form the interface in the closed state.</div>')

    # ===== 3. PAE
    A('<h2 id="s3">3. Predicted aligned error</h2>')
    pg = paegrid(acc)
    if pg:
        A(f'<p>AlphaFold v6 PAE for all {pg["n"]} residues, block-averaged to a {pg["nb"]}&times;{pg["nb"]} grid. '
          'Dark blocks on the diagonal are confidently placed units; a bright off-diagonal block means the two units\' '
          'relative position is not predicted. <b>A bright off-diagonal block does not distinguish a two-state switch '
          'from a floppy linker</b> &mdash; that is why the geometry above, not the PAE, decides open vs closed.</p>')
        A(f'<div class="card"><canvas id="pae" width="{pg["nb"]}" height="{pg["nb"]}" '
          'style="width:100%;max-width:560px;image-rendering:pixelated;border-radius:6px"></canvas>'
          '<div class="leg"><span>0 &Aring;</span>'
          '<span style="flex:1;min-width:120px;height:9px;border-radius:2px;background:linear-gradient(90deg,#0b2d6b,#2f7bbf,#9ec9e6,#f2f2f2)"></span>'
          '<span>30+ &Aring;</span></div>')
        A('<div class="leg">' + "".join(
            f'<span><span class="sw" style="background:{DCOL[i%10]}"></span>{esc(nm)}</span>' for i,(nm,a,b) in enumerate(doms)) + '</div></div>')
    else:
        A('<p>No PAE file available for this accession.</p>')

    # ===== 4. templates
    A('<h2 id="s4">4. Templates and homologs</h2>')
    exp = [s for s in m["structures"] if s["kind"] == "experimental"]
    sm  = [s for s in m["structures"] if s["kind"] == "swissmodel"]
    pred= [s for s in m["structures"] if s["kind"] not in ("experimental","swissmodel")]
    A(f'<p>{len(exp)} experimental structures of {gene} itself, {len(sm)} SWISS-MODEL models built on homologous '
      f'templates, {len(pred)} predicted models. For every one of them the all-pairs geometry is in section 2 &mdash; '
      'the homolog templates are the only independent evidence that a domain pair can occupy more than one arrangement, '
      'because a single predictor returns a single answer.</p>')
    for ttl, lst in (("Experimental structures of this protein", exp), ("SWISS-MODEL models on homologous templates", sm), ("Predicted models", pred)):
        if not lst: continue
        A(f'<h3>{ttl}</h3><div class="scroll"><table><thead><tr><th>Model</th><th>Source</th><th>Identity to target</th>'
          '<th>Domains spanned</th><th>Largest-moving pair: dist</th><th>contacts</th></tr></thead><tbody>')
        big = max(m["movement"], key=lambda k: m["movement"][k]["spread"]) if m["movement"] else None
        for s in lst:
            g = next((x for x in m["geom_all"] if x["label"] == s["label"]), None)
            v = (g or {}).get("pairs", {}).get(big) if big else None
            nd = len({d for p in (g or {}).get("pairs", {}) for d in p.split("|")}) if g else 0
            A(f'<tr><td>{esc(s["label"])}</td><td>{esc(s.get("src"))}</td><td>{fnum(s.get("identity"),1)}</td>'
              f'<td>{nd}</td><td>{fnum((v or {}).get("dist"),1)}</td><td>{fnum((v or {}).get("contacts"),0)}</td></tr>')
        A('</tbody></table></div>')
        if big: A(f'<p class="tiny">Largest-moving pair here = {esc(big).replace("|"," &harr; ")}.</p>')

    # ===== 5. clustering
    A('<h2 id="s5">5. Two-cluster split of all possible missense variants, and gnomAD enrichment</h2>')
    if cl.get("rich"):
        for tag, cc in (("rich", cl["rich"]), ("full", cl.get("full"))):
            if not cc: continue
            ttl = (f'Variants with the full predictor panel ({cc["n"]:,} of ~{19*L:,} possible)' if tag=="rich"
                   else f'All variants with the always-available predictors ({cc["n"]:,})')
            A(f'<h3>{ttl}</h3>')
            A(f'<p class="tiny">k-means, k=2, on {len(cc["keys"])} z-scored features, each oriented so that larger = more damaging: '
              + ", ".join(esc(k) for k in cc["keys"]) + ".</p>")
            dam = 1 if cc["means"]["1"].get("AlphaMissense", 0) >= cc["means"]["0"].get("AlphaMissense", 0) else 0
            ben = 1 - dam
            A('<div class="scroll"><table><thead><tr><th>Feature</th>'
              f'<th>cluster {ben} &mdash; tolerant (n={cc["sizes"][ben]:,})</th>'
              f'<th>cluster {dam} &mdash; damaging (n={cc["sizes"][dam]:,})</th></tr></thead><tbody>')
            for k in cc["keys"]:
                A(f'<tr><td>{esc(k)}</td><td>{fnum(cc["means"][str(ben)].get(k),3)}</td><td>{fnum(cc["means"][str(dam)].get(k),3)}</td></tr>')
            gf = cc.get("gnomad_frac"); gn = cc.get("gnomad_n")
            if gf:
                A(f'<tr><td><b>observed in gnomAD r4</b></td>'
                  f'<td><b>{100*gf[ben]:.1f}%</b> ({gn[ben]:,})</td><td><b>{100*gf[dam]:.1f}%</b> ({gn[dam]:,})</td></tr>')
            A('</tbody></table></div>')
            if gf and gf[dam] > 0:
                r = gf[ben]/gf[dam]
                w, bw = 460, 150
                A(f'<div class="card"><svg viewBox="0 0 {w} 150" style="max-width:520px" role="img" aria-label="gnomAD observation rate by cluster">')
                mx = max(gf)*1.25 or 1
                for i,(ci,col,nmc) in enumerate(((ben,"var(--good)","tolerant"),(dam,"var(--bad)","damaging"))):
                    h = 86*gf[ci]/mx; y = 110-h
                    A(f'<rect x="{70+i*180}" y="{y:.1f}" width="{bw}" height="{h:.1f}" rx="4" fill="{col}"/>')
                    A(f'<text x="{70+i*180+bw/2}" y="{y-7:.1f}" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="14" font-weight="600" fill="currentColor">{100*gf[ci]:.1f}%</text>')
                    A(f'<text x="{70+i*180+bw/2}" y="128" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="12" fill="currentColor" opacity=".7">cluster {ci} &#8212; {nmc}</text>')
                    A(f'<text x="{70+i*180+bw/2}" y="144" text-anchor="middle" font-family="Source Sans 3,sans-serif" font-size="11" fill="currentColor" opacity=".5">n={gn[ci]:,}</text>')
                A(f'<line x1="60" y1="110" x2="{w-20}" y2="110" stroke="currentColor" opacity=".25"/>')
                A(f'<text x="14" y="36" font-family="Source Sans 3,sans-serif" font-size="11" fill="currentColor" opacity=".6">% of</text>'
                  f'<text x="14" y="50" font-family="Source Sans 3,sans-serif" font-size="11" fill="currentColor" opacity=".6">cluster</text>'
                  f'<text x="14" y="64" font-family="Source Sans 3,sans-serif" font-size="11" fill="currentColor" opacity=".6">seen in</text>'
                  f'<text x="14" y="78" font-family="Source Sans 3,sans-serif" font-size="11" fill="currentColor" opacity=".6">gnomAD</text>')
                A('</svg>')
                A(f'<p class="tiny">The damaging cluster is <b>{r:.1f}&times; depleted</b> of variants actually observed in '
                  f'{gn[0]+gn[1]:,} gnomAD r4 observations. This is the Orianne-paper test: an unsupervised split made with '
                  'no population data recovers purifying selection.</p></div>')
    mc = cl.get("mut_cluster") or {}
    if mc:
        A('<h3>Where the literature mutations fall</h3><div class="scroll"><table><thead><tr><th>Mutation</th>'
          '<th>Literature label</th><th>Cluster</th></tr></thead><tbody>')
        for r in rows:
            c = mc.get(r["mut"])
            A(f'<tr><td class="mono">{esc(r["mut"])}</td><td><span class="chip {LBL.get(r["label"],"")}">{esc(r["label"])}</span></td>'
              f'<td>{"damaging" if c==1 else "tolerant" if c==0 else "<span class=\'tiny\'>not in the dbNSFP table</span>"}</td></tr>')
        A('</tbody></table></div>')
        A('<p class="tiny">dbNSFP indexes only substitutions reachable by a <b>single</b> nucleotide change &mdash; '
          'about 31% of all amino-acid substitutions are not, and those have no row here. '
          'V&rarr;F, for instance, needs two changes. The mutation is still fully computed in sections 6 to 8; '
          'only the clustering, which is built on the dbNSFP variant table, cannot place it.</p>')
        A('<p class="tiny">A GOF mutation landing in the tolerant cluster is not a failure: every predictor in the panel '
          'scores loss of function, so gain-of-function variants are systematically called benign. That is a known, '
          'structural limitation of the panel rather than noise.</p>')

    # ===== 6. mutations
    A('<h2 id="s6">6. Literature mutations &mdash; full computation</h2>')
    A(f'<p>{len(rows)} substitutions taken from the literature or ClinVar for {gene}. '
      '&Delta;&Delta;G is computed twice, once in the closed structure and once in the open one, with a cached '
      'wild-type local-repack PyRosetta protocol (ref2015, 8&nbsp;&Aring; repack shell). <b>Sign convention: positive = '
      'destabilising</b>, in Rosetta energy units, not kcal/mol.</p>')
    A('<div class="scroll"><table><thead><tr><th>Mut</th><th>Label</th><th>Domain</th>'
      '<th>&Delta;&Delta;G closed</th><th>&Delta;&Delta;G open</th><th>&Delta; (closed&minus;open)</th>'
      '<th>Interface</th><th>Pockets</th><th>pLDDT</th><th>RSA</th><th>SS</th>'
      '<th>AlphaMissense</th><th>ESM-1v</th><th>ESM-1b</th><th>FoldX</th><th>ThermoMPNN</th>'
      '<th>REVEL</th><th>CADD</th><th>SIFT</th><th>PolyPhen-2</th><th>MetaRNN</th><th>VEST4</th>'
      '<th>PrimateAI</th><th>PROVEAN</th><th>MutAssessor</th><th>ClinVar</th><th>Reference</th></tr></thead><tbody>')
    for r in rows:
        d = dd.get(r["mut"], {}); c, op = num(d.get("closed")), num(d.get("open"))
        fl = d.get("flag", {}) or {}
        def z(v, k):
            if v is None:
                s2 = stat(d.get(k))
                return f'<td class="tiny">{esc(s2)}</td>' if s2 else "<td>&ndash;</td>"
            cls = "pos" if v > 0 else "neg"
            s = "&#9888;" if fl.get(k) == "clash" else ""
            return f'<td class="{cls}">{v:+.2f}{s}</td>'
        diff = (c - op) if (c is not None and op is not None) else None
        A(f'<tr><td class="mono"><b>{esc(r["mut"])}</b></td>'
          f'<td><span class="chip {LBL.get(r["label"],"")}">{esc(r["label"])}</span></td>'
          f'<td>{esc(r.get("domain"))}</td>' + z(c,"closed") + z(op,"open") +
          (f'<td>{diff:+.2f}</td>' if diff is not None else "<td>&ndash;</td>") +
          f'<td>{"yes" if r.get("in_iface") else "no"}</td>'
          f'<td>{", ".join("#"+str(p) for p in (r.get("pockets") or [])) or "&ndash;"}</td>'
          f'<td>{fnum(r.get("plddt_af"),1)}</td><td>{fnum(r.get("rasa"),2)}</td><td>{(esc(r.get("ss")) or "&ndash;")}</td>'
          f'<td title="source: {esc(r.get("am_src") or "n/a")}">{fnum(r.get("am"),3)}</td>'
          f'<td>{fnum(r.get("esm1v"),2)}</td><td>{fnum(r.get("esm1b"),2)}</td>'
          f'<td>{fnum(r.get("foldx"),2)}</td><td>{fnum(r.get("tmpnn"),2)}</td>'
          f'<td>{fnum(r.get("revel"),3)}</td><td>{fnum(r.get("cadd"),1)}</td><td>{fnum(r.get("sift"),3)}</td>'
          f'<td>{fnum(r.get("polyphen"),3)}</td><td>{fnum(r.get("metarnn"),3)}</td><td>{fnum(r.get("vest4"),3)}</td>'
          f'<td>{fnum(r.get("primateai"),3)}</td><td>{fnum(r.get("provean"),2)}</td><td>{fnum(r.get("mutassessor"),2)}</td>'
          f'<td>{(esc(r.get("clinvar_sig")) or "&ndash;")}</td>'
          f'<td class="tiny">{esc(r.get("ref"))}</td></tr>')
    A('</tbody></table></div>')
    A('<p class="tiny">&#9888; marks a &Delta;&Delta;G whose magnitude exceeds 25 REU: that is repulsion, not a free energy. See caveats. '
      'Sign conventions differ between predictors and are left as each tool reports them: higher AlphaMissense, REVEL, CADD, '
      'PolyPhen-2, MetaRNN, VEST4 and MutAssessor mean more damaging; lower SIFT, PrimateAI, PROVEAN, ESM-1v and ESM-1b mean '
      'more damaging; higher FoldX and ThermoMPNN mean more destabilising. '
      'ESM-1v and ThermoMPNN come from the Liao &amp; Lehner proteome release, which covers 46 of the 54 screened proteins; '
      'where it is absent, AlphaMissense is taken from dbNSFP instead (hover the cell for the source). '
      'Empty dbNSFP cells are substitutions needing more than one nucleotide change.</p>')

    # ===== 7. pLDDT table
    A('<h2 id="s7">7. How pLDDT differs at the mutated sites</h2>')
    A('<p>pLDDT is a property of the <i>wild-type</i> prediction, so it does not change with the substitution; '
      'what it tells us is how much confidence to place in every structural number for that site. '
      'The columns compare the AlphaFold v6 value at the site with the median over its domain and over the whole chain.</p>')
    g0 = next((x for x in m["geom_all"] if x["kind"] == "prediction"), m["geom_all"][0])
    afat = ca(m["structures"][0]["file"], m["structures"][0].get("chain"))
    byres = {a[0]: a[5] for a in afat}
    dmed = {}
    for i,(nm,a,b) in enumerate(doms):
        vals = sorted(v for p,v in byres.items() if a <= p <= b)
        dmed[nm] = vals[len(vals)//2] if vals else None
    allv = sorted(byres.values()); gm = allv[len(allv)//2] if allv else None
    A('<div class="scroll"><table><thead><tr><th>Mut</th><th>Domain</th><th>pLDDT at site</th>'
      '<th>domain median</th><th>&Delta; vs domain</th><th>chain median</th><th>&Delta; vs chain</th>'
      '<th>window &plusmn;5 mean</th><th>Confidence band</th></tr></thead><tbody>')
    for r in rows:
        p = r["pos"]; v = byres.get(p); dn = r.get("domain") or ""
        dm = dmed.get(dn); w = [byres[q] for q in range(p-5, p+6) if q in byres]
        band = ("very high" if v and v >= 90 else "confident" if v and v >= 70 else "low" if v and v >= 50 else "very low" if v else "&ndash;")
        A(f'<tr><td class="mono">{esc(r["mut"])}</td><td>{esc(dn)}</td><td><b>{fnum(v,1)}</b></td>'
          f'<td>{fnum(dm,1)}</td><td>{fnum((v-dm) if (v and dm) else None,1)}</td>'
          f'<td>{fnum(gm,1)}</td><td>{fnum((v-gm) if (v and gm) else None,1)}</td>'
          f'<td>{fnum(sum(w)/len(w) if w else None,1)}</td><td>{band}</td></tr>')
    A('</tbody></table></div>')
    A(f'<p class="tiny">Window column is the mean pLDDT over the 11 residues centred on each mutated site. '
      f'Chain median {fnum(gm,1)}.</p>')

    # ===== 8. mechanisms
    A('<h2 id="s8">8. Proposed mechanism, mutation by mutation</h2>')
    A('<p>Each block below is assembled from <i>our</i> computations &mdash; the dual-state &Delta;&Delta;G, interface '
      'membership, pocket membership, burial and local confidence &mdash; and is then set beside what the literature says. '
      'Where the two disagree, the disagreement is stated rather than smoothed over.</p>')
    for r in rows:
        d = dd.get(r["mut"], {})
        txt, tags = mechanism(r, d, iface, hi, doms)
        A(f'<div class="mech"><div class="m-h">{esc(r["mut"])} '
          f'<span class="chip {LBL.get(r["label"],"")}">{esc(r["label"])}</span>'
          + "".join(f'<span class="chip">{t}</span>' for t in tags) + "</div>")
        A(f'<p style="margin:7px 0 0"><b>From our computations:</b> {txt}</p>')
        if r.get("mech_lit"):
            A(f'<p style="margin:7px 0 0"><b>Literature:</b> {esc(r["mech_lit"])} '
              f'<span class="tiny">({esc(r.get("ref"))})</span></p>')
        A('</div>')

    # ===== 9. literature
    A('<h2 id="s9">9. Literature review</h2>')
    lt = LIT.get(acc, {})
    for key, ttl, intro in (
        ("conf","9.1 Conformations: is there a real open and a real closed state?","What is actually known about this protein occupying more than one inter-domain arrangement."),
        ("mut","9.2 Mutations","Primary reports behind the substitutions computed in section 6."),
        ("drug","9.3 Drugs and drug resistance","Why the conformational question is a therapeutic question for this protein."),
        ("dis","9.4 Associated disease","")):
        items = lt.get(key) or []
        if not items: continue
        A(f'<h3>{ttl}</h3>')
        if intro: A(f'<p class="tiny">{intro}</p>')
        A('<ul class="refs">')
        for it in items:
            t = it["t"]
            if it.get("u"): t += f' &mdash; <a href="{esc(it["u"])}">link</a>'
            if it.get("v"): t += ' <span class="chip" style="background:var(--chip)">checked this session</span>'
            A(f'<li>{t}' + (f'<br><span class="tiny">{it["n"]}</span>' if it.get("n") else "") + "</li>")
        A('</ul>')

    # ===== 10. caveats
    A('<h2 id="s10">10. Caveats &mdash; read before using any number here</h2>')
    clashes = [(r["mut"], dd.get(r["mut"],{})) for r in rows
               if any((dd.get(r["mut"],{}).get("flag") or {}).get(k)=="clash" for k in ("closed","open"))]
    A('<div class="note"><b>1. Some &Delta;&Delta;G magnitudes are repulsion, not free energies.</b> '
      'The protocol repacks only an 8&nbsp;&Aring; shell around the mutated site and applies <b>no global FastRelax</b> '
      '(that choice buys ~100k variants/hour instead of ~11 minutes per structure). When a larger side chain cannot be '
      'accommodated by local repacking alone, the Lennard-Jones repulsive term dominates and the result is an arbitrary '
      'large positive number. Any |&Delta;&Delta;G| above 25 REU is flagged with &#9888; and should be read as '
      '&ldquo;sterically impossible without backbone relaxation&rdquo;, not as a measured energy.'
      + (f' Affected here: {", ".join("<code>"+esc(mu)+"</code>" for mu,_ in clashes)}.' if clashes else ' None affected in this protein.')
      + '</div>')
    A('<div class="note"><b>2. &ldquo;Open&rdquo; and &ldquo;closed&rdquo; here mean the inter-domain arrangement.</b> '
      'The same two words are used in the kinase literature for at least three other things: the G-loop over the ATP site '
      '(a few &Aring;), the DFG-in/DFG-out flip (~10&nbsp;&Aring;), and the WPD loop in phosphatases. A paper reporting that '
      'a mutation &ldquo;stabilises the closed conformation&rdquo; may well be talking about the active site, not the domain '
      'arrangement computed here. See <code>open_close/open_close_inf.md</code> in this repository for the measured '
      'comparison of the senses.</div>')
    A('<div class="note"><b>3. The predictor panel is blind to gain of function.</b> Every member scores '
      'loss of function or loss of stability. A constitutively activating mutation is therefore expected to score benign, '
      'and does. Cluster membership is evidence about tolerance, never about direction of effect.</div>')
    A('<div class="note"><b>4. Renumbering is sequence-based.</b> Template and experimental coordinates arrive in author '
      'numbering; each is mapped to canonical UniProt positions by the offset maximising sequence identity, and the '
      'achieved identity is reported in section 1. An offset with low identity means the mapping is unreliable and every '
      'per-residue number from that model with it.</div>')
    A('<div class="note"><b>5. Coverage limits the geometry.</b> A centroid distance computed from a partial domain is '
      'not comparable with one from the complete domain. Pairs where either domain is under 70% present are marked '
      'with * in section 2.</div>')
    A(f'<p class="tiny" style="margin-top:28px">Part of <a href="https://github.com/chervov/ProteinModelling1">'
      f'chervov/ProteinModelling1</a> &middot; data files: <code>more_proteins/top10/data/</code> &middot; '
      f'pipeline: <code>gather.py</code>, <code>geom.py</code>, <code>states.py</code>, <code>ddg.py</code>, '
      f'<code>mutfeat.py</code>, <code>clust.py</code>, <code>rep10.py</code></p>')

    # ---- scripts
    mdata = [{"id": f"v{i}", "pdb": s["pdb"]} for i, s in enumerate(models)]
    A("<script>")
    A("var DOMS=" + json.dumps([{"n": nm, "a": a, "b": b, "c": DCOL[i % 10]} for i,(nm,a,b) in enumerate(doms)]) + ";")
    A("var MODELS=" + json.dumps(mdata) + ";")
    A("var MUTPOS=" + json.dumps(sorted({r["pos"] for r in rows})) + ";")
    A("""
var VW={};
function plcol(b){return b>=90?'#0053d6':b>=70?'#65cbf3':b>=50?'#ffdb13':'#ff7d45';}
function domcol(p){for(var i=0;i<DOMS.length;i++){if(p>=DOMS[i].a&&p<=DOMS[i].b)return DOMS[i].c;}return '#9aa0a8';}
function paint(id,mode){var v=VW[id];if(!v)return;v.setStyle({},{});
 v.setStyle({},{cartoon:{style:'trace',thickness:0.7,colorfunc:function(a){return mode==='plddt'?plcol(a.b):domcol(a.resi);}}});
 MUTPOS.forEach(function(p){v.addStyle({resi:p},{sphere:{radius:1.5,color:'#d4213d'}});});
 v.render();}
function setmode(id,mode,btn){var g=btn.parentNode.querySelectorAll('.btn');for(var i=0;i<g.length;i++)g[i].setAttribute('aria-pressed','false');
 btn.setAttribute('aria-pressed','true');paint(id,mode);}
(function(){ if(typeof $3Dmol==='undefined'){document.querySelectorAll('.v3d').forEach(function(e){e.innerHTML='<p style="padding:14px;font-size:12px">3Dmol.js did not load; 3D views unavailable offline.</p>';});return;}
 MODELS.forEach(function(m){var el=document.getElementById(m.id);if(!el)return;
  var v=$3Dmol.createViewer(el,{backgroundAlpha:0});VW[m.id]=v;
  v.addModel(m.pdb,'pdb');paint(m.id,'dom');v.zoomTo();v.render();});})();
""")
    if pg:
        A("var PAE=" + json.dumps(pg) + ";")
        A("""
(function(){var c=document.getElementById('pae');if(!c||!PAE)return;var x=c.getContext('2d');
 var st=[[11,45,107],[47,123,191],[158,201,230],[242,242,242]];
 function col(v){var t=Math.min(v,30)/30,i=Math.min(2,Math.floor(t*3)),f=t*3-i;
  return 'rgb('+Math.round(st[i][0]+(st[i+1][0]-st[i][0])*f)+','+Math.round(st[i][1]+(st[i+1][1]-st[i][1])*f)+','+Math.round(st[i][2]+(st[i+1][2]-st[i][2])*f)+')';}
 for(var i=0;i<PAE.nb;i++)for(var j=0;j<PAE.nb;j++){x.fillStyle=col(PAE.g[i][j]);x.fillRect(j,i,1,1);}
 var sc=PAE.nb/PAE.n;DOMS.forEach(function(d){x.fillStyle=d.c;x.fillRect(d.a*sc,0,Math.max(1,(d.b-d.a)*sc),2);x.fillRect(0,d.a*sc,2,Math.max(1,(d.b-d.a)*sc));});})();
""")
    A("</script></div>\n</body>\n</html>")
    return "\n".join(o)

ORDER = ["P29597","P23458","Q06124","P12931","P00519","Q06187","Q5S007","P13569","P08183","O00571"]
out = os.path.join(D, "out"); os.makedirs(out, exist_ok=True)
sizes = []
for acc in ORDER:
    h = build(acc)
    fn = os.path.join(out, f"{META[acc]['gene']}_{acc}.html")
    open(fn, "w").write(h)
    sizes.append((META[acc]["gene"], acc, len(h)))
    print(f"  {META[acc]['gene']:8s} {acc}  {len(h)/1024:8.0f} KB")
json.dump(sizes, open(os.path.join(out, "_sizes.json"), "w"))
print("total %.1f MB" % (sum(s[2] for s in sizes)/1e6))

# ---------- index ----------
ix = [HEAD + '<title>Top ten conformational reports</title>', CSS, '</head>\n<body>', '<div class="wrap">',
      '<h1>Ten multi-domain proteins &mdash; deep conformational reports</h1>',
      '<p class="sub">Selected from the 54 proteins screened in <code>more_proteins/analysis1/</code> &middot; generated 2026-10-29</p>',
      '<p class="lede">Ten proteins that each have (a) several annotated domains, (b) literature describing more than one '
      'inter-domain arrangement, (c) more than one independent structural model spanning at least two of those domains, and '
      '(d) characterised mutations in the literature. Each report carries the full Orianne-paper battery: all-pairs '
      'inter-domain geometry across every structure, PAE, templates and homologs, the two-cluster split against gnomAD, '
      'dual-state &Delta;&Delta;G for every literature mutation, and a per-mutation mechanism.</p>',
      '<div class="scroll"><table><thead><tr><th>Gene</th><th>Protein</th><th>aa</th><th>Domains</th>'
      '<th>Structures</th><th>Largest-moving pair</th><th>Spread (&Aring;)</th><th>Muts</th>'
      '<th>gnomAD depletion</th><th>Report</th></tr></thead><tbody>']
for acc in ORDER:
    m = META[acc]; c = (CL.get(acc) or {}).get("rich") or {}
    gf = c.get("gnomad_frac"); dep = "&ndash;"
    if gf and min(gf) > 0:
        dam = 1 if c["means"]["1"].get("AlphaMissense",0) >= c["means"]["0"].get("AlphaMissense",0) else 0
        dep = f"{gf[1-dam]/gf[dam]:.1f}&times;"
    mv = sorted(m["movement"].items(), key=lambda kv: -kv[1]["spread"])
    big = mv[0] if mv else (None, {"spread": None})
    n = len((MF.get(acc) or {}).get("rows", []))
    ix.append(f'<tr><td><b>{m["gene"]}</b></td><td>{esc(m["name"])}</td><td>{m["length"]}</td>'
              f'<td>{len(m["domains"])}</td><td>{len(m["structures"])}</td>'
              f'<td>{(esc(big[0]).replace("|"," &harr; ") if big[0] else "&ndash;")}</td><td>{fnum(big[1]["spread"],1)}</td>'
              f'<td>{n}</td><td>{dep}</td><td><a href="{m["gene"]}_{acc}.html">open</a></td></tr>')
ix += ['</tbody></table></div>',
       '<div class="note">Read section 10 of any report before using a number from it: a minority of the '
       '&Delta;&Delta;G values are repulsion-dominated and unusable as free energies, and &ldquo;open/closed&rdquo; here '
       'always means the <b>inter-domain</b> arrangement, which is not the sense used in much of the kinase literature.</div>',
       f'<p class="tiny">Part of <a href="https://github.com/chervov/ProteinModelling1">chervov/ProteinModelling1</a></p>',
       '</div>', '</body>', '</html>']
open(os.path.join(out, "index.html"), "w").write("\n".join(ix))
print("index written")
