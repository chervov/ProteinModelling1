param(
  # jak2_variants_multimethod.csv; downloaded from this repo when not given.
  [string]$multimethod
)
# Independent check of ddg_approximation.md / ddg_approximator.py. Reimplements compute_ddg from
# the published source and runs three tests:
#   1. does the table in section 5 reproduce from the code in section 4?
#   2. can the model ever return a stabilising (negative) value?
#   3. does it correlate with ThermoMPNN / FoldX / mCSM / DDMut on the JAK2 set in this repo?
# Written in PowerShell because the machine it was produced on has no Python.
# Kept pure ASCII: PowerShell 5.1 reads a BOM-less .ps1 as ANSI and mangles anything else.
$ErrorActionPreference = 'Stop'

$AA_VOL = @{G=60.1;A=88.6;S=89.0;C=108.5;D=111.1;P=112.7;T=116.1;N=114.1;V=140.0;E=138.4;
            Q=143.8;H=153.2;I=166.7;L=166.7;M=162.9;K=168.6;F=189.9;Y=193.6;W=227.8;R=225.0}
$AA_CHG = @{D=-1.0;E=-1.0;K=1.0;R=1.0;H=0.1;G=0.0;A=0.0;S=0.0;C=0.0;P=0.0;
            T=0.0;N=0.0;V=0.0;Q=0.0;I=0.0;L=0.0;M=0.0;F=0.0;Y=0.0;W=0.0}

function Approx($wt, $mut, $burial = 0.8, $turn = $false, $salt = $false, $cat = $false, $auto = $false) {
  $alpha = 0.040; $kappa = 0.024; $born = 1.42; $glyP = 2.42; $proP = 1.45
  $dv = $AA_VOL[$mut] - $AA_VOL[$wt]
  $dq = [math]::Abs($AA_CHG[$mut] - $AA_CHG[$wt])
  $st = 0.0; $cav = 0.0; $el = 0.0; $bb = 0.0
  if ($dv -gt 0) { $st += $alpha * $dv * $burial; if ($auto) { $st += 1.2 } }
  if ($wt -eq 'G' -and $mut -ne 'G') { $st += $(if ($turn) { $glyP } else { 1.2 }) }
  if ($dv -lt 0) {
    $cav += $kappa * [math]::Abs($dv) * $burial
    if ($wt -in @('F','Y','W') -and $mut -in @('A','V','G','S')) { $cav += 1.1 }
  }
  if ($dq -gt 0) {
    if ($burial -gt 0.5) { $el += $born * $burial }
    if ($cat) { $el += 1.0 }
  }
  if ($salt -and [math]::Abs($AA_CHG[$wt]) -gt 0 -and $AA_CHG[$mut] -eq 0) { $el += 2.2 }
  if ($wt -eq 'P' -and $mut -ne 'P') { $bb += $proP }
  elseif ($wt -ne 'P' -and $mut -eq 'P') { $bb += $(if ($cat) { 1.8 } else { 1.2 }) }
  if ($wt -in @('V','I','L') -and $mut -in @('V','I','L')) {
    $st = [math]::Min($st, 0.4); $cav = [math]::Min($cav, 0.4)
  }
  [pscustomobject]@{ dv = $dv; steric = $st; cavity = $cav; elec = $el; bb = $bb
                     total = [math]::Round($st + $cav + $el + $bb, 2) }
}

function Ranks([double[]]$x) {
  $idx = 0..($x.Count - 1) | Sort-Object { $x[$_] }
  $r = New-Object double[] $x.Count
  $i = 0
  while ($i -lt $idx.Count) {
    $j = $i
    while ($j + 1 -lt $idx.Count -and $x[$idx[$j + 1]] -eq $x[$idx[$i]]) { $j++ }
    $avg = ($i + $j) / 2.0 + 1
    for ($k = $i; $k -le $j; $k++) { $r[$idx[$k]] = $avg }
    $i = $j + 1
  }
  $r
}
function Pear([double[]]$a, [double[]]$b) {
  $ma = ($a | Measure-Object -Average).Average; $mb = ($b | Measure-Object -Average).Average
  $n = 0.0; $da = 0.0; $db = 0.0
  for ($i = 0; $i -lt $a.Count; $i++) {
    $x = $a[$i] - $ma; $y = $b[$i] - $mb
    $n += $x * $y; $da += $x * $x; $db += $y * $y
  }
  if ($da -eq 0 -or $db -eq 0) { return [double]::NaN }
  $n / [math]::Sqrt($da * $db)
}

# ---- test 1: does section 5 reproduce? ---------------------------------------
'TEST 1  section 5 of ddg_approximation.md vs the code in section 4'
$claims = @{ V617F=3.0; G571R=3.4; V1110E=2.9; F240V=2.6; V578I=0.3; L805I=0.7; R938Q=3.2; P37A=1.4 }
$tests = @(
  @{id='V617F'; wt='V'; mut='F'; b=0.90; auto=$true},
  @{id='G571R'; wt='G'; mut='R'; b=0.80; turn=$true},
  @{id='V1110E';wt='V'; mut='E'; b=0.90; cat=$true},
  @{id='F240V'; wt='F'; mut='V'; b=0.95},
  @{id='V578I'; wt='V'; mut='I'; b=0.85},
  @{id='L805I'; wt='L'; mut='I'; b=0.50},
  @{id='R938Q'; wt='R'; mut='Q'; b=0.85; salt=$true},
  @{id='P37A';  wt='P'; mut='A'; b=0.40}
)
"{0,-8} {1,8} {2,8} {3,8} {4,7} {5,6} {6,8} {7,7} {8}" -f 'variant','dV','steric','cavity','elec','bb','CODE','DOC','check'
('-' * 82)
# not $matches: that is the automatic variable the -match operator writes to
$nMatch = 0
foreach ($t in $tests) {
  $res = Approx $t.wt $t.mut $t.b $t.turn $t.salt $t.cat $t.auto
  $doc = $claims[$t.id]
  $ok = [math]::Abs($res.total - $doc) -lt 0.06
  if ($ok) { $nMatch++ }
  "{0,-8} {1,8:N1} {2,8:N2} {3,8:N2} {4,7:N2} {5,6:N2} {6,8:N2} {7,7:N1} {8}" -f `
    $t.id, $res.dv, $res.steric, $res.cavity, $res.elec, $res.bb, $res.total, $doc,
    $(if ($ok) { 'match' } else { 'MISMATCH' })
}
"$nMatch of $($tests.Count) values in section 5 reproduce from the code."
''

# ---- test 2: can it ever be stabilising? -------------------------------------
'TEST 2  can the model return a negative (stabilising) value?'
$neg = 0; $tot = 0; $min = [double]::MaxValue
foreach ($a in $AA_VOL.Keys) {
  foreach ($b in $AA_VOL.Keys) {
    if ($a -eq $b) { continue }
    foreach ($bur in 0.0, 0.2, 0.5, 0.8, 1.0) {
      $res = Approx $a $b $bur
      $tot++
      if ($res.total -lt 0) { $neg++ }
      if ($res.total -lt $min) { $min = $res.total }
    }
  }
}
"$tot substitution/burial combinations: $neg negative, minimum $min"
"Section 1 defines ddG < 0 as stabilising, so that range is unreachable."
''

# ---- test 3: correlation with the methods already in this repo ---------------
'TEST 3  rank correlation with ThermoMPNN / FoldX / mCSM / DDMut'
if (-not $multimethod) {
  $multimethod = Join-Path $env:TEMP 'jak2_variants_multimethod.csv'
  if (-not (Test-Path $multimethod)) {
    Invoke-WebRequest -UseBasicParsing -TimeoutSec 300 -OutFile $multimethod `
      'https://raw.githubusercontent.com/chervov/ProteinModelling1/main/data/ddg/jak2_variants_multimethod.csv'
  }
}
$ap = @(); $tm = @(); $fx = @(); $mc = @(); $dm = @()
foreach ($row in (Import-Csv $multimethod)) {
  if ($row.variant -notmatch '^([A-Z])(\d+)([A-Z])$') { continue }
  $wt = $Matches[1]; $mu = $Matches[3]
  if (-not $AA_VOL.ContainsKey($wt) -or -not $AA_VOL.ContainsKey($mu)) { continue }
  if ($row.rsa_pct -notmatch '^\d') { continue }
  # burial from the structure, flags off: the flags are not derivable from a PDB
  $bur = [math]::Max(0.0, [math]::Min(1.0, 1.0 - [double]$row.rsa_pct / 100.0))
  $ap += (Approx $wt $mu $bur).total
  $tm += [double]$row.thermompnn; $fx += [double]$row.foldx
  $mc += [double]$row.mcsm_stability; $dm += [double]$row.ddmut
}
"n = $($ap.Count) JAK2 variants with RSA and all four methods"
"approximator range $([math]::Round(($ap | Measure-Object -Min).Minimum,2)) .. $([math]::Round(($ap | Measure-Object -Max).Maximum,2)), mean $([math]::Round(($ap | Measure-Object -Average).Average,2))"
$rk = Ranks $ap
foreach ($m in @(@('ThermoMPNN', $tm), @('FoldX', $fx), @('mCSM-Stability', $mc), @('DDMut', $dm))) {
  "  Spearman vs {0,-15} {1,6:N3}" -f $m[0], (Pear $rk (Ranks ([double[]]$m[1])))
}

