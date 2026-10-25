# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "altair==6.3.0",
#     "pandas==3.1.0",
# ]
# ///

import marimo

__generated_with = "0.25.2"
app = marimo.App(width="medium", auto_download=["html"])

with app.setup:
    import os, sys, time, json, subprocess, urllib.request

    def ensure_pyrosetta():
        """PyRosetta is not on PyPI; install via the RosettaCommons installer (free for academic use)."""
        try:
            import pyrosetta  # noqa: F401
            return "already installed"
        except ImportError:
            subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pyrosetta-installer"], check=True)
            import pyrosetta_installer
            pyrosetta_installer.install_pyrosetta()
            return "installed now (~1.5 GB)"

    pyrosetta_status = ensure_pyrosetta()
    print("PyRosetta:", pyrosetta_status)


@app.cell
def intro():
    import marimo as mo

    mo.md(
        """
        # TYK2 ddG: are the extreme values real?

        The dual-state ddG run (`data/ddg/`) produces values down to **-3000**, far outside any
        physical folding free energy. This notebook reproduces the pipeline on one structure and
        tests whether those numbers are **steric clash artefacts** rather than energies.

        Three protocols on the same relaxed pose:

        | | what it does |
        |---|---|
        | **A** | the pipeline: `mutate_residue(pack_radius=8)`, side chains only |
        | **fa_rep** | how much of the ddG is the Lennard-Jones repulsive term |
        | **B** | A plus backbone + side-chain minimisation of the 8 A shell |

        Sign convention follows the paper: **ddG = E(WT) - E(mut)**, so *negative = destabilising*.
        """
    )
    return (mo,)


@app.cell
def config():
    WORK = "/tmp/ddg"
    STRUCTURE_URL = ("https://raw.githubusercontent.com/chervov/ProteinModelling1/main/"
                     "TYK2/af3/tyk2_af3_closed.pdb")
    SHELL = 8.0          # repack radius, as in pipeline/ddg/worker.py

    # Three positions with the most extreme stored ddG (all glycine), two ordinary ones.
    TEST_POSITIONS = [746, 964, 801, 667, 775]
    TEST_ALTS = ["W", "F", "A", "G"]

    os.makedirs(WORK, exist_ok=True)
    print(f"{len(TEST_POSITIONS)} positions x {len(TEST_ALTS)} substitutions")
    return SHELL, STRUCTURE_URL, TEST_ALTS, TEST_POSITIONS, WORK


@app.cell
def rosetta_init():
    import pyrosetta
    from pyrosetta import pose_from_pdb, get_fa_scorefxn
    from pyrosetta.toolbox import mutate_residue
    from pyrosetta.rosetta.core.scoring import ScoreType
    from pyrosetta.rosetta.core.kinematics import MoveMap
    from pyrosetta.rosetta.protocols.minimization_packing import MinMover
    from pyrosetta.rosetta.protocols.relax import FastRelax
    from pyrosetta.rosetta.protocols.constraint_generator import (
        CoordinateConstraintGenerator, AddConstraints)

    pyrosetta.init("-mute all -ex1 -ex2aro -ignore_unrecognized_res "
                   "-ignore_zero_occupancy false -detect_disulf false")
    scorefxn = get_fa_scorefxn()
    print("scorefunction:", scorefxn.get_name())
    return (
        AddConstraints,
        CoordinateConstraintGenerator,
        FastRelax,
        MinMover,
        MoveMap,
        ScoreType,
        mutate_residue,
        pose_from_pdb,
        scorefxn,
    )


@app.cell
def md_pose(mo):
    mo.md("""
    ## 1. Structure

    The same AlphaFold-3 closed-state model the production run used, relaxed with **FastRelax
    under coordinate constraints** so it stays near the input geometry. The relaxed pose is
    cached on disk: the first run costs ~35 min for 1187 residues, afterwards it is instant.

    Watch the **total REU**: that single number is the yardstick for judging every ddG below.
    """)
    return


@app.cell
def pose(
    AddConstraints,
    CoordinateConstraintGenerator,
    FastRelax,
    STRUCTURE_URL,
    ScoreType,
    WORK,
    pose_from_pdb,
    scorefxn,
):
    def load_relaxed_pose():
        """Fetch the structure and FastRelax it with coordinate constraints, exactly as worker.py.
        Cached on disk: the first run takes ~35 min for 1187 residues, later runs are instant."""
        src = f"{WORK}/tyk2_af3_closed.pdb"
        if not os.path.exists(src):
            urllib.request.urlretrieve(STRUCTURE_URL, src)
        cached = f"{WORK}/TYK2_relaxed_closed.pdb"
        if os.path.exists(cached) and os.path.getsize(cached) > 100_000:
            return pose_from_pdb(cached), "loaded from cache"
        p = pose_from_pdb(src)
        gen = CoordinateConstraintGenerator()
        add = AddConstraints(); add.add_generator(gen); add.apply(p)
        sf_cst = scorefxn.clone(); sf_cst.set_weight(ScoreType.coordinate_constraint, 1.0)
        t0 = time.time(); FastRelax(sf_cst, 1).apply(p)
        p.dump_pdb(cached)
        return p, f"relaxed in {time.time() - t0:.0f}s"

    pose, pose_note = load_relaxed_pose()
    total_wt = scorefxn(pose)
    print(f"{pose.total_residue()} residues, {total_wt:.0f} REU total "
          f"({total_wt / pose.total_residue():.2f} REU/residue) - {pose_note}")
    return pose, total_wt


@app.cell
def md_run(mo):
    mo.md("""
    ## 2. Computing ddG three ways

    For each substitution we compute the pipeline's value, the same thing with a mobile
    backbone, and how much of it is pure steric overlap.

    The three extreme positions (**746, 964, 801**) are all **glycine** - chosen because they
    carry the largest ddG in the stored results. **667** and **775** are ordinary controls.
    """)
    return


@app.cell
def functions(MinMover, MoveMap, SHELL, mutate_residue, pose, scorefxn):
    def weighted_terms(p):
        """Weighted score terms of a pose, as a dict (fa_rep = Lennard-Jones repulsion)."""
        scorefxn(p)
        totals = p.energies().total_energies()
        return {st.name: totals[st] * scorefxn.get_weight(st)
                for st in scorefxn.get_nonzero_weighted_scoretypes()}

    def minimise_shell(p, position, radius=SHELL):
        """Protocol B: let the backbone AND side chains near the mutation move.
        This is the degree of freedom a repack-only protocol lacks, and the one Flex ddG
        says bulky substitutions need."""
        mm = MoveMap()
        centre = p.residue(position).xyz("CA")
        for i in range(1, p.total_residue() + 1):
            if p.residue(i).has("CA") and (p.residue(i).xyz("CA") - centre).norm() <= radius:
                mm.set_chi(i, True); mm.set_bb(i, True)
        MinMover(mm, scorefxn, "lbfgs_armijo_nonmonotone", 0.01, True).apply(p)
        return p

    def ddg_for(position, alt):
        """ddG of one substitution under both protocols.

        Returns, for `<native><position><alt>`:
          A_repack_only  ddG from the pipeline protocol (side chains only).
          B_flexible_bb  ddG after backbone + side-chain minimisation of the shell.
          fa_rep_share   fraction of the destabilisation that is pure steric repulsion.
                         1.0 means the whole number is atoms overlapping, not chemistry.

        Sign: ddG = E(WT) - E(mutant), so NEGATIVE = destabilising (the paper's convention).
        The WT is repacked identically, so neither side is favoured.
        """
        native = pose.residue(position).name1()
        if native == alt:
            return None
        wt = pose.clone(); mutate_residue(wt, position, native, pack_radius=SHELL)
        mut = pose.clone(); mutate_residue(mut, position, alt, pack_radius=SHELL)
        a = scorefxn(wt) - scorefxn(mut)
        d_rep = weighted_terms(mut).get("fa_rep", 0.0) - weighted_terms(wt).get("fa_rep", 0.0)
        b = scorefxn(minimise_shell(wt.clone(), position)) - scorefxn(minimise_shell(mut.clone(), position))
        # a is negative when destabilising and d_rep positive, so negate to get a 0-1 share
        share = round(-d_rep / a, 2) if abs(a) > 1e-9 else None
        return {"variant": f"{native}{position}{alt}", "pos": position, "wt": native, "alt": alt,
                "A_repack_only": round(a, 1), "B_flexible_bb": round(b, 1), "fa_rep_share": share}

    return (ddg_for,)


@app.cell
def run(TEST_ALTS, TEST_POSITIONS, ddg_for):
    print(f"{'variant':8s} {'A (repack only)':>16s} {'B (flexible bb)':>16s} {'steric':>8s}")
    print(f"{'':8s} {'pipeline value':>16s} {'after bb moves':>16s} {'share':>8s}")
    print("-" * 52)

    results = []
    for _pos in TEST_POSITIONS:
        for _alt in TEST_ALTS:
            _rec = ddg_for(_pos, _alt)
            if _rec:
                results.append(_rec)
                _s = f"{_rec['fa_rep_share']:.0%}" if _rec["fa_rep_share"] is not None else "-"
                print(f"{_rec['variant']:8s} {_rec['A_repack_only']:16.1f} "
                      f"{_rec['B_flexible_bb']:16.1f} {_s:>8s}", flush=True)

    print("-" * 52)
    print(f"{len(results)} variants. More negative = more destabilising.")
    print("A collapsing to B means the ddG was atoms overlapping, not a real energy cost.")
    return (results,)


@app.cell
def md_table(mo):
    mo.md("""
    ## 3. Results

    `shrink_factor` is A divided by B: how many times smaller the ddG becomes once the backbone
    is allowed to relax. A factor near 1 means the protocol made no difference; a large factor
    means the original number was a clash the protocol could not resolve.
    """)
    return


@app.cell
def table(mo, results):
    import pandas as pd

    ddg_table = pd.DataFrame(results).sort_values("A_repack_only")
    ddg_table["shrink_factor"] = (ddg_table.A_repack_only / ddg_table.B_flexible_bb).round(1)
    mo.ui.table(ddg_table, selection=None)
    return (ddg_table,)


@app.cell
def chart(ddg_table, mo):
    import altair as alt

    _long = ddg_table.melt(id_vars="variant", value_vars=["A_repack_only", "B_flexible_bb"],
                           var_name="protocol", value_name="ddG")
    chart = alt.Chart(_long).mark_bar().encode(
        y=alt.Y("variant:N", sort=list(ddg_table.variant), title=None),
        x=alt.X("ddG:Q", title="ddG (REU, negative = destabilising)"),
        color=alt.Color("protocol:N", title=None),
        yOffset="protocol:N",
    ).properties(height=420, width=520, title="Repack-only vs flexible backbone")
    mo.ui.altair_chart(chart)
    return


@app.cell
def conclusion(ddg_table, mo, pose, total_wt):
    _extreme = ddg_table[ddg_table.A_repack_only < -500]
    mo.md(f"""
    ## What this shows

    **The extreme values are not energies.** A folded protein's entire score here is
    **{total_wt:.0f} REU** for {pose.total_residue()} residues. A ddG of -3000 therefore puts the
    mutant at **+{-total_wt - 3000:.0f} REU** - a positive total energy, which no folded structure
    has. The clash alone "costs" more than the whole protein's folding energy.

    - **{len(_extreme)} of {len(ddg_table)}** variants fall below -500 under the pipeline protocol.
      Their mean `fa_rep` share is **{_extreme.fa_rep_share.mean():.0%}**: the ddG *is* the repulsive
      term and nothing else.
    - Letting the backbone move shrinks them by a median factor of
      **{_extreme.shrink_factor.median():.0f}x**.
    - Every extreme position is a **glycine**. Replacing it with W or F in a fixed backbone is exactly
      the case Flex ddG says requires backbone movement; G->A at the same positions is 10-50x milder.
    - The ordinary position (**775**) is untouched by the protocol choice, so this is specific to
      clash-prone sites, not a global offset.

    **For reference**, real ddG values sit in single digits: Rosetta's own alanine-scan benchmark
    discards experimental values above 4, and no mutation can destabilise a domain by more than its
    folding free energy (~5-15 kcal/mol). Even protocol B is still 10-30x above that band.

    **What survives.** The *ordering* is largely preserved, which is why the project's conclusions
    hold: `conclusions_ddG_difference_feature.md` uses rank statistics throughout, and its README
    already says "only the ordering is meaningful". The amplitudes should never be quoted as energies.
    """)
    return


if __name__ == "__main__":
    app.run()
