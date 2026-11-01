# Refazer os longos curtos (pedido do Lindson, 31/10)

Pedido do Lindson (dono da conta), repassado pela sessão coordenadora session_01XiFncet69pmvqfriyq8wAJ: "quero todos os vídeos longos feitos e no app dos dois canais; tem vídeo longo de 5 minutos, isso nunca existiu; consulte o agente Peter para entender as regras e refaça tudo, com agilidade". Trabalhe sozinho, sem perguntas.

SUA TAREFA: refazer UM vídeo longo: o vídeo indicado na mensagem que abriu a sua sessão (veja a tabela abaixo).
O que fazer com ele está na tabela "Vídeos" abaixo.

REGRAS DO PETER (obrigatórias; leia também .claude/agents/peter.md e o BRIEF do canal):
- Longo = 16 a 20 min = 2.400 a 2.900 palavras de narração (~150 ppm), 15 a 45 palavras por cena, ~85 a 100 cenas. Nunca abaixo de 2.250 palavras.
- Gancho nos primeiros 7 s; 2 ou 3 loops abertos e fechados explicitamente (o maior no fim); quebra de padrão a cada 1-2 min; 6 a 9 capítulos; citações com referência (versículo ou capítulo de O Príncipe); chamada da isca por volta de 40%; convite ao próximo vídeo no fim.
- Conversa com o ouvinte: Passaporte 4 a 6 momentos, Raposa 3 a 5, cada fala única deste vídeo e ligada à lição (campo "interage", como nos roteiros novos).
- Sem conteúdo inautêntico: não copie estrutura/frases de outro longo; varie abertura, ordem dos blocos e trilha; ponto de vista claro; linguagem simples de WhatsApp; sem inventar números ou fatos.
- Capas A e B claras, até 3 palavras, figura forte, sem vermelho. Título de 5 a 8 palavras com palavra-chave.

COMO FAZER (siga o repositório; leia ESTADO-DO-PROJETO.md seção "Sessão de 31/10", o PROCESSO.md e o BRIEF.md do canal, e use como modelo os roteiros novos que já estão na regra: Passaporte conteudo/youtube/passaporte/roteiros/longo-05..09.json; Raposa conteudo/youtube/raposa-e-leao/roteiros/longo-12..16.json):
1. Ambiente (o motor usa caminhos fixos; crie links, não edite código): S=<seu scratchpad>; mkdir -p $S/old-scratch/modelos /tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b && ln -sfn $S/old-scratch /tmp/claude-0/-home-user/5acf6937-9ac6-56e0-bc29-78bef210dc8b/scratchpad; ligue o clone em /home/user/lindson se estiver noutro caminho; pip install edge-tts soundfile scipy onnxruntime opencv-python-headless; curl -sSfL -o $S/old-scratch/modelos/depth.onnx https://huggingface.co/inference4j/depth-anything-v2-small/resolve/main/model.onnx. Passaporte: gravuras de Doré de https://www.gutenberg.org/cache/epub/8710/pg8710-h.zip (images/[0-9]*.jpg → conteudo/youtube/passaporte/dore/, conferir dore/MAPA.md). Raposa: imagens do acervo com raposa-e-leao/motor/acervo_faltantes.py / acervo.py (Wikimedia limita: espere e repita) e img/acervo/MAPA.md. Se capas_pv.py reclamar do módulo "icones", crie um icones.py no PYTHONPATH com icone(caminho) que baixa https://raw.githubusercontent.com/microsoft/fluentui-emoji/main/<caminho> e devolve data URI.
2. Roteiro: escreva o roteiro novo em roteiros/<id>.json no MESMO formato dos roteiros novos do canal (use os agentes especialistas/Peter se ajudar). Mantenha o tema e o título (ajuste o título para 5-8 palavras se precisar). Conte as palavras e confirme 2.400-2.900. Guarde o original se for substituir algo (prova de trabalho humano). Gere a entrada no pintura.json do canal pelo script do canal (Passaporte: motor/lote3.py — inclua o id na lista dele se não estiver; Raposa: motor/lote_rl.py — idem) e rode a conversa se o processo mandar. Commit e push do roteiro e dos scripts no branch claude/global-agent-installation-vdyowf (git pull --rebase antes; nunca force). Não faça commit de vídeos nem imagens.
3. Render DESACOPLADO (tarefas em segundo plano morrem em 2 h): cd conteudo/youtube/passaporte/motor && RETOMAR=1 setsid nohup python3 pintura.py <pintura.json do canal> <id> > $S/render.log 2>&1 < /dev/null & . Acompanhe com um until em segundo plano até existir o mp4 final; se o processo parar, relance com RETOMAR=1. Leva ~1h30.
4. Versão do app (≤20 MB, 720p, dois passos): d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 <video>.mp4); br=$(python3 -c "print(int(19*8*1024/$d-90))"); ffmpeg passo 1 e 2 como em conteudo/youtube/filas/lote7.sh → <id>-app.mp4.
5. Capas A e B claras: Passaporte motor/capas_pv.py; Raposa o gerador de capas do canal (veja PROCESSO.md e capas_v2.json). Gere só as deste vídeo se possível.
6. ENTREGA (não publique nem republique nenhum app): faça commit SÓ do <id>-app.mp4 e das 2 capas no branch entregas-videos (git fetch origin entregas-videos; se existir, git checkout -B entregas-videos origin/entregas-videos, senão crie a partir do seu HEAD), na pasta entregas/<canal>/; git pull --rebase origin entregas-videos e git push origin entregas-videos (sem -f; repita até 4 vezes). Volte ao branch principal depois.
7. Ao terminar, mande para a sessão coordenadora (send_message, session_id session_01XiFncet69pmvqfriyq8wAJ) uma linha: ENTREGUE <canal> <id> <duração m:ss> <palavras> entregas/<canal>/<arquivos> e o título/legenda novos (com capítulos) em texto. Se falhar, mande FALHOU <id> <motivo>.

## Vídeos (inventário do Peter, 31/10)
| Canal | id | Palavras hoje | Ação |
|---|---|---|---|
| passaporte | longo-01 | 1.960 | estender: +1-2 capítulos, loops e conversa, para 2.400-2.900 |
| passaporte | longo-02 | 1.799 | estender: +1-2 capítulos, loops e conversa |
| passaporte | longo-03 | 1.489 | refazer no formato de cenas do BRIEF aproveitando o texto + 3-4 capítulos |
| passaporte | longo-04 | 1.283 | refazer no formato de cenas do BRIEF aproveitando o texto + 3-4 capítulos |
| raposa | longo-01 | 1.479 | passar do formato antigo (longos/01/roteiro.json, seg/tela) para roteiros/longo-01.json no formato novo + 3-4 capítulos |
| raposa | longo-02 a longo-05 | 1.258-1.357 | idem (cada sessão faz um) |
| raposa | longo-06 | 1.745 | idem, +1-2 capítulos |
| raposa | longo-07 a longo-11 | 816-878 | REESCREVER do zero pelo BRIEF (só fica tema e título), ~2.700 palavras, ~90 cenas |

Passaporte 05-09 e Raposa 12-16 já estão na regra (só renderizar). No Raposa, os ids novos ficam em roteiros/longo-NN.json (formato dos 12-16) e são renderizados pelo pintura.py com canal raposa; o antigo longos/NN/ fica como histórico.
