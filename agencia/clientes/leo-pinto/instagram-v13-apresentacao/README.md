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
