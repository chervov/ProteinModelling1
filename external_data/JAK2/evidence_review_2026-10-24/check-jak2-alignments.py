import json
from pathlib import Path
# Global affine-gap alignment, standard BLOSUM62.
letters='ARNDCQEGHILKMFPSTWYV'
rows='''4 -1 -2 -2 0 -1 -1 0 -2 -1 -1 -1 -1 -2 -1 1 0 -3 -2 0
-1 5 0 -2 -3 1 0 -2 0 -3 -2 2 -1 -3 -2 -1 -1 -3 -2 -3
-2 0 6 1 -3 0 0 0 1 -3 -3 0 -2 -3 -2 1 0 -4 -2 -3
-2 -2 1 6 -3 0 2 -1 -1 -3 -4 -1 -3 -3 -1 0 -1 -4 -3 -3
0 -3 -3 -3 9 -3 -4 -3 -3 -1 -1 -3 -1 -2 -3 -1 -1 -2 -2 -1
-1 1 0 0 -3 5 2 -2 0 -3 -2 1 0 -3 -1 0 -1 -2 -1 -2
-1 0 0 2 -4 2 5 -2 0 -3 -3 1 -2 -3 -1 0 -1 -3 -2 -2
0 -2 0 -1 -3 -2 -2 6 -2 -4 -4 -2 -3 -3 -2 0 -2 -2 -3 -3
-2 0 1 -1 -3 0 0 -2 8 -3 -3 -1 -2 -1 -2 -1 -2 -2 2 -3
-1 -3 -3 -3 -1 -3 -3 -4 -3 4 2 -3 1 0 -3 -2 -1 -3 -1 3
-1 -2 -3 -4 -1 -2 -3 -4 -3 2 4 -2 2 0 -3 -2 -1 -2 -1 1
-1 2 0 -1 -3 1 1 -2 -1 -3 -2 5 -1 -3 -1 0 -1 -3 -2 -2
-1 -1 -2 -3 -1 0 -2 -3 -2 1 2 -1 5 0 -2 -1 -1 -1 -1 1
-2 -3 -3 -3 -2 -3 -3 -3 -1 0 0 -3 0 6 -4 -2 -2 1 3 -1
-1 -2 -2 -1 -3 -1 -1 -2 -2 -3 -3 -1 -2 -4 7 -1 -1 -4 -3 -2
1 -1 1 0 -1 0 0 0 -1 -2 -2 0 -1 -2 -1 4 1 -3 -2 -2
0 -1 0 -1 -1 -1 -1 -2 -2 -1 -1 -1 -1 -2 -1 1 5 -2 -2 0
-3 -3 -4 -4 -2 -2 -3 -2 -2 -3 -2 -3 -1 1 -4 -3 -2 11 2 -3
-2 -2 -2 -3 -2 -1 -2 -3 2 -1 -1 -2 -1 3 -3 -2 -2 2 7 -1
0 -3 -3 -3 -1 -2 -2 -3 -3 3 1 -2 1 -1 -2 -2 0 -3 -1 4'''
mat={(a,b):v for a,row in zip(letters,rows.splitlines()) for b,v in zip(letters,map(int,row.split()))}
def align(a,b,op=10,ext=.5):
 n,m=len(a),len(b); neg=-1e9
 S=[[[neg]*(m+1) for _ in range(n+1)] for _ in range(3)];P=[[[0]*(m+1) for _ in range(n+1)] for _ in range(3)]
 S[0][0][0]=0
 for i in range(1,n+1): S[1][i][0]=-op-(i-1)*ext;P[1][i][0]=1 if i>1 else 0
 for j in range(1,m+1): S[2][0][j]=-op-(j-1)*ext;P[2][0][j]=2 if j>1 else 0
 for i in range(1,n+1):
  for j in range(1,m+1):
   vs=[S[k][i-1][j-1] for k in range(3)];k=max(range(3),key=vs.__getitem__);S[0][i][j]=vs[k]+mat.get((a[i-1],b[j-1]),-1);P[0][i][j]=k
   vs=[S[0][i-1][j]-op,S[1][i-1][j]-ext,S[2][i-1][j]-op];k=max(range(3),key=vs.__getitem__);S[1][i][j]=vs[k];P[1][i][j]=k
   vs=[S[0][i][j-1]-op,S[1][i][j-1]-op,S[2][i][j-1]-ext];k=max(range(3),key=vs.__getitem__);S[2][i][j]=vs[k];P[2][i][j]=k
 i,j=n,m;k=max(range(3),key=lambda k:S[k][n][m]);aa=[];bb=[]
 while i or j:
  prev=P[k][i][j]
  if k==0:aa.append(a[i-1]);bb.append(b[j-1]);i-=1;j-=1
  elif k==1:aa.append(a[i-1]);bb.append('-');i-=1
  else:aa.append('-');bb.append(b[j-1]);j-=1
  k=prev
 return ''.join(aa[::-1]),''.join(bb[::-1])
data=json.loads(Path(__file__).with_name('JAK-family-reference-sequences.json').read_text())
out=[]
for g in ['JAK1','JAK3','TYK2']:
 for domain,targets in [('Protein kinase 1',[571,578,805]),('Protein kinase 2',[1110])]:
  da=next(f for f in data['JAK2']['features'] if f['type']=='Domain' and f['description']==domain);db=next(f for f in data[g]['features'] if f['type']=='Domain' and f['description']==domain)
  sa=da['location']['start']['value']-1;ea=da['location']['end']['value'];sb=db['location']['start']['value']-1;eb=db['location']['end']['value']
  for op,ext in [(8,.5),(12,1),(10,.5)]:
   x,y=align(data['JAK2']['sequence']['value'][sa:ea],data[g]['sequence']['value'][sb:eb],op,ext);p=sa;q=sb
   for u,v in zip(x,y):
    p+=u!='-';q+=v!='-'
    if p in targets and u!='-':out.append({'gene':g,'jak2_position':p,'other_position':q,'other_residue':v,'gap_open':op,'gap_extension':ext})
Path(__file__).with_name('JAK2-alignment-sensitivity.json').write_text(json.dumps(out,indent=2));print(json.dumps(out))
