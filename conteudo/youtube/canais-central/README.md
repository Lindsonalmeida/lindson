# Canais dark dentro da Central (conta Leandro, 09/11/2026)

Pedido do Lindson (09/11/2026): "exclua os apps externos dos canais dark e converta eles para dentro da central pra eu não ter que abrir várias guias".

- **No ar:** https://lindsonalmeida.pages.dev/painel/canais (só o admin; `#passaporte` ou `#raposa` abre direto o canal).
- **Substitui** os apps de postagem do claude.ai: Passaporte https://claude.ai/artifact/CT3Z4M3yrzGrqCt3nh95ak (e o antigo 1aUURghpLqrWgTQmkvBcG4) e Raposa https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH (e o antigo LSTErmeSra3qxFKBJMLiTC). **Nenhum foi apagado:** a lista do que pode ser apagado está no fim de `MIGRACAO.md` e só vale com o OK do Lindson depois de conferir a Central.

## O que a página tem
Sistema da Central (menu lateral, topo, cartões, `movimento.js`), duas abas (Passaporte da Bíblia e Raposa e Leão) com a identidade de cada canal nos acentos (Passaporte: âmbar + ciano + Cinzel; Raposa: ouro + tarja vermelha + Anton). Em cada vídeo: título, legenda com capítulos, comentário fixado, capas A/B/C ou capa do Short com botão de baixar, player, duração, botões de copiar e "Marquei como postado".

- **Status de postado:** salvo no servidor em `/api/dados?cli=passaporte&f=aprov` e `cli=raposa&f=aprov` (`itens: [{titulo: <id do vídeo>, postado, postadoEm, postadoPor}]`). Os já publicados (Passaporte pv-01 e Shorts 01-10; Shorts 11-20 programados no Metricool; Raposa Shorts 01-10) começam marcados; o Lindson desmarca se precisar. Sem servidor (arquivo local), salva só no aparelho e o topo avisa.
- **Mídia:** capas em `painel/canais/<canal>/capas/` (JPEG ≤ 300 KB). Vídeo migrado toca da Central; o que ainda não veio mostra a capa com o selo "Arquivo ainda no app antigo" e o botão para abrir o app.

## Gerar de novo
```
python3 conteudo/youtube/canais-central/montar-canais.py --manifesto /tmp/faltam.json   # o que falta baixar dos apps
# baixe cada asset com o Artifact tool (action read, url = app, path = id); os arquivos caem em <scratchpad>/artifact-files/
python3 conteudo/youtube/canais-central/montar-canais.py --cache <scratchpad>/artifact-files   # monta a página, as capas e o MIGRACAO.md
```
Depois: commit e push no privado (`painel/canais.html`, `painel/canais/`). Lê os mesmos dados dos geradores antigos (`passaporte/pintura.json`, `tempos.json`, `ativos*.json`; `raposa-e-leao/shorts|longos/NN/publicar*.json`, `tempos.json`, `ativos*.json`). Vídeo novo: suba o arquivo no app atual ou ponha o mp4 (≤ 20 MB) em `painel/canais/<canal>/videos/<id>.mp4` no privado e rode de novo.

**Vídeos (decisão pendente do Lindson):** os vídeos ainda não postados somam ~506 MB, acima do limite combinado de 300 MB para o repositório. Por isso nenhum vídeo foi copiado; continuam tocando no app antigo. Para trazer mesmo assim: baixe-os e rode com `--videos`. Alternativa sem inchar o repositório: guardar os vídeos fora do Git (R2 da Cloudflare) e só apontar o link aqui.

## Atalhos
- `dados/apps.json` (privado), aba "Canais dark": cartão **Canais dark** → `/painel/canais`, e os dois canais apontam para `/painel/canais#passaporte` e `#raposa`. Aparece no admin quando o `montar-site.py` rodar de novo.
- **Central de Comando:** o link `/painel/canais` entra na Central de Comando (`/painel/comando`, ferramenta "Canais dark"). Não editei `admin.html` nem `comando.html` porque estavam sendo refeitos por outro agente nesta hora; quem mexer neles, aponte "Canais dark" para `/painel/canais`.

## Arquivos
- `canais.html`: a página (modelo); `montar-canais.py`: o gerador; `MIGRACAO.md`: cada arquivo, migrado ou no link antigo.
- Capturas: `captura-desktop-1440.png`, `captura-desktop-raposa-1440.png`, `captura-celular-390.png` (teste em cópia `file://`).
