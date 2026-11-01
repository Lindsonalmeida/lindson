# Demo de mini site para vender (vídeo "já fiz o seu")

Método de venda: o Lindson escolhe o lead e manda o link dos vídeos/perfil. Eu monto um **protótipo** do mini site na identidade da pessoa (local, sem publicar e sem repositório) e gravo só o **vídeo de demonstração** em tela de iPhone. O site completo só é feito depois que o cliente fechar (processo em `../mini-site-cliente.md`).

## Passo a passo
1. Receber do Lindson: @ do Instagram ou prints do perfil, links dos vídeos, o que o negócio vende e o WhatsApp.
2. Baixar os vídeos dos links. Se a plataforma bloquear o download, pedir o arquivo do vídeo direto (um por mensagem). Não contornar bloqueio de site.
3. Criar o protótipo em `agencia/demos/<cliente>/index.html` na identidade da pessoa (cores, letras, logo, fotos reais), com os botões que o negócio precisa (WhatsApp por setor, catálogo, localização, agenda etc.).
4. Escrever o roteiro `<cliente>.json` (URL `file://` do protótipo + toques e rolagens) e rodar `python3 montar.py <cliente>.json agencia/demos/minisite-<cliente>.mp4`.
5. Enviar o vídeo ao Lindson e ajustar pelo retorno.

Endereço que aparece na barra do Safari: `<cliente>.pages.dev` (como ficará quando publicado).

## Retorno do Lindson
- Santa Beleza (1º teste): "ficou perfeito". A partir do próximo: **design mais premium** (mais sofisticação visual: tipografia de revista, mais respiro, fotos em destaque, detalhes dourados/foil ou texturas da marca, transições mais elegantes).
- Leads de venda de mini site ficam na lista "Mini site · Estética" do app de SDR. O botão de WhatsApp só aparece depois que o vídeo está marcado como pronto.

## Mensagem que o Lindson usou (Santa Beleza, aprovada)
1. "Criamos um mini site para a bio do Instagram, com a identidade de vocês, pronto só para atender os clientes e qualificar no atendimento"
2. "Estou enviando um vídeo para vocês verem como ficou este mini site" + vídeo com a legenda "Olha só que perfeição"
3. "A cliente consegue ter uma percepção total, além de falar com um chat que vai perguntar sobre as dores dela e já chega no whats de vocês com tudo que a cliente quer"
É a mensagem A da lista "Mini site · Estética" no app de SDR.

## Tutorial narrado do sistema do cliente (conta Lindson, 01/11/2026)
- **Comando:** `python3 tutorial.py tutorial-<cliente>.json <saida.mp4>`.
- **O que sai:** tela de iPhone com dedo e toques, legenda em cada passo e a **voz humanizada** dos canais (`conteudo/youtube/comum/voz_humana.py`). Cada passo dura pelo menos o tempo da fala, com música baixa por baixo.
- **Ações novas no roteiro:**
  - `legenda` e `ate` (segundos desde a legenda);
  - `clicar` (seletor CSS);
  - `digitar` (seletor + texto);
  - `js`.
- **Códigos de acesso nunca entram no roteiro:** use `{CODIGO:jaci}`. O `tutorial.py` lê o código de `agencia/sistema-clientes/privado/codigos-acesso.json`, e no vídeo ele aparece mascarado.
- **Como gravar a Central:** com o site rodando local (`npx wrangler@3 pages dev publico --kv CONTAS` em `agencia/sistema-clientes/site`).
- **Entregues em 01/11:** `tutorial-jaci.json` e `tutorial-leo.json`. Os vídeos estão em `agencia/demos/tutoriais/` (fora do Git).
