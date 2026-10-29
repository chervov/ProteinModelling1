import json, sys
sys.path.insert(0,'/Users/chervov/homol')
from cite import summ

# SRC-family extended set. tier A/B as before; "fam" names the protein actually studied.
EXT = [
 ("9024665","A","HCK","Displacing the SH3 domain with a high-affinity ligand ACTIVATES Hck: the functional proof that the inter-domain clamp, not the active site, holds activity down. Published back-to-back with the two 1997 crystals."),
 ("9405157","A","SRC (chicken)","The 2.35 A inactivated chicken Src, described by its authors as 'a dynamic molecule with multiple regulatory interactions' - a third independent closed structure that already framed the arrangement as an equilibrium, not a fixed state."),
 ("9405355","B","SRC","The SH2-kinase LINKER is the element the SH3 domain grips; mutagenesis mapping which linker residues hold the clamp."),
 ("10426955","B","SRC","Leu255 couples the intramolecular interactions to inhibition of catalysis - a single residue that transmits the inter-domain clamp to the active site."),
 ("18369437","A","SRC","Thermodynamics, pathways and mechanisms of Src conformational activation - the first systematic free-energy treatment."),
 ("19686639","B","SRC","String method with swarms of trajectories applied to Src activation; the method Fajer 2017 later builds on."),
 ("24584478","A","SRC","Markov state model of Src activation from massively distributed simulation: the pathway with INTERMEDIATE states, proposed as drug targets. The clearest statement that the transition is not two-state."),
 ("27482115","A","SRC","Transition path theory analysis of c-Src activation - the committor and the actual reactive flux, not just the endpoints."),
 ("28426203","C","Src family","The review that makes exactly the distinction this project insists on: inter-domain regulatory arrangement versus the aC-helix/activation-loop state inside the kinase domain."),
 ("32224253","A","HCK","A single glycine substitution in the SH3-SH2 connector shifts the POPULATION from assembled to disassembled - a mutation moving the open/closed equilibrium, measured. Directly analogous to what we compute."),
 ("18614016","B","SRC","Structural basis for recognition of c-Src by Csk, the kinase that creates the closed state by phosphorylating the C-terminal tail."),
 ("31331936","A","SRC","Autophosphorylation activates c-Src through GLOBAL structural rearrangements - the inter-domain change measured rather than inferred."),
 ("37848415","A","SRC","An allosteric switch between the activation loop and a C-terminal palindromic phospho-motif controls c-Src function."),
 ("35120901","A","SRC","Mechanical force can enhance c-Src activity by IMPAIRING AUTOINHIBITION - a third way of opening the clamp, neither ligand nor phosphorylation."),
]
# the pasted-list members we did not already carry
PASTED_ADD = [
 ("9024658","A","HCK","Crystal structure of Hck: the same SH2/SH3-mediated autoinhibitory arrangement in a second family member, published alongside the c-Src structure. PDB 1AD5 (AMP-PNP) and 2HCK (quercetin)."),
 ("10360180","A","HCK","Hck with a Src-family-selective inhibitor at 2.0 A - the standard autoinhibited HCK reference, PDB 1QCF, with an ordered inhibitory activation segment."),
 ("20798061","A","HCK","SAXS plus coarse-grained simulation and Bayesian population estimation: assembled, partially disassembled, reassembled and EXTENDED arrangements coexist in solution. The strongest argument that two endpoint structures are not enough."),
 ("36476673","A","LCK","Genuinely full-length Lck - SH4/unique region, myristoylation and palmitoylation, in a membrane - simulated from open and closed starting models, 100 us each. The closest Src-family analogue of Ayaz 2019 for JAK2."),
 ("39596456","B","SRC","Full-length c-Src models including the disordered N-terminal region, from AlphaFold2 coordinates plus experimental domains, compared across phosphorylation states."),
 ("41720803","B","SRC","Cryo-EM of beta-arrestin 1 disrupting Src autoinhibition through SH3 engagement - a binding partner opening the clamp."),
]
cit = {r["pmid"]: r for r in summ([p for p,_,_,_ in EXT+PASTED_ADD])}
rows=[]
for pmid, tier, fam, note in PASTED_ADD + EXT:
    c = cit.get(pmid)
    if not c: print("MISSING", pmid, file=sys.stderr); continue
    rows.append(dict(pmid=pmid, tier=tier, fam=fam, note=note, title=c["title"], j=c["j"],
                     date=c["date"], vol=c["vol"], pages=c["pages"], doi=c["doi"], authors=c["authors"]))
P="/Users/chervov/top10/conf_papers.json"
d=json.load(open(P)); d["_src_extended"]=rows; json.dump(d, open(P,"w"), indent=1)
print(f"{len(rows)} papers in the SRC-family extended set")
for r in rows: print(f'  [{r["tier"]}] {r["fam"]:<12} {r["authors"][0]} {r["j"]} {r["date"].split()[0]} | {r["doi"]}')
