# Religa os 3 robôs SDR (conta Zuleide, 22/11/2026). Cole no PowerShell do PC.
# 1) acha a pasta do robô  2) fecha os robôs  3) aplica o robo-sdr.zip mais novo de Downloads (sem apagar token.txt e .wwebjs_auth)
# 4) corrige config.json (30/dia, todo dia)  5) abre sdr1, sdr2, sdr3 com 40 s entre eles
$ErrorActionPreference = 'Stop'
$pasta = Get-ChildItem "$env:USERPROFILE\Desktop","$env:USERPROFILE\OneDrive\Desktop","$env:USERPROFILE\Downloads","$env:USERPROFILE\Documents","C:\" -Filter robo.js -Recurse -Depth 4 -ErrorAction SilentlyContinue |
  Where-Object { Test-Path (Join-Path $_.DirectoryName 'config.json') } | Sort-Object LastWriteTime -Descending | Select-Object -First 1 | ForEach-Object DirectoryName
if (-not $pasta) { Write-Host 'Nao achei a pasta do robo (robo.js).' -ForegroundColor Red; return }
Write-Host "Pasta do robo: $pasta"
Get-CimInstance Win32_Process -Filter "Name='node.exe'" | Where-Object { $_.CommandLine -match 'robo\.js' } | ForEach-Object { Stop-Process -Id $_.ProcessId -Force }
Get-Process cmd -ErrorAction SilentlyContinue | Where-Object { $_.MainWindowTitle -like 'Robo sdr*' } | Stop-Process -Force
$zip = Get-ChildItem "$env:USERPROFILE\Downloads" -Filter 'robo-sdr*.zip' -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
if ($zip) {
  $tmp = Join-Path $env:TEMP 'robo-sdr-novo'; Remove-Item $tmp -Recurse -Force -ErrorAction SilentlyContinue
  Expand-Archive $zip.FullName $tmp -Force
  $src = (Get-ChildItem $tmp -Filter robo.js -Recurse | Select-Object -First 1).DirectoryName
  Get-ChildItem $src -Force | Where-Object { $_.Name -notin 'token.txt','.wwebjs_auth','.wwebjs_cache','node_modules' } | Copy-Item -Destination $pasta -Recurse -Force
  Write-Host "Atualizado com $($zip.Name)"
} else { Write-Host 'Sem robo-sdr.zip em Downloads: so corrijo o config e religo.' -ForegroundColor Yellow }
$cfgPath = Join-Path $pasta 'config.json'; $cfg = Get-Content $cfgPath -Raw | ConvertFrom-Json
foreach ($n in 'sdr1','sdr2','sdr3') { if ($cfg.$n) { $cfg.$n.teto = 30; $cfg.$n.inicial = 30; $cfg.$n.aumento = 0; $cfg.$n.fim_de_semana = $true } }
$cfg | ConvertTo-Json -Depth 10 | Set-Content $cfgPath -Encoding UTF8
Set-Location $pasta
if (-not (Test-Path 'node_modules')) { npm install }
foreach ($n in 'sdr1','sdr2','sdr3') {
  Start-Process cmd -ArgumentList "/k title Robo $n && cd /d `"$pasta`" && node robo.js --numero $n"
  Write-Host "Abri $n"; if ($n -ne 'sdr3') { Start-Sleep 40 }
}
Write-Host 'Pronto. Se alguma janela pedir QR, escaneie com o chip daquele numero.' -ForegroundColor Green
