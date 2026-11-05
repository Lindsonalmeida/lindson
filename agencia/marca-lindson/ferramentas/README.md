# Ferramentas das artes do Lindson (conta Pedro, 03/11/2026)
- `cor.py` — tratamento de cor das fotos dele (fica COLORIDA: luz laranja do estúdio → âmbar #F5C518, pele natural, contraste, nitidez). Precisa de `selfie.tflite` (MediaPipe) só para proteger a pele.
- `recorte.py` — **padrão de recorte**: BiRefNet portrait (`pip install "rembg[cpu]"`), máscara do tamanho da foto inteira (`cNN-full.png`) + curva que firma a borda.
  Regras (erros que o Lindson apontou em 03/11): nunca recortar o corpo de terno escuro sobre fundo escuro; o corpo vem da própria foto e o recorte só cobre onde o texto passa por trás (máscara em degradê abaixo do texto); o recorte recebe o MESMO escurecimento do fundo (senão fica halo e degrau de brilho); conferir ampliado cabelo, orelhas e ombros antes de enviar.
- Fotos (fora do Git): aba "Minhas fotos" do admin da Central (cli=lindson), baixadas para `artes-v1/fotos/`.
- `recorte2.py` — **recorte v2 (05/11, padrão atual)**: BiRefNet portrait + filtro guiado + descontaminação de cor (pymatting), sem halo. Usar no lugar do `recorte.py` (o Lindson reprovou o recorte do site: halo bege no cabelo e borda mole). Conferir a 200% no preto e no amarelo.
