"""FoldX ddG for JAK3, from ProtVar - with a fallback while the EBI host is unreachable.

This stands in for the paper's "MutFunc score", as the JAK1 directory also did. mutfunc serves
the *same* FoldX number - verified bit-for-bit in `JAK1/clustering/build_foldx_jak1_info.md` 1b -
but at roughly 8% coverage against ProtVar's 94.6%, so ProtVar is the source and mutfunc the
fallback of last resort. See build_foldx_jak3_info.md.

TWO ROUTES, tried in order:

  1. STREAM FROM SOURCE - https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/
     2025.02.10_foldx_energy.csv.gz, 1.5 GB, 208,792,558 rows, sorted by accession, so the
     stream stops once past the target. This is the route that works for an arbitrary protein.

  2. COMMITTED EXTRACT - external_data/protvar_foldx_jak_src.csv, pulled from that same file on
     28 October 2026 when the host was reachable. Identical values; it is an extract, not a
     different dataset.

As of 3 November 2026 ftp.ebi.ac.uk times out from this sandbox (www.ebi.ac.uk is fine), so
route 2 runs. Nothing else changes when the host returns.

    python3 build_foldx.py              # try source, fall back
    python3 build_foldx.py --source     # source only, fail loudly if unreachable
    python3 build_foldx.py --local      # extract only, skip the network attempt

Writes jak3_foldx.csv.
"""
import csv
import gzip
import pathlib
import sys
import time
import urllib.request

HERE = pathlib.Path(__file__).parent
ACC = "P52333"
URL = ("https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/"
       "2025.02.10_foldx_energy.csv.gz")
EXTRACT = HERE / ".." / ".." / "external_data" / "protvar_foldx_jak_src.csv"
TIMEOUT = 30


def from_source(acc):
    """Stream the sorted 1.5 GB archive, keep `acc`, stop once past it."""
    req = urllib.request.Request(URL, headers={"User-Agent": "research-script"})
    found, scanned, t0 = {}, 0, time.time()
    with urllib.request.urlopen(req, timeout=TIMEOUT) as fh:
        for line in gzip.GzipFile(fileobj=fh):
            s = line.decode(errors="replace").rstrip("\n")
            if s.startswith("uniprot_accession"):
                continue
            scanned += 1
            f = s.split(",")
            if f[0] == acc:
                found[f"{f[4]}{f[1]}{f[5]}"] = (float(f[6]), float(f[7]))
            elif found:
                break
    print(f"  streamed {scanned:,} rows in {time.time()-t0:.0f}s, stopped past {acc}")
    return found


def from_extract(acc):
    path = EXTRACT.resolve()
    if not path.exists():
        sys.exit(f"extract not found at {path}")
    rows = [r for r in csv.DictReader(open(path)) if r["uniprot_accession"] == acc]
    print(f"  read {path.name}: {len(rows):,} rows for {acc} "
          f"(extracted from the same archive, 2025.02.10)")
    return {f"{r['wild_type']}{r['uniprot_position']}{r['mutated_type']}":
            (float(r["foldx_ddg"]), float(r["plddt"])) for r in rows}


def main():
    only_src = "--source" in sys.argv
    only_loc = "--local" in sys.argv
    seq = (HERE / f"JAK3_{ACC}_1124aa.txt").read_text().splitlines()[1]
    print(f"JAK3 {ACC}, {len(seq)} aa")

    fx, route = None, None
    if not only_loc:
        print(f"route 1: streaming ProtVar from ftp.ebi.ac.uk (1.5 GB, sorted)")
        try:
            fx, route = from_source(ACC), "EBI stream (from source)"
        except Exception as exc:
            print(f"  UNREACHABLE: {type(exc).__name__}: {str(exc)[:90]}")
            if only_src:
                sys.exit("  --source given, so not falling back")
            print("  falling back to the committed extract")
    if fx is None:
        fx, route = from_extract(ACC), "committed extract (same archive, 2025.02.10)"

    bad = [v for v in fx if not (1 <= int(v[1:-1]) <= len(seq))
           or seq[int(v[1:-1]) - 1] != v[0]]
    if bad:
        sys.exit(f"wild-type mismatch on {len(bad)} rows, first {bad[:3]}")
    print(f"  wild type agrees with the pinned sequence on all {len(fx):,} rows")

    universe = [r["variant"] for r in csv.DictReader(open(HERE / "jak3_variant_universe.csv"))]
    out = HERE / "jak3_foldx.csv"
    n = 0
    with open(out, "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["index", "variant", "wt", "pos", "alt", "foldx", "plddt", "source"])
        for i, v in enumerate(universe, 1):
            hit = fx.get(v)
            n += hit is not None
            w.writerow([i, v, v[0], v[1:-1], v[-1],
                        "" if not hit else f"{hit[0]:.4f}",
                        "" if not hit else f"{hit[1]:.2f}",
                        "" if not hit else route.split()[0]])
    vals = [h[0] for h in fx.values()]
    miss = sorted({int(v[1:-1]) for v in universe if v not in fx})
    print(f"\nwrote {out.name}: {len(universe):,} rows, {n:,} populated "
          f"({100*n/len(universe):.1f}%)  via {route}")
    print(f"  range {min(vals):.2f} .. {max(vals):.2f}; POSITIVE = destabilising "
          f"(opposite to this project's Rosetta ddG)")
    lo = sum(1 for h in fx.values() if h[1] < 70)
    print(f"  pLDDT < 70 on {lo:,} rows ({100*lo/len(fx):.1f}%) - ProtVar no longer filters these")
    print(f"  missing at {len(miss)} positions, range {min(miss)}-{max(miss)}; "
          f"1-38 is AlphaFold's low-confidence N-terminus, which ProtVar trims")


if __name__ == "__main__":
    main()
