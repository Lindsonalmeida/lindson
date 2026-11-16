# Barzakh · tráfego pago (conta Leandro, 16/11/2026)

Situação: **rascunho para aprovação do Lindson.** Nada no ar. Tudo é montado em rascunho/pausado até ele aprovar a verba.

Base: `../marca/ESTRATEGIA.md` (posicionamento, tom, palavras proibidas), `../CANAIS.md` (@barzakhstudio, pacotes Limiar/Travessia/Horizonte, mensagens de WhatsApp), `../../README.md` (persona), `../../OFERTA.md` (processo em 6 etapas), `../../v2/oferta/anuncio/` (carrossel de 5 telas) e os 6 cases de `../../behance/`. Formato copiado das estratégias de tráfego da equipe: `agencia/clientes/rt-full-jobs/trafego/ESTRATEGIA-V2.md` e `agencia/ofertas/low-ticket/trafego/ESTRATEGIA-V2.md` (conta Pedro). Criativos: `CRIATIVOS.md`. Montagem na Meta: `PROMPT-EXTENSAO-META.md`.

Agentes consultados (em silêncio): Traffic Chief, Pedro Sobral, Molly Pittman, Depesh Mandalia, Media Buyer, Pixel Specialist, Fiscal, Creative Analyst, Hormozi Ads, Donald Miller, Maquiavel (conferência), Social media e Copy.

> **Sem promessa de resultado e sem número inventado.** Nenhum CPL, CPA ou ROAS esperado aparece aqui. Os gatilhos da seção 8 são **regras de decisão** (fórmulas a preencher com o dado real da conta), não previsão. **Verba: definir com o Lindson.**

---

## 0. O que trava (precisa do Lindson)

| Item | Situação | O que falta |
|---|---|---|
| Conta de anúncios Meta (no portfólio do Al Kántara Group ou no do Lindson) | **travado: precisa do Lindson** | Dizer qual portfólio usar; forma de pagamento é só ele que cadastra. |
| Página do Facebook + Instagram @barzakhstudio | **travado: precisa do Lindson** | Criar as contas (usuário conferido na hora, ordem de `../CANAIS.md`) e ligar ao portfólio. Sem isso não existe anúncio "Barzakh". |
| WhatsApp Business do estúdio | **travado: precisa do Lindson** | Confirmar o número (hoje wa.me/5598985621808) e ligá-lo à Página; quem responde em até 5 min. |
| Pixel (conjunto de dados) + API de Conversões | **travado: precisa do Lindson** | A extensão cria o Pixel e mostra o ID; a instalação na página e o token da CAPI ficam com a equipe, com o token guardado como segredo (nunca no GitHub). |
| Página de destino com nome Barzakh | **travado: precisa do Lindson** | Hoje a página de venda é https://lindsonalmeida.pages.dev/site/identidade/ (nome Lindson Almeida Studio, v2). Antes de anunciar: trocar a assinatura para Barzakh (`gerador/conteudo.py` → `STUDIO`/`HANDLE`) e decidir se ganha domínio próprio. |
| Conta Google Ads + Perfil da Empresa no Google | **travado: precisa do Lindson** | Criar/indicar a conta, cadastrar pagamento, conferir o Perfil da Empresa "Barzakh" (endereço ou área de atendimento). |
| Valor médio dos pacotes e taxa de fechamento | **travado: precisa do Lindson** | Só ele sabe (esteira interna no privado). Sem isso não se calcula o custo máximo por conversa (seção 8). |
| Verba diária/mensal | **travado: precisa do Lindson** | "Verba: definir com o Lindson." A estrutura abaixo é em %. |
| Autorização de uso dos cases em anúncio | **travado: precisa do Lindson** | Real Time e WF Celulares são clientes: confirmar que autorizam aparecer em anúncio pago (no orgânico já aparecem no Behance). |

---

## 1. Objetivo

**Gerar conversas no WhatsApp com donos de negócio de São Luís e do interior do Maranhão que querem uma identidade visual**, e levar essas conversas a briefing e proposta (o valor só na proposta, nunca no anúncio).

Métrica que manda: **conversa qualificada** = a pessoa respondeu às 3 perguntas da resposta "quanto custa?" de `../CANAIS.md` (o que vende, onde a marca vai aparecer, para quando precisa). Conversa que só diz "oi" não conta como resultado bom, mesmo que barata.

Funil:
1. **Frio** (Meta e Google): vê um case aplicado ou pesquisa "identidade visual são luís" → chama no WhatsApp ou abre a página.
2. **Morno** (remarketing): viu a página, assistiu ao vídeo de um case, interagiu com o @barzakhstudio → vê processo, etapas e prazo → chama.
3. **Fundo** (WhatsApp, fora do anúncio): resposta em até 5 min → 3 perguntas → briefing (`site/identidade/briefing.html`) → proposta PDF (`../../oferta/`) → fechamento.

Teste da persona (dono de clínica, loja, restaurante, 28 a 50 anos, decide no celular à noite): **compraria?** Sim, se o anúncio mostra o case pronto e aplicado, fala simples e leva direto ao WhatsApp com o designer. Não, se soar esotérico ("portal", "energia") ou prometer venda.

---

## 2. Regras atuais das plataformas que moldam a estrutura (pesquisa 16/11/2026)

1. **Meta Andromeda = sistema de recuperação de anúncios.** A Meta descreve o Andromeda como o motor de *retrieval* que reduz dezenas de milhões de anúncios candidatos a alguns milhares para o leilão; na implantação, informou +6% de *recall* e, para quem passou a usar os recursos de IA do Advantage+ criativo, +22% de ROAS (dado da Meta sobre anunciantes dela, **não** previsão para a Barzakh). Fonte: [Meta Engineering, dez/2024](https://engineering.fb.com/2024/12/02/production-engineering/meta-andromeda-advantage-automation-next-gen-personalized-ads-retrieval-engine/).
2. **O criativo virou a segmentação.** Com público amplo, é o anúncio que "escolhe" quem vê. Diversidade = conceitos realmente diferentes (dor, persona, formato, gatilho), não 5 versões da mesma arte: variações da mesma ideia contam como um bilhete só no leilão. Fontes: [Jon Loomer · Meta Andromeda](https://www.jonloomer.com/meta-andromeda/), [Influencer Marketing Hub](https://influencermarketinghub.com/meta-andromeda-update-explained-how-meta-ads-work-now/), [Design Pickle, dez/2025](https://designpickle.com/produce-meta-ad-creative-advantage-plus-era), [dentsu](https://www.dentsu.com/ae/en/our-latest-thinking/meta-andromeda-strategy). Cuidado: [Jon Loomer, dez/2025](https://pubcast.jonloomer.com/stop-blaming-andromeda-for-your-results/) lembra que muito problema atribuído ao Andromeda é estrutura ou criativo ruim.
3. **Estrutura simples:** 1 campanha por objetivo, 1 conjunto amplo (Advantage+ público, interesses só como sugestão), muitos conceitos, mudanças em lote para não reiniciar o aprendizado. Já é a regra da equipe (`.claude/agents/pedro.md`, Andromeda).
4. **Anúncio de clique para o WhatsApp** pode rodar em Engajamento, Leads, Vendas ou Tráfego; o padrão para negócio local que fecha na conversa é otimizar por **conversas**. A **API de Conversões para mensagens** (Business Messaging) permite devolver à Meta eventos de dentro da conversa (lead qualificado, venda) e otimizar mais fundo no funil, mas exige WhatsApp Business **API** (o app comum não manda o `ctwa_clid`). Fontes: [WhatsApp Business · Conversions API](https://whatsappbusiness.com/blog/conversions-api-messaging/), [Twilio, guia 2026](https://www.twilio.com/en-us/blog/products/2026-guide-to-create-ads-that-click-to-whatsapp-with-twilio), [CustomerLabs](https://www.customerlabs.com/blog/why-meta-algorithm-chases-chatters-not-buyers-for-ctwa-ads) (a Meta "persegue quem conversa, não quem compra" se só receber o sinal de conversa). Na fase 1 usamos o app + código na mensagem; API fica para a fase 2 (travado: precisa do Lindson).
5. **Atributos pessoais (Padrões de Publicidade da Meta):** o anúncio não pode afirmar nem insinuar que sabe uma característica de quem vê (raça, religião, idade, saúde, **situação financeira**, orientação, nome etc.). "Seu negócio está quebrado?" ou "Está sem dinheiro pra marca?" reprova. Descrever a oferta ou falar de um grupo em 3ª pessoa passa. Ser dono de negócio não é atributo protegido. Fontes: [Stackmatix · personal attributes](https://www.stackmatix.com/blog/meta-ads-personal-attributes-policy), [Audit Socials 2026](https://www.auditsocials.com/blog/meta-ad-misleading-claims-personal-attributes-prohibited-content-policy-2026). [Conferir] o texto atual no Central de Transparência da Meta antes de publicar.
6. **Antes e depois:** a restrição forte da Meta é para saúde, estética e emagrecimento ([Audit Socials 2026](https://www.auditsocials.com/blog/meta-beauty-cosmetics-ads-2026-before-after-photos-appearance-claims-policy), [LeadEnforce](https://leadenforce.com/blog/why-using-before-and-after-images-can-break-facebook-ads-guidelines)). Antes × depois de **logo** não é tema de saúde, mas a regra de "resultado improvável/enganoso" vale: nada de "antes: 0 clientes, depois: fila na porta". Regra nossa: antes × depois só da **marca** (logo velho × logo novo), só com o "antes" real e autorizado pelo cliente, e sem nenhum número de resultado. Sem o "antes" autorizado, mostrar só a marca aplicada.
7. **Política e temas sociais:** no Brasil, anúncio "feito por ou sobre" candidato, figura pública ou partido exige autorização e o rótulo "Pago por", e fica 7 anos na Biblioteca de Anúncios. Fonte: [Meta · Anúncios sobre temas sociais, eleições ou política](https://transparency.meta.com/pt-br/policies/ad-standards/SIEP-advertising/SIEP/). **Por isso o case Leo Pinto fica FORA do tráfego pago** (risco de reprovação, de a conta virar "anunciante político" e de expor o vereador, que é situação). Leo segue só no orgânico (Behance, Pinterest).
8. **Google Ads local:** começar por **Pesquisa** (mais controle sobre intenção e local) com lances inteligentes quando houver conversão medida; o AI Max para Pesquisa amplia termos por correspondência ampla, ativos e página de destino, e é recomendado junto com Smart Bidding, mas deve ser **validado**, não ligado às cegas. Não misturar mercados distintos numa campanha só. Fontes: [Google Ads Help · AI Max](https://support.google.com/google-ads/answer/15910187), [Google · reaching the right customers on search](https://business.google.com/us/accelerate/resources/articles/reaching-the-right-customers-on-search/), [Location3 · AI Max](https://location3.com/blog/ai-max-franchise-conversion-growth/), [dev.to · AI Max local 2026](https://dev.to/yositeup/ai-max-for-local-businesses-location-based-campaign-configuration-in-2026-97i).
9. **Pinterest Ads:** o Brasil aparece na lista de países com conta de anúncios direta ([Pinterest Help](https://help.pinterest.com/en/business/article/promoted-pins-overview)); [Conferir] a lista ao vivo ao criar a conta.

---

## 3. Divisão da verba (estrutura em %; **verba: definir com o Lindson**)

| Fase | Meta | Google | Pinterest |
|---|---|---|---|
| Dias 1 a 14 | 70% | 30% | 0% |
| Dias 15 a 30 | conforme o custo por **conversa qualificada** de cada canal (seção 8): o canal com menor custo por conversa qualificada ganha até +10 pontos do outro, em lote, no dia 15 | idem | 0% até haver pin com tração (seção 6) |

Dentro da **Meta**:

| Campanha | Antes do Pixel/CAPI | Depois do Pixel/CAPI instalados e testados |
|---|---|---|
| M1 · Mensagens WhatsApp (frio) | 100% (85% quando o M3 ligar) | 65% |
| M2 · Página de identidade (pixel/CAPI) | 0% (criada desligada) | 20% |
| M3 · Remarketing | 0% até o público quente existir; depois 15% **tirados** do M1 | 15% |

Dentro do **Google**: G1 São Luís 75% · G2 Interior do MA 25% (se o G2 não gastar por falta de busca, a verba volta ao G1; não forçar).

Regra do Fiscal: a soma nunca passa da verba aprovada; subir verba só com o Lindson (seção 8).

---

## 4. Meta: estrutura de campanhas

Nomenclatura: `BZ · <canal> · <objetivo> · <público>`; anúncio = código do criativo (`BZ-E1` a `BZ-E6`, `BZ-V1` a `BZ-V6`, de `CRIATIVOS.md`).

### M1 · `BZ · Meta · Mensagens WhatsApp · MA Amplo`
- **Objetivo:** Engajamento › Mensagens › WhatsApp · meta "maximizar conversas" · orçamento na campanha (Advantage+ orçamento / CBO).
- **1 conjunto** `MA Prioritário · 25-55 · Advantage+`:
  - **Local** ("pessoas que moram ou estiveram recentemente"): Grande São Luís (São Luís, São José de Ribamar, Paço do Lumiar, Raposa) + polos do interior: Imperatriz, Caxias, Timon, Bacabal, Santa Inês, Codó, Balsas, Açailândia, Pinheiro, Chapadinha, Barreirinhas, Zé Doca, São João Batista. (Atendimento é online; o interior entra porque a persona inclui o interior.)
  - **Idade:** 25 a 55 (persona 28-50, com folga para o algoritmo).
  - **Público Advantage+ ligado**, com **sugestões** (não restrições): administradores de página de empresa, pequenas empresas, proprietários de pequenas empresas, empreendedorismo, marketing para pequenas empresas, design gráfico, branding [Conferir quais opções ainda existem no Gerenciador: a Meta vem consolidando a segmentação detalhada].
  - **Excluir:** quem mandou mensagem nos últimos 30 dias (público P3), para não pagar conversa de quem já está no WhatsApp.
  - Posicionamentos Advantage+ (no dia 7 conferir se Audience Network/Messenger comem verba com conversa ruim; se sim, ficar só Instagram e Facebook: Feed, Reels, Stories).
- **Anúncios:** 6 a 8 conceitos diferentes no dia 1 (ver `CRIATIVOS.md`, seção "Lote 1"); o resto entra no dia 14.
- **Mensagem pronta** com código: `Oi! Vim pelo anúncio (BZ-V1). Quero saber da identidade visual da minha marca.` (trocar o código em cada anúncio).

### M2 · `BZ · Meta · Página Identidade · MA Amplo` (criada **desligada**; liga quando o Pixel + CAPI estiverem testados)
- **Objetivo:** Leads (ou Vendas, se a conta pedir) otimizando o evento **Contact** (clique no botão de WhatsApp da página) e, quando houver volume, **Lead** (briefing enviado). Se em 7 dias o evento escolhido tiver pouco volume para sair do aprendizado (a Meta pede ~50 eventos por semana por conjunto), otimizar temporariamente por **ViewContent** (abriu um case), sem criar outro conjunto.
- Mesmo conjunto do M1 (local, idade, Advantage+).
- Destino: `https://lindsonalmeida.pages.dev/site/identidade/` (ou o domínio Barzakh, se o Lindson criar) com UTM da seção 9.
- **Por que existe:** parte da persona quer "ver mais antes de chamar"; a página mostra cases e processo e alimenta o remarketing.
- **Pixel + CAPI (Pixel Specialist):** navegador e servidor juntos, com deduplicação por `event_id`. Eventos: `PageView`; `ViewContent` (abriu um case ou rolou até os cases); `Contact` (clique no WhatsApp); `Lead` (envio do briefing). A CAPI pode rodar numa Function da própria Cloudflare Pages (a Central já usa Functions); o token fica em segredo da Cloudflare, nunca no repositório. **Travado: precisa do Lindson** (ID do Pixel e token).

### M3 · `BZ · Meta · Remarketing · Quente 90d` (criada **desligada**)
- **Objetivo:** Mensagens WhatsApp (mesma meta do M1).
- **Público (soma):** P1 Engajou IG/FB 90d + P2 Viu 50% de vídeo 90d + P4 Visitou a página 30d (pixel) + P5 Abriu um case 30d (pixel, `ViewContent`). **Excluir** P3 (mandou mensagem 30d).
- **Liga quando:** o público somado passar de ~1.000 pessoas (regra da equipe, RT v2) e no mínimo no dia 10. Verba tirada do M1, não somada.
- **Anúncios de morno:** processo, etapas e prazo, bastidor, carrossel de cases (ver `CRIATIVOS.md`, coluna "Funil").

### Públicos (criados todos no dia 0, mesmo pequenos)
| Código | Público | Origem |
|---|---|---|
| P1 | `BZ · Engajou IG+FB 90d` | Instagram @barzakhstudio + Página |
| P2 | `BZ · Viu 50% vídeo 90d` | vídeos da Página/IG |
| P3 | `BZ · Mensagem 30d` | quem enviou mensagem (exclusão) |
| P4 | `BZ · Visitou página 30d` | Pixel |
| P5 | `BZ · Abriu case 30d` | Pixel, `ViewContent` |
| P6 | `BZ · Clientes` (lista) | CSV de quem fechou (nome, telefone, e-mail, com consentimento). **Só quando houver base**: a Meta exige no mínimo 100 pessoas de um país para gerar semelhante. Hoje: não criar. |
| P7 | `BZ · Semelhante 1% Clientes` | a partir do P6, Brasil, **mas usado só como sugestão** no Advantage+ e restrito ao Maranhão pelo local do conjunto. Só quando houver P6. |

---

## 5. Google Ads: Pesquisa local

Duas campanhas (mercados distintos não se misturam), mesmos grupos de anúncios em cada uma.

- **G1 · `BZ · Google · Pesquisa · São Luís`**: local = São Luís, São José de Ribamar, Paço do Lumiar, Raposa; opção de local **"Presença: pessoas que estão ou estão regularmente nos locais"** (não "interesse").
- **G2 · `BZ · Google · Pesquisa · Interior MA`**: Imperatriz, Caxias, Timon, Bacabal, Santa Inês, Codó, Balsas, Açailândia, Pinheiro, Chapadinha.
- **Redes:** só Rede de Pesquisa (desligar Rede de Display e parceiros de pesquisa no início).
- **Lances:** com conversão medida (clique no WhatsApp da página e briefing enviado, via Google Tag/GTM) → **Maximizar conversões** desde o início. Se a conversão ainda não estiver medida (travado), começar com **Maximizar cliques com limite de CPC máximo** definido pelo Lindson e trocar para Maximizar conversões assim que a conversão registrar. tCPA só depois, com o custo real (seção 8).
- **AI Max:** desligado nos 30 dias de teste; avaliar no dia 30 com teste A/B (experimento) se houver conversões.
- **Correspondência:** frase e exata nos 30 dias. Ampla só com lances inteligentes e conversões medidas, depois do dia 30.
- **Ativos:** sitelinks (Cases · Processo · Pacotes · Briefing), frase de destaque (Processo em 6 etapas · Marca em mockup · Fale com o designer · Prazo por escrito), ativo de **ligação/WhatsApp** (número do estúdio), ativo de **local** (Perfil da Empresa, quando existir), imagens dos mockups (dos cases autorizados).
- **Horário:** todos os dias; ver no dia 14 se a madrugada gasta sem conversão (a persona decide à noite: não cortar a noite).

### Grupos de anúncios e palavras-chave
| Grupo | Palavras-chave (frase "..." e exata [...]) |
|---|---|
| **GA1 Identidade visual** | "identidade visual são luís", [identidade visual são luís], "identidade visual para empresa", "criar identidade visual", "identidade visual profissional", "empresa de identidade visual", "identidade visual maranhão", "fazer identidade visual" |
| **GA2 Logo** | "criar logo profissional", "logo profissional", "criar logomarca", "fazer logomarca", "logomarca para empresa", "designer de logo", "criação de logotipo", "logo para empresa são luís" |
| **GA3 Designer/estúdio** | "designer em são luís", [designer em são luís], "designer gráfico são luís", "estúdio de design são luís", "agência de branding são luís", "designer maranhão", "designer de marcas" |
| **GA4 Branding e brand book** | "branding para empresa", "branding são luís", "manual de marca", "brand book", "guia de marca", "manual de identidade visual" |
| **GA5 Rebranding** | "rebranding", "mudar logo da empresa", "renovar marca da empresa", "redesign de logo", "atualizar identidade visual" |
| **GA6 Marca do estúdio** (verba mínima, proteção) | [barzakh], [barzakh studio], [barzakh design] |

No G2, trocar "são luís" pelo nome da cidade em GA1/GA3 ("identidade visual imperatriz", "designer em imperatriz" etc.) e manter os termos sem cidade.

### Palavras negativas (lista compartilhada `BZ · Negativas`, nível de conta)
- **Grátis e faça você mesmo:** grátis, gratuito, gratis, free, de graça, online grátis, gerador, gerar logo, app, aplicativo, canva, inteligência artificial, ia, chatgpt, modelo pronto, template, png, vetor grátis, download, baixar, editável, psd, mockup grátis.
- **Estudo e emprego:** curso, aula, apostila, pdf, tcc, faculdade, apresentação escolar, o que é, significado, conceito, exemplos, história, vaga, vagas, emprego, estágio, salário, contratando, freelancer vaga, quanto ganha, como ser designer.
- **Fora do serviço:** tatuagem, tattoo, escudo de time, time de futebol, camisa, camiseta, adesivo, convite, papel de parede, wallpaper, fonte, fontes, cartão de visita grátis, gráfica, impressão, plotagem, fachada (avaliar: pode ser bom; começa negativa e revisa no dia 14), uniforme.
- **Concorrência de plataforma:** fiverr, 99designs, 99freelas, workana, logaster, looka, hatchful, wix.
- **O nome em sentido religioso:** alcorão, corão, islã, islam, morte, além, significado barzakh, o que é barzakh.
- Revisar o relatório de **termos de pesquisa** nos dias 4, 7, 14, 21 e 28 e negativar o que não é intenção de contratar.

### Anúncio responsivo de pesquisa (RSA), mesmo para todos os grupos (trocar o título 1 pelo termo do grupo)
**Títulos (até 30 caracteres, conferidos):**
1. Identidade Visual em São Luís (29) · fixar na posição 1 no GA1
2. Logo Profissional e Branding (28)
3. Barzakh · Estúdio de Marca (26)
4. Marca Aplicada em Mockup (24)
5. Processo em 6 Etapas (20)
6. Fale com o Designer (19)
7. Orçamento pelo WhatsApp (23)
8. Brand Book e Guia de Marca (26)
9. Prazo Combinado por Escrito (27)
10. Designer em São Luís, MA (24)
11. Cases Reais Aplicados (21)
12. Do Logo ao Instagram (20)
13. Atendemos Todo o Maranhão (25)
14. Rebranding de Empresas (22)
15. A Passagem da Sua Marca (23)

**Descrições (até 90 caracteres, conferidas):**
1. Identidade visual completa: logo, cores, letras e a marca aplicada no Instagram e papel. (88)
2. Você vê a marca aplicada em mockup antes do arquivo final. Fale direto com o designer. (86)
3. Estúdio de São Luís com processo em 6 etapas e prazo combinado no início. Peça orçamento. (89)
4. Do briefing ao brand book: referências do mundo inteiro e a marca pronta para usar. (83)

Sem preço, sem "o melhor", sem "garantido", sem número de resultado.

---

## 6. Pinterest Ads (opcional, fase 2)

- **Quando ligar:** só depois de 30 dias de pins orgânicos (`../textos_pins.json`, 1 pin/dia útil) e **só para os pins com tração**: pins cujos salvamentos **e** cliques de saída nos últimos 30 dias estão acima da **mediana dos pins da própria conta** (dado do Pinterest Analytics; sem número fixo inventado).
- **Campanha:** `BZ · Pinterest · Consideração · Pins vencedores` · objetivo Consideração (cliques para o site) · destino a página de identidade com UTM · público: Brasil (o Pinterest é buscador e o atendimento é online), palavras-chave das 6 pastas SEO de `../CANAIS.md` (identidade visual para pequenas empresas, mockup de cartão de visita, branding para Instagram, embalagem, pôster de marca, identidade visual para restaurante) + **Pinterest Tag** na página (evento `pagevisit` e `lead`). Retargeting de quem interagiu com pins.
- **Verba:** sai da parte do canal que perder no dia 30; nunca somada sem o Lindson. **Travado: precisa do Lindson** (conta de anúncios Pinterest e pagamento).

---

## 7. Calendário de testes (30 dias)

| Dia | Meta | Google | Quem decide |
|---|---|---|---|
| **0** | Extensão monta tudo **pausado** (`PROMPT-EXTENSAO-META.md`). Conferir textos contra a seção 2 (atributos pessoais, antes/depois, Leo fora). Criar públicos P1-P5. | Montar G1 e G2 pausadas, lista de negativas, conversões (Google Tag). | Lindson aprova verba e liga. |
| **1** | Liga M1 com o **Lote 1** (6 a 8 conceitos). | Liga G1 e G2. | Lindson |
| **1-3** | Só ler. Mexer só em anúncio reprovado ou com 0 entrega. Responder conversa em até 5 min. | Só ler. | equipe |
| **4** | Conferir entrega por anúncio (a Meta concentra verba em poucos: normal). | 1ª leitura dos termos de pesquisa → negativas. | equipe |
| **7** | **1º corte** (seção 8). Conferir posicionamentos. Anotar padrões vencedores (ângulo × formato). | Termos de pesquisa + negativas; pausar palavra-chave com gasto ≥ 2× o custo máximo por clique de conversa e 0 conversão. | equipe; verba só Lindson |
| **10** | Se P1+P2+P4+P5 > ~1.000 pessoas: ligar M3 (15% tirados do M1). Se Pixel+CAPI testados: ligar M2. | — | Lindson liga |
| **14** | **Lote 2** (4 a 6 conceitos novos, de uma vez, inspirados nos vencedores; ver `CRIATIVOS.md`). Fixar o custo-alvo com o dado real. Rebalancear Meta × Google (seção 3). | Revisar horário, local (G2 gasta?), negativas, "fachada". | Lindson aprova rebalanceamento |
| **15-21** | **Teste 2:** M1 (WhatsApp direto) × M2 (página) → comparar custo por **conversa qualificada**, não por conversa. | Se houver conversões suficientes para o aviso de "lances aprendendo" sumir, avaliar tCPA no custo real. | equipe |
| **21** | 2º corte; trocar os 2 piores por reservas. Decidir Pinterest (seção 6). | Termos + negativas. | equipe / Lindson (Pinterest) |
| **28-30** | Relatório: gasto, conversas, conversas qualificadas, briefings, propostas, fechamentos por código BZ-*, por canal e por criativo. Proposta de escala (ou de parar) ao Lindson. | Mesmo relatório + decisão AI Max (experimento). | Lindson |

Sempre: **desligar, nunca excluir**; mudanças em lote; nunca mais da metade dos anúncios desligados no mesmo dia; nunca mexer em conjunto antes do dia 7.

---

## 8. Regras de otimização (fórmulas; números só com o dado real)

### Valores que o Lindson informa (travado: precisa do Lindson)
- **VMP** = valor médio do pacote fechado (média ponderada de Limiar, Travessia e Horizonte pelo que realmente vende).
- **% de aquisição** = quanto do VMP ele aceita gastar em anúncio para fechar 1 cliente.
- **Taxas do funil** (medidas na planilha a partir do dia 7): `t1` = conversa → conversa qualificada; `t2` = qualificada → proposta enviada; `t3` = proposta → fechou.

### Custos máximos
- **CAC máximo** = VMP × % de aquisição.
- **Custo máximo por conversa qualificada** = CAC máximo × t2 × t3.
- **Custo máximo por conversa** (o que a Meta mostra) = custo máximo por conversa qualificada × t1.
- **Custo máximo por clique (Google)** = custo máximo por conversa × taxa clique → conversa da página/WhatsApp (medida).
- Até ter `t1`, `t2`, `t3` reais (dia 14), usar o **custo médio por conversa da própria conta** como régua.

### Pausar (por anúncio, depois do dia 7)
- Gastou **≥ 2× o custo máximo por conversa** (ou 2× a média da conta, antes do dia 14) **sem gerar conversa** → desligar.
- **Taxa de gancho** = visualizações de 3 s ÷ impressões. Abaixo da **metade da média dos vídeos da conta**, com ≥ 1.000 impressões → desligar ou trocar o gancho. (Regra da equipe na RT v2: < 20%.)
- **Taxa de retenção** = ThruPlays ÷ visualizações de 3 s. Gancho bom e retenção baixa → o meio do vídeo está fraco: refazer o meio, manter o gancho.
- **CTR de link/mensagem** abaixo da metade da média da conta com ≥ 1.000 impressões → criativo fraco. (Regra da equipe na RT v2: < 0,8%.)
- Conversas **baratas mas não qualificadas** (t1 baixo) por 7 dias → problema de público ou de mensagem, não de verba: trocar o ângulo e a mensagem pronta, não aumentar verba.
- **Frequência > 2,5** em 7 dias no frio (regra da equipe) com CTR caindo → entrar conceito novo; se persistir, ampliar local.

### Escalar (só o Lindson aprova)
- Custo por conversa qualificada ≤ custo máximo por **7 dias seguidos**, **e** pelo menos uma proposta saindo dessas conversas → pedir ao Lindson **+20% de verba**, no máximo a cada 3-4 dias, sempre na campanha (nunca duplicar conjunto).
- **Vencedor** (custo por conversa qualificada abaixo da média) → 2 a 3 conceitos novos no mesmo ângulo e formato diferente no próximo lote (graduação, Depesh Mandalia).
- Google: palavra-chave com custo por conversão ≤ custo máximo por 14 dias → subir verba da campanha (nunca lance manual por palavra).

### Qualidade do atendimento (o que mais mata a campanha)
- Resposta em até 5 min no horário comercial e à noite (a persona decide à noite).
- Toda conversa recebe a resposta "quanto custa?" de `../CANAIS.md` e o link do briefing.

---

## 9. UTMs e códigos

### Meta (Parâmetros de URL no anúncio que leva à página)
```
utm_source=meta&utm_medium=paid_social&utm_campaign={{campaign.name}}&utm_term={{adset.name}}&utm_content={{ad.name}}&utm_id={{campaign.id}}
```
### Google (modelo de acompanhamento na conta; marcação automática gclid ligada)
```
{lpurl}?utm_source=google&utm_medium=cpc&utm_campaign={campaignid}&utm_term={keyword}&utm_content={creative}&matchtype={matchtype}
```
### Pinterest (fase 2; parâmetros fixos por campanha)
```
?utm_source=pinterest&utm_medium=paid_social&utm_campaign=bz-pinterest-consideracao&utm_content=<codigo-do-pin>
```
### Orgânico (bio e Behance, para separar do pago)
`utm_source=instagram&utm_medium=bio` · `utm_source=behance&utm_medium=perfil` · `utm_source=linkedin&utm_medium=pagina`.

### WhatsApp (o rastreio que funciona sem API)
- Mensagem pronta de cada anúncio leva o código: `Oi! Vim pelo anúncio (BZ-V3). Quero saber da identidade visual da minha marca.`
- Botão da página leva o código da origem: `wa.me/5598985621808?text=Oi!%20Vim%20pela%20página%20(BZ-PG-<utm_content>)...`
- Google: `BZ-GA1` a `BZ-GA6` no texto do botão de WhatsApp da página quando `utm_source=google`.
- **Planilha (ou aba na Central):** data · código · nome · nicho · cidade · qualificada (s/n) · briefing (s/n) · proposta (s/n) · pacote · fechou (s/n) · valor. É dela que saem `t1`, `t2`, `t3`.

---

## 10. Regras de conteúdo do anúncio (conferência do Maquiavel)
- Persona: dono de negócio local, linguagem de WhatsApp, Conexão → Dor → Desejo → Pergunta.
- Sem preço, sem promessa de resultado, sem "o melhor de São Luís", sem palavra proibida de `../marca/ESTRATEGIA.md` (energia, alma, portal, despertar, garantido, explodir, faturar mais).
- Sem insinuar atributo pessoal do leitor (seção 2, item 5); sem número de resultado em antes × depois.
- Leo Pinto fora do pago. Dra. Jaci fora (CFO). Real Time e WF só com autorização.
- Vídeo sempre com narração fluida (voz clonada aprovada do Lindson, "voz 6"; Antonio reprovado para a marca dele), SFX e VFX.
- Cada foto/mockup usado em anúncio entra na aba Usadas (`FOTOS-USADAS.md` do projeto) e não se repete entre criativos.
