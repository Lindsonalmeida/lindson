# Demo de mini site para vender (vídeo "já fiz o seu")

Método de venda: o Lindson escolhe o lead e manda o link dos vídeos/perfil. Eu monto um **protótipo** do mini site na identidade da pessoa (local, sem publicar e sem repositório) e gravo só o **vídeo de demonstração** em tela de iPhone. O site completo só é feito depois que o cliente fechar (processo em `../mini-site-cliente.md`).

## Passo a passo
1. Receber do Lindson: @ do Instagram ou prints do perfil, links dos vídeos, o que o negócio vende e o WhatsApp.
2. Baixar os vídeos dos links. Se a plataforma bloquear o download, pedir o arquivo do vídeo direto (um por mensagem). Não contornar bloqueio de site.
3. Criar o protótipo em `agencia/demos/<cliente>/index.html` na identidade da pessoa (cores, letras, logo, fotos reais), com os botões que o negócio precisa (WhatsApp por setor, catálogo, localização, agenda etc.).
4. Escrever o roteiro `<cliente>.json` (URL `file://` do protótipo + toques e rolagens) e rodar `python3 montar.py <cliente>.json agencia/demos/minisite-<cliente>.mp4`.
5. Enviar o vídeo ao Lindson e ajustar pelo retorno.

Endereço que aparece na barra do Safari: `<cliente>.pages.dev` (como ficará quando publicado).
