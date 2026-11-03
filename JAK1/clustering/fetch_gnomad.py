"""gnomAD r4 missense variants for JAK1, keyed (position, alt) -> allele frequency."""
import json, urllib.request
AA3={"Ala":"A","Arg":"R","Asn":"N","Asp":"D","Cys":"C","Gln":"Q","Glu":"E","Gly":"G","His":"H",
     "Ile":"I","Leu":"L","Lys":"K","Met":"M","Phe":"F","Pro":"P","Ser":"S","Thr":"T","Trp":"W",
     "Tyr":"Y","Val":"V","Ter":"*"}
q=("query($g:String!){gene(gene_symbol:$g,reference_genome:GRCh38){variants(dataset:gnomad_r4)"
   "{consequence hgvsp exome{af ac an} genome{af ac an}}}}")
body=json.dumps({"query":q,"variables":{"g":"JAK1"}}).encode()
r=urllib.request.Request("https://gnomad.broadinstitute.org/api",data=body,
    headers={"Content-Type":"application/json","User-Agent":"research-script"})
d=json.load(urllib.request.urlopen(r,timeout=600))
out={}; nmis=0
for v in (d["data"]["gene"]["variants"] or []):
    if v.get("consequence")!="missense_variant": continue
    nmis+=1
    h=(v.get("hgvsp") or "")
    if not h.startswith("p."): continue
    b=h[2:]; wt3,rest=b[:3],b[3:]
    pos="".join(c for c in rest if c.isdigit()); alt3=rest[len(pos):]
    if not pos or wt3 not in AA3 or alt3 not in AA3: continue
    ex=v.get("exome") or {}; ge=v.get("genome") or {}
    af=ex.get("af") or ge.get("af"); ac=(ex.get("ac") or 0)+(ge.get("ac") or 0)
    k=f"{pos}{AA3[alt3]}"
    if af is None: continue
    if k not in out or af>out[k]["af"]: out[k]={"af":af,"ac":ac,"wt":AA3[wt3],"pos":int(pos)}
print(f"gnomAD r4 JAK1: {nmis} missense records -> {len(out)} unique (pos,alt) with AF")
json.dump(out, open("jak1_gnomad.json","w"))
