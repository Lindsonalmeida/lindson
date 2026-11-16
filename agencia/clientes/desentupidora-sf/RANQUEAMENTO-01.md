# Desentupidora SF · Relatório de ranqueamento nº 1 (conta Leandro, 16/11/2026)

Fila `esp-sf-ranking`. Guia: `agencia/especialista/ranqueamento-sites/`. Site: https://desentupidorasf.pages.dev

## 1. Auditoria técnica (feita agora, sem precisar de acesso)
| Item | Situação |
|---|---|
| robots.txt e sitemap.xml | ✅ ok, com 11 páginas |
| Canonical em cada página | ✅ ok |
| Um H1 por página | ✅ ok |
| Dados estruturados | ✅ Plumber, Service, Offer, FAQPage e City; ⚠️ falta `openingHours` |
| Tamanho das páginas | ✅ 16 a 28 KB, leve |
| Texto por página | ✅ 740 a 1.290 palavras |
| Títulos | ⚠️ 3 páginas passam de 60 caracteres e são cortados no Google |
| Descrição da home | ⚠️ 215 caracteres; o Google mostra só ~155 |
| Imagens sem alt | ⚠️ o logo, em todas as páginas |
| Home × /desentupidora-sao-luis/ | ⚠️ as duas disputam a mesma busca ("Desentupidora em São Luís MA") |
| Search Console | ✅ arquivo de verificação no ar (google7ec…html); falta o acesso da conta Leandro para ler Páginas e Desempenho |
| Domínio | ⚠️ `pages.dev` ranqueia, mas um domínio próprio (.com.br) passa mais confiança |

## 2. Ajustes, em ordem de impacto
1. **Search Console:** o site já está verificado. Confira se o `sitemap.xml` foi enviado e adicione a conta da agência como usuário (Configurações → Usuários e permissões) para gerar o relatório de Páginas e Desempenho.
2. **Diferenciar a home de /desentupidora-sao-luis/.**
   - Home: "Desentupidora SF · Desentupimento 24h em São Luís e região".
   - /desentupidora-sao-luis/: focar nos bairros (Cohama, Turu, Cohab, Centro…), com uma lista de bairros e um mapa.
3. **Títulos com até 60 caracteres:**
   - Home: `Desentupidora em São Luís 24h | Desentupidora SF` (48)
   - Vaso: `Desentupir vaso sanitário em São Luís | SF` (42)
   - Caixa de gordura: `Limpeza de caixa de gordura em São Luís | SF` (44)
4. **Descrição da home com até 155 caracteres:** `Desentupidora em São Luís 24h: pia, vaso, ralo, esgoto e caixa de gordura. Orçamento grátis pelo WhatsApp e atendimento em toda a Ilha.` (138)
5. **Alt do logo:** `alt="Desentupidora SF"`.
6. **`openingHours` no Plumber** (ex.: `Mo-Su 00:00-23:59`, se for 24h de verdade) e o mesmo horário na ficha do Google.
7. **Domínio próprio** (ex.: desentupidorasf.com.br, cerca de R$ 40/ano), apontado para a Cloudflare, com redirecionamento 301 do pages.dev.
8. **Links da ficha do Google** apontando para a página do serviço ou da cidade, e não só para a home.

## 3. Quando houver acesso ao Search Console (relatório nº 2, 28 dias depois)
- Páginas: quais foram indexadas e o motivo de cada exclusão.
- Desempenho: as 20 consultas com mais impressões, CTR e posição média.
- Ação: página com muitas impressões e CTR abaixo de 2% ganha um título novo; consulta na posição 8 a 20 ganha uma seção nova na página.

Não prometemos posição no Google. O relatório mostra o que mudou mês a mês.

## 4. Aplicado em 16/11 (repositório GruposSF)
Itens 3, 4 e 5 no ar: títulos até 60 caracteres, descrição da home com 135 e alt no logo. Pendentes: o 2 (reescrever a página /desentupidora-sao-luis/), o 6 (horário de atendimento real), o 7 (domínio próprio) e o 8 (links da ficha do Google).
