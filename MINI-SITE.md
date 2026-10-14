# MINI SITE

Página de links da bio do Instagram de **Lindson Almeida** (@lindsonalmeida_).

**No ar:** https://lindsonalmeida.github.io/lindson/links/

## O que tem na página

- Foto, nome com selo de verificado e as funções: Conteudista, Assessor Político e Marketing Digital
- Frase "Comunicação que mobiliza e engaja. O Maranhão é o meu território."
- Números: 14 anos de conteúdo, 9,1 mil seguidores e MA
- Vídeo de fundo com bastidores de gravação, visor de câmera (REC e timecode) e rede de pontos animada
- Trilha de rock instrumental original que só toca quando o visitante aperta "Ativar som"
- **Fale comigo no WhatsApp** (botão laranja): abre a conversa com +55 98 98562-1808, sem mensagem
- **Quero um mini site** (botão com borda animada): abre o WhatsApp com a mensagem
  "Oi, Lindson! Quero ter um mini site no link da minha bio"
- Redes: Instagram, LinkedIn e Threads
- Projetos: Alkantara Connections, Núcleo SLZ e Meu Vereador 5.0

## Arquivos

| Arquivo | O que é |
|---|---|
| `links/index.html` | A página inteira: textos, links, cores e animações |
| `links/avatar.jpg` | Foto de perfil |
| `links/bg.mp4` | Vídeo de fundo (12 s em loop, sem som) |
| `links/bg-poster.jpg` | Imagem mostrada enquanto o vídeo carrega |
| `links/rock.mp3` | Trilha sonora (48 s em loop) |
| `divulgacao/story-1-antes-depois.png` | Story 1: antes × depois |
| `divulgacao/story-2-vitrine.png` | Story 2: vitrine |
| `divulgacao/story-3-autoridade.png` | Story 3: autoridade |
| `divulgacao/story-4-como-pedir.png` | Story 4: como pedir em 3 toques |

## Identidade visual

O branding book completo está em `branding/` (`README.md`, `instagram.md`, `tokens.json` e os componentes). `branding/modelos/stories.html` é o arquivo-fonte dos 4 Stories, para criar novas peças no mesmo estilo.

## Brand book

Apresentação 16:9 com 16 slides da identidade visual (manifesto, pilares, voz, assinatura, cores, tipografia, grafismos, fotografia, Stories, mini site e usos).

- Arquivos: `branding/brand-book/` (`index.html` e as imagens em `img/`)
- No ar: https://lindsonalmeida.github.io/lindson/branding/brand-book/
- Prévia no Claude: https://claude.ai/artifact/L1959UErxHBmmtqe7gwKBS

## Identidade 01

"Identidade 01" é o nome da identidade visual do brand book (fundo ink, signal, sun, Bricolage Grotesque, Manrope e JetBrains Mono, visor de câmera e rede de nós). Conteúdos feitos nela ficam em `conteudo/identidade-01/`, cada um com os PNGs e a pasta `fonte/` para reeditar.

- `carrossel-03-os-5-pecados-do-growth/`: base Sun (capa e fecho) + Paper (ranking).
- `carrossel-02-regra-do-pesquisador/`: carrossel de feed 1080×1350, 5 slides.
- `carrossel-01-sequencia-do-iniciante/`: carrossel de feed 1080×1350, 5 slides. Cores de status só neste tipo de conteúdo: laranja `#FF8A3D` (aviso) e verde `#2FD07A` (tudo certo).

## Regras de conteúdo

- **Nunca usar a mesma foto duas vezes.** O controle fica em `conteudo/fotos/REGISTRO.md`: escolha só fotos de `conteudo/fotos/disponiveis/` e, ao usar, mova para `usadas/` e anote onde entrou.
- **Acabaram as fotos? Peça novas ao Lindson** antes de produzir, em vez de repetir.
- Tire nomes e marcas visíveis das fotos (boné, carro, roupas) antes de publicar.
- **Feed variado.** Não repita a mesma fórmula de um carrossel para o outro: alterne o tipo de capa e a cor dominante, sempre dentro da Identidade 01 (cores, fontes e grafismos do brand book). Rodízio de bases:
  - **Ink** (escuro, azul e âmbar): base padrão. Usada nos carrosséis 01 e 02.
  - **Paper** (fundo claro `#EEF2FF`, texto ink, destaque signal).
  - **Signal** (fundo azul `#4C8DFF`, texto ink e paper).
  - **Sun** (fundo âmbar `#FFB547`, texto `#1A1205`, cartões ink).
  - **Foto cheia** (foto ocupando a capa toda, texto sobre véu).
  Tipos de capa para alternar: foto + título embaixo (01 e 02), só tipografia gigante, número enorme, tela dividida foto/texto, pergunta em destaque, citação.

## Agência (recomeço)

- `agencia/ofertas/instagram-que-vende-90-dias.md`: oferta principal (Hormozi Squad), com pendências.
- `agencia/app/recomeco90.html`: fonte do app gamificado "Recomeço 90" (missões, jornada, caixa com cálculo automático e cartões de aprendizado). No ar como artefato: https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N (progresso salvo na conta do Lindson, capacidade `db`).

## Como publicar uma mudança

A página é servida pelo GitHub Pages a partir do branch `claude/global-agent-installation-vdyowf`.
Qualquer mudança enviada para esse branch entra no ar em 1 ou 2 minutos.

Não renomeie nem mova a pasta `links/`: o endereço da bio depende dela.

## Versões

Versão 1 (13/10/2026): commit `1c459cd` do branch `claude/global-agent-installation-vdyowf`.
