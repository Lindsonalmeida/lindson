# Estratégia do Pinterest · Barzakh · um estúdio Al Kántara
Conta Zuleide, 18/11/2026 · situação: aguardando aprovação do Lindson · dados em `plano.json` · peças em `pins/`, `capas/`, `previa.jpg`.
Continua (não refaz) os pins da v3 (`marca-lindson/projeto-designer/v3/pinterest/pins/`, 34 pins com rodapé Barzakh) e os 42 por cliente de `projeto-designer/pinterest/v3/`.

## 1. Persona (5 linhas)
- Dono(a) de negócio local de 28 a 50 anos (clínica, loja, restaurante, escritório, curso) que vai abrir, reposicionar ou "subir de nível" a marca.
- Usa o Pinterest à noite, no celular, para montar pasta de referência antes de contratar ("identidade visual elegante", "cartão de visita minimalista").
- Dor: a marca atual parece amadora e menor que o negócio; tem medo de pagar e receber "só um logo".
- Confia em: trabalho real aplicado (cartão, fachada, embalagem), consistência, estúdio com conceito e endereço.
- Afasta: chamada de anúncio, preço em selo, template genérico, texto em cima da imagem.

## 2. Posicionamento
Pinterest é busca visual, não rede social: a Barzakh entra como **a referência que a persona salva**. Cada pin é uma peça de marca em tela cheia que responde a uma busca; o clique leva ao site e ao WhatsApp. Frase: "A passagem da sua marca." (não vai no pin, vai na bio do site).

## 3. Perfil
- **Conta comercial** (Pinterest Business, gratuita), usuário **@barzakhstudio**.
- **Nome com palavra-chave:** "Barzakh · Identidade visual e branding".
- **Bio:** "Estúdio de identidade visual e branding em São Luís (MA). Marcas com conceito: logo, cores, papelaria e brand book. Um estúdio Al Kántara."
- **Avatar:** monolito em Obsidiana (`barzakh-avatar-obsidiana.png`). **Capa:** `capas/capa-do-perfil-1600x900.jpg` (placa aprovada no concreto).
- **Reivindicar site:** alkantaragroup.pages.dev por meta tag no `<head>` (trocar por barzakh.studio quando comprar).
- **Rich Pins:** ativar após reivindicar (Open Graph na página da Barzakh: título, descrição, imagem).
- **Destaque do perfil ("Criados"):** fixar os 6 pins novos.

## 4. Pastas (SEO) e seções
| Pasta | Seções |
|---|---|
| Identidade visual premium | Placa e sinalização · Hot stamping e ouro · Arco e arquitetura |
| Identidade visual para pequenas empresas | Pizzaria e restaurante · Loja e varejo · Curso online · Produtora e audiovisual · App e tecnologia · Comunicação pública |
| Cartão de visita e papelaria de marca | Cartão de visita elegante · Papel timbrado e envelope · Mockup de cartão de visita |
| Paleta de cores para marca | Paletas escuras e elegantes · Azul e dourado · Cores das marcas reais |
| Brand book e manual de marca | Capas de brand book · Páginas de manual · Tipografia da marca |
| Logo e logotipo elegante | Símbolos e monogramas · Logotipos em serifa · Avatar e versões |

Descrições de cada pasta em `plano.json`. Capas em `capas/pasta-01..06-*.jpg` (recorte do pin, sem texto). As pastas antigas da v3 (Embalagem, Instagram, Pôster) viram seções dentro de "pequenas empresas".

## 5. Palavras-chave (busca pública do Pinterest BR, 18/11)
Fonte: guias que o próprio Pinterest sugere em cada busca (`pesquisa/guias-busca-pinterest.json`). **Volume não medido**: validar no Pinterest Trends com a conta logada.
- **identidade visual** → elegante, minimalista, paleta de cores, loja, arquitetura, psicologia, manual de, logomarca.
- **cartão de visita** → elegante, minimalista, criativo, advogado, arquitetura, mockup, estética.
- **logotipo** → elegantes, minimalista, modernos, de loja, de marca. **brand book** → luxury, layout, cover, typography, color palette.
- **embalagem** → de luxo, minimalista, criativa. **mockup** → business card, poster, iphone, box. **papelaria personalizada** → logomarca, kit.
Regra: palavra-chave no começo do título, repetida natural na descrição e no nome da pasta; nunca lista de hashtags.

## 6. Tipos de pin
- **Estático 2:3 (1000×1500)**: o principal. Mockup em tela cheia, legenda pequena (título serifa + linha mono + monolito), nada de chamada.
- **Vídeo/Idea 9:16 (6 a 15 s)**: a partir do mês 2, reaproveitando os Reels do feed v3 (placa acendendo, hot stamping girando), sempre com áudio (trilha + SFX), sem texto em cima.
- **Carrossel (2 a 5 imagens)**: um case por carrossel (capa da marca → cartão → embalagem → Instagram), a partir da semana 3.

## 7. Padrão visual
Placa em arco, monolito em ouro escovado, concreto, brilho Lápis #2B3A8F, Obsidiana, Marfim; Fraunces + JetBrains Mono. "Clean e rico": uma peça por pin, luz rasante, grão. Cases de cliente entram com a cor deles (dão vida) e o mesmo rodapé Barzakh. Mockup de IA leva "imagem gerada por IA" na descrição.

## 8. Ritmo e agendamento
- **1 pin novo por dia** nos primeiros 30 dias (constância vale mais que volume), alternando Barzakh e cliente; horários 12h45, 16h45 e 20h45 (São Luís), dentro da janela 8h-21h.
- **Agendar no próprio Pinterest** (até 2 semanas à frente) ou importar em massa pelo CSV (`Title, Media URL, Pinterest board, Description, Link, Keywords`), gerado do `plano.json`.
- Repetir o mesmo pin em outra pasta só depois de 7 dias; nunca o mesmo pin duas vezes no mesmo dia.

## 9. Calendário de 30 dias (20/11 a 19/12/2026)
Os 30 itens (data, hora, imagem, pasta, seção, título, descrição, alt e link com UTM) estão em `plano.json → calendario`. Semana 1 abre com os 6 pins novos intercalados com cases.

## 10. Funil
Pin (busca) → salvar → clique → **alkantaragroup.pages.dev** (UTM `utm_source=pinterest&utm_content=<pin>`) → página Barzakh com cases → botão WhatsApp (wa.me/5598985621808) com mensagem pronta "Vi a Barzakh no Pinterest e quero falar sobre a minha marca" → proposta (sem preço no Pinterest). Pin nunca fala preço nem promete resultado.

## 11. Métricas e rotina
- **Toda semana (segunda, 15 min):** Pinterest Analytics: impressões, salvamentos, cliques de saída por pin e por pasta. 3 linhas: repetir o que mais salvou, cortar o que não teve clique, testar uma palavra-chave nova.
- **Todo mês:** UTM no site (cliques do Pinterest) e conversas no WhatsApp que citam o Pinterest. Sem dado, dizer que falta; nunca inventar número.
- **Diário (5 min):** conferir se o pin do dia saiu e responder comentários.

## Travas (@Lindson)
1. Criar a conta comercial @barzakhstudio no Pinterest. 2. Página própria da Barzakh no ar (hoje o link vai para a home do Al Kántara Group) e, se possível, comprar barzakh.studio para reivindicar e ativar Rich Pins. 3. Aprovar esta estratégia e os 6 pins novos.
