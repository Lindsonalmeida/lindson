#!/usr/bin/env bash
# Instala os squads do Xquads GLOBALMENTE (Mac/Linux) para o Claude Code e
# demais agentes compatíveis, em qualquer pasta ou projeto.
#
# O que fica instalado:
#   ~/.agents/skills/<squad>     fonte única (lida por Codex, Gemini CLI, Cursor)
#   ~/.claude/skills/<squad>     link → aparece como /<squad> no Claude Code
#   ~/.claude/commands/<squad>/  cada agente vira /<squad>:agents:<agente>
#   ~/.claude/commands/xquads.md /xquads — chefe geral que escolhe o squad
#
# Uso:
#   bash instalar-xquads.sh               instala/atualiza tudo
#   bash instalar-xquads.sh --uninstall   remove
set -euo pipefail

REPO="https://github.com/ohmyjahh/xquads-squads.git"

command -v git >/dev/null || { echo "ERRO: instale o git primeiro." >&2; exit 1; }

TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT
echo "Baixando o Xquads..."
git clone --depth 1 "$REPO" "$TMP/xquads-squads" >/dev/null 2>&1

# Garante que o Claude Code seja detectado mesmo se ainda não foi aberto.
mkdir -p "$HOME/.claude"

if [ "${1:-}" = "--uninstall" ]; then
  bash "$TMP/xquads-squads/install.sh" --uninstall
else
  bash "$TMP/xquads-squads/install.sh" --claude-commands
  echo "Pronto. Feche e abra o Claude Code e digite / para ver os squads e agentes."
fi
