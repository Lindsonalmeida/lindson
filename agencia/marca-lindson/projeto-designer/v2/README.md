# Projeto Designer v2 (conta Leandro, 16/11/2026) · aguardando aprovação

A v1 foi reprovada ("ficou horrível": capa = slide recortado, fundo preto vazio, sem mockup, proposta com placeholder). A v2 começa pela pesquisa (`PESQUISA.md`) e vive de **mockups fotorrealistas** com o logo oficial de cada marca.

Nome do estúdio: **Lindson Almeida Studio** (recomendado na v1, aguardando aprovação). Visual: editorial claro (off-white #F2EFE9, preto #0A0A0A, amarelo #F5C518 só em detalhe), Instrument Serif + Manrope + JetBrains Mono; Anton só na assinatura do estúdio.

## O que tem aqui
- `PESQUISA.md` + `referencias/`: Pinterest, Behance e 11 estúdios de 7 países (capturas).
- `behance/<case>/`: 6 cases (Leo Pinto, Real Time, Processo Legislativo, WF Celulares, Orégano Turbo, Dublê). Capa 808x632 sem texto + 12 a 13 módulos de 1400 px (hero, conceito, logo, versões, paleta, tipografia, papelaria, celular, detalhe, embalagem, pôster, outdoor, fecho) + `TEXTO.md`. Leo: sem outdoor e sem slogan (nada com cara de campanha).
- `pinterest/`: perfil, 6 pastas SEO, 30 pins, `PINS.csv`, 3 vídeos.
- `oferta/`: página de venda (`pagina/index.html` + prévia), proposta PDF v2 ("Sua marca", cases reais, sem preço) e anúncio carrossel de 5 telas (`anuncio/`).
- `gerador/`: `texturas.py` (logo e paleta oficiais do brand book → texturas), `cenas.js` + `mockups.py` (cenas 3D em Three.js: cartões, papelaria, celular com Instagram, pôster na parede, embalagem, outdoor), `compor.py` (Behance + pins), `oferta.py`.

## Como refazer
```
BB_TMP=/tmp/bb python3 gerador/texturas.py <tex>
python3 gerador/mockups.py <tex> <mk> <node_modules/three>            # paisagem
python3 gerador/mockups.py <tex> <mk> <node_modules/three> --retrato  # pins
BB_TMP=/tmp/bb python3 gerador/compor.py <tex> <mk> .
python3 gerador/oferta.py <mk> .
```
(three@0.169.0 via `npm i three@0.169.0`; Playwright com Chromium.)
Painel: privado `painel/admin-rede/projeto-designer/v2/` (folha.jpg e arquivos).
