# Projeto Designer v2 · Pesquisa (conta Leandro, 16/11/2026)

A v1 foi reprovada ("ficou horrível"). Antes de criar a v2, pesquisa de como o Pinterest e o Behance funcionam para quem vende design, e 11 referências de estúdios de 7 países (capturas em `referencias/`).

## 1. Pinterest para designer vender
- **Formato:** pin padrão 2:3, **1000 x 1500 px** (600x900 e 2000x3000 também servem). Pin de vídeo vertical curto. Imagem grande manda: o pin é visto em coluna estreita, o texto precisa ser pouco e grande.
- **O Pinterest é buscador, não rede social:** a palavra-chave entra no **nome da pasta** (sinal forte), na descrição da pasta (2 a 3 frases, 3 a 5 palavras-chave), no título do pin (até 100 caracteres), na descrição (até 500), no texto alternativo e até no nome do arquivo. Pasta "Inspo" não aparece; "Identidade visual para clínica" aparece.
- **Conta empresa:** nome de exibição com a palavra-chave ("Lindson Almeida Studio | Identidade Visual"), bio dizendo o que fixa e para quem, site reivindicado (lindsonalmeida.pages.dev) para ganhar atribuição e Rich Pins (metadados do site no pin).
- **Frequência:** constância vale mais que volume. Pin novo (imagem nova) toda semana; o mesmo pin em várias pastas é tratado como repetição, então cada pin vai para uma pasta só.
- **Estúdios que vendem:** perfis de branding no Pinterest mostram **o mockup, não o slide**: cartão de visita em luz natural, papelaria vista de cima, fachada, embalagem. O título fica pequeno, discreto, na marca do estúdio.
Fontes: [SocialRails, tamanhos](https://socialrails.com/blog/pinterest-pin-size-dimensions-guide) · [SocialRails, boas práticas](https://socialrails.com/blog/pinterest-best-practices) · [Search Engine Journal, SEO do Pinterest](https://www.searchenginejournal.com/pinterest-seo-tips/200282/) · [WP Tasty, SEO do Pinterest](https://www.wptasty.com/pinterest-seo) · [GoDaddy, design de pin](https://www.godaddy.com/resources/skills/pinterest-design-tips)

## 2. Behance: o que o case curado tem
- **A curadoria é humana** e escolhe cerca de 1% do que é publicado: trabalho "inovador, polido, pensado e bem acabado", publicado completo (eles não revisam de novo). [Behance, curadoria](https://medium.com/behance-blog/behance-curation-philosophy-and-approach-6e0ae9ab350f) · [Como ser destaque](https://medium.com/behance-blog/how-to-get-featured-on-behance-insights-and-tips-from-our-curation-team-b81358a46b29) · [Ajuda Behance](https://help.behance.net/hc/en-us/articles/204484044-Guide-Discover-Creative-Work-on-Behance)
- **Capa:** a marca aplicada (mockup, pôster, logo), um foco só, alto contraste para funcionar pequena e **sem texto** (o Behance recorta a miniatura). A v1 errou aqui: slide recortado com texto cortado na borda.
- **Ritmo de módulos:** hero imersivo → conceito numa frase → logo grande → grade/construção → cores → tipografia → sequência de mockups (do perto para o longe: cartão, papelaria, celular, embalagem, parede, rua) → fecho. 12 a 16 imagens, largura 1400 px, espaçamento 0 entre módulos. [Adobe, case com Boards](https://www.adobe.com/learn/firefly/web/build-a-behance-case-study-with-boards) · [Icons8, como fazer um bom case](https://blog.icons8.com/articles/how-to-make-a-good-behance-case/) · [Unilink, projeto Behance 2026](https://unil.ink/blog/best-behance-projects-2026)

## 3. Referências (capturas em `referencias/`, 11 estúdios, 7 países)
| Estúdio | País | O que tiramos |
|---|---|---|
| Pentagram | EUA/Reino Unido | fundo claro, muito respiro, trabalho fala sozinho |
| Collins | EUA | frase única em serifa enorme sobre off-white ("Rewrite your worth.") |
| Porto Rocha | EUA/Brasil | **marca aplicada no mundo real** (MASP) como imagem principal |
| Manual | EUA | fundo claro + foto de aplicação grande + frase editorial |
| Landor | EUA/Reino Unido | wordmark gigante, cor chapada só num ponto |
| Studio Dumbar | Holanda | foto noturna de fachada com a marca |
| Lundgren+Lindqvist | Suécia | grade editorial, legenda mono pequena |
| Bureau Borsche | Alemanha | grid de projetos em blocos iguais |
| Anagrama | México | celular e papelaria como prova do sistema |
| Mucho | Espanha/EUA | foto escura cinematográfica + título branco curto |
| Snøhetta | Noruega | texto curto, muito branco |

**As 3 mais impactantes, combinadas na v2:** (1) **Collins**: fundo off-white e frase de conceito enorme; (2) **Porto Rocha / Manual**: a marca aplicada em foto (mockup) é sempre a imagem principal; (3) **Lundgren+Lindqvist**: legenda mono pequena e grade editorial.
**Descartadas:** fundo preto chapado da v1 (Bureau Borsche/Mucho funcionam com foto, sem foto ficam vazios), wordmark gigante da Landor (compete com a marca do cliente).

## 4. Decisões da v2
1. Apresentação **clara e editorial** (off-white #F2EFE9, texto #0A0A0A, amarelo #F5C518 só em detalhe): todos os estúdios de referência vendem assim, e a cor do cliente aparece mais forte sobre fundo claro.
2. **Mockups fotorrealistas** em 3D (Three.js, luz natural, sombra suave, sombra de janela, grão): cartões, papelaria, celular com Instagram, pôster na parede, embalagem e outdoor, cada um com o logo oficial em arquivo (nada recortado de slide).
3. Capa do Behance = mockup sem texto. Pin = mockup grande + título pequeno no rodapé.
4. Sem placeholder: a oferta usa "Sua marca" e cases reais.
