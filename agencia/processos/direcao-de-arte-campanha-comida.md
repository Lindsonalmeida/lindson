# Direção de arte de campanha de comida: lista de cenas e prompts (agente Rocco, conta Leandro, 06/11/2026)

**Para quê:** produzir o estilo que o Lindson chama de "identidade visual de verdade, impactante, criativa". O agente que usa este processo é `.claude/agents/rocco.md`.

**Três caminhos de produção:**
1. **Foto real do cliente:** a melhor opção. Lista de cenas na seção 1.
2. **Montagem:** recorte de comida, cor chapada e sombra de flash. Receita na seção 2.
3. **IA de imagem:** para as cenas com pessoa, quando o Nano Banana estiver liberado. Prompts na seção 3.

## 1. Lista de cenas para uma manhã de fotos na pizzaria (celular serve)
**Material:**
- 3 cartolinas grandes de cor forte: vermelho, laranja ou amarelo, e verde-limão ou azul;
- flash do celular, ou luz dura de uma janela com sol;
- borrifador de água;
- ingredientes soltos: calabresa, tomate, manjericão, queijo ralado.

| # | Cena | Como fazer |
|---|---|---|
| 1 | Fatia com o queijo puxando, segurada para a câmera | Fundo de cartolina vermelha, flash ligado, a mão vindo de baixo |
| 2 | Mordida de verdade | Close da boca mordendo, com o queijo esticando, fundo de 1 cor |
| 3 | Caixa aberta segurada com as 2 mãos | Pizza inteira vista de cima, contra a cartolina laranja |
| 4 | Pizza vista de cima com os ingredientes espalhados em volta | Em cima da cartolina, celular a 1 metro de altura, sem sombra de mão |
| 5 | Ingredientes "voando" | Jogar manjericão e calabresa por cima da pizza e fotografar no modo rajada |
| 6 | Pizzaiolo de avental, de baixo para cima | Grande-angular (0,5×) de baixo, com o céu ou o forno atrás |
| 7 | Caixa na mão do motoboy | De baixo, com o céu azul atrás, e a caixa ocupando metade da foto |
| 8 | Mão com a caixa no balcão | A marca da caixa virada para a câmera |
| 9 | Família de produtos | Pizzas, bebidas e sobremesas numa bandeja ou cesta, vistas de cima, sobre a cor |

## 2. Montagem (sem fotos novas)
1. **Foto licenciada** (Wikimedia Commons CC com crédito, ou do cliente): melhorar com `ferramentas/melhorar_foto.py`.
2. **Recorte** da pizza e dos ingredientes com BiRefNet/rembg (uma imagem por processo, porque a memória é limitada).
3. **Fundo** de 1 cor chapada saturada.
4. **Sombra de flash:** cópia da silhueta em preto com opacidade de 35 a 45%, deslocada 18 a 30 px para baixo e para a direita, desfoque de 2 a 4 px. É dura, não esfumada.
5. **Brilho:** sobreposição clara de 6 a 10% no topo do produto; contraste e saturação +8 a 12%.
6. **Ingredientes voando** em volta: tamanhos variados, alguns com desfoque de movimento de 4 a 8 px.
7. **Manchete gorda** (Google Fonts: Bagel Fat One, Lilita One, Anton, Rubik Mono One, Bowlby One) atrás ou na frente do produto. Pode ser maior que a margem.
8. **Grão fino** por cima, com 4 a 6% de opacidade.

## 3. Prompts para IA de imagem (Nano Banana / Gemini), cenas com pessoa
Sempre em inglês para o modelo. Troque a cor e o produto. **Não use rosto de pessoa real conhecida.**

1. **Mordida:** "Extreme close-up of a young Brazilian man biting a slice of pepperoni pizza, long stretchy melted cheese pull, sauce on lips, holding the slice toward camera, solid bright lime green background, harsh direct on-camera flash, hard shadow, high saturation, editorial food advertising photography, 35mm, sharp detail, 4:5"
2. **Mão com a caixa:** "A hand with painted nails holding an open pizza box toward the camera, whole pizza visible, shot from low angle against clear blue sky and sun flare, wide-angle lens, harsh sunlight, vibrant colors, bold food brand campaign photography, 4:5"
3. **Produto voando:** "A whole pizza floating mid-air with flying slices, basil leaves, tomato pieces and pepperoni exploding around it, solid tomato red background, studio flash, crisp hard shadows, high-speed photography, food advertising, 4:5"
4. **Vista de cima:** "Top-down flat lay of an open pizza box inside a metal shopping basket filled with tomatoes, basil and peppers, solid orange background, direct flash, hard shadows, bold packaging photography, 4:5"
5. **Estilo de vida:** "Young woman with sunglasses laughing and holding a pizza slice outside a yellow car window, low angle wide-angle shot, deep blue sky, summer sunlight, vibrant editorial lifestyle photography, flash fill, 4:5"
6. **Motoboy:** "Delivery rider holding a pizza box high, shot from below with wide-angle lens, blue sky, motion energy, bold advertising photography, saturated colors, 4:5"

**Regra:** imagem gerada por IA não se apresenta como foto real do cliente nem do produto dele. Quando for anúncio, seguir as regras da plataforma sobre conteúdo gerado.

## 4. Modelos de manchete (português, com atitude, até 5 palavras)
- **Para a pizzaria do cliente:** "QUEIJO ATÉ O TETO" · "PEDE QUE VEM" · "SEM DÓ DE CALABRESA" · "FATIA QUE ESTICA" · "TERÇA TAMBÉM É DIA" · "FOME DE QUÊ?" · "CHEGOU QUENTE"
- **Para a Orégano Turbo** (vendendo para o dono de pizzaria):
  - "SUA PIZZA MERECE FILA"
  - "FORNO CHEIO TODO DIA"
  - "MENOS APP, MAIS ZAP"
  - "TERÇA VAZIA? AQUI NÃO"
  - "PEDIDO NA MESA, NÚMERO NA MÃO"
  - Sempre sem promessa de resultado.
