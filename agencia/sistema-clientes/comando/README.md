# Central de Comando (`/painel/comando`) · conta Leandro, 09/11/2026

Pedido do Lindson (09/11): "quero montar um sistema único, integrado com todas as minhas contas, onde eu peça em um único lugar, visualize resultados, análises, com template de sistema, comandos por voz, visual tecnológico… botões para todas as funções que eu mais preciso."

No ar em **https://lindsonalmeida.pages.dev/painel/comando** (só o admin abre). Atalho em destaque no painel do admin (menu "Visão" e cartão na Visão geral) e em `dados/apps.json`.

## v4.1 (10/11/2026, conta Zuleide): cérebro gratuito
O Lindson: "não quero comprar mais nada, eu já assino o plano" (a assinatura do Claude não dá chave de API).
- **Cérebro principal: Workers AI da Cloudflare, plano gratuito** (10.000 neurônios por dia, zera às 00:00 UTC = 21h de São Luís). Modelo `@cf/google/gemma-4-26b-a4b-it` sem raciocínio (rápido, bom em pt-BR, ~40 neurônios por resposta, umas 250 falas por dia); se ele falhar, `@cf/meta/llama-3.3-70b-instruct-fp8-fast`. Quando a cota acaba, o VEKTOR avisa com educação e os comandos de voz da v3 continuam.
- **Claude opcional:** só é usado se um dia existir o segredo `ANTHROPIC_API_KEY`. A página não pede chave.
- **Ligar o binding (grátis, uma vez):** Workers e Pages → lindsonalmeida → Configurações → Vinculações → Adicionar → Workers AI → nome `AI` → Salvar. O próximo deploy (qualquer push no privado) já pega.
- **Por que não pelo `wrangler.toml`:** com o arquivo, ele vira a única fonte de configuração do projeto Pages, e o painel deixa de valer para KV, variáveis e data de compatibilidade. Como não dá para ver daqui os nomes exatos dessas configurações, um arquivo errado derrubaria o login de todos os clientes. O binding pelo painel não mexe em nada disso.
- **Conferir sem login:** `https://lindsonalmeida.pages.dev/api/vektor?saude` responde `{"ligado":true}` quando o cérebro está ligado (só sim ou não).
- O prompt ganhou regras de ouro (sempre pt-BR, sem lista falada) e exemplos do jeito dele, para o modelo menor soar natural.

## v4 (10/11/2026, conta Zuleide, Webdesigner): o VEKTOR conversa
Pedido do Lindson: "ele não conversa comigo"; "quero que entenda tudo que eu falo em português do Brasil e converse comigo… fluido, como uma pessoa real, o JARVIS do Homem de Ferro".
- **Cérebro:** `functions/api/vektor.js` (privado; cópia em `site/functions/api/`), só para o admin. Na v4 usava o Claude (trocado na v4.1) (`claude-opus-5-5`, esforço baixo, resposta em fluxo) com o segredo **`ANTHROPIC_API_KEY`** da Cloudflare. Plano B: Workers AI (binding `AI`). Sem nenhum dos dois, a página avisa o que ativar e volta aos comandos da v3.
- **Contexto:** fila e equipe ao vivo (KV) + placar, em andamento, últimas entregas, atividade e agenda do Instagram (`functions/_vektor_ctx.js`, gerado pelo `montar-comando.py`, sem imagens).
- **Conversa:** "Vektor" abre; depois, por 60 s desde a última fala dele, tudo vai para ele, sem repetir o nome. A frase fecha numa pausa de ~700 ms. Histórico (16 falas) e uma memória curta vão em cada chamada e ficam na sessão do navegador.
- **Fala frase por frase** conforme a resposta chega; "hum, deixa eu ver" se demorar; som curto do HUD ao pensar. Dá para **interromper** falando (o que bate com a fala dele é tratado como eco e descartado).
- **Pedidos:** ele resume e pergunta "posso mandar para a fila?"; com o sim (ou "enviar"/"pode mandar") a página cria o pedido pelo mesmo caminho do botão Enviar, com o aviso de "já existe". O servidor só aceita criar o pedido que estava pendente.
- **Tela:** balões discretos (VOCÊ / VEKTOR) no HUD, com o detalhe em letra pequena; no celular, o título some enquanto conversa.
- **Contas criam pedido:** `acao: "criar"` na `/api/automacao` (ver `PROTOCOLO-CONTAS.md`).
- **Preparado, ainda não ligado:** aviso no celular (`v4/app/`: service worker, manifesto e ícones, já copiados para `painel/comando/`). Foi para depois, por decisão do Lindson.
- **Voz:** a melhor voz pt-BR do navegador (no Edge, as vozes "Natural" são as melhores). TTS neural no servidor não sai de graça em pt-BR (os modelos de voz do Workers AI não falam português); com uma chave paga (ElevenLabs ou Azure) dá para criar `/api/voz`.
- Conferência: `v4/v4-desktop-1440-conversa.png`, `v4/v4-celular-390-conversa.png` (conversa simulada de 6 trocas, com o servidor de teste).

## v3 (09/11/2026, conta Leandro): o VEKTOR, que ouve sempre
- **Escuta automática:** ao abrir, pede o microfone uma vez e liga a voz contínua em pt-BR. Ela reinicia sozinha quando cai, pausa com a aba escondida e mostra o estado no topo e no núcleo: ouvindo, pausado, bloqueado (com o passo a passo) ou sem voz (pede Chrome ou Edge). Se o navegador exigir um toque, o primeiro toque em qualquer lugar liga a escuta.
- **Comandos:** "Vektor, reels da Jaci sobre clareamento" monta o pedido; "enviar", "manda" ou "pode mandar" no fim envia. Sem "Vektor", só navegação e envio.
- **Avatar:** holograma de partículas no centro, com anéis de HUD, dados em órbita, voz própria (liga e desliga) e fio de varredura entre as seções. Pesquisa e decisões no `TEMPLATE.md`; capturas e vídeo em `v3/`.

## v2 (09/11/2026, conta Leandro): estação de comando, lugar único
O Lindson disse: "não quero que pareça vibe code" e "quero abrir só essa página do sistema e nenhuma outra mais". A página virou uma rolagem só, com cinco seções:
1. **Comando:** vídeo real em loop, camadas com parallax, grão, HUD e botão físico de falar. Abaixo, o deck com os clientes e 16 teclas de equipamento.
2. **Fila ao vivo:** quadro de partidas, com o resultado **dentro da página** (galeria, player, PDF, prévia de site), as perguntas das contas com respostas rápidas ou por voz, e Aprovar / Ajuste.
3. **Resultados:** números gigantes, placar, aprovações dos clientes com miniaturas reais e botões Aprovar / Ajuste (gravam no `f=aprov` do cliente), vídeos com prévia ao passar o dedo, entregas e análise.
4. **Equipe:** um módulo por conta com o estado (trabalhando, livre, limite de hoje, limite da semana), quando volta, a barra até o reset, a carga, a última atividade e quantas vezes bateu cada limite no mês. O Lindson tem os botões "esgotou hoje até…", "esgotou a semana até…" e "liberar".
5. **Configurar contas:** o prompt de uma vez por conta e se a tarefa horária está ativa.

**Também na v2:**
- Contador "Esperando você" no topo, com som discreto que se desliga.
- Ferramentas (Recomeço 90 e Canais dark) abertas por dentro da página.

**Distribuição automática:** `functions/_distribuir.js` (privado; cópia em `site/functions/`). Regras e API em `PROTOCOLO-CONTAS.md`. O quadro da equipe fica em `dados:admin:eq` (`f=eq`, acrescentado ao `FERR` do `dados.js`).

**Arquivos da v2:**
- `v2/media/`: vídeo e pôster do hero; o montar copia para `painel/comando/media/` no privado.
- `v2/referencias/`: capturas da pesquisa.
- `v2/v2-*.png` e `v2/v2-rolagem-desktop.mp4`: conferência.
- `v2/CREDITOS.md`.

**O `montar-comando.py` agora também gera:**
- a última atividade de cada conta, pelos commits "(conta X)";
- as peças para aprovar, tiradas dos painéis (sem prova social);
- os vídeos entregues;
- o perfil de especialidade.

## Telas (v1)
| Tela | O que faz |
|---|---|
| **Comando** | Microfone gigante (voz em pt-BR no navegador, com campo de texto de reserva), chips de cliente (Jaci, Tribuna 98, Leo e Real Time marcados como pagantes; Orégano, Minha marca, Outro) e 16 botões de função. Toca no cliente e na função, fala ou escreve um detalhe e toca em **Enviar para a equipe**. Antes de mandar, mostra **"Já existe"** se o mesmo cliente e a mesma função têm pedido aberto ou pronto nos últimos 14 dias, e também entregas parecidas do `REGISTRO-DAS-CONTAS.md`. No celular, uma barra "Enviar" aparece em cima das abas quando o pedido está montado. |
| **Fila** | Pedidos com status **novo → com &lt;conta&gt; → pronto → aprovado / ajuste**; conta, datas, link do resultado, **Aprovar** e **Pedir ajuste** (fala ou escreve a nota; o pedido volta para a fila). Atualiza sozinha a cada 45 s. |
| **Resultados e análises** | Placar (barras por projeto), parado esperando o Lindson, aprovações dos clientes ao vivo (`f=aprov` de jaci, tribuna, leo, rt, oregano), pedidos por status, tempo médio até pronto, entregas por conta em 7 dias, o que cada conta está fazendo, últimas 15 entregas e a agenda do @lindsonalmeida_. Nenhum número é inventado: o que não tem dado mostra "—". |

**Voz** (exemplos): "Reels da Jaci sobre clareamento, enviar" (monta e envia) · "carrossel do Leo sobre 15 de novembro" (monta; ele toca em Enviar) · "status" (abre Resultados) · "fila" · "abrir painel do Leo" (vai para `/painel/leo`) · "aprovar Jaci" (abre as aprovações dela). Funciona no Chrome (Android e computador); no iPhone o Safari tem voz a partir do iOS 14.5; sem voz, o campo de texto faz o mesmo.

## Arquivos
- `comando.html`: a página (fonte). Sistema no visual do modelo da Central: menu lateral, cartões de números, `movimento.js`.
- `montar-comando.py`: lê PLACAR, REGISTRO, QUADRO ("Em andamento") e `agencia/marca-lindson/agenda-status.json`; gera no privado `painel/comando/estado.js` (`window.__ESTADO`) e `painel/comando.html`.
- `PROTOCOLO-CONTAS.md`: como as 4 contas leem e marcam a fila.
- `TEMPLATE.md` + `referencias/`: pesquisa premium (11 referências, 4 países).
- `captura-desktop-1440.png`, `captura-celular-390.png`: conferência (fila vazia, sem dado de cliente).

## Dados
- **Fila:** KV `dados:admin:ped`, formato `{dados:{itens:[{id, cli, func, texto, st, conta, link, criado, atualizado, nota, ajustes, prontoEm, notas}]}, versao}`. A página grava por `/api/dados?cli=admin&f=ped` (com versão; em 409 junta e tenta de novo). O `admin.html` não lê essa chave (ele lê o `f=ped` de cada cliente), então a aba atual não muda.
- **Contas:** `/api/automacao?fila=ped` com `Authorization: Bearer <AUTOMACAO_TOKEN>` (segredo da Cloudflare). Ver `PROTOCOLO-CONTAS.md`.

## Toda conta, ao terminar uma entrega
```bash
cd /home/user/lindson && python3 agencia/sistema-clientes/comando/montar-comando.py
cd /home/user/centrallindsonalmeida && git add painel/comando painel/comando.html && git commit -m "Comando: estado atualizado" && git push origin main
```
(Depois de registrar no REGISTRO e no PLACAR, para os Resultados mostrarem a entrega.)

## Proteção
`functions/painel/_middleware.js` (cópia em `site/functions/`): `admin`, `comando`, `contas` e `membros` só abrem para o admin, mesmo se um dia existir um cliente com esse nome. `/painel/comando/estado.js` também fica atrás do login de admin.

## Próximos passos (v4)
- Ligar o aviso no celular (arquivos prontos em `v4/app/`).
- TTS neural pt-BR em `/api/voz`, se o Lindson quiser pagar uma chave de voz.
