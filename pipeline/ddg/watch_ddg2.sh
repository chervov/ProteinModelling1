#!/bin/bash
# Phase 1: poll every 2 min until both boxes have a worker running (PyRosetta install finishes).
# Phase 2: the normal 30-min collect/analyse cycle.
cd /Users/chervov
echo "### PHASE 1: waiting for PyRosetta, deploying as each box becomes ready"
for i in $(seq 1 25); do
  launched=0
  while read IDX U N; do
    out=$(bash ~/.claude/skills/marimo-pair/scripts/execute-code.sh \
            --url https://$U.sb.molab.run/ \
            ~/.claude/jobs/e920d48f/tmp/deploy$IDX.py 2>&1 | grep -v '^Warning')
    st=$(echo "$out" | grep -E 'LAUNCHED|ALREADY|NOT LAUNCHED' | head -1)
    echo "  [$(date '+%H:%M:%S')] $N: $st"
    case "$st" in *LAUNCHED\ pid*|*ALREADY*) launched=$((launched+1));; esac
  done < ~/boxes.txt
  nboxes=$(wc -l < ~/boxes.txt)
  if [ "$launched" -ge "$nboxes" ]; then
    echo "### all $nboxes boxes running after $i attempt(s)"; break
  fi
  sleep 120
done
echo
echo "### PHASE 2: 30-minute cycles"
for i in $(seq 1 20); do
  echo "########## cycle $i  $(date '+%F %H:%M')"
  python3 cycle.py 2>&1
  rc=$?
  if [ "$rc" = "42" ]; then
    echo "### STALLED: all boxes dead. Exiting so this surfaces instead of spinning."
    break
  fi
  echo
  sleep 1800
done
echo "WATCH_LOOP_FINISHED"
