import json, sys, urllib.request, urllib.parse, time
sys.path.insert(0,'/Users/chervov/homol')
from cite import summ
def search(term, n=14):
    u=("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&sort=relevance"
       f"&retmax={n}&term=" + urllib.parse.quote(term))
    for _ in range(4):
        try: return json.load(urllib.request.urlopen(u, timeout=40))["esearchresult"]["idlist"]
        except Exception as e: print("retry",e,file=sys.stderr); time.sleep(3)
    return []
Q = json.load(open(sys.argv[1]))
for gene, term in Q:
    ids = search(term)
    print(f"\n########## {gene}\n# {term}")
    for r in summ(ids):
        a=r["authors"]
        print(f'  [{r["pmid"]}] {r["date"]} {r["j"]} {r["vol"]}:{r["pages"]}  {a[0] if a else "?"} et al.')
        print(f'      {r["title"]}')
    time.sleep(1)
