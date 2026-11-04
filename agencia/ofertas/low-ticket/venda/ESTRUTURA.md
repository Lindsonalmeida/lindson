# Estrutura de venda dos 5 produtos low ticket: da montagem até a venda

Agente: Estrategista de Growth e Vendas do Builder Squad (Vector), com a base do Hormozi Offers e Pricing (`../hormozi.md`), do Pedro Sobral (`agencia/marca-lindson/ESTRATEGIA.md` §7) e do padrão de copy (`agencia/prospeccao/PADRAO-COPY.md`). Data: 04/11/2026.

**Regras que valem para o documento inteiro:**
- Nenhum número de resultado, de venda ou de depoimento foi inventado. Os únicos números são os que já estão nos arquivos (quantidade de roteiros, páginas, mensagens) e as taxas da Hubla que o Lindson passou (8,9% + R$ 2,49 por venda, **confirmar na página oficial**).
- **O preço é decisão do Lindson.** A faixa ao lado de cada produto é a sugestão do Hormozi Squad (`../hormozi.md`), para teste. Preço nunca vai no feed. Só aparece na página de venda, no checkout e na conversa.
- Toda mensagem curta segue **Conexão → Dor → Desejo → Pergunta**, até 280 caracteres, sem "vi que", "parece que" nem jargão. Na sequência pós-venda o link só vai depois que a pessoa disser sim (a não ser no D0, que é a entrega).
- Legenda: ✔ = já existe (com o caminho) · ✘ = falta fazer · ◐ = existe em parte.
- `CentralLindsonALmeida/` = repositório privado (cópia local em `/home/user/centrallindsonalmeida/`). O resto é este repositório `lindson`.

**Índice:** [A. Ordem de lançamento](#a-ordem-de-lançamento) · [B. Os 5 produtos](#b-os-5-produtos) (1 Kit Mês Pronto · 2 Kit WhatsApp que Fecha · 3 Raio-X do Perfil · 4 Bio que Vende · 5 Kit Prospecção) · [C. Parte comum](#c-parte-comum-a-comunidade-única-na-hubla) (comunidade, passo a passo do Lindson, o que a equipe entrega) · [D. O que falta, em ordem](#d-o-que-falta-em-ordem-de-prioridade)

---

## A. Ordem de lançamento

A nota é a do `../RANKING.md` (estimativa, não pesquisa: a ordem real sai das vendas). Quando a nota empata, ganha o que já está pronto para entregar hoje.

| Ordem | Produto | Nota | Por que nesta posição | Pronto para vender? |
|---|---|---|---|---|
| **1º** | Kit Mês Pronto | 88 (1º do ranking) | Dor nº 1 do público ("não sei o que postar"), PDF de 52 páginas e planilha prontos, os dois agentes (Hormozi e Maquiavel) indicaram primeiro. | Falta só aprovação, preço, página e Hubla |
| **2º** | Kit WhatsApp que Fecha | 83 | Dor nº 2 ("pergunta o preço e some"), PDF e 43 atalhos prontos. É o **upsell natural** do Kit Mês Pronto: o conteúdo traz a conversa, o kit fecha. Lançar junto ou logo depois do 1º. | Falta aprovação, preço, página e Hubla |
| **3º** | Raio-X do Perfil em Vídeo | 85 | Nota alta e vira caixa no mesmo dia, mas depende da hora do Lindson (ele grava um por um, vaga limitada de verdade) e é a ponte para a agência. Entra depois que os dois kits estiverem rodando sozinhos. | Falta formulário, roteiro do vídeo e decisão sobre a avaliação gratuita |
| **4º** | Bio que Vende em 15 Minutos | 85 | Nota alta e o mais barato: é o **order bump** dos outros. Só não vem antes porque só existe o template. Quando o PDF ficar pronto, entra como bump nos checkouts 1, 2 e 3. | Falta o PDF inteiro e o bump (capas de destaque) |
| **5º** | Kit Prospecção pelo WhatsApp | 80 | Público diferente (social media, freelancer, agência pequena), que o feed do Lindson ainda não atrai. Tem o conteúdo e a planilha, falta o PDF. | Falta PDF, página e conteúdo para o público B |

**Resumo:** começar pelos dois kits prontos (dores nº 1 e nº 2, um vende o outro), ligar o Raio-X quando houver tempo na agenda, encaixar a Bio como bump assim que o PDF sair e deixar a Prospecção por último, porque pede outro público.

---

## B. Os 5 produtos

### Estrutura de cada ficha
1. Entregáveis · 2. Oferta · 3. Página de venda · 4. Checkout na Hubla · 5. Entrega · 6. Tráfego e conteúdo · 7. Pós-venda (D0, D1, D3, D7) · 8. Métricas

**Seções da página de venda (iguais nos 5, já é a estrutura do `copy.json`):** topo (pílula + palavra gigante + título + subtítulo + botão) → as 3 dores → a virada → o que você leva (cartões) → como funciona em 3 passos → para quem é / para quem não é → bônus → quem é o Lindson → garantia de 7 dias → perguntas frequentes → chamada final com botão. Preço e botão de checkout ficam em `{{PRECO}}` e `{{CHECKOUT}}` no `copy.json` até o Lindson decidir.
Fonte do texto das 5 páginas: `CentralLindsonALmeida/produtos/landing/copy.json` ✔. **As páginas em HTML ainda não existem** ✘ (a pasta `landing/` só tem o `copy.json`).

---

### 1. Kit Mês Pronto (1º a lançar)

**1. Entregáveis**
- ✔ PDF de 52 páginas: `CentralLindsonALmeida/produtos/kit-mes-pronto/entrega/Kit-Mes-Pronto.pdf`
- ✔ Calendário em planilha: `CentralLindsonALmeida/produtos/kit-mes-pronto/entrega/calendario-30-dias.xlsx` e `.csv`
- ✔ Motor para gerar de novo: `CentralLindsonALmeida/produtos/kit-mes-pronto/fonte/` (`kit.py`, `gerar-pdf.js`)
- ✔ Oferta e copy: `agencia/ofertas/low-ticket/produtos/kit-mes-pronto/OFERTA.md`, `README.md`, `TEMPLATE.md`
- ✔ Capa da área de membros: `agencia/marca-lindson/artes-v2/artes/membros/h-kit-mes-pronto.jpg`
- ✘ Aprovação do PDF pelo Lindson (`README.md`, "Situação")
- ✘ Decisão sobre o visual v3 (`produtos/VISUAL-V3.md`, aguardando o Lindson; se aprovar, o PDF é refeito no v3 antes de vender)
- ✘ Vídeo curto de boas-vindas "como usar em 1 hora por semana" (opcional, 1 a 3 min, o Lindson grava)
- ✘ Mockup da capa do kit para a página e o anúncio

**2. Oferta**
- **Promessa:** "O seu mês inteiro de Instagram pronto para gravar: você só troca os colchetes e aperta o REC." (`OFERTA.md`)
- **Bônus que já existe:** o calendário também em planilha (Excel e CSV), com colunas de gravado, postado e quantas pessoas chamaram no WhatsApp ✔
- **Garantia:** 7 dias: "se não for pra você, devolvo seu dinheiro." (já no `copy.json`). Sugestão do `hormozi.md`: a pessoa fica com o bônus mesmo se pedir o reembolso.
- **Preço:** faixa sugerida **R$ 67 a 97** (kit, `hormozi.md` §Kits) · **decisão do Lindson:** ☐ R$ ____

**3. Página de venda**
- Texto: `copy.json`, bloco `kit-mes-pronto` ✔ (título "Seu mês inteiro de Instagram *pronto* pra gravar.", botão "Quero meu mês pronto")
- **Estilo próprio sugerido:** o mesmo do PDF, o **HUGE · Social Media Manager's Kit** (ArtisanaAura, `TEMPLATE.md`): páginas que alternam off-white e preto, "PRONTO" gigante em Anton até a borda com a 1ª letra em serifa itálica amarela, faixa de rótulos "30 ROTEIROS · 50 GANCHOS · 30 DIAS · 10 LEGENDAS", rodapé técnico em mono e o bloco "Como funciona" desenhado como a página dupla do calendário. Assim a página e o produto parecem a mesma coisa.
- ✘ Página em HTML · ✘ mockup do PDF aberto (3 páginas reais em leque)

**4. Checkout na Hubla**
- **Campos:** nome, e-mail, WhatsApp com DDD (obrigatório: a entrega também vai pelo WhatsApp), CPF se a Hubla pedir para Pix. Pagamento: Pix e cartão.
- **Order bump:** **Bio que Vende em 15 Minutos** ("o vídeo traz a pessoa para o perfil; a bio faz ela chamar"). É mais barato que o kit, como manda a regra do bump. Enquanto o PDF da Bio não existir, o checkout sai **sem bump**.
- **Upsell pós-compra (1 clique, página de obrigado):** **Kit WhatsApp que Fecha** ("o vídeo vai trazer gente perguntando o preço: chegue com a resposta pronta").
- **Cupom:** nenhum cupom aberto no lançamento (Hormozi Pricing: não dar desconto). Se o Lindson quiser, um único cupom para quem já comprou outro produto, com prazo real, valor decidido por ele.

**5. Entrega (área de membros)**
- **Módulo 0 · Comece aqui:** aula 1 "Como usar em 1 hora por semana" (vídeo curto ✘ ou o texto da página 2 do PDF ✔).
- **Módulo 1 · Baixe o seu kit:** aula "PDF do Kit Mês Pronto" (anexo `Kit-Mes-Pronto.pdf`) · aula "Calendário em planilha" (anexos `.xlsx` e `.csv`, com a dica de abrir no Google Planilhas pelo celular).
- **Módulo 2 · Semana a semana** (opcional, para a pessoa voltar à área): 4 aulas "Semana 1" a "Semana 4", cada uma com o texto "grave estes 7 roteiros: páginas X a Y do PDF". Ajuda a medir quem está usando.
- **Como o arquivo entra:** na Hubla, cada aula aceita material para baixar; subir o PDF e a planilha como anexo da aula (não como link externo), para só quem comprou baixar.
- **E-mail de boas-vindas (texto pronto):**
  > **Assunto:** Seu Kit Mês Pronto chegou
  > Oi, [NOME]! Aqui é o Lindson.
  > Seu kit já está liberado. Entre na área de membros por aqui: [LINK DA ÁREA]
  > Lá você baixa o PDF com os 30 roteiros, os 50 ganchos, o calendário de 30 dias e as 10 legendas, e o calendário em planilha.
  > Comece assim: no domingo, abra o calendário, escolha os 7 roteiros da semana e troque o que está em amarelo pelo seu serviço e o seu bairro. Depois grave tudo de uma vez.
  > Qualquer dúvida, é só responder este e-mail ou me chamar no WhatsApp.
  > Lindson Almeida
- **WhatsApp de boas-vindas:** é o D0 da sequência abaixo.

**6. Tráfego e conteúdo**
- **Isca do produto:** comentar **MÊS** para receber o link (`OFERTA.md`) ✔ · post de chamada "Não sabe o que postar amanhã?" ✔ (texto) / ✘ (arte).
- **Posts que já existem e servem de porta** (`agencia/marca-lindson/CALENDARIO.md` e `artes-v2/LEGENDAS.md`): 11/11 r2 "Um mês de vídeos. Um dia." · 15/11 r4 "Mito: precisa postar todo dia" · 27/11 m5 "3 roteiros de vídeo do seu nicho, de graça" (isca **ROTEIRO**, código `VD`). Hoje essas chamadas levam para a agência. Sugestão: quem pede os 3 roteiros grátis e não fecha a agência recebe o Kit Mês Pronto como próximo passo, na conversa.
- **Anúncio sugerido (Pedro Sobral):** Reels do Lindson falando para a câmera com o gancho "Você sabe que precisa postar. Só não sabe o que postar amanhã." → 3 telas do PDF passando → "o mês inteiro pronto, é só trocar pelo seu serviço" → botão para a página. Objetivo de vendas, evento Compra. Teste de 3 criativos por 3 dias (`agencia/processos/modelo-estrategia/README.md`, pág. 14).
- **Público:** segmentação aberta para dono de negócio local (quem filtra é o gancho, `ESTRATEGIA.md` §7); remarketing para quem viu metade dos Reels ou visitou a página e não comprou. Verba: decisão do Lindson.

**7. Pós-venda (WhatsApp)**
- **D0 (entrega):** "Oi, [NOME]! Aqui é o Lindson. Seu Kit Mês Pronto já está liberado: [LINK DA ÁREA]. Comece pelo calendário: no domingo escolha os 7 roteiros da semana e troque o que está em amarelo. Qual é o seu negócio?"
- **D1 (uso):** "Oi, [NOME]! Lindson aqui. O mais difícil é gravar o primeiro vídeo, depois a semana anda. Quer que eu te diga qual dos 30 roteiros eu gravaria primeiro no seu negócio?"
- **D3 (próximo problema → Kit WhatsApp que Fecha):** "Oi, [NOME]! Aqui é o Lindson. Quando o vídeo funciona, o cliente chama e pergunta o preço… e muita gente perde a venda ali. Juntei as mensagens que levam a conversa até o fechado. Quer que eu te mostre?"
- **D7 (→ Bio que Vende, ou Raio-X se a Bio ainda não existir):** "Oi, [NOME]! Lindson aqui. A pessoa vê o seu vídeo, entra no perfil e, se não entende o que você faz, vai embora. Tenho um guia para arrumar a bio em 15 minutos. Posso te mandar?"

**8. Métricas (só medir, sem meta)**
Visitas da página · checkout iniciado · compras · bump aceito (quando existir) · upsell do Kit WhatsApp aceito · reembolsos (e o motivo) · respostas ao D1 · quem comprou o próximo produto pelo D3 ou D7. Decisão: página com muita visita e pouco checkout → trocar o topo da página; muito checkout e pouca compra → revisar preço e meios de pagamento.

---

### 2. Kit WhatsApp que Fecha (2º a lançar)

**1. Entregáveis**
- ✔ PDF de 24 páginas 4:5: `CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/entrega/Kit-WhatsApp-que-Fecha.pdf`
- ✔ 43 atalhos: `CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/entrega/atalhos.txt` e `atalhos.csv`
- ✔ Motor: `CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/fonte/` (`gerar.py`, `gerar-pdf.js`)
- ◐ Amostra v3 (3 páginas): `CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/fonte/v3-amostra.html` (aguardando o Lindson)
- ✔ Oferta: `agencia/ofertas/low-ticket/produtos/kit-whatsapp-que-fecha/OFERTA.md`, `README.md`, `TEMPLATE.md`
- ✔ Capa da área: `agencia/marca-lindson/artes-v2/artes/membros/h-kit-whatsapp-que-fecha.jpg`
- ✘ Aprovação do PDF · ✘ vídeo de 2 a 3 min "como cadastrar os atalhos no WhatsApp Business" (gravação de tela) · ✘ mockup da capa em pé (o template pede)

**2. Oferta**
- **Promessa:** "Pare de perder cliente no 'quanto custa?': as mensagens prontas do primeiro oi até a venda." (`OFERTA.md`)
- **Bônus que já existe:** as 6 etiquetas do WhatsApp Business (Novo contato, Preço enviado, Vou pensar, Agendado, Fechou, Não fechou) ✔ (no PDF)
- **Garantia:** 7 dias (já no `copy.json`)
- **Preço:** faixa sugerida **R$ 47 a 67** (`hormozi.md` §Kits) · **decisão do Lindson:** ☐ R$ ____

**3. Página de venda**
- Texto: `copy.json`, bloco `kit-whatsapp-que-fecha` ✔ (botão "Quero fechar no WhatsApp")
- **Estilo próprio sugerido:** o do PDF, **Freelancer Client-Winning AI Prompt Kit** (Fused4Design, `TEMPLATE.md`): fundo preto com brilho amarelo no canto, pílula mono acima do título, "FECHA" com 1 palavra em serifa itálica, a capa do kit em pé com luz, e no lugar do "como funciona" um **celular com a conversa de WhatsApp** indo do "oi" ao "fechado" (atalhos /oi, /perguntas, /valor). Bloco de oferta no cartão preto com o preço em amarelo.
- ✘ Página em HTML

**4. Checkout na Hubla**
- **Campos:** nome, e-mail, WhatsApp com DDD, CPF se pedido. Pix e cartão.
- **Order bump:** **Bio que Vende** ("o cliente olha o seu perfil antes de responder; a bio passa confiança"). Até a Bio existir, sem bump.
- **Upsell pós-compra:** **Kit Mês Pronto** ("agora que você sabe fechar, falta trazer gente: o mês de conteúdo pronto"). Se a pessoa já veio do Kit Mês Pronto, a Hubla não deve oferecer de novo (conferir a regra de upsell para quem já tem o produto).
- **Cupom:** igual ao Kit Mês Pronto (nenhum aberto).

**5. Entrega (área de membros)**
- **Módulo 0 · Comece aqui:** aula "Cadastre os atalhos em 10 minutos" (vídeo de tela ✘, ou as páginas do PDF que explicam ✔).
- **Módulo 1 · Baixe o seu kit:** aula "PDF do Kit WhatsApp que Fecha" (anexo PDF) · aula "Atalhos prontos" (anexos `atalhos.txt` e `atalhos.csv`).
- **Módulo 2 · Os 6 passos** (opcional): 1 aula por passo, com o texto da mensagem para copiar direto do celular (sem abrir o PDF). O conteúdo já está em `fonte/conteudo.py`.
- **E-mail de boas-vindas:**
  > **Assunto:** Suas mensagens prontas chegaram
  > Oi, [NOME]! Aqui é o Lindson.
  > Seu Kit WhatsApp que Fecha já está liberado: [LINK DA ÁREA]
  > Lá estão o PDF com os 6 passos, as 20 respostas para "quanto custa?", as mensagens para quem sumiu e os 43 atalhos para colar no WhatsApp Business.
  > Comece pelos atalhos: cadastre uma vez e, na próxima vez que alguém perguntar o preço, digite /valor.
  > Qualquer dúvida, responda este e-mail ou me chame no WhatsApp.
  > Lindson Almeida

**6. Tráfego e conteúdo**
- **Isca do produto:** comentar **FECHA** (`OFERTA.md`) ✔ · post "O cliente pergunta o preço e some?" ✔ texto / ✘ arte.
- **Posts que já existem e servem de porta:** 16/11 s2_r5 Reels "Responder só o preço faz o cliente sumir" · 24/11 m2 carrossel "O que responder quando perguntam o preço" (`artes-v2/LEGENDAS.md`). Hoje terminam em **PERFIL**; para vender o kit, a chamada vira **FECHA** nesses dois.
- **Anúncio sugerido:** gravação de tela de uma conversa de WhatsApp (negócio fictício) morrendo depois do preço × a mesma conversa com os 6 passos. Gancho: "O cliente pergunta o preço e some? Não é o preço. É a resposta." Objetivo de vendas, evento Compra.
- **Público:** dono de negócio que vende pelo WhatsApp (serviço, loja, clínica, beleza, comida), segmentação aberta; remarketing para compradores do Kit Mês Pronto é desnecessário (eles recebem o D3).

**7. Pós-venda**
- **D0:** "Oi, [NOME]! Aqui é o Lindson. Seu Kit WhatsApp que Fecha já está liberado: [LINK DA ÁREA]. Comece cadastrando os atalhos: leva uns minutos e, na próxima pergunta de preço, é só digitar /valor. Qual é o seu negócio?"
- **D1:** "Oi, [NOME]! Lindson aqui. Já cadastrou os atalhos? Se travar em algum, me manda print que eu te ajudo a colocar."
- **D3 (→ Kit Mês Pronto):** "Oi, [NOME]! Aqui é o Lindson. Mensagem pronta só funciona se tem gente chamando, e muita gente para de postar porque não sabe o que gravar. Montei o mês inteiro de roteiros, é só trocar pelo seu serviço. Quer ver?"
- **D7 (→ Raio-X do Perfil):** "Oi, [NOME]! Lindson aqui. Antes de chamar no WhatsApp, o cliente olha o seu perfil, e às vezes desiste ali. Eu gravo um vídeo olhando o seu e te mostro o que arrumar em 7 dias. Quer saber como funciona?"

**8. Métricas**
Visitas · checkout iniciado · compras · bump aceito · upsell do Kit Mês Pronto aceito · reembolsos (motivo) · quantos responderam o D1 dizendo que cadastraram os atalhos · compras vindas do D3/D7.

---

### 3. Raio-X do Perfil em Vídeo (3º a lançar · é serviço)

**1. Entregáveis**
- ✔ Modelo do Plano de 7 Dias (PDF de 3 páginas): `CentralLindsonALmeida/produtos/raio-x-do-perfil/plano/plano.html`, `gerar.js`, modelo em branco `plano/dados/modelo.js`
- ✔ Exemplo pronto: `CentralLindsonALmeida/produtos/raio-x-do-perfil/plano/saida/exemplo/plano-7-dias.pdf` (+ `pagina-1.png` a `pagina-3.png`, servem de prévia na página de venda)
- ✔ Template: `agencia/ofertas/low-ticket/produtos/raio-x-do-perfil/TEMPLATE.md`
- ✔ Capa da área: `agencia/marca-lindson/artes-v2/artes/membros/h-raio-x-do-perfil.jpg`
- ✘ `README.md` e `OFERTA.md` do produto (os outros dois kits têm, este não)
- ✘ **Formulário de entrada** (o @, o que vende, onde atende, o que quer que o Instagram traga): campos extras no checkout da Hubla, se ela permitir, ou formulário curto logo depois da compra
- ✘ **Roteiro do vídeo de 5 minutos** (os 11 pontos na ordem, o que falar em cada um, como gravar a tela do perfil) para o Lindson gravar sempre igual
- ✘ Os 4 textos prontos (chamada do fixado, mensagem automática do WhatsApp, fim de legenda, resposta ao preço) como modelo em branco no `modelo.js` (hoje a página 3 do plano tem a bio antes × depois; conferir se os 4 textos já cabem nela)
- ✘ Controle de vagas da semana (quantas o Lindson aceita: decisão dele)
- ✘ **Decisão do Lindson:** a avaliação gratuita do perfil (isca **PERFIL**, `ESTRATEGIA.md` §4) e o Raio-X pago olham a mesma coisa. Sugestão: a gratuita continua curta (3 problemas + 1 solução, em texto, porta para a agência) e o Raio-X é a versão completa (vídeo + 11 pontos + plano de 7 dias), oferecida a quem recebeu a gratuita e não fechou a agência.

**2. Oferta**
- **Promessa:** "Eu olho o seu perfil e mostro onde você perde cliente." (`copy.json`)
- **Bônus que já existe:** "O valor volta se você seguir comigo": quem fechar qualquer pacote da agência em até 7 dias tem o valor abatido do primeiro mês ✔ (no `copy.json` e na caixa do próximo passo do plano)
- **Garantia:** 7 dias (já no `copy.json`). Atenção: por ser serviço feito, combinar com o Lindson se a garantia vale antes ou depois da entrega do vídeo (o texto atual diz só "se não for pra você, devolvo").
- **Escassez real:** "faço um por um, por isso as vagas da semana são limitadas" (já no FAQ). Só falar em vaga se o número for real.
- **Preço:** faixa sugerida **R$ 47 a 97** (`hormozi.md` 1.4) · **decisão do Lindson:** ☐ R$ ____

**3. Página de venda**
- Texto: `copy.json`, bloco `raio-x-do-perfil` ✔ (pílula "SERVIÇO · ENTREGA EM ATÉ 72 H", botão "Quero meu Raio-X")
- **Estilo próprio sugerido:** o do Plano de 7 Dias, **Forward Together** (NIVORA, `TEMPLATE.md`): cara de revista, "RAIO-X" condensado gigante, o círculo amarelo com a nota do perfil, a **linha do tempo vertical Dia 1 → Dia 7** no "como funciona" e a grade dos 11 pontos com os selos OK / AJUSTAR / URGENTE. As 3 páginas do exemplo (`saida/exemplo/pagina-*.png`) entram como prévia real. É a única página com a foto do Lindson em destaque, porque o serviço é ele.

**4. Checkout na Hubla**
- **Campos:** nome, e-mail, WhatsApp com DDD, CPF se pedido, e, se a Hubla aceitar campos extras: @ do Instagram, o que vende, onde atende, o que quer que o Instagram traga. Pix e cartão.
- **Order bump:** **Kit WhatsApp que Fecha** ("o Raio-X arruma o perfil; o kit fecha quem chamar"), só se o preço do kit ficar abaixo do Raio-X. Se não ficar, sem bump. A Bio que Vende **não** entra aqui: o Raio-X já entrega a bio antes × depois.
- **Upsell pós-compra:** nenhum de 1 clique (a pessoa ainda vai receber o vídeo). O upsell é a **agência**, no vídeo e no plano, com o abatimento em 7 dias. Dentro da área, o Kit Mês Pronto fica em "Outros produtos".
- **Cupom:** nenhum. O abatimento na agência já faz o papel.

**5. Entrega**
- **Na área de membros (igual para todos):** Módulo 0 · "Como funciona o seu Raio-X" (texto: prazo de até 72 h, o que vai receber) · aula "Responda o formulário" (link do formulário ✘, se não estiver no checkout) · aula "Exemplo de Plano de 7 Dias" (anexo `plano-7-dias.pdf` do exemplo, para a pessoa ver o que vem).
- **O vídeo e o plano de cada pessoa NÃO entram na área** (é individual): vão pelo WhatsApp, o vídeo como link não listado (YouTube não listado ou Drive) e o PDF gerado com `node gerar.js <cliente>`.
- **Rotina do Lindson por pedido:** receber o formulário → gravar a tela do perfil seguindo o roteiro ✘ → preencher `dados/<cliente>.js` a partir do `modelo.js` → gerar o PDF → mandar vídeo + PDF no WhatsApp em até 72 h.
- **E-mail de boas-vindas:**
  > **Assunto:** Recebi o seu pedido do Raio-X
  > Oi, [NOME]! Aqui é o Lindson.
  > Seu Raio-X do Perfil está confirmado. Para eu começar, preciso de 3 respostas rápidas: [LINK DO FORMULÁRIO]
  > Assim que você responder, eu gravo o vídeo olhando o seu perfil e te mando, junto com o Plano de 7 Dias, no seu WhatsApp em até 72 horas.
  > Se quiser ver como fica o plano, o exemplo está na área de membros: [LINK DA ÁREA]
  > Lindson Almeida

**6. Tráfego e conteúdo**
- **Isca do produto:** ✘ sugerida: comentar **RAIOX** (não usar **PERFIL**, que já é a avaliação gratuita).
- **Posts que já existem e servem de porta:** 13/11 p1 "Avaliação gratuita do seu perfil" · 17/11 s2_c3 "5 coisas que todo perfil que vende tem" · 21/11 s2_c4 "Antes × depois: a bio da Dra. Jaci" (só com autorização dela) · 28/11 m6 "Perfil sem destaques e com destaques". Também `conteudo/avaliacao-gratuita/` (PLANO, LEGENDAS, conteúdos), que é a mesma lógica.
- **Anúncio sugerido:** o Lindson gravando a tela de um perfil fictício, apontando 3 dos 11 pontos ("a bio não diz o que você vende", "o link não vai para o WhatsApp"), fechando com "eu faço isso com o seu, em vídeo, e te mando o plano de 7 dias". Objetivo de vendas.
- **Público:** dono de negócio local, com foco em São Luís (o abatimento só vale para quem pode virar cliente da agência); remarketing para quem pediu a avaliação gratuita e não fechou.

**7. Pós-venda**
- **D0 (pedido):** "Oi, [NOME]! Aqui é o Lindson. Seu Raio-X está confirmado. Pra eu começar, me responde 3 perguntas rápidas: [LINK]. Assim que chegar, gravo o vídeo do seu perfil e te mando em até 72 horas. Combinado?"
- **Dia da entrega (D1 a D3):** "Oi, [NOME]! Lindson aqui. Seu Raio-X está pronto: o vídeo [LINK] e o Plano de 7 Dias no PDF abaixo. Comece pelos itens em URGENTE. Quer que eu te explique algum ponto?"
- **D3 depois da entrega (uso):** "Oi, [NOME]! Aqui é o Lindson. Muita gente trava no dia 1 do plano porque não sabe como escrever a bio nova. Já trocou a sua? Se quiser, me manda que eu dou uma olhada."
- **D7 depois da entrega (→ agência, com o abatimento):** "Oi, [NOME]! Lindson aqui. Arrumar o perfil é o primeiro passo, mas sem vídeo novo todo mês ele para de novo. Se fechar comigo até [DATA], o valor do Raio-X sai do primeiro mês. Quer que eu te mostre como seria?"

**8. Métricas**
Visitas · checkout iniciado · compras · formulários respondidos · Raio-X entregues dentro de 72 h · reembolsos · quantos fecharam a agência em até 7 dias (o abatimento usado) · tempo do Lindson por Raio-X (para ele decidir o número de vagas e o preço).

---

### 4. Bio que Vende em 15 Minutos (4º a lançar · bump dos outros)

**1. Entregáveis**
- ✔ Template escolhido e referências: `agencia/ofertas/low-ticket/produtos/bio-que-vende/TEMPLATE.md` e `referencias/`
- ✔ Texto da página: `copy.json`, bloco `bio-que-vende`
- ✔ Capa da área: `agencia/marca-lindson/artes-v2/artes/membros/h-bio-que-vende.jpg`
- ✘ **O PDF do guia** (fórmula em 5 partes, caminho do cliente, Teste dos 5 Segundos, destaques e fixados, antes e depois, caixas "Lembre" e "Faça agora"), no template COURAGE (NIVORA). Não existe pasta `CentralLindsonALmeida/produtos/bio-que-vende/`.
- ✘ Exemplos de antes × depois com **negócios fictícios** (nunca bio de cliente, `hormozi.md` regra 2)
- ✘ **Pack de capas de destaque** (o bump: capas só tipográficas em preto, amarelo e branco, template Almeria Haus em `TEMPLATE.md`), em PNG e com a versão editável
- ✘ `README.md` e `OFERTA.md` do produto

**2. Oferta**
- **Promessa:** "Sua bio está espantando cliente. Arrume em 15 minutos." (`copy.json`)
- **Bônus que já existe:** nenhum (`"bonus": null` no `copy.json`). Sugestão sem custo: o Teste dos 5 Segundos como checklist de 1 página para imprimir (já está previsto dentro do guia; pode virar a página destacada como bônus).
- **Garantia:** 7 dias (já no `copy.json`)
- **Preço:** faixa sugerida **R$ 17 a 27** (`hormozi.md` 1.1) · **decisão do Lindson:** ☐ R$ ____
- **Atenção à taxa:** produto barato perde mais em taxa fixa. Conta com as taxas informadas (8,9% + R$ 2,49): em R$ 17 a taxa é cerca de R$ 4,00 por venda; em R$ 27, cerca de R$ 4,89. Confirmar na Hubla antes de decidir.

**3. Página de venda**
- Texto: `copy.json` ✔ (botão "Quero minha bio nova"). O FAQ já cita o Pack de capas como bump.
- **Estilo próprio sugerido:** o do guia, **COURAGE** (NIVORA, `TEMPLATE.md`): topo em página amarela inteira com manchete preta condensada em 4 linhas ("SUA BIO ESTÁ ESPANTANDO CLIENTE."), bloco escuro com a fórmula em 5 partes com marcadores amarelos redondos e a seta perfil → bio → link → WhatsApp, e o **antes × depois** com o celular do perfil dentro do círculo amarelo. É a página mais curta das cinco: produto de impulso.
- ✘ Página em HTML

**4. Checkout na Hubla**
- **Campos:** nome, e-mail, WhatsApp com DDD, CPF se pedido. Pix e cartão.
- **Order bump:** **Pack de capas de destaque** ✘ (precisa existir antes; preço abaixo do da Bio, decisão do Lindson).
- **Upsell pós-compra:** **Raio-X do Perfil** ("você arrumou a bio; eu olho o resto do perfil em vídeo"), como manda o `hormozi.md` (1.4 para quem comprou 1.1). Se o Raio-X estiver sem vaga na semana, oferecer o **Kit Mês Pronto**.
- **Cupom:** nenhum.
- **Também é bump** nos checkouts do Kit Mês Pronto e do Kit WhatsApp que Fecha (e pode ser do Kit Prospecção, ver abaixo). Na Hubla, criar o produto uma vez e ligá-lo como bump nos outros.

**5. Entrega**
- **Módulo 0 · Comece aqui:** aula "Os 15 minutos, um por um" (texto curto com a ordem).
- **Módulo 1 · Baixe o guia:** aula com o PDF (anexo).
- **Módulo 2 · Capas de destaque** (só libera para quem levou o bump: na Hubla, o bump é um produto separado com a própria aula).
- **E-mail de boas-vindas:**
  > **Assunto:** Sua bio nova começa agora
  > Oi, [NOME]! Aqui é o Lindson.
  > Seu guia Bio que Vende já está liberado: [LINK DA ÁREA]
  > Separe 15 minutos, abra o seu perfil no celular e siga o guia minuto a minuto. No fim, faça o Teste dos 5 Segundos para conferir.
  > Me manda a bio nova quando terminar, eu gosto de ver.
  > Lindson Almeida

**6. Tráfego e conteúdo**
- **Isca do produto:** ✘ sugerida: comentar **BIO**.
- **Posts que já existem e servem de porta:** 10/11 c1 carrossel "Arrume sua bio em 3 passos" · 08/11 a2 "Do perfil ao WhatsApp" · 05/12 "Sua bio é uma lista de links. Ou é a sua vitrine." (`CALENDARIO.md`).
- **Anúncio sugerido:** carrossel ou Reels de tela "antes × depois" de uma bio fictícia, gancho "A pessoa entra no seu perfil e não entende o que você faz?". Como é barato, serve como **produto de entrada** que paga o anúncio e alimenta a lista para os outros 4.
- **Público:** dono de negócio local, segmentação aberta.

**7. Pós-venda**
- **D0:** "Oi, [NOME]! Aqui é o Lindson. Seu guia Bio que Vende já está liberado: [LINK DA ÁREA]. Separa 15 minutos, abre o seu perfil e segue o guia. Quando terminar, me manda a bio nova?"
- **D1:** "Oi, [NOME]! Lindson aqui. Já trocou a bio? Se ficou na dúvida em alguma das 5 partes, me manda a sua que eu te digo o que ajustar."
- **D3 (→ Kit Mês Pronto):** "Oi, [NOME]! Aqui é o Lindson. Bio arrumada, mas se o perfil fica sem post novo, quem entra acha que você sumiu. Montei o mês inteiro de roteiros, é só trocar pelo seu serviço. Quer ver?"
- **D7 (→ Raio-X do Perfil):** "Oi, [NOME]! Lindson aqui. A bio é uma parte do perfil. Tem mais 10 que fazem o cliente chamar ou ir embora. Eu gravo um vídeo olhando o seu e te mando o plano de 7 dias. Quer saber como funciona?"

**8. Métricas**
Visitas · checkout iniciado · compras · bump das capas aceito · upsell do Raio-X aceito · reembolsos · quantas vezes a Bio foi aceita como **bump** nos outros checkouts (mostra se ela vende melhor sozinha ou junto) · quem mandou a bio nova no D0/D1.

---

### 5. Kit Prospecção pelo WhatsApp (5º a lançar · público B)

**1. Entregáveis**
- ✔ As 100 mensagens em texto: `CentralLindsonALmeida/produtos/kit-prospeccao/100-Mensagens-Kit-Prospeccao.txt`
- ✔ Planilha com abas Como usar, Cadência, Painel, Config, Mensagens, Nichos, Objeções: `CentralLindsonALmeida/produtos/kit-prospeccao/Planilha-Cadencia-Kit-Prospeccao.xlsx`
- ✔ Dados e motor: `CentralLindsonALmeida/produtos/kit-prospeccao/fonte/` (`dados.json` com toques, nichos, ordem, objeções; `dados.py`, `planilha.py`)
- ✔ Template: `agencia/ofertas/low-ticket/produtos/kit-prospeccao/TEMPLATE.md` (Pocus)
- ✔ Capa da área: `agencia/marca-lindson/artes-v2/artes/membros/h-kit-prospeccao.jpg`
- ✘ **O PDF** (capa "WHATSAPP" gigante + "100 MENSAGENS" vazado, método, cadência de 4 toques, filtro, cuidados com LGPD e limites do WhatsApp, objeções), no template Pocus
- ✘ Conferir se as **buscas prontas no Google** por nicho, prometidas na página, estão na planilha (a página lista 6 entregáveis; a planilha não tem aba "Buscas")
- ✘ Pasta `entrega/` (os arquivos estão soltos na raiz do produto, diferente dos outros dois kits), `README.md` e `OFERTA.md`
- ✘ Vídeo de tela "como usar a planilha no celular" (opcional)

**2. Oferta**
- **Promessa:** "100 mensagens prontas pra chamar negócio local no WhatsApp." (`copy.json`)
- **Bônus que já existe:** 10 respostas para as objeções ("quanto custa?", "já tenho alguém", "vou pensar", "já paguei agência" e mais 6) ✔ (aba Objeções e `dados.json`)
- **Garantia:** 7 dias (já no `copy.json`)
- **Preço:** faixa sugerida **R$ 27 a 47** (`hormozi.md` 5.3) · **decisão do Lindson:** ☐ R$ ____
- **Cuidado:** este kit ensina a vender o mesmo serviço que o Lindson vende. A regra do `hormozi.md` é que nada de cliente vira produto; as mensagens usam [SEU NOME] e [CIDADE], sem dado de cliente ✔.

**3. Página de venda**
- Texto: `copy.json`, bloco `kit-prospeccao` ✔ (botão "Quero as 100 mensagens")
- **Estilo próprio sugerido:** o do PDF, **The Product-Led Sales Playbook** (Pocus, `TEMPLATE.md`): topo de cor cheia (preto) com "CLIENTE" gigante e "100 MENSAGENS" vazado sangrando na base, uma faixa de **números do método** (100 mensagens, 10 nichos, 4 toques, 280 caracteres: só números do produto, nenhum resultado), a **linha de pontos que crescem** Dia 1 → Dia 2 → Dia 3 → Dia 5 no "como funciona" e os cartões lado a lado "entra na fila / não entra". É a única página que fala com social media e agência, não com dono de negócio.
- ✘ Página em HTML

**4. Checkout na Hubla**
- **Campos:** nome, e-mail, WhatsApp com DDD, CPF se pedido. Pix e cartão.
- **Order bump:** **Bio que Vende** ("antes de chamar o dono, arrume o seu perfil: ele vai olhar antes de responder"). Até a Bio existir, sem bump.
- **Upsell pós-compra:** **Kit WhatsApp que Fecha** ("abordou, agora precisa fechar", `hormozi.md` 5.3 → 5.1).
- **Cupom:** nenhum.

**5. Entrega**
- **Módulo 0 · Comece aqui:** aula "Sua primeira manhã de prospecção" (texto: configurar a aba Config com o seu nome e a sua cidade, escolher o nicho, mandar a primeira mensagem).
- **Módulo 1 · Baixe o seu kit:** aula com o PDF ✘ · aula "Planilha de cadência" (anexo `.xlsx`, com a dica de abrir no Google Planilhas) · aula "As 100 mensagens em texto" (anexo `.txt`).
- **Módulo 2 · Os 10 nichos** (opcional): 1 aula por nicho com as 10 mensagens para copiar do celular.
- **E-mail de boas-vindas:**
  > **Assunto:** Suas 100 mensagens chegaram
  > Oi, [NOME]! Aqui é o Lindson.
  > Seu Kit Prospecção já está liberado: [LINK DA ÁREA]
  > Comece pela planilha: na aba Config, coloque o seu nome e a sua cidade. Depois escolha um nicho, anote os negócios e toque em "Abrir WhatsApp". A mensagem já vem escrita.
  > Uma mensagem por vez, só para quem tem WhatsApp e Instagram. Quem pedir para parar sai da fila.
  > Lindson Almeida

**6. Tráfego e conteúdo**
- **Isca do produto:** ✘ sugerida: comentar **CLIENTE**.
- **Posts que já existem:** nenhum para este público ✘. O feed do Lindson fala com dono de negócio. Precisa de uma linha de conteúdo para social media (ex.: bastidor da rotina de prospecção dele, `agencia/prospeccao/ROTINA.md`).
- **Anúncio sugerido:** gravação de tela da planilha: toca em "Abrir WhatsApp", a conversa abre com a mensagem escrita, toca em enviar. Gancho: "Você trava na primeira mensagem pro cliente?". Objetivo de vendas.
- **Público:** social media, freelancer de foto, vídeo, tráfego ou site, agência pequena; interesses de marketing digital e social media. É outro público, outro criativo e outra conta de resultado: medir separado dos outros 4.

**7. Pós-venda**
- **D0:** "Oi, [NOME]! Aqui é o Lindson. Seu Kit Prospecção já está liberado: [LINK DA ÁREA]. Comece pela aba Config da planilha, coloque seu nome e sua cidade. Qual nicho você vai chamar primeiro?"
- **D1:** "Oi, [NOME]! Lindson aqui. A primeira mensagem é a que mais trava. Já mandou a sua? Se quiser, me fala o nicho que eu te digo qual das 10 eu mandaria primeiro."
- **D3 (→ Kit WhatsApp que Fecha):** "Oi, [NOME]! Aqui é o Lindson. Quando o dono responde e pergunta o preço, muita conversa morre ali. Juntei as mensagens que levam do 'quanto custa?' até o fechado. Quer que eu te mostre?"
- **D7 (→ Bio que Vende, se não levou no bump):** "Oi, [NOME]! Lindson aqui. Antes de responder, o dono abre o seu perfil, e se não entende o que você faz, não responde. Tenho um guia pra arrumar a bio em 15 minutos. Posso te mandar?"

**8. Métricas**
Visitas · checkout iniciado · compras · bump aceito · upsell do Kit WhatsApp aceito · reembolsos (e o motivo: aqui o risco é "achei que era disparo em massa") · compras vindas do D3/D7. Medir o custo por compra deste público **separado** dos outros.

---

## C. Parte comum: a comunidade única na Hubla

### C.1 Como a comunidade fica montada
- **Uma comunidade só** com os 5 produtos. Quem compra um vê só aquele liberado; os outros aparecem com cadeado e o botão **Comprar**, que leva ao checkout de cada um. É o que o Lindson pediu em 04/11 (`agencia/sistema-clientes/membros/README.md`).
- **Na Hubla, cada produto é um produto separado** (com o próprio checkout, bump e upsell), todos dentro da mesma área de membros, e a vitrine **"Outros produtos"** mostra os que a pessoa ainda não tem. Conferir no painel da Hubla se o recurso se chama assim e se fica dentro da mesma área (se a Hubla só permitir uma área por produto, usar a vitrine para ligar as cinco).
- **Produtos extras que também viram produto na Hubla:** o **Pack de capas de destaque** (bump da Bio) ✘. Ele só aparece para quem levou o bump, não na vitrine.
- **Ordem na vitrine** (a do funil, não a do ranking): 1. Kit Mês Pronto · 2. Kit WhatsApp que Fecha · 3. Bio que Vende · 4. Raio-X do Perfil · 5. Kit Prospecção. Os liberados sempre primeiro ("Continuar"); depois os bloqueados nessa ordem. Por quê: o Mês Pronto é a porta, o WhatsApp é o próximo problema, a Bio é o mais barato (compra fácil dentro da área), o Raio-X leva à agência e a Prospecção é de outro público (fica por último para não confundir o dono de negócio).
- **Visual:** o protótipo aprovado é o **NEXUS** (Adam Max, dribbble.com/shots/27716502) na marca preto e amarelo: `agencia/sistema-clientes/membros/prototipo.html` (abrir com `?tem=kit-mes-pronto,kit-whatsapp-que-fecha`). Capas horizontais prontas em `agencia/marca-lindson/artes-v2/artes/membros/` (`h-*.jpg` e `hero.jpg`), geradas por `artes-v2/gerar-membros.js` a partir de `membros.html`. As fotos do Lindson ficam fora do Git (`artes-v1/fotos/`), nenhuma repetida.
- **Dois caminhos (decisão do Lindson):** (1) usar a área de membros da própria Hubla com essas capas, **recomendado para lançar** (menos coisa para dar errado); (2) a área própria dentro da Central (`lindsonalmeida.pages.dev`) com o checkout da Hubla e o webhook liberando o produto. O caminho 2 fica para depois, quando houver vendas.

### C.2 Passo a passo do Lindson na Hubla
Os nomes exatos dos menus podem mudar: siga o que aparecer no painel e confira as taxas na página oficial antes de começar.

1. **Decidir os preços** dos 5 produtos e do Pack de capas (faixas na seção B). Sem isso nada sobe.
2. **Aprovar** os PDFs do Kit Mês Pronto e do Kit WhatsApp que Fecha e decidir sobre o visual v3 (`produtos/VISUAL-V3.md`).
3. **Criar a conta na Hubla** com o CPF ou CNPJ dele e cadastrar a conta bancária ou chave Pix para receber.
4. **Criar o primeiro produto (Kit Mês Pronto):** tipo produto digital / área de membros, nome, descrição curta (subtítulo do `copy.json`), preço, imagem de capa (`h-kit-mes-pronto.jpg`), garantia de 7 dias.
5. **Montar a área de membros desse produto:** criar os módulos e aulas da ficha (seção B, item 5), subir o PDF e a planilha como **material da aula**, pôr a capa horizontal e, se a Hubla pedir, a vertical.
6. **Configurar o checkout:** campos (nome, e-mail, WhatsApp obrigatório, CPF se pedido), Pix e cartão, a cor amarela da marca (#F5C518) e o logo.
7. **Configurar a mensagem e o e-mail de entrega:** colar o e-mail de boas-vindas da ficha. Se a Hubla mandar WhatsApp automático, colar o D0; se não, o Lindson manda o D0 à mão (ou pela automação que a equipe montar).
8. **Repetir os passos 4 a 7** para o Kit WhatsApp que Fecha. Depois ligar o **upsell** de um no outro (página de obrigado / oferta de 1 clique) e, quando a Bio existir, o **order bump**.
9. **Ativar a vitrine "Outros produtos"** e pôr a ordem da seção C.1.
10. **Pixel da Meta:** no Gerenciador de Eventos da Meta, criar ou pegar o pixel da conta de anúncios dele e colar o ID na integração da Hubla. Conferir se a Hubla manda os eventos de visita, início de checkout e compra. Fazer uma compra de teste e ver o evento chegar.
11. **Domínio (opcional):** se ele quiser endereço próprio para a área de membros ou para o checkout, criar o subdomínio (ex.: `membros.` + o domínio dele, se tiver) e apontar no DNS como a Hubla mandar. Sem domínio, funciona com o endereço da Hubla.
12. **Compra de teste** em cada produto (Pix de valor real ou o modo de teste, se existir): conferir e-mail, liberação só do produto comprado, cadeado e botão Comprar nos outros, bump e upsell. Depois pedir o reembolso para testar a garantia.
13. **Mandar para a equipe** os 5 links de checkout e o link da área: a equipe troca o `{{CHECKOUT}}` e o `{{PRECO}}` nas páginas e publica.
14. **Raio-X, quando for lançar:** dizer quantas vagas por semana aceita e como prefere receber o formulário (campos no checkout ou formulário depois).
15. **Pedir depoimentos** aos primeiros compradores (com autorização por escrito) antes de pôr qualquer prova na página.

### C.3 O que a equipe (Claude) entrega pronto
| Entrega | Situação | Onde |
|---|---|---|
| PDF + planilha do Kit Mês Pronto | ✔ pronto | `CentralLindsonALmeida/produtos/kit-mes-pronto/entrega/` |
| PDF + atalhos do Kit WhatsApp que Fecha | ✔ pronto | `CentralLindsonALmeida/produtos/kit-whatsapp-que-fecha/entrega/` |
| Mensagens + planilha do Kit Prospecção | ✔ pronto · PDF ✘ | `CentralLindsonALmeida/produtos/kit-prospeccao/` |
| Modelo do Plano de 7 Dias do Raio-X | ✔ pronto · formulário e roteiro do vídeo ✘ | `CentralLindsonALmeida/produtos/raio-x-do-perfil/plano/` |
| PDF da Bio que Vende + Pack de capas | ✘ a fazer (template escolhido) | `agencia/ofertas/low-ticket/produtos/bio-que-vende/TEMPLATE.md` |
| Texto das 5 páginas de venda | ✔ pronto | `CentralLindsonALmeida/produtos/landing/copy.json` |
| As 5 páginas em HTML, cada uma no estilo do seu PDF | ✘ a fazer | (destino: repositório próprio que o Lindson criar; até lá, `CentralLindsonALmeida/produtos/landing/`) |
| Capas da área de membros | ✔ prontas | `agencia/marca-lindson/artes-v2/artes/membros/` |
| Protótipo da área estilo NEXUS | ✔ pronto | `agencia/sistema-clientes/membros/prototipo.html` |
| E-mails e WhatsApp de boas-vindas, D0 a D7 | ✔ neste arquivo | seção B, itens 5 e 7 |
| Mockups dos produtos (capa em pé, PDF aberto) | ✘ a fazer | — |
| Artes dos posts de chamada (MÊS, FECHA, BIO, RAIOX, CLIENTE) e criativos de anúncio | ✘ a fazer (textos de MÊS e FECHA prontos nos `OFERTA.md`) | — |
| Painel de métricas dos produtos na Central | ✘ a fazer (no padrão de `agencia/sistema-clientes/prototipo/painel.html`) | — |
| Automação do D0 a D7 no WhatsApp | ✘ a decidir (Hubla, ou botão `wa.me` no padrão dos apps de SDR do `CLAUDE.md`) | — |

**O que só o Lindson faz:** preços, aprovações, conta e configuração da Hubla, pixel, domínio, gravar os vídeos (boas-vindas e cada Raio-X), pedir depoimentos e decidir a verba de anúncio.

### C.4 Medição comum aos 5
- **Funil por produto:** visitas da página → checkout iniciado → compras → bump aceito → upsell aceito → reembolsos. A Hubla mostra vendas e reembolsos; visitas e checkout iniciado vêm do pixel e da própria página.
- **Entre produtos:** quem comprou mais de um, e por qual porta (D3, D7, vitrine "Outros produtos", upsell).
- **Origem:** cada isca (MÊS, FECHA, BIO, RAIOX, CLIENTE) com o próprio código no link, como já é feito com AV, AD, VD e MS (`ESTRATEGIA.md` §4), para saber qual post vendeu.
- **Sem meta inventada.** A média de cada número sai das primeiras vendas. Regra de decisão, igual à da estratégia: cortar o criativo cujo custo por compra passar da média da conta depois de gastar o dobro dela; escalar aos poucos o que estiver abaixo.

---

## D. O que falta, em ordem de prioridade

1. **Preço de cada produto e aprovação dos PDFs** (Kit Mês Pronto, Kit WhatsApp que Fecha) e do visual v3 (Lindson).
2. **Conta da Hubla com os produtos, checkout, área de membros e pixel** (Lindson, seção C.2).
3. **As 5 páginas de venda em HTML**: só existe o texto (`copy.json`), com `{{PRECO}}` e `{{CHECKOUT}}` em aberto (equipe).
4. **PDF da Bio que Vende e o Pack de capas de destaque**: hoje só há o template, e a Bio é o bump de três checkouts (equipe).
5. **PDF do Kit Prospecção**, com a conferência das "buscas prontas no Google" que a página promete (equipe).
6. **Raio-X:** formulário de entrada, roteiro do vídeo de 5 minutos, `OFERTA.md`/`README.md` e a decisão sobre a avaliação gratuita × Raio-X pago (equipe + Lindson).
7. Mockups, artes dos posts de chamada e criativos de anúncio; isca e conteúdo para o público do Kit Prospecção (equipe).
8. Depoimentos autorizados dos primeiros compradores (Lindson).
