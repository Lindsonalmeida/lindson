# Painel Mova Street (conta Leandro, 18/11/2026)

`python3 montar-mova.py` → `painel-mova.html` + privado `painel/mova-street.html` (rode também `../site/painel-feitas/injetar.py <privado>/painel`).

- `tema-mova.css`: sistema visual único do painel (asfalto + laranja #FF5A1F, Archivo/JetBrains Mono, fio de 1px, sem sombra).
- `agenda-mova.js`: aba Agendamentos (mês/semana, lista do dia, criar/remarcar/cancelar, botões WhatsApp que registram o envio). API `functions/api/agenda.js` (KV `dados:mova-street:agenda`).
- `crm-mova.js`: CRM comercial (kanban arrastável das 9 etapas da estratégia v2 + perdido, lista/filtros, ficha, linha do tempo, follow-up D1/D3/D7/D15/D30 automático, WhatsApp que registra e avança, agendar visita ligado ao lead, link da proposta `?empresa=`, contrato e renovação, 10 telas e exclusividade por ramo, métricas, CSV). Dados em `/api/dados?f=crm`.
- `ferr-mova.json`: Financeiro e Notícias (prototipo/ferramentas.js). `aprov-extra.json` / `arq-extra.json`: cartões e arquivos postos por outras contas (não se perdem ao remontar).

## Lembrete automático no WhatsApp (DESLIGADO)
Endpoint pronto: `POST /api/agenda/lembretes?cli=mova-street` com cabeçalho `x-cron: <AGENDA_CRON>` a cada 15 min (cron-job.org ou Worker com cron).
Manda D-1 às 18h e no dia (2 h antes) para o contato e o responsável. Para ligar, na Cloudflare Pages (variáveis secretas):
`WA_API_URL` (ex.: Z-API `https://api.z-api.io/instances/<ID>/token/<TOKEN>/send-text`), `WA_TOKEN` (Client-Token; cabeçalho em `WA_TOKEN_HEADER`, padrão `Client-Token`) e `AGENDA_CRON`.
Falta: a Mova contratar o número de envio (Z-API ou similar). Sem isso, os botões wa.me cobrem tudo.
