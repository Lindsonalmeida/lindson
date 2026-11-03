# Desentupidora SF · feed do Instagram v1 (4 artes 1080×1350) · conta Zuleide, 03/11/2026

**Situação:** criadas e aguardando a aprovação do Lindson (criação). Só sobem para o painel do cliente na Central depois do OK dele.

Prévia na ordem de postagem: `previa-feed.jpg` (a tag da linha editorial aparece só na prévia e no card de aprovação, não na arte).
Legendas, datas, linhas e modelo de cada arte: `textos.json`.

## Os 4 posts

| Ordem | Data sugerida | Linha editorial | Arte | Foto ou só logo | Fundo | Modelo copiado |
|---|---|---|---|---|---|---|
| 1 | 10/11 (ter) | Socorro rápido | `p1-socorro-rapido.jpg` · "Água voltando pelo ralo?" | foto (Pexels) | azul royal | Designi [Desentupidora Precisa de Ajuda Urgente](https://www.designi.com.br/58a306c92cd5fca2): foto grande ocupando a arte, cartão de cor arredondado à direita com a pergunta em caixa alta, pílula branca de chamada com seta e 2ª pílula branca embaixo (no modelo, bandeiras de cartão; aqui, os serviços). Tirado o selo 3D. |
| 2 | 13/11 (sex) | Evite o prejuízo | `p2-evite-o-prejuizo.jpg` · "Óleo na pia" (lembrete) | só logo (cenário quase transparente) | laranja | Designi [Lembrete Não Espere o Entupimento Acontecer](https://www.designi.com.br/29d59e4074114199): frase repetida 4× em letras gigantes, cartão branco no centro com faixa de cor no topo, botão saindo da base do cartão, onda escura no rodapé com os contatos. |
| 3 | 17/11 (ter) | Bastidores do serviço | `p3-bastidores.jpg` · "Caixa de esgoto cheia assim?" | foto (técnico da SF + foto real de serviço) | marinho escuro | Designi [Desentupidora Pia da Cozinha Entupida](https://www.designi.com.br/273594c76412bf7e): cartão laranja com o profissional no alto à esquerda, traço laranja + título em duas cores à direita, pílula laranja do telefone por cima da 2ª foto, assinatura embaixo. Tirado o escudo 3D. |
| 4 | 20/11 (sex) | Fala com a gente | `p4-fala-com-a-gente.jpg` · enquete "O que já entupiu aí na sua casa?" | só logo | branco azulado | Cartão de enquete "Conta pra gente!" do Leo (31/12, aprovado pelo Lindson em 03/11; `../../leo-pinto/instagram-v14-datas/p5-31-12.jpg`): pergunta no topo com a 2ª linha numa caixa de cor, cartão com 4 opções numeradas, palavra gigante quase transparente atrás e "comenta o número". |

Alternância conferida: foto, só logo, foto, só logo; nenhum fundo nem composição repetidos em sequência. Ganchos pela dor (água voltando, prejuízo, cheiro, esgoto voltando), sem dados inventados: tudo o que as artes e as legendas afirmam está no site do cliente (orçamento grátis, sem quebra-quebra, máquinas de cabo rotativo, teste na hora, serviços e cidades).

## Linhas editoriais da Desentupidora SF (criadas nesta versão)
- **Socorro rápido:** o problema aconteceu agora (água voltando, vaso transbordando) e a saída é chamar no WhatsApp.
- **Evite o prejuízo:** dicas de prevenção com o lado negativo (o que estraga, o que custa caro).
- **Bastidores do serviço:** fotos reais de serviços da SF, equipamento e como é feito.
- **Fala com a gente:** enquetes e perguntas para gerar comentário e conversa no direct.

## Identidade usada (do site e do flyer do cliente)
Azul marinho `#061a4a`/`#0a2a6e`, royal `#1d5fd0`, céu `#3fa9ff`, laranja `#ff8a00`/`#ff6a00`, branco azulado `#f4f8ff`; Montserrat 600 a 900, itálico 900 em caixa alta nos títulos (como no flyer); logo circular oficial. **Assinatura fixa** em todas: logo + @desentupidorasf_slz + WhatsApp (98) 98915-3929 no rodapé esquerdo. Sem emojis, adesivos e ícones 3D (o selo e o escudo 3D dos modelos foram retirados).

## Fotos usadas e créditos
- `assets/pexels-6419128.jpg`: mãos de profissional no encanamento embaixo da pia, [Pexels 6419128](https://www.pexels.com/photo/plumber-installs-pipe-fittings-6419128/) (licença Pexels, uso livre). Com véu azul.
- `assets/pexels-220612.jpg`: ralo de inox, [Pexels 220612](https://www.pexels.com/photo/stainless-steel-sink-drainage-220612/) (licença Pexels). Só cenário, quase transparente, com véu laranja.
- `assets/tecnico.jpg` e `assets/caixa-esgoto.jpg`: material do cliente, já público no site (`GruposSF/img/`). A caixa de esgoto é foto real de serviço; o "play" do canto do vídeo original fica fora do recorte.
- `assets/logo.jpg`: logo oficial do site.
- Os bancos de foto (Pexels e Unsplash) bloqueiam a busca neste ambiente; os IDs vieram de busca na web e foram baixados direto de `images.pexels.com`.

## Como gerar
```
cd agencia/clientes/desentupidora-sf/instagram-v1
python3 gerar.py . && node render.js "$PWD" && \
cp out/p1.jpg p1-socorro-rapido.jpg && cp out/p2.jpg p2-evite-o-prejuizo.jpg && cp out/p3.jpg p3-bastidores.jpg && cp out/p4.jpg p4-fala-com-a-gente.jpg && \
python3 feed.py .
```
Mesmo fluxo aprovado do Leo v14 (HTML → Playwright → JPG). O `render.js` usa o proxy do ambiente (`HTTPS_PROXY`) para carregar a Montserrat e avisa se a fonte não carregou.

## Referências (`referencias/`)
Capturas dos 3 modelos do Designi e da busca "desentupidora" no Designi (`designi-busca-desentupidora.jpg`, 03/11/2026). O modelo do post 4 é o do Leo, já no repositório.

## Próximos passos
1. Lindson aprova a criação (ou pede ajuste: tirar do painel e só subir depois de ajustado).
2. Subir os 4 posts nas Aprovações do painel da Desentupidora SF na Central, com legenda e tag, para o cliente aprovar no site.
3. Pedir ao cliente fotos reais dos serviços (uma por mensagem) para os próximos "Bastidores".
