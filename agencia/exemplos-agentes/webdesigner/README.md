# Exemplo do agente Webdesigner · Pizzaria Brasa Viva (08/11/2026)

Mini site (bio/landing) de uma pizzaria **fictícia**, feito só para mostrar o que o agente Webdesigner entrega. Não publicado, sem repositório próprio, fora do portfólio. Fotos não marcadas como usadas.

Abrir: `index.html` (HTML, CSS e JS sem build, sem bibliotecas externas além do Google Fonts). Prévias v2: `previa-celular.png` (390 px, 2x, página inteira), `previa-celular-topo.png` (3 primeiras dobras), `previa-computador.png` (1440×1800) e `previa-computador-inteira.jpg` (página inteira, 720 px). A **v1** (só fotos) está guardada em `v1/`.

## v2 · "use fotos e vídeos no site" (pedido do Lindson, 08/11)
- **Herói:** o vídeo do forno a lenha (pizza entrando) roda dentro da **moldura-arco** com os anéis do símbolo ("a boca do forno"); a pizza recortada sobrepõe a base do arco e "BRASA VIVA" corre atrás.
- **Trilho "Do forno pra sua porta"** (estilo Aparelho Studio): 4 vídeos verticais 9:16 (Massa, Lenha, Fatia, Pronta), que se arrastam no celular e ficam em 4 colunas desencontradas no computador.
- **Manifesto** com vídeo da lenha queimando no fundo, mantendo as palavras que acendem.
- **Galeria em mosaico "Da lenha à mesa"** com 9 fotos grandes (6 do banco Pexels + 3 Wikimedia), a primeira na moldura-arco, sem buracos no grid.
- Entrega: foto da moça no carro (IA, marcada) na moldura-arco.
- Vídeos: mudos, `autoplay` via JS, `playsinline`, `loop`, pôster jpg; carregam só perto da tela (`preload="none"` + IntersectionObserver; o trilho inteiro carrega junto), pausam fora da tela; com `prefers-reduced-motion` fica só o pôster. Cada vídeo tem menos de 1 MB.
- Tudo da v1 continua: pedido pelo WhatsApp com mensagem pronta, montador, aberto/fechado pelo horário de São Luís, abas do cardápio, combos, botão flutuante. Sem rolagem horizontal (conferido em 390 e 1440 px).

## Créditos
- **Vídeos:** Mixkit, licença gratuita Mixkit (#28144, #32415, #42469, #44014, #42484). Detalhes em `assets/video/CREDITOS.md`.
- **Fotos Pexels** (licença Pexels, banco `agencia/bancos/pexels-pizza/`): 11447751, 3343622, 3343627, 3915857, 35017349, 1878346 (links no rodapé).
- **Fotos Wikimedia Commons** (`agencia/operacao-propria/identidade/fotos-v4/CREDITOS.md` e `fotos-v3/CREDITOS.md`): BullDawg2021, Horacio Cambeiro, jeffreyw, Foodie Moodie, Andy Li (fotos-v4) e CDibisceglia (fotos-v3).
- **IA:** pizza recortada do topo e moça no carro (`fotos-ia/hd/B7`), marcadas "imagem gerada por IA".

## Persona (cliente final)
1. Mariana, 32 anos, mora no Cohama/Renascença, em São Luís; trabalha o dia todo e pede pizza na sexta e no domingo à noite.
2. Chega pelo Instagram, no celular, com fome e pressa: quer decidir em 1 minuto.
3. Dor: cardápio em PDF ilegível, sem preço, sem saber se entrega no bairro, pizza chegando fria, demora para responder.
4. Valoriza foto de pizza de verdade, preço claro, combo para dividir e pedir pelo WhatsApp sem digitar tudo.
5. Confia quando vê horário, bairros atendidos e a mensagem já pronta. Teste: em 3 segundos ela sabe o que é, se está aberto e onde tocar para pedir.

## As 3 referências copiadas (só composição e técnica)
1. **Lando Norris · OFF+BRAND** (Awwwards Site of the Year 2025, `agencia/marca-lindson/site/TEMPLATE.md`): uma cor só de destaque, palavra-chave em caixa, manifesto gigante que acende palavra por palavra (v2: com vídeo no fundo), pílula de pedido fixa.
2. **Dennis Snellenberg** (Awwwards SOTD) + **Locomotive / Aparelho Studio** (BR, SOTD): nome gigante em marquee atrás do herói e trilho de vídeos verticais.
3. **Owner.com** (`agencia/operacao-propria/site/TEMPLATE.md`): tudo leva ao pedido; celular mostrando a conversa do WhatsApp que se monta ao vivo.

Identidade: a do Designer gráfico (`../designer-grafico/SISTEMA.md`): Brasa #E2431D, Farinha #F3E7D3, Carvão #1A1411 e Chama #FFB321 só numa palavra; Bricolage Grotesque 800 condensada + DM Sans; símbolo do arco do forno no topo, moldura-arco no herói, na galeria e na entrega. Número (98) 9 0000-0000 e valores são ilustrativos.
