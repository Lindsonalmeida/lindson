# Barzakh · funil de vendas e operação comercial (conta Leandro, 16/11/2026)

Situação: **rascunho para aprovação do Lindson.** Parte do pedido "monte o funil de vendas, campanhas de tráfego pago, estratégias de conteúdo, gere todo o meu marketing e vendas". Este arquivo cobre só o **funil e a operação comercial**. Tráfego e conteúdo ficam em outros arquivos desta pasta, feitos por outras frentes.

**Base:**
- `../marca/ESTRATEGIA.md`: nome, tom, promessa, palavras proibidas.
- `../CANAIS.md`: pacotes Limiar, Travessia e Horizonte, bios, WhatsApp.
- `../../README.md`: a persona.
- `../../OFERTA.md`: etapas e briefing.
- `../../v2/oferta/`: proposta v2 e carrossel de anúncio.
- `agencia/prospeccao/PADRAO-COPY.md` e `agencia/prospeccao/ROTINA.md`.
- As regras de SDR do `CLAUDE.md`.

**Frameworks:**
- **Hormozi Offers:** equação de valor, bônus e garantia.
- **Donald Miller (StoryBrand):** o cliente é o herói e a Barzakh é o guia.
- **Pedro Sobral:** distribuição e métricas.

As listas de agentes estão em `AGENTES.md`.

**Regras que valem aqui:**
- Sem promessa de resultado e sem número inventado.
- Nenhum preço em peça pública ou no PDF. **Valores: definir com o Lindson**, e eles só aparecem na conversa.
- Pagamento sempre antecipado.
- A esteira de produtos do Lindson, de até R$ 3.500, não muda.
- Copy segue Conexão → Dor → Desejo → Pergunta, sem "vi que", "parece que" ou "gargalo".
- Na fila de contato só entra lead com WhatsApp (celular) **e** Instagram.
- WhatsApp do estúdio: wa.me/5598985621808.
- Página de venda: https://lindsonalmeida.pages.dev/site/identidade/

---

## 0. A história que o funil conta (StoryBrand em 7 linhas)

| Parte | Barzakh |
|---|---|
| **Herói** | O dono de negócio local que já atende bem e cresceu no boca a boca |
| **Problema externo** | A marca foi feita às pressas: logo improvisado e cada post de um jeito |
| **Problema interno** | Vergonha de mandar o perfil para um cliente maior e receio de cobrar mais |
| **Problema filosófico** | Negócio bom merece parecer o que é |
| **Guia** | Empatia: "isso é muito comum". Autoridade: cases reais aplicados, processo em 6 etapas, o designer no WhatsApp |
| **Plano** | 1. Conversa e briefing. 2. Conceito apresentado em mockup. 3. Marca entregue com guia para usar |
| **Chamada** | Direta: "Me chama no WhatsApp". De transição: o diagnóstico gratuito ou o checklist |
| **Fracasso evitado** | Refazer fachada, cartão e perfil daqui a um ano. Continuar parecendo menor que o negócio |
| **Sucesso** | Uma marca pronta para se apresentar, a mesma em tudo e sem pedir desculpa |

Toda peça e toda mensagem do funil saem desta tabela. A Barzakh nunca é a heroína da história: ela é o guia. Por isso a mensagem fala do negócio do cliente, e não do estúdio.

---

## 1. Mapa do funil

```text
TOPO (atenção)                         MEIO (conversa)                         FUNDO (decisão)
───────────────────────────            ───────────────────────────            ───────────────────────────
Instagram @barzakhstudio ──┐           Isca 1: diagnóstico de marca            Reunião de 20 min
Pinterest (pins SEO) ──────┤           gratuito em 3 telas                       ↓
Behance (cases) ───────────┤           Isca 2: checklist "Sua marca            Proposta em PDF (sem preço)
LinkedIn (página + Lindson)┼──► Página  está pronta para se apresentar?"       + valor dito na conversa
Anúncios Meta (mensagem) ──┤   de venda    ↓                                      ↓
Anúncios Google (busca) ───┤   ou direto  WhatsApp (scripts da seção 4)        Fechamento: contrato +
Indicação ─────────────────┤   no         ↓                                    pagamento antecipado
Prospecção ativa (SDR) ────┘   WhatsApp   Briefing (formulário)                   ↓
 Instagram + Google Maps                                                       Entrega (6 etapas)
                                                                                  ↓
PÓS-VENDA ──► depoimento ──► indicação (volta ao topo) ──► upsell (site, social, kit de posts, tráfego)
       └──► quem não fechou: downsell ou nutrição (conteúdo + reabordagem depois de 90 dias)
```

### 1.1 Etapas, com dono e saída

| # | Etapa | O que acontece | Quem faz | Sai quando | Etapa no app (seção 6) |
|---|---|---|---|---|---|
| 1 | **Entrada** | O lead chega por um dos canais com um **código de origem** na mensagem (tabela 1.2) | Tráfego e conteúdo (outras frentes); SDR (seção 3) | Manda a 1ª mensagem ou responde à abordagem | `novo` → `enviado` |
| 2 | **Isca** | Pede o diagnóstico de 3 telas ou o checklist | Claude prepara, o Lindson aprova e envia | Recebeu a isca | `respondeu` → `diagnostico` |
| 3 | **Página de venda** | Vê os cases, os pacotes (sem preço) e o processo em /site/identidade/ | — | Toca em "Orçamento no WhatsApp" | — |
| 4 | **WhatsApp** | Qualificação em 3 perguntas: o que vende, onde a marca aparece, para quando precisa | O Lindson toca em "enviar"; a mensagem já vem pronta | Aceitou a reunião ou o briefing | `respondeu` |
| 5 | **Briefing** | Preenche `site/identidade/briefing.html`, que envia pelo WhatsApp | O cliente | Formulário recebido | `briefing` |
| 6 | **Reunião** | 20 min por vídeo ou ligação (roteiro em 3.5) | O Lindson | Pediu a proposta | `reuniao` |
| 7 | **Proposta** | PDF na identidade Barzakh, **sem preço impresso**; valor e forma de pagamento vão na conversa logo depois | Claude monta e o Lindson envia | Disse sim, ou acabou o follow-up (3.6) | `proposta` |
| 8 | **Fechamento** | Contrato (`agencia/processos/modelo-contrato/`) + pagamento antecipado + data de início | O Lindson | Pagamento confirmado | `fechado` |
| 9 | **Entrega** | 6 etapas: briefing → persona e pesquisa → conceito em mockup → sistema → aplicações → entrega. Tudo sobe no painel do cliente na Central | Equipe Designer + Lindson | Arquivos e guia entregues | `entrega` |
| 10 | **Pós-venda** | Checagem, depoimento, indicação e upsell (2.5) | O Lindson, com mensagens prontas | Depoimento recebido ou upsell fechado | `posvenda` |

### 1.2 Códigos de origem (para saber de onde veio cada cliente)

Cada canal tem seu link wa.me com o texto já escrito e um código no fim. O código vai para a ficha do lead e é a base das métricas da seção 5.

| Canal | Código | Texto pronto do link (exemplo) |
|---|---|---|
| Instagram (bio, stories, Reels) | `IG` | "Oi! Quero saber da identidade visual (IG)" |
| Pinterest | `PIN` | "Oi! Vim pelo Pinterest e quero saber da identidade visual (PIN)" |
| Behance | `BEH` | "Oi! Vi o portfólio no Behance (BEH)" |
| LinkedIn | `LIN` | "Oi! Vim pelo LinkedIn (LIN)" |
| Anúncio Meta (mensagem) | `META` | Resposta automática do anúncio + "(META)" no campo de mensagem pronta |
| Anúncio Google | `GOOG` | "Oi! Vi o anúncio no Google, quero um orçamento (GOOG)" |
| Isca: diagnóstico | `DIAG` | "Oi! Quero o diagnóstico gratuito da minha marca (DIAG)" |
| Isca: checklist | `CHECK` | "Oi! Quero o checklist da marca (CHECK)" |
| Indicação | `IND` | "Oi! O(a) [nome] me indicou (IND)" |
| Prospecção ativa | `SDR` | Registrado sozinho pelo app quando o Lindson toca em "enviar" |
| Página de venda | `SITE` | O botão "Orçamento no WhatsApp" da /site/identidade/ |

### 1.3 As duas iscas

**Isca 1 · Diagnóstico de marca gratuito em 3 telas** (a principal; é ela que puxa a reunião)
- **Tela 1, "Sua marca hoje":** a marca como ela aparece hoje em 3 lugares (perfil do Instagram, um post e cartão ou fachada), lado a lado. Só imagem, sem crítica.
- **Tela 2, "O que dá para alinhar":** 3 pontos de consistência ditos com respeito, como "o logo aparece em 3 versões diferentes" ou "as cores mudam de post para post". Sem nota, sem "está feio" e sem número.
- **Tela 3, "Uma direção possível":** prancha com 3 referências premium do segmento (do método de `agencia/processos/pesquisa-premium.md`) e o próximo passo: "Quer que eu te explique como seria o projeto em 20 min?".
- Formato 4:5, na identidade Barzakh (Obsidiana, Marfim e Bronze; Instrument Serif + Inter Tight), enviado no WhatsApp como 3 imagens.
- **Prazo de entrega da isca:** [definir com o Lindson], porque depende da agenda dele.
- **Limite de diagnósticos por semana:** [definir com o Lindson], para a isca não comer o tempo das entregas pagas.

**Isca 2 · Checklist "Sua marca está pronta para se apresentar?"** (para o topo: comentário, story e Pinterest)

PDF de 1 página com 10 perguntas de sim ou não:
1. O logo é o mesmo no Instagram, na fachada e no cartão?
2. Existe uma versão do logo que funciona pequena (foto de perfil)?
3. As cores são sempre as mesmas?
4. As letras dos posts seguem um padrão?
5. Você teria orgulho de mandar o perfil para o seu maior cliente?
6. Quem faz os posts sabe as regras da marca?
7. Você tem os arquivos do logo em boa qualidade (SVG ou PDF)?
8. A marca combina com o preço que você cobra?
9. O cliente reconhece um post seu antes de ler o nome?
10. A marca aguenta uma fachada, uma embalagem e um uniforme?

Fecho: "Marcou 3 ou mais 'não'? Me chama que eu te mostro por onde começar." E o link wa.me com o código `CHECK`.

Entrega: palavra no comentário ou no direct (**MARCA**). Resposta com o PDF; sem ferramenta de automação de direct, o Lindson responde com o texto pronto da seção 4.

---

## 2. Oferta grand slam por pacote

### 2.1 A equação de valor (Hormozi) aplicada à Barzakh

Valor = (resultado sonhado × probabilidade percebida) ÷ (tempo de espera × esforço). O que a Barzakh faz em cada parte da equação, sem prometer resultado:

| Alavanca | O que a Barzakh faz |
|---|---|
| **Resultado sonhado ↑** | "Sua marca vai sair pronta para se apresentar": a mesma marca em tudo, que você tem orgulho de mostrar |
| **Probabilidade percebida ↑** | Cases reais aplicados (Real Time, WF Celulares, Processo Legislativo, Orégano Turbo, Dublê); conceito mostrado em mockup **antes** do arquivo final; processo em 6 etapas por escrito; fala direta com o designer |
| **Tempo de espera ↓** | Prazo por escrito no contrato (10, 20 e 30 dias úteis após o briefing) e datas de cada etapa na proposta |
| **Esforço ↓** | Briefing guiado (formulário + 20 min); a Barzakh aplica a marca para você; modelos prontos para quem posta; guia simples de uso |

### 2.2 Garantia da Travessia bem feita (garantia de processo, nunca de resultado)

A ideia vem do manifesto: "Não prometemos milagre. Prometemos a travessia bem feita." Ela vale para todos os pacotes. Os itens marcados com [decidir] dependem do Lindson.

1. **Prazo por escrito.** Cada etapa tem data na proposta e no contrato. Se a Barzakh atrasar por causa dela (e não por espera de resposta ou de material do cliente), o cliente ganha [decidir: uma aplicação extra ou uma rodada a mais].
2. **Rodadas de ajuste combinadas:** Limiar 2, Travessia 3 e Horizonte 3, mais o acompanhamento do 2.3.
3. **Conceito em mockup antes do arquivo final.** O cliente vê a marca aplicada antes de aprovar.
4. **Recomeço de conceito.** Se nenhum caminho apresentado fizer sentido na 1ª apresentação, refazemos o conceito do zero **uma vez**, sem custo. [decidir]
5. **Arquivos seus.** Na entrega final, todos os arquivos ficam com o cliente (PNG, SVG e PDF), sem mensalidade para usar a marca.

**Proibido na garantia:** "garantia de vendas", "de clientes", "de seguidores", "ou seu dinheiro de volta se não vender" e qualquer número de resultado.

### 2.3 Os três pacotes

Os valores ficam **a definir com o Lindson**. A esteira interna com faixas está só no privado (`dados/agencia/projeto-designer/ESTEIRA-INTERNA.md`).

Todos os bônus abaixo são sugestão. O Lindson confirma, porque cada um tem custo de produção.

#### Limiar: "atravesse para uma marca profissional"

**Para quem:** está começando ou nunca teve marca de verdade.

**Entrega** (de `../CANAIS.md`):
- briefing e persona;
- pesquisa de referências;
- 1 conceito de logo com versões (horizontal, vertical e símbolo);
- paleta e tipografia;
- 2 rodadas de ajuste;
- arquivos finais em PNG, SVG e PDF.

**Prazo:** até 10 dias úteis após o briefing.

**Bônus sugeridos:**
- Kit de perfil: foto de perfil e capa padronizadas para Instagram, WhatsApp Business, Google e LinkedIn.
- Guia de 1 página "Como usar sua marca": o que pode e o que não pode.
- Assinatura do WhatsApp Business: foto, catálogo e mensagem de saudação na identidade.

**Garantia:** a do 2.2.

#### Travessia: "a marca completa, no Instagram e no papel"

**Para quem:** já vende e quer a mesma marca em tudo. É o pacote **recomendado por padrão**: o meio que a maioria escolhe.

**Entrega:**
- tudo do Limiar;
- 2 caminhos de conceito;
- elementos gráficos e direção de fotografia;
- tom de voz;
- aplicações: perfil do Instagram, destaques, cartão e assinatura de e-mail;
- guia de marca em PDF;
- 3 rodadas de ajuste.

**Prazo:** até 20 dias úteis.

**Bônus sugeridos:**
- **Kit de lançamento da marca nova:** 3 posts e 2 stories anunciando a marca.
- **6 modelos editáveis no Canva** (post, carrossel e story) travados na identidade. Isso responde à objeção "o sobrinho faz no Canva".
- **30 dias de suporte no WhatsApp** depois da entrega, para dúvidas de uso.

**Garantia:** a do 2.2.

#### Horizonte: "a marca inteira, pronta para crescer"

**Para quem:** tem equipe, mais de uma unidade, ou vai abrir, expandir ou reformar.

**Entrega:**
- tudo da Travessia;
- brand book de 17 páginas;
- social kit, ou mini site/landing na identidade;
- apresentação da marca em reunião.

**Prazo:** até 30 dias úteis.

**Bônus sugeridos:**
- **Vídeo de apresentação da marca** (motion de 30 a 45 s com narração fluida, SFX e VFX, pela regra de vídeo com áudio). Serve para lançar a marca.
- **Treino de 1 h com quem posta**, para a equipe usar a marca sem improviso.
- **Revisão das 5 primeiras peças** que a equipe do cliente fizer com a marca nova.
- **60 dias de suporte no WhatsApp.**

**Garantia:** a do 2.2.

### 2.4 Escassez e urgência honestas

- **Vagas por mês:** [N], **decididas pelo Lindson** pela capacidade real da equipe. O número só aparece se for verdade no calendário. Nunca contador falso nem "últimas vagas" inventado.
- **Data de início:** toda proposta tem a data em que o projeto começa ("começo dia [data]"). Se o cliente não fechar, a data vai para o próximo encaixe livre. Essa é a urgência real.
- **Momento do cliente** (urgência que é dele, não nossa): inauguração, loja nova, reforma de fachada, impressão de cardápio, uniforme ou embalagem. Fazer a marca **antes** de imprimir evita gastar duas vezes.
- **Validade da proposta:** [definir com o Lindson] dias. Depois disso, a data de início é recalculada.

### 2.5 Upsell, cross-sell e downsell

Isto não mexe na esteira de produtos do Lindson (até R$ 3.500). Os valores de tudo abaixo ficam a definir com o Lindson.

| Tipo | Oferta | Quando oferecer | Quem entrega |
|---|---|---|---|
| Upsell no fechamento | Limiar → Travessia, Travessia → Horizonte. Mostrar o que o pacote de cima tem a mais, item por item | Na reunião, se o cliente citou fachada, equipe ou expansão | Barzakh |
| Upsell na entrega | **Site ou landing** na identidade nova | Na entrega final (mensagem 4.8) | Webdesigner / Al Kántara Labs |
| Upsell na entrega | **Kit de posts mensal** na identidade (modelos novos todo mês) | 30 dias depois da entrega | Barzakh |
| Cross-sell | **Social media / gestão do Instagram** e **tráfego pago** | 30 dias depois da entrega, se ele postar pouco | Agência do Lindson / Al Kántara Media |
| Cross-sell | Aplicações avulsas: fachada, embalagem, uniforme, cardápio, sinalização | Sempre que ele citar | Barzakh |
| Downsell 1 | **Limiar** (o essencial) para quem achou a Travessia cara | Objeção "caro" (3.4) | Barzakh |
| Downsell 2 | **Ajuste de marca:** refinar o logo que já existe, com paleta, tipografia e 3 aplicações, sem logo novo. [decidir se entra como oferta] | Objeção "já tenho logo" com logo aproveitável | Barzakh |
| Downsell 3 | **Parcelamento** do pacote, mantendo o pagamento antes de cada etapa começar. [decidir forma] | Quando o problema é o caixa do mês | O Lindson |
| Nutrição | Sem compra agora: entra na lista de conteúdo e volta a ser abordado depois de 90 dias | Fim da cadência sem resposta ou "agora não" | SDR |

---

## 3. Prospecção ativa

### 3.1 Lead ideal (persona de compra, em 5 linhas)

1. **Quem:** dono ou dona de negócio local da Grande São Luís (São Luís, São José de Ribamar, Paço do Lumiar e Raposa) e, depois, das capitais do Nordeste, de 28 a 50 anos.
2. **Nichos de entrada:** clínicas (estética, odonto, médicas), lojas de moda e calçados, restaurantes, hamburguerias, cafés e confeitarias, escritórios (advocacia, contabilidade), arquitetura e planejados, salões e barbearias premium, cursos e escolas livres.
3. **Sinal de momento** (melhor lead): inauguração ou "em breve", segunda unidade, mudança de endereço, reforma, aniversário de anos de casa, troca de nome ou de sócio.
4. **Sinal de capacidade:** ponto físico ou equipe, perfil ativo com posts recentes, presença no Google Maps com avaliações. A **régua de porte** (seguidores, avaliações) fica a definir com o Lindson; o SDR da Orégano usa ≥ 5 mil seguidores e serve de comparação.
5. **Sinal de dor** (só para a nota interna, **nunca na mensagem**): logo em versões diferentes, cores que mudam a cada post, foto de perfil cortada, perfil sem padrão.

**Fica fora:**
- pizzarias, que vão para o SDR da Orégano Turbo, para nunca abordar a mesma pizzaria duas vezes;
- clientes ativos da agência;
- franquias nacionais com marketing próprio;
- negócio fechado ou com perfil parado;
- perfil pessoal sem negócio;
- número achado só em agregador de CNPJ.

### 3.2 Onde achar

- **Google Maps:** busca por nicho + bairro (Renascença, Calhau, Cohama, Ponta d'Areia, Turu, Cohab, Olho d'Água, Ponta do Farol, Jardim Eldorado, centro de Ribamar). Ordenar por "aberto recentemente" quando a busca permitir.
- **Instagram:** hashtags e localizações da cidade (#saoluisma, #inauguracaosaoluis, #embreve + bairro), perfis de shoppings e centros comerciais que anunciam loja nova, perfis de associações e feiras locais.
- **Guias públicos:** Solutudo, Apontador e Guia Mais (os mesmos da `agencia/prospeccao/ROTINA.md`).
- **LinkedIn** (secundário, para empresa maior): sócios e gerentes de marketing de empresas locais. A mensagem é a mesma, com tom um pouco mais formal.

### 3.3 Filtro (obrigatório, sem exceção)

1. **WhatsApp de celular** confirmado em fonte do próprio negócio: bio, Linktree, site ou perfil do Google.
2. **Instagram próprio** ativo, com posts.
3. **Sem repetir:** comparar com os leads dos últimos 30 dias de **todos** os SDRs (agência, Orégano e Barzakh) pelo @, pelo nome normalizado e pelos últimos 8 dígitos do telefone.
4. Campo não achado fica `null`. Nunca inventar dado.

Quem não tem os dois contatos (WhatsApp e Instagram) não entra na fila: sem botão, sem mensagem.

### 3.4 Cadência: 5 toques em 10 dias

Cada mensagem tem no máximo 280 caracteres e é enviada pelo botão do app, com o texto já escrito. Preencha [nome] e [negócio].

| Dia | Canal | Toque |
|---|---|---|
| D0 | WhatsApp | Abordagem (Conexão → Dor → Desejo → Pergunta) |
| D2 | WhatsApp | Prova: 1 imagem de case aplicado (sem link) |
| D4 | Direct do Instagram | Toque leve + oferta da isca |
| D7 | WhatsApp | Isca: diagnóstico gratuito em 3 telas |
| D10 | WhatsApp | Despedida educada → etapa `nutrir`, reabordagem depois de 90 dias |

Respondeu em qualquer toque: a cadência para e o lead vai para `respondeu`.

**D0 · abordagem.** Escolha a versão do nicho e varie a abertura entre leads do mesmo nicho.

Clínica:
```
Oi, Dra. [nome]! Aqui é o Lindson, do estúdio Barzakh, de São Luís.
A paciente escolhe a clínica que passa mais confiança, muitas vezes antes de marcar.
Eu crio a marca completa, do logo ao Instagram, com a mesma cara em tudo.
Posso te mostrar como ficaria a da [negócio]?
```
Loja e comércio:
```
Oi, [nome]! Aqui é o Lindson, do estúdio Barzakh, de São Luís.
Muita loja boa perde cliente porque a marca parece menor que o negócio.
Eu crio a identidade visual completa, do logo ao Instagram, pra passar confiança.
Posso te mostrar como ficaria a da [negócio]?
```
Comida (restaurante, café, hamburgueria):
```
Oi, [nome]! Sou o Lindson, do estúdio Barzakh, aqui de São Luís.
Comida boa perde venda quando a marca não mostra o capricho que tem no prato.
Eu faço a identidade completa: logo, cores, embalagem e Instagram.
Quer ver como ficaria a do [negócio]?
```
Escritório e profissional liberal:
```
Oi, Dr. [nome]! Meu nome é Lindson, do estúdio Barzakh, de São Luís.
O cliente pesquisa o escritório no Instagram antes de ligar e escolhe quem passa mais seriedade.
Eu crio a identidade visual completa, à altura do seu trabalho.
Posso te mostrar como faria?
```
Negócio abrindo ou mudando (sinal de momento):
```
Oi, [nome]! Aqui é o Lindson, do estúdio Barzakh, de São Luís.
Abrir com marca improvisada costuma sair caro: depois tem que refazer fachada, cartão e tudo.
Eu crio a marca certa antes de imprimir.
Posso te mandar como funciona?
```

**D2 · prova** (com 1 imagem de case aplicado: WF Celulares, Real Time, Processo Legislativo ou Orégano Turbo, o mais próximo do nicho):
```
[nome], te mando um trabalho do estúdio pra você ter uma ideia: a marca da [case], já aplicada no Instagram e no cartão.
Se fizer sentido pra [negócio], te mostro como seria a sua. Pode ser?
```

**D4 · direct do Instagram:**
```
Oi, [nome]! Aqui é o Lindson, do estúdio Barzakh. Te chamei no WhatsApp também.
Faço identidade visual pra negócio de São Luís.
Se quiser, monto um diagnóstico rápido da marca da [negócio], de graça, em 3 telas. Quer?
```

**D7 · isca:**
```
[nome], uma ideia sem compromisso: monto um diagnóstico rápido da marca da [negócio] em 3 telas.
Como ela aparece hoje, o que dá pra alinhar e uma direção possível.
É gratuito. Quer que eu faça?
```

**D10 · despedida:**
```
[nome], não quero te encher de mensagem, então paro por aqui.
Se um dia quiser arrumar a marca da [negócio], é só me chamar neste número que eu te atendo.
Sucesso aí!
```

### 3.5 Quebra de objeções

Regra das respostas: concordar, explicar com um fato do processo e terminar com uma pergunta fácil. Sem pressão e sem promessa.

**"Tá caro."**
```
Entendo, [nome]. Por isso existem 3 pacotes: dá pra começar pelo Limiar, com o essencial, e crescer depois.
E a marca você usa em tudo que imprime e posta, por muito tempo.
Quer que eu te mostre o que cabe agora?
```

**"Agora não / depois."**
```
Tranquilo, [nome]. Só uma pergunta: vem aí alguma fachada, cardápio, uniforme ou loja nova?
Se vier, vale fazer a marca antes de imprimir, pra não gastar duas vezes.
Quando é melhor eu te chamar de novo?
```

**"Meu sobrinho faz no Canva."**
```
Faz sentido, e o Canva ajuda muito no dia a dia.
A diferença é que a gente entrega o sistema: logo, cores, letras e modelos prontos, até no Canva, pra quem posta seguir a mesma cara.
Quer ver um exemplo?
```

**"Já tenho logo."**
```
Ótimo, então não começamos do zero.
Muitas vezes o logo fica e o que falta é o resto: cores, letras, versões e como aplicar no Instagram e no papel.
Me manda o seu? Te digo com sinceridade o que vale manter.
```

**"Vou pensar."**
```
Claro, [nome]. Pra te ajudar a pensar: ficou alguma dúvida sobre prazo, o que entra no pacote ou forma de pagamento?
Me fala que eu te respondo direto.
```

**"Preciso falar com meu sócio ou minha sócia."**
```
Perfeito. Quer que eu te mande um resumo curto pra mostrar?
Se preferir, faço uma chamada de 15 min com vocês dois. Qual fica melhor?
```

### 3.6 Roteiro da reunião de 20 minutos

Por chamada de vídeo ou ligação de WhatsApp, com o briefing já recebido, se possível. O cliente fala mais que o Lindson.

| Min | Bloco | O que fazer e dizer |
|---|---|---|
| 0–2 | **Abertura** | Agradecer e combinar: "Vou te ouvir, te mostrar 2 trabalhos e o caminho. No fim você decide se faz sentido." |
| 2–9 | **Escuta** (o herói fala) | 1. "Me conta do negócio: o que vende e quem compra de você?" 2. "Onde a marca aparece hoje?" 3. "O que te incomoda na marca hoje?" 4. "Vem alguma coisa aí: fachada, loja nova, impressão?" 5. "O que acontece se ficar como está mais um ano?" 6. "Quem decide junto com você?" 7. "Pra quando você precisa?" Anotar as palavras dele: elas vão para a proposta. |
| 9–13 | **Mostrar** (o guia) | 2 cases antes e depois **aplicados** (o mais parecido com o nicho). O processo em 6 etapas. "Você vê a marca no mockup antes de qualquer arquivo final." |
| 13–17 | **Recomendação** | 1 pacote recomendado e o porquê, com as palavras dele ("você falou da fachada nova, por isso a Travessia"). Citar os outros dois. **Dizer o valor aqui, na conversa**, com a forma de pagamento (antecipado). |
| 17–20 | **Próximo passo** | "Te mando a proposta por escrito até [amanhã/hoje]. Tenho início livre dia [data]. Faz sentido a gente começar nessa data?" Marcar no app: `proposta`. |

**Não fazer:**
- prometer venda, cliente ou seguidor;
- usar jargão ("branding 360", "DNA", "posicionamento disruptivo");
- falar mal do designer anterior;
- falar da origem religiosa do nome sem o cliente perguntar (`../marca/ESTRATEGIA.md`, seção 7).

### 3.7 Proposta e follow-up da proposta

**A proposta em PDF** parte do modelo `../../v2/oferta/proposta-identidade-visual-v2.pdf` (8 lâminas 16:9), refeito na identidade Barzakh.

Troca da v2 para a v3:
- "Lindson Almeida Studio" passa a "Barzakh · um estúdio Al Kántara";
- Essencial, Completo e Premium passam a Limiar, Travessia e Horizonte.

O que entra:
- resumo do briefing com as palavras do cliente;
- o pacote recomendado;
- o que entrega;
- bônus;
- a Garantia da Travessia bem feita;
- etapas com data;
- validade;
- próximo passo.

**Sem preço impresso.** Decisão a confirmar: a v2 tinha "Investimento: [preencher]". Pelo pedido de 16/11, o valor vai na conversa, logo depois do PDF.

| Quando | Mensagem |
|---|---|
| D+0, junto com o PDF | (abaixo) |
| D+1 | (abaixo) |
| D+3 | (abaixo, com 1 imagem de case parecido) |
| D+7 | (abaixo; só se a data for real) |
| D+14 | Encerramento → `nutrir` |

D+0:
```
[nome], aqui está a proposta da [negócio], com tudo que conversamos e as datas de cada etapa.
O investimento do pacote [pacote] é [valor], pago antes de começar. Ficou alguma dúvida?
```
D+1:
```
[nome], conseguiu ver a proposta com calma?
Se quiser, te explico qualquer parte por áudio.
```
D+3:
```
[nome], separei um trabalho parecido com o da [negócio] pra você ver como fica aplicado.
Ficou alguma dúvida sobre o pacote ou as datas?
```
D+7 (escassez honesta, só se for verdade no calendário):
```
[nome], estou fechando a agenda de [mês]. Tenho início livre dia [data].
Quer que eu reserve pra [negócio]?
```
D+14:
```
[nome], vou arquivar a proposta por aqui pra não te incomodar.
Se quiser retomar, me chama que eu atualizo as datas e a gente começa.
```

---

## 4. Scripts de WhatsApp para inbound

Responder rápido, no horário comercial. Primeiro qualificar em 3 perguntas, depois oferecer a isca ou a reunião. Uma pergunta fácil por mensagem.

**4.1 Resposta ao anúncio** (`META`/`GOOG`):
```
Oi, [nome]! Aqui é o Lindson, do estúdio Barzakh. Que bom que você chamou.
Pra eu te mostrar o caminho certo, me conta: qual é o seu negócio e onde a marca aparece hoje (Instagram, loja, fachada)?
```
E em seguida, depois da resposta:
```
Entendi. Te mando 2 trabalhos parecidos com o seu.
Se quiser, faço um diagnóstico rápido da sua marca, de graça, em 3 telas. Me manda seu @ e o logo atual, se tiver?
```

**4.2 "Quanto custa?"** (2 mensagens; o valor só sai depois do briefing ou da reunião):
```
Depende do que a sua marca precisa agora, [nome]. São 3 pacotes: Limiar (o essencial), Travessia (a marca completa no Instagram e no papel) e Horizonte (brand book e tudo pronto pra crescer).
```
```
Me responde 3 coisas rapidinho? O que você vende, onde a marca vai aparecer e pra quando precisa.
Aí te digo qual pacote faz sentido, com valor e prazo certinhos.
```
Se ele insistir no valor antes: dar a **faixa** do pacote mais provável, na conversa, e voltar às 3 perguntas. Faixas: esteira interna do privado; nunca em peça pública.

**4.3 "Vi no Pinterest"** (`PIN`):
```
Oi, [nome]! Que bom que chegou pelo Pinterest. Lá estão alguns trabalhos do estúdio.
Qual deles mais chamou sua atenção? Me conta também o que você vende, que eu te mostro como ficaria na sua marca.
```

**4.4 Behance ou LinkedIn** (`BEH`/`LIN`, empresa maior):
```
Oi, [nome]! Aqui é o Lindson, diretor criativo da Barzakh. Obrigado pelo contato.
Pra eu entender o projeto: é marca nova ou mudança de uma que já existe? E qual prazo vocês têm em mente?
```

**4.5 Indicação** (`IND`; quem indicou recebe agradecimento no mesmo dia):
```
Oi, [nome]! Aqui é o Lindson, do estúdio Barzakh. O(a) [quem indicou] me passou seu contato e disse que você está pensando na marca da [negócio].
Posso te mandar como a gente trabalha?
```

**4.6 Checklist** (`CHECK`/palavra MARCA):
```
Oi, [nome]! Aqui está o checklist "Sua marca está pronta para se apresentar?". São 10 perguntas de sim ou não.
Marcou 3 ou mais "não"? Me chama que eu te mostro por onde começar.
```

**4.7 Entrega do diagnóstico** (`DIAG`):
```
[nome], aqui está o diagnóstico da [negócio], em 3 telas. A última mostra uma direção possível.
Se fizer sentido, a gente conversa 20 min e eu te explico como seria o projeto. Qual o melhor dia?
```
Confirmação da reunião:
```
Combinado, [nome]: [dia] às [hora], por [vídeo/ligação], 20 min.
Antes, se puder, preenche o briefing rapidinho: [link do briefing]. Assim a conversa rende mais.
```

**4.8 Pós-venda** (depois da entrega final):

D+7, checagem:
```
[nome], já deu pra usar a marca nova? Ficou alguma dúvida sobre os arquivos ou o guia?
Estou por aqui.
```
D+15, depoimento:
```
[nome], posso te pedir um favor? Me manda 2 ou 3 linhas, ou um áudio, contando como foi o processo com a gente.
Com a sua autorização, vai pro portfólio do estúdio.
```
D+30, indicação e upsell:
```
[nome], com a marca pronta, o próximo passo natural é colocar ela pra trabalhar: site, kit de posts ou a gestão do Instagram.
Quer que eu te mostre o que faria mais sentido agora pra [negócio]?
```
```
E se conhecer alguém que está precisando arrumar a marca, me apresenta?
Eu cuido com o mesmo carinho.
```
O que fazer com o depoimento:
- vai para o card do portfólio (portfólio automático) e para o case do Behance;
- **nada de número de resultado** ("vendi 3× mais"): esse trecho fica fora;
- em saúde, seguir a regra CFO/CRO (sem promessa).

---

## 5. Métricas e rotina

### 5.1 Métricas: só nomes e fórmulas

Nenhuma meta é inventada. Média e meta saem dos próprios dados, depois de 4 semanas de registro.

| Métrica | Fórmula | Onde lê |
|---|---|---|
| Leads na fila | contatos com etapa `novo` que passaram no filtro | App SDR |
| Abordados | contatos que saíram de `novo` no período | App SDR |
| Taxa de número sem WhatsApp | números sem WhatsApp ÷ envios tentados | Robô SDR |
| Taxa de resposta | contatos em `respondeu` ou adiante ÷ abordados | App SDR |
| Taxa de pedido de isca | diagnósticos pedidos ÷ respostas (ativo) ou ÷ conversas (inbound) | App SDR |
| Conversas inbound por canal | conversas com o código X no período | Códigos de origem |
| Custo por conversa (anúncio) | investimento do anúncio ÷ conversas iniciadas com `META`/`GOOG` | Gerenciador + app |
| Taxa de reunião | reuniões feitas ÷ (respostas + conversas inbound qualificadas) | App SDR |
| Comparecimento | reuniões feitas ÷ reuniões marcadas | App SDR |
| Taxa de proposta | propostas enviadas ÷ reuniões feitas | App SDR |
| Taxa de fechamento | fechados ÷ propostas enviadas | App SDR |
| Taxa de fechamento por origem | fechados com código X ÷ propostas com código X | App SDR |
| Mix de pacotes | fechados de cada pacote ÷ total de fechados | App SDR |
| Ticket médio | receita fechada ÷ número de fechados | App + financeiro |
| Ciclo de venda | média de (data do fechamento − data do 1º contato) | App SDR |
| Custo por cliente (CAC) | (investimento em anúncio + custos de prospecção) ÷ clientes novos | Financeiro |
| Prazo cumprido | entregas no prazo ÷ entregas | Painel do cliente |
| Rodadas usadas | média de rodadas de ajuste por projeto | Painel do cliente |
| Taxa de depoimento | depoimentos recebidos ÷ entregas | Pós-venda |
| Taxa de indicação | clientes novos com `IND` ÷ clientes novos | Códigos de origem |
| Taxa de upsell | clientes com 2º serviço ÷ clientes entregues | App SDR / Central |
| Receita por cliente (LTV) | soma de tudo que o cliente pagou (pacote + upsell) | Financeiro |

### 5.2 Rotina do Lindson: 15 minutos por dia

O app deixa tudo pronto. Ele só lê, toca em "enviar" e decide. Reunião e entrega ficam fora destes 15 minutos.

| Bloco | Min | O que faz |
|---|---|---|
| 1. Responder | 5 | Abre a esteira, filtra `respondeu`, e responde com os scripts da seção 3.5 e da seção 4 (um toque copia ou abre a mensagem) |
| 2. Disparar | 5 | No modo disparo: os toques do dia (D2, D4, D7, D10) e os follow-ups de proposta (D+1, D+3, D+7, D+14). O robô SDR cuida do D0 |
| 3. Mover e agendar | 5 | Arrasta as etapas, marca as reuniões da semana e confere o que o Claude deixou para aprovar (diagnósticos, propostas) |

Varia por dia:
- **Segunda:** no bloco 3, aprova a lista de leads da semana (5 min).
- **Quarta:** no bloco 3, aprova os diagnósticos da semana antes de enviar.
- **Sexta:** troca o bloco 3 pela leitura do relatório semanal (métricas 5.1, uma linha de decisão: o que cortar e o que manter).

---

## 6. Automação: o que já existe e o que falta

### 6.1 O que já existe (procurado com `git grep sdr` e `git log --all --grep sdr`)

**1. Aba SDR do painel do administrador da Central**
- Endereço: `/painel/admin#sdr` em lindsonalmeida.pages.dev. Feita pela conta Leandro em 11/11.
- Código no branch `origin/claude/aba-sdr`, ainda **não juntado** ao branch principal deste repositório. O site no ar sai do privado `CentralLindsonALmeida`.
- Arquivos: `agencia/sistema-clientes/site/admin-sdr.js`, `functions/api/sdr.js` e `functions/_sdr.js`.
- Já faz:
  - lista por nota;
  - **modo disparo** em lotes de 20;
  - botões Instagram e WhatsApp com a mensagem pronta (`wa.me/<número>?text=`). Ao tocar, o envio é registrado e o contato vai para a esteira.
- Etapas da esteira: `novo → enviado → respondeu → reuniao → proposta → fechado / perdido`, guardadas no KV `sdr:status`.
- Os contatos estão fixos em `_sdr.js`: são leads de **agência**, não de identidade visual.

**2. Robô SDR no WhatsApp Web**
- Pasta: `agencia/prospeccao/robo-sdr/`, no mesmo branch `origin/claude/aba-sdr`. Registro de 12/11 da conta Pedro.
- Pega o lote da `/api/sdr?lote=20` e envia sozinho.
- Limites: 20 por dia, 4 a 9 min entre envios, de segunda a sexta das 9h às 18h, e para depois de 3 números sem WhatsApp.
- Roda no WhatsApp Business principal do Lindson (decisão de 12/11). Risco anotado: vai contra as regras do WhatsApp.
- Status e botão Pausar/Ligar ficam na aba SDR.

**3. SDR da Orégano Turbo (o modelo mais completo para copiar)**
- Endereço: `/painel/oregano#sdr`. Feito pela conta Zuleide em 15/11.
- Funil de 10 etapas, cadência D+2/D+5/D+10, botão WhatsApp que registra o envio e meta diária.
- Arquivos: API `/api/sdr-oregano` (KV `sdr:oregano:*`), gerador `agencia/sistema-clientes/oregano-turbo/montar-sdr.py`.
- Régua do público-alvo: `agencia/operacao-propria/sdr/PUBLICO-ALVO.md`. Tem tarefa diária de busca de leads.

**4. Outros apps**
- **SDR para Agências** (artifact `NztpiSW1Dd4JAjpXZ5CwBd`) e **Recomeço 90** (funil e lista diária, `agencia/app/recomeco90.html`). Estão em `ESTADO-DO-PROJETO.md`.

**5. Formulário de briefing**
- No privado: `site/identidade/briefing.html`. Envia as respostas pelo WhatsApp.

**6. Contratos, Downloads e Tarefas feitas**
- O app de contratos usa `agencia/processos/modelo-contrato/`.
- Os PDFs vão para a página de Downloads.
- Toda entrega é lançada em Tarefas feitas (`/api/automacao?fila=ped`, acao `feito`).

### 6.2 O que falta (em ordem)

1. **Aba SDR da Barzakh:** copiar o `montar-sdr.py` da Orégano para `/painel/admin#sdr-barzakh` (ou um painel próprio da Barzakh na Central), com API `/api/sdr-barzakh` e KV `sdr:barzakh:*`.
   - **Etapas:** `novo → enviado → respondeu → diagnostico → briefing → reuniao → proposta → fechado → entrega → posvenda`, mais `perdido` e `nutrir`.
   - **Cadência:** a da seção 3.4.
   - **Botão WhatsApp:** com a mensagem da etapa (seções 3 e 4), visível na ficha fechada. Ao tocar, registra o envio e avança a etapa. Sem número, copia a mensagem.
   - **Fila:** só entra lead com WhatsApp e Instagram.
2. **Busca diária de leads Barzakh:** tarefa agendada no padrão da Orégano, com o ICP da seção 3.1 e o filtro da 3.3.
   - Deduplicar contra **todos** os SDRs.
   - Gravar os descartados com o motivo.
   - Antes, salvar a régua em `agencia/operacao-propria/sdr/PUBLICO-ALVO-BARZAKH.md`.
3. **Juntar o branch `claude/aba-sdr`** (robô e aba) ao branch principal, ou confirmar que a versão no ar é a do privado. Hoje o código do robô só está nesse branch.
4. **Robô SDR por fila:** o robô lê só `/api/sdr`. Falta ler o lote da Barzakh (parâmetro `fila=barzakh`) sem passar dos 20 envios por dia **somados** de todas as filas, porque o número de WhatsApp é o mesmo.
5. **Códigos de origem automáticos:** ao chegar mensagem com `(IG)`, `(PIN)` etc., o app cria a ficha com a origem. Hoje é manual: o Lindson cola o código na ficha.
6. **Gerador do diagnóstico de 3 telas:** script que monta as 3 imagens 4:5 a partir do @ e de fotos do perfil enviadas pelo cliente. As capturas do Instagram não abrem sem login: o cliente manda os prints, ou o Lindson tira.
7. **Proposta v3 Barzakh:** refazer o PDF da v2 com o nome e os pacotes novos, sem preço impresso, e um gerador que preencha nome, briefing, pacote e datas.
8. **Página de venda e briefing com o nome novo:** trocar `STUDIO`/`HANDLE` em `../../gerador/conteudo.py` e rodar `gerador/landing.py`. Também o campo "Pacote de interesse" para Limiar, Travessia e Horizonte. Isto já estava apontado no `../CANAIS.md`.
9. **Briefing salvo na Central,** não só no WhatsApp: o formulário grava no KV e cria a ficha em `briefing`.
10. **Pós-venda automático:** ao marcar `entrega`, o app agenda os lembretes D+7, D+15 e D+30 (seção 4.8) e, ao fechar, cria o painel do cliente na Central (de `prototipo/painel.html`) e lança em Tarefas feitas.
11. **Relatório semanal:** bloco da sexta com as fórmulas da seção 5.1, calculadas do histórico (`hist[]`) de cada ficha.

**Limite real:** o direct do Instagram não tem envio automático permitido. O botão Instagram abre o perfil e copia a mensagem; o Lindson cola e envia.

---

## 7. Decisões que dependem do Lindson

1. Valores e faixas de cada pacote (só na conversa) e forma de pagamento antecipado (Pix, cartão, parcelamento).
2. Vagas por mês e validade da proposta.
3. Quais bônus entram em cada pacote (todos têm custo de produção).
4. Garantia: o que o cliente ganha se a Barzakh atrasar, e se o "recomeço de conceito" entra.
5. Se o "Ajuste de marca" (downsell 2) vira oferta.
6. Régua de porte do lead (seguidores ou avaliações) e quantos diagnósticos gratuitos por semana.
7. Proposta sem preço impresso, como pedido em 16/11 (a v2 tinha o campo "Investimento").
8. Se a prospecção da Barzakh divide o limite de 20 envios por dia do robô com o SDR da agência.
