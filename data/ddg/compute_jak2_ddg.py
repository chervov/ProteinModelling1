#!/usr/bin/env python3
"""
compute_jak2_ddg.py — DeltaDeltaG for a list of JAK2 (UniProt O60674) missense variants.

WHAT THIS DOES
  1. Fetches the canonical JAK2 sequence from UniProt and VERIFIES every variant's
     wild-type residue against it. A mismatch is reported, never silently "fixed".
  2. Looks each variant up in two precomputed saturation-mutagenesis tables:
       - ThermoMPNN  (external_data/thermompnn_jak_src.csv)  -> ddG_pred
       - ProtVar FoldX v5.0 on AlphaFold2 (external_data/protvar_foldx_jak_src.csv) -> foldx_ddg
     Both already contain the COMPLETE 1132 x 19 = 21,508 JAK2 substitution set, so no
     new inference is required. Recompute from scratch only if you change the structure.
  3. Places each variant in the percentile of JAK2's own 21,508-variant distribution,
     which is the only way to say whether a ddG is large *for this protein*.

SIGN CONVENTION
  Positive = DESTABILISING in both tables (verified empirically, not assumed).

INTERPRETATION FLOOR -- read before quoting any single number
  * +-0.5 kcal/mol is the experimental noise floor for ddG measurements.
  * +-0.69 kcal/mol is ThermoMPNN's own measured antisymmetry bias on Ssym
    (mean delta = ddG(A->B) + ddG(B->A), which thermodynamics requires to be 0).
  A prediction smaller than these is not interpretable, and its SIGN is meaningless.

USAGE
  python compute_jak2_ddg.py --variants T108A,Y317H,...  [--out results.csv]
  python compute_jak2_ddg.py --variants-file my_variants.txt
"""
import argparse, io, os, sys
import pandas as pd, numpy as np, requests

ACC = "O60674"
RAW = "https://raw.githubusercontent.com/chervov/ProteinModelling1/main/external_data"
NOISE_FLOOR, ANTISYM_BIAS = 0.5, 0.69

def uniprot(acc=ACC):
    r = requests.get(f"https://rest.uniprot.org/uniprotkb/{acc}.json", timeout=120); r.raise_for_status()
    j = r.json()
    doms = [(f["description"], f["location"]["start"]["value"], f["location"]["end"]["value"])
            for f in j["features"] if f["type"] == "Domain"]
    return j["sequence"]["value"], doms

def load(name):
    p = f"external_data/{name}"
    if os.path.exists(p):
        return pd.read_csv(p, low_memory=False)
    r = requests.get(f"{RAW}/{name}", timeout=600); r.raise_for_status()
    return pd.read_csv(io.StringIO(r.text), low_memory=False)

def parse(v):
    v = v.strip().upper()
    return v[0], int(v[1:-1]), v[-1]

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--variants"); ap.add_argument("--variants-file")
    ap.add_argument("--out", default="jak2_ddg_results.csv")
    a = ap.parse_args()
    if a.variants_file:
        vars_ = [x for x in open(a.variants_file).read().replace(",", " ").split() if x]
    elif a.variants:
        vars_ = [x for x in a.variants.replace(",", " ").split() if x]
    else:
        sys.exit("supply --variants or --variants-file")

    seq, doms = uniprot()
    tm = load("thermompnn_jak_src.csv"); tm = tm[tm.uniprot == ACC]
    pv = load("protvar_foldx_jak_src.csv"); pv = pv[pv.uniprot_accession == ACC]
    bg = tm.ddG_pred.dropna()
    tmk = tm.set_index(["new_position", "wildtype", "mutation"]).ddG_pred
    pvk = pv.set_index(["uniprot_position", "wild_type", "mutated_type"]).foldx_ddg

    rows = []
    for v in vars_:
        wt, pos, mt = parse(v)
        obs = seq[pos-1] if 1 <= pos <= len(seq) else None
        rec = dict(variant=v, wt=wt, pos=pos, mt=mt, uniprot_residue=obs,
                   domain=next((d for d, s, e in doms if s <= pos <= e), "-"), note="")
        if mt == "X":
            rec["note"] = "nonsense (stop) - no folded mutant state, ddG undefined"
            rows.append(rec); continue
        if obs != wt:
            hint = f"{obs}{pos}{wt}" if obs == mt else f"{obs}{pos}{mt}"
            rec["note"] = (f"WILD-TYPE MISMATCH: position {pos} is {obs} in {ACC}, not {wt}. "
                           f"Check numbering/isoform; {hint} may be intended "
                           f"(wt/mut transposed)." if obs == mt else
                           f"WILD-TYPE MISMATCH: position {pos} is {obs} in {ACC}, not {wt}. "
                           f"Check numbering/isoform; {hint} may be intended.")
            rows.append(rec); continue
        k = (pos, wt, mt)
        tv = float(tmk.get(k)) if k in tmk.index else None
        fv = float(pvk.get(k)) if k in pvk.index else None
        rec["thermompnn"] = tv; rec["foldx"] = fv
        if tv is not None:
            rec["pct_in_JAK2"] = round(float((bg < tv).mean()*100), 1)
            rec["below_noise_floor"] = abs(tv) < NOISE_FLOOR
            rec["below_antisym_bias"] = abs(tv) < ANTISYM_BIAS
        if fv is None:
            rec["note"] = (rec["note"] + " no FoldX row (ProtVar omits some low-confidence "
                                        "positions despite its README)").strip()
        rows.append(rec)

    R = pd.DataFrame(rows)
    R.to_csv(a.out, index=False)
    print(R.to_string(index=False))
    ok = R[R.get("thermompnn").notna()] if "thermompnn" in R else R.iloc[:0]
    if len(ok):
        print(f"\nJAK2 background median {bg.median():.2f} kcal/mol over {len(bg):,} variants")
        print(f"these variants: median {ok.thermompnn.median():.2f}, "
              f"median percentile {ok.pct_in_JAK2.median():.0f}")
        print(f"inside noise floor: {ok.below_noise_floor.mean():.0%}")

if __name__ == "__main__":
    main()
