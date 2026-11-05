#!/usr/bin/env bash
# install_and_verify.sh - rebuild the ddG toolchain on THIS machine and prove it works.
#
# Every step is idempotent and self-checking. Run from a scratch workdir:
#     bash install_and_verify.sh 2>&1 | tee install_log.txt
#
# IF YOU ARE AN AGENT: steps marked [AGENT] must be done with the manage_packages /
# manage_environments tools instead of pip, or they will NOT persist past a workspace
# cleanup (see ddg_build_review.md section 0.1). The pip fallbacks here work for a
# single session only.
set -uo pipefail
say(){ printf '\n=== %s\n' "$*"; }
T0=$(date +%s)

REPO=/Users/chervov/ProteinModelling1
PROTVAR=/Users/chervov/protvar
PYROSETTA=/opt/anaconda3/bin/python

say "0. Preconditions"
for p in "$REPO" "$PROTVAR"; do
  [ -d "$p" ] && echo "  OK   $p" || { echo "  MISS $p  -> request_host_access(\"$p\",\"ro\")"; }
done
$PYROSETTA -c "import pyrosetta" 2>/dev/null \
  && echo "  OK   PyRosetta at $PYROSETTA" \
  || echo "  MISS PyRosetta -> see ddg_build_review.md section 1 (1.4 GB wheel, ~25 min)"

say "1. Structures - do NOT download, alphafold.ebi.ac.uk returns 403 (checked 6 Nov 2026)"
for f in JAK1_afdb_P23458 JAK2_afdb_O60674 JAK3_afdb_P52333 TYK2_afdb_P29597; do
  [ -f "$f.pdb" ] || cp "$REPO/AFDB/$f.pdb" . 2>/dev/null
  n=$(awk '$1=="ATOM" && substr($0,13,4)~/CA/' "$f.pdb" 2>/dev/null | wc -l | tr -d ' ')
  [ "${n:-0}" -gt 100 ] && echo "  OK   $f.pdb  CA=$n" || echo "  FAIL $f.pdb  CA=${n:-0}  <-- a 403 error page saves silently; always count CA"
done

say "2. ThermoMPNN  [AGENT: deps via manage_packages into env 'ddg']"
if [ ! -d ThermoMPNN-main ]; then
  t=$(date +%s)
  curl -sL https://codeload.github.com/Kuhlman-Lab/ThermoMPNN/tar.gz/refs/heads/main -o t.tar.gz
  # --exclude, NOT `-T keep.txt`: bsdtar treats -T entries as prefix patterns and the
  # top-level dir entry re-matches .idea, which this filesystem refuses to create.
  tar xzf t.tar.gz --exclude='*/.idea*'
  echo "  installed in $(( $(date +%s)-t ))s"
else echo "  already present"; fi
[ -f ThermoMPNN-main/models/thermoMPNN_default.pt ] && echo "  OK   weights bundled" || echo "  FAIL weights missing"

say "3. RSALOR  [AGENT: sdist-only - manage_environments(create 'rsalor') then manage_packages(use_pip=True)]"
python -c "import rsalor" 2>/dev/null && echo "  OK   rsalor importable" || {
  echo "  not in this env; pip fallback (session-only):"; pip install -q rsalor && echo "  installed"; }

say "4. FoldX - nothing to install, read the precomputed dump"
ls -lh "$PROTVAR/foldx_energy_2025.02.10.csv.gz" 2>/dev/null | awk '{print "  OK   "$9" "$5}' \
  || echo "  MISS ProtVar dump"

say "5. VERIFY: ThermoMPNN end-to-end on JAK1 (1154 aa -> 23080 rows)"
export PYTHONPATH="$PYTHONPATH:$PWD/ThermoMPNN-main/analysis"
t=$(date +%s)
python ThermoMPNN-main/analysis/custom_inference.py --pdb JAK1_afdb_P23458.pdb --chain A \
  --model_path ThermoMPNN-main/models/thermoMPNN_default.pt --out_dir ./tm_verify >/dev/null 2>&1
el=$(( $(date +%s)-t ))
n=$(wc -l < tm_verify/ThermoMPNN_inference_JAK1_afdb_P23458.csv 2>/dev/null || echo 0)
[ "$n" -eq 23081 ] && echo "  PASS ${n} lines (23080 rows + header) in ${el}s  [expect ~53s]" \
                   || echo "  FAIL got $n lines, expected 23081"

say "6. VERIFY: PyRosetta scores"
$PYROSETTA - <<'PY' 2>/dev/null | tail -1
import pyrosetta; pyrosetta.init("-mute all")
from pyrosetta import pose_from_sequence
sf=pyrosetta.create_score_function("ref2015_cart")
e=sf(pose_from_sequence("AAAAAAAAAA"))
print(f"  {'PASS' if 25<e<35 else 'FAIL'} ref2015_cart on poly-Ala = {e:.2f} REU  [expect ~31]")
PY

say "DONE in $(( $(date +%s)-T0 ))s total"
