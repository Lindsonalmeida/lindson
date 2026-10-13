Identidade visual de **Lindson Almeida**: conteudista há 14 anos, assessor político e profissional de marketing digital em São Luís, Maranhão. Ela nasceu no mini site da bio (`lindsonalmeida.github.io/lindson/links`) e nos Stories de venda desse mini site, e serve para tudo o que for publicado no Instagram.

## Essência

**Comunicação que mobiliza e engaja.** A marca se comporta como um sinal no ar: parte de uma pessoa, se espalha e conecta gente. Três ideias guiam cada peça:

- **No ar.** Tudo parece estar acontecendo agora: visor de câmera com REC, timecode correndo, bastidores em vídeo.
- **Sinal que se espalha.** Ondas saindo da foto e uma rede de pontos conectados ao fundo mostram alcance e mobilização.
- **Território.** O Maranhão aparece como fato, não como enfeite: "São Luís · Maranhão", coordenadas `2°31′S 44°18′W`, a sigla MA.

Autoridade vem de prova concreta, nunca de adjetivo: "14 anos de conteúdo", "9,1 mil seguidores", selo de verificado, rosto real.

## Voz e escrita

- Escreva em português do Brasil, falando com **você** ("Sua bio merece um upgrade"). Lindson fala em primeira pessoa ("Agora eu levo isso para a sua bio").
- Frases curtas, verbo na frente, sem jargão. Exemplos reais: "Toque em 'Quero um mini site'", "Envie a mensagem que já vem pronta", "Eu te respondo e a gente começa o seu."
- Títulos têm uma **virada**: a primeira parte em `fg`, a palavra que muda tudo em `sun` ou `signal` ("Sua bio é uma lista de links. **Ou é a sua vitrine.**").
- Use números exatos e com unidade: "14 anos", "9,1 mil", "3 toques", "12 segundos". Vírgula decimal, como no Brasil.
- Chamadas para ação dizem o gesto: "Responda este story com 'EU QUERO'", "Toque no link abaixo".
- Emoji não entra nas peças gráficas. Na legenda e na bio, no máximo um por linha.
- Caixa alta só nos rótulos em mono (`story-label`, `label`).

## Cor

A marca é **escura por padrão**: `ink` é o fundo de tudo.

- Texto principal em `fg`; apoio em `lead` (Stories) ou `muted` (tela).
- `signal` é a assinatura: anel da foto, ícones, palavras-chave, foco. Use-o com generosidade em traços e pouco em áreas.
- `sun` é a ação. **Um único elemento `sun` por tela**: o botão do WhatsApp, o selo NOVO ou a palavra de virada. Texto sobre `sun` sempre em `sun-ink`.
- `violet` só aparece junto de `signal` e `sun` no botão "Quero um mini site" e no passo do meio dos tutoriais.
- `rec` é só a luz do REC e o risco do "antes".
- A única peça de fundo claro é o Story "Vitrine": fundo inteiro `sun`, texto `sun-ink`, cartões `ink`. Use esse modo para quebrar a sequência, no máximo uma peça em cada quatro.
- Superfícies são de vidro: `panel` com borda `line` e desfoque de fundo, nunca cinza chapado.

## Tipografia

Três famílias do Google Fonts, cada uma com um papel:

- **Bricolage Grotesque** (`display`), peso 800, entrelinha 0,95 e espaçamento negativo, para títulos e números. É a voz alta da marca.
- **Manrope** (`body`) para texto corrido, títulos de link e etiquetas.
- **JetBrains Mono** (`mono`) em caixa alta e espaçada para rótulos, REC, timecode, coordenadas e paginação. É o "instrumento técnico" da marca.

Nos Stories, use `story-title` para títulos e `story-lead` para a frase de apoio; no mini site, `site-name`, `link-title` e `caption`. Nunca use mais de duas famílias na mesma linha.

## Grafismos

Use estes elementos, sempre em traço fino e cor da marca, nunca como ilustração:

- **Rede de nós:** pontos ligados por linhas `signal` em baixa opacidade; cerca de 1 em cada 10 pontos em `sun`. Fica atrás de tudo.
- **Ondas de sinal:** três anéis `signal` saindo da foto de perfil.
- **Visor de câmera:** quatro cantos de enquadramento em `fg` a 45–60%, "● REC" com a luz `rec` e um timecode em `mono`.
- **Brilho radial:** um halo `signal` saindo de um canto da peça; um halo `sun` fraco no canto oposto, se precisar.
- **Selo de verificado:** estrela azul `signal` com check branco, ao lado do nome.

## Fotografia e vídeo

- Rosto real e olhar para a câmera. O retrato de estúdio em fundo cinza é a foto de autoridade; a foto de perfil é o recorte dele em círculo com anel `signal`.
- Vídeo de bastidores (estúdio de madeira com luz âmbar) entra como fundo, coberto por um véu `ink` entre 30% no topo e 82% na base, para o texto continuar legível.
- Em peças de autoridade, a foto ocupa o topo inteiro e se dissolve em `ink` de baixo para cima.

## Layout

- **Story 1080×1920:** margem lateral `story-margin`; nada de texto nos `story-safe` de cima e de baixo. O título começa logo abaixo da faixa segura de cima; a chamada para ação termina acima da faixa de baixo.
- **Post 1080×1350:** mesma margem, paginação em `mono` no canto superior ("02 / 03").
- **Mini site:** coluna única de até 480px, margem `space-gutter`, blocos separados por `space-section`, links empilhados com `space-stack`.
- Alinhe à esquerda por padrão; centralize só peças de impacto (Story "Vitrine").
- Mockups de celular entram inclinados de 4° a 8°, com `glow-signal`.

## Movimento

Movimento lento e contínuo, como algo no ar: a rede de nós deriva, as ondas pulsam a cada 3,6 s, o REC pisca, a borda do botão "Quero um mini site" gira em 4 s. Quem pede menos movimento (`prefers-reduced-motion`) vê tudo parado e o vídeo pausado. Som só depois de um toque ("Ativar som").

## Iconografia

Ícones de traço feitos à mão em SVG, 24×24, traço 1,8 a 2, pontas e cantos arredondados, cor `signal` dentro de um quadro `radius-icon` com fundo `signal` a 12%. O conjunto atual: WhatsApp, Instagram, LinkedIn, Threads, conexões (projetos), alvo (Núcleo SLZ), edifício público (Meu Vereador 5.0), celular com estrela (mini site), seta de avanço, pino de mapa, alto-falante. Não há logotipo: o nome "Lindson Almeida" em `display` 800 com o selo de verificado faz esse papel.

## O que não fazer

- Fundo branco ou cinza claro (a exceção é o fundo `sun` do Story "Vitrine").
- Dois botões `sun` na mesma tela.
- Branco sobre `sun`.
- Gradiente azul-roxo em áreas grandes; o gradiente só existe na borda do botão do mini site e no destaque "3 toques".
- Emoji como ícone, fotos de banco de imagem, mascotes.
- Texto dentro das faixas seguras do Story.
