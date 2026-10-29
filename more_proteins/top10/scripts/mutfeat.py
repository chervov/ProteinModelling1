"""Per-mutation evidence: all predictors, pLDDT, pocket membership, interface membership."""
import json, os, sys, csv, collections
sys.path.insert(0,'/Users/chervov/top10'); os.chdir('/Users/chervov/top10')
from muts import MUTS
FEAT="/Users/chervov/analysis1/feat"
META=json.load(open("meta.json")); STATES=json.load(open("states.json"))
POCK=json.load(open("pockets.json"))

def plddt_map(path):
    out={}
    for L in open(path,errors="replace"):
        if L.startswith("ATOM") and L[12:16].strip()=="CA":
            try: out[int(L[22:26])]=float(L[60:66])
            except ValueError: pass
    return out

def load(acc):
    F={}
    p=f"{FEAT}/{acc}.foldx.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: F[(int(r["pos"]),r["alt"])]={"foldx":float(r["foldx_ddg"]),"plddt":float(r["plddt"])}
            except ValueError: pass
    p=f"{FEAT}/{acc}.tmpnn.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: k=(int(r["new_position"]),r["mutation"].strip())
            except (ValueError,KeyError): continue
            d=F.setdefault(k,{})
            def n(c):
                try: return float(r[c])
                except (ValueError,KeyError,TypeError): return None
            d.update(tmpnn=n("ddG_pred"),esm1v=n("ESM1v_all_variants"),am=n("am_pathogenicity"),
                     am_class=r.get("am_class"),rasa=n("exposure_rasa"),ss=r.get("exposure_ss"),
                     plddt2=n("exposure_plddt"),
                     clinvar=(r.get("clinvar_variation_id") or "").strip() or None,
                     clinvar_sig=(r.get("clinvar_clinical_significance") or "").strip() or None)
    p=f"{FEAT}/{acc}.dbnsfp.csv"
    if os.path.exists(p):
        for r in csv.DictReader(open(p)):
            try: k=(int(r["pos"]),r["alt"])
            except (ValueError,KeyError): continue
            d=F.setdefault(k,{})
            for c in ("revel","cadd","sift","polyphen","metarnn","vest4","primateai",
                      "mutassessor","provean","esm1b","gerp"):
                v=r.get(c)
                if v: 
                    try: d[c]=float(v)
                    except ValueError: pass
            # the Liao & Lehner proteome set covers 46 of our 54 proteins; where it is missing
            # (PTPN11, LRRK2) dbNSFP still carries AlphaMissense, so fall back to it and record
            # which source the number came from.
            v=r.get("am_dbnsfp")
            if v and d.get("am") is None:
                try: d["am"]=float(v); d["am_src"]="dbNSFP"
                except ValueError: pass
            elif d.get("am") is not None:
                d.setdefault("am_src","Liao&Lehner")
    return F

out={}
for acc,rec in META.items():
    F=load(acc); gene=rec["gene"]
    plm=plddt_map(f"af/{acc}.pdb") if os.path.exists(f"af/{acc}.pdb") else {}
    iface=set(STATES.get(acc,{}).get("iface",[]))
    # high-confidence pockets -> residue -> pocket ids
    pres=collections.defaultdict(list)
    for p in POCK.get(acc,[]):
        if p["score"]<800: continue
        for t in str(p["resid"]).replace(";",",").split(","):
            t=t.strip()
            if t.isdigit(): pres[int(t)].append(p["pid"])
    rows=[]
    for wt,pos,alt,lab,mech,ref in MUTS.get(acc,[]):
        f=F.get((pos,alt),{})
        dom=next((d[0] for d in rec["domains"] if d[1]<=pos<=d[2]), None)
        rows.append(dict(mut=f"{wt}{pos}{alt}",wt=wt,pos=pos,alt=alt,label=lab,mech_lit=mech,ref=ref,
            domain=dom, in_iface=pos in iface, pockets=pres.get(pos,[]),
            plddt_af=round(plm.get(pos),2) if pos in plm else None, **f))
    out[acc]=dict(gene=gene,rows=rows)
    nf=sum(1 for r in rows if r.get("foldx") is not None)
    ni=sum(1 for r in rows if r["in_iface"]); npk=sum(1 for r in rows if r["pockets"])
    print(f"{gene:<8}{len(rows):>2} mutations | predictors on {nf} | at interface {ni} | in a high-conf pocket {npk}",flush=True)
json.dump(out,open("mutfeat.json","w"),indent=1)
print("\nmutfeat.json written")
