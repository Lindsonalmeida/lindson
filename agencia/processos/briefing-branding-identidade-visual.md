# Briefing de Branding e Identidade Visual
> Pesquisa de referência para o Claude Code criar as identidades visuais (e as apresentações delas) das nossas marcas.
> Data: 21/11/2026

---

## 0. Como usar este arquivo (instrução direta pro Claude Code)

Você vai criar **identidades visuais completas + a apresentação de cada uma**, no padrão dos melhores cases do Behance. Para cada marca:

1. Primeiro monte a **plataforma de marca** (seção 2) — sem isso, não desenhe nada.
2. Depois crie o **sistema visual** (seção 3) e salve os tokens em `brand.json`.
3. Por fim gere a **apresentação** (seção 4) como página HTML com slides 16:9 (1920×1080), exportável em PNG pra postar no Behance/Instagram.
4. Aplique o **checklist de qualidade** (seção 7) antes de entregar.

**Regras fixas:**
- Marca pessoal **Lindson Almeida**: cores **preto e amarelo**, seguindo a identidade que já existe no repositório (`Lindsonalmeida/CentralLindsonALmeida` e o repo `lindson`). Não inventar outra. Usar as fotos de **terno**, nunca as da fazenda.
- Antes de criar qualquer coisa, procurar materiais/logos/fotos existentes em **todos os repositórios GitHub do Lindson**.
- Salvar os resultados no repositório geral (`CentralLindsonALmeida`), uma pasta por marca.

**Marcas candidatas** (sites em pages.dev): Lindson Almeida, Orégano Turbo, Desentupidora SF, Dra. Jaci Cunha, Real Time SLZ, Tribuna 98, WF Celulares, Rafael Imports.

---

## 1. O processo de branding (ordem certa)

Todo bom processo segue a mesma lógica: **estratégia → expressão verbal → expressão visual → aplicação → gestão**. O erro mais comum é pular direto pro logo.

| Etapa | O que sai dela |
|---|---|
| 1. Diagnóstico | Público, concorrentes, o que a marca já tem, o que funciona e o que não funciona |
| 2. Plataforma de marca | Propósito, posicionamento, valores, personalidade/arquétipo, promessa |
| 3. Identidade verbal | Tom de voz, tagline, pilares de mensagem, palavras que usa / evita |
| 4. Direção visual | Moodboard, conceito, palavras-chave visuais |
| 5. Identidade visual | Logo + variações, cores, tipografia, grafismos, ícones, fotografia |
| 6. Aplicações | Mockups nos pontos de contato reais do negócio |
| 7. Manual / brand book | Regras de uso (área de proteção, tamanho mínimo, usos proibidos) |
| 8. Gestão | Consistência no dia a dia, templates, revisão periódica |

O Sebrae define branding como a gestão da identidade da empresa rumo aos objetivos do negócio, começando pelo propósito e seguindo para o posicionamento. Também é bom traduzir palavras vagas do cliente ("moderno", "confiável") em critérios específicos antes do primeiro conceito — palavras amplas demais não guiam decisão de design (Smashing Magazine, 2026).

---

## 2. Plataforma de marca (preencher para cada marca)

```yaml
marca: ""
segmento: ""
cidade/praça: ""
proposito: ""            # por que a marca existe (além de vender)
publico:
  quem: ""
  dores: []
  desejos: []
  linguagem_que_usam: [] # palavras reais dos clientes
concorrentes: []          # 3 a 5, com o que cada um comunica
posicionamento: "[público] escolhe [marca] para [benefício], porque [crença/prova]"
diferencial: ""
valores: []               # 3 a 5
arquetipo: ""             # ex.: Herói, Sábio, Cuidador, Rebelde, Governante, Explorador...
personalidade: []         # 3 a 5 adjetivos
tom_de_voz:
  e: []                   # ex.: direto, caloroso
  nao_e: []               # ex.: arrogante, técnico demais
tagline: ""
palavras_chave_visuais: [] # 3 a 5 que vão guiar o design
```

**Arquétipos** (baseados nos conceitos de Jung) ajudam a definir personalidade e voz de forma rápida e coerente do texto ao visual.

---

## 3. O sistema visual (o que toda identidade precisa ter)

### 3.1 Logo
- **Principal** (horizontal ou empilhado) + **secundária** + **símbolo/ícone** isolado + **versão só tipografia**.
- Versões: colorida, monocromática, negativa (sobre fundo escuro), positiva (sobre fundo claro).
- **Área de proteção** definida por proporção de um elemento do próprio logo (ex.: altura de uma letra), não por medida fixa.
- **Tamanho mínimo** em px (digital) e mm (impresso). Testar como favicon 16–32 px.
- **Usos incorretos**: esticar, girar, trocar cor, sombra, contorno, fundo poluído, invadir a área de proteção.
- Entregar em **SVG** (idealmente com animação CSS opcional), PNG transparente e versões para avatar redondo.

### 3.2 Cores
- 1 cor principal + 1–2 de apoio + neutros. Dar **nome** a cada cor (ex.: a Cajuá usa "Folha", "Areia", "Raiz", "Caramelo", "Verão", "Mar").
- Para cada cor: HEX, RGB, CMYK e proporção de uso (ex.: 60/30/10).
- Checar contraste (WCAG AA) das combinações texto/fundo.

### 3.3 Tipografia
- Principal (títulos), secundária (texto), e opcional de apoio/destaque.
- Mostrar hierarquia: H1, H2, corpo, legenda, com tamanhos e pesos.
- Preferir fontes com licença livre (Google Fonts) para uso web.

### 3.4 Elementos de apoio
- **Grafismos/padrões** derivados do logo ou do conceito.
- **Ícones/ilustrações** num estilo único (a Cajuá usa ilustrações de traço de objetos brasileiros: cadeira de praia, filtro de barro, tucano, onça, frutas).
- **Selos/stickers** circulares para redes sociais.
- **Direção de fotografia**: tipo de luz, enquadramento, o que mostrar e o que evitar.
- **Grid** e regras de espaço em branco para posts e páginas.

### 3.5 Tokens (`brand.json`)
```json
{
  "name": "",
  "colors": { "primary": "#", "secondary": "#", "accent": "#", "dark": "#", "light": "#" },
  "fonts": { "display": "", "body": "", "accent": "" },
  "logo": { "primary": "logo-primary.svg", "symbol": "symbol.svg", "mono": "logo-mono.svg", "negative": "logo-negative.svg" },
  "clearspace": "1x altura da letra X",
  "minSize": { "px": 24, "mm": 15 },
  "radius": 24,
  "voice": { "is": [], "isNot": [] }
}
```

---

## 4. Como apresentar a identidade (formato dos cases do Behance)

### 4.1 Anatomia do case Cajuá (aberto e analisado)
14 imagens, todas em **16:9 (1401×788)**, cada slide uma ideia:

1. **Capa** — fundo na cor principal + textura sutil, "IDENTIDADE VISUAL" pequeno à esquerda, logo grande à direita.
2. **Moodboard** — mosaico de fotos com as referências culturais da marca.
3. **Conceito** — texto à esquerda ("O Conceito:") explicando o significado de cada elemento + foto grande à direita.
4. **Paleta** — colunas verticais de cor de ponta a ponta, com nome e códigos embaixo.
5. **Logo hero** — logo principal grande e centralizado no fundo da marca.
6. **Variações** — grade 2×2 de cards arredondados, cada um num fundo de cor diferente com uma versão do logo.
7. **Família tipográfica** — cards "Aa" com etiqueta (principal / secundária / apoio) e nome da fonte.
8. **Ilustrações/ícones** — biblioteca de grafismos em traço sobre fundo de cor sólida.
9–12. **Mockups** — ecobag (2 versões lado a lado), caneca, caderno, em cenário real (grama, areia, mesa com plantas).
13. **Social/campanha** — foto forte + moldura arredondada + frase da marca + selos/stickers nos cantos.
14. **Encerramento** — logo cercado pelos ícones em cards coloridos, fundo kraft.

### 4.2 Estrutura recomendada (consenso das fontes)
Combinando o case acima com os guias de apresentação de marca:

1. Capa
2. Contexto / desafio (o que a marca precisava)
3. Pesquisa e estratégia resumida (público, posicionamento, palavras-chave)
4. Moodboard
5. Conceito (o "porquê" de cada escolha — isso faz o design parecer intencional, não aleatório)
6. Construção do logo (grid, geometria, rascunho → final)
7. Logo hero
8. Variações e versões
9. Área de proteção e tamanho mínimo
10. Usos incorretos
11. Paleta de cores
12. Tipografia
13. Grafismos, ícones, padrões
14. Direção de fotografia
15. Aplicações / mockups (os mais relevantes pro negócio)
16. Redes sociais (feed, stories, destaque, avatar)
17. Encerramento / assinatura

**Regras de mockup:**
- Só mostrar aplicações que fazem sentido pro negócio real. Ex.: pizzaria → caixa de pizza, fachada, cardápio, uniforme, sacola de delivery, app/iFood; advogada/médica → cartão, papelaria, fachada de consultório, receituário, perfil do Instagram.
- Contar uma "jornada": rua (fachada/outdoor) → mão do cliente (embalagem, cartão) → dia a dia (caneca, sacola) → celular (posts).
- Ajustar cores e luz dos mockups ao clima da marca; misturar mockups grandes (full) e pequenos (grade).

### 4.3 Formatos de entrega da apresentação
| Formato | Uso |
|---|---|
| Slides 16:9 (1920×1080) em HTML → PNG | Case no Behance, PDF pro cliente |
| Carrossel 4:5 (1080×1350) | Mostrar a identidade no Instagram |
| Brand book em página web | Manual vivo com link, busca e download dos arquivos — hoje considerado o melhor formato de manual |
| PDF resumo de 1–2 páginas | Ficha rápida da marca para o cliente/parceiros |

---

## 5. Tendências 2026 (usar com critério, não por moda)

- **Sistemas flexíveis/responsivos**: logo que se adapta (versão completa → símbolo → favicon) e identidade pensada como sistema modular.
- **Identidade cinética**: logo e grafismos pensados pra se mover (SVG animado, vinhetas de Reels).
- **Folk / artesanal / regional**: tipografia rústica e marcas folclóricas simplificadas — funciona muito bem pra comida, bebida, hospitalidade e lifestyle (ótimo pro Orégano Turbo).
- **Maximalismo e tipografia expressiva**: formas inesperadas, assimetria, fontes com personalidade.
- **Traço à mão / anti-design**: escrita "ingênua", imperfeição intencional (para marcas jovens e ousadas).
- **Storytelling autêntico e branding emocional/de valores**.
- **Identidade sonora**: marcas também sendo reconhecidas pelo som (vinheta curta pros vídeos).
- **IA acelera, humano valida**: usar IA pra variações, mas a decisão final é de critério.

---

## 6. Direção sugerida por marca (ponto de partida — validar com a plataforma de marca)

| Marca | Clima | Aplicações-chave |
|---|---|---|
| Lindson Almeida | Autoridade, premium, direto — **preto + amarelo** (identidade existente) | Instagram, carrosséis, capa de Reels, cartão, apresentação de serviços, site |
| Orégano Turbo | Energia, velocidade, sabor, regional/folk | Caixa de pizza, cardápio, fachada, motoboy/bag, iFood, stories |
| Desentupidora SF | Confiança, rapidez, emergência 24h | Carro adesivado, uniforme, ímã de geladeira, Google Meu Negócio |
| Dra. Jaci Cunha | Cuidado, credibilidade, elegância | Receituário, cartão, fachada, Instagram educativo |
| Real Time SLZ / Tribuna 98 | Notícia, urgência, clareza | Templates de manchete, vinheta, thumbnails |
| WF Celulares / Rafael Imports | Tecnologia, preço, confiança | Etiquetas, sacola, vitrine, posts de produto |

---

## 7. Checklist de qualidade antes de entregar

- [ ] A plataforma de marca está preenchida e o conceito explica cada escolha visual
- [ ] Logo funciona em 16 px, em P&B e sobre fundo escuro e claro
- [ ] Área de proteção, tamanho mínimo e usos incorretos documentados
- [ ] Todas as cores com nome + HEX/RGB/CMYK + contraste checado
- [ ] Fontes com licença ok pra uso comercial
- [ ] Mockups relevantes pro negócio (nada de mockup aleatório)
- [ ] Apresentação em 16:9 com um assunto por slide, muito respiro e hierarquia clara
- [ ] Arquivos exportados: SVG, PNG, `brand.json`, slides PNG, PDF
- [ ] Marca pessoal do Lindson: preto e amarelo, fotos de terno, identidade do repositório

---

## 8. Técnicas de designer traduzidas pra código (LEIA ANTES DE DESENHAR)

> Esta seção existe porque o ponto fraco é a parte visual. Aqui estão regras objetivas, com números, para o resultado parecer feito por designer e não "cara de IA/template".

### 8.1 Princípio nº 1: menos coisa, maior, com mais espaço
- **Um assunto por slide.** Se tem duas ideias, são dois slides.
- **Espaço em branco é elemento de design.** Margem mínima do slide 1920×1080: **120 px** nas laterais, **96 px** em cima/embaixo. Nunca encostar conteúdo na borda (exceto imagens que sangram de propósito).
- **Contraste de escala**: o elemento principal deve ser **3 a 6× maior** que o resto. Título pequeno + logo enorme (como na capa da Cajuá) é mais elegante que tudo médio.
- Se estiver em dúvida: **tire um elemento**.

### 8.2 Grid e espaçamento
- Grid de **12 colunas**, gutter 24 px, dentro das margens acima.
- Escala de espaçamento base 8: `8, 16, 24, 32, 48, 64, 96, 128`. Nunca usar valores soltos (13 px, 37 px).
- Alinhar TUDO a uma borda ou centro em comum. Nada "quase alinhado".
- Composições que funcionam: **split 50/50** (texto | imagem), **5/7** (texto estreito | imagem larga), **centralizado** (hero), **grade 2×2 ou 3×2** de cards, **full bleed** (imagem ocupa tudo + texto por cima).

### 8.3 Tipografia (onde mais se erra)
- Escala modular **1.25 ou 1.333**. Ex. em slides: legenda 20 · corpo 28 · subtítulo 40 · título 72 · display 144–220 px.
- No máximo **2 famílias** (3 se a terceira for só destaque).
- Títulos grandes: `letter-spacing: -0.02em` a `-0.04em`, `line-height: 0.95–1.1`.
- Rótulos pequenos ("IDENTIDADE VISUAL", "CONCEITO"): CAIXA ALTA, 14–18 px, `letter-spacing: 0.12–0.2em`, peso 500–600. É o "tempero" que dá cara de case profissional.
- Corpo de texto: `line-height: 1.5`, linhas de **45–75 caracteres** (`max-width: 60ch`).
- Use pesos para hierarquia (400 vs 700), não só tamanho. Evite itálico + negrito + sublinhado juntos.
- Fontes que não parecem template: evite Arial, Roboto e Montserrat como principal. Boas opções Google Fonts: *Space Grotesk, Sora, Syne, Clash/Satoshi (Fontshare), DM Serif Display, Fraunces, Bricolage Grotesque, Unbounded, Archivo, Inter Tight*.

### 8.4 Cor
- Regra **60-30-10**: 60% cor dominante (fundo), 30% secundária, 10% destaque (CTA, detalhe).
- Fundo nunca #FFFFFF puro nem #000000 puro em apresentação: use off-white (`#F6F1E7`, `#FAF8F3`) e quase-preto (`#0E0E0E`, `#121212`). Fica muito mais sofisticado.
- Para preto + amarelo (Lindson): amarelo como **destaque de 10–30%**, não fundo de tudo. Amarelo sobre preto para títulos/realces; preto sobre amarelo só em cards de impacto.
- Gere tons da cor principal (claro/escuro) para variar fundos de slides sem sair da paleta.
- Checar contraste de texto: mínimo 4.5:1.

### 8.5 Textura e profundidade (o que tira a "cara de vetor chapado")
- **Grão/ruído** sutil por cima do fundo: SVG `feTurbulence` com opacidade 0.04–0.08.
- **Ícone gigante recortado** como marca d'água: símbolo da marca em 150–200% de tamanho, opacidade 0.05–0.1, saindo pela borda (a Cajuá faz isso com a folha na capa).
- **Cantos arredondados consistentes** (ex.: 24 ou 32 px) em todos os cards.
- Sombras realistas em mockups: várias camadas suaves, ex.:
  `box-shadow: 0 1px 2px rgba(0,0,0,.08), 0 8px 24px rgba(0,0,0,.12), 0 32px 64px rgba(0,0,0,.18);`
- Perspectiva para mockup de tela/cartão: `transform: perspective(1600px) rotateY(-12deg) rotateX(6deg);`

### 8.6 Construção do logo (técnicas)
- Partir de **formas geométricas simples** (círculo, quadrado, triângulo) e de um conceito (iniciais, objeto do negócio, metáfora).
- Mostrar a **grade de construção**: círculos e linhas finas (stroke 1 px, cor 30% opacidade) sobre o logo — é um slide clássico de case.
- Testar o logo: em **16 px**, em **uma cor só**, **invertido**, e de **longe** (borrar com `filter: blur(4px)` — se ainda reconhece, está bom).
- Wordmark: ajustar **kerning** manualmente entre letras críticas (AV, TA, LT); usar fonte base e modificar 1 detalhe (corte, ligadura, um caractere especial) para ficar proprietário.
- Símbolo + logotipo: altura do símbolo ≈ altura das maiúsculas ou 1,5–2× ela, alinhado pela linha de base ou pelo centro óptico.
- Gerar em SVG limpo (paths, sem fontes embutidas).

### 8.7 Receitas de slide (copiar a estrutura)
| Slide | Receita |
|---|---|
| Capa | Fundo cor principal + grão + símbolo gigante a 6% de opacidade; rótulo pequeno em caixa alta à esquerda; logo grande à direita ou centro |
| Conceito | Split 5/7: título "O Conceito" + 3 parágrafos curtos com palavras-chave em negrito | foto full-height |
| Moodboard | Grade de 9–15 fotos sem espaço entre elas (ou gap 8 px), cores harmonizadas |
| Paleta | Colunas verticais de altura total, cada uma com nome da cor + HEX/RGB/CMYK na base em caixa alta pequena |
| Logo hero | Só o logo, enorme, centralizado, no fundo da marca. Nada mais |
| Variações | Grade 2×2 de cards arredondados, cada card com um fundo da paleta e uma versão do logo |
| Construção | Logo em linha fina sobre grade geométrica, cotas com setas e medidas |
| Proteção / mínimo | Logo com retângulo tracejado em volta mostrando a área "X"; ao lado, os tamanhos mínimos em px e mm |
| Usos incorretos | Grade 3×2 com o logo errado + ✕ vermelho pequeno e legenda curta (esticado, girado, cor errada, sombra, fundo poluído, contorno) |
| Tipografia | Cards com "Aa" enorme + nome da fonte + etiqueta da função; depois um slide com alfabeto e hierarquia aplicada |
| Grafismos | Biblioteca de ícones/padrão sobre fundo sólido, espaçados em grade regular |
| Mockups | Foto/mockup full bleed (um por slide) ou 2 lado a lado; sem texto ou com texto mínimo |
| Social | 3 telas de celular com feed/post/story lado a lado, levemente em perspectiva, sobre fundo da cor da marca |
| Encerramento | Logo central cercado pelos grafismos em cards coloridos, ou só o logo + @ / site |

### 8.8 Mockups sem Photoshop
- Usar fotos livres (Unsplash/Pexels) de objetos em cena (sacola, caixa, cartão, fachada, camiseta) e posicionar o logo por cima com `mix-blend-mode: multiply` (fundo claro) ou `screen` (fundo escuro) + leve `transform` para acompanhar a perspectiva.
- Mockups 100% em CSS/SVG que ficam bons: cartão de visita (dois cards sobrepostos com sombra), tela de celular (moldura arredondada com notch), crachá, ecobag (forma + alça), embalagem/caixa (3 faces com tons diferentes da mesma cor).
- Se houver ferramenta de geração de imagem disponível, gerar a cena **sem** o logo e aplicar o logo vetorial por cima — texto e logo gerados por IA costumam sair deformados.

### 8.9 Anti-padrões ("cara de IA") — NÃO FAZER
- Gradiente roxo/azul genérico, glassmorphism sem motivo, emojis como ícone.
- Tudo centralizado e do mesmo tamanho.
- Sombra preta pesada, bordas 1 px cinza em tudo.
- Mais de 3 fontes, ou fontes padrão do sistema.
- Ícones de bibliotecas misturadas (estilos diferentes de traço).
- Texto longo em slide. Slide de case quase não tem texto.
- Logo pequeno no meio de muito espaço sem intenção.
- Mockups aleatórios (caneca e boné pra advogada).

### 8.10 Processo de trabalho que funciona
1. Gere **3 direções diferentes** de conceito (ex.: geométrica, artesanal, tipográfica) em 1 slide cada, antes de detalhar.
2. Escolha uma e só então construa o sistema completo.
3. Renderize cada slide como PNG (Playwright/puppeteer em 1920×1080) e **olhe a imagem** antes de seguir — corrija alinhamento, respiro e hierarquia.
4. Compare lado a lado com o case Cajuá: se o seu parece mais "cheio" ou mais "pequeno", corte e aumente.
5. Revise com o checklist da seção 7.

---

## 9. Referências para olhar

**Cases no Behance (busca "identidade visual")**
- Identidade Visual Brasileira | Cajuá — https://www.behance.net/gallery/249158505/Identidade-Visual-Brasileira-Cajua
- Outros bem avaliados na mesma busca: Smoosh (smoothie bar), Identidade Visual • Teen Talk, Coado Café Brasileiro, AUmoçinho (pet delivery), Restaurante Grande Sertão, Herbíssimo, Belnore, Manual de Marca Personal.

**Apresentação de marca**
- How to Present a Brand Identity to a Client — https://wannathis.one/blog/how-to-present-a-brand-identity-to-a-client
- Branding Mockups: 7 Ways to Present Your Design — https://www.ls.graphics/blog/branding-mockups-7-ways-to-present-your-design-to-a-client
- Present a Brand, Not a Logo — https://medium.com/cmd-opt-shift/present-a-brand-not-a-logo-cf27c8a95a5d
- Logo Design Guide: Notes on Presenting — https://medium.com/studio-function/logo-design-guide-4-of-5-notes-on-presenting-e1c130974dd0
- Inspiração de apresentações — https://speckyboy.com/branding-presentation.md

**Manual de marca**
- 19 brand guidelines examples (Frontify) — https://www.frontify.com/en/guide/brand-guidelines-examples
- 25 brand guidelines examples (ManyPixels) — https://www.manypixels.co/blog/post/best-brand-guide-examples
- 25 brand style guide examples (HubSpot) — https://blog.hubspot.com/marketing/examples-brand-style-guides
- Logo usage guidelines (Vistaprint) — https://www.vistaprint.com/hub/logo-usage-guidelines/

**Estratégia e processo**
- Manual completo de branding para negócios (Sebrae PE) — https://sebrae.com.br/Sebrae/Portal Sebrae/UFs/PE/Anexos/Manual completo de branding para negócios.pdf
- Plataforma de marca (Tera) — https://somostera.com/blog/branding-na-pratica-plataforma-de-marca
- How to create a brand strategy (Column Five) — https://www.columnfivemedia.com/how-to-create-a-brand-strategy/
- From kickoff to first concept (Smashing Magazine) — https://smashingmagazine.com/2026/07/how-turn-brand-strategy-into-visual-direction/

**Tendências 2026**
- Top 10 Branding Trends 2026 (Design Shack) — https://designshack.net/articles/trends/top-branding-trends/
- Graphic design trends 2026 (Vistaprint) — https://www.vistaprint.com/hub/graphic-design-trends
- Branding trends (Envato) — https://elements.envato.com/learn/branding-trends
- Design trends 2026: flexible brand systems (Renderforest) — https://renderforest.com/blog/design-trends-2026-brand-systems
