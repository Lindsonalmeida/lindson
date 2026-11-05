# Site do Lindson no Google: passo a passo (conta Leandro, 05/11/2026)

O site está pronto para o Google desde 05/11:
- sitemap com /site/, /site/portfolio/ e /bio/;
- robots liberando só essas áreas (os painéis da Central ficam fora);
- dados estruturados de pessoa no portfólio e na bio.

## Search Console (5 minutos)
1. Abra **search.google.com/search-console** → Adicionar propriedade → **Prefixo do URL** → `https://lindsonalmeida.pages.dev/` → **Arquivo HTML** → baixe o `googleXXXX.html` e mande ao Claude.
2. **O Claude:** publica o arquivo na raiz do site, pelo privado `CentralLindsonALmeida`, e avisa. Então clique em **Verificar**.
3. **Sitemaps** → `sitemap.xml` → **Enviar**. Deve mostrar 3 URLs.
4. **Inspeção de URL** → **Solicitar indexação**:
   - https://lindsonalmeida.pages.dev/site/
   - https://lindsonalmeida.pages.dev/site/portfolio/
   - https://lindsonalmeida.pages.dev/bio/

## Perfil da Empresa (opcional)
- **Só vale se você atende como empresa:** nome comercial, ou "Lindson Almeida · Estrategista Digital", com área de atendimento em São Luís e no Maranhão, sem endereço público.
- **Categoria:** Agência de marketing.
- **WhatsApp:** o do site.
- **Descrição:** puxar do manifesto do site.
- **Decisão sua:** se quer o perfil no Maps.
