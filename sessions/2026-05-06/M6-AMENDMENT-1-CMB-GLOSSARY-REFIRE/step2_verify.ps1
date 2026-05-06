$L = [System.IO.File]::ReadAllLines("tex\submitted\CMB.txt")
Write-Host "Total lines: $($L.Length)"
$tests = @(
    @{n=404;  rx='M9 caveat profile.*M6'},
    @{n=941;  rx='M9 GATING.*\{M4, M6\}'},
    @{n=993;  rx='M9 gating: \{M4, M6\} stands'},
    @{n=1517; rx='M6 .*-vs-Phase-A/B\.5 arbitration'}
)
foreach ($t in $tests) {
    $idx = $t.n - 1
    $line = $L[$idx]
    $m = ($line -match $t.rx)
    Write-Host ("L{0,4}: match={1}  ::  {2}" -f $t.n, $m, $line)
}
Write-Host '---verbatim block boundaries---'
Write-Host ("L1644: {0}" -f $L[1644-1])
Write-Host ("L1837: {0}" -f $L[1837-1])
