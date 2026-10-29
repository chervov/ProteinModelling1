"""Curated set: for each of the ten, five papers that report or model distinct
inter-domain conformational states — the same level of evidence as the four JAK papers."""
import json, sys
sys.path.insert(0,'/Users/chervov/homol')
from cite import summ

# pmid -> (tier, what two states it establishes)
# tier A = reports two or more distinct inter-domain arrangements of this protein
# tier B = one arrangement experimentally, or the transition modelled
# tier C = the state is inferred from a ligand/homolog, or a conformational review
SET = {
"P29597": [  # TYK2
 ("24843152","A","The 2.8 A crystal of the TYK2 JH2-JH1 module: the only experimental CLOSED inter-domain state anywhere in the JAK family. Our 4OLI."),
 ("24704786","B","TYK2 FERM-SH2 bound to the IFNAR1 box1/box2 region - the other half of the architecture, fixing where the N-terminal module sits."),
 ("35271300","A","Full-length JAK on a receptor dimer by cryo-EM: the autoinhibited JH2-JH1 module docked against FERM-SH2, and the activated dimer. The architecture TYK2 is read onto."),
 ("40378946","B","Allosteric TYK2-specific inhibitors acting by a triple mechanism; the drug works by holding the JH2-JH1 arrangement, so it is a conformational readout."),
 ("35525559","B","Pseudokinase-domain STABILISERS that allosterically inhibit TYK2 - small molecules selected for locking the closed state."),
],
"P23458": [  # JAK1
 ("35271300","A","Full-length JAK1 cryo-EM: the compact autoinhibited arrangement and the activated receptor-dimer arrangement side by side."),
 ("36867534","A","Structural basis of JAK trans-activation - the dimeric, activated JH1-JH1 arrangement that the closed state must give way to."),
 ("38446738","A","Multi-domain motions in JAK1 activation studied on an energy landscape: explicitly the open-vs-closed inter-domain question, computationally."),
 ("40868963","B","MD of JAK1 initial activation: phosphorylation-induced conformational dynamics and inter-domain interactions."),
 ("27227461","B","Crystal structure of the JAK2 FERM-SH2 module - the evidence that FERM and SH2 move as one rigid block, which is why only FERM-vs-kinase moves."),
],
"Q06124": [  # PTPN11 / SHP2
 ("9491886","A","The founding autoinhibited crystal: N-SH2 inserted into the PTP catalytic cleft. The CLOSED state of this protein."),
 ("27362227","A","SHP099 binds a tunnel formed only where N-SH2, C-SH2 and PTP meet - an allosteric site that exists in the closed state and not the open one."),
 ("30375376","A","Mechanism of activating mutations AND allosteric drug inhibition: the open and closed states and the mutations that shift between them."),
 ("30375388","A","Structural reorganization by oncogenic mutations, and why an open-shifted oncoprotein resists an inhibitor that needs the closed state."),
 ("38129686","A","An atomistic ensemble of the ACTIVE (open) phosphatase - the open state characterised in its own right rather than inferred."),
],
"P12931": [  # SRC
 ("9024657","B","The first three-dimensional structure of c-Src: the assembled, autoinhibited SH3-SH2-kinase arrangement."),
 ("10360179","A","Crystal structures of c-Src revealing the autoinhibitory mechanism - the SH3-SH2 clamp on the back of the kinase domain."),
 ("15939018","A","An ACTIVE-conformation c-Src complex, with the proposed steps of activation: the second state, and the path between."),
 ("27715044","A","The conformational transition pathway and free energy landscape of c-Src activation - the open/closed transition computed end to end."),
 ("31331936","A","Autophosphorylation activates c-Src through GLOBAL structural rearrangements - the inter-domain change measured, not the active site."),
],
"P00519": [  # ABL1
 ("12654251","A","Structural basis for the autoinhibition of c-Abl: the assembled SH3-SH2-kinase clamp. The CLOSED state."),
 ("12654250","A","The myristoyl/phosphotyrosine switch - the latch that holds the closed state, and what releasing it does."),
 ("16543148","A","Organization of the SH3-SH2 unit in ACTIVE AND INACTIVE forms of c-Abl: both inter-domain arrangements in one paper."),
 ("33004676","A","Conformational states dynamically populated by a kinase determine its function - the Abl state ensemble, not a single structure."),
 ("37843155","B","The myristoyl group's dual role in allosterically regulating and localising Abl: simulations of the latched and unlatched arrangements."),
],
"Q06187": [  # BTK
 ("25699547","A","Autoinhibition of BTK and its activation by soluble IP6: the compact autoinhibited arrangement and what opens it."),
 ("31019091","A","D. E. Shaw Research. Structural mechanism for BTK activation at the cell membrane - the full open/closed transition from long-timescale MD."),
 ("31591208","A","The lipid-targeting PH domain turns its AUTOINHIBITORY face toward the TEC kinases - how the PH-TH module docks in the closed state."),
 ("33226337","A","Differential impact of active-site inhibitors on the conformational state of FULL-LENGTH BTK: drugs read out as open or closed."),
 ("39728925","A","The clinically approved BTK inhibitors against full-length BTK conformation, with the CLL resistance mutations - conformation and resistance in one study."),
],
"Q5S007": [  # LRRK2
 ("32814344","A","Cryo-EM of LRRK2 and a model for microtubule interaction: the first full inter-domain architecture."),
 ("32783917","A","The IN SITU structure of LRRK2 inside cells - the arrangement as it actually occurs, including the filament form."),
 ("34107286","A","Structural analysis of full-length human LRRK2: the autoinhibited, closed inter-domain arrangement of the whole protein."),
 ("38127736","A","Rab29-dependent ASYMMETRICAL activation - two different inter-domain arrangements within one assembly."),
 ("42575089","A","The structural basis for LRRK2's activation and autoinhibition: the open and closed states and the transition, 2026."),
],
"P13569": [  # CFTR
 ("27912062","B","The first atomic structure of CFTR (zebrafish, dephosphorylated): the NBD-separated state."),
 ("28340353","A","Molecular structure of the HUMAN CFTR ion channel in the dephosphorylated, NBD-separated state. Our 5UAK lineage."),
 ("28735752","A","Conformational changes of CFTR upon phosphorylation AND ATP binding - the NBD-separated and NBD-dimerised states in one study. Exactly our open/closed pair."),
 ("30459277","A","The ATP-bound, phosphorylated human CFTR: the NBD-dimerised CLOSED state at higher resolution. Our 6MSM lineage."),
 ("36949202","A","CFTR function, pathology and pharmacology at single-molecule resolution - the state occupancies measured one molecule at a time."),
],
"P08183": [  # ABCB1
 ("29440498","A","Zosuquidar- and UIC2-bound human-mouse chimeric ABCB1: an inhibitor-trapped inward-facing arrangement."),
 ("30765569","A","Structural insight into substrate and inhibitor discrimination by human P-glycoprotein - different NBD arrangements for different cargo."),
 ("30622258","A","INWARD- AND OUTWARD-FACING X-ray structures of a homodimeric P-glycoprotein: both ends of the transport cycle in one paper."),
 ("33020312","A","Cryo-EM structures revealing distinct mechanisms of inhibition of human ABCB1 - several distinct NBD arrangements."),
 ("31641149","A","Dynamics of P-glycoprotein in THREE conformational states - the states characterised dynamically, not as static snapshots."),
],
"O00571": [  # DDX3X
 ("26598523","A","Autoinhibitory INTERDOMAIN interactions redefine the catalytic core of human DDX3 - the RecA1-RecA2 open/closed question stated directly."),
 ("25724843","A","Cancer-associated DDX3X mutants defective in RNA-stimulated ATP hydrolysis, with crystal structures: the mutations that break domain closure."),
 ("31300642","A","The mechanism of RNA duplex recognition and unwinding by DDX3X - the RNA-bound CLOSED state of the two RecA lobes."),
 ("34056415","B","C-terminally truncated DDX3X with RNA and nucleotide substrates: how ligand occupancy sets the inter-lobe arrangement."),
 ("42497113","A","DDX3X syndrome mutations LOCK DDX3X-RNA conformational states - pathogenic variants acting by trapping one state. 2026."),
],
}

# the four JAK reference papers, pinned exactly
JAKREF = [
 ("24918548","Shan / D. E. Shaw Research, JAK2 JH2-JH1","MD-derived model of the pseudokinase-kinase autoinhibitory interface; nearly all activating disease mutations map to it."),
 ("biorxiv-727727","Ayaz / D. E. Shaw Research, FULL-LENGTH JAK2","Structural models of full-length JAK2 in active AND inactive forms from long-timescale MD - the four-domain arrangement, i.e. exactly our open/closed sense."),
 ("24843152","Lupardus, experimental TYK2","The 2.8 A JH2-JH1 crystal: the only experimental closed inter-domain state in the family."),
 ("35271300","Glassman, experimental full-length JAK","Cryo-EM of a JAK-cytokine-receptor complex: autoinhibited module and activated dimer."),
]

out = {}
allp = [p for v in SET.values() for p,_,_ in v]
cit = {r["pmid"]: r for r in summ(sorted(set(allp + [p for p,_,_ in JAKREF if p.isdigit()])))}
for acc, lst in SET.items():
    rows = []
    for pmid, tier, note in lst:
        c = cit.get(pmid)
        if not c: print("MISSING", pmid, file=sys.stderr); continue
        rows.append(dict(pmid=pmid, tier=tier, note=note, title=c["title"], j=c["j"],
                         date=c["date"], vol=c["vol"], pages=c["pages"], doi=c["doi"],
                         authors=c["authors"]))
    out[acc] = rows
out["_jakref"] = [dict(pmid=p, label=l, note=n,
                       **({k: cit[p][k] for k in ("title","j","date","vol","pages","doi","authors")} if p in cit else {}))
                  for p, l, n in JAKREF]
json.dump(out, open("/Users/chervov/top10/conf_papers.json","w"), indent=1)
print("conf_papers.json written:", {k: len(v) for k, v in out.items()})
