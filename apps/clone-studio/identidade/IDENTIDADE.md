# Dublê · identidade visual (conta Pedro, 03/11/2026)

O app interno de clone de voz e imagem do Lindson, antes "Clone Studio". O código fica em `apps/clone-studio/`. O nome foi escolhido em `NOME.md`.
Método: `brand-squad`. Alina Wheeler deu o sistema completo e os 9 ideais. Marty Neumeier deu o "único" e o MAYA. Regra da casa: **nada se cria, tudo se copia**, então cada decisão abaixo diz de qual marca real ela foi copiada.

Arquivos: `logo.svg` (horizontal), `simbolo.svg` (quadrado), `favicon.svg` (32 px), `tema.py` (tema do Gradio 6 + CSS), `previa.png` (logo e símbolo), `previa-app.png` (o tema aplicado numa tela de teste) e `PROMPT-CLAUDE-DESIGN.md`.

## 1. Conceito

Todo dublê trabalha com contrato. O Dublê copia a voz e o rosto de quem autorizou (o Lindson, clientes como o vereador e a dentista, e personagens de domínio público como Maquiavel e as gravuras de Doré) e só deixa usar essa cópia com o termo assinado e o vídeo da própria pessoa. O símbolo mostra a ideia: um círculo partido ao meio. A metade cheia é o **original**, o rosto. A outra metade é feita de barras de som, que são o **duplo**, a voz que se repete e vai sumindo como um eco. A palavra "dublê" tem a mesma ideia, porque o "d" e o "b" são o espelho um do outro.

**Único (Neumeier):** "O Dublê é o único estúdio de clone que só grava quem disse sim."

## 2. Personalidade

| É | Não é |
|---|---|
| Preciso, como um estúdio profissional | Brincalhão, de app de efeitos |
| Confiável: avisa, pede e registra | Misterioso, "hacker" ou "deepfake" |
| Moderno e calmo: escuro, limpo, uma ação por tela | Cheio de neon, brilho e gradiente |
| Direto, em português simples | Técnico ou em inglês |

Arquétipo: **o Mago com regra** (transforma, mas com ética). Voz: "você", frases curtas, sem jargão (igual à marca do Lindson).

## 3. Paleta

| Nome | Hex | Uso | Proporção | Contraste no Grafite |
|---|---|---|---|---|
| Grafite | `#0B0B10` | fundo de tudo | **60%** | n/a |
| Painel | `#15151C` | cartões, campos e blocos | **30%** (com a Linha) | n/a |
| Linha | `#2A2A35` | bordas e divisões | dentro dos 30% | só para borda, não para texto |
| Papel | `#F2F1EC` | texto principal e metade cheia do símbolo | n/a | **17,4:1** (AAA) |
| Apagado | `#9C9AAB` | texto de apoio e legendas | n/a | **7,1:1** (AAA) |
| **Eco** | `#8B7CFF` | botão principal, foco, aba ativa e barras de voz | **10%** | **6,0:1** (AA) |
| Eco claro | `#A99DFF` | hover e links | dentro dos 10% | 8,4:1 |
| Selo | `#F5C518` | **só** consentimento e "liberado" (é o amarelo da Central) | menos de 2% | 12,0:1 |
| Certo | `#5CC98A` | "Liberado" e sucesso | pontual | 9,5:1 |
| Erro | `#F0705C` | "Bloqueado" e erro | pontual | 6,7:1 |

Regras:
- O texto do botão Eco é **Grafite** (6,0:1, AA). Texto branco sobre o Eco dá só 3,3:1 e está **proibido**.
- No Painel, todos os textos continuam AA (Papel 16,1 · Apagado 6,6 · Eco 5,6).
- Fundo claro, só em impressão: Eco escuro `#5B4BE0` sobre `#F7F6F2` (5,5:1).
- Sem gradiente. A única "animação de cor" é a onda das barras enquanto a voz é gerada.

## 4. Tipografia (Google Fonts)

| Papel | Fonte | Peso | Detalhe |
|---|---|---|---|
| Títulos | **Geist** | 600 (SemiBold) | espaçamento -2%, títulos curtos |
| Texto, botões e campos | **Manrope** | 400 / 500 / 700 | a mesma da Central e da marca do Lindson |
| Números, selos e duração do áudio | **Geist Mono** | 500 | caixa alta, espaçamento +4% |

Hierarquia: H1 32 px / H2 22 px / H3 18 px (Geist 600) · corpo 15 px · legenda 13 px (Manrope) · selo 12 px (Geist Mono).
Se a fonte não carregar (o notebook está sem internet), entra `system-ui` / `Segoe UI`, que já fica no `tema.py`.

## 5. Logo

- **Símbolo:** um círculo partido. A metade esquerda é cheia (Papel) e a direita tem 3 barras arredondadas (Eco) que vão de 40 para 30 e depois 16 de altura. A metade é o rosto e as barras são a voz em eco.
- **Palavra:** "dublê" em minúsculas, desenhada à mão em traço geométrico (círculo + haste, pontas redondas, traço de 9 em 80). Não usa fonte, porque as letras são formas. Só o acento circunflexo vai em Eco: é o "chapéu" do duplo e repete as barras.
- **Horizontal (`logo.svg`):** símbolo à esquerda e palavra à direita. O vão entre os dois tem a largura de um "d".
- **Área de proteção:** a altura de uma barra do meio em volta de tudo. **Tamanho mínimo:** logo horizontal com 96 px de largura e símbolo com 16 px.
- **Usos proibidos:** esticar, girar, trocar as cores das metades, pôr o símbolo sobre foto sem a placa Painel, usar gradiente, sombra ou brilho, e escrever "Duble" sem acento na tela.

## 6. Ícone e favicon

- `simbolo.svg`: placa quadrada Painel (`#15151C`) com cantos de 14/64, borda Linha de 1 px e o símbolo no centro. É o ícone do atalho na área de trabalho e o avatar.
- `favicon.svg`: a mesma ideia com só **2 barras**, mais grossas, para ler bem em 16 e 32 px (conferido na `previa.png`).
- No Gradio: `app.launch(favicon_path='identidade/favicon.svg')`. Se o navegador não mostrar o SVG, converta para PNG de 32 px.

## 7. Estilo de interface (modo escuro sempre)

- Fundo Grafite e conteúdo em cartões Painel com borda Linha de 1 px. Cantos de 12 px nos cartões e **pílula** nos botões. Sem sombra (só no foco).
- **Um único botão Eco por tela**, que é a ação principal. O resto fica em botão Painel.
- Abas com sublinhado Eco na aba ativa e as outras em Apagado.
- **Faixa de consentimento:** borda esquerda Selo (amarelo) e fundo amarelo a 7%. É o único lugar com amarelo, para ele chamar a atenção.
- **Selos da biblioteca:** pílulas em Geist Mono maiúsculo. LIBERADO em verde e BLOQUEADO em vermelho, os dois com fundo a 12%.
- **Gerando:** as 3 barras do símbolo se mexem como uma onda. A animação para quando o computador pede movimento reduzido.
- Largura máxima de 1180 px e cabeçalho com o logo e a frase "Voz e rosto, só com autorização · uso interno".
- Tudo isso já está no `tema.py` (`TEMA`, `CSS` e `CABECALHO`). Tela de teste: `previa-app.png`.

## 8. Microcópias (português simples)

**Botões**
| Lugar | Texto |
|---|---|
| Biblioteca | **Salvar dublê** |
| Voz | **Gerar voz** |
| Vídeo | **Gerar vídeo** |
| Secundários | Ouvir amostra · Trocar arquivo · Baixar áudio · Apagar dublê |

**Rótulos**
- Nome do dublê · Quem é (Lindson / Cliente / Personagem) · Termo vale até · Amostra de voz (10 s a 2 min, sem barulho) · Vídeo base (2 min olhando para a câmera) · Termo assinado (PDF ou foto) · Vídeo de consentimento · De onde vem o personagem (obra, autor, licença).
- Voz: Voz de quem · Emoção (mais alto = mais emoção) · Deixar humano (pausas, respiração, som de estúdio) · Texto ("Escreva como se fala: frases curtas e números por extenso.").

**Avisos de consentimento**
- Faixa fixa na Biblioteca: **"Só com autorização.** Rosto e voz de gente real só entram aqui com o termo assinado e um vídeo da própria pessoa dizendo que autoriza."
- Frase do vídeo: "Eu, [nome completo], autorizo o Lindson Almeida a usar a minha imagem e a minha voz para criar conteúdo com inteligência artificial para [finalidade], até [data]. Hoje é [data de hoje]."
- Selo: **LIBERADO** · **BLOQUEADO**, com o motivo embaixo: "Falta o termo assinado." / "Falta o vídeo de consentimento." / "O termo venceu em [data]." / "Falta dizer de onde vem o personagem."
- Ao salvar: "Dublê salvo e liberado." ou "Dublê salvo, mas bloqueado: [motivo]."
- Ao tentar gerar com um bloqueado: "Esse dublê está bloqueado: [motivo]. Resolva na Biblioteca."
- Depois de gerar: "Pronto: [x] s de áudio. Feito com IA: avise o público quando parecer real."
- Rodapé: "Uso interno. Nada sai daqui sem a autorização da pessoa."

**Erros:** "Escolha um dublê na Biblioteca." · "Escreva o texto." · "Esse arquivo não abriu. Tente MP3, WAV ou MP4."

## 9. Referências copiadas (nada se cria, tudo se copia)

| Decisão | Copiado de | Link |
|---|---|---|
| Símbolo feito de barras verticais arredondadas (a voz como barras) | **ElevenLabs**: o logo é feito de duas barras verticais | https://elevenlabs.io |
| Interface preta e branca, botão principal em pílula e um só por tela | **ElevenLabs** (site e app) | https://elevenlabs.io/app |
| Fundo quase preto com cartões de borda fina de 1 px e sem sombra | **Vercel** (dashboard e sistema Geist) | https://vercel.com/geist/introduction |
| Fontes Geist (títulos) e Geist Mono (números e selos) | **Vercel Geist**, gratuita no Google Fonts | https://fonts.google.com/specimen/Geist |
| Destaque violeta único sobre grafite, aba ativa sublinhada, títulos com espaço negativo | **Linear** (destaque roxo-índigo da marca e do app) | https://linear.app/brand |
| Violeta como cor de "clone e avatar" | **HeyGen** (marca e app em roxo) | https://www.heygen.com |
| Palavra em minúsculas, geométrica e curta | **Suno** e **Runway** (wordmarks em minúsculas, sem enfeite) | https://suno.com · https://runwayml.com |
| Selo de autorização e frase de consentimento gravada | **HeyGen** (vídeo de consentimento do avatar) e **ElevenLabs** (verificação da voz profissional), da nossa pesquisa | `conteudo/referencias/ia-video-voz/HEYGEN.md` · `ELEVENLABS.md` |
| Fundo escuro, Manrope e amarelo `#F5C518` | **Central Lindson Almeida** (`agencia/sistema-clientes/prototipo/painel.html`) | https://lindsonalmeida.pages.dev |

### Por que não é igual à Central
O Lindson pediu uma identidade **única** para este app. A regra 13 da memória ("apps com a mesma identidade da Central") continua valendo: o Dublê é uma **marca da mesma família**. Ele tem o mesmo fundo escuro, a mesma fonte de texto (Manrope), o mesmo amarelo (só no selo de consentimento) e a mesma voz. Muda só o nome, o símbolo e a cor de destaque (Eco). Se ele preferir tudo igual à Central, troque `ECO` por `#F5C518` no `tema.py`. O texto do botão continua Grafite.

## 10. Checagem dos 9 ideais (Alina Wheeler)

Visão (uso interno, com ética) · **Sentido** (rosto + voz e só com autorização) · Autenticidade (é o que o app faz) · **Diferença** (nome em português e símbolo partido, contra os nomes em inglês das ferramentas) · Duração (sem modismo de gradiente) · **Coerência** (as barras se repetem no logo, no favicon, no acento e na animação) · Flexibilidade (o símbolo funciona sozinho em 16 px) · Compromisso (`tema.py` é a única fonte das cores) · Valor (o Lindson reconhece o app na hora, na barra do navegador).
