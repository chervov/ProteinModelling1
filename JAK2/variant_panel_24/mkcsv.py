"""Consolidated table for the 24 JAK2 variants: domains, predictors, clinical/population
databases, and cross-mapping onto the TYK2 4OLI and JAK1 closed/open interfaces."""
import json, csv
T = "/Users/chervov/.claude/jobs/e920d48f/tmp"
J2 = json.load(open(T+"/j2/JAK2.json")); TY = json.load(open(T+"/j2/TYK2.json")); J1 = json.load(open(T+"/j2/JAK1.json"))
mp = json.load(open(T+"/j2/map.json")); IF = json.load(open(T+"/j2/ifaces.json"))
J2IF = json.load(open(T+"/j2/jak2_ifaces.json")); XDB = json.load(open(T+"/j2/extra_db.json"))
SH = json.load(open(T+"/j2/shan_ifaces.json"))
BIG = {r['Variant']: r for r in csv.DictReader(open(T+"/jak2/jak2_variants_inf_predict_ext.csv"))
       if r['Variant'] and not r['Variant'].startswith('SECTION')}

# predictors fetched from dbNSFP for the five rows our JAK2 table does not carry
XPRED = {
 "H345L": dict(am=0.2062, amc="likely benign",    revel=0.151, cadd=19.44, sift=0.135, pp2=0.036, metarnn=0.3184, vest4=0.636, esm1b=-9.094,  eve=0.2107),
 "H608N": dict(am=0.4878, amc="ambiguous",        revel=0.344, cadd=29.9,  sift=0.007, pp2=0.965, metarnn=0.7901, vest4=0.910, esm1b=-8.919,  eve=0.7724),
 "L611S": dict(am=0.7743, amc="likely pathogenic",revel=0.664, cadd=28.6,  sift=0.003, pp2=0.991, metarnn=0.8323, vest4=0.884, esm1b=-10.913, eve=0.6591),
 "F240V": dict(am=0.7148, amc="likely pathogenic",revel=0.154, cadd=23.5,  sift=0.339, pp2=0.020, metarnn=0.5114, vest4=0.786, esm1b=-9.664,  eve=0.3056),
 "R426X": dict(am="",     amc="nonsense (no missense predictor applies)",
               revel="",  cadd=42.0,  sift="",    pp2="",    metarnn="",     vest4=0.979, esm1b="",      eve=""),
}
NOTE = {
 "R683S": "LISTED AS R755S, WHICH CANNOT EXIST: position 755 of O60674 is already Ser (GDKPL-S755-ALDSQ); "
          "nearest Arg are 761 and 769. R683S assumed - the canonical pseudokinase GOF of Down-syndrome B-ALL.",
 "R426X": "Stop-gain. dbNSFP indexes missense only, so most predictors are undefined; CADD 42 is the usable signal.",
 "R1063H":"Listed as a prior GOF but ClinVar calls it Benign/Likely benign with 8,630 gnomAD alleles and 46 "
          "homozygotes - a common polymorphism. Worth re-checking the source.",
 "V617F": "gnomAD AF 2.93e-4 with 17 homozygotes reflects somatic clonal haematopoiesis leaking into gnomAD, "
          "not germline tolerance.",
 "H380Y": "Last residue of the FERM domain (380/380).",
}
GROUPS = [("GROUP 1 - GOF VARIANTS PREVIOUSLY REPORTED",
           ["T108A","Y317H","H345L","H608N","L611S","V617I","V617F","V625F","E846D","R867Q","T875N","R683S","R938Q","R1063H"]),
          ("GROUP 2 - VARIANTS IDENTIFIED IN THIS STUDY",
           ["P37A","F240V","H380Y","R426X","C427R","G571R","V578I","L805I","I1065T","V1110E"])]

oli  = set(IF["TYK2 4OLI"]["jh2"]) | set(IF["TYK2 4OLI"]["jh1"])
olimod = set(IF["TYK2 4OLI"]["modelled"])
j1c  = set(IF["JAK1 ma-l9b1f (Jeanpierre closed)"]["jh2"]) | set(IF["JAK1 ma-l9b1f (Jeanpierre closed)"]["jh1"])
j1o  = set(IF["JAK1 ma-a1sai (Jeanpierre open)"]["jh2"])   | set(IF["JAK1 ma-a1sai (Jeanpierre open)"]["jh1"])
afj  = set(J2IF["AlphaFold JAK2"]["jh2"]) | set(J2IF["AlphaFold JAK2"]["jh1"])
ocj  = set(J2IF["our JAK2 closed"]["jh2"]) | set(J2IF["our JAK2 closed"]["jh1"])
shan = set(SH["Shan JAK2"]["jh2"]) | set(SH["Shan JAK2"]["jh1"])          # native JAK2 numbering
shan_mod = set(range(520, 1132))
shj1 = set(SH["Shan JAK1"]["jh2"]) | set(SH["Shan JAK1"]["jh1"])          # JAK1 numbering
rev  = {g: {v: int(k) for k, v in mp[g].items()} for g in ("TYK2","JAK1")}
ALLIF_J2 = ({rev["TYK2"][p] for p in oli if p in rev["TYK2"]} |
            {rev["JAK1"][p] for p in j1c if p in rev["JAK1"]} |
            {rev["JAK1"][p] for p in shj1 if p in rev["JAK1"]} | shan | afj | ocj)
DOMS = J2["domains"]

COLS = ["Group","Variant","WT","Position","Alt","Consequence","Sequence_validated",
        "Domain","Domain_start","Domain_end","Position_in_domain","Domain_length",
        "AlphaMissense","AlphaMissense_class","REVEL","CADD_phred","SIFT","PolyPhen2_HVAR","MetaRNN",
        "VEST4","ESM1b","EVE","PrimateAI","PROVEAN","MVP","BayesDel_addAF","ClinPred","MutationAssessor",
        "LIST_S2","DEOGEN2","GERP_91mammals","phyloP_100way","MutPred","PhACTboost",
        "ClinVar","ClinVar_review_status","ClinVar_condition","ClinVar_variation_ID",
        "Somatic_clinical_impact","OMIM_allelic_variant",
        "gnomAD_allele_count","gnomAD_AF","gnomAD_homozygotes",
        "cBioPortal_patients","cBioPortal_top_cancer_types","COSMIC","LOVD_entries","LOVD_reported_effect",
        "DECIPHER","CIViC_evidence","DRUG","dbSNP","Seen_in","Conclusions","Brief_evidence","Reference",
        "TYK2_equivalent","TYK2_position","in_4OLI_JH2_JH1_interface",
        "JAK1_equivalent","JAK1_position","in_Jeanpierre_CLOSED_interface","in_Jeanpierre_OPEN_interface",
        "in_Shan_JAK2_model_interface","in_Shan_JAK1_model_interface",
        "in_AlphaFold_JAK2_interface","in_our_JAK2_closed_interface",
        "n_interface_models_hit","n_interface_models_tested","distance_to_nearest_interface_residue","Notes"]

def dominfo(p):
    for nm, s, e in DOMS:
        if s <= p <= e: return nm, s, e, p-s+1, e-s+1
    return "linker/other", "", "", "", ""

rows = []
for gname, lst in GROUPS:
    rows.append({c: "" for c in COLS} | {"Group": "SECTION", "Variant": "SECTION: " + gname})
    for v in lst:
        wt, alt, p = v[0], v[-1], int(v[1:-1])
        b = BIG.get(v, {}); x = XPRED.get(v, {}); xd = XDB.get(v, {})
        g  = lambda k: (b.get(k) or "").strip()
        pv = lambda k, xk: g(k) or (x.get(xk, "") if x else "")
        nm, ds, de, pid, dl = dominfo(p)
        t = mp["TYK2"].get(str(p)); j = mp["JAK1"].get(str(p))
        hits = sum([bool(t and t in oli), bool(j and j in j1c), bool(j and j in shj1),
                    p in shan, p in afj, p in ocj])
        dist = min((abs(q-p) for q in ALLIF_J2), default="")
        yn = lambda c: "yes" if c else "no"
        rows.append({
          "Group": gname.split(" - ")[0], "Variant": v, "WT": wt, "Position": p, "Alt": alt,
          "Consequence": "stop_gained" if alt == "X" else "missense",
          "Sequence_validated": "yes" if J2["seq"][p-1] == wt else f"NO - residue {p} is {J2['seq'][p-1]}",
          "Domain": nm, "Domain_start": ds, "Domain_end": de, "Position_in_domain": pid, "Domain_length": dl,
          "AlphaMissense": pv('AlphaMissense','am'), "AlphaMissense_class": pv('AlphaMissense class','amc'),
          "REVEL": pv('REVEL','revel'), "CADD_phred": pv('CADD phred','cadd'), "SIFT": pv('SIFT','sift'),
          "PolyPhen2_HVAR": pv('PolyPhen-2 HVAR','pp2'), "MetaRNN": pv('MetaRNN','metarnn'),
          "VEST4": pv('dbNSFP vest4.score','vest4'), "ESM1b": pv('ESM1b','esm1b'), "EVE": pv('dbNSFP eve.score','eve'),
          "PrimateAI": g('dbNSFP primateai.score'), "PROVEAN": g('dbNSFP provean.score'),
          "MVP": g('dbNSFP mvp.score'), "BayesDel_addAF": g('dbNSFP bayesdel.add_af.score'),
          "ClinPred": g('dbNSFP clinpred.score'), "MutationAssessor": g('dbNSFP mutationassessor.score'),
          "LIST_S2": g('dbNSFP list-s2.score'), "DEOGEN2": g('dbNSFP deogen2.score'),
          "GERP_91mammals": g('dbNSFP gerp.91_mammals.score'), "phyloP_100way": g('dbNSFP phylop.100way_vertebrate.score'),
          "MutPred": g('dbNSFP mutpred.score'), "PhACTboost": g('dbNSFP phactboost.score'),
          "ClinVar": g('ClinVar') or xd.get("ClinVar","") or ("not in ClinVar" if v in XDB else ""),
          "ClinVar_review_status": g('Review status'), "ClinVar_condition": g('Condition') or xd.get("Condition",""),
          "ClinVar_variation_ID": g('ClinVar variation ID') or xd.get("ClinVar variation ID",""),
          "Somatic_clinical_impact": g('Somatic clinical impact'), "OMIM_allelic_variant": g('OMIM allelic variant'),
          "gnomAD_allele_count": g('gnomAD allele count') or xd.get("gnomAD allele count",""),
          "gnomAD_AF": g('gnomAD AF') or xd.get("gnomAD AF",""), "gnomAD_homozygotes": g('gnomAD homozygotes'),
          "cBioPortal_patients": g('cBioPortal patients'), "cBioPortal_top_cancer_types": g('cBioPortal top cancer types'),
          "COSMIC": ("COSMIC" if "COSMIC" in g('Seen in') else "") or xd.get("COSMIC",""),
          "LOVD_entries": g('LOVD entries'), "LOVD_reported_effect": g('LOVD reported effect'),
          "DECIPHER": g('DECIPHER'), "CIViC_evidence": g('CIViC evidence'), "DRUG": g('DRUG'),
          "dbSNP": xd.get("dbSNP",""), "Seen_in": g('Seen in'), "Conclusions": g('Conclusions'),
          "Brief_evidence": g('Brief evidence'), "Reference": g('Reference'),
          "TYK2_equivalent": f"{TY['seq'][t-1]}{t}" if t else "no aligned residue", "TYK2_position": t or "",
          "in_4OLI_JH2_JH1_interface": ("not modelled in 4OLI" if (t and t not in olimod)
                                        else ("n/a" if not t else yn(t in oli))),
          "JAK1_equivalent": f"{J1['seq'][j-1]}{j}" if j else "no aligned residue", "JAK1_position": j or "",
          "in_Jeanpierre_CLOSED_interface": yn(j and j in j1c) if j else "n/a",
          "in_Jeanpierre_OPEN_interface":   yn(j and j in j1o) if j else "n/a",
          "in_Shan_JAK2_model_interface": (yn(p in shan) if p in shan_mod else "not modelled (Shan covers 520-1131)"),
          "in_Shan_JAK1_model_interface": (yn(j in shj1) if j else "n/a"),
          "in_AlphaFold_JAK2_interface": yn(p in afj), "in_our_JAK2_closed_interface": yn(p in ocj),
          "n_interface_models_hit": hits, "n_interface_models_tested": 6,
          "distance_to_nearest_interface_residue": dist,
          "Notes": NOTE.get(v, "")})

out = "/Users/chervov/homol/JAK2_24_variants_full.csv"
w = csv.DictWriter(open(out, "w", newline=""), fieldnames=COLS)
w.writeheader(); w.writerows(rows)
print(f"wrote {out}")
print(f"  {len(COLS)} columns, {len(rows)} rows ({sum(1 for r in rows if r['Group']=='SECTION')} section headers + 24 variants)")
