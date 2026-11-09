# Reels 30 s do Lindson: pesquisa premium e template copiado (conta Leandro, 09/11/2026)

> Esta é a pesquisa premium que faltou para a leva de 10 Reels de 30 s (`ESTRATEGIA.md` §5, `roteiros.json`). Segue a regra de 05/11 (`agencia/processos/pesquisa-premium.md`).
> Copiamos **técnica de motion** (composição, tipo, ritmo, transição). Cores, fontes e assinatura continuam as do Lindson: preto #0B0B0B, amarelo #F5C518, Anton + Manrope + mono e @lindsonalmeida_.
> Capturas novas, feitas hoje com Playwright, em `referencias/2026-11-09/`. Nenhuma captura antiga foi reaproveitada.

## Persona antes da referência
- **Quem vê:** dono de negócio local em São Luís (loja, clínica, restaurante, oficina), de 25 a 50 anos.
- **Rotina:** rola o Instagram no intervalo do balcão, com som baixo ou sem som.
- **O que precisa:** entender a frase em 1 segundo, ver o próprio problema (perfil, WhatsApp, cliente que some) e sentir que quem fala é sério.
- **O que tira a confiança:** cara de "template de agência", desenho lúdico e promessa de número.
- **A pergunta:** "essa pessoa pararia e confiaria nisso?". Ela filtrou as referências abaixo, antes do gosto de designer.

## As 3 escolhidas (combinadas)

### 1. Studio Dumbar/DEPT®: DEMO Design in Motion Festival 2025 (Holanda)
- **Links:** https://studiodumbar.com/work/demo-2025 (lista em https://studiodumbar.com/work).
- **Capturas:** `referencias/2026-11-09/26-studiodumbar-demo-2025.jpg`, `26b-studiodumbar-demo-2025-telas.jpg`, `12-studiodumbar.jpg`.
- **Reconhecimento:**
  - Studio Dumbar é um estúdio de Roterdã que hoje faz parte do grupo DEPT®.
  - O DEMO, segundo a página do estúdio, é "o maior festival de motion design do mundo": nasceu nas telas da Amsterdam Centraal em 2019 e em 2025 foi para 15 cidades.
  - Prêmios do projeto: não conferidos.
- **Por que ganhou:**
  - É tipografia em movimento feita para quem passa andando e lê uma tela em 1 segundo, a mesma situação do dono que rola o feed.
  - Fundo preto e uma palavra gigante por vez combinam com a marca do Lindson sem mudar nada.
- **Técnica que copiamos:**
  - **Composição:** uma ideia por tela, com a palavra-chave ocupando a largura inteira (margem de 60 px) e mais nada em volta.
  - **Tipografia:** a palavra entra por **máscara** (masked reveal: a letra sobe de trás de uma linha invisível), e não só com blur. As palavras de apoio ficam pequenas, em mono.
  - **Ritmo:**
    - no gancho (0 a 3 s), um corte seco a cada 0,4 a 0,6 s, no beat da trilha;
    - depois, a cada 1,5 a 2 s.
  - **Transição:** corte seco, com 2 quadros de branco (#flash) só no impacto principal.
- **Como entra no motor:** `motor/palco.html` já tem o que é preciso. A mudança fica no roteiro de cada cena:
  - camada `.layer` com `.A` em tamanho ajustado à largura (1000 px úteis);
  - `clip-path: inset(100% 0 0 0)` indo a `inset(0)` com `eo()` em cerca de 8 quadros dentro de `render(t)`;
  - amarelo só na palavra-chave (`.hl`);
  - SFX "hit" anotado em `window.SFX` em cada corte seco.

### 2. ManvsMachine: "Trade Every Play" para a Robinhood (Reino Unido)
- **Link:** https://mvsm.com/project/trade-every-play
- **Capturas:** `referencias/2026-11-09/28-manvsmachine-robinhood-trade-every-play.jpg` e `06-manvsmachine.jpg`.
- **Reconhecimento:**
  - ManvsMachine é um estúdio de Londres e Los Angeles.
  - É um projeto de campanha comercial em destaque na home do estúdio.
  - Prêmios do projeto: não conferidos.
  - O player do vídeo pediu verificação. Não foi contornado: a técnica foi lida no texto do estúdio ("slowing the clock to a crawl" + "dynamic trading UI").
- **Por que ganhou:**
  - Junta cena real com **dado na tela**: o número aparece em cima do lance, no momento certo.
  - Para o dono, é a prova sem promessa. Ele vê o que acontece com o cliente dele (3 segundos no perfil, mensagem sem resposta) desenhado em cima de uma cena real.
- **Técnica que copiamos:**
  - **Composição:** vídeo de banco real (balcão, celular na mão, cliente indo embora) com **anotações de interface**: uma linha fina que nasce do objeto, um rótulo em mono e um número em Anton amarelo.
  - **Ritmo:** **speed ramp**. A cena desacelera (câmera lenta) no instante do problema, a anotação desenha e a cena volta à velocidade normal.
  - **Transição:** motion blur direcional na saída da câmera lenta.
- **Como entra no motor:**
  - **Anotação:** SVG com `stroke-dasharray`/`stroke-dashoffset` animado em `render(t)`, mais `.tag`/`.mono` para o rótulo e `.badge .n` para o número.
  - **Speed ramp:** no corte do clipe de banco antes do palco, com `setpts` do ffmpeg por trecho (por exemplo `setpts=2.5*PTS` no meio segundo do impacto).
  - **Blur:** o filtro `#mb` (feGaussianBlur direcional) que já existe.
  - Tudo em amarelo e branco sobre o vídeo, com vinheta (`#vig`) para dar leitura.

### 3. BUCK: Microsoft + Intel, campanha global B2B (Estados Unidos)
- **Link:** https://buck.co/work/microsoft-intel-global-b2b-campaign
- **Capturas:** `referencias/2026-11-09/22-buck-microsoft-intel-b2b.jpg` e `05-buck.jpg`.
- **Reconhecimento:**
  - BUCK é um estúdio de Los Angeles e Nova York, com escritórios em outros países.
  - A página diz que a campanha era para **pequenas e médias empresas** e que gerou "milhões de ativações". O número é do estúdio e não foi conferido.
- **Por que ganhou:** foi feita para o mesmo público, o dono de pequeno negócio, e passa **confiança**:
  - frase curta e direta;
  - produto real no contexto;
  - nenhum truque visual que distraia.
  - Equilibra a energia das outras duas.
- **Técnica que copiamos:**
  - **Composição:** manchete de 3 linhas curtas alinhada à esquerda (Manrope 800) e, ao lado, a tela real inclinada (cerca de -12°) com moldura de luz atrás.
  - **Ritmo:** mais lento, um movimento por vez: a manchete entra linha a linha e depois a tela desliza com leve parallax. Fica nas cenas de prova e de CTA (de 18 s a 28 s).
- **Como entra no motor:**
  - `.phone` (o celular com o perfil do Instagram que já existe) com `rotate(-12deg)` e `translate` em parallax dentro de `render(t)`;
  - a manchete em `.layer` com reveal por linha (o mesmo `clip-path` da escolhida 1);
  - a moldura de luz no `box-shadow` amarelo que o `.phone` já usa;
  - SFX "whoosh" suave na entrada do celular.

### Qual cena do Reels copia qual referência
| Trecho do Reels de 30 s | Referência | Técnica |
|---|---|---|
| Gancho 0 a 3 s | Dumbar DEMO | Palavra gigante por máscara, cortes secos no beat |
| Problema 3 a 12 s | MvsM Robinhood | Banco real em câmera lenta com anotação de dado em amarelo |
| Virada 12 a 18 s | Dumbar DEMO | Card amarelo (cards de impacto do §5) com uma palavra que ocupa a largura |
| Prova e CTA 18 a 30 s | BUCK Microsoft + Intel | Manchete de 3 linhas e celular inclinado com parallax, ritmo calmo de confiança |

A legenda palavra por palavra (`#cap`), o light leak âmbar, o grão e o @lindsonalmeida_ continuam como estão em `ESTRATEGIA.md` §5.

## Comparadas e descartadas
| Referência | País | Link | Captura | Por que não |
|---|---|---|---|---|
| Behance: "instagram reels motion" e "kinetic typography reels" | — | behance.net/search/projects/… | `01-…`, `02-behance-…` | **Bloqueado (HTTP 403, verificação de robô).** Não foi contornado |
| Motion Array: templates de kinetic typography | — | motionarray.com/browse/… | `09-motionarray-kinetic.jpg` | **Bloqueado (verificação de segurança Cloudflare).** Não foi contornado |
| Godly | — | godly.website | — | O endereço não respondeu (DNS) |
| Awwwards: animação | — | awwwards.com/websites/animation | — | Erro 502 na hora da captura |
| HOLOGRAPHIK®: tipografia cinética com palavra repetida e virada de página (shot popular, cerca de 232 mil views) | Croácia | dribbble.com/holographik | `03-dribbble-kinetic-typography.jpg`, `16-dribbble-holographik.jpg` | Lindo, mas a palavra repetida vira textura e pede leitura lenta. Fica só como fundo de marquee (`.marq` já existe) |
| LANARS: "Rethink / Remake" em contorno repetido | Ucrânia (não conferido) | dribbble.com/search/kinetic-typography | `03-dribbble-kinetic-typography.jpg` | Efeito de template comum, sem ideia de marca |
| Studio Dumbar: Utah Jazz 25-26 | Holanda | studiodumbar.com/work/utah-jazz-25-26 | `27-studiodumbar-utah-jazz.jpg` | Sistema esportivo em roxo e montanha. Do Dumbar ficou o DEMO, mais próximo do formato |
| ManvsMachine: home (Moncler, Canva, OpenAI) | Reino Unido | mvsm.com | `06-manvsmachine.jpg` | Projetos de moda e 3D caro, fora da realidade do dono local |
| BUCK: TurboTax, loja-conceito | Estados Unidos | buck.co/work/turbotax-flagship-store-digital-content | `21-buck-turbotax-digital-content.jpg` | Conteúdo para telas horizontais de loja. A campanha B2B fala mais com o nosso público |
| Giant Ant: "Mark Eting" (Optimizely) | Canadá | giantant.ca | `08-giantant.jpg` | Tema de marketing, mas é ilustração surreal. A persona confia em imagem real, não em desenho |
| Ordinary Folk: reels e Google Doodles | Canadá (Vancouver) | ordinaryfolk.co/work | `07-ordinaryfolk.jpg`, `24-ordinaryfolk-work.jpg` | Animação de personagem lúdica, longe de "estrategista sério" |
| DixonBaxi | Reino Unido | dixonbaxi.com | `13-dixonbaxi.jpg` | Identidade forte, mas sem peça vertical de motion visível para copiar |
| LOBO: Xbox e outros filmes | Brasil (São Paulo) | lobo.cx | `14-lobo.jpg` | Live-action de grande produção, que não se reproduz em HTML. Serve só de referência para o light leak âmbar quente |
| Vimeo Staff Picks | Estados Unidos | vimeo.com/channels/staffpicks | `04-vimeo-staffpicks.jpg` | Curtas-metragens, não formato social de 30 s |
| Juan John: Reels da barbearia Rufianes | não conferido | dribbble.com/shots/27833847 | `18-dribbble-rufianes-barbershop-reel.jpg` | É negócio local, mas é só vídeo bruto, sem tipografia nem marca. Nível abaixo do pedido |
| Grazie Guevara: Metanoia Wellness | não conferido | dribbble.com/shots/27620047 | `19-dribbble-metanoia-content.jpg` | Edição comum de conteúdo, sem técnica nova |
| Natasha: Canderel Social Motion | não conferido | dribbble.com/shots/27737739 | `20-dribbble-canderel-social-motion.jpg` | Mockup de feed com cara de template |
| Brand New (UnderConsideration) | Estados Unidos | underconsideration.com/brandnew | `11-brandnew.jpg` | Blog de identidade, sem motion vertical |
| Savee | — | savee.it | `15-savee.jpg` | Pede login para ver os quadros |

## Países cobertos
- Holanda;
- Reino Unido;
- Estados Unidos;
- Canadá;
- Croácia;
- Brasil;
- Ucrânia (não conferido).

São 7 países e mais de 15 referências olhadas.

## Conferência antes de renderizar
- Ao lado do DEMO, do Robinhood e da campanha da BUCK, o quadro do Reels aguenta a comparação? Se parecer template de CapCut, refazer.
- O dono entende a frase em 1 segundo, sem som?
- O amarelo está só na palavra-chave e nos cards? A identidade não muda.
