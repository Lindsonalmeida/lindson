# Instala o Builder Squad GLOBALMENTE (Windows) para o Claude Code: funciona em qualquer pasta ou projeto.
#
# O que fica instalado (na sua pasta de usuário, não em um projeto):
#   %USERPROFILE%\.claude\builder-squad\                núcleo (agentes, tasks, workflows, templates, checklists...)
#   %USERPROFILE%\.claude\commands\builder-squad.md     /builder-squad  → Builder Chief (porta de entrada)
#   %USERPROFILE%\.claude\commands\builder-squad\*.md   /builder-squad:<agente>  → cada especialista
#   %USERPROFILE%\.claude\agents\builder-*.md           subagentes (aparecem em /agents)
#   %USERPROFILE%\.claude\skills\builder-squad\SKILL.md skill que ativa o squad quando o assunto for construir app/sistema/agente
#
# Uso (PowerShell):
#   powershell -ExecutionPolicy Bypass -File instalar-builder-squad.ps1             instala/atualiza
#   powershell -ExecutionPolicy Bypass -File instalar-builder-squad.ps1 -Uninstall  remove
param([switch]$Uninstall)
$ErrorActionPreference = 'Stop'

$Zip      = 'https://github.com/ohmyjahh/builder-squad/archive/refs/heads/main.zip'
$Claude   = Join-Path $HOME '.claude'
$Core     = Join-Path $Claude 'builder-squad'
$Cmds     = Join-Path $Claude 'commands'
$CmdDir   = Join-Path $Cmds 'builder-squad'
$Agents   = Join-Path $Claude 'agents'
$Skill    = Join-Path $Claude 'skills\builder-squad'
$CoreTxt  = '~/.claude/builder-squad'

function Remover {
  foreach ($p in @($Core, $CmdDir, $Skill, (Join-Path $Cmds 'builder-squad.md'))) { if (Test-Path $p) { Remove-Item $p -Recurse -Force } }
  if (Test-Path $Agents) { Get-ChildItem $Agents -Filter 'builder-*.md' | Where-Object { (Get-Content $_.FullName -Raw) -match 'builder-squad' } | Remove-Item -Force }
}

if ($Uninstall) { Remover; Write-Host 'Builder Squad removido.'; exit 0 }

$Tmp = Join-Path ([IO.Path]::GetTempPath()) ("builder-squad-" + [guid]::NewGuid())
New-Item -ItemType Directory -Path $Tmp | Out-Null
try {
  Write-Host 'Baixando o Builder Squad...'
  Invoke-WebRequest -Uri $Zip -OutFile "$Tmp\bs.zip" -UseBasicParsing
  Expand-Archive "$Tmp\bs.zip" -DestinationPath $Tmp
  $Origem = Get-ChildItem $Tmp -Directory | Where-Object { Test-Path (Join-Path $_.FullName 'agents') } | Select-Object -First 1
  if (-not $Origem) { throw 'Não encontrei a pasta agents no pacote baixado.' }

  Remover
  foreach ($d in @($Core, $CmdDir, $Agents, $Skill)) { New-Item -ItemType Directory -Force -Path $d | Out-Null }
  Get-ChildItem $Origem.FullName -Force | Where-Object { $_.Name -notin @('.git', '.github', 'tests') } |
    ForEach-Object { Copy-Item $_.FullName -Destination $Core -Recurse -Force }
  Copy-Item (Join-Path $Origem.FullName 'adapters\claude-code') -Destination (Join-Path $Core 'adapter') -Recurse -Force

  $utf8 = New-Object System.Text.UTF8Encoding($false)
  $lista = @()
  foreach ($f in Get-ChildItem (Join-Path $Core 'agents') -Filter '*.md') {
    $txt = Get-Content $f.FullName -Raw -Encoding UTF8
    $id = $f.BaseName
    $titulo = if ($txt -match '(?m)^\s+title:\s*(.+)$') { $Matches[1].Trim('"', ' ') } else { $id }
    $quando = if ($txt -match '(?m)^\s+whenToUse:\s*(.+)$') { $Matches[1].Trim('"', ' ') } else { "Especialista $titulo do Builder Squad." }
    $quando = $quando -replace '"', "'"
    $lista += "- /builder-squad:$id — $titulo"

    $cmd = @"
---
description: Builder Squad · $titulo
argument-hint: [o que você precisa]
---
Ative o agente **$titulo** do Builder Squad.

1. Leia e siga integralmente ``$CoreTxt/agents/$id.md`` (no Windows: ``%USERPROFILE%\.claude\builder-squad\agents\$id.md``).
2. O núcleo do Builder Squad (tasks, workflows, templates, checklists, data, config, schemas) está em ``$CoreTxt/``. Onde as instruções disserem ``.builder-squad/``, use esse caminho.
3. Siga as regras gerais em ``$CoreTxt/adapter/CLAUDE.builder-squad.md``.
4. Grave a memória do projeto (project.yaml, status.yaml, decisions/, handoffs/) na pasta do projeto atual, nunca dentro de ``$CoreTxt/``.

Pedido: `$ARGUMENTS
"@
    [IO.File]::WriteAllText((Join-Path $CmdDir "$id.md"), $cmd, $utf8)

    $nome = if ($id -like 'builder-*') { $id } else { "builder-$id" }
    $sub = @"
---
name: $nome
description: "Builder Squad · $titulo. $quando"
---
Você é o agente $titulo do Builder Squad. Leia e siga integralmente ``$CoreTxt/agents/$id.md`` e use ``$CoreTxt/`` como núcleo canônico (onde estiver ``.builder-squad/``, use esse caminho). Regras gerais: ``$CoreTxt/adapter/CLAUDE.builder-squad.md``. Grave a memória do projeto na pasta do projeto atual.
"@
    [IO.File]::WriteAllText((Join-Path $Agents "$nome.md"), $sub, $utf8)
  }

  $chefe = @"
---
description: Builder Squad · Builder Chief (porta de entrada para criar app, sistema, agente ou automação)
argument-hint: [sua ideia ou demanda]
---
Ative o **Builder Chief** do Builder Squad e comece com ``*start-project``.

1. Leia, nesta ordem: ``$CoreTxt/config/config.yaml``, ``$CoreTxt/data/state-machine.yaml``, ``$CoreTxt/agents/builder-chief.md`` e ``$CoreTxt/adapter/CLAUDE.builder-squad.md``.
2. Use ``$CoreTxt/`` como núcleo canônico (onde estiver ``.builder-squad/``, use esse caminho) e a pasta do projeto atual para a memória do projeto.
3. Primeira pergunta obrigatória: o projeto é para uso interno, para o mercado ou começa interno com intenção futura de venda?

Especialistas disponíveis (também em /builder-squad:<agente>):
$($lista -join "`n")

Demanda: `$ARGUMENTS
"@
  [IO.File]::WriteAllText((Join-Path $Cmds 'builder-squad.md'), $chefe, $utf8)

  $sk = @"
---
name: builder-squad
description: Builder Squad, time de agentes para transformar uma demanda em app, sistema, agente de IA ou automação (uso interno, cliente ou mercado). Use quando o usuário pedir para criar, planejar ou construir um software, sistema, painel, app, agente ou automação, ou citar o Builder Squad ou o Builder Chief.
---
Ative o Builder Chief: leia ``$CoreTxt/agents/builder-chief.md`` e ``$CoreTxt/adapter/CLAUDE.builder-squad.md`` e use ``$CoreTxt/`` como núcleo canônico. Comece perguntando se o projeto é para uso interno, mercado ou híbrido.
"@
  [IO.File]::WriteAllText((Join-Path $Skill 'SKILL.md'), $sk, $utf8)

  Write-Host ''
  Write-Host "Builder Squad instalado globalmente em $Core"
  Write-Host 'No Claude Code, digite /builder-squad para o Builder Chief, ou /builder-squad: para escolher um especialista.'
  Write-Host 'Reinicie o Claude Code (ou abra uma nova conversa) para os comandos aparecerem.'
}
finally { Remove-Item $Tmp -Recurse -Force -ErrorAction SilentlyContinue }
