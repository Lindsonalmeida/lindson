# Instala o robô do Instagram no PC do Lindson: pede os tokens uma vez (guardados criptografados), baixa o robô e agenda a cada 15 min + ao entrar no Windows.
# Rodar no PowerShell (sem administrador). Depois testa com -Teste (não publica nada).
$ErrorActionPreference = 'Stop'
[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12
$Pasta = Join-Path $env:LOCALAPPDATA 'RoboInstagram'
New-Item -ItemType Directory -Force -Path $Pasta | Out-Null
$Robo = Join-Path $Pasta 'robo-instagram.ps1'
$Fonte = Join-Path $PSScriptRoot 'robo-instagram.ps1'
if ($PSScriptRoot -and (Test-Path $Fonte)) { Copy-Item $Fonte $Robo -Force }
else { Invoke-WebRequest -UseBasicParsing -Uri 'https://lindsonalmeida.pages.dev/robo/robo-instagram.ps1' -OutFile $Robo }

Write-Host "`n== Robô do Instagram @lindsonalmeida_ ==" -ForegroundColor Cyan
$arq = Join-Path $Pasta 'tokens.xml'
if ((Test-Path $arq) -and (Read-Host 'Já existem tokens salvos. Trocar? (s/N)') -ne 's') { Write-Host 'Mantendo os tokens salvos.' }
else {
  $meta = Read-Host 'Cole o TOKEN DA META (longa duração) e tecle Enter' -AsSecureString
  $robo = Read-Host 'Cole o IG_ROBO_TOKEN (o mesmo salvo na Cloudflare) e tecle Enter' -AsSecureString
  $ig = Read-Host 'ID da conta do Instagram (Enter = 17841443356770777)'
  if (-not $ig) { $ig = '17841443356770777' }
  [pscustomobject]@{ Meta = $meta; Robo = $robo; IgUser = $ig } | Export-Clixml -Path $arq   # DPAPI: só este usuário neste PC abre
  Write-Host 'Tokens guardados criptografados.' -ForegroundColor Green
}

$acao = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -WindowStyle Hidden -File `"$Robo`""
$cada15 = New-ScheduledTaskTrigger -Once -At (Get-Date).Date -RepetitionInterval (New-TimeSpan -Minutes 15) -RepetitionDuration (New-TimeSpan -Days 3650)
$logon = New-ScheduledTaskTrigger -AtLogOn -User "$env:USERDOMAIN\$env:USERNAME"
$cfg = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew -ExecutionTimeLimit (New-TimeSpan -Minutes 45)
Register-ScheduledTask -TaskName 'Robo Instagram Lindson' -Action $acao -Trigger @($cada15, $logon) -Settings $cfg -Description 'Posta a agenda do @lindsonalmeida_ (8h-21h)' -Force | Out-Null
Write-Host 'Tarefa "Robo Instagram Lindson" agendada (a cada 15 min e ao entrar no Windows).' -ForegroundColor Green

Write-Host "`nTeste (não publica nada):" -ForegroundColor Cyan
& powershell.exe -NoProfile -ExecutionPolicy Bypass -File $Robo -Teste
Write-Host "`nPronto. Registro: $Pasta\robo.log" -ForegroundColor Green
