# Robô SDR · instalador do time (conta Pedro, 22/11/2026).
# Cria, para cada número: iniciar-sdrN.cmd e ligar-sdrN.vbs com CAMINHO ABSOLUTO (funcionam mesmo copiados para outra pasta),
# o ícone "Robô SDR N" na Área de Trabalho e o ATALHO na Inicialização do Windows (nunca uma cópia do .cmd).
$ErrorActionPreference = 'Stop'
$pasta = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location $pasta
Write-Host "`n=== Robô SDR: instalação do time ===`nPasta do robô: $pasta`n"
if (-not (Get-Command node -ErrorAction SilentlyContinue)) { Write-Host 'Falta o Node.js. Instale em https://nodejs.org (botão LTS) e rode este instalador de novo.'; exit 1 }
$node = (Get-Command node).Source
do { $q = Read-Host 'Quantos números (chips) vão trabalhar neste PC? (1, 2 ou 3)' } until ($q -match '^[1-3]$')
$nums = 1..[int]$q
$extra = Read-Host 'Algum número já roda em OUTRO PC? Digite quais (ex.: 3) ou só Enter'
if ($extra -match '[1-3]') { $nums = @($nums | Where-Object { $extra -notmatch "$_" }) ; if (-not $nums) { $nums = 1..[int]$q } }
if (-not (Test-Path (Join-Path $pasta 'token.txt'))) {
  $t = Read-Host 'Cole o token do robô (o mesmo de antes; ele fica só neste PC)'
  Set-Content -Path (Join-Path $pasta 'token.txt') -Value $t.Trim() -NoNewline -Encoding ascii
}
Write-Host 'Instalando o necessário (1 a 3 minutos)...'
$env:PUPPETEER_SKIP_DOWNLOAD = 'true'; $env:PUPPETEER_SKIP_CHROMIUM_DOWNLOAD = 'true'
& npm install --no-audit --no-fund | Out-Null
$sh = New-Object -ComObject WScript.Shell
$desk = [Environment]::GetFolderPath('Desktop'); $start = [Environment]::GetFolderPath('Startup')
# limpa os ícones e cópias antigas (inclusive o iniciar.cmd copiado no Startup, que dava MODULE_NOT_FOUND)
foreach ($d in @($desk, $start)) { Get-ChildItem $d -ErrorAction SilentlyContinue | Where-Object { $_.Name -match '^(Rob.*SDR.*\.lnk|iniciar\.cmd|ligar-escondido\.vbs)$' } | Remove-Item -Force }
foreach ($n in $nums) {
  $id = "sdr$n"; $espera = ($n - 1) * 40
  $cmd = Join-Path $pasta "iniciar-$id.cmd"; $vbs = Join-Path $pasta "ligar-$id.vbs"
  @"
@echo off
rem Robô SDR $n (gerado pelo instalar.ps1). Caminho absoluto: funciona de qualquer lugar.
title Robo SDR $n
cd /d "$pasta"
timeout /t $espera /nobreak >nul
:loop
"$node" "$pasta\robo.js" --numero $id
echo Robo SDR $n parou. Reiniciando em 1 minuto...
timeout /t 60 >nul
goto loop
"@ | Set-Content -Path $cmd -Encoding oem
  @"
' Robô SDR $n sem janela preta (use só depois do QR escaneado). Caminho absoluto.
CreateObject("WScript.Shell").Run "cmd /c ""$cmd""", 0, False
"@ | Set-Content -Path $vbs -Encoding ascii
  foreach ($d in @($desk, $start)) {
    $l = $sh.CreateShortcut((Join-Path $d "Robô SDR $n.lnk"))
    $l.TargetPath = $env:ComSpec; $l.Arguments = "/c `"$cmd`""; $l.WorkingDirectory = $pasta
    $l.IconLocation = 'C:\Windows\System32\shell32.dll,24'; $l.WindowStyle = $(if ($d -eq $start) { 7 } else { 1 }); $l.Save()
  }
  Write-Host "Pronto: Robô SDR $n (ícone na Área de Trabalho + liga com o Windows, minimizado)."
}
Write-Host "`nAgora abra cada ícone 'Robô SDR N' da Área de Trabalho, UM POR VEZ, e escaneie o QR que aparece na janela com o celular do chip certo."
