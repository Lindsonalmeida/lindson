# Feed v13 · Apresentação do Vereador Leo Pinto (3 primeiras artes) · conta Lindson, 02/11/2026

Três posts 1080×1350 que formam **uma imagem só** na grade do perfil @_leonardopinto.
Identidade nova (02/11/2026): **só fontes (Anton, Kaushan Script, Montserrat), logo e cores**, sem raios, faixas, ícones, fumaça ou sol.

- `REFERENCIAS.md`: pesquisa (Behance, campanhas premiadas, técnica da grade 3:4, ordem de postagem), feita pelo design-squad + brand-squad.
- `TEXTOS.md`: textos das artes (opção A) e as 3 legendas SEO, feitos pelo time de mensagem (Donald Miller + copy-squad).
- Composição: **Direção B simplificada**, com duas cores chapadas (amarelo e azul royal; a troca passa atrás do Leo) e retrato central (foto leo-01, polo laranja, cor realçada de leve).
  1. Esquerda (amarelo): SOU O **LEO** · vereador de São João Batista · Eleito em 2024 · Maranhão
  2. Meio: retrato · engenheiro e na rua · **DA BAIXADA**
  3. Direita (azul): JUNTOS PODEMOS **MAIS!** · me conta sua demanda · Siga e acompanhe o mandato de perto · logo oficial
- Grade 3:4: a arte-mestra tem 3 × 1012 px visíveis + 34 px de sangria; cada post repete 34 px do vizinho, então o painel encaixa sem "pulo" nas miniaturas. Prévia: `previa-grade.jpg`.

## Como postar
1. Postar **3-direita**, depois **2-meio**, depois **1-esquerda**, em sequência e sem outro post no meio. Não mexer no ajuste da miniatura.
2. Desafixar o que estiver fixado e fixar **3, depois 2, depois 1** (o último fixado aparece primeiro).
3. Legendas em `TEXTOS.md`.

## Como gerar de novo
Recortes (fora do Git, fotos do cliente): `python3 ../instagram-v12-feed/recortar.py <album> assets leo-01:original`, realce de cor (Color 1.28, Contrast 1.06) → `assets/leo-01-cor.png`; `assets/logo.png` = `../instagram-v12-feed/marca/logo_principal.png`.
Depois: `python3 gerar.py . && node render.js $PWD && python3 cortar.py .`

## Versão 3 (atual, 02/11/2026) · `gerar3.py`
Pedido do Lindson: "mais sofisticadas, camadas, degradês" e duas referências para aplicar (Social Media Marcelo Tavares Prefeito e Erick Monteiro Deputado Estadual).
- Aplicado: retrato grande de perto (foto **leo-14**, polo amarela), nome em **blocos de cor** (LEO na caixa amarela, PINTO na caixa branca), rótulo espaçado, frase empilhada em Montserrat Black (fonte da logo), etiquetas (laranja e branca), **mapa oficial de São João Batista** em camada translúcida (contorno do IBGE via geodata-br, `mapa-sjb.json`), degradê azul com luz diagonal e granulação fina.
- Não aplicado: rabiscos à mão (vão contra a decisão de 02/11 de não usar grafismos).
- Textos do Lindson (02/11): **vereador mais bem votado** · **do povo para o povo** · **jovem, engenheiro, compromisso com São João Batista**.
  1. Esquerda: retrato · "Prazer, eu sou o Leo"
  2. Meio: São João Batista • MA · LEO / PINTO · VEREADOR MAIS BEM VOTADO · Jovem • Engenheiro · compromisso com São João Batista
  3. Direita: DO POVO PARA O POVO · juntos podemos mais! · ME CONTA SUA DEMANDA · Siga e acompanhe o mandato de perto · logo
- Recortes: `assets/leo-14-original.png` (do `recortar.py`) e `assets/logo.png`. Gerar: `python3 gerar3.py . && node render.js $PWD && python3 cortar.py .`
- Versão 2 (`gerar2.py`: amarelo/azul em diagonal, "BAIXADA" fantasma, vidro fosco) fica guardada como alternativa.
- **Legendas:** as de `TEXTOS.md` foram escritas para a versão 1; ajustar com os textos novos antes de postar.
