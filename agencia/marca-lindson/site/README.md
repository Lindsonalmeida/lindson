# Site oficial e mini site da bio do Lindson (conta Pedro, 05/11/2026)

Pedido do Lindson (04/11): "crie um site para mim e reconstrua o meu mini site da bio [...] comunidade de produtos, portfólio completo, contatos [...] páginas com vídeos rolando". Builder Squad (frontend) com o olhar do Design Squad. Pesquisa e template: `TEMPLATE.md` (Lando Norris SOTY 2025 + Dennis Snellenberg + Locomotive/Aparelho Studio).

## Links
- **Site oficial:** https://lindsonalmeida.pages.dev/site/ (portfólio completo em `/site/portfolio/`)
- **Mini site da bio (novo):** https://lindsonalmeida.pages.dev/bio/ : é este link que vai na bio do Instagram. O endereço antigo (`lindsonalmeida.github.io/lindson/links/`) continua no ar, sem mudança.

## Onde está o código
Repositório **privado** `CentralLindsonALmeida` (fotos do Lindson não entram neste repositório público):
- `site/index.html` (home), `site/portfolio/index.html`, `site/assets/site.css`, `site/assets/site.js`
- `site/assets/dados.js`: **os dados** (clientes do portfólio, produtos, redes, mensagens do WhatsApp). Trabalho novo = um item a mais em `trabalhos`.
- `site/img/` (fotos e capas em webp/jpg leves) e `site/media/` (vídeos mudos em loop, 6,3 MB no total, cada um com o pôster .jpg)
- `bio/index.html` (página única, sem bibliotecas), `bio/bg.mp4` (o mesmo vídeo de bastidor da bio antiga), `bio/trilha.mp3` (a trilha de rock da bio antiga, só toca em "Ativar som")
- `robots.txt` agora libera `/site/` e `/bio/` para o Google (o resto da Central continua fechado); a fonte é `agencia/sistema-clientes/site/montar-site.py`.

## Seções do site
1. Abertura: showreel em tela cheia (cenas dos canais Passaporte da Bíblia e Raposa e Leão), "LINDSON ALMEIDA —" gigante correndo atrás do recorte dele, "Comunicação que mobiliza e **engaja**", horário de São Luís.
2. Manifesto (acende palavra por palavra): "Há 14 anos eu faço conteúdo..." + os 3 papéis (conteudista, assessor político, marketing digital).
3. Faixas: números reais (14 anos de conteúdo, 4 sites de clientes no ar, 2 canais no YouTube, 5 produtos na comunidade) e os nomes dos clientes.
4. Em cena: 11 vídeos verticais rodando (motions do Leo, Reels do Lindson, Short do Raposa, gravações dos mini sites).
5. Trabalhos selecionados: nomes gigantes com prévia em vídeo seguindo o cursor.
6. Comunidade **Estado Próprio ▲**: área de membros e os 5 produtos com link para as páginas de venda (sem preço).
7. Sobre: quem é + o plano em 3 passos (vitrine, mês gravado em 1 dia, gente no WhatsApp) + serviços.
8. Contato: WhatsApp com mensagem pronta, "Quero um site", "Quero um mini site", "Quero um Instagram que traz cliente", redes, projetos (Alkantara Connections, Núcleo SLZ, Meu Vereador 5.0).

## Vídeos usados (v2, 05/11: "os vídeos não têm qualidade", pedido de vídeos cinematográficos de banco)
**Banco (licença livre para uso comercial, sem atribuição obrigatória; créditos registrados aqui):**
- Abertura `hero-d/hero-m`: "Fortress near the sea" (Coverr, coverr.co, 1080p) + faíscas "Fire particles on dark background" (Mixkit #3460) e "Sparks of fire on a black background" (Mixkit #3463).
- Estado Próprio `estado-d/estado-m`: "Castle wall" (Mixkit #4236, 1080p) + faíscas (Mixkit #3463).
- Manifesto `xadrez-d`: "Cinematic shot of a wooden chess" (Mixkit #49721, 1080p).
- Contato `brasas-d`: "Fire particles on dark background" (Mixkit #3460, 1080p). Reserva: `mapa-d` "Ancient map of the world in the dark lit by candlelight" (Mixkit #21612).
- Tratamento: preto profundo e âmbar (#F5C518) por ffmpeg (curvas, mistura de canais, vinheta), H.264 crf 22-25, 7 a 10 s em loop com fade, pôster .jpg. Licenças: Mixkit License (mixkit.co/license) e Coverr License (coverr.co/license).
- Fora (regra do Estado Próprio, `ESTADO-PROPRIO-BRANDING.md`): coroa, trono, raposa, leão e retrato renascentista (a abertura v1 usava cenas do Raposa e Leão: trocada).

**Trabalho real (prova):** motions do Leo (`leo-motion-1/3/4`), Reels do Lindson (`reel-tier`, `reel-pare`, `reel-como`), Short do Raposa (`yt-raposa-short`) e stories do Dublê (`duble-story`) em 720×1280 a partir dos originais 1080p; sites dos clientes (`site-*-m` 720×1558 e `site-*-d` 1600×900) feitos de **print da página inteira em 2x** com rolagem suave por ffmpeg (nítidos, sem a gravação de tela tremida da v1).

## Recorte (v2, 05/11: "o recorte está mal feito")
Foto c13 melhorada com Real-ESRGAN x2 (`ferramentas/melhorar_foto.py`), BiRefNet portrait em resolução cheia, filtro guiado na máscara (borda segue o cabelo), 1 px de erosão e **descontaminação de cor** (pymatting `estimate_foreground_ml`): sem halo bege. WebP com transparência de 1031×1800. Conferido a 200% no preto e no amarelo. Script: `agencia/marca-lindson/ferramentas/recorte2.py` (`python recorte2.py foto.jpg saida.webp [corte]`; corte -1 mantém o tamanho da foto inteira). O mesmo passo a passo serve para qualquer recorte: BiRefNet → guiado → descontaminação).

## Fotos do Lindson usadas
Ver `../FOTOS-USADAS.md`. Uma foto por lugar, sem repetir dentro do site.

## Como mudar
Texto e lista de trabalhos: `site/assets/dados.js` e `site/index.html`. Depois: commit e push no `main` do privado; a Cloudflare publica em 1 a 2 minutos.
