# Desentupidora SF no Google: passo a passo e textos prontos (conta Zuleide, 03/11/2026)

**Página com botão de copiar em cada endereço e texto:** https://claude.ai/artifact/CN1KaTtRGTpzCWrKk3AHi7 (fonte: `google-links.html` nesta pasta).

Segue o processo `agencia/processos/google-mini-site.md`. A parte do site (SEO local, sitemap, robots, dados estruturados `Plumber` com serviços, cidades e FAQ, verificação do Search Console) foi feita em 26/10. Falta a parte na conta Google do Lindson.

## Passo 1 · Search Console (5 minutos)
1. Abra **search.google.com/search-console** com a conta Google que verificou o site em 26/10 e escolha `https://desentupidorasf.pages.dev/`.
   - Se o site não aparecer na lista: Adicionar propriedade → Prefixo do URL → `https://desentupidorasf.pages.dev/` → Arquivo HTML. O arquivo `google7ec77465d11f840f.html` já está no ar: só clique em **Verificar**.
2. Menu **Sitemaps** → digite `sitemap.xml` → **Enviar**. Deve aparecer "Concluído" com 11 URLs.
3. Menu **Inspeção de URL** (barra no topo) → cole cada endereço abaixo → **Solicitar indexação** (o Google aceita cerca de 10 por dia; comece pelos 5 primeiros):
   - https://desentupidorasf.pages.dev/
   - https://desentupidorasf.pages.dev/desentupidora-sao-luis/
   - https://desentupidorasf.pages.dev/desentupimento-de-esgoto/
   - https://desentupidorasf.pages.dev/desentupimento-de-pia/
   - https://desentupidorasf.pages.dev/desentupimento-de-vaso-sanitario/
   - https://desentupidorasf.pages.dev/desentupimento-de-ralo/
   - https://desentupidorasf.pages.dev/limpeza-de-caixa-de-gordura/
   - https://desentupidorasf.pages.dev/desentupimento-de-calhas/
   - https://desentupidorasf.pages.dev/desentupidora-sao-jose-de-ribamar/
   - https://desentupidorasf.pages.dev/desentupidora-paco-do-lumiar/
   - https://desentupidorasf.pages.dev/desentupidora-raposa/
4. Mande ao Claude um print de **Páginas** e de **Desempenho** depois de 7 dias.

## Passo 2 · Perfil da Empresa no Google (Maps)
Abra **business.google.com** → Adicionar empresa. Textos prontos (só dados que estão no site; o que falta, pergunte ao cliente):
- **Nome:** Desentupidora SF
- **Categoria principal:** Serviço de desentupimento · **Categoria adicional:** Encanador
- **Tem local que os clientes visitam?** Não (atende na casa do cliente) → **Área de atendimento:** São Luís, São José de Ribamar, Paço do Lumiar, Raposa
- **Telefone e WhatsApp:** (98) 92010-5710 · **Site:** https://desentupidorasf.pages.dev
- **Serviços:** Desentupimento de pia · Desentupimento de ralo · Desentupimento de vaso sanitário · Desentupimento de esgoto · Limpeza de caixa de gordura · Desentupimento de calhas
- **Descrição (até 750 caracteres):**
  > Desentupidora em São Luís, São José de Ribamar, Paço do Lumiar e Raposa. Desentupimos pia, ralo, vaso sanitário, esgoto e calhas e fazemos a limpeza de caixa de gordura com equipamento de cabo rotativo, sem quebrar piso nem parede. O técnico testa o escoamento na hora, na sua frente. Orçamento grátis pelo WhatsApp (98) 92010-5710: mande uma foto do problema e a gente responde.
- **Falta perguntar ao cliente:** horário de atendimento (e se atende 24 horas e fim de semana), CNPJ ou nome do responsável para a verificação do Google (por vídeo ou ligação), fotos reais da equipe, do veículo e de serviços (antes e depois).
- **Fotos:** logo (`/home/user/GruposSF/img/logo.jpg`), capa com o flyer do cliente e fotos reais de serviço. Nada de foto de banco no perfil.
- **Depois de verificado:** pedir avaliação a cada cliente atendido (o CRM de chamados do painel já tem a mensagem na etapa "Serviço feito"; trocar o link pelo link de avaliação do perfil em `montar-sf.py`, campo `linkGoogle`).

## Passo 3 · Ligar tudo
- Link do site na bio do Instagram @desentupidorasf_slz e no Perfil da Empresa.
- Pendência antiga (01/11): Pixel da Meta e UTM no site antes de medir anúncios.

## Situação
| Passo | Situação |
|---|---|
| Site pronto para o Google | feito (26/10) |
| Search Console verificado | feito (26/10); confirmado em 03/11 pelo print do Lindson (propriedade `https://desentupidorasf.pages.dev/` na conta Google dele) |
| Sitemap enviado | enviado em 26/10, mas com status **"Não foi possível buscar o sitemap"** e 0 páginas (print de 03/11). Em 03/11 o sitemap abre normal (200, application/xml, XML válido, 11 URLs, também para o Googlebot): o Google não chegou a ler. Correção: remover e enviar de novo + pedir indexação da página inicial. **03/11: reenviado pelo Lindson**; logo depois o status voltou a "Não foi possível buscar" com "Última leitura" vazia (o Google ainda não tentou: é o aviso padrão do Search Console para sitemap recém-enviado). Sitemap conferido de novo às 21h19 UTC: 200, application/xml, XML válido, também com o robô do Google. Teste definitivo: Inspeção de URL do próprio `https://desentupidorasf.pages.dev/sitemap.xml` → Testar URL publicado. Conferir de novo em 24 a 48 h |
| Página inicial no Google | **indexada** (Inspeção de URL, print do Lindson de 03/11: "O URL está no Google", HTTPS ok). A busca na web feita por nós em 03/11 não mostrava o site, mas o Search Console confirma a indexação |
| Indexação das outras 10 páginas | 03/11: `/desentupidora-sao-luis/` aparece como "O Google não reconhece o URL" (normal: ainda não rastreada; a página inicial já tem link para todas). O pedido de indexação deu **"A cota foi excedida"** (cota diária do Search Console). Continuar em 04/11, poucas por dia, começando por `/desentupidora-sao-luis/` |
| Perfil da Empresa | a fazer (Lindson, com dados do cliente) |
