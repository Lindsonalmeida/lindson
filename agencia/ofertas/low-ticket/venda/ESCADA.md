# Escada de venda: upsells, downsells e a chamada para a agência

Hormozi Squad (Hormozi Models: atrair → vender mais → reter · Hormozi Offers: cada oferta resolve o próximo problema · Hormozi Pricing: nunca desconto) + Russell Brunson (escada de valor, bump, upsell, downsell). Data: 04/11/2026. **Rascunho para o Lindson aprovar.**

Pedido do Lindson (04/11/2026): *"em todo produto, gere upsells e downsells, nunca perca uma oportunidade de vender ou de as pessoas me contratarem."*

Base: `ESTRUTURA.md` (fichas, bump e upsell já definidos, pós-venda D0 a D7), `../hormozi.md` (escada, regras, downsells), `../../esteira-de-produtos.md` (planos da agência), `../produtos/*/OFERTA.md` e `README.md`, `agencia/prospeccao/PADRAO-COPY.md`.

**Regras deste arquivo**
- **Só produtos que existem:** os 5 (Kit Mês Pronto, Kit WhatsApp que Fecha, Raio-X do Perfil, Bio que Vende, Kit Prospecção), o **Pack de capas de destaque** (bump da Bio, pronto, `produtos/bio-que-vende/README.md`) e os **planos da agência** (`esteira-de-produtos.md`: Vídeo, Tráfego, Alcance, Presença, Instagram que Vende, mini site avulso). O curso do `produto-master.md` ainda não existe, por isso não entra.
- **Preço: decisão do Lindson.** Onde aparece "mais barato que", é a regra do bump/downsell (o item oferecido tem que custar menos que o recusado). Se o preço que ele escolher quebrar a regra, a linha cai e vale a alternativa escrita ao lado.
- **Nunca desconto, nunca cupom aberto, nunca "só hoje".** O downsell troca por um **produto menor**, por **parcelamento** (se a Hubla oferecer no cartão) ou por **ajuda real** (tirar a dúvida, reenviar o Pix). Nenhum bônus novo é inventado.
- **Nada de número de resultado, nada de escassez falsa.** Vaga limitada só no Raio-X, e só se o número for real.
- **Reembolso é direito (7 dias, CDC art. 49).** A troca é oferecida uma vez, com o reembolso garantido do mesmo jeito. Se a pessoa não responder em 24 h, ou disser "quero o dinheiro", o reembolso é feito sem mais perguntas.
- **Nunca oferecer o que a pessoa já tem.** Antes de cada upsell, downsell ou mensagem, conferir na Hubla o que ela já comprou e pular para a próxima opção da lista.
- **Mensagens** no padrão Conexão → Dor → Desejo → Pergunta, até 280 caracteres, sem "vi que", "parece que", "gargalo" nem jargão. Link só depois do sim (exceto entrega e recuperação de pagamento, em que a pessoa já disse sim ao comprar).
- **"Valor abate no 1º mês"** = o que a pessoa pagou no produto sai do primeiro mês da agência se ela fechar em até 7 dias. **Já existe e está aprovado só no Raio-X** (`copy.json`). Nos outros produtos está marcado **SUGESTÃO · só se o Lindson aprovar**.

---

## 1. A escada geral

Do mais barato ao mais caro. A posição de 2 a 5 segue a faixa sugerida no `ESTRUTURA.md`; a ordem final depende do preço que o Lindson escolher.

| Degrau | O quê | Papel na escada | Próximo passo natural |
|---|---|---|---|
| 0 · Grátis | Avaliação gratuita do perfil (isca **PERFIL**) e 3 roteiros grátis (isca **ROTEIRO**) | Atrair, porta da agência | Agência; quem não fecha → Raio-X ou Kit Mês Pronto |
| 1 · Bump | **Pack de capas de destaque** | Só como bump/downsell, nunca na vitrine | Bio que Vende |
| 2 · Entrada | **Bio que Vende em 15 Minutos** | Produto de impulso, paga o anúncio, bump dos outros | Raio-X → Kit Mês Pronto |
| 3 · Entrada (público B) | **Kit Prospecção pelo WhatsApp** | Para social media e freelancer | Kit WhatsApp que Fecha |
| 4 · Kit | **Kit WhatsApp que Fecha** | Dor nº 2: "pergunta o preço e some" | Kit Mês Pronto → plano Tráfego |
| 5 · Kit | **Kit Mês Pronto** | Dor nº 1: "não sei o que postar" | Kit WhatsApp → plano Vídeo |
| 6 · Serviço | **Raio-X do Perfil em Vídeo** | Ponte para a agência (abatimento aprovado) | plano Presença |
| 7 · Agência (porta) | **Vídeo** ou **Tráfego** (mensais, sem fidelidade) · **mini site avulso** (pagamento único) | "Eu faço por você" | Subir de degrau (`esteira-de-produtos.md`, "Como subir o cliente de degrau") |
| 8 · Agência (topo) | **Alcance → Presença → Instagram que Vende** (mínimo 3 meses) | Reter | Vídeo extra e subir de degrau |

**A regra: todo ponto de contato tem um próximo passo.** Ou a pessoa compra o degrau seguinte, ou contrata o Lindson. Nenhuma página, e-mail, PDF, mensagem ou resposta a reembolso termina sem uma dessas duas portas (às vezes as duas: "faça você mesmo com o próximo kit, ou deixe que eu faço").

| Ponto de contato | Próximo passo obrigatório |
|---|---|
| Post e isca (MÊS, FECHA, BIO, RAIOX, CLIENTE/CHAMAR) | Página do produto |
| Página de venda | Checkout + no rodapé "prefere que eu faça por você? me chama no WhatsApp" |
| Checkout | Order bump |
| Checkout abandonado | Mensagem de 1 h e de 24 h (produto menor ou parcelamento, nunca desconto) |
| Página de obrigado | Upsell de 1 clique → se "não", downsell → se "não" de novo, o card da agência |
| E-mail de boas-vindas | P.S. com o próximo produto ou a agência |
| WhatsApp D0 a D7 | D3 = próximo produto · D7 = produto seguinte ou agência · **D14 (novo, sugestão)** = agência |
| Área de membros | Vitrine "Outros produtos" (cadeado + Comprar) + card "Quer que o Lindson faça por você?" |
| Última página do PDF | "Seu próximo passo": produto seguinte + "quer que eu faça por você?" |
| Pedido de reembolso | Oferta de troca uma vez, reembolso garantido |
| Avaliação gratuita sem fechar | Raio-X (perfil) ou Kit Mês Pronto (conteúdo), como já sugerido no `ESTRUTURA.md` |
| Cliente da agência | Subir de degrau (esteira) |

**Fluxo da página de obrigado (igual nos 5):**
```
Compra ──► Página de obrigado: UPSELL de 1 clique
              ├─ "Sim, quero" ──► entrega dos dois
              └─ "Não, obrigado" ──► DOWNSELL (produto menor)
                                       ├─ "Sim" ──► entrega
                                       └─ "Não" ──► página final: acesso à área + card da agência
```
Se a Hubla não tiver downsell automático, o link "Não, obrigado" aponta para uma página nossa (na pasta das landings) com o botão do checkout do downsell. Conferir no painel.

---

## 2. Produto por produto

### 2.1 Kit Mês Pronto

| Etapa | Oferta | Por quê (o próximo problema) |
|---|---|---|
| **Order bump** | Bio que Vende (já definido) | "O vídeo traz a pessoa ao perfil; a bio faz ela chamar." |
| **Upsell 1 clique** | Kit WhatsApp que Fecha (já definido) | O vídeo funciona, o cliente chama e pergunta o preço. |
| **Downsell (recusou o upsell)** | Bio que Vende, se não levou no bump · se já levou: Pack de capas de destaque · se já tem os dois: sem downsell, vai para o card da agência | Produto menor que termina o perfil. |
| **Checkout abandonado** | 1 h: ajuda no pagamento (Pix expirou, cartão travou, parcelamento no cartão se a Hubla tiver). 24 h: começar menor com a Bio que Vende, ou o mesmo kit parcelado. | Sem desconto: troca o tamanho do passo, não o preço. |
| **Pedido de reembolso** | Troca pelo Kit WhatsApp que Fecha (se o problema for "já tenho conteúdo, o que falta é fechar") ou pelo plano **Vídeo** ("não tenho tempo de gravar": eu gravo por você). Reembolso garantido. | A dor nº 1 de quem não usa o kit costuma ser tempo, e o plano Vídeo resolve exatamente isso. |
| **Chamada para a agência** | Plano **Vídeo** (4 vídeos/mês gravados em 1 dia, `esteira`). Momentos: contracapa do PDF (já tem o convite para gravar com o Lindson ✔), card da área, D7 (se já tem o Kit WhatsApp) ou **D14**. | "Você tem os roteiros; eu gravo e edito." **SUGESTÃO · só se o Lindson aprovar:** o valor do kit abate no 1º mês do Vídeo se fechar em até 7 dias. |

### 2.2 Kit WhatsApp que Fecha

| Etapa | Oferta | Por quê |
|---|---|---|
| **Order bump** | Bio que Vende (já definido) | O cliente olha o perfil antes de responder. |
| **Upsell 1 clique** | Kit Mês Pronto (já definido) · se já tem: Raio-X do Perfil | Mensagem pronta só funciona se tem gente chamando. |
| **Downsell** | Bio que Vende, se não levou no bump · se já levou: Pack de capas · se tem os dois: card da agência | Produto menor. |
| **Checkout abandonado** | 1 h: ajuda no pagamento. 24 h: Bio que Vende como passo menor, ou o kit parcelado. | Sem desconto. |
| **Pedido de reembolso** | Troca pelo Kit Mês Pronto (se o problema for "quase ninguém me chama") ou pela Bio que Vende. Reembolso garantido. | Quem não tem conversa para fechar precisa de conteúdo, não de script. |
| **Chamada para a agência** | Plano **Tráfego** (gestão do anúncio, `esteira`). Momentos: última página do PDF, card da área, **D14**. | "Agora você sabe fechar. Quer mais gente chamando? Eu cuido do anúncio." **SUGESTÃO · só se o Lindson aprovar:** valor do kit abate no 1º mês. |

### 2.3 Raio-X do Perfil em Vídeo (serviço)

| Etapa | Oferta | Por quê |
|---|---|---|
| **Order bump** | Kit WhatsApp que Fecha **só se custar menos que o Raio-X** (já definido) · se não: **Pack de capas de destaque** (SUGESTÃO nova: destaque é um dos 11 pontos, e o pack resolve na hora). Bio que Vende não entra (o Raio-X já reescreve a bio). | O Raio-X diz o que arrumar; o bump já entrega uma parte pronta. |
| **Upsell 1 clique** | **Kit Mês Pronto** (SUGESTÃO nova: o `ESTRUTURA.md` dizia "nenhum"; a ordem de 04/11 pede não perder a chance) | O plano arruma os 7 primeiros dias; do dia 8 em diante a pessoa precisa de conteúdo. |
| **Downsell** | Kit WhatsApp que Fecha (se não levou no bump e custar menos que o Kit Mês Pronto) · se não: Pack de capas · se já tem: card da agência | Produto menor. |
| **Checkout abandonado** | 1 h: ajuda no pagamento + lembrar que o Lindson faz um por um (só se as vagas forem reais). 24 h: Bio que Vende ("começar sozinho em 15 minutos"). | Sem desconto e sem escassez inventada. |
| **Pedido de reembolso** | **Antes do vídeo:** reembolso imediato ou troca pelo Kit Mês Pronto ou Kit WhatsApp. **Depois do vídeo:** reembolso dentro dos 7 dias; a regra de garantia antes/depois da entrega é **decisão do Lindson** (`README.md` do Raio-X). | Serviço já feito tem custo de hora, mas o direito continua. |
| **Chamada para a agência** | Plano **Presença** (perfil + tráfego + vídeos) ou o degrau que o vídeo indicar. **Abatimento aprovado ✔:** o valor do Raio-X sai do 1º mês se fechar em até 7 dias. Momentos: fim do vídeo, última página do plano (caixa do próximo passo ✔), D7 depois da entrega ✔ e card da área. | "Entram no perfil e vão embora → Presença" (`ESTRATEGIA.md`). |

### 2.4 Bio que Vende em 15 Minutos

| Etapa | Oferta | Por quê |
|---|---|---|
| **Order bump** | Pack de capas de destaque ✔ (pronto) | A bio arrumada, os destaques ainda bagunçados. |
| **Upsell 1 clique** | Raio-X do Perfil (já definido) · sem vaga na semana: Kit Mês Pronto | "Você arrumou a bio; eu olho o resto do perfil." |
| **Downsell** | Pack de capas, se não levou no bump · se já levou: Kit WhatsApp que Fecha **só se custar menos que o Raio-X** · se não: card da agência | Produto menor. |
| **Checkout abandonado** | É o produto mais barato: não há passo menor (o Pack só existe junto). 1 h: ajuda no pagamento. 24 h: tirar a dúvida + lembrar a garantia de 7 dias. | Aqui o que trava é atrito, não preço. |
| **Pedido de reembolso** | Troca pelo Kit Mês Pronto ou Kit WhatsApp, pagando só a diferença (se o problema não é a bio, é o conteúdo ou a conversa). Reembolso garantido. | Mecânica da troca na Hubla (reembolso + compra nova) a conferir. |
| **Chamada para a agência** | **Mini site avulso** (link da bio que leva ao WhatsApp) e plano **Presença**. Momentos: última página do PDF, card da área, D7 (se recusou o Raio-X) ou **D14**. | "Quer que eu faça o seu perfil por você?" **SUGESTÃO · só se o Lindson aprovar:** valor da Bio abate no mini site ou no 1º mês. |

### 2.5 Kit Prospecção pelo WhatsApp (público B: social media, freelancer, agência pequena)

| Etapa | Oferta | Por quê |
|---|---|---|
| **Order bump** | Bio que Vende (já definido) | O dono abre o perfil do freelancer antes de responder. |
| **Upsell 1 clique** | Kit WhatsApp que Fecha (já definido) | Abordou, agora precisa fechar. |
| **Downsell** | Bio que Vende, se não levou no bump · se já levou: Pack de capas · se tem os dois: Kit Mês Pronto fica na vitrine (não é downsell, costuma custar mais) | Produto menor. |
| **Checkout abandonado** | 1 h: ajuda no pagamento. 24 h: Bio que Vende como passo menor ("arrume o seu perfil antes de chamar"). | Sem desconto. |
| **Pedido de reembolso** | Atenção ao motivo comum "achei que era disparo em massa" (`ESTRUTURA.md`): explicar uma vez, oferecer troca pelo Kit WhatsApp que Fecha, reembolso garantido. | Ninguém fica preso a um produto que não queria. |
| **Chamada para a agência** | Público B não é o cliente da agência. O próximo passo dele é **produto**: Kit WhatsApp → **Kit Mês Pronto** (os roteiros servem para os clientes dele). Card da agência só para quem também tem negócio próprio ("tem um negócio e quer que eu faça por você?"). | Não empurrar a agência para quem vende o mesmo serviço. Parceria ou terceirização para social media **não existe** hoje: não oferecer. |

### 2.6 Pack de capas de destaque (só bump e downsell)
Não tem upsell próprio: quem leva o Pack já está no funil da Bio. Próximo passo: o `LEIA-ME` do zip termina com o texto da seção 3.6 (Raio-X + agência).

---

## 3. Textos prontos

Colchetes `[NOME]`, `[LINK]`, `[NÚMERO DO LINDSON]`, `[DATA]` são trocados pela Hubla ou pela equipe. Nenhum texto leva preço (o preço só aparece no botão/checkout).

### 3.1 Páginas de upsell (página de obrigado)

**Kit Mês Pronto → upsell Kit WhatsApp que Fecha**
- **Título:** Espera: o seu vídeo vai trazer gente perguntando o preço.
- 1. É ali que muita venda morre: a pessoa pergunta "quanto custa?" e some.
- 2. O Kit WhatsApp que Fecha tem as mensagens prontas do primeiro oi até o fechado, e 43 atalhos para colar no WhatsApp Business.
- 3. Entra junto com o seu kit, sem preencher nada de novo.
- **Botão sim:** Sim, quero fechar mais no WhatsApp
- **Link não:** Não, obrigado. Vou responder do meu jeito.

**Kit WhatsApp que Fecha → upsell Kit Mês Pronto**
- **Título:** Espera: mensagem pronta só funciona se tem gente chamando.
- 1. Quem para de postar para de receber conversa.
- 2. O Kit Mês Pronto traz 30 roteiros, 50 ganchos e o calendário de 30 dias: é só trocar pelo seu serviço e gravar.
- 3. Uma hora por semana e o mês está pronto.
- **Botão sim:** Sim, quero o meu mês pronto
- **Link não:** Não, obrigado. Eu já sei o que postar.

**Raio-X do Perfil → upsell Kit Mês Pronto**
- **Título:** Seu plano arruma os 7 primeiros dias. E o dia 8?
- 1. Perfil arrumado e sem post novo volta a parecer parado.
- 2. O Kit Mês Pronto tem o mês inteiro de roteiros, ganchos e legendas, é só trocar pelo seu serviço.
- 3. Chega hoje; o seu Raio-X chega em até 72 horas.
- **Botão sim:** Sim, quero o meu mês pronto
- **Link não:** Não, obrigado. Só o Raio-X por agora.

**Bio que Vende → upsell Raio-X do Perfil**
- **Título:** A bio é uma parte. O cliente olha o perfil inteiro.
- 1. Foto, destaques, fixados, link: cada um faz a pessoa chamar ou ir embora.
- 2. Eu gravo um vídeo de até 5 minutos olhando o seu perfil e te mando o Plano de 7 Dias.
- 3. Se você fechar com a agência em até 7 dias, o valor do Raio-X sai do primeiro mês.
- **Botão sim:** Sim, quero o meu Raio-X
- **Link não:** Não, obrigado. Vou arrumar sozinho.

**Kit Prospecção → upsell Kit WhatsApp que Fecha**
- **Título:** Espera: o dono vai responder. E aí?
- 1. A conversa mais difícil é a do "quanto custa?".
- 2. O Kit WhatsApp que Fecha tem o script de 6 passos, as 20 respostas para o preço e as mensagens para quem sumiu.
- 3. Você aborda com um kit e fecha com o outro.
- **Botão sim:** Sim, quero fechar as conversas
- **Link não:** Não, obrigado. Só a prospecção por agora.

### 3.2 Páginas de downsell (depois do "não, obrigado")

**Downsell Bio que Vende** (Kit Mês Pronto, Kit WhatsApp, Kit Prospecção)
- **Título:** Tudo bem. Então só uma coisa antes de você ir.
- A pessoa que chega pelo seu vídeo ou pela sua mensagem entra no seu perfil. Se a bio não diz o que você faz, ela vai embora.
- O guia Bio que Vende arruma isso em 15 minutos, com o celular na mão.
- **Botão sim:** Sim, quero a minha bio nova
- **Link não:** Não, obrigado. Ir para o meu acesso.

**Downsell Pack de capas de destaque** (para quem já tem a Bio)
- **Título:** Última coisa: os seus destaques.
- 36 capas prontas em preto, amarelo e branco, com a versão para trocar a palavra.
- O perfil fica arrumado de cima a baixo hoje mesmo.
- **Botão sim:** Sim, quero as capas
- **Link não:** Não, obrigado. Ir para o meu acesso.

**Downsell Kit WhatsApp que Fecha** (Raio-X, Bio, quando custar menos que o recusado)
- **Título:** Tudo bem. Então leve a parte que fecha.
- Perfil arrumado traz conversa. As mensagens prontas levam a conversa até o fechado.
- **Botão sim:** Sim, quero as mensagens
- **Link não:** Não, obrigado. Ir para o meu acesso.

**Página final (depois do último "não")**
- **Título:** Pronto, seu acesso está liberado.
- **Botão:** Entrar na área de membros
- **Abaixo:** o card da seção 3.7.

### 3.3 WhatsApp de checkout abandonado

Regra: a pessoa já disse sim ao clicar em comprar, por isso o link vai na mensagem de 1 h. Uma mensagem de 1 h e uma de 24 h, e para. Quem pedir para parar sai da lista.

**Kit Mês Pronto**
> **1 h:** Oi, [NOME]! Aqui é o Lindson. Seu Kit Mês Pronto ficou parado no pagamento. Às vezes o Pix expira ou o cartão trava. Se quiser terminar, o link é este: [LINK]. Deu algum problema que eu possa ajudar?

> **24 h:** Oi, [NOME]! Lindson de novo. Se o mês inteiro pareceu muita coisa agora, dá pra começar menor: um guia que arruma a sua bio em 15 minutos. Ou levar o kit parcelado no cartão. Quer que eu te mande um dos dois?

**Kit WhatsApp que Fecha**
> **1 h:** Oi, [NOME]! Aqui é o Lindson. Suas mensagens prontas ficaram paradas no pagamento. Às vezes o Pix expira ou o cartão trava. Se quiser terminar, é por aqui: [LINK]. Precisa de ajuda com alguma coisa?

> **24 h:** Oi, [NOME]! Lindson de novo. O cliente continua perguntando o preço e sumindo? Se preferir começar menor, tenho um guia para arrumar a bio em 15 minutos. Ou o kit parcelado no cartão. Quer um dos dois?

**Raio-X do Perfil**
> **1 h:** Oi, [NOME]! Aqui é o Lindson. Seu Raio-X ficou parado no pagamento. Às vezes o Pix expira ou o cartão trava. Se quiser terminar, é por aqui: [LINK]. Assim que pagar, eu já começo a olhar o seu perfil. Posso ajudar?

> **24 h:** Oi, [NOME]! Lindson de novo. Se preferir arrumar sozinho primeiro, tenho um guia que deixa a sua bio pronta em 15 minutos. E o Raio-X continua aqui quando quiser. Quer que eu te mande o guia?

**Bio que Vende**
> **1 h:** Oi, [NOME]! Aqui é o Lindson. Seu guia da bio ficou parado no pagamento. Às vezes o Pix expira ou o cartão trava. Se quiser terminar, é por aqui: [LINK]. São 15 minutos e o seu perfil fica outro. Posso ajudar?

> **24 h:** Oi, [NOME]! Lindson de novo. Ficou alguma dúvida sobre o guia? Se não for pra você, você tem 7 dias pra pedir o dinheiro de volta. Quer que eu te explique o que tem dentro?

**Kit Prospecção**
> **1 h:** Oi, [NOME]! Aqui é o Lindson. Suas 100 mensagens ficaram paradas no pagamento. Às vezes o Pix expira ou o cartão trava. Se quiser terminar, é por aqui: [LINK]. Precisa de ajuda com alguma coisa?

> **24 h:** Oi, [NOME]! Lindson de novo. Antes de chamar cliente, o dono vai olhar o seu perfil. Se quiser começar por aí, tenho um guia que arruma a bio em 15 minutos. Ou o kit parcelado. Quer um dos dois?

### 3.4 Mensagem para pedido de reembolso

Regra: responder no mesmo dia, dizer primeiro que o reembolso está garantido, oferecer a troca **uma vez**. Sem resposta em 24 h, ou "quero o dinheiro" → reembolsar na Hubla na hora.

**Modelo (troque o [PRODUTO] e a [TROCA] pela linha "Pedido de reembolso" da seção 2):**
> Oi, [NOME]! Aqui é o Lindson. Recebi seu pedido e o reembolso está garantido. Só pergunto antes: o que faltou? Se for [MOTIVO], posso trocar pelo [TROCA] no lugar. Prefere a troca ou o dinheiro de volta?

Exemplos prontos:
> **Kit Mês Pronto:** Oi, [NOME]! Aqui é o Lindson. Seu reembolso está garantido. Só pergunto: o que travou foi tempo de gravar? Se for, eu posso gravar por você, e te explico como. Prefere isso ou o dinheiro de volta?

> **Kit WhatsApp que Fecha:** Oi, [NOME]! Aqui é o Lindson. Seu reembolso está garantido. Só pergunto: o problema é que quase ninguém te chama? Se for, posso trocar pelo Kit Mês Pronto, com o mês de conteúdo. Prefere a troca ou o dinheiro?

> **Raio-X (antes do vídeo):** Oi, [NOME]! Aqui é o Lindson. Seu reembolso está garantido. Se preferir algo pra fazer no seu tempo, posso trocar por um dos kits: o do mês de conteúdo ou o das mensagens do WhatsApp. Quer a troca ou o dinheiro de volta?

> **Bio que Vende:** Oi, [NOME]! Aqui é o Lindson. Seu reembolso está garantido. Só pergunto: o que falta pra você é o que postar ou o que responder no WhatsApp? Tenho um kit pra cada, você paga só a diferença. Prefere a troca ou o dinheiro?

> **Kit Prospecção:** Oi, [NOME]! Aqui é o Lindson. Seu reembolso está garantido. O kit é pra mandar uma mensagem por vez, não disparo. Se o que você precisa é fechar quem já responde, troco pelo Kit WhatsApp que Fecha. Prefere a troca ou o dinheiro?

Depois do reembolso feito (sem pedir nada):
> Oi, [NOME]! Lindson aqui. Reembolso feito, deve aparecer no seu extrato nos próximos dias. Obrigado por ter testado. Se um dia quiser que eu faça o seu Instagram por você, é só me chamar aqui. Posso te avisar quando tiver conteúdo novo?

### 3.5 D14: chamada para a agência (novo, sugestão)
Entra depois do D7 do `ESTRUTURA.md`, só para quem não respondeu ao D7 nem comprou o próximo produto.
> **Kit Mês Pronto:** Oi, [NOME]! Aqui é o Lindson. Roteiro pronto ajuda, mas tem semana que não dá tempo nem de gravar. Se quiser, eu gravo e edito os seus vídeos do mês num dia só. Quer que eu te mostre como seria?

> **Kit WhatsApp que Fecha:** Oi, [NOME]! Aqui é o Lindson. Agora que você sabe responder o preço, o que falta é mais gente chamando. Eu cuido do anúncio pra trazer cliente pro seu WhatsApp. Quer que eu te mostre como seria?

> **Bio que Vende:** Oi, [NOME]! Aqui é o Lindson. Bio arrumada é o começo, mas o perfil precisa de post novo e de alguém cuidando. Eu faço isso por você, todo mês. Quer que eu te mostre como seria pro seu negócio?

(Raio-X já tem o D7 com o abatimento; Kit Prospecção não recebe D14 de agência, só o Kit Mês Pronto: "os 30 roteiros servem pros seus clientes também. Quer ver?")

### 3.6 Última página de cada PDF: "Seu próximo passo"

Dois blocos lado a lado (ou um embaixo do outro no 4:5): à esquerda **"Faça você mesmo"** (produto seguinte, botão para o checkout), à direita **"Quer que eu faça por você?"** (agência, botão `wa.me/55[NÚMERO DO LINDSON]?text=` com a mensagem já escrita, no padrão dos apps do `CLAUDE.md`).

**Kit Mês Pronto** (complementa a contracapa atual, que já tem o convite para gravar)
- **Seu próximo passo:** o vídeo vai trazer gente perguntando o preço. O **Kit WhatsApp que Fecha** tem as respostas prontas, do oi ao fechado. → *Quero fechar mais no WhatsApp*
- **Quer que eu faça por você?** Você já tem os roteiros. Eu gravo os seus vídeos do mês num dia só e entrego editados. → *Chamar o Lindson* (mensagem pronta: "Oi, Lindson! Comprei o Kit Mês Pronto e quero saber como é você gravar os meus vídeos.")

**Kit WhatsApp que Fecha**
- **Seu próximo passo:** mensagem pronta só funciona se tem gente chamando. O **Kit Mês Pronto** traz o mês inteiro de roteiros para o seu negócio. → *Quero o meu mês pronto*
- **Quer que eu faça por você?** Eu cuido do anúncio para trazer mais gente para o seu WhatsApp, e você só fecha. → *Chamar o Lindson* ("Oi, Lindson! Comprei o Kit WhatsApp que Fecha e quero saber como é o anúncio com você.")

**Raio-X · Plano de 7 Dias** (a caixa do próximo passo já existe ✔; confirmar que diz isto)
- **Seu próximo passo:** do dia 8 em diante, o perfil precisa de post novo. O **Kit Mês Pronto** tem os 30 roteiros. → *Quero o meu mês pronto*
- **Quer que eu faça por você?** Se você fechar comigo até [DATA], o valor do Raio-X sai do primeiro mês. → *Chamar o Lindson* ("Oi, Lindson! Recebi o meu Raio-X e quero saber como seria você cuidar do meu perfil.")

**Bio que Vende**
- **Seu próximo passo:** a bio é uma parte. No **Raio-X do Perfil** eu olho o perfil inteiro em vídeo e te mando o Plano de 7 Dias. → *Quero o meu Raio-X*
- **Quer que eu faça por você?** Eu monto o seu mini site com botão de WhatsApp, ou cuido do seu perfil todo mês. → *Chamar o Lindson* ("Oi, Lindson! Comprei o Bio que Vende e quero saber como é você cuidar do meu perfil.")

**Kit Prospecção**
- **Seu próximo passo:** o dono respondeu e perguntou o preço? O **Kit WhatsApp que Fecha** leva a conversa até o fechado. E os 30 roteiros do **Kit Mês Pronto** servem para os seus clientes. → *Quero fechar as conversas*
- **Tem um negócio próprio e quer que eu faça por você?** → *Chamar o Lindson* ("Oi, Lindson! Comprei o Kit Prospecção e quero saber como você trabalha.")

**Pack de capas (fim do LEIA-ME)**
- Seu próximo passo: no **Raio-X do Perfil** eu olho o resto do seu perfil em vídeo. Quer que eu faça por você? Me chama no WhatsApp: [LINK wa.me].

### 3.7 Card da área de membros: "Quer que o Lindson faça por você?"

Fica fixo abaixo dos produtos liberados (acima da vitrine "Outros produtos"), no visual NEXUS do `agencia/sistema-clientes/membros/prototipo.html`, com a foto do Lindson (uma que ainda não foi usada, `FOTOS-USADAS`). O texto muda conforme o que a pessoa comprou; quem tem mais de um vê o do produto mais caro.

**Texto geral (padrão)**
- **Título:** Quer que o Lindson faça por você?
- **Texto:** Você já tem o material. Se faltar tempo, eu faço: gravo os vídeos, cuido do perfil e do anúncio, e o cliente chama no seu WhatsApp.
- **Botão:** Chamar o Lindson no WhatsApp (abre `wa.me` com "Oi, Lindson! Sou aluno da área de membros e quero saber como você pode fazer o meu Instagram.")

**Variações (só a linha do texto muda)**
- Kit Mês Pronto: "Você tem os roteiros. Eu gravo os seus vídeos do mês num dia só."
- Kit WhatsApp que Fecha: "Você já sabe fechar. Eu trago mais gente chamando com anúncio."
- Raio-X: "Você já sabe o que arrumar. Eu arrumo e cuido todo mês. Fechando até [DATA], o valor do Raio-X sai do primeiro mês."
- Bio que Vende: "Sua bio está pronta. Eu faço o mini site e cuido do resto do perfil."
- Kit Prospecção: "Tem um negócio próprio? Eu cuido do Instagram dele." (card menor, público B)
- **SUGESTÃO · só se o Lindson aprovar**, nos 4 primeiros: "+ o valor que você pagou aqui sai do primeiro mês, se fechar em até 7 dias."

### 3.8 P.S. do e-mail de boas-vindas
Acrescentar no fim de cada e-mail do `ESTRUTURA.md`:
> P.S.: Se preferir que eu faça por você, é só responder este e-mail com "QUERO". Eu te explico como funciona.

---

## 4. Onde aplicar

| Onde | O que entra | Quem faz | Situação |
|---|---|---|---|
| **Checkout Hubla** | Order bump de cada produto (seção 2), parcelamento no cartão ligado, campo WhatsApp obrigatório (para a recuperação) | **Lindson na Hubla** | ✘ (depende do preço) |
| **Recuperação de checkout (Hubla)** | Se a Hubla mandar mensagem de carrinho abandonado: colar os textos de 1 h e 24 h (3.3). Se não mandar: lista diária para a equipe com o botão `wa.me` | **Lindson** liga / **equipe** monta a lista | ✘ conferir recurso na Hubla |
| **Página de obrigado (Hubla)** | Upsell de 1 clique (3.1) → "não" leva ao downsell (3.2) → página final com o card (3.7) | **Lindson** configura na Hubla · **equipe** faz as páginas de downsell se a Hubla não tiver | ✘ |
| **Área de membros** | Vitrine "Outros produtos" (ordem do `ESTRUTURA.md` C.1) + card "Quer que o Lindson faça por você?" (3.7) | **Equipe** no protótipo e nas capas · **Lindson** ativa na Hubla | ◐ vitrine prevista, card ✘ |
| **Última página do PDF** | "Seu próximo passo" (3.6) | **Equipe** nos motores (`fonte/` de cada produto no privado) e regera os PDFs | ✘ (Kit Mês Pronto tem só o convite para gravar; Raio-X tem a caixa ✔) |
| **LEIA-ME do Pack de capas** | Próximo passo (3.6) | **Equipe** em `produtos/bio-que-vende/bump/` | ✘ |
| **Pós-venda WhatsApp** | D3 e D7 do `ESTRUTURA.md` ✔ + D14 (3.5) + mensagens de reembolso (3.4) | **Lindson** manda (ou a automação que a equipe montar, botão `wa.me`) | ◐ |
| **E-mail de boas-vindas** | P.S. (3.8) | **Lindson** cola na Hubla · **equipe** atualiza o `ESTRUTURA.md` | ✘ |
| **Landing page** | Rodapé "prefere que eu faça por você?" com botão `wa.me` + o upsell citado no FAQ ("depois da compra você pode levar junto…") | **Equipe** nas páginas (`CentralLindsonALmeida/produtos/landing/`, com a conta Pedro) | ✘ |
| **Reembolso** | Responder com 3.4, uma vez; reembolsar na Hubla | **Lindson** | ✘ |

**Decisões que ficam com o Lindson antes de ligar:**
1. Preço de cada produto e do Pack (define se cada bump/downsell cabe na regra "mais barato que").
2. Abatimento no 1º mês da agência para os 4 produtos além do Raio-X (sugestão) e o prazo (7 dias).
3. Upsell novo do Raio-X (Kit Mês Pronto) e bump alternativo do Raio-X (Pack de capas).
4. Garantia do Raio-X antes ou depois da entrega do vídeo.
5. Se o D14 entra na sequência.
6. Isca do Kit Prospecção: o `ESTRUTURA.md` diz **CLIENTE** e o `OFERTA.md` diz **CHAMAR**. Escolher uma.
