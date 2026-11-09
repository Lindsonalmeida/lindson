# Central de Comando · pesquisa premium e template

## v2 (09/11/2026, conta Leandro): "não quero que pareça vibe code"
Pedido do Lindson: "quero um template único e tecnológico, com imagens, camadas, vídeos, rolagem etc." Também lidos no privado: `web-design-premium/README.md` (os 7 estilos, a anatomia do hero e os sinais de amadorismo), `edit-ia-pro/README.md` §5 e `motion-animacao-vfx/` (#137 HUD "● REC", #152 light leak âmbar, #35 grão, #25 parallax 2.5D, #52 tipografia gigante).

### Sinais de "vibe code" da v1, todos tirados
| Sinal na v1 | Na v2 |
|---|---|
| Cartões iguais arredondados em grade (KPIs 4×, tudo `border-radius:18px`) | Sem cartão: fios finos, quadro de partidas na fila, chassi com canto chanfrado e parafusos, módulos de rack na equipe |
| Gradiente escuro genérico com brilho radial | Vídeo real em loop com tratamento âmbar, luz vazando (#152), grão de filme (#35) e linhas de varredura |
| Ícones de linha de biblioteca | Nenhum ícone de pacote: teclas com código gravado (RLS, CAR, STR…) e LED, como no OP-1 |
| Tudo do mesmo tamanho, sem hierarquia | Títulos Anton de 104 a 184 px, números de 132 px, número da seção vazado gigante; o resto em Manrope e mono |
| Nenhuma imagem real | Artes reais dos painéis dos clientes, entregas da fila em miniatura e os motions do Leo com prévia ao passar o dedo |
| Layout de "dashboard template" (sidebar + topbar + grade, telas por hash) | Uma página só que conta a operação: Comando → Fila ao vivo → Resultados → Equipe → Contas, com trilho numerado e HUD |
| Chips em pílula colorida | Seletores de equipamento com LED e faixa inclinada em marquee com os números reais |

### Referências (capturas em `v2/referencias/`: `-1` abertura, `-2` e `-3` depois de rolar)
| # | Referência | País | Reconhecimento | Técnica |
|---|---|---|---|---|
| 1 | **Igloo Inc** (igloo.inc), estúdio **abeto** | EUA (cliente) · estúdio não conferido | **Awwwards Site of the Year e Developer SOTY 2024** (conferido) | camadas em profundidade, HUD mono sobre a cena, rolagem que conduz (o WebGL não renderizou no robô) |
| 2 | **Teenage Engineering · OP-1 field** | Suécia | OP-1: Design S Award 2012 (conferido) | teclas físicas com código, cor por grupo, chassi de equipamento |
| 3 | **Lando Norris** · OFF+BRAND | Reino Unido | **Awwwards SOTD 18/11/2025** (conferido) | tipografia gigante sobre a cena, revelar por rolagem, uma cor elétrica |
| 4 | basement.studio | Argentina | Awwwards SOTD 25/04/2025 (conferido) | preto puro, HUD "online", wireframe |
| 5 | rabbit r1 | EUA | Red Dot e iF 2025 (selos na captura) | um botão físico para falar |
| 6 | Apple Vision Pro | EUA | não conferido | vídeo e texto que trocam na rolagem |
| 7 | Vercel Ship | EUA | não conferido | palco escuro com vídeo, agenda em grade fina |
| 8 | Linear | EUA | não conferido | rótulos mono, interface como produto |
| 9 | Nothing Phone (3) | Reino Unido | não conferido (abriu o seletor de loja) | pontos e tipografia técnica |
| 10 | Arc | EUA | não conferido | página de despedida; serviu só de contraste |

4 países: EUA, Suécia, Reino Unido e Argentina.

### As 3 escolhidas e o que se copiou (técnica e composição, nunca o layout)
1. **Igloo Inc / abeto:** a cena em **planos de profundidade** (vídeo ao fundo, luz, varredura, mira, HUD e título em z diferentes) que se mexem com o mouse e com a rolagem, e o HUD mono como camada de informação.
2. **Teenage Engineering OP-1:** as funções viraram **teclas de equipamento** com código gravado, LED e cor por grupo (amarelo conteúdo, branco sites, cinza documentos, laranja acompanhar). As 3 mais pedidas são teclas largas. Os clientes são seletores com LED.
3. **Lando Norris / OFF+BRAND:** **tipografia gigante** sobre o vídeo, palavra-chave em caixa de cor, título que sobe linha a linha e seções que **revelam por máscara** na rolagem, com uma cor só (o amarelo #F5C518 da marca).

**Vídeo de fundo:** Mixkit #42343 (desktop, cidade à noite vista do alto) e #49878 (celular, vertical), licença livre do Mixkit, tratados em âmbar, sem som, 10 s, mp4 e webm com pôster (`v2/media/`, de 0,5 a 1 MB cada).

### Descartadas na v2
- **Apple Vision Pro e Nothing:** fundo claro e produto físico que não temos.
- **Arc:** a página virou despedida, sem a técnica que interessava.
- **WebGL de verdade (Igloo):** pesado para o celular. Ficou o efeito de camadas em CSS, sem biblioteca.

---

## v1 (09/11/2026)

**Persona:** o Lindson, dono da agência, 1 pessoa decidindo tudo, quase sempre no celular, entre gravação, cliente e WhatsApp. Dor: perde tempo trocando de conta, recomeça e repete pedidos. Confia em algo que pareça **ferramenta real** (não página de cartões), que responda rápido e mostre o que está parado. Afasta: digitar muito, telas soltas, número inventado.
Teste dos 3 segundos no celular: um botão grande para falar, os clientes e as funções em teclas, e a barra "Enviar".

Também lidos: privado `dados/agencia/referencias/web-design-premium/` (estilo "3D / tech" e "SaaS clean"), `motion-animacao-vfx/` (#137 HUD "● REC") e `edit-ia-pro/` (HUD com rótulo mono "● EDITANDO AO VIVO" e contadores).

## Referências (capturas em `referencias/`, abertura `-1` e depois de rolar `-2`, em 09/11/2026)
| # | Referência | País | Reconhecimento | O que serve |
|---|---|---|---|---|
| 1 | **Linear** (linear.app) | EUA | referência de tendência em interface de produto; prêmio **não conferido** | escuro, grade fina, rótulos mono, interface como produto |
| 2 | **Teenage Engineering · OP-1 field** | Suécia | OP-1 original: Design S Award 2012 (conferido na busca); Red Dot do field **não conferido** | teclas grandes de hardware com ícone e código, rótulos técnicos |
| 3 | **rabbit r1** (rabbit.tech) | EUA (design com a Teenage Engineering) | **Red Dot 2025 e iF Design Award 2025** (selos visíveis na captura) | um botão físico para falar, objeto único e forte |
| 4 | basement.studio | Argentina | **Awwwards SOTD** (25/04/2025, conferido na busca) | HUD mono, indicador "online", preto puro |
| 5 | Raycast | Reino Unido | não conferido | comando rápido, atalho para tudo |
| 6 | ElevenLabs · agentes de voz | EUA / Reino Unido | não conferido | bolha de voz, "Talk to an agent" |
| 7 | Vercel · Observability | EUA | não conferido | "mission control", gráfico ao vivo |
| 8 | Grafana | Suécia / EUA | não conferido | painel de observabilidade, "Ask AI" |
| 9 | Warp | EUA | não conferido | grade de pontos com status, rótulos mono |
| 10 | Nothing | Reino Unido | não conferido | tipografia de pontos, tecnologia simples |
| 11 | Resend | EUA | não conferido | escuro editorial, 3D sutil |

4 países (EUA, Suécia, Argentina, Reino Unido).

## As 3 escolhidas e o que se copiou (composição, nunca marca, texto ou imagem)
1. **Linear:** fundo preto com **grade fina** que some para baixo, brilho sutil no topo, rótulos em **JetBrains Mono** caixa-alta espaçada e o menu lateral do sistema.
2. **Teenage Engineering OP-1:** as funções viraram **teclas** com ícone, nome curto e código (F01…F16), com relevo e afundamento no toque; grade de 6 no computador e 3 no celular.
3. **rabbit r1:** **um botão só para falar**, grande, redondo, na cor de destaque (amarelo #F5C518), que vira vermelho "● GRAVANDO" com ondas, mais o HUD "● AO VIVO" com relógio (que conversa com o #137 "● REC" e o "● EDITANDO AO VIVO" do EDIT.IA PRO).

Marca do Lindson: preto #0B0B0B, amarelo #F5C518 só em botões, palavras-chave e números de ação; Anton nos títulos, Manrope no texto, JetBrains Mono nos rótulos.

## Descartadas e por quê
- **ElevenLabs, Grafana, Warp (abertura clara):** fundo claro foge da marca preto e amarelo.
- **Vercel e Resend:** bonitos, mas é página de venda, não tela de trabalho.
- **Nothing:** a tipografia de pontos não lê bem em 390 px.
- **WebGL e 3D pesado (basement, Resend):** o Lindson usa no celular; fica só o HUD mono.
- **Raycast:** a paleta de comandos depende de teclado; no celular, teclas grandes funcionam melhor.
