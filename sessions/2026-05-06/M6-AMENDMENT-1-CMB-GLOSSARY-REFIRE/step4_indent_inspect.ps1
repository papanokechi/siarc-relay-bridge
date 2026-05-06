$L = [System.IO.File]::ReadAllLines("tex\submitted\CMB.txt")
$targets = @(404, 941, 993, 1517)
foreach ($t in $targets) {
    $line = $L[$t - 1]
    $leading = ''
    for ($i = 0; $i -lt $line.Length; $i++) {
        $c = $line[$i]
        if ($c -eq ' ' -or $c -eq "`t") { $leading += $c } else { break }
    }
    Write-Host ("L{0,4}: leading-len={1}, leading-bytes={2}" -f $t, $leading.Length, ((($leading.ToCharArray() | ForEach-Object { '{0:X2}' -f [int][char]$_ }) -join '-')))
    Write-Host ("       content='{0}'" -f $line)
    if ($t + 1 -le $L.Length) {
        $next = $L[$t]
        $nextLeading = ''
        for ($i = 0; $i -lt $next.Length; $i++) {
            $c = $next[$i]
            if ($c -eq ' ' -or $c -eq "`t") { $nextLeading += $c } else { break }
        }
        Write-Host ("       next L{0}: leading-len={1}, content='{2}'" -f ($t + 1), $nextLeading.Length, $next)
    }
}
