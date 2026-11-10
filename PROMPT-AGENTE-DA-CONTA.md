# Prompt: transformar cada conta da equipe em agente (Lindson, 10/11/2026)

Cole o texto abaixo numa conversa da conta, trocando NOME e CONTA. As contas são Lindson (`lindsonmkt`), Pedro (`passaportedabiblia`) e Leandro (`raposaeleaomq`). A Zuleide já fez a dela em `.claude/agents/zuleide.md`, que serve de modelo.

---

Você é a conta NOME (CONTA) da equipe do Lindson. Faça isto sem me perguntar nada:

1. Leia a nossa conversa inteira, desde o início, e tudo o que a conta NOME fez no repositório. Use `git log --all --author` e as linhas "(conta NOME)" no REGISTRO-DAS-CONTAS.md, no QUADRO-DA-EQUIPE.md, na MEMORIA-DO-LINDSON.md e no ESTADO-DO-PROJETO.md.
2. Leia o CLAUDE.md, a MEMORIA-DO-LINDSON.md, o MAPA-DO-REPOSITORIO.md, todos os agentes em `.claude/agents/` (o `zuleide.md` é o modelo) e os processos em `agencia/processos/`. No privado CentralLindsonALmeida, leia o CLAUDE.md, as skills em `.claude/skills/` e o índice `dados/agencia/referencias/README.md`.
3. Aprenda como eu ensino e o que eu peço: resposta curta, procurar antes de perguntar, usar os agentes, automatizar sem pedir permissão, nada pago sem eu pedir, e as aprovações e reprovações.
4. Crie o agente `.claude/agents/nome-da-conta.md` no mesmo formato do `zuleide.md`, com estas partes:
   - como o Lindson ensina;
   - as regras aprendidas;
   - as ferramentas e os cuidados;
   - as entregas desta conta;
   - o fecho de tarefa.
   Inclua só o que for específico desta conta e aponte para os arquivos de origem. Não repita o que já está no CLAUDE.md.
5. Se aprender algo útil para os outros agentes (Peter, Designer gráfico, Webdesigner, Social media, Paollo, Rocco), agregue em poucas linhas a cada um, citando a fonte e a data.
6. Acrescente uma linha no MAPA-DO-REPOSITORIO.md e no REGISTRO-DAS-CONTAS.md e faça commit e push no branch `claude/global-agent-installation-vdyowf`.
7. Me responda em 3 linhas: o caminho do agente e as 3 coisas mais importantes que você aprendeu.
