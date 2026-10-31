#!/usr/bin/env bash
# Instala o Builder Squad GLOBALMENTE (Mac/Linux) para o Claude Code: funciona em qualquer pasta ou projeto.
# Mesmo resultado do instalar-builder-squad.ps1 (Windows):
#   ~/.claude/builder-squad/                 núcleo
#   ~/.claude/commands/builder-squad.md      /builder-squad  → Builder Chief
#   ~/.claude/commands/builder-squad/*.md    /builder-squad:<agente>
#   ~/.claude/agents/builder-*.md            subagentes (/agents)
#   ~/.claude/skills/builder-squad/SKILL.md  skill
# Uso: bash instalar-builder-squad.sh            instala/atualiza
#      bash instalar-builder-squad.sh --remover  remove
set -euo pipefail
ZIP=${BS_ZIP:-https://github.com/ohmyjahh/builder-squad/archive/refs/heads/main.zip}
C="$HOME/.claude"; CORE="$C/builder-squad"; CMDS="$C/commands"; CMDDIR="$CMDS/builder-squad"; AG="$C/agents"; SK="$C/skills/builder-squad"
T='~/.claude/builder-squad'

remover() {
  rm -rf "$CORE" "$CMDDIR" "$SK" "$CMDS/builder-squad.md"
  [ -d "$AG" ] && grep -l 'builder-squad' "$AG"/builder-*.md 2>/dev/null | xargs -r rm -f
  return 0
}
if [ "${1:-}" = "--remover" ]; then remover; echo "Builder Squad removido."; exit 0; fi

TMP=$(mktemp -d); trap 'rm -rf "$TMP"' EXIT
echo "Baixando o Builder Squad..."
if [ -f "$ZIP" ]; then cp "$ZIP" "$TMP/bs.zip"; (cd "$TMP" && unzip -q bs.zip)
elif curl -fsSL "$ZIP" -o "$TMP/bs.zip"; then (cd "$TMP" && unzip -q bs.zip)
else echo "Download do ZIP recusado; usando git clone."; git clone -q --depth 1 https://github.com/ohmyjahh/builder-squad.git "$TMP/builder-squad-main"; fi
ORIG=$(find "$TMP" -mindepth 1 -maxdepth 1 -type d -exec test -d '{}/agents' ';' -print | head -1)
[ -n "$ORIG" ] || { echo "Não encontrei a pasta agents no pacote."; exit 1; }

remover
mkdir -p "$CORE" "$CMDDIR" "$AG" "$SK"
(cd "$ORIG" && for e in * .gitattributes .gitignore; do case "$e" in .git|.github|tests) ;; *) [ -e "$e" ] && cp -R "$e" "$CORE/";; esac; done)
cp -R "$ORIG/adapters/claude-code" "$CORE/adapter"

LISTA=""
for f in "$CORE"/agents/*.md; do
  id=$(basename "$f" .md)
  titulo=$(grep -m1 -E '^\s+title:' "$f" | sed -E 's/^\s+title:\s*//; s/^"//; s/"$//')
  [ -n "$titulo" ] || titulo="$id"
  quando=$(grep -m1 -E '^\s+whenToUse:' "$f" | sed -E 's/^\s+whenToUse:\s*//; s/^"//; s/"$//; s/"/'"'"'/g')
  [ -n "$quando" ] || quando="Especialista $titulo do Builder Squad."
  LISTA="$LISTA- /builder-squad:$id — $titulo
"
  cat > "$CMDDIR/$id.md" <<EOF
---
description: Builder Squad · $titulo
argument-hint: [o que você precisa]
---
Ative o agente **$titulo** do Builder Squad.

1. Leia e siga integralmente \`$T/agents/$id.md\`.
2. O núcleo do Builder Squad (tasks, workflows, templates, checklists, data, config, schemas) está em \`$T/\`. Onde as instruções disserem \`.builder-squad/\`, use esse caminho.
3. Siga as regras gerais em \`$T/adapter/CLAUDE.builder-squad.md\`.
4. Grave a memória do projeto (project.yaml, status.yaml, decisions/, handoffs/) na pasta do projeto atual, nunca dentro de \`$T/\`.

Pedido: \$ARGUMENTS
EOF
  nome=$id; case "$id" in builder-*) ;; *) nome="builder-$id";; esac
  cat > "$AG/$nome.md" <<EOF
---
name: $nome
description: "Builder Squad · $titulo. $quando"
---
Você é o agente $titulo do Builder Squad. Leia e siga integralmente \`$T/agents/$id.md\` e use \`$T/\` como núcleo canônico (onde estiver \`.builder-squad/\`, use esse caminho). Regras gerais: \`$T/adapter/CLAUDE.builder-squad.md\`. Grave a memória do projeto na pasta do projeto atual.
EOF
done

cat > "$CMDS/builder-squad.md" <<EOF
---
description: Builder Squad · Builder Chief (porta de entrada para criar app, sistema, agente ou automação)
argument-hint: [sua ideia ou demanda]
---
Ative o **Builder Chief** do Builder Squad e comece com \`*start-project\`.

1. Leia, nesta ordem: \`$T/config/config.yaml\`, \`$T/data/state-machine.yaml\`, \`$T/agents/builder-chief.md\` e \`$T/adapter/CLAUDE.builder-squad.md\`.
2. Use \`$T/\` como núcleo canônico (onde estiver \`.builder-squad/\`, use esse caminho) e a pasta do projeto atual para a memória do projeto.
3. Primeira pergunta obrigatória: o projeto é para uso interno, para o mercado ou começa interno com intenção futura de venda?

Especialistas disponíveis (também em /builder-squad:<agente>):
$LISTA
Demanda: \$ARGUMENTS
EOF

cat > "$SK/SKILL.md" <<EOF
---
name: builder-squad
description: Builder Squad, time de agentes para transformar uma demanda em app, sistema, agente de IA ou automação (uso interno, cliente ou mercado). Use quando o usuário pedir para criar, planejar ou construir um software, sistema, painel, app, agente ou automação, ou citar o Builder Squad ou o Builder Chief.
---
Ative o Builder Chief: leia \`$T/agents/builder-chief.md\` e \`$T/adapter/CLAUDE.builder-squad.md\` e use \`$T/\` como núcleo canônico. Comece perguntando se o projeto é para uso interno, mercado ou híbrido.
EOF

echo ""
echo "Builder Squad instalado globalmente em $CORE"
echo "No Claude Code, digite /builder-squad para o Builder Chief, ou /builder-squad: para escolher um especialista."
echo "Reinicie o Claude Code (ou abra uma nova conversa) para os comandos aparecerem."
