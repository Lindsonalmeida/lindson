# Painel Mova Street (conta Leandro, 18/11/2026)

`python3 montar-mova.py` → `painel-mova.html` + privado `painel/mova-street.html` (rode também `../site/painel-feitas/injetar.py <privado>/painel`).

- `tema-mova.css`: sistema visual único do painel (asfalto + laranja #FF5A1F, Archivo/JetBrains Mono, fio de 1px, sem sombra).
- `agenda-mova.js`: aba Agendamentos (mês/semana, lista do dia, criar/remarcar/cancelar, botões WhatsApp que registram o envio). API `functions/api/agenda.js` (KV `dados:mova-street:agenda`).
- `crm-mova.js`: CRM comercial (kanban arrastável das 9 etapas da estratégia v2 + perdido, lista/filtros, ficha, linha do tempo, follow-up D1/D3/D7/D15/D30 automático, WhatsApp que registra e avança, agendar visita ligado ao lead, link da proposta `?empresa=`, contrato e renovação, pacote de 10 telas por 30 dias com valor = pacote × meses (+50% com exclusividade, mínimo 6 meses), vagas na programação e exclusividade por ramo, métricas, CSV). Dados em `/api/dados?f=crm`.
- `ferr-mova.json`: Financeiro e Notícias (prototipo/ferramentas.js). `aprov-extra.json` / `arq-extra.json`: cartões e arquivos postos por outras contas (não se perdem ao remontar).

## Lembrete automático no WhatsApp (DESLIGADO)
Endpoint pronto: `POST /api/agenda/lembretes?cli=mova-street` com cabeçalho `x-cron: <AGENDA_CRON>` a cada 15 min (cron-job.org ou Worker com cron).
Manda D-1 às 18h e no dia (2 h antes) para o contato e o responsável. Para ligar, na Cloudflare Pages (variáveis secretas):
`WA_API_URL` (ex.: Z-API `https://api.z-api.io/instances/<ID>/token/<TOKEN>/send-text`), `WA_TOKEN` (Client-Token; cabeçalho em `WA_TOKEN_HEADER`, padrão `Client-Token`) e `AGENDA_CRON`.
Falta: a Mova contratar o número de envio (Z-API ou similar). Sem isso, os botões wa.me cobrem tudo.

## Aba "Dados e Vendas" (menu "Dados", 19–20/11/2026)
Arquivos próprios: `aba-dados.js` (tela) + `dados-vendas.json` (conteúdo com fonte). O `montar-mova.py` só injeta os dois (bloco "7"). Números da equipe salvos em `/api/dados?cli=mova-street&f=vendas` (chave `vendas` liberada em `functions/api/dados.js`), mesmo mecanismo versionado do CRM; sem internet, fica no aparelho.
- **Mercado:** 11 dados com fonte e link, conferidos na página da fonte em 19/11/2026 (Cenp-Meios, IAB/Ibope, MAGNA/Uber, OAAA/Harris, Datafolha, IBGE PNAD e Estimativas 2026, Fecomércio-MA, Censo 2022). Não entrou (não confirmado): frota de veículos de São Luís, tempo de deslocamento só da Ilha, consumo por bairro, alcance de OOH da Kantar (dado de 2022).
- **Métricas:** semana (contatos, mapas, propostas, fechamentos, renovações, contratos que venceram, pacotes pagos) + mês (receita e metas). Taxas, gráfico das 8 semanas, semana × anterior, CSV e "Puxar do CRM". Começa vazio.
- **Perspectivas:** 3 tendências (WOO 2026, Uber 2º tri 2026) e datas fortes de São Luís com prazo ideal para vender.
- **Aplicar às vendas:** lembrete fixo (sem promessa de alcance; TSE proíbe propaganda eleitoral em carro de app), calculadora por dia só com a tabela oficial (pacote 10 telas/30 dias; adesivo até R$ 15/dia por carro = R$ 450 ÷ 30), 6 ramos com frase PADRAO-COPY e 6 objeções.

### Time (contribuição de cada um)
- **Data Squad (Data Chief → Avinash Kaushik):** métrica principal = **pacotes de telas pagos** (a mesma do CRM). Teste "e daí?": cada número tem dono e ação; taxa só com denominador real (renovação ÷ contratos que venceram); nada de vaidade (alcance, visualização).
- **Builder Squad (Builder Chief, Frontend, Data Architect):** módulo isolado, sem mexer no CRM; dados mínimos `{semanas:{segunda:{...}}, meses:{AAAA-MM:{...}}}`; 409 junta e tenta de novo; estados vazio, carregando, sem conexão; teclado e leitores de tela no gráfico.
- **Hormozi Closer:** objeções pelo "por trás" (a dúvida real) e preço por dia; nunca pressão.
- **Copy Squad (Copy Chief) + PADRAO-COPY:** frases de WhatsApp conexão → dor → desejo → pergunta, até 280 caracteres, sem preço nem link.
- **Maquiavel:** nada de promessa de alcance, não vender espaço para candidato (TSE), exclusividade só com contrato de 6 meses, sem plano de vendas aqui (outra frente).
- **Webdesigner:** pesquisa em `referencias-dados/` (9 referências de 5 países). Escolhidas: Our World in Data (UK, fonte sob cada número), Plausible (Estônia, painel escuro com variação e barras finas), Ramp Economics Lab (EUA, número grande editorial com rótulo mono). Descartadas: Attio (cartões flutuantes = cara de vibe code), Pitch (degradê roxo), Nexo (colorido demais), Stripe (carta clara), Linear e Datawrapper (só herói/blog). The Economist bloqueou a captura.
