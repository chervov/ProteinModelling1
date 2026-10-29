import json, os, sys, time, urllib.request
def get(url, tries=5, timeout=120):
    for k in range(tries):
        try: return json.load(urllib.request.urlopen(url, timeout=timeout))
        except Exception:
            if k==tries-1: raise
            time.sleep(4+4*k)
def grab(url, path, tries=3):
    for k in range(tries):
        try: urllib.request.urlretrieve(url, path); return True
        except Exception:
            if k==tries-1: return False
            time.sleep(3+3*k)
sys.path.insert(0,'/Users/chervov/top10'); os.chdir('/Users/chervov/top10')
from ten import TEN
# extra experimental structures known to capture specific states
EXTRA = {
 "P29597": [("4OLI","closed JH2-JH1 (X-ray 2.8 A)","A")],
 "P23458": [],   # ModelArchive open/closed handled separately
 "P00519": [("1OPL","autoinhibited ABL1 (SH3-SH2 clamped)","A"),("2GQG","imatinib-bound","A")],
 "P12931": [("2SRC","autoinhibited c-Src","A"),("1FMK","inactive c-Src","A"),("1Y57","activated-like","A")],
 "Q06187": [("8GMB","BTK full-length autoinhibited","A")],
 "Q06124": [("4DGX","autoinhibited SHP2","A"),("6CRF","activated SHP2 E76K","A")],
 "P13569": [("5UAK","CFTR dephosphorylated/NBD-separated","A"),("6MSM","CFTR phosphorylated ATP-bound","A")],
 "P08183": [("6QEX","P-gp inward-open","A"),("6C0V","P-gp nucleotide-bound occluded","A")],
 "Q5S007":[("7LHW","LRRK2 full-length","A")],
 "O00571": [("5E7M","DDX3X helicase domains","A")],
}
MA = {"P23458":[("ma-l9b1f","Jeanpierre closed JAK1"),("ma-a1sai","Jeanpierre open JAK1")]}
meta=json.load(open("meta.json")) if os.path.exists("meta.json") else {}
for gene,acc,why in TEN:
    if acc in meta and meta[acc].get("structures"):
        print(f"{gene:<8}cached ({len(meta[acc]['structures'])} structures)",flush=True); continue
    rec=dict(gene=gene,acc=acc,why=why,structures=[])
    # UniProt
    u=get(f"https://rest.uniprot.org/uniprotkb/{acc}.json?fields=ft_domain,length,protein_name")
    rec["length"]=u["sequence"]["length"]
    rec["name"]=u.get("proteinDescription",{}).get("recommendedName",{}).get("fullName",{}).get("value")
    rec["domains"]=[[f.get("description","?"),f["location"]["start"]["value"],f["location"]["end"]["value"]]
                    for f in u.get("features",[]) if f["type"]=="Domain"]
    # AlphaFold + PAE
    try:
        d=get(f"https://alphafold.ebi.ac.uk/api/prediction/{acc}")[0]
        for url,sub,ext in ((d["pdbUrl"],"af","pdb"),(d["paeDocUrl"],"pae","json")):
            p=f"{sub}/{acc}.{ext}"
            if not os.path.exists(p): grab(url,p)
        rec["structures"].append(dict(label="AlphaFold v6",file=f"af/{acc}.pdb",kind="prediction",
                                      identity=100.0,chain=None,src="AlphaFold DB"))
    except Exception as e: rec["af_err"]=str(e)[:70]
    # extra experimental
    for pid,lab,ch in EXTRA.get(acc,[]):
        p=f"st/{acc}_{pid}.pdb"
        if not os.path.exists(p):
            if not grab(f"https://files.rcsb.org/download/{pid}.pdb",p): continue
        rec["structures"].append(dict(label=f"{pid} — {lab}",file=p,kind="experimental",
                                      identity=None,chain=ch,src=f"RCSB {pid}"))
    for mid,lab in MA.get(acc,[]):
        p=f"st/{acc}_{mid}.cif"
        if not os.path.exists(p):
            if not grab(f"https://www.modelarchive.org/doi/10.5452/{mid}.cif",p): continue
        rec["structures"].append(dict(label=f"{mid} — {lab}",file=p,kind="model",
                                      identity=None,chain=None,src=f"ModelArchive {mid}"))
    # SWISS-MODEL: own models (UniProt-numbered), keep identity -> own protein vs homolog
    try:
        r=get(f"https://swissmodel.expasy.org/repository/uniprot/{acc}.json")["result"]
        cand=[]
        for s in r.get("structures",[]):
            if s.get("provider")!="SWISSMODEL": continue
            fr,to=s.get("from"),s.get("to")
            if not (fr and to): continue
            ncov=sum(1 for n,a,b in rec["domains"] if fr<=a and b<=to)
            if ncov<2: continue
            cand.append((ncov,to-fr+1,s))
        cand.sort(key=lambda z:(-z[0],-z[1]))
        seen=set(); n=0
        for ncov,L,s in cand:
            tpl=(s.get("template") or "")
            pid=tpl[:4].lower()
            if pid in seen: continue
            seen.add(pid)
            p=f"st/{acc}_sm_{tpl.replace('.','-')}.pdb"
            if not os.path.exists(p):
                if not grab(s["coordinates"],p): continue
            idn=s.get("identity")
            rec["structures"].append(dict(label=f"{tpl} ({idn and round(idn,1)}% id)",file=p,
                kind="swissmodel", identity=idn, chain=None,
                src=f"SWISS-MODEL on {tpl}", ndom=ncov))
            n+=1
            if n>=12: break
    except Exception as e: rec["sm_err"]=str(e)[:70]
    meta[acc]=rec
    json.dump(meta,open("meta.json","w"),indent=1)
    own=[s for s in rec["structures"] if (s.get("identity") or 0)>=99]
    hom=[s for s in rec["structures"] if s.get("identity") is not None and s["identity"]<99]
    exp=[s for s in rec["structures"] if s["kind"] in ("experimental","model")]
    print(f"{gene:<8}{len(rec['domains']):>2}dom  structures: {len(rec['structures']):>2} "
          f"(own {len(own)}, homolog {len(hom)}, experimental/model {len(exp)})",flush=True)
    time.sleep(0.4)
json.dump(meta,open("meta.json","w"),indent=1)
print("\nmeta.json written")
