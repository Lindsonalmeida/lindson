# Consultar antes de fazer (regra do Lindson, 07/11/2026)

Vale para todas as contas (Lindson, Zuleide, Pedro, Leandro) e todas as sessões, inclusive as abertas em paralelo.

"Nunca mais faça nada sem perguntar ao repositório, e aprender o que já foi feito. Nunca repita algo que já foi feito." (Lindson, 07/11/2026)

## Antes de qualquer ação, nesta ordem
1. `git pull --rebase` na branch da equipe e `git log --oneline -30` (também `git log --all --oneline --grep="<cliente ou tema>"`).
2. Procure o que já existe: `git grep -i "<tema>"` e as pastas do cliente em `agencia/clientes/<cliente>/` e `agencia/sistema-clientes/<cliente>/`.
3. Leia a `MEMORIA-DO-LINDSON.md` (decisões e pedidos anteriores), o `TRAVA-MAQUIAVEL.md` (escopo e status do projeto) e o `QUADRO-DA-EQUIPE.md` (quem está fazendo o quê).
4. Se o item já existe, não refaça. Diga ao Lindson: "Isso já existe em [caminho], feito pela conta X em DD/MM." Só faça uma versão nova se ele pedir.
5. Se o item existe mas está incompleto, continue a partir dele (versão 2, 3…) e diga o que mudou.

## Pedido que parece novo
- Confirme no repositório antes de criar pasta, site, repositório, painel ou arte.
- Se houver dúvida se é a mesma coisa, pergunte ao Lindson uma vez, antes de começar.

## Sessões abertas em paralelo
- Antes de criar ou mover qualquer coisa, conferir o que as outras sessões já commitaram (`git log` da branch).
- Não mover, refazer nem recriar o que outra sessão ou conta já entregou. Nunca tocar em algo de outro cliente.
