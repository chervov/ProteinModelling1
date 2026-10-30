import json
from Bio import Align
from Bio.Align import substitution_matrices
T = "/Users/chervov/.claude/jobs/e920d48f/tmp/j2"
al = Align.PairwiseAligner()
al.substitution_matrix = substitution_matrices.load("BLOSUM62")
al.open_gap_score, al.extend_gap_score = -11, -1
al.mode = "global"
J2 = json.load(open(T+"/JAK2.json"))["seq"]
out = {}
for g in ("TYK2","JAK1"):
    S = json.load(open(f"{T}/{g}.json"))["seq"]
    a = al.align(J2, S)[0]
    pr = {}
    for (s1,e1),(s2,e2) in zip(a.aligned[0], a.aligned[1]):
        for k in range(e1-s1): pr[s1+k+1] = s2+k+1
    ident = sum(1 for p,q in pr.items() if J2[p-1]==S[q-1])
    print(f"JAK2 -> {g}: score {a.score:.0f}, {len(pr)} aligned pairs, {ident} identical "
          f"({100*ident/len(pr):.1f}% over aligned, {100*ident/len(J2):.1f}% of JAK2)")
    out[g] = {str(int(k)): int(v) for k, v in pr.items()}
json.dump(out, open(T+"/map.json","w"))
# spot check on landmarks
mp = out
print("\nlandmark check (JAK2 -> TYK2 / JAK1):")
for p, lab in [(617,"V617F"), (595,"F595 pi-stack partner"), (1008,"JH1 catalytic")]:
    t = mp["TYK2"].get(str(p)); j = mp["JAK1"].get(str(p))
    tt = json.load(open(T+"/TYK2.json"))["seq"]; jj = json.load(open(T+"/JAK1.json"))["seq"]
    print(f"  JAK2 {J2[p-1]}{p} -> TYK2 {tt[t-1]}{t} | JAK1 {jj[j-1]}{j}")
