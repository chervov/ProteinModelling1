# ddg_build_review — how to install and run every ΔΔG method, on this exact machine

**Audience: another agent working on this same host.** Everything below was verified by running it
on 5–6 November 2026, not recalled. Paths are absolute and real. Where something is gone or
unreachable, that is stated rather than glossed.

Host: macOS (Apple Silicon, arm64), 8 cores, 16 GiB RAM, 274 GiB free on `/`.

---

## 0. Read this first — state of the machine right now

| resource | status | path |
|---|---|---|
| **PyRosetta 2026.39** | **INSTALLED AND WORKING** — do not re-download | `/opt/anaconda3/bin/python` |
| **ProtVar FoldX dump, 1.5 GB** | **ON DISK** — do not re-download | `/Users/chervov/protvar/foldx_energy_2025.02.10.csv.gz` |
| ProtVar JAK extract (89,927 rows) | on disk | `/Users/chervov/protvar/jak_src_foldx.csv` |
| ThermoMPNN JAK source table | on disk, in the repo | `/Users/chervov/ProteinModelling1/external_data/thermompnn_jak_src.csv` |
| Repo working copy, 9.7 GB | granted, read/write | `/Users/chervov/ProteinModelling1` |
| torch 2.14.1, fair-esm 2.0.0, lightning, omegaconf, torchmetrics, openmm, pdbfixer, sklearn | installed | conda env `ddg` |
| mafft, lxml, biopython, gemmi, scipy, pandas, matplotlib | installed | conda env `python` |
| **ThermoMPNN source tree** | **GONE** — must reinstall (§3.1) | — |
| **RaSP source tree** | **GONE** — must reinstall (§3.4) | — |
| **rsalor** | **GONE** — must reinstall (§3.3) | — |
| `~/ddg_jak2`, `~/ddg_jak3`, `~/ddg_overnight` | exist but **sandbox-blocked** | need `request_host_access` |

### 0.1 The persistence rule — the single most important thing here

> **`manage_packages` installs persist. Raw `pip install` from a `bash` cell does not.**

The `python` and `ddg` tool environments resolve to a **workspace-relative venv**
(`./.venv/<env>`, confirmed via `sys.prefix`), and the workspace is deleted after ~6 h idle.
Packages added with the `manage_packages` tool land in `/Users/chervov/.claude-science/conda/envs/<env>/`
and survive; packages added with `pip install` inside a shell land in the workspace venv and are wiped.

That is exactly why `torch` (installed via `manage_packages`) is still here, while `rsalor` and the
agent-env `pyrosetta` (both installed with bare `pip` in a shell) are gone — even though the latter
was a 1.4 GB download.

**Consequence for you:** use `manage_packages` for anything you want to keep. For anything large
that must be built or downloaded, `save_artifacts` a tarball of it immediately.

### 0.2 Sandbox boundaries

`/Users/chervov/*` is blocked at the OS level (`Operation not permitted`) **except** the
`.claude-science` subtree and whatever has been explicitly granted. A grant on
`/Users/chervov` itself **fails** ("Directory could not be accessed"); grants on specific
subdirectories succeed. Grants take effect for **new** kernels only.

```python
request_host_access(host_path="/Users/chervov/ProteinModelling1", mode="ro")   # works
request_host_access(host_path="/Users/chervov/protvar",           mode="ro")   # works
request_host_access(host_path="/Users/chervov",                   mode="ro")   # FAILS
```

---

## 1. PyRosetta — already installed, just use it

**Do not reinstall.** Verified working:

```bash
/opt/anaconda3/bin/python -c "
import pyrosetta; pyrosetta.init('-mute all')
from pyrosetta import pose_from_sequence
sf = pyrosetta.create_score_function('ref2015_cart')
print(sf(pose_from_sequence('AAAAAAAAAA')))"     # -> 30.99 REU, ~1.9 s
```

Version `2026.39+release.49e05e797c`, at
`/opt/anaconda3/lib/python3.13/site-packages/pyrosetta`.

### If you ever do need to reinstall it

The `pyrosetta-installer` PyPI package **stalls silently** — it printed nothing for 50 minutes and
downloaded nothing. Fetch the wheel directly. Apple Silicon needs the **`.m1.`** build; the `.mac.`
builds are x86_64 only and will install but not import.

```bash
D=https://west.rosettacommons.org/pyrosetta/release/release/PyRosetta4.Release.python311.m1.wheel/
W=$(curl -s "$D" | grep -o 'href="pyrosetta-[^"]*\.whl"' | sed 's/href="//;s/"//' | tail -1)
curl -L -o "/tmp/$W" "$D$W"      # 1.4 GB, ~25 min at ~1 MB/s
pip install "/tmp/$W"
```

**Gotcha:** keep the canonical wheel filename. `cp pr.whl` then `pip install /tmp/pr.whl` fails with
`ERROR: Invalid wheel filename (wrong number of parts): 'pr'`.

Requires the domain `west.rosettacommons.org` on the network allowlist
(`request_network_access(domain="west.rosettacommons.org")` — was granted).
Licence is free for academic/non-commercial use but is granted to the institution, not to the agent.

### Running cartesian_ddg

Two stages. Both scripts are in the repo at `data/ddg/relax_stage.py` and `data/ddg/ddg_stage.py`.

```bash
cd /path/to/workdir            # needs AF-O60674-F1.pdb present
curl -o AF-O60674-F1.pdb https://alphafold.ebi.ac.uk/files/AF-O60674-F1-model_v6.pdb   # note: v4 404s
cp /Users/chervov/ProteinModelling1/data/ddg/{relax_stage,ddg_stage}.py .
/opt/anaconda3/bin/python relax_stage.py      # stage 1
/opt/anaconda3/bin/python ddg_stage.py        # stage 2
```

**Stage 1 (`relax_stage.py`)** — Frenz et al. 2020 protocol (`10.3389/fbioe.2020.558247`):
relax the starting model **20× in Cartesian space without all-atom constraints**, keep the
**lowest-energy** model. Constrained prep is what the paper explicitly argues against.

**Stage 2 (`ddg_stage.py`)** — per variant: repack the 6 Å shell, Cartesian-minimise a 10 Å shell
with backbone **and** side-chain DOFs free, iterate until the two lowest energies agree within
1 REU (max 5), take the lowest. ΔΔG = min(E_mut) − min(E_wt). **Positive = destabilising.**

| step | hardware | measured time |
|---|---|---|
| one Cartesian FastRelax, 276 residues | 1 core | 575 s |
| full relax stage, 40 jobs (2 constructs × 20) | 8 cores | **170.5 min** |
| ddG stage, 23 variants | 8 cores | **0.6 min** (~4 s/variant, both states) |

Full-length JAK2 (1,132 aa) cannot be relaxed 20× in reasonable time. Two natural modules were used:
**FERM-SH2 = residues 20–497** and **JH2-JH1 = 545–1132** (the latter spans the linker so E846D is
covered). Pad past your variants: P37A sits exactly on the FERM domain start.

**Two traps, both measured:**

1. **`cart_bonded` can dominate.** For V625F it contributed +48.67 of +58.55 REU (83%) — bond-geometry
   strain, not stability. Cause: `MutateResidue` places the side chain against a Cartesian-relaxed
   (non-ideal) backbone; if the MoveMap frees backbone DOFs only at i±1 the strain cannot relax.
   Always record `Δcart_bonded` per variant and flag `|Δcart_bonded| > 2 REU`.
2. **Do NOT substitute FastRelax for pack+minimise.** It is stochastic and relaxes wild type and
   mutant into *different* local minima. V617F went from +3.22 to +31.75 REU, at **340 s/variant
   instead of 4 s**. The pack+minimise protocol is **deterministic: SD = 0.00 REU over 6 repeats
   with free random seeds**.

---

## 2. FoldX — do not install, the data is already here

No FoldX binary was ever run. All FoldX values come from EBI ProtVar's precomputed FoldX 5 run on
AlphaFold models.

```bash
ls -l /Users/chervov/protvar/foldx_energy_2025.02.10.csv.gz   # 1.5 GB, already downloaded
head -1 /Users/chervov/protvar/jak_src_foldx.csv
# uniprot_accession,uniprot_position,alphafold_fragment_id,alphafold_fragment_position,
# wild_type,mutated_type,foldx_ddg,plddt
```

Extract one accession without decompressing the whole file:

```bash
gzcat /Users/chervov/protvar/foldx_energy_2025.02.10.csv.gz \
  | awk -F, 'NR==1 || $1=="O60674"' > jak2_foldx.csv
```

Upstream URL if you must re-download (~1.56 GB):
`https://ftp.ebi.ac.uk/pub/databases/ProtVar/predictions/stability/2025.02.10_foldx_energy.csv.gz`
— CC BY 4.0, **208,792,558 data rows**, 20,437 accessions, 76.0% of canonical human residues.

**Four traps, all measured:**
1. Sign convention is **positive = destabilising**.
2. **The README is stale** — it describes a pLDDT-70 filter leaving 34,838,191 rows; the real file is
   16.7% larger than that implies.
3. **17.3% of positions are fragment duplicates** (same residue under more than one AlphaFold
   fragment). Deduplicate on `(uniprot_accession, uniprot_position, mutated_type)` before aggregating.
4. Coverage is worst exactly where multi-domain proteins live: **64.1% for 1,001–2,700 aa**. For JAK2,
   20,349 of 21,508 substitutions are present (94.6%); the 61 absent positions have median pLDDT 31.8
   against 93.1 for present ones.

---

## 3. Tools that must be reinstalled

### 3.1 ThermoMPNN — gone, ~5 min to restore

```bash
# do NOT `git clone`: the repo contains a .idea/ directory which this filesystem refuses to
# create. git aborts the checkout, leaves an empty tree, and still exits 0.
curl -L https://codeload.github.com/Kuhlman-Lab/ThermoMPNN/tar.gz/refs/heads/main -o t.tar.gz
tar xzf t.tar.gz --exclude='*/.idea*'          # 9 s; 62 MB tarball -> 156 MB tree
```

> **Corrected 6 Nov.** An earlier version of this guide used
> `tar tzf ... | grep -v '/\.idea/' > keep.txt && tar xzf t.tar.gz -T keep.txt`.
> **That does not work.** macOS `bsdtar` treats `-T` entries as *prefix patterns*, and the list
> still contains the top-level `ThermoMPNN-main/` entry, which re-matches everything underneath —
> including `.idea`. Extraction completes but emits `Can't create 'ThermoMPNN-main/.idea'` and
> exits non-zero via "Error exit delayed from previous errors". Use `--exclude` as above.

Dependencies are **already in the `ddg` conda env** (torch 2.14.1, fair-esm 2.0.0,
pytorch-lightning 2.6.6, omegaconf 2.4.0, torchmetrics 1.9.0). If you need them elsewhere, install
with `manage_packages`, not pip.

```bash
export PYTHONPATH=$PYTHONPATH:$PWD/ThermoMPNN-main/analysis     # required, else ImportError
python ThermoMPNN-main/analysis/custom_inference.py \
    --pdb JAK1_afdb_P23458.pdb --chain A \
    --model_path ThermoMPNN-main/models/thermoMPNN_default.pt \
    --out_dir ./tm_jak1
# writes ./tm_jak1/ThermoMPNN_inference_<pdb-stem>.csv
# columns: Model, Dataset, ddG_pred, position, wildtype, mutation, pdb, chain
```

> **Corrected 6 Nov.** Two things. (a) `--model_path` is **required** — there is no default, and
> model weights ship inside the tarball at `models/thermoMPNN_default.pt` plus
> `vanilla_model_weights/*.pt`, so nothing extra is downloaded. The flag is `--out_dir`, not `--out`.
> (b) An earlier version told you to `sed -i '' 's/accel:.*/accel: "cpu"/' local.yaml`. That
> **silently does nothing** — the key is indented (`  accel: "gpu"`) so `^accel:` never matches.
> It also turns out to be **unnecessary**: the run completed on CPU with `accel` still set to
> `"gpu"`, because torch falls back when no device is present.
>
> Row count is **20 per position, not 19** — the self-substitution is included. JAK1 (1,154 aa)
> yields 23,080 rows.

**Numbering trap:** `custom_inference.py` reports
`position = PDB_author_number − min_author_number`. It indexes from the first observed residue
**including gaps** — it is NOT a dense index and NOT the author number. Map back explicitly.

**Timing:** **336 variants/s** median over 23 proteins (range 198–487); 269,458 variants in 961 s on
one core. A 1,132-residue saturation scan (21,508 variants) takes about a minute.

### 3.2 mCSM-Stability and DDMut — no install, HTTP only

Host `biosig.lab.uq.edu.au` must be on the allowlist
(`request_network_access(domain="biosig.lab.uq.edu.au")` — was granted).

```bash
# mCSM-Stability — BATCH endpoint. Mutation list is CHAIN FIRST: "A V617F", not "V617F A".
printf 'A V617F\nA I1065T\n' > mutlist.txt
curl -s -X POST https://biosig.lab.uq.edu.au/mcsm/stability_prediction_list \
     -F wild=@AF-O60674-F1.pdb -F mutation_list=@mutlist.txt
# -> HTML page; results at /mcsm/results_stability_prediction/<job_id>
# parse with pandas.read_html(StringIO(html))  [needs lxml, already installed]
```

mCSM-Stability lives at **`/mcsm/stability`**; `/mcsm_stability` is a 404.

```bash
# DDMut — proper JSON API, submit then poll
curl -s -X POST https://biosig.lab.uq.edu.au/ddmut/api/prediction_list \
     -F pdb_file=@AF-O60674-F1.pdb -F mutations_list=@mutlist.txt     # -> {"job_id": "..."}
curl -s -X GET  https://biosig.lab.uq.edu.au/ddmut/api/prediction_list -F job_id=<id>
# returns {"status": "RUNNING"} until done, then a dict keyed "0","1",... plus "results_page"
```

**Both report NEGATIVE = destabilising.** Negate before merging with ThermoMPNN/FoldX/Rosetta.
Verified against their own text labels: mCSM returned −2.106 for H608N tagged "Highly Destabilizing"
and +1.129 for H380Y tagged "Stabilizing".

**Timing:** mCSM batch of 23 returned by the first poll. DDMut batch of 23 took ~15 min.

### 3.3 RSALOR — gone, ~2 min to restore

```python
# rsalor is SDIST-ONLY on PyPI (no wheels at all). The shared `python` environment is
# wheel-only, so manage_packages there FAILS with:
#     ERROR: Could not find a version that satisfies the requirement rsalor (from versions: none)
# The fix is a dedicated environment, where building from source is permitted:
manage_environments(mode="create", name="rsalor", language="python",
                    python_version="3.11", packages=["pandas","numpy","biopython"])
manage_packages(environment="rsalor", mode="install", packages=["rsalor"], use_pip=True)
```
Takes **10 s** — it compiles the C++ backend and caches a wheel
(`rsalor-1.1.11-cp311-cp311-macosx_11_0_arm64.whl`). Verified to land in the **persistent** layer at
`/Users/chervov/.claude-science/conda/envs/rsalor/lib/python3.11/site-packages/rsalor` (568 KB).
mafft is already at `/Users/chervov/.claude-science/conda/envs/python/bin/mafft`.

RSALOR needs an MSA and **does not build one**:

```bash
# 1. homologues — add the paralogues or Neff will be hopeless
for acc in O60674 P23458 P52333 P29597; do
  curl -s "https://rest.uniprot.org/uniprotkb/stream?query=uniref_cluster_50:UniRef50_${acc}&format=fasta" \
       -o clus_${acc}.fasta
done
# 2. concatenate, put the TARGET FIRST, drop exact duplicates and fragments <60% of target length
# 3. align
mafft --auto --thread 2 jak_family_input.fasta > jak_family_msa.fasta    # 902 seqs, ~3 min
```

```python
from rsalor import MSA
MSA("jak_family_msa.fasta", "AF-O60674-F1.pdb", "A", num_threads=2) \
    .save_scores("rsalor_jak2.csv")
```

**Column trap:** use **`mutation_pdb`** (`wt + chain + pos + mt`, e.g. `MA1A`).
`mutation_fasta` uses *untrimmed-alignment* numbering and is not the UniProt position.

**Known limitation:** this alignment reaches only **Neff = 30.2** despite 877 sequences — the UniRef50
clusters are nearly all vertebrate orthologues above 80% identity. Adding the three paralogues moved
Neff only from 23.9 to 30.2. Residue frequencies from ~30 effective sequences are noisy. A proper
jackhmmer/HHblits run against UniRef90/BFD would fix it but needs a ~25 GB database not present here,
and the EBI HMMER REST endpoint returns **405 to POST**.

### 3.4 RaSP — gone, ~20 min to restore, four patches required

Source: `github.com/KULL-Centre/_2022_ML-ddG-Blaabjerg` (~1.5 GB with weights).
Extra deps beyond the `ddg` env: `pytz`, `mpl-scatter-density` (openmm, pdbfixer, reduce, dssp,
scikit-learn are already there).

Four 2022-era breakages must be patched:

| breakage | fix |
|---|---|
| `np.int` removed from NumPy | replace with `int` |
| `Bio.SubsMat` removed from Biopython | use `Bio.Align.substitution_matrices` |
| `mkdssp` 4.x accepts **only mmCIF** | substitute Biopython's Shrake–Rupley SASA — verified harmless, `resenv.sasa` is read only by `visualization.py` |
| training-only plot imports at module scope | make the `ptitprince` import optional; it is not otherwise needed |

**One real optimisation:** `helpers.ds_pred` recomputes the cavity model once per ensemble member
although it does not depend on it. Hoisting it out of the loop gave **213.6 s → 23.2 s (9×)** with
identical values.

**Output trap:** `ds_pred` returns a malformed DataFrame (list objects packed into the
`pdbid`/`chainid`/`variant` cells). Take keys from the **input frame order** instead —
`get_ddg_dataloader` uses `shuffle=False, drop_last=False` for `data_type='pred'`, so output order
equals input order exactly.

**Timing:** ~125 variants/s.

---

## 4. What could not be installed or run, and why

| target | reason | would it help to retry? |
|---|---|---|
| **DUET**, **SDM** | Server fault. `POST /duet/stability_prediction` returns **HTTP 500 for any uploaded PDB**, including DUET's own example protein 2OCJ with its own example mutation R282W chain A. The hardcoded demo at `/duet/run_example_stability` works, so the server is up and the upload path is broken. | No — upstream bug. Retry later. |
| **PoPMuSiC 3.1** | Hosts `soluble.db.ulb.ac.be` and `dezyme.com` are **not on the allowlist**, *and* the service requires a registered account with web-form submission. | Allowlisting alone is insufficient; an account is needed. |
| **DDGun / DDGun3D** | All three score terms require a ~25 GB hhblits/uniclust profile database. Supplying a single-sequence profile would silently degrade it to a substitution matrix. | Only with the database. Do not fake the profile. |
| **molab remote compute** | Not registered under Customize → Compute, so `list_compute()` returns `{"providers": []}`. The URL serves a marimo frontend (`/health`, `/api/status` → 200; `/api/kernels` → 404). Sandboxes expire ~4 h. | Needs the user to register it as a compute target. |
| **EBI HMMER (deeper MSA)** | `hmmer.ebi.ac.uk` not allowlisted; `www.ebi.ac.uk/Tools/hmmer/search/phmmer` returns **405 to POST**. | Needs a local sequence database instead. |
| **`~/ddg_jak2`, `~/ddg_jak3`, `~/ddg_overnight`** | Sandbox-blocked. | Yes — `request_host_access` on each specific path works. |

---

## 5. End-to-end reproduction, shortest path

```bash
# 0. grants (new kernels only)
#    request_host_access("/Users/chervov/ProteinModelling1", "ro")
#    request_host_access("/Users/chervov/protvar", "ro")
#    request_network_access("biosig.lab.uq.edu.au")

# 1. structure — AlphaFold numbering == UniProt numbering, chain A, 1132 residues
curl -o AF-O60674-F1.pdb https://alphafold.ebi.ac.uk/files/AF-O60674-F1-model_v6.pdb

# 2. FoldX: read from disk, no compute
gzcat /Users/chervov/protvar/foldx_energy_2025.02.10.csv.gz | awk -F, 'NR==1 || $1=="O60674"' > foldx.csv

# 3. ThermoMPNN: §3.1, ~1 min for the full saturation scan
# 4. Rosetta:    /opt/anaconda3/bin/python relax_stage.py && ddg_stage.py   (~171 min)
# 5. RSALOR:     §3.3
# 6. mCSM+DDMut: §3.2, remember to NEGATE
```

**Always verify every wild-type residue against the structure before submitting anything.** In this
variant set `R755S` failed that check — position 755 is **S** in O60674, not R.

---

## 6. Sanity checks before trusting any output

1. **Fix the sign convention empirically, never from documentation.** Three conventions are in play
   in this project at once: positive = destabilising for ThermoMPNN / FoldX-ProtVar / this
   `cartesian_ddg`; negative = destabilising for mCSM, DDMut, and the dual-state Rosetta files in
   `data/ddg/`. Check that buried hydrophobic→charged substitutions and helix prolines come out
   destabilising.
2. **Check the proline tail.** If >50% of X→P substitutions are extreme outliers, the protocol is not
   rebuilding the backbone. Measured on the dual-state files: X→P median **−215 REU** against **+3.41**
   (FoldX) and **+2.03** (ThermoMPNN); 92.5% of X→P below −10 in Rosetta, 0.0% in ThermoMPNN.
3. **Check determinism.** Run one variant 6× with free random seeds. Pack+minimise gives SD = 0.00 REU;
   anything stochastic is measuring relaxation noise, not the mutation.
4. **Do not build a consensus column.** On 386 held-out human measurements ThermoMPNN alone scores
   r = 0.517, ThermoMPNN+FoldX 0.509, all three 0.489. The predictors agree with each other
   (r 0.583–0.702) more than any agrees with experiment (mean 0.424), so averaging reinforces shared bias.
5. **Respect the floors.** ±0.50 kcal/mol (experimental noise) for "is there an effect"; ±0.69
   (ThermoMPNN's measured antisymmetry bias) for "does the sign mean anything"; ±1.47 (RMSE on
   held-out human data) for "is the difference between two variants real".

---

## 7. Where the outputs live

| file | path |
|---|---|
| six-method table, 24 variants | `data/ddg/jak2_variants_multimethod.csv` |
| Rosetta per-variant energies + `cart_bonded` | `data/ddg/jak2_rosetta_cartesian.csv` |
| Rosetta stage scripts | `data/ddg/relax_stage.py`, `data/ddg/ddg_stage.py` |
| full report | `data/ddg/jak2_selected.html` |
| survey with figures | `data/ddg/survey_claudesci/` |
| dual-state audit + P1/P2 reproducibility | `data/ddg/rosetta_dualstate_qc.md` |
| ThermoMPNN JAK source table | `external_data/thermompnn_jak_src.csv` |

---

## 8. Rebuild log — 6 November 2026

The guide above was **executed end to end** to verify it. Five things were wrong or had changed;
all are fixed in place above and listed here with the symptom, so you can recognise them.

### 8.1 Problems hit, and the fix

| # | problem | symptom | fix |
|---|---|---|---|
| 1 | **`rsalor` is sdist-only** | `manage_packages(environment="python", packages=["rsalor"])` → `Could not find a version that satisfies the requirement rsalor (from versions: none)`. PyPI has **no wheels** for it, only `.tar.gz`; the shared env is wheel-only. | Create a dedicated env with `manage_environments`, then `manage_packages(environment="rsalor", use_pip=True)`. Builds the C++ backend from source in 10 s. |
| 2 | **Environments are two layers** | Bare `pip install` inside a shell reports `prefix ./.venv/<env>` and vanishes on workspace cleanup, even for a 1.4 GB install. | conda layer `/Users/chervov/.claude-science/conda/envs/<env>/` is **persistent**; the workspace `.venv/<env>/` overlay (724 KB for three envs) is **ephemeral**. Always install through `manage_packages`. |
| 3 | **`tar -T keep.txt` does not exclude `.idea`** | `Can't create 'ThermoMPNN-main/.idea'`, then `Error exit delayed from previous errors`. | bsdtar treats `-T` entries as prefix patterns and the top-level dir entry re-matches everything. Use `tar xzf t.tar.gz --exclude='*/.idea*'`. |
| 4 | **`sed -i '' 's/accel:.*/.../'` is a no-op** | `grep accel local.yaml` still shows `accel: "gpu"` after the sed. | The key is indented, so `^accel:` never matches. It is also **unnecessary** — the run completes on CPU regardless, because torch falls back when no device is present. |
| 5 | **AlphaFold downloads now return HTTP 403** | `alphafold.ebi.ac.uk/files/AF-*-model_v{4,5,6}.pdb` → 403 for every version; curl writes a 4 KB HTML error page that looks like a PDB until you count `CA` atoms (0). | Worked on 30 Oct, blocked on 6 Nov. **Use the copies already in the repo**: `/Users/chervov/ProteinModelling1/AFDB/{JAK1_afdb_P23458,JAK2_afdb_O60674,JAK3_afdb_P52333,TYK2_afdb_P29597}.pdb`. Verified: 1,154 and 1,132 CA atoms. Otherwise `request_network_access(domain="alphafold.ebi.ac.uk")`. |

**Always check `CA` count after fetching a structure** — a 403 error page saves without complaint:

```bash
awk '$1=="ATOM" && substr($0,13,4)~/CA/' f.pdb | wc -l     # must be ~the residue count, not 0
```

### 8.2 Installation timings, measured today

| step | time | note |
|---|--:|---|
| RSALOR (sdist → compiled wheel) | **10 s** | into the dedicated env; persistent |
| ThermoMPNN download + extract | **9 s** | 62 MB tarball → 156 MB tree, weights bundled |
| PyRosetta | **0 s** | already installed at `/opt/anaconda3`; init from warm cache is instant |
| structures | **0 s** | taken from the repo, AlphaFold being 403 |
| *(not redone)* RaSP | ~20 min | 1.5 GB plus four source patches |

Total to a working three-method setup: **under 30 seconds**, because PyRosetta and the ProtVar dump
both survived. From cold it would be ~45 min, dominated by the PyRosetta wheel.

### 8.3 Computation timings, measured today

Separate from installation. All single-process unless noted.

| run | scale | time | rate |
|---|--:|--:|---|
| **ThermoMPNN**, JAK1 full saturation | 1,154 aa → 23,080 rows | **53 s** | **435 variants/s** |
| **RSALOR**, JAK2 full saturation | 1,132 aa → 22,640 scores | **2 s** | ~11,000 scores/s |
| **PyRosetta** one Cartesian FastRelax | 276-residue construct | **535 s** | — |
| **PyRosetta** `cartesian_ddg` per variant | 276-residue construct | **1.5 s** | 0.67 variants/s |

Two observations that matter for planning:

- **The 53 s JAK1 run is 435 variants/s**, above the 336/s median recorded earlier across 23 mixed
  proteins — large single proteins amortise model loading better than many small ones.
- **`cartesian_ddg` cost scales strongly with construct size**: 1.5 s/variant on the 276-residue
  JH1 construct against **8.7 s/variant** on the 588-residue JH2-JH1 construct used in production.
  Trim to the smallest construct that still pads your variants.

### 8.4 Reproducibility of the results themselves

| quantity | original run | rebuild | agreement |
|---|--:|--:|---|
| RSALOR Neff (JAK2 family MSA) | 30.22 | **30.22** | exact |
| RSALOR scores produced | 22,640 | **22,640** | exact |
| ThermoMPNN rows, JAK1 | 23,080 | **23,080** | exact |
| one Cartesian relax, 276 res | 575 s | **535 s** | 7% faster, same machine |
| I1065T `cartesian_ddg` | +10.13 REU | **+9.72 REU** | 4% — see note |

The I1065T difference is expected, not drift: the rebuild used a **JH1-only construct (849–1124)
relaxed once**, whereas production used **JH2-JH1 (545–1132) relaxed 20× with the lowest-energy model
kept**. That two protocol changes move the value by only 0.4 REU is reassuring for the protocol's
stability — and note the *ranking* is unchanged, with I1065T still far above R1063H (+1.86) and
V1110E (+0.49).
