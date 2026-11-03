# Mapa do repositório: o que já existe e onde

Leia antes de criar qualquer coisa: se já existe aqui, continue a partir disso (regra do `CLAUDE.md`, "Trabalho em equipe"). Montado pela conta Lindson em 01/11/2026. Quem criar pasta, app ou processo novo acrescenta aqui.

Branch principal: `claude/global-agent-installation-vdyowf`. Outros branches: `entregas-videos` (vídeos e capas prontos dos canais dark, para o app) e `claude/padrao-estrategia-completa` (antigo, primeiras versões da identidade do Leo Pinto; o conteúdo atual está no principal).

## Arquivos da raiz
| Arquivo | Para quê |
|---|---|
| `CLAUDE.md` | Regras de trabalho de todas as contas |
| `PROMPT-DA-EQUIPE.md` | Prompt para colar no começo de qualquer conversa: quem é quem, o que buscar no repositório e o que as contas já sabem |
| `MEMORIA-DO-LINDSON.md` | **Leia primeiro:** tudo o que o Lindson pediu, aprovou (guardar e melhorar) e reprovou (nunca repetir), regras por cliente, pedidos já feitos e pendências. Toda conta atualiza ao fim de cada pedido |
| `QUADRO-DA-EQUIPE.md` | O que cada conta está fazendo agora e o que está livre |
| `REGISTRO-DAS-CONTAS.md` | Tudo o que já foi entregue, por conta e data |
| `ESTADO-DO-PROJETO.md` | Apps publicados, filas de vídeo e como retomar uma renderização |
| `MINI-SITE.md`, `links/` | Mini site de links da bio do Lindson |
| `README.md`, `instalar-xquads.*`, `instalar-builder-squad.*`, `ferramentas/` | Instaladores globais dos agentes Xquads e do Builder Squad; `ferramentas/nano_banana.py` gera e edita imagens com o Nano Banana (precisa de GEMINI_API_KEY no ambiente) |

## Agência (`agencia/`)
| Pasta / arquivo | O que tem |
|---|---|
| `ofertas/` | Esteira de produtos (5 degraus até R$ 3.500), oferta Instagram que Vende: 90 Dias, **produto master** (curso + mentoria para donos de negócio), dores e desejos do público (com versão negativa), pesquisa das autoridades do nicho |
| `prospeccao/` | Padrão de copy (Conexão → Dor → Desejo → Pergunta), padrão de entrega, rotina da lista diária de leads |
| `processos/` | Mini site de cliente, demo de mini site (vídeo de iPhone), modelo de contrato, modelo de estratégia completa (19 páginas), proposta curta (8 páginas) |
| `app/` | Fontes dos apps **Recomeço 90** (`recomeco90.html`) e **Fábrica de Conteúdo** (`fabrica.html`) |
| `clientes/` | Dra. Jaci Cunha (ficha, contrato, estratégia premium e manual de identidade, estilo das artes do Instagram `jaci-cunha/instagram-estilo/`), Leo Pinto (identidades v2 e v3, feed do Instagram aprovado v12, apresentação em painel v13 `instagram-v13-apresentacao/` (padrão aprovado), datas comemorativas v14 `instagram-v14-datas/`, foto de perfil `instagram-perfil/`, prompt do Claude Design; desde 02/11 identidade só com fontes, logo e cores), Katje Garcez (falas) |
| `sistema-clientes/` | Central do Cliente: ideias, protótipo do login e do painel (modelo para novos clientes), painéis do Leo Pinto e da Dra. Jaci (`jaci-cunha/`), site publicável com login no servidor (`site/`, publicar num repositório privado) |
| `indicacao/` | Banner do programa de indicação |
| `identidade-oferta.md` | Identidade dos posts de oferta (estilo lançamento) |
| `contratos/`, `propostas/` | Dados pessoais e de clientes: **fora do GitHub** (peça ao Lindson) |

## Marca do Lindson (`branding/`)
Brand book, componentes (Cover, LinkCard, StatStrip…), modelos e guia de Instagram (`instagram.md`).

## Conteúdo (`conteudo/`)
| Pasta / arquivo | O que tem |
|---|---|
| `esteira/` | **Esteira de Reels, Teste 01**: 300 roteiros de 30 s (3 formatos × 10 conteúdos × 10 ganchos), já no app Recomeço 90. Regras em `ROTINA.md`; gerador `montar.py` |
| `formatos-que-engajam.md` | Os 10 formatos que mais engajam, com dados de 2026 |
| `identidade-01/` | 4 carrosséis da identidade 01 |
| `avaliacao-gratuita/` | Campanha Avaliação Gratuita (10 conteúdos) e o **modelo de legenda SEO** |
| `reels/` | Reels de tráfego v1, v2 e v3 (motion design) e roteiros "5 erros" |
| `top-x/` | Quadro Top X: pesquisa de virais e legendas |
| `criativos-vendas/`, `ensaio-mini-site/`, `fotos/` | Criativos de venda, ensaio do mini site, registro de fotos |
| `noticias/` | Perfil de notícias BOMBOU (identidade, padrão de foto, gerador de arte) |
| `referencias/` | Engenharia reversa do Behance, ensinamentos de Maquiavel (248) e acervo completo em `referencias/maquiavel/` (comece por `INDICE-POR-SITUACAO.md`; `ensinamentos-complementares.md` 249–641; revisão em `REVISAO.md` e `revisao/`, com testes do agente em `revisao/testes-v3/`; obras, fichas dos *Discursos* `discursos-fichas-livro-1/2/3.md`, `REVISAO.md`, `TESTES.md`, memória de decisões `CONSELHOS.md`; agente `.claude/agents/maquiavel.md`); `referencias/dinheiro-online/` |
| `youtube/passaporte/` | Canal **Passaporte da Bíblia**: identidade, processo, pesquisas, roteiros, motor Pintura Viva (`motor/pintura.py`), capas (`motor/capas2.py` + `capas_v2.json`) |
| `youtube/raposa-e-leao/` | Canal **Raposa e Leão** (Maquiavel): identidade, processo, 30 Shorts, longos, roteiros, acervo de imagens |
| `youtube/comum/` | Voz humanizada |
| `youtube/filas/` | Filas de renderização e instruções para refazer os longos |
| `youtube/pesquisa/`, `youtube/biblia/` | Top 5 canais dark, referência do canal da Bíblia |

## Agentes
| Agente | Onde | Quando |
|---|---|---|
| Peter | `.claude/agents/peter.md` | Canal dark e monetização no YouTube |
| Xquads (15 squads, 183 agentes) | instalados por `instalar-xquads.sh` | Oferta, copy, tráfego, marca etc. |
| `agencia/clientes/desentupidora-sf/` e `agencia/sistema-clientes/desentupidora-sf/` | Desentupidora SF: artes do Instagram (`instagram-v1/`) e painel da Central (`montar-sf.py`) | (conta Zuleide, 03/11) |
| `agencia/clientes/rt-full-jobs/` | cliente novo RT Full Jobs: prints e resumo do briefing | (conta Zuleide, 03/11) |
| `AGENTES.md` | lista de todos os 201 agentes por categoria (nossos, Xquads, Builder Squad) e qual chamar para cada pedido | (conta Zuleide, 03/11) |

## Apps publicados por conta
Todos reunidos, com os antigos e repetidos marcados, no painel do administrador da Central (https://lindsonalmeida.pages.dev/painel/admin). A lista fica em `CentralLindsonALmeida/dados/apps.json`.

Cada app é privado da conta que criou. Para editar de outra conta, peça ao dono para compartilhar com edição (entre organizações diferentes, nem assim dá para publicar).

**Conta Lindson:** Recomeço 90 https://claude.ai/artifact/DQFTjzVzhH2ZaHtFQwXw5N · Fábrica de Conteúdo https://claude.ai/artifact/WxeZuhrzQutLDTJ36y6EVt · Downloads Lindson https://claude.ai/artifact/VLijrTZyfqg1D53UYrKM6w · Legendas Top X https://claude.ai/artifact/PHe4b5buViTfSGqQzBc2XT · Brand Book https://claude.ai/artifact/L1959UErxHBmmtqe7gwKBS · Design System https://claude.ai/artifact/G4tLQ1bQj4JWnLiFU615oU · Gerador de propostas https://claude.ai/artifact/UV4P5h6vJS1kxVgKnXP2rB

**Conta Pedro:** Passaporte (app único) https://claude.ai/artifact/CT3Z4M3yrzGrqCt3nh95ak · Raposa e Leão (app único) https://claude.ai/artifact/2k4SSuvALdqXDcXnBQMVZH · Painel do Leo Pinto https://claude.ai/artifact/7TjjwEUN5jASCbytXAvhHk

**Outros apps citados no `ESTADO-DO-PROJETO.md`** (Downloads Alkantara, SDR para Agências, Minhas 3 Prioridades, Contratos Alkantara, Postagens antigas do Passaporte e do Raposa, Central do cliente): dono não confirmado; não aparecem na lista de apps da conta Lindson.

## Tarefas agendadas (conta Lindson)
Todas desligadas desde 26/10 (as de 3 em 3 horas falharam por limite de uso do plano). Para religar, peça ao Lindson.
| Nome | Quando | Situação |
|---|---|---|
| Lista diária de leads (100 com WhatsApp) | todo dia 6h26 (São Luís) | desligada desde 26/10; última rodada boa em 26/10 |
| Captação por cidades | a cada 3 h | desligada desde 26/10 (falhou por limite de uso) |
| Notícias BOMBOU | a cada 3 h | desligada desde 26/10 (falhou por limite de uso em 27/10) |
| Roteiros diários de Reels | 5h41 | desligada de propósito (os 300 roteiros foram entregues de uma vez em 22/10) |

- `conteudo/referencias/ia-video-voz/`: pesquisa de clone de imagem e voz (HeyGen, ElevenLabs, outras ferramentas) e plano do nosso app interno (conta Pedro, 03/11/2026).
- `agencia/clientes/rt-full-jobs/identidade/v1/`: identidade e manual de marca da Real Time (premium) (conta Pedro, 03/11/2026).
- `apps/clone-studio/`: **Dublê**, app interno de clone de voz e imagem do Lindson (identidade em `identidade/`, tela v2 em `web/` copiada do template Sermo; stories e vídeo de divulgação em `divulgacao/`) (Gradio, roda no notebook dele; dados fora do Git) (conta Pedro, 03/11/2026).
