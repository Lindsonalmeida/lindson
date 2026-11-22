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
