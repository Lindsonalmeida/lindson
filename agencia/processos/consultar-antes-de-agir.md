# Consultar o repositório antes de agir (regra do Lindson, 07/11/2026)

**Regra (dita pelo Lindson em 07/11/2026, vale para todas as contas): nunca faça nada sem antes consultar o repositório, e aprenda o que já foi feito.**

## Antes de qualquer ação (criar, editar, publicar, responder)
1. `git pull` no branch da equipe (`claude/elegant-goodall-6s5brw`) e nos branches de `origin/`.
2. Procure o que já existe: `git grep` pelo nome do cliente, do item e do arquivo; `git log --grep` pelo assunto; `git log --all --since=<data>`.
3. Leia o registro: `QUADRO-DA-EQUIPE.md` (em andamento), `REGISTRO-DAS-CONTAS.md` (entregas), `TRAVA-MAQUIAVEL.md` (escopo e decisões), `MEMORIA-DO-LINDSON.md` (o que foi aprovado e reprovado).
4. Se já existe: **não refaça**. Diga ao Lindson o que existe, quem fez e onde está, e continue dali.
5. Se não existe: confirme no registro e só então faça. Se o pedido conflita com o que está no repositório, pergunte ao Lindson antes de mudar.

## Depois de agir
- Commit e push na branch da equipe, com linha no `REGISTRO-DAS-CONTAS.md` e atualização do quadro.
- Se criou algo que o cliente vai ver, confira que nada interno aparece para ele (decisões, notas de equipe, nomes não confirmados).

## Por que existe
Em 07/11 duas contas refizeram trabalho já pronto (painel do Tribuna, painel do curso, números de redes) e um recado de outra sessão mudou nomes sem conferir o registro. Consultar primeiro evita isso.
