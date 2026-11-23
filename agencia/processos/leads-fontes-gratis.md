# Leads de fontes grátis (teste 22/11/2026)

Destino: `functions/_sdr.js` (CONTATOS) no privado CentralLindsonALmeida, mesmo formato (id, nome, ig, wa 55+DDD+9, nicho, cidade, nota, motivo, msg, fonte). Dedupe por wa e ig.

## Funcionou
- **TeleListas** (`https://www.telelistas.net/<uf>/<cidade>/<categoria>` + subpáginas `em+<bairro>`): cada cartão tem `data-telefone`, `data-site` e link `/locais/...`. Filtrar celular (11 dígitos, 3º = 9), abrir a página /locais e o site para achar `instagram.com/<handle>`. Rendeu 1.104 cartões → 151 com celular → 3 com Instagram (dentistas). Pouco Instagram no cadastro: é o gargalo.

## Falhou
- Overpass (kumi.systems e lz4): proxy derruba a conexão.
- GuiaMais: 406. Apontador, Doctoralia, cardapio.menu: sem celular+Instagram no HTML.
- Busca web (snippets): não devolve perfis do Instagram com número.

## Próximo passo sugerido
Para os 151 celulares sem Instagram, buscar o nome + "instagram" um a um (lento) ou usar o perfil do Google Maps no navegador.

## Melhor caminho (23/11/2026, conta Zuleide): TeleListas → site do negócio
- Pegar TODOS os cartões com `data-site` (mesmo com fixo), abrir a página `/locais/...` e o site, e extrair `instagram.com/<handle>` + `wa.me/` / `api.whatsapp.com/send?phone=` (celular 55+DDD+9). O WhatsApp do botão do site rende muito mais que o telefone do cadastro.
- Paginação: `?pag=2..6`. Bairros: `/ma/sao+luis/em+<bairro>/<categoria>`. Categorias válidas: ver links da página `/ma/sao+luis` (ex.: `advogado`, `clinicas+e+servicos+de+estetica`, `clinicas+de+psicologia`).
- Filtros: DDD tem que bater com a UF do cadastro; descartar redes/franquias e handle genérico (`whatsapp`, `p`, `reel`).
- Rendimento 23/11: ~7.700 cartões → ~165 leads válidos (cerca de 85 BR e 28 MA após dedupe). MA rende pouco: poucas empresas com site.
- Script usado: Python simples com ThreadPool (16-24 conexões), roda em ~8 min por lote.
