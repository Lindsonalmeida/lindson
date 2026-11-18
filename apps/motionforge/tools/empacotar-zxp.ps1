# MotionForge - gera o instalador assinado .zxp (Windows)
# Uso: powershell -ExecutionPolicy Bypass -File tools\empacotar-zxp.ps1 [-Senha "suaSenha"]
# Resultado: dist\MotionForge-<versao>.zxp  (instale com o ZXP Installer da aescripts)
param([string]$Senha = "motionforge")
$ErrorActionPreference = "Stop"
$raiz = Split-Path -Parent $PSScriptRoot
$src = Join-Path $raiz "com.motionforge.panel"
$dist = Join-Path $raiz "dist"
$stage = Join-Path $dist "stage\com.motionforge.panel"
$tools = Join-Path $dist "bin"
New-Item -ItemType Directory -Force -Path $dist, $tools | Out-Null

[xml]$m = Get-Content (Join-Path $src "CSXS\manifest.xml")
$versao = $m.ExtensionManifest.ExtensionBundleVersion

# 1. ZXPSignCmd oficial da Adobe (Adobe-CEP/CEP-Resources)
$zxp = Join-Path $tools "ZXPSignCmd.exe"
if (-not (Test-Path $zxp)) {
  Write-Host "Baixando ZXPSignCmd 4.1.3..."
  Invoke-WebRequest "https://raw.githubusercontent.com/Adobe-CEP/CEP-Resources/master/ZXPSignCMD/4.1.3/x64/ZXPSignCmd.exe" -OutFile $zxp
}

# 2. Pasta limpa (sem testes, sem .debug)
if (Test-Path (Join-Path $dist "stage")) { Remove-Item (Join-Path $dist "stage") -Recurse -Force }
New-Item -ItemType Directory -Force -Path $stage | Out-Null
robocopy $src $stage /E /XD tests node_modules /XF .debug /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "Falha ao copiar (robocopy $LASTEXITCODE)" }

# 3. Certificado autoassinado (uso interno). Guarde o .p12: atualizacoes precisam do mesmo.
$cert = Join-Path $dist "motionforge-cert.p12"
if (-not (Test-Path $cert)) {
  & $zxp -selfSignedCert BR MA "Lindson Almeida" MotionForge $Senha $cert
  if ($LASTEXITCODE -ne 0) { throw "Falha ao criar o certificado" }
}

# 4. Assinar
$out = Join-Path $dist "MotionForge-$versao.zxp"
if (Test-Path $out) { Remove-Item $out -Force }
& $zxp -sign $stage $out $cert $Senha -tsa http://timestamp.digicert.com
if ($LASTEXITCODE -ne 0) {
  Write-Host "Sem servidor de carimbo de tempo; assinando sem -tsa..." -ForegroundColor Yellow
  & $zxp -sign $stage $out $cert $Senha
  if ($LASTEXITCODE -ne 0) { throw "Falha ao assinar" }
}
& $zxp -verify $out
Write-Host ""
Write-Host "Pronto: $out" -ForegroundColor Green
