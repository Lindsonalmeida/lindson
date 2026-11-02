# Como cada frente salva o trabalho (para nada se perder se o tempo da conta acabar)

Depois de CADA seção pronta do seu arquivo (não só no fim), rode no repositório /home/user/lindson:

```
cd /home/user/lindson
git add <SEU ARQUIVO>
git commit -m "Maquiavel: <arquivo> — <seção> (conta Zuleide)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01HVWyXQ8DhXpZMrJC5vTM2J"
git pull --rebase -q origin claude/global-agent-installation-vdyowf
git push -q origin HEAD:claude/global-agent-installation-vdyowf
```

- Só `git add` do seu arquivo (outras frentes escrevem ao mesmo tempo). Nunca `git add -A`.
- Se der `index.lock`, `HTTP 429` ou push rejeitado: espere 15 a 30 segundos e repita (até 5 vezes).
- Nunca use `--force`, nunca apague arquivo de outra frente.
- No topo do arquivo, mantenha uma linha "**Situação:** parcial — feito até a seção X" (ou "completo"), para outra conta saber de onde continuar.
