# Auditoria dos clientes na Central · 10/11/2026 (conta Leandro)

Pedido do Lindson: "verifique se tudo dos clientes está correto, tem coisa errada lá" e "os conteúdos dos clientes estão trocados".

| Cliente | O que estava errado | O que foi corrigido | Depende do Lindson |
|---|---|---|---|
| Todos (Central de Comando) | O filtro de "prova social/TCLE" do `montar-comando.py` lia também o base64 das imagens; letras sorteadas ("tcle", "prova") sumiam com peças de outros clientes, e a lista ficava desencontrada do painel. Peças em si não estavam trocadas: APROV e KV de cada cliente só têm peças dele (conferido um a um). | Filtro só no título e no caminho da imagem; agora a Central mostra as mesmas peças do painel de cada cliente (Leo 26 → todas, Real Time 30 → todas). | — |
| Dra. Jaci | 5 legendas (Black Friday e os 4 carrosséis de novembro) sem "Resultados variam" e sem CRO-MA 8514. A contagem "34 peças" era a lista toda; no KV só 1 está aguardando (Black Friday). | Assinatura com "Resultados variam" e CRO-MA 8514 posta em `instagram-nov/textos.json` e no painel. | Aprovar a Black Friday e definir a condição até 18/11; TCLE da prova social. |
| Tribuna 98 | Placar em 13% sem o que ele fez em 09/11. | Placar 38%: site principal, bio site, capas dos Reels e fotos do perfil (feito pelo Lindson). Painel sem peças para aprovar. | Qual Instagram reformular; fotos dos sócios; Insights. |
| Leo Pinto | KV guarda uma versão antiga "Quem conhece o seu bairro?" (não aparece em lugar nenhum; a peça atual é "povoado"). | Nada a mudar na tela; legendas atuais sem "bairro". | Aprovar Natal e Ano Novo (revisado), em ajuste. |
| Real Time | Placar dizia "cliente aprovar no painel", mas tudo já está aprovado no KV. | Placar 43%: aprovado e duas semanas agendadas pelo Lindson. | Contrato e preços; cidade e fotos. |
| Desentupidora SF | Não existia nas aprovações da Central nem no distribuidor; o painel `/painel/sf` tem 4 artes. | SF entrou nas aprovações, no VEKTOR ("Desentupidora SF tem painel") e nas palavras do distribuidor; placar atualizado com a campanha que ele fez em 09/11. | Aprovar as 4 artes; Google e Pixel. |
| Orégano Turbo | Preços conferidos: só Raio-X R$ 297 (aprovado); os outros valores são "exemplo ilustrativo", sem promessa. | Placar: Instagram criado pelo Lindson em 09/11. | Capa de destaque Zap em ajuste; INPI. |
| Tarefas feitas (09/11) | A semente das 10 tarefas só conferia o marcador "semente-0911"; se o marcador existisse com itens faltando (o teste simulado tinha só 2), ficava "Ontem: 1 tarefa". Sem rota para ler o KV das feitas. | A semente agora repõe item por item (Tribuna 4, Orégano 2, Real Time 1, SF 3). `GET /api/automacao?fila=feitas` para conferir. | — |

Sites: drajacicunha, tribuna98, realtimeslz e desentupidorasf .pages.dev abrem com 200. Bateria do VEKTOR: 51/51, console 0.
