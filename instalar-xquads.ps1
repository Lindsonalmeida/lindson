# Instala os squads do Xquads GLOBALMENTE (Windows) para o Claude Code e
# demais agentes compatíveis, em qualquer pasta ou projeto.
#
# O que fica instalado:
#   %USERPROFILE%\.agents\skills\<squad>      fonte única (Codex, Gemini CLI, Cursor)
#   %USERPROFILE%\.claude\skills\<squad>      aparece como /<squad> no Claude Code
#   %USERPROFILE%\.claude\commands\<squad>\   cada agente vira /<squad>:agents:<agente>
#   %USERPROFILE%\.claude\commands\xquads.md  /xquads — chefe geral que escolhe o squad
#
# Uso (PowerShell):
#   powershell -ExecutionPolicy Bypass -File instalar-xquads.ps1             instala/atualiza
#   powershell -ExecutionPolicy Bypass -File instalar-xquads.ps1 -Uninstall  remove
param([switch]$Uninstall)
$ErrorActionPreference = 'Stop'

$Zip      = 'https://github.com/ohmyjahh/xquads-squads/archive/refs/heads/main.zip'
$Hub      = Join-Path $HOME '.agents\skills'
$Skills   = Join-Path $HOME '.claude\skills'
$Commands = Join-Path $HOME '.claude\commands'

$Tmp = Join-Path ([IO.Path]::GetTempPath()) ("xquads-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $Tmp | Out-Null
try {
  Write-Host 'Baixando o Xquads...'
  Invoke-WebRequest -Uri $Zip -OutFile "$Tmp\xquads.zip" -UseBasicParsing
  Expand-Archive "$Tmp\xquads.zip" -DestinationPath $Tmp
  $Origem = Join-Path $Tmp 'xquads-squads-main'

  # Um squad é toda pasta com SKILL.md na raiz.
  $Squads = Get-ChildItem $Origem -Directory |
    Where-Object { Test-Path (Join-Path $_.FullName 'SKILL.md') } |
    ForEach-Object { $_.Name }

  foreach ($dir in @($Hub, $Skills, $Commands)) {
    New-Item -ItemType Directory -Force -Path $dir | Out-Null
    foreach ($s in $Squads) {
      $alvo = Join-Path $dir $s
      # Só substitui o que veio do Xquads (tem SKILL.md); nunca apaga skills de terceiros.
      if (Test-Path $alvo) {
        if (Test-Path (Join-Path $alvo 'SKILL.md')) { Remove-Item $alvo -Recurse -Force }
        else { Write-Warning "pulei $alvo (já existe e não é do Xquads)"; continue }
      }
      if (-not $Uninstall) { Copy-Item (Join-Path $Origem $s) $alvo -Recurse }
    }
  }

  $Entrada = Join-Path $Commands 'xquads.md'
  if ($Uninstall) {
    if (Test-Path $Entrada) { Remove-Item $Entrada -Force }
    Write-Host 'Xquads removido.'
  } else {
    Copy-Item (Join-Path $Origem 'xquads\command-entry.md') $Entrada -Force
    Write-Host "$($Squads.Count) squads instalados."
    Write-Host 'Pronto. Feche e abra o Claude Code e digite / para ver os squads e agentes.'
  }
} finally {
  Remove-Item $Tmp -Recurse -Force -ErrorAction SilentlyContinue
}
