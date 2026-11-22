# Robôs e automações da agência (inventário)

Pedido do Lindson (22/11/2026): "conseguimos montar um app de organização pros robôs? pra visualizar em um único lugar?" Feito pela conta Leandro (Builder; webdesigner no visual, Data squad na métrica: **robôs com erro**, a única que pede ação).

**Onde ver:** Central → admin → menu *Minha agência* → **Robôs** (`/painel/admin#robos`). Cartões de números (total, ativos, com erro, parados), filtros por frente, lista ou kanban *Por situação*, última e próxima execução, dono, link para a aba e o arquivo de cada robô, e o motivo quando trava.

## Como atualizar
- Robô novo ou mudança: edite o `CATALOGO` de `gerar_robos.py` (uma linha por robô).
- Rotinas agendadas do Claude (conta Leandro): atualize `gatilhos.json` com o `list_triggers` (última execução e resultado; sem ids nem prompts).
- Rode `python3 agencia/sistema-clientes/robos/gerar_robos.py --repo /home/user/lindson --testar` (lê a última execução nos commits dos dois repositórios e testa só o código HTTP de `/api/automacao` e `/api/sdr`; nenhum segredo é lido).
- Monte: o `site/montar-site.py` chama `site/painel-robos/injetar_robos.py`; avulso: `python3 agencia/sistema-clientes/site/painel-robos/injetar_robos.py /home/user/centrallindsonalmeida/painel/admin.html` e commit no privado.
- Ao vivo, no navegador do admin: o time de SDR (`/api/sdr?robo=1`) e a fila do robô do Instagram (`/api/agenda-ig`). A aba só lê; pausar/ligar números continua na aba SDR (conta Pedro).

## Cloudflare: crons
Nenhum. A Central é Cloudflare **Pages** (Functions sem cron). O que roda sozinho vem do PC do Lindson (robôs SDR e do Instagram), das rotinas agendadas do Claude ou de um agendador externo (lembretes da agenda, ainda desligado).

## Inventário (2026-11-22 15:26 UTC)

| Robô | Frente | O que faz | Onde roda | Dono | Frequência | Última | Situação |
|---|---|---|---|---|---|---|---|
| Robô SDR 1 | Vendas | Manda a mensagem de prospecção no WhatsApp, 1 lead por vez, e conversa com quem responde (follow-ups). | PC do Lindson | Pedro | a cada 4–9 min, 09:00–18:00, todos os dias (30/dia) | 2026-11-22 15:23 | ativo |
| Robô SDR 2 | Vendas | Segundo número do time de SDR: só os leads dele, saudação e pergunta variadas. | PC do Lindson | Pedro | a cada 5–10 min, 09:20–17:40, todos os dias (30/dia) | 2026-11-22 15:17 | ativo |
| Robô SDR 3 | Vendas | Terceiro número do time de SDR. | PC do Lindson | Pedro | a cada 5–11 min, 09:40–17:20, todos os dias (30/dia) | 2026-11-22 15:22 | ativo |
| Pesquisa de leads do SDR | Vendas | Põe leads novos (WhatsApp celular + Instagram, nota 80+) na lista do time de SDR quando ela acaba. | Nuvem Claude | Leandro (coordenação) · Pedro | quando a lista acaba | 2026-11-22 15:23 | ativo |
| SDR Orégano (pizzarias) | Vendas | Lista diária de pizzarias com mensagem pronta no painel da Orégano Turbo; envio pelo botão WhatsApp (cadência). | Nuvem Claude + Central | Zuleide | diária (leads); envio manual | 2026-11-22 10:47 | ativo |
| Real Time · postar 3x ao dia | Postagem | Pega o próximo post APROVADO da Real Time e publica no Instagram pelo Windsor; marca como postado no painel. | Nuvem Claude | Leandro | 09:58, 13:58 e 17:58 | 2026-11-22 12:58 | **com erro**: A Central recusa a chave AUTOMACAO_TOKEN (API 401): não lê as aprovações nem marca o postado. |
| Robô do Instagram @lindsonalmeida_ | Postagem | Publica sozinho a agenda do Instagram do Lindson pela API oficial (post, carrossel, Reels), 4 h entre posts. | PC do Lindson | Pedro | a cada 15 min, 08:00–21:00 | — | atenção: Sem confirmação de que está instalado no PC (precisa do token da Meta e do IG_ROBO_TOKEN). A aba confere ao vivo na fila /api/agenda-ig. |
| Coordenação das equipes | Equipe | Lê o quadro A fazer e os cadernos, divide o trabalho na fila, cobra quem não confirmou e sincroniza o quadro do admin. | Nuvem Claude | Leandro | a cada 2 h, 08:07–22:07 | 2026-11-16 11:07 | **com erro**: A Central recusa a chave AUTOMACAO_TOKEN (API 401): não lê nem atualiza o quadro A fazer da Central (usa só a fila do repositório). Sem sinal há 6.2 dias (esperado a cada 6 h ou menos). |
| Rodada da equipe Lindson (fila) | Equipe | Pega o próximo item livre da fila da equipe Lindson, faz, sobe no painel do cliente e fecha. | Nuvem Claude | Leandro (rotina) · equipe Lindson | a cada 2 h (:36) | 2026-11-22 13:36 | **com erro**: A Central recusa a chave AUTOMACAO_TOKEN (API 401): não lê nem atualiza o quadro A fazer da Central (usa só a fila do repositório). Dispara a cada 2 h, mas não pega item da fila desde 16/11. |
| Agregação horária | Equipe | Verifica de hora em hora o que entrou no repositório e agrega aos agentes e à memória. | Nuvem Claude | Zuleide | de hora em hora (:50) | 2026-11-22 14:51 | ativo |
| Rodadas das equipes Zuleide e Pedro | Equipe | Cada equipe pega o próximo item dela na fila da coordenação a cada 2 h. | Nuvem Claude | Zuleide · Pedro | a cada 2 h | 2026-11-16 14:05 | atenção: Sem sinal há 6.1 dias (esperado a cada 24 h ou menos). |
| VEKTOR (gerente por voz) | Central | Conversa por voz e texto com o Lindson na Central de Comando e cria pedidos para as equipes (Workers AI). | Cloudflare | Leandro · Zuleide | sob demanda | — | ativo |
| Notícias do nicho | Central | Busca notícias do nicho de cada cliente (Google Notícias, reserva Bing) e guarda 3 h. | Cloudflare | Lindson (conta) | sob demanda, cache de 3 h | — | ativo |
| Lembretes da agenda no WhatsApp (Mova Street) | Central | Avisa contato e responsável no WhatsApp (D-1 às 18h e 2 h antes). | Cloudflare + agendador externo | Leandro | a cada 15 min (quando ligado) | — | parado: Desligado: faltam na Cloudflare o provedor de WhatsApp (WA_API_URL, WA_TOKEN) e a senha do agendador (AGENDA_CRON), e um agendador a cada 15 min. |
| Notícias BOMBOU | Parados | Notícias virais do Maranhão e do Brasil para o @bombouof (5 + 5 a cada 3 h). | Nuvem Claude | Leandro | a cada 3 h | 2026-10-27 15:01 | parado: Desligada em 26/10 (limite de uso da conta na última execução). |
| Captação por cidades | Parados | Leads de todos os tipos de negócio, cidade por cidade, no app Recomeço 90. | Nuvem Claude | Leandro | a cada 3 h | 2026-10-26 18:09 | parado: Desligada em 26/10 (limite de uso); substituída pelo time de SDR. |
| Roteiros diários de Reels | Parados | 5 roteiros de Reels de 30 s por dia no app Recomeço 90. | Nuvem Claude | Leandro | diária 05:41 | — | parado: Desligada em 22/10: os 300 roteiros do Teste 01 foram gerados de uma vez. |

## O que destrava (para o Lindson)
1. **Chave AUTOMACAO_TOKEN recusada (API 401)** desde 15/11: a postagem da Real Time roda 3x ao dia mas não lê as aprovações, e a coordenação não lê o quadro A fazer. Conferir na Cloudflare (lindsonalmeida → Variáveis e segredos) que o valor de `AUTOMACAO_TOKEN` é o mesmo salvo como credencial da rede nas sessões do Claude; se trocou, salvar de novo nos dois lugares.
2. **Robô do Instagram**: confirmar se está instalado no PC (token da Meta de 60 dias + `IG_ROBO_TOKEN`).
3. **Lembretes da agenda (Mova Street)**: escolher o provedor de WhatsApp (ex.: Z-API) e criar `WA_API_URL`, `WA_TOKEN` e `AGENDA_CRON`.
4. **Rodadas das equipes** sem pegar item da fila desde 16/11 (as contas estão trabalhando por pedido direto): a coordenação decide se mantém ou desliga.

Fontes: `list_triggers` (conta Leandro), commits dos repositórios `lindson` e `CentralLindsonALmeida`, `functions/api/*.js` do privado, `agencia/processos/time-sdr-whatsapp.md`, `agencia/processos/automacao-operacao.md`, `coordenacao/COORDENACAO.md`.
