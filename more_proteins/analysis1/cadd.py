import json, os, sys, time, urllib.request, urllib.parse, csv
sys.path.insert(0,"/Users/chervov/analysis1"); os.chdir("/Users/chervov/analysis1")
T=json.load(open("targets.json")); SEQ=json.load(open("seqs.json"))
def flat(v):
    if isinstance(v,list):
        for x in v:
            r=flat(x)
            if r is not None: return r
        return None
    return v
def norm_aa(aa):
    for it in (aa if isinstance(aa,list) else [aa]):
        if not isinstance(it,dict): continue
        ref,alt,pos=it.get("ref"),it.get("alt"),it.get("pos")
        pl=[p for p in (pos if isinstance(pos,list) else [pos]) if isinstance(p,int)]
        if ref and alt and pl: yield str(ref),str(alt),pl
def fetch(gene,acc):
    seq=SEQ.get(acc,""); out={}; frm=0
    while True:
        q=urllib.parse.urlencode({"q":f"dbnsfp.genename:{gene}",
            "fields":"cadd.phred,dbnsfp.aa,dbnsfp.genename","size":"1000","from":str(frm)})
        d=None
        for att in range(5):
            try:
                d=json.load(urllib.request.urlopen(f"https://myvariant.info/v1/query?{q}",timeout=240)); break
            except Exception:
                if att==4: return out,"failed"
                time.sleep(8+8*att)
        hits=d.get("hits",[])
        if not hits: break
        for h in hits:
            b=h.get("dbnsfp") or {}
            gn=b.get("genename"); gn=gn if isinstance(gn,str) else flat(gn)
            if gn and str(gn).upper()!=gene.upper(): continue
            ph=(h.get("cadd") or {}).get("phred"); ph=flat(ph)
            if ph is None: continue
            for ref,alt,pl in norm_aa(b.get("aa")):
                if len(alt)!=1 or len(ref)!=1: continue
                good=[p for p in pl if 1<=p<=len(seq) and seq[p-1]==ref]
                if not good: continue
                k=(good[0],alt)
                if k not in out:
                    try: out[k]=float(ph)
                    except (TypeError,ValueError): pass
        frm+=len(hits)
        if len(hits)<1000 or frm>=d.get("total",0): break
        time.sleep(0.35)
    return out,None
if __name__=="__main__":
    for i,(acc,e) in enumerate(sorted(T.items(),key=lambda kv:kv[1]["gene"]),1):
        src=f"feat/{acc}.dbnsfp.csv"
        if not os.path.exists(src):
            print(f"[{i:>2}/54] {e['gene']:<10} no dbnsfp file yet",flush=True); continue
        rows=list(csv.DictReader(open(src)))
        if not rows:
            print(f"[{i:>2}/54] {e['gene']:<10} empty dbnsfp table, skipped",flush=True); continue
        if sum(1 for r in rows if r.get("cadd"))>0.5*len(rows):
            print(f"[{i:>2}/54] {e['gene']:<10} cadd already present",flush=True); continue
        C,err=fetch(e["gene"],acc)
        n=0
        for r in rows:
            try: k=(int(r["pos"]),r["alt"])
            except ValueError: continue
            if k in C: r["cadd"]=C[k]; n+=1
        with open(src,"w",newline="") as fh:
            w=csv.DictWriter(fh,fieldnames=list(rows[0].keys())); w.writeheader(); w.writerows(rows)
        print(f"[{i:>2}/54] {e['gene']:<10} cadd filled {n:,}/{len(rows):,}{' | '+err if err else ''}",flush=True)
        time.sleep(0.7)
    print("CADD DONE",flush=True)
