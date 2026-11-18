# MotionForge - instalador para Windows (sem precisar de administrador)
# Uso: clique com o botao direito > "Executar com o PowerShell"  (ou rode INSTALAR.bat)
# Opcoes: -Gpu (instala rembg com GPU NVIDIA)  -SemPython  -SemFfmpeg  -BaixarModelo
param([switch]$Gpu, [switch]$SemPython, [switch]$SemFfmpeg, [switch]$BaixarModelo)
$ErrorActionPreference = "Stop"
function Passo($t) { Write-Host ""; Write-Host "==> $t" -ForegroundColor Cyan }
function Ok($t) { Write-Host "    OK  $t" -ForegroundColor Green }
function Aviso($t) { Write-Host "    !!  $t" -ForegroundColor Yellow }

$raiz = Split-Path -Parent $PSScriptRoot
$src = Join-Path $raiz "com.motionforge.panel"
if (-not (Test-Path (Join-Path $src "CSXS\manifest.xml"))) { throw "Pasta com.motionforge.panel nao encontrada ao lado de tools\." }

Passo "1/5 Liberando extensoes nao assinadas (PlayerDebugMode)"
foreach ($v in "11","12") { & reg add "HKCU\Software\Adobe\CSXS.$v" /v PlayerDebugMode /t REG_SZ /d 1 /f | Out-Null }
Ok "CSXS.11 e CSXS.12 = 1"

Passo "2/5 Copiando o painel para a pasta de extensoes do usuario"
$dst = Join-Path $env:APPDATA "Adobe\CEP\extensions\com.motionforge.panel"
if (Test-Path $dst) { Remove-Item $dst -Recurse -Force }
New-Item -ItemType Directory -Force -Path $dst | Out-Null
robocopy $src $dst /E /XD tests node_modules /XF .debug /NFL /NDL /NJH /NJS /NP | Out-Null
if ($LASTEXITCODE -ge 8) { throw "Falha ao copiar (robocopy $LASTEXITCODE)" }
Ok $dst

function Achar-Python {
  foreach ($c in @("py","python","python3")) {
    try { $v = & $c --version 2>&1; if ("$v" -match "Python 3") { return $c } } catch {}
  }
  return $null
}

if (-not $SemPython) {
  Passo "3/5 Python + rembg (remover fundo local, gratis)"
  $py = Achar-Python
  if (-not $py) {
    Aviso "Python 3 nao encontrado. Instalando pelo winget..."
    winget install -e --id Python.Python.3.12 --accept-source-agreements --accept-package-agreements
    $env:Path = [Environment]::GetEnvironmentVariable("Path","User") + ";" + [Environment]::GetEnvironmentVariable("Path","Machine")
    $py = Achar-Python
    if (-not $py) { throw "Instale o Python em python.org (marque 'Add python.exe to PATH') e rode este instalador de novo." }
  }
  Ok "Python: $py ($(& $py --version 2>&1))"
  $pacote = if ($Gpu) { "rembg[gpu]" } else { "rembg[cpu]" }
  & $py -m pip install --upgrade pip | Out-Null
  & $py -m pip install --upgrade "$pacote" pillow
  if ($LASTEXITCODE -ne 0) { throw "pip falhou ao instalar $pacote" }
  & $py (Join-Path $dst "python\remove_bg.py") --check
  if ($BaixarModelo) {
    Passo "Baixando o modelo birefnet-general agora (cerca de 1 GB, so uma vez)"
    $tmp = Join-Path $env:TEMP "mf_teste.png"
    & $py -c "from PIL import Image; Image.new('RGB',(64,64),(200,40,40)).save(r'$tmp')"
    & $py (Join-Path $dst "python\remove_bg.py") $tmp ($tmp + ".out.png") birefnet-general
  }
} else { Aviso "Python pulado (-SemPython)" }

if (-not $SemFfmpeg) {
  Passo "4/5 ffmpeg (remover fundo de VIDEO)"
  $ff = Get-Command ffmpeg -ErrorAction SilentlyContinue
  if (-not $ff) {
    Aviso "ffmpeg nao encontrado. Instalando pelo winget..."
    winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
    Aviso "Se o painel ainda nao achar o ffmpeg, feche e abra o After Effects (o PATH novo so vale para programas abertos depois)."
  } else { Ok $ff.Source }
} else { Aviso "ffmpeg pulado (-SemFfmpeg)" }

Passo "5/5 Pronto"
Write-Host "    Abra o After Effects > Janela > Extensoes > MotionForge" -ForegroundColor White
Write-Host "    Na aba Config, cole a chave do fal.ai (fal.ai/dashboard/keys) para Animar e Gerar." -ForegroundColor White
