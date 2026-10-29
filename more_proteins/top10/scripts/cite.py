import json, sys, urllib.request, time
def summ(ids):
    u=("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="
       + ",".join(str(i) for i in ids))
    for _ in range(4):
        try:
            d=json.load(urllib.request.urlopen(u, timeout=40))["result"]; break
        except Exception as e:
            print("retry", e, file=sys.stderr); time.sleep(3)
    else: return []
    out=[]
    for k in d["uids"]:
        v=d[k]
        out.append(dict(pmid=k, date=v["pubdate"], j=v["source"], vol=v.get("volume"),
                        pages=v.get("pages"), title=v["title"],
                        authors=[a["name"] for a in v.get("authors",[])],
                        doi=(v.get("elocationid") or "").replace("doi: ","")))
    return out
if __name__=="__main__":
    for r in summ(sys.argv[1].split(",")):
        a=r["authors"]
        al=", ".join(a[:10])+(f" ... ({len(a)} authors)" if len(a)>10 else "")
        print(f'PMID {r["pmid"]} | {r["date"]} | {r["j"]} {r["vol"]}:{r["pages"]} | {r["doi"]}')
        print(f'  {r["title"]}')
        print(f'  {al}\n')
