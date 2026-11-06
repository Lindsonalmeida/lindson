# Kit de rede social v3 · @oreganoturbo (Paollo + Rocco, conta Leandro, 06/11/2026)

**Pedido do Lindson (06/11):** "não estou gostando da composição das artes para redes sociais. Melhore. Use o agente Paollo."

**O que mudou em relação às pranchas de campanha** (`../../identidade/pecas-campanha/`): antes era a foto inteira com uma manchete Anton jogada no canto e o logo pequeno. Agora cada peça é uma composição com design em volta:
- a foto recortada (BiRefNet) com a letra passando por trás;
- o sistema da marca: xadrez, selos, ícones, faixa, tarja e etiqueta;
- uma chamada para o zap.

Nenhuma peça repete a composição da vizinha.

**Prévia do feed:** `previa-feed.jpg` (grade 3×3, p01 no canto superior esquerdo).

## Peças
| Arquivo | Manchete | Foto | Composição copiada (biblioteca-pizzaria) |
|---|---|---|---|
| `pecas/p01-foto-que-da-fome.jpg` | FOTO QUE DÁ FOME. | B1 mordida (IA) | HOTWHIZ (`favoritas/pin-1144969905302172033.jpg`: boca mordendo, fundo chapado) + "PIZZA gigante atrás": a manchete passa **por trás** do rosto, e há selo girado e adesivo de chamada |
| `pecas/p02-terca-tambem-tem-fome.jpg` | TERÇA TAMBÉM TEM FOME. | B2 caixa no céu (IA) | "O nosso delivery está ON" (chave de interface com a pizza no lugar da bolinha) + Decaf Girl (`favoritas/pin-962081539173882007.jpg`: céu azul, produto na mão); "TERÇA" passa por trás da tampa |
| `pecas/p03-grade-so-pizzarias.jpg` | SÓ PIZZARIAS. (×4) | B3 pizza voando, recortada (IA) | Grade de 4 cores com a mesma manchete (Rocco, formato 5; Drip Riot `favoritas/rel-2033-04.jpg`) + família por cor do Mario hot sauce |
| `pecas/p04-menos-app-mais-zap.jpg` | MENOS APP. MAIS ZAP. | A8 saco "pedido saindo", recortado (IA) | Manchete em 2 tamanhos ("AQUI / não tem / ERRO") + adesivos girados + faixa em loop (Pizzino, `pinterest/img/busca-31.jpg`) |
| `pecas/p05-raio-x-cartaz.jpg` | RAIO-X DA SUA PIZZARIA | pizza da B2, recortada (IA) | Cartaz retrô "Retro PIZZA National Day" (`pinterest/img/retro-13.jpg`): título gordo, explosão de preço R$ 297, faixa de rodapé; moldura em xadrez (Jonny's, `retro-14.jpg`) |
| `pecas/p06-cardapio-da-casa.jpg` | CARDÁPIO DA CASA | fatia v4 (Wikimedia, CC BY 3.0, crédito na arte) | Cardápio-cartaz (Jonny's `retro-14.jpg`, menu `busca-34.jpg`) + fatia gigante saindo da arte |
| `pecas/p07-so-pizzarias-avental.jpg` | SÓ PIZZARIAS. | A4 avental (IA) **com o símbolo oficial** | Moldura xadrez + foto inclinada com adesivos (La Verona `busca-26.jpg`, Antonelli `busca-27.jpg`, Don Diovanni `retro-20.jpg`) |
| `pecas/p08-5-vagas-fundadoras.jpg` | SÓ 5 VAGAS DE FUNDADORA. | B3 pizza voando, recortada (IA) | "PIZZA gigante atrás da pizza", com o número no lugar da palavra, + produto voando (Drip Riot) |
| `pecas/p09-pizza-na-cabeca.jpg` | PIZZA NA CABEÇA. | A6 boné, recortado (IA) | Merch com atitude (boné Crosta `busca-33.jpg`) + faixas em loop cruzadas (Pizzino) |
| `pecas/story-1-enquete.jpg` | DIA FRACO TEM NOME? | B2 recortada | Decaf Girl + figurinha de enquete (segunda, terça ou quarta) |
| `pecas/story-2-raio-x.jpg` | RAIO-X DA SUA PIZZARIA | B3 recortada | Cartaz com explosão de preço (`retro-13.jpg`) + produto voando + faixa "5 vagas" |
| `pecas/story-3-pedido-no-zap.jpg` | PEDIDO DIRETO NO ZAP. | A8 recortada | Conversa de WhatsApp sobre a foto, marcada como "Exemplo ilustrativo" |

## Regras respeitadas
- **Sem promessa de resultado.** Nenhuma peça diz "garantimos pedidos" ou "o anúncio se paga". Fala de dia fraco, foto, zap e Raio-X.
- **Preços:** só os de `../../DECISOES-APROVADAS.md`:
  - Raio-X R$ 297, abatido no 1º mês se fechar em 7 dias;
  - 5 vagas de fundadora, com o preço do anual no semestral.
- **IA:** toda peça com imagem do Gemini leva "imagem gerada por IA". Nada é apresentado como foto de cliente.
- **Exemplo ilustrativo:** a conversa do story 3 vem marcada assim.
- **Logo errado do Gemini:**
  - A10 (fachada) e A9 (cartão) ficaram **fora**.
  - A4 (avental) entrou só depois da correção (`corrigir_avental.py`): o símbolo em contorno foi coberto com o próprio tecido (clonagem de Poisson) e o símbolo oficial foi estampado em branco com a trama.
- **Fatia de banco (p06):** "MVS9966, CC BY 3.0, Wikimedia Commons", com o crédito na arte.

## Como refazer
```
python3 recortar.py B1-mordida        # MODELO=birefnet-portrait (pessoa, mão) ou birefnet-general; 1 por processo
python3 cortar_bbox.py                # versões -bb (recortadas no contorno) para posicionar livre
python3 corrigir_avental.py           # fotos/A4-avental-corrigido.jpg
python3 gerar.py && node render.js && python3 previa.py
```
- `recortes/` tem os recortes em quadro cheio (o mesmo tamanho da foto, para a letra passar por trás) e as versões `-bb`.
- `B2-pizza.webp` é só a pizza da caixa (birefnet-general).
- `B2-caixa-ceu.webp` é a caixa com a mão (birefnet-portrait).

Referências escolhidas e descartadas: `TEMPLATE.md`.
