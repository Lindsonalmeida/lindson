# Black Friday 2026 · Dra. Jaci Cunha · stories (toxina botulínica + preenchimento)

Conta Pedro, 10/11/2026 (Social media + Designer gráfico + Pedro Sobral). Situação: **aguardando aprovação do Lindson**.
Decisão do Lindson (10/11): **sem preço nos stories e nos anúncios**; a condição é passada no WhatsApp, de forma individual.

## Persona (5 linhas)
1. Mulher de 28 a 50 anos, Zé Doca e cidades vizinhas; professora, servidora, comerciante ou dona de casa com renda própria.
2. Vê os stories à noite, depois de pôr a casa em ordem, ou no intervalo do trabalho; decide pelo WhatsApp.
3. Dor, nas palavras dela: "tenho medo de ficar com a cara parada", "vi promoção barata e fiquei com medo", "não sei se é pra mim".
4. Confia em: rosto da Dra., CRO à vista, explicação simples, ninguém empurrando procedimento.
5. Afasta: preço gritado, "50% OFF", antes e depois de estranha, promessa de "rejuvenescer 10 anos".
Ela compraria? Sim, se a Black Friday parecer **oportunidade com segurança**, não liquidação.

## Conceito
**"O seu rosto não é liquidação."** A Black Friday muda a condição, não o produto, a técnica nem a avaliação (gancho negativo, regra de 22/10). Fecha a coerência com o post d03 de 27/11 ("Segurança não entra em liquidação").

## Os 8 stories (artes em `artes/`, prévia `folha-guia.jpg`, código `stories.html` + `render.js`, vídeos `video.py`)
| # | Composição (copiada de) | Texto principal | Figurinha |
|---|---|---|---|
| 1 | Foto real gigante + "Black Friday" serifada dourada (ref. joalheria de luxo, M. Shakeel) | Toxina botulínica · preenchimento · 23 a 30/11 | **Contagem regressiva** "Black Friday da Dra. Jaci" → 27/11 |
| 2 | Tipografia bordô, palavra riscada (ref. Arbrea "We don't discount our expertise") | O seu rosto não é ~~liquidação~~ | — |
| 3 | Palavra gigante fina + balão (modelo real dela "botox / perguntas") | Toxina botulínica: o que é | — |
| 4 | Faixa caramelo com fio e pontos + checklist (modelo real "Bioestimulador / quando começar?") | Preenchimento com ácido hialurônico | — |
| 5 | Preto, dois cartões A/B | Qual te dá mais vontade? | **Enquete** "Toxina" × "Preenchimento" |
| 6 | Cartões de app em escada (ref. D.Luxe, editorial) | Como funciona: BF26 → avaliação → condição até 30/11 | — |
| 7 | Aspas gigantes, bordô (modelo real "as perguntas que você pensa mas não faz") | Dói? Fica artificial? | **Caixa de perguntas** "Pergunte à Dra. Jaci" |
| 8 | Foto real + degradê vinho | Os horários são poucos. O cuidado, não. Chama no WhatsApp | **Link** wa.me (mensagem abaixo) |

Fotos reais só na 1ª e na última (2º uso no mês das fotos antigas, exceção aprovada em 04/11). As versões "guia" mostram onde vai cada figurinha (caixa verde tracejada); as "limpo" são as que sobem.
**Vídeos:** cada story em MP4 de 8 a 11 s com narração feminina neutra (Francisca, pt-BR), trilha "Inspired" de Kevin MacLeod (incompetech.com, CC BY 4.0) em ducking, whoosh na entrada, zoom lento e flash de luz. Ficam fora do Git (scratchpad e painel).
Crédito (na legenda, quando for vídeo): `Música: "Inspired", Kevin MacLeod (incompetech.com), CC BY 4.0`.

## Calendário (janela 8h–21h, de 4 em 4 h)
| Dia | 08h45 | 12h45 | 16h45 | 20h45 |
|---|---|---|---|---|
| seg 23/11 | S1 capa (contagem) | S2 liquidação | S3 toxina | S5 enquete |
| ter 24/11 | S4 preenchimento | S7 caixa de perguntas | S6 como funciona | S8 WhatsApp |
| qua 25 e qui 26/11 | Dra. Jaci responde a caixa (vídeo dela, selfie) | resultado da enquete | S6 | S8 |
| **sex 27/11** | S1 | S6 | S8 | S2 |
| sáb 28 e dom 29/11 | S8 | resposta da caixa | — | S8 |
| seg 30/11 (último dia) | S8 "último dia" (texto da figurinha) | S6 | S8 | S8 |

## Mensagem pronta do link (figurinha do story 8 e anúncios)
`https://wa.me/559885672646?text=Oi!%20Vi%20a%20Black%20Friday%20da%20Dra.%20Jaci%20e%20quero%20saber%20a%20condi%C3%A7%C3%A3o.%20%5BBF26%5D`
Texto: "Oi! Vi a Black Friday da Dra. Jaci e quero saber a condição. [BF26]"

## Roteiro curto do WhatsApp (orçamento) · PADRAO-COPY + CFO
1. **Boas-vindas** (resposta rápida `/bf`): "Oi! Que bom te ver por aqui 🤍 A Black Friday da Dra. Jaci vai até 30/11. Me conta seu nome e de qual cidade você fala?"
2. **Qual procedimento** (`/bf2`): "Prazer, [nome]! Você pensa em toxina botulínica, preenchimento ou ainda tá em dúvida? Pode falar sem vergonha, aqui ninguém empurra nada."
3. **Dor e confiança** (`/bf3`): "Muita gente tem medo de ficar com o rosto parado ou artificial. Por isso tudo começa com uma avaliação de 30 min com a Dra. Jaci, para ver se é indicado para você."
4. **Condição** (`/bf4`, só humano): "A condição de Black Friday é [CONDIÇÃO DEFINIDA PELA CLÍNICA] e vale para procedimento indicado na avaliação e agendado até 30/11. Resultados variam de pessoa para pessoa."
5. **Agendar** (`/bf5`): "Tenho [dia/hora] ou [dia/hora] para sua avaliação. Qual fica melhor pra você?"
6. **Confirmação na véspera:** usar `/confirma` de `../meta-ads/CAMPANHA.md`.
Nunca no WhatsApp: promessa de resultado, diagnóstico por foto, antes e depois de paciente sem autorização.

## Regras checadas (CFO e Meta)
Sem preço, sem "%", sem "OFF", sem "grátis" nas peças públicas; "toxina botulínica" (nunca a marca); CRO-MA 8514 em todas; "resultados variam" nas telas de procedimento; sem antes e depois; sem agulha ou paciente sendo tratada; sem falar do corpo de quem lê ("você tem rugas?").
**Atenção (CFO):** o Código de Ética veda anunciar preços e promoções de forma que comercialize a odontologia. Por isso a condição só aparece na conversa individual. A Dra. Jaci deve confirmar o texto com o CRO-MA, se tiver dúvida.

## Pesquisa premium (8 referências, 6 países; capturas em `referencias/`)
| # | Referência | País | Escolhida? |
|---|---|---|---|
| 01 | Arbrea Labs, "We Don't Discount Our Expertise" (arbrea-labs.com/black-friday) | Suíça | **Sim**: conceito "o seu rosto não é liquidação" (S2) |
| 05 | Maryam Shakeel, Luxury Jewelry Black Friday Campaign (contra.com) | Paquistão/EUA | **Sim**: retrato editorial + serifada dourada sobre escuro (S1, S8) |
| 07 | D.Luxe Aesthetics, redesign (Talia Przybyszewski) | Reino Unido | **Sim**: serifada itálica editorial e cartões limpos (S6) |
| 02 | Hautestock, roundup "minimalist & elevated" | EUA | Não: genérico de template |
| 03 | Tubik Studio, Black Friday case study | Ucrânia | Não: cartum colorido, fora do tom de clínica |
| 04 | Linearity, Black Friday Instagram Stories | Alemanha | Não: varejo, preço gritado (só a ideia de cartões A/B) |
| 06 | Bisma Iqbal, Luxury Aesthetic Clinic Branding | Paquistão | Não: bege genérico (já reprovado na Jaci) |
| 08 | Marina Terenti, Regen Aesthetics | — | Não: mockup de app, sem rosto |
