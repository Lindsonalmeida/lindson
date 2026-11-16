# Prompt para a extensão do Chrome (Claude) · Barzakh · estrutura completa na Meta, tudo PAUSADO
(conta Leandro, 16/11/2026; estratégia em `TRAFEGO.md`, criativos em `CRIATIVOS.md`; formato copiado de `agencia/clientes/rt-full-jobs/trafego/PROMPT-EXTENSAO-META.md`, conta Pedro)

Antes de colar, o Lindson precisa ter feito (**travado: precisa do Lindson**): Instagram @barzakhstudio e Página do Facebook "Barzakh" criados; número do WhatsApp Business do estúdio confirmado; decisão de qual portfólio empresarial usar. Cole o texto abaixo na extensão, com o Chrome logado no Facebook do Lindson.

---

Você vai montar a estrutura de anúncios do estúdio **Barzakh** (identidade visual e branding, São Luís/MA, um estúdio do Al Kántara Group) na Meta. Trabalhe em business.facebook.com e adsmanager.facebook.com. Vá passo a passo e me mostre um resumo curto ao fim de cada etapa.

**Regra principal: TUDO fica DESLIGADO (pausado) ou em rascunho.** Eu ligo depois de aprovar a verba. Nunca clique em "Publicar" com campanha ativa; se o Gerenciador obrigar a publicar para salvar, publique com campanha, conjuntos e anúncios **desligados** e me avise.

**PARE e me chame antes de:** cadastrar cartão ou forma de pagamento; aceitar termos em meu nome; digitar senha ou código de verificação; definir qualquer valor de orçamento (deixe o campo para eu preencher, ou use o mínimo que o sistema exigir com a campanha desligada e me avise); ligar qualquer coisa; excluir qualquer coisa (nunca exclua: desligue). Nunca escreva senha nem token em lugar nenhum.

**Nunca use** nenhuma imagem, nome ou vídeo do vereador Leo Pinto nos anúncios (regra de anúncio político da Meta). Não marque nenhum anúncio como "Temas sociais, eleições ou política": se o sistema sugerir essa categoria, PARE e me chame.

## 1. Portfólio empresarial
- Use o portfólio que eu indicar: **[Al Kántara Group / Lindson Almeida]**. Se não existir um chamado "Al Kántara Group", pergunte se deve criar antes de criar.
- Adicione a Página do Facebook "Barzakh" e o Instagram @barzakhstudio. Se a Página não existir, PARE e me chame (eu crio; categoria "Designer gráfico" ou "Serviço de design").
- Conecte o WhatsApp Business do estúdio à Página. Se pedir código no celular, me chame.

## 2. Conta de anúncios
- Se já existir uma conta "Barzakh · Anúncios", use. Se não, crie: nome "Barzakh · Anúncios", fuso America/Fortaleza, moeda BRL.
- Dê acesso de administrador a mim.
- Pagamento: PARE e me chame.

## 3. Conjunto de dados (Pixel)
- Crie o "Barzakh · Pixel", ligado à conta de anúncios.
- Mostre o ID. Não instale nada no site e não gere token da API de Conversões; a equipe instala.
- Em Gerenciador de Eventos, anote se já chega algum evento de lindsonalmeida.pages.dev.

## 4. Públicos (Públicos > Criar)
1. **BZ · Engajou IG+FB 90d:** quem interagiu com o Instagram @barzakhstudio ou com a Página nos últimos 90 dias.
2. **BZ · Viu 50% vídeo 90d:** quem assistiu a pelo menos 50% de qualquer vídeo da Página ou do Instagram.
3. **BZ · Mensagem 30d:** quem enviou mensagem para a Página, o Instagram ou o WhatsApp nos últimos 30 dias.
4. **BZ · Visitou página 30d:** Pixel, todos os visitantes de URLs que contêm `/site/identidade`, 30 dias.
5. **BZ · Abriu case 30d:** Pixel, evento ViewContent, 30 dias. Se o evento ainda não existir, crie assim mesmo e anote.
- Não crie público semelhante nem lista de clientes agora.

## 5. Campanhas (todas DESLIGADAS)

### M1 · `BZ · Meta · Mensagens WhatsApp · MA Amplo`
- Objetivo **Engajamento**, local da conversão **Apps de mensagem → WhatsApp**, meta de desempenho **maximizar conversas**.
- Orçamento na campanha (Advantage+ orçamento / CBO): **deixe para eu preencher** ("verba: definir com o Lindson").
- **1 conjunto** `MA Prioritário · 25-55 · Advantage+`:
  - Local, "pessoas que moram ou estiveram recentemente": São Luís, São José de Ribamar, Paço do Lumiar, Raposa, Imperatriz, Caxias, Timon, Bacabal, Santa Inês, Codó, Balsas, Açailândia, Pinheiro, Chapadinha, Barreirinhas, Zé Doca e São João Batista (todas no Maranhão).
  - Idade 25 a 55.
  - Público Advantage+ ligado, com **sugestões** de público (não restrição): administradores de página de empresa, pequenas empresas, proprietários de pequenas empresas, empreendedorismo, design gráfico, branding. Me diga quais dessas opções existem e quais não achou.
  - Excluir o público "BZ · Mensagem 30d".
  - Posicionamentos Advantage+. Horário contínuo.

### M2 · `BZ · Meta · Página Identidade · MA Amplo`
- Objetivo **Leads** (se não deixar otimizar pelo Pixel sem eventos, use **Tráfego** com meta "visualizações da página de destino" e me avise).
- Evento: **Contact** (se ainda não existir no Pixel, escolha o que houver e me avise).
- Mesmo conjunto do M1 (copie as configurações), nome `MA Prioritário · Página`.
- Site: `https://lindsonalmeida.pages.dev/site/identidade/` (ou o endereço que eu indicar).
- Parâmetros de URL em todos os anúncios:
  `utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&utm_id={{campaign.id}}`

### M3 · `BZ · Meta · Remarketing · Quente 90d`
- Objetivo **Engajamento → WhatsApp → maximizar conversas**.
- 1 conjunto `Quente 90d`: públicos 1, 2, 4 e 5 somados; excluir o 3. Sem restrição de idade além de 18+. Local: Brasil (o público já é só quem conhece o estúdio).
- Anote o tamanho estimado do público.

## 6. Anúncios (todos DESLIGADOS)
Os arquivos de imagem e vídeo estão numa pasta do meu computador que eu vou indicar (`Barzakh/anuncios/`), um arquivo por código. **Se o arquivo de um código não estiver lá, crie o anúncio só com o texto, sem mídia, deixe desligado e anote "falta mídia".** Não use foto de banco nem gere imagem com IA no lugar.

- Nome de cada anúncio = o código (ex.: `BZ-V1`).
- Botão: **Enviar mensagem** (M1, M3) / **Saiba mais** (M2).
- Mensagem pronta do WhatsApp (troque só o código): `Oi! Vim pelo anúncio (BZ-V1). Quero saber da identidade visual da minha marca.`
- Desligue os "aprimoramentos criativos Advantage+" que mudam texto, música ou geram imagem (deixe só ajustes de corte/brilho, se quiser). Me diga quais estavam ligados.
- **M1 (lote 1):** BZ-E1, BZ-E2, BZ-E5, BZ-V1, BZ-V2, BZ-V5 e, se houver o vídeo, BZ-V3.
- **M2:** BZ-E5 e BZ-V2 (versões com botão "Saiba mais").
- **M3:** BZ-E3 e BZ-V4.
- Lote 2 (BZ-E4, BZ-E6, BZ-V6) **não** sobe agora.

Textos (texto principal · título · descrição), sem mudar nenhuma palavra:

**BZ-E1** · Aqui é o Lindson, do Barzakh, estúdio de design de São Luís. Muito negócio bom ainda se apresenta com um logo feito às pressas. A gente cria a identidade visual completa e mostra a marca aplicada antes do arquivo final. Quer ver como ficaria a sua? · Identidade visual em São Luís · Fale com o designer

**BZ-E2** · Oi! Sou o Lindson, do estúdio Barzakh, aqui de São Luís. Mandar fazer fachada e cartão sem ter visto a marca pronta é um risco caro. Aqui você vê a marca aplicada na fachada, no cartão e no Instagram antes de qualquer arquivo final. Posso te mostrar como funciona? · Sua marca aplicada antes de imprimir · Projeto Real Time

**BZ-E3** · Oi, de novo! Aqui é o Lindson, do Barzakh. Muita gente desiste de fazer a marca porque não sabe como o processo funciona nem quanto tempo leva. Aqui são 6 etapas, com prazo combinado no início e conversa direta com o designer. Quer que eu te mande o passo a passo? · Processo em 6 etapas · Prazo combinado por escrito

**BZ-E5** · Aqui é o Lindson, do estúdio Barzakh, de São Luís. Antes de chamar no WhatsApp, o cliente abre o perfil. Se cada post sai de um jeito, ele chama outro. A gente monta a identidade e o kit do Instagram pra tudo sair com a mesma cara. Posso te mostrar como ficaria o seu? · Instagram com cara de marca · Do logo ao Instagram

**BZ-V1** · Aqui é o Lindson, do Barzakh, estúdio de design de São Luís. Muita marca nasce num rabisco e fica nele por anos. A gente transforma em identidade completa e mostra aplicada antes do arquivo final. Quer ver como ficaria a sua? · Do rabisco à marca pronta · Projeto Orégano Turbo

**BZ-V2** · Oi! Sou o Lindson, do estúdio Barzakh, em São Luís. O cliente olha o perfil antes de chamar, e decide em poucos segundos. A gente cria a marca e o Instagram com a mesma cara, como fizemos na Real Time. Posso te mostrar como ficaria o seu? · O cliente decide no perfil · Projeto Real Time

**BZ-V3** · Aqui é o Lindson. Barzakh quer dizer passagem, e é isso que a gente faz com a sua marca. Muito negócio bom se apresenta menor do que é. Você fala direto comigo, do briefing à entrega. Quer conversar sobre a sua? · Fale direto com o designer · Barzakh · São Luís

**BZ-V4** · Oi, de novo! Aqui é o Lindson, do Barzakh. Muita gente adia a marca porque não sabe como é o processo. Aqui são 6 etapas, com prazo combinado por escrito e conversa direta comigo. Quer que eu te mande como funciona? · Como uma marca nasce aqui · Projeto Processo Legislativo

**BZ-V5** · Aqui é o Lindson, do estúdio Barzakh, de São Luís. Quando cada material sai de um jeito, o cliente não lembra da sua marca. A gente entrega a marca e um guia simples pra ela sair igual em tudo. Quer ver o projeto da WF? · A mesma marca em tudo · Projeto WF Celulares

(Quebre o texto principal em 4 linhas, uma por frase, como está em `CRIATIVOS.md`.)

## 7. Conferência antes de terminar
- Confira que **nenhuma** campanha, conjunto ou anúncio está ligado.
- Confira que nenhum texto tem preço, "garantido", "o melhor", número de resultado ou pergunta sobre dinheiro, idade, saúde ou religião de quem lê.
- Se algum anúncio foi reprovado ou marcado como político, anote o motivo exato e não tente contornar.

## 8. Fim
Me mande uma lista curta:
- ID do portfólio, da conta de anúncios e do Pixel;
- os 5 públicos criados, com o tamanho estimado;
- as 3 campanhas, conjuntos e anúncios, cada um com a mídia usada ou "falta mídia", e o status (todos DESLIGADOS);
- as sugestões de público que não existiam;
- o que ficou pendente (pagamento, verba, WhatsApp, Pixel no site, mídias que faltam).
