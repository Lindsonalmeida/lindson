# Stories · Vender sites (marca do Lindson, conta Pedro, 05/11/2026)

Pedido do Lindson: "quero divulgar os sites que eu fiz no Instagram, gere uma sequência de stories, para eu vender esse serviço".
Feito com **Copy Squad** (copy-chief + Hormozi Hooks: gancho pela dor, prova, oferta sem preço) e **Design Squad** (visual).
Identidade v2 aprovada (preto e amarelo #F5C518, Anton, Manrope 800, palavra em caixa amarela, foto colorida com luz âmbar).
Isca **SITE**, código **`MS`** no link do WhatsApp (`ESTRATEGIA.md`, seção 4). Preço só na conversa. Modelos copiados: `TEMPLATE.md`.
Situação: **entregue, aguardando aprovação do Lindson.**

## Onde está
- Telas finais (PNG 1080×1920 e MP4 H.264 1080×1920, 30 fps, 9 a 10,5 s, **com narração na voz dele, SFX, trilha e VFX**, AAC 192k 48 kHz, -14 LUFS): privado `CentralLindsonALmeida/painel/admin-rede/stories-sites/`
  (`s01.png` … `s10.png`, `s04.mp4` … `s07.mp4`, e `guia/` com a posição das figurinhas e as zonas do Instagram marcadas).
  No admin da Central: **Minha rede social → Artes → "Stories · Vender sites"**.
- Fotos do Lindson: só nas telas 01 e 10, por isso as telas não vão para este repositório público.
- Aqui: `stories.html` (as 10 telas), `gerar.js` (gera PNG, MP4, guia), `subir-painel.py` (sobe para a aba Artes), `TEMPLATE.md`.

## A sequência (postar nesta ordem)
Zona segura respeitada: nada importante nos 250 px de cima nem nos 300 px de baixo. Cada tela tem composição diferente da anterior e o fundo alterna preto e amarelo.

| # | Tipo | Fundo e composição | Texto principal | Figurinha (onde) |
|---|---|---|---|---|
| 01 | imagem | preto · foto dele (variação) na frente de "NADA?" gigante | **Seu cliente procura você no Google e não acha nada.** · rótulo "Erro que custa cliente" · "Toque para ver o que eu faço →" | nenhuma |
| 02 | imagem | amarelo · tela de busca: "seu serviço em São Luís" → concorrente, concorrente, você não aparece | **ELE FECHA COM O OUTRO.** · "E quem clica no link da sua bio cai numa página bagunçada… e desiste." | **Controle deslizante** no centro, logo abaixo do texto (y ≈ 1440–1580). Pergunta: "Quanto isso te incomoda?" (emoji 😬) |
| 03 | imagem | preto · "24H" gigante com luz | **Um site que vende por você o dia todo.** · 01 Aparece quando procuram no Google · 02 Mostra seu trabalho com foto de verdade · 03 Leva o cliente direto pro seu WhatsApp | nenhuma |
| 04 | **vídeo 10,4 s** | amarelo · celular inclinado em 3D com o site rolando | **RAFAEL IMPORTS** · mini site da bio · "Loja de celular em São Luís: ofertas, lançamentos e WhatsApp num link só." | **Link** à esquerda, abaixo do texto (y ≈ 1180): `https://rafaelimports.pages.dev` · texto do link: "Ver o site" |
| 05 | **vídeo 10,2 s** | preto · "11" gigante + navegador com o site + celular por cima, os dois rolando | **Desentupidora SF · 11 páginas feitas pro Google** · "Quem procura, acha e chama no WhatsApp." | **Link** embaixo à esquerda (y ≈ 1460): `https://desentupidorasf.pages.dev` |
| 06 | **vídeo 9,0 s** | amarelo · "MANCHETES AO VIVO" andando atrás, celular reto no centro | **Tribuna 98 · jornalismo** · "A bio puxa as notícias do dia sozinha." | **Link** centralizado embaixo (y ≈ 1500): `https://tribuna98.pages.dev` |
| 07 | **vídeo 10,2 s** | preto · dois celulares desencontrados rolando | **Produtora e clínica. Cada um com a sua cara.** · Real Time: site com 8 páginas + bio · Dra. Jaci Cunha: site oficial + bio | opcional: **Link** `https://lindsonalmeida.pages.dev/site/portfolio/` ("Ver mais trabalhos") no espaço entre o título e os celulares |
| 08 | imagem | amarelo · 3 cartões numerados empilhados | **3 PASSOS.** 01 Você responde SITE aqui nos stories. · 02 Eu te mando um vídeo do site já com a cara do seu negócio. De graça. · 03 Gostou? Vai pro ar com o seu link e o seu WhatsApp. | **Caixa de pergunta** embaixo, centralizada (y ≈ 1300–1560): "Qual é o seu negócio?" |
| 09 | imagem | preto · dois cartões de opção, o do Google em amarelo | **Dois jeitos de ter o seu site.** · MINI SITE DA BIO (link bonito da bio, botão pro WhatsApp, serviços com foto real) · SITE COMPLETO NO GOOGLE (uma página pra cada serviço, feito pra aparecer no Google, mini site da bio junto) · "Valores só na conversa" | **Enquete** embaixo, centralizada (y ≈ 1290–1540): "Qual é a sua?" · opções "Mini site da bio" / "Site no Google" |
| 10 | imagem | amarelo · "SITE" gigante atrás dele (variação), degradê preto | **Responde SITE aqui que eu te mostro o seu.** · "ou toque no link → WhatsApp" | **Link** embaixo à esquerda (y ≈ 1470): WhatsApp com o código, texto do link "Me chama no WhatsApp" |

Link do WhatsApp (tela 10), mensagem pronta com o código MS:
`https://wa.me/5598985621808?text=Oi%2C%20Lindson!%20Quero%20um%20site%20pro%20meu%20neg%C3%B3cio%20(MS)`
("Oi, Lindson! Quero um site pro meu negócio (MS)")

## Vídeos: narração, SFX, trilha e VFX (regra do Lindson, 05/11: "nunca faça vídeos sem áudio, sempre narração fluida que não pareça IA, VFX e SFX")
**Narração na voz clonada do próprio Lindson** (Dublê, Chatterbox Multilingual; ele mesmo mandou os áudios e autorizou a voz). Método aprovado do `apps/clone-studio/motor_voz.py`: melhor trecho + identidade média da amostra inteira, temperatura 0,6, voz limpa e fluida (blocos de até ~220 caracteres, pausas de ~0,2 s, sem respiração artificial, estalos aparados, estúdio leve). Sem rosto no vídeo (só as telas dos sites). Conferido com Whisper: texto certo, sem corte e sem pausa robótica (maior silêncio no meio da fala: 0,39 s, na troca de frase).

| Vídeo | Fala (1ª pessoa, Conexão → Dor → Desejo) | Voz | Vídeo |
|---|---|---|---|
| 04 Rafael Imports | "Esse é o mini site da Rafael Imports. Ofertas, lançamentos e o WhatsApp da loja e da assistência, tudo num link só, direto na bio." | 9,0 s | 10,4 s |
| 05 Desentupidora SF | "Agora, a Desentupidora SF. Um site com onze páginas, feito pra aparecer no Google. Quem procura, acha, e já chama no WhatsApp." | 8,9 s | 10,2 s |
| 06 Tribuna 98 | "Esse aqui é da Tribuna 98. A bio puxa as notícias do dia sozinha: saiu no blog, já aparece ali, sem ninguém mexer." | 7,6 s | 9,0 s |
| 07 Real Time + Dra. Jaci | "E cada negócio com a sua cara. A Real Time, produtora, com site de oito páginas. A Doutora Jaci Cunha, com site oficial e bio. Bora fazer o seu?" | 8,9 s | 10,2 s |

Textos em `falas.json` ("SF" vai escrito "Esse Efe" para a voz ler a sigla). A amostra da voz dele **não vai para o Git** (dado biométrico).
- **SFX** (sintetizados, mesmo sintetizador do motion do Leo): whoosh quando o aparelho entra, pop em cada texto e selo, impacto leve na palavra-chave, 3 cliques suaves quando a rolagem começa. Deixas tiradas da própria animação (`cues.json`).
- **Trilha:** Kevin MacLeod (incompetech.com), licença CC BY 4.0 (creativecommons.org/licenses/by/4.0/): 04 e 07 "Carefree", 05 "Life of Riley", 06 "Wholesome". Baixinha (-17 dB) e abaixada para -27 dB sob a voz. **Crédito obrigatório:** se postar com a trilha, pôr em algum lugar do perfil ou da legenda: "Música: Kevin MacLeod (incompetech.com), CC BY 4.0".
- **VFX:** vazamento de luz âmbar na entrada e na saída, tremida de câmera de 3 quadros no impacto, borrão direcional (vertical) no aparelho que entra, grão de filme que muda a cada quadro, paralaxe leve (halo, nome fantasma, faixas). Identidade v2, sem raio nem fumaça.
- **Mix:** -14 LUFS (loudnorm em 2 passadas), pico real ≤ -1,5 dBTP (medido no MP4 final), AAC 192k 48 kHz.
- Os sites são gravados no ar de novo, quadro a quadro, na duração da narração (`gravar.js`: rolagem suave e exata).

## Quem responder (direct)
- Respondeu **SITE**, votou na enquete ou mandou o negócio na caixa: responder no padrão `agencia/prospeccao/PADRAO-COPY.md` e seguir a isca: pedir o @ e o WhatsApp e mandar o **vídeo de demonstração do mini site no nome dele** (processo `agencia/processos/demo-minisite/`). Valores só na conversa.
- Exemplo: "Oi, [nome]! Aqui é o Lindson. Recebi sua resposta: quer que eu monte um vídeo mostrando como ficaria o site da [negócio]? É de graça. Me manda seu WhatsApp."

## Quando postar
- **Quinta 12/11**, à noite, depois do Reels "Mini site da Rafael Imports" (dia da isca SITE no `CALENDARIO.md`), e de novo na **quinta 19/11**, depois do Reels do site da Desentupidora SF.
- Horário: começar entre 18h e 20h (depois do expediente do dono de negócio) e ajustar pelo horário de pico que o Insights mostrar. Postar as 10 de uma vez, na ordem.
- Fixar depois nos destaques **"Mini site"**.

## Fotos do Lindson (regra: foto usada não se repete)
Todas as fotos de estúdio já tinham sido usadas; ele liberou variações ("pode criar variações com IA"). Usamos **variações** (registradas em `../FOTOS-USADAS.md`):
- tela 01: **c11 espelhada**, recorte do busto (recorte2.py, sem halo, conferido a 200% no preto e no amarelo), fundo preto com luz âmbar;
- tela 10: **c16 espelhada**, recorte do busto, sobre amarelo com "SITE" atrás.
As variações ficam em `../artes-v1/fotos/c11-rec2-esp.png` e `c16-rec2-esp.png` (fora do Git).

## Fatos usados (todos do repositório, nenhum número inventado)
Rafael Imports: mini site da bio, loja em São Luís (está no próprio site). Desentupidora SF: site com 11 páginas. Tribuna 98: bio que puxa as manchetes ao vivo. Real Time: site de SEO com 8 páginas + bio. Dra. Jaci: site oficial + bio. Fonte: `../site/INVENTARIO-PORTFOLIO.md`. Os sites são gravados no ar (`gravar.js`).

## Como gerar de novo
```bash
cd agencia/marca-lindson/stories-sites
# fotos-variação em ../artes-v1/fotos/ (para refazer: python3 ../ferramentas/recorte2.py ../artes-v1/fotos/c11.jpg /tmp/c11-rec2.webp -1 e espelhar o PNG)
<venv-chatterbox>/bin/python narra.py <amostra-da-voz.wav> <pasta-voz>   # narração na voz dele (fora do Git)
python3 -c "import soundfile as sf,json;json.dump({s:round(30*(.45+len(sf.read('<pasta-voz>/s0'+s+'.wav')[0])/44100+.95)) for s in '4567'},open('duracoes.json','w'))"
node gerar.js            # as 10 telas; os sites são gravados no ar na duração certa (só as de vídeo: node gerar.js 4 5 6 7)
python3 audio.py <privado>/painel/admin-rede/stories-sites <pasta-voz> <pasta-musicas-kevin-macleod> <pasta-quadros>   # voz + SFX + trilha + -14 LUFS
python3 subir-painel.py  # copia para o privado e põe na aba Artes do admin (artes-aprovadas.json)
python3 ../../sistema-clientes/site/montar-site.py && cp ../../sistema-clientes/site/publico/painel/admin.html /home/user/centrallindsonalmeida/painel/admin.html
```
Prévia de uma tela no navegador: `stories.html?s=4&q=/pasta/dos/quadros&f=45` (`&guia=1` mostra figurinhas e zonas do Instagram).
