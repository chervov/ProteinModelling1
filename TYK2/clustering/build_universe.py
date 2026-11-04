"""The TYK2 variant universe: every possible single amino-acid substitution, in canonical order.

Pins the sequence (UniProt P29597) and enumerates all 19 substitutions at each of its 1,187
positions, giving 22,553 variants. Self-substitutions are NOT included - unlike the JAK1
directory, which kept them only to match Dataset EV1 row-for-row. There is no published TYK2
clustering to match, so that convention buys nothing here.

ORDER: by position ascending, then by the substituted-in residue alphabetically. That is the
natural order for everything positional - plots along the protein, grouping by domain - and is
what ProtVar ships. It is NOT what the other sources use: Liao & Lehner (AlphaMissense, ESM-1v,
ThermoMPNN) ships a lexicographic sort of the variant string, which puts position 1022 before
1034 before 110 before 39; dbNSFP has no stable order at all, being keyed on nucleotide variants
rather than amino-acid substitutions. Every join in this directory is therefore on `variant`,
never on row position.

Writes TYK2_P29597.fasta, TYK2_P29597_1187aa.txt, tyk2_sequence_info.json,
tyk2_variant_universe.csv.
"""
import hashlib
import json
import pathlib
import urllib.request

HERE = pathlib.Path(__file__).parent
ACC = "P29597"
AAS = "ACDEFGHIKLMNPQRSTVWY"


def fetch_uniprot():
    fasta = urllib.request.urlopen(
        f"https://rest.uniprot.org/uniprotkb/{ACC}.fasta", timeout=120).read().decode()
    meta = json.load(urllib.request.urlopen(
        f"https://rest.uniprot.org/uniprotkb/{ACC}.json", timeout=120))
    return fasta, meta


def main():
    fasta, meta = fetch_uniprot()
    (HERE / f"TYK2_{ACC}.fasta").write_text(fasta)
    seq = "".join(l.strip() for l in fasta.splitlines() if not l.startswith(">"))

    # plain text as well as FASTA: one comment line, then the whole sequence unwrapped on a
    # single line, so it can be pasted into a web form or read with one readline(). The length
    # is in the filename too, which makes a truncated copy obvious at a glance.
    plain = HERE / f"TYK2_{ACC}_{len(seq)}aa.txt"
    plain.write_text(f"# UniProt {ACC} TYK2_HUMAN | {len(seq)} aa | "
                     f"md5 {hashlib.md5(seq.encode()).hexdigest()}\n{seq}\n")

    info = {
        "accession": ACC,
        "entry_name": meta.get("uniProtkbId"),
        "protein": meta["proteinDescription"]["recommendedName"]["fullName"]["value"],
        "length": len(seq),
        "uniprot_entry_version": meta["entryAudit"]["entryVersion"],
        "sequence_version": meta["entryAudit"]["sequenceVersion"],
        "last_modified": meta["entryAudit"]["lastSequenceUpdateDate"],
        "md5": hashlib.md5(seq.encode()).hexdigest(),
        "sha256": hashlib.sha256(seq.encode()).hexdigest(),
        "domains": [[f["description"], f["location"]["start"]["value"],
                     f["location"]["end"]["value"]]
                    for f in meta["features"] if f["type"] == "Domain"],
    }
    json.dump(info, open(HERE / "tyk2_sequence_info.json", "w"), indent=1)
    print(f"wrote {plain.name}: comment line + {len(seq)} residues on one line")
    print(f"{info['entry_name']} ({ACC}), {len(seq)} aa, "
          f"entry version {info['uniprot_entry_version']}, md5 {info['md5'][:12]}...")
    for nm, s, e in info["domains"]:
        print(f"    {nm:<22}{s:>6}-{e}")

    rows = [(f"{seq[p - 1]}{p}{a}")
            for p in range(1, len(seq) + 1)
            for a in AAS if a != seq[p - 1]]
    assert len(rows) == 19 * len(seq), f"expected {19*len(seq)}, got {len(rows)}"

    out = HERE / "tyk2_variant_universe.csv"
    with open(out, "w", newline="") as fh:
        fh.write("index,variant\n")
        for i, v in enumerate(rows, 1):
            fh.write(f"{i},{v}\n")
    print(f"\nwrote {out.name}: {len(rows):,} variants = 19 x {len(seq):,} positions")
    print(f"  first 10 : {', '.join(rows[:10])}")
    print(f"  last 3   : {', '.join(rows[-3:])}")

    # the checks that make the file trustworthy
    assert all(seq[int(v[1:-1]) - 1] == v[0] for v in rows), "wild type mismatch"
    assert len(set(rows)) == len(rows), "duplicate variant"
    assert not any(v[0] == v[-1] for v in rows), "self-substitution present"
    print("  checks: wild type matches the sequence at every row, no duplicates, "
          "no self-substitutions")


if __name__ == "__main__":
    main()
