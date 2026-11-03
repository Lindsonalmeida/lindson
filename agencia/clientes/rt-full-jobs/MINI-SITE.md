# Real Time · mini site da bio (rascunho, conta Zuleide, 03/11/2026)

Seguiu o processo `agencia/processos/mini-site-cliente.md` e o método dos mini sites aprovados: estrutura de bio do **Rafael Imports** (botões grandes de WhatsApp com mensagem pronta por assunto) e SEO local da **Desentupidora SF** (title, description, Open Graph, schema, robots e sitemap).

## Onde está
- **Rascunho do site:** `/home/user/realtime-site` (git local, branch `main`, ainda sem repositório no GitHub). O site **não** fica neste repositório `lindson`.
- **Cópia de segurança:** repositório privado `CentralLindsonALmeida/dados/clientes-arquivos/rt-full-jobs/mini-site/`. Prints do teste (390 e 1280 px): `.../rt-full-jobs/mini-site-prints/`.
- **Link previsto:** https://realtime.pages.dev (confirmar quando a Cloudflare criar o projeto; se o nome mudar, trocar `realtime.pages.dev` no `index.html`, `robots.txt` e `sitemap.xml`).

## O que tem
- **Marca nova v1** (conta Pedro, `identidade/v1/`): assinatura e símbolo em SVG de `marca/`, cores e fontes do manual (Geist, Geist Mono, Manrope; Preto Set, Branco Luz, Azul Real, vermelho só no REC). Composição do template **VideoLab** (Framer), o mesmo do manual: foto no visor com cantos, REC, HD/4K, timecode e títulos em 2 tons. A logo recortada do print **não** é mais usada.
- **Botões:** WhatsApp (98) 99133-1727 com mensagem pronta para Locar equipamento, Alugar o estúdio, Orçamento de produção e Conteúdo mensal, mais Instagram. Cada kit tem o próprio botão. As mensagens levam os códigos de rastreio da estratégia v2 (RT-CINEMA, RT-LUZ, RT-ESTUDIO, RT-MENSAL, RT-PROD). Barra fixa "Reservar no WhatsApp" no celular.
- **Seções:** Kits de locação (Cinema, Luz, Ópticas), Estúdio (chroma key, teleprompter, intercom), Realtime Conteúdo e Realtime Produções (5 etapas), Bastidores, lista de equipamentos do levantamento de 20/10 (com "modelo a confirmar" no STORM 1200 e no amaran 300c) e fechamento "Seu job é na Real Time."
- **Fotos:** recortes reais do Instagram (`identidade/v1/fotos/` e print 03) e fotos de produto de `fotos-equipamentos/` (Sony FX3 da Wikimedia Commons, CC BY 2.0, com crédito; Aputure STORM 80c, imagem do fabricante, com crédito). Fotos de fabricante só servem para divulgação: antes de anúncio pago, trocar pela foto do equipamento da RT.
- **SEO:** title e description "locação de equipamentos audiovisuais em São Luís", Open Graph com imagem 1200×630 (`img/og.jpg`), schema LocalBusiness **sem endereço** (área atendida: Maranhão).
- **Sem** preços, endereço, números de clientes ou anos de mercado.

## Falta do cliente
- [ ] **Cidade e endereço do estúdio.** O title usa "São Luís" a pedido; **confirmar** (a bio nova ainda diz só "Maranhão"). Quando chegar, preencher o objeto `ENDERECO` no fim do `index.html` (a seção "Onde fica" aparece sozinha) e pôr o endereço no schema.
- [ ] Horário de atendimento.
- [ ] Fotos do **próprio** equipamento e do estúdio (uma por mensagem), para trocar as fotos de fabricante.
- [ ] Confirmar os modelos: STORM 1200 (ou segundo 1200x), amaran 300c, versão da Tilta Mirage e do 24-70 GM.
- [ ] Preços que podem ser divulgados (se houver).
- [ ] Aprovação da marca nova v1 (o site usa a v1, que está aguardando aprovação).

## Situação (03/11, conta Leandro)
- Repositório `Lindsonalmeida/realtime` criado pelo Lindson (**público**; o processo pede privado: dá para trocar em Settings → Change visibility, a Cloudflare continua funcionando).
- Rascunho enviado para a branch `main` pela conta Leandro, sem mudanças. **Próximo: passo 4 (Cloudflare).**

## Passos do Lindson
1. Criar o repositório vazio e **privado** em github.com/new, na conta `Lindsonalmeida`, com o nome do cliente sem espaço nem acento (sugestão: `realtime`).
2. Liberar o app do Claude para esse repositório (All repositories).
3. Mandar no chat: "Repositório Lindsonalmeida/realtime criado, pode publicar." O Claude envia o rascunho de `/home/user/realtime-site` (ou da cópia no privado) para a branch `main`.
4. Cloudflare: Workers e Pages → Criar → Pages → Importar repositório → Project name `realtime` → branch `main` → framework `None` → build vazio → Save and Deploy. Se o nome já existir, usar `realtimeslz` ou `realtimefulljobs` e avisar para trocar os links.
5. Testar no celular (botões, mensagens, Instagram, fotos) e pôr o link na bio do Instagram (no lugar do `wa.me` da bio nova).
6. Depois de publicado, atualizar "Clientes ativos" em `agencia/processos/mini-site-cliente.md`.
