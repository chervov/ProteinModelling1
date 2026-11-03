"""One entry point for the whole JAK1 clustering report.

Runs the six steps in the only order that works, from a clean checkout:

    build_gnomad.py   -> jak1_gnomad.csv, jak1_gnomad.json   (network: gnomAD GraphQL)
    analyse.py        -> stats.json + X/pap/reb/ing/gaf/ncov .npy
    derive_stats.py   -> EXTENDS stats.json
    plots*.py         -> figs/*.png
    build_html.py     -> jak1_clustering_analysis.html

The order is not cosmetic. analyse.py REWRITES stats.json from scratch, so derive_stats.py
must follow it, and build_html.py needs the keys both of them write. Running build_html.py
after a bare analyse.py raises KeyError('auc_subsets') - which is the failure this script
exists to prevent.

    python3 build_report.py            # everything
    python3 build_report.py --no-fetch # skip the network step, reuse jak1_gnomad.csv
"""
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).parent
STEPS = [
    ("build_gnomad.py", "fetch gnomAD r4 and write the feature file", True),
    ("analyse.py",      "AUC, enrichment, and the cached arrays",     False),
    ("derive_stats.py", "stratified ORs, ARI by subset, disagreement tables", False),
    ("plots.py",        "histograms, correlation, AUC, gnomAD enrichment",    False),
    ("plots2.py",       "disagreement, stratified ARI, along the protein",    False),
    ("plots3.py",       "AUC on matched subsets",                     False),
    ("plots4.py",       "pooled vs stratified OR, external ARI",      False),
    ("build_html.py",   "assemble the report with figures inlined",   False),
]


def main():
    skip_fetch = "--no-fetch" in sys.argv
    for script, what, needs_network in STEPS:
        if needs_network and skip_fetch:
            print(f"-- SKIPPED {script} ({what})")
            continue
        print(f"\n== {script}  --  {what}")
        t = time.time()
        r = subprocess.run([sys.executable, str(HERE / script)], cwd=HERE)
        if r.returncode:
            sys.exit(f"FAILED at {script} (exit {r.returncode}); "
                     f"later steps depend on it, so nothing further was run.")
        print(f"   ok, {time.time() - t:.1f}s")
    out = HERE / "jak1_clustering_analysis.html"
    print(f"\ndone -> {out.name}, {out.stat().st_size / 1e6:.2f} MB")


if __name__ == "__main__":
    main()
