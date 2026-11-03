# Estado do projeto (para continuar de qualquer conta)

Atualizado em 29/10/2026. Leia também o `QUADRO-DA-EQUIPE.md` (quem está fazendo o quê agora), o `MAPA-DO-REPOSITORIO.md` (onde está cada coisa), o `REGISTRO-DAS-CONTAS.md` (quem fez o quê, com a conta de cada entrega), o `CLAUDE.md` (regras de trabalho) e o agente Peter em `.claude/agents/peter.md` (regras de YouTube, retenção e monetização).

## Apps e páginas publicadas (claude.ai)
São privados da conta que criou. **Para abrir ou editar de outra conta, compartilhe pelo menu "Compartilhar" de cada página** (dê acesso de edição se a outra conta for publicar nela). Os endereços `/_blob/...` dos arquivos `ativos*.json` só funcionam dentro do app de origem.

| Página | Link | Fonte no repositório |
|---|---|---|
| Downloads Alkantara (PDFs, demos) | https://claude.ai/artifact/3Vn9qpHt3iXgG2JAhcubs7 | gerada à mão (sem fonte) |
| SDR para Agências (funil, botão WhatsApp) | https://claude.ai/artifact/NztpiSW1Dd4JAjpXZ5CwBd | dados no banco do app |
| Minhas 3 Prioridades (organização pessoal) | https://claude.ai/artifact/4FbvcXArU9RPegh9D5PjsU | dados no banco do app |
| Contratos Alkantara | https://claude.ai/artifact/B9QirY7ndLJWP9iZ61mozz | `agencia/processos/modelo-contrato/` |
| Passaporte da Bíblia · Postagens | https://claude.ai/artifact/1aUURghpLqrWgTQmkvBcG4 | `conteudo/youtube/passaporte/motor/app_pv.py` + `ativos.json` |
| Raposa e Leão · Postagens | https://claude.ai/artifact/LSTErmeSra3qxFKBJMLiTC | `conteudo/youtube/raposa-e-leao/motor/app_rl.py` + `ativos.json` |
| Central do cliente (login, protótipo) | https://claude.ai/artifact/XjCkj5eULmE2Pg8KptnKcV | `agencia/sistema-clientes/prototipo/` |
| Fábrica de Conteúdo (conta Lindson) | https://claude.ai/artifact/WxeZuhrzQutLDTJ36y6EVt | `agencia/app/fabrica.html`; aba Passaporte: `passaporte/motor/fabrica_pv.py` |
| Recomeço 90: missões, funil, lista diária de leads e aba Conteúdo com os 300 roteiros de Reels (conta Lindson) | https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N | `agencia/app/recomeco90.html` · `conteudo/esteira/` |
| Painel do Vereador Leo Pinto (Central, cliente `LEO-…`) | https://claude.ai/artifact/7TjjwEUN5jASCbytXAvhHk (conta passaportedabiblia) | `agencia/sistema-clientes/leo-pinto/` (README) |

**Atenção (31/10):** os apps acima, exceto o painel do Leo, estão noutra organização do Claude. Compartilhar com edição por e-mail **não** libera escrita entre organizações: a conta passaportedabiblia abre, mas não publica neles. Para atualizar, use uma sessão da conta dona ou recrie o app nesta conta.

Decisão do Lindson: os vídeos do Passaporte e do Maquiavel ficam **nos apps próprios** de cada canal, não na Fábrica.

## Sistema de clientes (vereador e próximos)
- Ideias e decisões em `agencia/sistema-clientes/IDEIAS.md`: multi-cliente, o Lindson vê todos e cada cliente só o seu, com login próprio.
- Protótipo da tela de login: https://claude.ai/artifact/XjCkj5eULmE2Pg8KptnKcV
  - O código fica em `agencia/sistema-clientes/prototipo/login.html` e é montado com `prototipo/montar.sh`.
  - As fotos e imagens ficam fora do Git, em `agencia/sistema-clientes/fotos/`: `rec-68.webp` (foto principal recortada) e `casos/*.webp`. Noutra conta, peça as fotos ao Lindson ou baixe-as do artifact.
  - A foto foi recortada com `rembg` (modelo `u2net_human_seg`).
- Instaladores globais: `instalar-xquads.ps1/.sh` (squads do Xquads) e `instalar-builder-squad.ps1/.sh` (Builder Squad), para rodar no computador do Lindson.

## Canais de YouTube (dark)
Motor único **Pintura Viva** em `conteudo/youtube/passaporte/motor/pintura.py`. Ele serve aos dois canais pelo campo `"canal"`: `passaporte` usa as gravuras de Doré e `raposa` usa as pinturas do acervo. Recursos:
- voz humanizada em `conteudo/youtube/comum/voz_humana.py`;
- conversa com o ouvinte (balões);
- cortes a cada ~4 s;
- 3 aberturas e 3 fechamentos;
- trilha variada.

Processo completo em `conteudo/youtube/passaporte/PROCESSO.md` e `conteudo/youtube/raposa-e-leao/PROCESSO.md`.

### Passaporte da Bíblia
- **Longos 05 a 09**, de 16 a 20 min, roteiros em `passaporte/roteiros/` (gerados pelo `BRIEF.md` + agentes roteiristas).
  - Prontos e no app: 05 Gênesis e 09 Parábolas.
  - Em renderização: 06 Reis, depois 07 Profetas e 08 Vida de Jesus.
- **Refazer com a voz nova e a conversa:** pv-01, Shorts 01 a 20 e longos 01 a 04 (fila `conteudo/youtube/filas/lote8.sh`, pausada para dar prioridade aos longos).
- **Capas:** `motor/capas_pv.py`. Os longos novos têm capas claras com até 3 palavras e sem vermelho (estilo C).
- **Ordem dos comandos:** `lote3.py` (longos 05-09) → `pintura.py` → `capas_pv.py` → `app_pv.py ativos.json` → publicar o app. Depois de qualquer `lote2.py`, rodar `conversa.py`.

### Raposa e Leão
- App próprio criado com os 30 Shorts e 11 longos. Os textos de publicação ficam em `shorts/NN/publicar.json` e `longos/NN/publicar.json`.
- **Shorts refeitos com a voz nova:** 01 a 18 (07-18 em 31/10, enviados como assets `raposa-short-NN.mp4` no app https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH; a página do app ainda aponta para os arquivos antigos). Faltam 19 a 30: `lote.sh shorts 19 … 30`.
- **5 longos novos** (próximo passo, depois do Passaporte). Os temas:
  1. O Príncipe explicado
  2. Os Médici
  3. Por que Roma caiu segundo Maquiavel
  4. Em quem confiar: o teste de Maquiavel
  5. Maquiavel não era o vilão que te contaram
  - Brief em `raposa-e-leao/roteiros/BRIEF.md`.
  - Imagens em domínio público em `img/acervo/`, baixadas por `motor/acervo.py`. A Wikimedia limita o ritmo (pausas e miniatura de 1920 px). As imagens ficam fora do Git: rode `acervo.py` de novo noutra conta.
  - Falta: concluir o acervo e criar `img/acervo/MAPA.md` (o que cada imagem mostra), os 5 roteiros, a renderização (`pintura.py` com `canal: raposa`), as capas claras e subir no app.

### Sessão de 31/10 (conta passaportedabiblia): o que ficou rodando e como continuar
- **Ambiente:** os scripts usam caminhos da sessão antiga. Em vez de editar o código, recrie-os com links: `ln -s <seu scratchpad>/old-scratch /tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad` e `ln -s <clone do repo> /home/user/lindson`. Instale `edge-tts soundfile scipy` e baixe o modelo `https://huggingface.co/inference4j/depth-anything-v2-small/resolve/main/model.onnx` para `<scratchpad antigo>/modelos/depth.onnx`.
- **Gravuras de Doré:** `https://www.gutenberg.org/cache/epub/8710/pg8710-h.zip`, pasta `images/` (já numeradas `001.jpg`…; batem com `dore/MAPA.md`).
- **Acervo do Raposa:** `raposa-e-leao/motor/acervo_faltantes.py` baixa só as imagens que os roteiros 12-16 usam (título exato do `creditos.json` ou busca pela obra) e registra o crédito. O Wikimedia limita a 429: o script espera e tenta de novo.
- **Fila do Passaporte:** longos 06, 07 e 08 (mesmos passos do `lote7.sh`, sem refazer 05 e 09). Cada longo leva ~1h20 a 1h40 em 4 núcleos. Rode desacoplado (`setsid nohup … &`): tarefas em segundo plano da sessão morrem em 2 h. `RETOMAR=1` continua do último quadro.
- **Apps únicos desta conta (31/10, 12h UTC):** Passaporte https://claude.ai/artifact/CT3Z4M3yrzGrqCt3nh95ak (`ativos-novo.json`, `python3 app_pv.py ../ativos-novo.json`) e Raposa https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH (`ATIVOS=../ativos-novo.json python3 app_rl.py`). No app (31/10, 12h45 UTC): Raposa Shorts 07-30 (voz nova); Passaporte longos 07, 08 e Shorts 02-07. Em sessões filhas (tag `canais-dark-render`): Passaporte Shorts 08-20; Raposa longos 12-16 (a Wikimedia bloqueia a saída de rede, então imagens que faltarem são trocadas por obras do acervo); **roteiros novos de 16-20 min** para Raposa longos 06-11 (`raposa-e-leao/roteiros/longo-NN.json`, formato dos 12-16) e Passaporte longos 03-04 (`passaporte/roteiros/`).
- **Regra (Lindson, 31/10): todo vídeo longo tem de 16 a 20 min (2.400 a 2.900 palavras, BRIEF de cada canal).** Os roteiros antigos (`raposa-e-leao/longos/01-11/roteiro.json` e os longos 01-04 do Passaporte em `pintura.json`) são curtos, de 5 a 10 min: não renderize com eles. Antes de pôr um longo no app, confira que passa de 15 min.
- **Depois:** longos 12-16 do Raposa (`filas/lote_rl.sh`) e a fila de refazer com a voz nova (`filas/lote8.sh` e `raposa-e-leao/motor/lote.sh shorts`). Os vídeos ficam fora do Git.

### Retomar uma renderização
- Os quadros vão para a pasta temporária da sessão (`TMP` no topo de `pintura.py`). Noutra conta ou sessão, troque esse caminho pelo da sua pasta temporária.
- `RETOMAR=1 python3 pintura.py ../pintura.json <id>` continua de onde parou.
- O vídeo final completo (1080p) fica em `passaporte/videos/<id>.mp4`, fora do Git. A versão do app (`<id>-app.mp4`) é comprimida para caber em 20 MB. **Para o YouTube, use o arquivo completo.**

## Real Time (RT Full Jobs) · estado em 03/11/2026 (contas Pedro, Zuleide e Leandro)
| O quê | Onde | Situação |
|---|---|---|
| **Site principal (SEO)**, 8 páginas, template GAFFER | https://realtimeslz.pages.dev · código `Lindsonalmeida/realtime` (`python3 gerar.py`) | no ar (Leandro) |
| **Mini site da bio** | https://realtimeslz.pages.dev/bio/ (`bio/index.html`, noindex) | no ar (Zuleide, publicado pelo Leandro) |
| Painel do cliente | https://lindsonalmeida.pages.dev/painel/rt (30 artes para aprovar, botão Baixar em todas) | no ar (Leandro; 2º código pelo Pedro) |
| Identidade v1 + manual com rebranding (21 p.) | `agencia/clientes/rt-full-jobs/identidade/v1/` | aguardando o cliente (Pedro; rebranding Leandro) |
| Estratégia v2 (19 p.) | `agencia/clientes/rt-full-jobs/estrategia/v2/` · PDF no painel | aguardando o cliente (Leandro; v1 do Pedro no privado) |
| Artes v1 (Pedro), v2 e série Inventário (Leandro), legendas | `agencia/clientes/rt-full-jobs/instagram-v1/` e `instagram-v2/` | no painel |
| Bio, foto de perfil e 6 capas de destaques | `agencia/clientes/rt-full-jobs/instagram-v1/perfil/` (BIO.md) | entregues ao Lindson |
| 56 fotos reais dos equipamentos | `agencia/clientes/rt-full-jobs/fotos-equipamentos/` (FONTES.md) | feito |
**Como retomar:** falta pôr o site no Google (`agencia/processos/google-mini-site.md`), confirmar a cidade (`CIDADE` no `gerar.py` do site), os modelos a confirmar (STORM 1200, 24-70 GM/GM II, Mirage, intercom, teleprompter), uma fala real de cliente e fotos do equipamento da RT.

## Leo Pinto · novidades de 03/11/2026 (conta Leandro)
- Bio v2: `agencia/clientes/leo-pinto/instagram-perfil/BIO.md`. Capas de destaques: `agencia/clientes/leo-pinto/instagram-destaques/`.
- Modelo de aniversário (padrão = modelo B, com story): `agencia/clientes/leo-pinto/instagram-aniversario/` (README). Josef Figueiredo aprovado e no painel; fontes no privado `dados/clientes-arquivos/leo/aniversarios/`.
- Foto melhorada antes de usar: `ferramentas/melhorar_foto.py` (Real-ESRGAN).

## Ferramentas que ficam fora do Git
- **Agentes Xquads** (Hormozi, Donald Miller, Pedro Sobral, copy-squad…): instale com `instalar-xquads.sh` (Mac/Linux) ou `instalar-xquads.ps1` (Windows).
- **Modelo de profundidade** (Depth Anything V2 ONNX) usado pelo motor: baixe para `<pasta temporária>/modelos/depth.onnx`.
- **Dados pessoais e de clientes** (`agencia/contratos/`, `agencia/propostas/`): não vão para o GitHub de propósito. Peça ao Lindson quando precisar.

## Pesquisas e estratégias
- Passaporte: `conteudo/youtube/passaporte/pesquisa/` (estratégia, pesquisa de dores, estilos de vídeo, nomes) e `IDENTIDADE.md`.
- Raposa e Leão: `IDENTIDADE.md`, `ROTEIROS-SHORTS.md`, `ROTEIROS-LONGOS.md`.
- Peter (YouTube): `.claude/agents/peter.md`.

## Central do Cliente (conta Lindson, 01/11/2026)
- **No ar:** https://lindsonalmeida.pages.dev. Um sistema só: o cliente cria a conta uma vez com senha e código e depois entra com e-mail e senha; o admin vê tudo.
- **Site montado:** repositório privado `Lindsonalmeida/CentralLindsonALmeida`.
- **Fonte:** `agencia/sistema-clientes/` (ver `site/README.md`).
- **Atualizar:** rode `site/montar-site.py`, copie `functions/` e o conteúdo de `publico/` para a raiz do repositório privado e faça push. A Cloudflare publica sozinha.

## Nano Banana, imagens com Gemini (conta Lindson, 01/11/2026)
- **Chave:** em Segredos de rede do ambiente "Default" da conta Lindson (host `generativelanguage.googleapis.com`, cabeçalho `x-goog-api-key`, sem prefixo). O proxy coloca a chave sozinho, e ela nunca aparece no código.
- **Uso:** `python3 ferramentas/nano_banana.py "prompt" saida.png [fotos de referência]`.
- **Primeiro teste:** numa sessão nova. Nas outras contas, a chave precisa ser cadastrada de novo no ambiente de cada uma.
