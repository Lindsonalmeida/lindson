# Especialista em SEO (aparecer no Google sem pagar)

Conta Leandro, 15/11/2026 (fila `cad2-marca-11`). Base que já existe: `agencia/processos/google-mini-site.md` (Parte 1: SEO local, sitemap, robots, verificação) e as páginas por serviço e cidade da SF, Jaci e Real Time. Ranqueamento e acompanhamento estão no guia irmão `../ranqueamento-sites/`.

## 1. O que o especialista sabe
- **Como o Google funciona:** rastreia (robô lê a página), indexa (guarda) e classifica (mostra na busca). Página que não está indexada não aparece. Fonte: [Como a Pesquisa Google funciona](https://developers.google.com/search/docs/fundamentals/how-search-works).
- **Conteúdo útil, feito para pessoas:** o Google premia página que responde a dúvida real com experiência própria (E-E-A-T: experiência, especialidade, autoridade, confiança). Fonte: [Criar conteúdo útil e confiável](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
- **Básico na página:** 1 tema por página; `<title>` único com serviço + cidade; meta description que convida ao clique; um H1; texto com perguntas que o cliente faz; imagem com `alt`. Fonte: [Guia de SEO para iniciantes](https://developers.google.com/search/docs/fundamentals/seo-starter-guide).
- **Técnico:** sitemap, robots, canonical, site rápido no celular (Core Web Vitals), HTTPS. Fontes: [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview), [Core Web Vitals](https://developers.google.com/search/docs/appearance/core-web-vitals).
- **Dados estruturados** (`LocalBusiness`, `Dentist`, `Plumber`, `FAQPage`) ajudam o Google a entender a empresa. Fonte: [Dados estruturados de empresa local](https://developers.google.com/search/docs/appearance/structured-data/local-business).
- **SEO local** = site + Perfil da Empresa + avaliações + o mesmo nome/telefone/endereço em todo lugar.
- **Spam proibido:** texto repetido trocando só a cidade, palavra escondida, comprar links. Fonte: [Políticas de spam](https://developers.google.com/search/docs/essentials/spam-policies).

## 2. Trilha de 7 dias (1 h por dia)
| Dia | Estudo | Prática |
|---|---|---|
| 1 | [Como a Pesquisa funciona](https://developers.google.com/search/docs/fundamentals/how-search-works) | `site:desentupidorasf.pages.dev` no Google: quantas páginas aparecem? |
| 2 | [Guia de SEO para iniciantes](https://developers.google.com/search/docs/fundamentals/seo-starter-guide) | Revisar title/description de 3 páginas da Jaci |
| 3 | [Conteúdo útil](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) | Escrever 5 perguntas frequentes reais de um cliente |
| 4 | [Pesquisa de palavras com Google Trends](https://trends.google.com.br) e sugestões do Google | Lista de 10 buscas por cliente (serviço + cidade) |
| 5 | [Dados estruturados](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) + [Teste de pesquisa aprimorada](https://search.google.com/test/rich-results) | Testar o site da SF |
| 6 | [PageSpeed Insights](https://pagespeed.web.dev) | Medir os 4 mini sites e anotar o que corrigir |
| 7 | [Search Console: primeiros passos](https://support.google.com/webmasters/answer/9128668) | Montar o relatório mensal modelo |

## 3. Checklist de execução (por site)
1. Lista de buscas do cliente (serviço + cidade + dúvida).
2. Uma página por serviço e uma por cidade, cada uma com texto próprio (não copiar trocando o nome da cidade).
3. Title até ~60 caracteres, description até ~155, H1, FAQ, telefone e WhatsApp visíveis.
4. Dados estruturados do tipo certo + `FAQPage`; validar no Teste de pesquisa aprimorada.
5. `sitemap.xml`, `robots.txt`, canonical para o `pages.dev`, Open Graph.
6. Imagens comprimidas (WebP) e com `alt`; PageSpeed no celular acima de 90.
7. Search Console verificado, sitemap enviado, indexação pedida (passo a passo do `google-mini-site.md`).
8. Link do site no Perfil da Empresa e na bio do Instagram.
9. 1 conteúdo novo por mês (página de dúvida ou de serviço) com o que os clientes perguntam no WhatsApp.
10. Relatório mensal: páginas indexadas, cliques, buscas que trouxeram visita.

## 4. Como vender
- **Oferta:** "Site que aparece no Google": mini site com páginas por serviço e bairro, pronto para o Google ler, e acompanhamento mensal. Mini site avulso **R$ 497** (aprovado, `agencia/ofertas/esteira-de-produtos.md`); já incluso no plano Instagram que Vende (R$ 3.500). Acompanhamento mensal de SEO avulso: preço a definir com o Lindson.
- **Sem promessa:** nunca "primeira página garantida". SEO leva semanas a meses e depende da concorrência.
- **Mensagem:**
  > Oi, Dona Maria! Tudo bem? Sou o Lindson, aqui de São Luís.
  > Quem procura seu serviço no Google acaba achando o concorrente primeiro.
  > Eu faço um site simples que o Google entende, com seu WhatsApp em todas as páginas.
  > Quer que eu te mostre como ficaria?

## 5. Erros comuns e regras
- Página idêntica para cada cidade (spam), site lento com foto pesada, esquecer de enviar o sitemap, mudar endereço do site sem redirecionar.
- **Saúde:** texto educativo, sem promessa de resultado, sem antes e depois, sem preço (CFO/CFM). Sempre CRO/CRM no rodapé.
- **Eleitoral:** site do Leo é de mandato; nada de pedido de voto ou crítica à prefeitura; em período eleitoral seguir a lei eleitoral.
- **LGPD:** formulário só pede o necessário e tem aviso de privacidade; sem rastreio de visitante sem aviso.

## 6. Aplicar já nos clientes
| Cliente | Próxima ação | Quem |
|---|---|---|
| Desentupidora SF | Conferir no Search Console se o sitemap foi enviado e pedir indexação das 11 URLs (`desentupidora-sf/GOOGLE.md`) | Pedro + Lindson (dono) |
| Dra. Jaci | Rodar PageSpeed e Teste de pesquisa aprimorada nas 7 páginas e corrigir | conta Lindson |
| Real Time | Mesmo teste nas 8 páginas; acrescentar FAQ por serviço | conta Lindson |
| Orégano Turbo | Site no repositório `oreganoturbo`: acrescentar sitemap, robots, `Restaurant` + `Menu` | Zuleide |
| Tribuna 98 | Página "Ouvir ao vivo" e páginas por programa com title próprio | Leandro |
| Leo Pinto | Páginas por tema de mandato (projetos, bairros) com title próprio, sem pedir voto | Leandro |
| WF Celulares | Planejar páginas "conserto de tela iPhone em São Luís" etc. quando o site existir | conta Lindson |
