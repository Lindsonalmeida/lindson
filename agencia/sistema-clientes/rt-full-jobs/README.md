# Painel da Real Time na Central (conta Leandro, 03/11/2026)

**Endereço:** https://lindsonalmeida.pages.dev/painel/rt (o cliente cria a conta na tela inicial com o código de acesso).

Pedido do Lindson (03/11): "suba o painel do cliente e todos esses conteúdos lá".

**O que tem:** o sistema da Central (menu lateral, cartões, animações) com a **marca nova v1** da Real Time (Preto Set, Azul Real, REC vermelho, Geist + Geist Mono, assinatura realtime).
- **Aprovações (10):** bio nova + 6 destaques (prévia do perfil), 7 posts do feed v1 com a legenda SEO de cada um, 2 stories com a figurinha. Prévia do feed na ordem de postagem. Ficam de fora o post 05 e o story 03 (depoimento): só com fala real de cliente.
- **Entregas e arquivos** com botão **Baixar**: manual de marca com rebranding (21 p.), logo em SVG (zip), estratégia de vendas v2 (19 p.), capas dos destaques + bio (zip). Os arquivos ficam no privado em `painel/rt/arquivos/` (só quem entrou como Real Time ou o admin abre). Os PDFs do painel são a versão leve (páginas em imagem, ~2 MB), porque a Cloudflare aceita no máximo 25 MB por arquivo.
- **Calendário de novembro:** os 7 posts às segundas, quartas e sextas (9 a 23/11).
- **Gestão:** CRM de reservas (Novo contato → Orçamento enviado → Reserva confirmada → Em uso → Job concluído → Cliente recorrente, e "Não fechou"), com WhatsApp pronto em cada etapa e origens pelos códigos dos anúncios (RT-CINEMA, RT-LUZ, RT-ESTUDIO, RT-MENSAL, RT-PROD); Financeiro; Notícias do setor (audiovisual no Maranhão, editais, equipamentos, publicidade, videocast, filmmaking).

**Gerar e publicar:**
```bash
cd agencia/sistema-clientes
python3 rt-full-jobs/montar-rt.py     # lê CentralLindsonALmeida/dados/rt.json (privado)
python3 site/montar-site.py           # gera site/publico/ (fora do Git)
# copie publico/painel/rt.html (e admin.html, contas.html se mudaram) para o privado e faça push: a Cloudflare publica sozinha
```
`painel-rt.html` fica fora do Git. Atenção: no ambiente da nuvem, os painéis da Jaci e do Leo e a tela inicial saem diferentes dos que estão no ar (faltam fotos fora do Git): **não copie esses** por cima dos do privado.

**Código de acesso:** `site/novo-codigo.py rt RTJ`; só o hash está em `CentralLindsonALmeida/functions/_codigos.js`. O código foi entregue ao Lindson na conversa.
