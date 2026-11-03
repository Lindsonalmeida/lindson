# Real Time · bio e destaques novos (conta Leandro, 03/11/2026)

Pedido do Lindson (03/11): "crie nova bio, novos destaques". Parte da estratégia v2 (página 6, "O perfil que vende") e da marca nova v1.

## Nome do perfil (aparece na busca do Instagram)
`Real Time · Locação de Cinema` (29 caracteres; o campo nome é pesquisável: entra o que o cliente digita).

## Bio escolhida (até 150 caracteres)
<!-- bio -->
🎬 Locação de câmera, lente e luz de cinema
🟩 Estúdio com fundo verde · Maranhão
🎥 Produção de vídeo para marcas
👇 Reserve seu kit no WhatsApp
<!-- fim -->

Link: `wa.me/5598991331727` (com a mensagem "Oi! Quero reservar um kit." quando tiver o site, trocar pelo link da bio).

**Por que assim:** linha 1 = o que mais vende hoje (locação); linha 2 = o estúdio e onde fica; linha 3 = a frente nova (Produções); linha 4 = o próximo passo. Sem frase de efeito: as palavras que o cliente usa ("locação", "câmera", "fundo verde", "vídeo"). O emoji só marca o começo de cada linha.

### Outras 2 opções (se o Lindson preferir)
- **B (mais curta):** "Equipamento de cinema para alugar · Estúdio com fundo verde · Produção de vídeo no Maranhão · 👇 Reserve no WhatsApp"
- **C (com o slogan):** "Câmera, lente, luz e estúdio prontos para o seu job. 🎬 Locação · Estúdio · Produções · Maranhão. Seu job é na Real Time 👇"

**Conferir:** a cidade do estúdio. Se for São Luís, trocar "Maranhão" por "São Luís - MA" (a busca local fica melhor).

## Destaques (ordem = caminho do cliente)
| # | Destaque | O que vai dentro | Capa |
|---|---|---|---|
| 01 | **Kits** | Kit Cinema, Kit Ópticas, Kit completo: o que vem em cada um (fotos reais) | `capa-01.png` |
| 02 | **Luz** | Aputure STORM 1200x, 400x, 80c e amaran, antes e depois da luz | `capa-02.png` |
| 03 | **Estúdio** | fundo verde montado, o que dá para gravar, tour de 15 s | `capa-03.png` |
| 04 | **Produções** | campanhas, clipes e filmes feitos, do roteiro à entrega | `capa-04.png` |
| 05 | **Clientes** | falas reais e repost de quem gravou (só com autorização) | `capa-05.png` |
| 06 | **Reservar** | passo a passo: escolha o kit → data → WhatsApp → retirada | `capa-06.png` |

Saem: destaques antigos sem tema claro. Ficam fixados no feed: 1 Kit completo, 2 Estúdio fundo verde, 3 Produções (estratégia v2).

**Capas:** composição do visor do template VideoLab (o mesmo do manual: cantos por fora, ponto REC, rótulo em caixa alta, timecode) com os ícones de traço do manual. Fundo Preto Set, branco e o REC vermelho como único detalhe. Desenho no centro (área que o círculo do destaque mostra). Prévia do perfil: `previa-perfil.png`.

## Como gerar
`node gerar.js` (lê a bio deste arquivo entre `<!-- bio -->` e `<!-- fim -->`).
