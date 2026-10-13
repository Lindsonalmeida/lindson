# Xquads — instalação global

Scripts que instalam os squads do [Xquads](https://github.com/ohmyjahh/xquads-squads)
(15 squads, 183 agentes) **na pasta do usuário**, então eles ficam disponíveis no
Claude Code em qualquer projeto, não só em uma pasta.

## Instalar

**Mac / Linux** (Terminal):

```bash
curl -sL https://raw.githubusercontent.com/lindsonalmeida/lindson/claude/global-agent-installation-vdyowf/instalar-xquads.sh | bash
```

**Windows** (PowerShell):

```powershell
irm https://raw.githubusercontent.com/lindsonalmeida/lindson/claude/global-agent-installation-vdyowf/instalar-xquads.ps1 -OutFile $env:TEMP\instalar-xquads.ps1; powershell -ExecutionPolicy Bypass -File $env:TEMP\instalar-xquads.ps1
```

Depois **feche e abra o Claude Code**. Digite `/` e aparecem:

| Comando | O que faz |
|---|---|
| `/xquads` | Chefe geral: você descreve o problema e ele escolhe o squad |
| `/copy-squad`, `/brand-squad`, ... | Ativa o chefe de um squad |
| `/copy-squad:agents:gary-halbert` | Ativa um agente específico |

Rodar o script de novo atualiza para a versão mais recente.

## Remover

- Mac/Linux: `curl -sL <url do .sh acima> | bash -s -- --uninstall`
- Windows: rode o `.ps1` com `-Uninstall`

## Onde fica instalado

| Pasta | Para quê |
|---|---|
| `~/.agents/skills/` | Fonte única (Codex, Gemini CLI e Cursor leem direto) |
| `~/.claude/skills/` | Squads como skills globais do Claude Code |
| `~/.claude/commands/` | Agentes individuais no menu `/` do Claude Code |
