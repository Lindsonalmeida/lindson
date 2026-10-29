# Instruções do repositório (Lindson Almeida)

## Mini site de cliente (bio)

Sempre que o Lindson pedir um mini site / site bio para um cliente, **antes de começar**, lembre a ele o passo a passo de `agencia/processos/mini-site-cliente.md` e siga-o:

1. Cada cliente tem **o próprio repositório** na conta `Lindsonalmeida` (nome do cliente, sem espaço nem acento, privado). Peça para ele criar o repositório vazio e liberar o acesso do app Claude (All repositories).
2. O site fica no repositório do cliente, **nunca** dentro deste repositório `lindson` (o link não pode ter o nome Lindson).
3. Publicação pela **Cloudflare Pages**: Workers e Pages → Criar → Pages → Importar repositório → Project name = nome do cliente, branch `main`, framework `None`, build vazio. Link final: `nomedocliente.pages.dev`.
4. Links internos absolutos (prévia do WhatsApp, cards) usam o endereço `pages.dev` do cliente.
5. Fotos: pedir uma por mensagem (imagens enviadas no meio de uma resposta não ficam salvas). Nunca usar ilustração no lugar de foto real de produto.
6. Depois de publicar, atualizar a tabela "Clientes ativos" no fim de `agencia/processos/mini-site-cliente.md`.

Clientes ativos hoje: Rafael Imports → `Lindsonalmeida/rafaelimports` → https://rafaelimports.pages.dev · Desentupidora SF → `Lindsonalmeida/GruposSF` → https://desentupidorasf.pages.dev

## Demo de mini site para vender

Lead escolhido pelo Lindson: montar um protótipo do mini site na identidade da pessoa e entregar só o **vídeo de demonstração** em tela de iPhone (sem publicar). Processo e gravador em `agencia/processos/demo-minisite/` (README). O site completo só depois que fechar.

## Copy de vendas (padrão aprovado)

Legendas de post: sempre estilo blog SEO (título com palavra-chave, introdução, subtítulos, exemplo, conclusão, chamada e 3 a 5 hashtags pesquisadas e variadas — tema + nicho + local, nunca o mesmo bloco; até 2.200 caracteres) — modelo em `conteudo/avaliacao-gratuita/LEGENDAS.md`.

Carrosséis: depois da capa, nenhuma tela repete o layout da anterior. Variar composição dentro da identidade (número grande, número de fundo, cor invertida, cartão, problema × solução, faixas, frase de impacto).

Posts estáticos: nunca dois seguidos na mesma composição nem na mesma cor. Alternar entre foto inclinada, celular, palavra gigante, manchete, foto dividida, checklist, conversa e selo — sempre na identidade.

Lead que respondeu "pode mostrar": entregar a **estratégia completa** em PDF (19 páginas 4:5) na identidade visual DO CLIENTE, seguindo `agencia/processos/modelo-estrategia/README.md`: passo a passo técnico, linhas editoriais, campanhas de tráfego, WhatsApp, calendário de 90 dias e relatório. Sem preços nem planos (valores só na conversa) e sem inventar números. Usar os agentes Xquads (Hormozi Offers, Pedro Sobral, Donald Miller). Versão curta de 8 páginas: `agencia/processos/proposta-cliente.md`.

Toda mensagem de abordagem e copy curta de venda segue `agencia/prospeccao/PADRAO-COPY.md`: **Conexão → Dor → Desejo → Pergunta**, linguagem simples de WhatsApp, entendida numa única leitura. Nunca usar "vi que", "parece que", "gargalo", jargão de marketing ou análise do perfil da pessoa.

## Apps de prospecção e SDR

Todo app de prospecção/SDR (e funil de clientes) tem, em cada contato, um botão **WhatsApp** que abre a conversa do lead já com a mensagem da etapa escrita (link `wa.me/55<número>?text=<mensagem>`), sem copiar e colar. Ao clicar, o app registra sozinho o envio e avança a etapa/cadência. O botão fica visível na ficha fechada, sem precisar abrir. Sem número de WhatsApp, o botão copia a mensagem. O objetivo é o Lindson não fazer nada manual além de tocar em "enviar". Só entram na fila de contato leads com **WhatsApp (celular) e Instagram**; quem não tiver os dois fica fora (sem botão, não manda). Ao buscar leads, trazer só quem tem os dois confirmados.

## Contratos

Pedido de contrato de cliente: usar o modelo `agencia/processos/modelo-contrato/` (README explica). Dados do Lindson em `agencia/contratos/meus-dados.json` e do cliente em `agencia/contratos/<cliente>/dados.json`, ambos fora do GitHub. Se faltarem, pedir. Entregar PDF A4.

## Entrega de PDFs

Todo PDF entregue (estratégia, contrato, planos) também entra na página de downloads com botão de baixar: https://claude.ai/artifact/3Vn9qpHt3iXgG2JAhcubs7

## Como trabalhar

Sempre que o Lindson pedir algo, acione os agentes especialistas (Xquads em `scratchpad/xq/src`: Hormozi Offers, Donald Miller, Pedro Sobral, copy-squad, brand-squad etc., e agentes de pesquisa na internet) para fazer o trabalho, escolhendo os melhores para cada pedido.

Para canal dark e monetização no YouTube (Passaporte da Bíblia, Raposa e Leão, nichos novos), acionar o agente **Peter** (`.claude/agents/peter.md`).

## Estado atual e continuidade

Antes de continuar qualquer trabalho (de qualquer conta), leia `ESTADO-DO-PROJETO.md`: links dos apps, o que está pronto, o que falta e como retomar.
