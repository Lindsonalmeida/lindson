# Software e IA (SaaS, micro-SaaS, apps, automações, agentes, extensões, APIs)

**Situação:** completo (rodada 1, 02/11/2026, conta Zuleide). Aprofunda `modelos.md` §2.8 e §2.10 (conta Pedro), que já traz o caso Pieter Levels.

Legenda: "oficial" = página da empresa; "blog" = terceiro; **[Interpretação]** = opinião do agente.

---

## 1. Os modelos

| Modelo | O que vende | Investimento | Primeira venda | Risco | Escala | Encaixe Lindson |
|---|---|---|---|---|---|---|
| **SaaS** (software por assinatura) | Ferramenta online para muitos clientes | Médio a alto | Meses | Construir o que ninguém usa; suporte | Muito alta | Médio |
| **Micro-SaaS** | Ferramenta pequena para um nicho, feita por 1 a 3 pessoas | Baixo a médio (menor com IA) | Semanas a meses | Nicho pequeno demais | Média a alta | **Alto** (apps que ele já tem) |
| **App mobile** (App Store, Google Play) | App pago ou com assinatura | Médio | Meses | Comissão da loja; descoberta difícil | Alta | Baixo |
| **Agência de automação / IA** | Monta chatbots, integrações (n8n, Make, Zapier), agentes | Baixo | Semanas | Vira commodity rápido | Média | **Alto** |
| **Agentes de IA para PMEs** | "Funcionário de IA": atendente no WhatsApp, SDR, agendamento | Baixo a médio | Semanas | Erros da IA com cliente final; custo por mensagem | Média a alta | **Alto** |
| **Extensão de navegador / plugin** | Extensão do Chrome, plugin de WordPress, app da Shopify | Baixo | Meses | Dependência da loja de extensões | Média | Baixo |
| **API paga** | Dado ou função cobrada por uso | Médio | Meses | Concorrência de grandes | Alta | Baixo |
| **Template de automação / GPT / prompt** | Pacote pronto para outros usarem | Muito baixo | Dias | Copiável | Baixa | Médio (bônus de curso) |
| **"Service as software"** | O serviço da agência entregue em parte por software, cobrado como assinatura | Médio | Semanas | — | Alta | **Alto** |

---

## 2. Custos e comissões das lojas e infraestrutura

| Item | Número | Fonte e data |
|---|---|---|
| **Apple App Store** | Comissão de **15%** para quem fatura até US$ 1 milhão/ano (Small Business Program, desde 01/01/2021); padrão 30% | Apple Newsroom, 18/11/2020 |
| **Google Play** | Faixa de 15% para o primeiro US$ 1 milhão (amplamente noticiada) | **Não conferido nesta rodada** |
| **Stripe Billing** (cobrança recorrente) | **0,7%** do volume, além da taxa do cartão (3,99% + R$ 0,39 nacional; +2% internacional) | **Oficial**, stripe.com/br/pricing, 02/11/2026 |
| **WhatsApp Business Platform (API)** | Cobrança **por mensagem** desde **01/07/2025** (antes era por conversa). Mensagem de atendimento (dentro da janela de resposta) grátis; marketing e utilidade pagas. Brasil: marketing ~US$ 0,0625 ou ~R$ 0,38–0,39; utilidade ~US$ 0,0068 ou R$ 0,04–0,08 (números de terceiros, divergentes). A Meta publicaria preços em reais até 01/06/2026 | **Oficial** para a mudança (developers.facebook.com, documentação de preços); valores: blogs (Hyperleap, Message Central, 2026) |

**Por que o custo do WhatsApp importa:** um "agente de IA no WhatsApp" para cliente da Alkantara tem custo variável por mensagem de marketing. **[Interpretação]** Responder quem chama (atendimento) é grátis; disparo de oferta é pago. O app de SDR do Lindson usa `wa.me` (conversa aberta à mão, sem API): não paga por mensagem, mas também não automatiza o envio. Isso é bom para não ser bloqueado (`golpes-e-riscos.md`).

---

## 3. Casos (com o tamanho da dúvida)
- **Brasil, micro-SaaS:** a newsletter *Micro-SaaS* (Bruno Okamoto, Substack) registra o **Clonou** (Jonatan Fróes) indo de **R$ 20 mil para R$ 198 mil de MRR em 5 meses** (maio a outubro de 2023), uma ferramenta de resumos de grupos de WhatsApp com IA a ~R$ 3 mil de MRR e um micro-SaaS de IA + WhatsApp crescendo 30% ao mês. **Números informados pelos fundadores, sem auditoria.**
- **Agregador (não conferido):** ferramenta brasileira de IA para advogados com mais de R$ 70 mil de MRR (lilys.ai, 2025).
- **Mercado:** a Wonderful (plataforma de agentes de IA) diz mirar **US$ 1 bilhão de receita no Brasil até 2028** (Baguete); o Banco Inter testa a IA "Seven" no WhatsApp com 18 mil clientes fazendo Pix e 40 mil operações de jan. a mai./2026 (citado em busca; não conferido).
- **Fora:** Pieter Levels (Photo AI etc.) em `modelos.md` §2.8.
- **[Interpretação]** O padrão dos casos que dão certo: **um nicho que o fundador conhece + WhatsApp + cobrança mensal baixa + venda direta**.

---

## 4. O que o Lindson já tem e pode virar produto
Inventário no repositório (ver `ESTADO-DO-PROJETO.md`):
1. **App de SDR para agências** (funil com botão de WhatsApp, cadência automática) → micro-SaaS para social medias e pequenas agências. **Alto potencial.**
2. **Central do cliente** (login, painel por cliente, `agencia/sistema-clientes/`) → "portal do cliente" white label para outras agências.
3. **Gravador de demo de mini site** (`agencia/processos/demo-minisite/`) → ferramenta para vender sites.
4. **Motor Pintura Viva** (vídeo com gravuras e narração) → serviço de canal dark para clientes (o Peter já cita) ou ferramenta.
5. **Fábrica de Conteúdo / Recomeço 90** (roteiros, missões) → bônus do curso ou assinatura.

**Caminho sugerido (interpretação):**
1. Usar internamente até funcionar sem o Lindson mexer.
2. Oferecer a **3 agências parceiras** como serviço com software (mensalidade baixa, ele configura).
3. Só depois abrir cadastro sozinho (SaaS de verdade), com Stripe Billing ou Asaas/Mercado Pago para cobrar em reais.

---

## 5. Agência de automação e agentes de IA (o modelo mais rápido desta família)
- **O que vender a negócios locais (interpretação):** atendente de IA no WhatsApp que responde dúvidas e agenda; follow-up de orçamento; resumo semanal de leads; geração de conteúdo com revisão humana.
- **Preço:** implantação única + mensalidade (prática comum; sem fonte de preço médio confiável no Brasil).
- **Riscos:** a IA errar com o cliente final (preço errado, promessa indevida); **LGPD** (dados de clientes da empresa passam pela IA: precisa de base legal e contrato de operador; ver `riscos-legais-e-regras.md`); custo por mensagem da API; ferramentas de "agente pronto" baixando o preço.
- **Encaixe:** forte como **degrau novo da esteira** ("Atendimento que vende": WhatsApp com IA + Script de Fechamento), ligado ao componente "Script de Fechamento" que já existe na oferta Instagram que Vende. **[Interpretação]**

---

## 6. Riscos específicos
- **Construir antes de vender:** o erro número um em software. Venda 3 assinaturas antes de programar a versão 2. **[Interpretação]**
- **Dependência de API de terceiros** (OpenAI, Anthropic, Meta): preço e regras mudam.
- **Suporte:** cada cliente de software vira um chamado. Documentação e vídeos curtos reduzem.
- **Dados:** quem guarda dados de clientes de outras empresas vira operador na LGPD.

---

## Uso pelo agente
- **Lição 1:** o Lindson já escreveu software que outros pagariam. O ativo existe; falta empacotar.
- **Lição 2:** comece como serviço com software (white label para agências) antes de SaaS aberto.
- **Lição 3:** WhatsApp é a interface do Brasil. Ferramenta que vive no WhatsApp vende mais fácil aqui.
- **Lição 4:** cobrança recorrente automática (Stripe Billing 0,7%, Pix Automático) desde o primeiro cliente.
- Maquiavel: "chi non fa e' fondamenti prima, gli potrebbe con una grande virtù farli poi, ancora che si faccino con disagio dello architettore e periculo dello edifizio" (quem não faz os alicerces antes poderia, com grande virtude, fazê-los depois, mas com incômodo do arquiteto e perigo do edifício) (*Príncipe* VII). Em software, os alicerces são cobrança, dados e suporte: monte antes de crescer.

## Lacunas
- Tabela oficial da API do WhatsApp em reais (publicada pela Meta em 2026).
- Comissões atuais de Google Play, Chrome Web Store e Shopify App Store.
- Casos brasileiros auditados de micro-SaaS e de agências de IA.
- Preço médio de mercado de atendente de IA para PME no Brasil.
