#!/usr/bin/env bash
# Instala o Builder Squad de forma GLOBAL (vale em qualquer pasta e projeto).
#   bash ferramentas/instalar-builder-squad.sh            instala ou atualiza
#   bash ferramentas/instalar-builder-squad.sh --remover  desinstala
# Núcleo em ~/.builder-squad. Cada agente vira uma skill em ~/.agents/skills,
# ligada em ~/.claude/skills, e aparece no "/" do Claude Code.
set -euo pipefail
REPO="https://github.com/ohmyjahh/builder-squad.git"
NUCLEO="$HOME/.builder-squad"
HUB="$HOME/.agents/skills"
CLAUDE="$HOME/.claude/skills"

if [ "${1:-}" = "--remover" ]; then
  for d in "$HUB"/builder-* "$CLAUDE"/builder-*; do
    [ -e "$d" ] || [ -L "$d" ] || continue
    if [ -L "$d" ] || [ -f "$d/.builder-squad-global" ]; then rm -rf "$d"; fi
  done
  rm -rf "$NUCLEO"
  echo "Builder Squad removido."; exit 0
fi

if [ -d "$NUCLEO/.git" ]; then
  git -C "$NUCLEO" pull -q --ff-only
else
  rm -rf "$NUCLEO"; git clone -q --depth 1 "$REPO" "$NUCLEO"
fi

campo() { sed -n "s/^  $2: *//p" "$1" | head -1 | sed 's/^"//;s/"$//'; }

criar() { # id nome titulo quando arquivo-do-agente
  local id="$1" dir="$HUB/$1"
  rm -rf "$dir"; mkdir -p "$dir"; touch "$dir/.builder-squad-global"
  local desc="Builder Squad · $3 ($2). $4"
  desc="${desc//\"/\'}"
  cat > "$dir/SKILL.md" <<SK
---
name: $id
description: "$desc"
---
# $3 · Builder Squad

Você vai atuar como **$2**, $3 do Builder Squad.

O núcleo do Builder Squad está instalado globalmente em \`$NUCLEO\`. Use essa pasta como núcleo canônico, sempre que as instruções falarem em \`.builder-squad/\`.

1. Leia e siga \`$NUCLEO/adapters/claude-code/CLAUDE.builder-squad.md\`.
2. Leia a sua definição completa em \`$5\`.
3. Siga as tasks em \`$NUCLEO/tasks/\`, os workflows em \`$NUCLEO/workflows/\` e os gates em \`$NUCLEO/checklists/\`, com leitura progressiva.
4. A memória do projeto (project.yaml, status.yaml, decisions/, handoffs/) fica na pasta do projeto atual, nunca dentro de \`$NUCLEO\`. A CLI roda com \`node $NUCLEO/scripts/builder-squad.mjs <comando>\`.

Pedido do usuário: \$ARGUMENTS
SK
  mkdir -p "$CLAUDE"
  rm -rf "$CLAUDE/$id"; ln -s "$dir" "$CLAUDE/$id"
}

n=0
for f in "$NUCLEO"/agents/*.md; do
  base="$(basename "$f" .md)"
  nome="$(campo "$f" name)"; titulo="$(campo "$f" title)"; quando="$(campo "$f" whenToUse)"
  if [ "$base" = "builder-chief" ]; then id="builder-squad"; quando="Porta de entrada: diagnostica a demanda e conduz a criação de app, sistema, agente ou automação. $quando"
  else id="builder-$base"; fi
  criar "$id" "${nome:-$base}" "${titulo:-$base}" "$quando" "$f"
  echo "  ✓ /$id"; n=$((n+1))
done
echo "$n agentes do Builder Squad instalados. Reinicie o Claude Code e digite /builder"
